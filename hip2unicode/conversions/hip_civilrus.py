"""
HIP to Civil Russian

Перекодировка в русскую гражданку.

"""

from hip2unicode.representations.RE import *
from hip2unicode.representations.hip import *
from hip2unicode.representations import antconc

conversion = (
    (r'<\(\(>', '«'),       # замена кавычек <((>
    (r'<\)\)>', '»'),       # <))>
    (r'<->',    '\u2014'),  # тире EM DASH

    # удаление ненужных html-тегов
    (r'<p>',    ''),
    (r'<a.*?>', ''),
    (r'</a>',   ''),
    (r'<br>',   ''),
    (r'<hip>',  ''),
    (r'</hip>',     ''),
    (r'<title>',    ''),
    (r'</title>',   ''),
    (r'<pre>',      ''),
    # hip-нормализация
    # ...
    # удаление ненужной разметки
    # киноварь
    (r'%<',    ''),
    (r'%>',    ''),

    (r'%\(',   ''),
    (r'%\)',   ''),

    (r'%\[',   ''),
    (r'%\]',   ''),

    (r'\([cсCС]\.\ *\d+\)',    ''),

    (r'%{![^{}]+?{[^{}]*?}[^{}]*?}',   ''),
    (r'%{![^{}]+?}',                   ''),
    (r'%{Глава`}',                     'Глава '),
    (r'%t',                            ''),

    # сноски
    # <сноска 1> ::= *{  <текст сноски> *  <текст сноски> }
    (r'\*{.*?\*.*?}',          ''),
    # <сноска 2> ::= **{ <текст сноски> ** <текст сноски> }
    (r'\*\*{.*?\*\*.*?}',      ''),

    # Знаки типикона для обозначения разных типов служб (шестеричная,
    # полиелейная и т.п.)
    (r'<\(\+\)>',  ''),  #    <(+)>   Бдение под великие праздники
    (r'<\\\+/>',   ''),  #    <\+/>   Бдение
    (r'<\+>',      ''),  #     <+>    Полиелей
    (r'<\(:\.>',   ''),  #    <(:.>   Славословие или шестеричная служба
    (r'<М\\р>',    ''),  #    <М\р>

    # символ "бреве" над буквой, иногда кавыка (?)
    (r'\\\@',      ''),  #    \@
    (r'\\\[\@\]',  ''),  #    \[@]

    # настоящие сноски
    # Имеют вид:
    #
    #    <text> ::= <текст, к которому относится сноска>
    #    <note> ::= <текст сноски>
    #
    #    1) <text>@{<note>}
    #    2) @<text>@{@<note>@}
    #    3) @@<text>@@{@@<note>@@}
    #

    (r'\{\s+\@',   '{@'),
    (r'\@\s+\}',   '@}'),

    # звездочки для поющих на клиросе
    (r'\*',    ''),
    # разделения на строки -- //
    # и разделители для поющих на клиросе -- /
    (r'/',    ''),
    # широкая омега
    (r'<_w>',  'о'),
    (r'<_W>',  'О'),
    # (сверх)узкое о
    (r'<о_>',  'о'),  # кирил.
    (r'<o_>',  'о'),  # лат.
    # разные зело и земли
    (r'<з>',    'з'),
    (r'<_з>',   'з'),

    # Regular expressions for character replacement
    # in text marked as being typed in Church Slavonic script
    # (script tag <::слав> or without any script tag
    # if no script tag is in the document)
    (A, 'А'),
    (a, 'а'),

    (B, 'В'),
    (b, 'в'),

    (E, 'Е'),
    (e, 'е'),

    (r's', 'з'),
    (r'S', 'З'),
    (i_without_dot, '\u0131'), # U+0131 LATIN SMALL LETTER DOTLESS I

    (K, 'К'),
    (k, 'к'),

    (M, 'М'),
    (m, 'м'),

    (H, 'Н'),
    (h, 'н'),

    (O, 'О'),
    (o, 'о'),

    (P, 'Р'),
    (p, 'р'),

    (C, 'С'),
    (c, 'с'),

    (T, 'Т'),
    (t, 'т'),

    (X, 'Х'),
    (x, 'х'),

    (V_double_gravis, antconc.CAPITAL_IZHICA),
    (v_double_gravis, antconc.SMALL_IZHICA),

    (Ole, 'О'),
    (ole, 'о'),

    (Wide_E, 'Е'),
    (wide_e, 'е'),

    (Yat, 'Е'),
    (yat, 'е'),

    (V, antconc.CAPITAL_IZHICA),
    (v, antconc.SMALL_IZHICA),

    (Ksi, 'Кс'),
    (ksi, 'кс'),

    (Wide_O, 'О'),
    (wide_o, 'о'),

    (Ot, 'От'),
    (ot, 'от'),

    (Psi, 'Пс'),
    (psi, 'пс'),

    (F, 'Ф'),
    (f, 'ф'),

    (J_a, 'Я'),
    (j_a, 'я'),

    (Ja, 'Я'),
    (ja, 'я'),

    (equal_sign, r''),  # ur'’',
                        # U+2019 RIGHT SINGLE QUOTATION MARK :
                        # single comma quotation mark

    (r'\\[бБ]', r'\Б'),
    (r'\\[вВ]', r'\В'),
    (r'\\[гГ]', r'\Г'),
    (r'\\[дД]', r'\Д'),
    (r'\\[жЖ]', r'\Ж'),
    (r'\\[зЗ]', r'\З'),
    (r'\\[кК]', r'\К'),
    (r'\\[лЛ]', r'\Л'),
    (r'\\[мМ]', r'\М'),
    (r'\\[нН]', r'\Н'),
    (r'\\[оО]', r'\О'),
    (r'\\[пП]', r'\П'),
    (r'\\[рР]', r'\Р'),
    (r'\\[сС]', r'\С'),
    (r'\\[тТ]', r'\Т'),
    (r'\\[{0}{1}]'.format(antconc.SMALL_FITA, antconc.CAPITAL_FITA),
                r'\Ф'),
    # ^ нельзя писать ur'\\[fF]', т.к. они уже ранее были заменены на
    # антконковские фиты.

    (r'\\[хХ]', r'\Х'),
    (r'\\[цЦ]', r'\Ц'),
    (r'\\[чЧ]', r'\Ч'),
    (r'\\[шШ]', r'\Ш'),
    (r'\\[ъЪ]', r'\Ъ'),

    (Oy, 'У'),
    (oy, 'у'),

    (W, 'О'),
    (w, 'о'),

    (r'(?<!_)' + Y, 'У'),
    (r'(?<!_)' + y, 'у'),

    (r'i', 'и'),
    (r'I', 'И'),

    (r'_у', 'у'),
    (r'#', '\u0482'),  # знак тысячи

    (r'\ {2,}', ' '),  # два и более пробелов заменяем на один
    (r"['`\^]", ''),

    (r'([Аа])[Пп]\\С[Лл]', r'\g<1>постол'),
    (r'([Аа])п\\Стол',     r'\g<1>постол'),
    (r'([Бб])[Гг]~',       r'\g<1>ог'),
    (r'([Бб])ж~тв',        r'\g<1>ожеств'),
    (r'([Бб])ж~',          r'\g<1>ож'),
    (r'([Бб])ж\\Ств',      r'\g<1>ожеств'),
    (r'([Бб])з~',          r'\g<1>оз'),
    (r'([Бб])л~г',     r'\g<1>лаг'),
    (r'([Бб])л~ж',     r'\g<1>лаж'),
    (r'([Бб])л~з',     r'\g<1>лаз'),
    (r'([Бб])л\\Гв',   r'\g<1>лагов'),
    (r'([Бб])лг\\Дт',  r'\g<1>лагодат'),
    (r'([Бб])лг\\Св',  r'\g<1>лагослов'),
    (r'([Бб])лг\\Сл',  r'\g<1>лагосл'),
    (r'([Бб])лг\\С',   r'\g<1>лагос'),
    (r'([Бб])ч\\Ден',  r'\g<1>огородичен'),
    (r'([Бб])ц\\Д',    r'\g<1>огородиц'),
    (r'([Вв])л\\Дк',   r'\g<1>ладык'),
    (r'([Вв])л\\Дц',   r'\g<1>ладыц'),
    (r'([Вв])л\\Дчц',  r'\g<1>ладычиц'),
    (r'([Вв])л\\Дч',   r'\g<1>ладыч'),
    (r'ѵ\\Гл',          'вангел'),     # Евангел...
    (r'ѵ\\Г',           'ванг'),       # Евангел...
    (r'гг[е~]л',        'нгел'),       # ангел
    (r'([Гг])л~',      r'\g<1>лагол'),
    (r'([Гг])л\\В',    r'\g<1>лав'),
    (r'([Гг])д\\Снь',  r'\g<1>осподень'),
    (r'([Гг])д\\Св',   r'\g<1>осподев'),
    (r'([Гг])д\\С',    r'\g<1>оспод'),
    (r'([Гг])п\\Сж',   r'\g<1>оспож'),
    (r'([Дд])в~д',     r'\g<1>авид'),
    (r'([Дд])в~',      r'\g<1>ев'),
    (r'([Дд])в\\Ств',  r'\g<1>евств'),
    (r'([Дд])с~',      r'\g<1>ус'),
    (r'([Дд])х~',      r'\g<1>ух'),
    (r'([Дд])ш~',      r'\g<1>уш'),
    (r'([Ии])~с',      r'\g<1>сус'),
    (r'([Ии])и~л',     r'\g<1>зраил'),
    (r'([Кк])р~с',     r'\g<1>рес'),
    (r'([Кк])р~ш',     r'\g<1>реш'),
    (r'([Кк])р~щ',     r'\g<1>рещ'),
    (r'([Кк])р\\Ст',   r'\g<1>рест'),
    (r'([Кк])р\\Сни',  r'\g<1>ресени'),  # К сожалению это правило
    # не 100%-ное, потому что, например, для формы ``воскрСнiи`` встречается
    # как предложный падеж существительного ВОСКРЕСЕНИЕ, так и мн.ч.
    # прилагательного ВОСКРЕСНЫЙ, хотя последний случай довольно редкий. Также
    # это правило будет работать ещё хуже в текстах с ненормированной
    # орфографией.

    (r'([Кк])р\\С',    r'\g<1>рес'),
    (r'([Кк])\\Ср',    r'\g<1>рес'),
    (r'([Мм])\\Др',    r'\g<1>удр'),
    (r'([Мм])л~тв',    r'\g<1>олитв'),
    (r'([Мм])л\\Днцъ', r'\g<1>ладенец'),
    (r'([Мм])л\\Дн',   r'\g<1>ладен'),
    (r'([Мм])л\\Срд',  r'\g<1>илосерд'),
    (r'([Мм])л\\Ст',   r'\g<1>илост'),
    (r'([Мм])л\\С',    r'\g<1>илос'),
    (r'([Мм])т~р',     r'\g<1>атер'),
    (r'([Мм])т~',      r'\g<1>ат'),
    (r'([Мм])р~и',     r'\g<1>ари'),
    (r'([Мм])\\Рк',    r'\g<1>ярек'),   # Имярек
    (r'([Мм])ч~нк',    r'\g<1>ученик'),
    (r'([Мм])ч~нц',    r'\g<1>учениц'),
    (r'([Мм])ч~нч',    r'\g<1>ученич'),
    (r'([Мм])ч~н',     r'\g<1>учен'),
    (r'([Мм])ц\\С',    r'\g<1>есяц'),
    (r'([Нн])б~с',     r'\g<1>ебес'),
    (r'([Нн])б\\Сс',   r'\g<1>ебес'),
    (r'([Нн])б\\С',    r'\g<1>ебес'),
    (r'([Нн])б~',      r'\g<1>еб'),
    (r'([Нн])л\\Д',    r'\g<1>едел'),
    (r'([Нн])н~',      r'\g<1>ын'),
    (r"([Оо])ч~ь",     r'\g<1>течь'),
    (r"([Оо])ч~ес",    r'\g<1>течес'),
    (r"([Оо])ч~",      r'\g<1>тч'),
    (r"([Оо])ц~ъ",     r'\g<1>тец'),
    (r"([Оо])ц~",      r'\g<1>тц'),
    (r'([Пп])ра\\З\\b[\.]!', r'\g<1>раз.'), # праЗ(.) --> праз.[дник-]
    (r'([Пп])рв\\Днъ', r'\g<1>раведен'),
    (r'([Пп])рв\\Дн',  r'\g<1>раведн'),
    (r'([Пп])р\\Дтч',  r'\g<1>редтеч'), # Предтеча
    (r'([Пп])р\\Дт',   r'\g<1>редт'),   # Предтеча
    (r'([Пп])рп\\Дб',  r'\g<1>реподоб'),
    (r'([Пп])реп\\Дб', r'\g<1>реподоб'),
    (r'([Пп])р\\Ор',   r'\g<1>рор'),    # Пророк
    (r'([Пп])р\\Сн',   r'\g<1>рисн'),
    (r'([Пп])р\\Ст',   r'\g<1>рест'),
    (r'([Пп])рч\\Ст',  r'\g<1>речист'),
    (r'([Пп])\\Скп',   r'\g<1>ископ'),  # епископ
    (r'([Пп])\\Ск',    r'\g<1>иск'),
    (r'([Рр])ж\\Ств',  r'\g<1>ождеств'),
    (r'([Рр])\\Сл',    r'\g<1>усал'),   # Иерусалим
    (r'([Сс])л~нц',    r'\g<1>олнц'),
    (r'([Сс])н~',      r'\g<1>ын'),
    (r'([Сс])п~с',     r'\g<1>пас'),
    (r'([Сс])п\\Сн',   r'\g<1>пасен'),
    (r'([Сс])п\\С',    r'\g<1>пас'),
    (r'([Сс])р\\Дц',   r'\g<1>ердц'),
    (r'([Сс])р\\Дч',   r'\g<1>ердеч'),
    (r'([Сс])т~',      r'\g<1>вят'),
    (r'([Сс])тр\\Ст',  r'\g<1>траст'),
    (r'([Сс])\\Х',     r'\g<1>тих'),
    (r'([Сс])т\\Хр',   r'\g<1>тихир'),
    (r'([Сс])щ~',      r'\g<1>вящ'),
    (r'([Тт])р\\Оц',   r'\g<1>роиц'),
    (r'([Тт])р\\Оч',   r'\g<1>роич'),
    (r'([Тт])р\\Ст',   r'\g<1>рисвят'),
    (r'([Хх])р\\Ст',   r'\g<1>рист'),
    (r'([Цц])р~к',     r'\g<1>ерк'),
    (r'([Цц])р~',      r'\g<1>ар'),
    (r'([Цц])р\\С',    r'\g<1>арс'),
    (r'([Цц])\\Ср',    r'\g<1>арс'),
    (r'([Чч])л~в',     r'\g<1>елов'),
    (r'([Чч])~нк',     r'\g<1>еник'),
    (r'([Чч])~нц',     r'\g<1>ениц'),
    (r'([Чч])~тл',     r'\g<1>ител'),
    (r'([Чч])н~к',     r'\g<1>еник'),
    (r'([Чч])н~ц',     r'\g<1>ениц'),
    (r'([Чч])н~',      r'\g<1>ен'),
    (r'([Чч])\\Стн',   r'\g<1>естн'),
    (r'([Чч])т\\Сн',   r'\g<1>естн'),
    (r'([Чч])\\Ст',    r'\g<1>ист'),
    (r'([Чч])т\\С',    r'\g<1>ист'),
    (r'([Чч])т~л',     r'\g<1>ител'),

    (r'а' + antconc.SMALL_IZHICA,  'ав'),
    (r'е' + antconc.SMALL_IZHICA,  'ев'),
    (antconc.SMALL_IZHICA,          'и'),

    (r'\\З', 'з'),
    (r'\\Ъ', 'ъ'),

    (r'(ъ$)|(ъ(?=[\sБбВбГгДдЖжЗзКкЛлМмНнПпРрСсТтФфХхЦцЧчШшЩщ,\.;:\?\!]))', ''),

    (r'ъа', 'а'),
    (r'ъо', 'о'),
    (r'ъу', 'у'),
    (r'ъы', 'ы'),
    (r'ъи', 'ы'),

    (r'жы', 'жи'),
    (r'шы', 'ши'),
    (r'щы', 'щи'),
    (r'жя', 'жа'),
    (r'шя', 'ша'),
    (r'щя', 'ща'),
)
