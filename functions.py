# -*- coding: UTF-8 -*-

from hip2unicode.conversions import hip2cslav
import re

eols = {

    'unix'  :   u'\n',
    'linux' :   u'\n',

    'dos'   :   u'\r\n',
    'win'   :   u'\r\n',

    'mac'   :   u'\r',
}

eols_re = {

    'unix'  :   ur'\n',
    'linux' :   ur'\n',

    'dos'   :   ur'\r\n',
    'win'   :   ur'\r\n',

    'mac'   :   ur'\r',

}

def make_conversion(regexp_dictionaries_list):
    substitute_list = []
    for d in regexp_dictionaries_list:
        for k, v in d.items():
            key      = re.compile(k, re.X + re.M + re.U)
            # value    = re.compile(v, re.X + re.U)
            substitute_list.append( (key, v) )
    return substitute_list


def eol_normalization(text, eol='unix'):
    
    """ Приводит все символы конца строки
    в единообразное состояние """

    # преобразуем все EOL к юниксовскому виду
    text = text.replace( eols['win'], eols['unix'] ) 
    text = text.replace( eols['mac'], eols['unix'] )
    
    # выполняем конечное преобразование EOL,
    # если ОС имеет конец строк отличный от UNIX или Linux
    if eol not in ('unix', 'linux'):
        text = text.replace( eols['unix'], eols[eol] )

    return text


def paragraphs(text, eol='unix'):
    
    """ Объединяет все строки, 
    не отделённые друг от друга 
    пустыми строками, в абзацы (=строки).
    При удалении символов конца строки
    заменяет их на одинарный пробел. """

    space = re.compile(ur'[ \t]%s' % eols_re[eol])
    text = space.sub(eols[eol], text)

    nEoP = re.compile(ur'''
        (?<! %(EOL)s )  # перед концом строки не д.б. другого конца строки
             %(EOL)s    # необходимо найти конец строки
        (?!  %(EOL)s )  # после конца строки не д.б. другого конца строки
        ''' % {'EOL': eols_re[eol]},
        re.VERBOSE
    )
    text = nEoP.sub(u' ', text)

    return text


def fragments(text):

    """ Разбивает текст на части 
    по глобальным тэгам указания письменности
    вроде <::слав>, <::греч> и т.д. 
    Возвращает список картежей вида 
    (tag, fragment). Полученные части могут
    быть  в том числе пустыми. """

    text = eol_normalization(text)
    text = paragraphs(text)

    # глобальные тэги переключения систем письма
    script_tags = (
        u'<::слав>',
        u'<::греч>',
        u'<::рус>',
        u'<::лат>',
        u'<::глаг>',
    )

    # В соответствии со стандартом HIP, по умолчанию предполагаем, 
    # что передаваемая строка представляет собой 
    # текст на церковно-славянском/старославянском языке
    marked_text_fragments = [(u'<::слав>', text),]

    for tag in script_tags:
        
        _marked_text_fragments = marked_text_fragments[:]
        delta = 0 # накопительное смещение фрагмента
        
        for fragment_number, (fragment_tag, fragment) in enumerate(_marked_text_fragments):
            
            new_fragments = fragment.split(tag)
            new_marked_fragments = [(fragment_tag, new_fragments[0]),]
            new_marked_fragments.extend(
                [ (tag, f) for f in new_fragments[1:] ]
            )
            marked_text_fragments[
                fragment_number + delta: 
                fragment_number + delta + 1
            ] = new_marked_fragments

            delta += len(new_marked_fragments) - 1

    return marked_text_fragments


def non_empty_fragments(text):
    
    """ Аналогична функции fragments,
    за тем исключением, что удаляет из выходного списка
    все картежи с пустыми fragment. """
    
    marked_text_fragments = fragments(text)
    return [ (tag, fragment) for tag, fragment in marked_text_fragments if fragment.strip() ]


def convert(text, conversion):
    
    """ Преобразует строку text на основе
    соответствий указанных в словаре conversion """
    
    if conversion=='delete':
        text = u''
    elif conversion:
        for src, dst in conversion:
            text = src.sub(dst, text)

    return text

def all_hip_conversions(slav=None, grec=None, rus=None, lat=None, glag=None):

    conversion_refs = {
        u'<::слав>':    slav,
        u'<::греч>':    grec,
        u'<::рус>':     rus,
        u'<::лат>':     lat,
        u'<::глаг>':    glag,
    }
    return conversion_refs


def hip2unicode(text, conversions=None):
    
    """ Преобразует символы, 
    закодированные HIP, в Unicode """

    # объявляем соответствие систем письма
    # и связанных с ними перекодировок
    if not conversions:
        conversion_refs = all_hip_conversions(slav=make_conversion(hip2cslav.hip2cslav))
    else:
        conversion_refs = conversions

    # Разбиваем текст на фрагменты
    # по глобальным тэгам систем письма
    marked_text_fragments = non_empty_fragments(text)
    
    # перекодируем каждый фрагмент
    # в соответствии используемой в нем системой письма
    converted_fragments = []
    for tag, fragment in marked_text_fragments:
        converted_fragments.append(
            convert(fragment, conversion_refs[tag])
        )

    return ''.join(converted_fragments)
