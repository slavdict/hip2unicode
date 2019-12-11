import re

eols = {

    'unix'  :   '\n',
    'linux' :   '\n',

    'dos'   :   '\r\n',
    'win'   :   '\r\n',

    'mac'   :   '\r',
}

eols_re = {

    'unix'  :   r'\n',
    'linux' :   r'\n',

    'dos'   :   r'\r\n',
    'win'   :   r'\r\n',

    'mac'   :   r'\r',

}

def make_conversion(regexp_dictionaries_list):
    """ Получает на вход список словарей с правилами конвертации, оформленными
    в виде словарных пар "ключ-значение". Последовательно перебирает все
    словари и формирует список пар <откомпилированное регулярное выражение,
    необходимая для неё текстовая замена>.

    Данная функция оставлена для совместимости и признается устаревшей.
    Поскольку все правила конвертации решено оформлять в виде списка
    упорядоченных пар <НЕоткомпилированное регулярное выражение, результирующая
    текстовая подстановка> """

    substitute_list = []
    for d in regexp_dictionaries_list:
        for k, v in list(d.items()):
            key      = re.compile(k, re.M + re.U)
            substitute_list.append( (key, v) )
    return substitute_list


def compile_conversion(conversion):
    """ Получает на вход список или картеж пар вида <НЕоткомпилированное
    регулярное выражение, результирующая текстовая подстановка>. В этом списке
    все сырые строки неоткомпилированных RegExp заменяются на сами
    откомпилированные объекты регулярных выражений. """

    substitute_list = []
    for to_find, to_substitute in conversion:
        compiled_re = re.compile(to_find, re.M + re.U)
        substitute_list.append( (compiled_re, to_substitute) )
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

    space = re.compile(r'[ \t]%s' % eols_re[eol])
    text = space.sub(eols[eol], text)

    nEoP = re.compile(r'''
        (?<! %(EOL)s )  # перед концом строки не д.б. другого конца строки
             %(EOL)s    # необходимо найти конец строки
        (?!  %(EOL)s )  # после конца строки не д.б. другого конца строки
        ''' % {'EOL': eols_re[eol]},
        re.VERBOSE
    )
    text = nEoP.sub(' ', text)

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
        '<::слав>',
        '<::греч>',
        '<::рус>',
        '<::лат>',
        '<::глаг>',
    )

    # В соответствии со стандартом HIP, по умолчанию предполагаем,
    # что передаваемая строка представляет собой
    # текст на церковно-славянском/старославянском языке
    marked_text_fragments = [('<::слав>', text),]

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
        text = ''
    elif conversion:
        for src, dst in conversion:
            text = src.sub(dst, text)

    return text

def all_hip_conversions(slav=None, grec=None, rus=None, lat=None, glag=None):

    conversion_refs = {
        '<::слав>':    slav,
        '<::греч>':    grec,
        '<::рус>':     rus,
        '<::лат>':     lat,
        '<::глаг>':    glag,
    }
    return conversion_refs


def hip2unicode(text, conversions=None):

    """ Преобразует символы,
    закодированные HIP, в Unicode """

    # объявляем соответствие систем письма
    # и связанных с ними перекодировок
    if not conversions:
        # Если соответствия не переданы,
        # для всех систем письма
        # назначается тождественное преобразование,
        # т.е. никакой конвертации происходить не будет.
        conversion_refs = all_hip_conversions()
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
