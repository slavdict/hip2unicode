# -*- coding: UTF-8 -*-

from hip2unicode.conversions import hip2cslav
import re

def make_conversion(regexp_dictionaries_list):
    substitute_list = []
    for d in regexp_dictionaries_list:
        for k, v in d.items():
            key      = re.compile(k, re.X + re.M + re.U)
            # value    = re.compile(v, re.X + re.U)
            substitute_list.append( (key, v) )
    return substitute_list


def paragraphs(str):
    return str


def fragments(str):

    """ Разбивает текст на части 
    по глобальным тэгам указания письменности
    вроде <::слав>, <::греч> и т.д. 
    Возвращает список картежей вида 
    (tag, fragment). Полученные части могут
    быть  в том числе пустыми. """

    # глобальные тэги переключения систем письма
    script_tags = (
        u'<::слав>',
        u'<::греч>',
        u'<::рус>',
        u'<::лат>',
        u'<::глаг>',
    )

    # гарантируем, что переданая строка 
    # будет представлена в Unicode
    str = unicode(str)

    # В соответствии со стандартом HIP, по умолчанию предполагаем, 
    # что передаваемая строка представляет собой 
    # текст на церковно-славянском/старославянском языке
    marked_text_fragments = [(u'<::слав>', str),]

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


def non_empty_fragments(str):
    
    """ Аналогична функции fragments,
    за тем исключением, что удаляет из выходного списка
    все картежи с пустыми fragment. """
    
    marked_text_fragments = fragments(str)
    return [ (tag, fragment) for tag, fragment in marked_text_fragments if fragment.strip() ]


def convert(str, conversion):
    
    """ Преобразует строку str на основе
    соответствий указанных в словаре conversion """
    
    if conversion:
        for src, dst in conversion:
            str = src.sub(dst, str)

    return str


def hip2unicode(str):
    
    """ Преобразует символы, 
    закодированные HIP, в Unicode """

    # объявляем соответствие систем письма
    # и связанных с ними перекодировок
    conversion_refs = {
        u'<::слав>':    make_conversion(hip2cslav.hip2cslav),
        u'<::греч>':    None,
        u'<::рус>':     None,
        u'<::лат>':     None,
        u'<::глаг>':    None,
    }

    # Разбиваем текст на фрагменты
    # по глобальным тэгам систем письма
    marked_text_fragments = non_empty_fragments(str)
    
    # перекодируем каждый фрагмент
    # в соответствии используемой в нем системой письма
    converted_fragments = []
    for tag, fragment in marked_text_fragments:
        converted_fragments.append(
            convert(fragment, conversion_refs[tag])
        )

    return " ".join(converted_fragments)
