from hip2unicode.representations import hip
from hip2unicode.representations import antconc

conversion = (
    ('<\(\(>', '«'),      # замена кавычек <((>
    ('<\)\)>', '»'),      # <))>
    ('<->',    '\u2014'), # тире EM DASH

    # удаление ненужных html-тегов
    ('<p>',    ''),
    ('<a.*?>', ''),
    ('</a>',   ''),
    ('<br>',   ''),
    ('<hip>',  ''),
    ('</hip>',     ''),
    ('<title>',    ''),
    ('</title>',   ''),
    ('<pre>',      ''),
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

    # Адреса для АнтКонка
    (r'%{!Адрес:([^{}]*?)}',   r'<\1>'),
    # TODO: Текст адреса становится подвержен перекодированию из HIP
    # в формат для АнтКонка. Кажется, у нас в адресах не используется
    # ничего, что может быть перекодировано, но опасность остается.

    (r'%{![^{}]+?{[^{}]*?}[^{}]*?}',   ''),
    (r'%{![^{}]+?}',                   ''),
    (r'%{Глава`}',                     'Глава` '),
    (r'%t',                            ''),

    # сноски
    # <сноска 1> ::= *{  <текст сноски> *  <текст сноски> }
    (r'\*{.*?\*.*?}',          ''),
    # <сноска 2> ::= **{ <текст сноски> ** <текст сноски> }
    (r'\*\*{.*?\*\*.*?}',      ''),

    # Знаки типикона для обозначения разных типов служб (шестеричная,
    # полиелейная и т.п.)
    (r'<\(\+\)>',  ''), #     <(+)>   Бдение под великие праздники
    (r'<\\\+/>',   ''), #     <\+/>   Бдение
    (r'<\+>',      ''), #      <+>    Полиелей
    (r'<\(:\.>',   ''), #     <(:.>   Славословие или шестеричная служба
    (r'<М\\р>',    ''), #     <М\р>

    # символ "бреве" над буквой, иногда кавыка (?)
    (r'\\\@',      ''), #     \@
    (r'\\\[\@\]',  ''), #     \[@]

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
    # NB: Отбиваем пробелами символы фигурных скобок и собаки, чтобы нормально
    # искался текст в антконке по старым запросам.
    (r'\{',        ' { '),
    (r'\}',        ' } '),
    (r'(\@{1,2})', r' \1 '),

    (r'\[',        ' [ '),
    (r'\(',        ' ( '),
    (r'\]',        ' ] '),
    (r'\)',        ' ) '),

    (r'\{\s+\@',   '{@'),
    (r'\@\s+\}',   '@}'),

    # звездочки для поющих на клиросе
    (r'\*',    ''),
    # разделения на строки -- //
    # и разделители для поющих на клиросе -- /
    (r'/',    ''),
    # широкая омега
    (r'<_w>',  antconc.SMALL_OMEGA),
    # (сверх)узкое о
    (r'<о_>',  'о'), # кирил.
    (r'<o_>',  'о'), # лат.
    # разные зело и земли
    ('<з>',    'з'),
    ('<_з>',   'з'),

    # Regular expressions for character replacement
    # in text marked as being typed in Church Slavonic script
    # (script tag <::слав> or without any script tag
    # if no script tag is in the document)
    (hip.A, antconc.CAPITAL_AZ),
    (hip.a, antconc.SMALL_AZ),

    (hip.B, antconc.CAPITAL_VEDI),
    (hip.b, antconc.SMALL_VEDI),

    (hip.E, antconc.CAPITAL_ESTJ),
    (hip.e, antconc.SMALL_ESTJ),

    ('s', '\u0455'),
    ('S', '\u0405'),
    (hip.i_without_dot, '\u0131'), # U+0131 LATIN SMALL LETTER DOTLESS I

    (hip.K, antconc.CAPITAL_KAKO),
    (hip.k, antconc.SMALL_KAKO),

    (hip.M, antconc.CAPITAL_MYSLETE),
    (hip.m, antconc.SMALL_MYSLETE),

    (hip.H, antconc.CAPITAL_NASH),
    (hip.h, antconc.SMALL_NASH),

    (hip.O, antconc.CAPITAL_ON),
    (hip.o, antconc.SMALL_ON),

    (hip.P, antconc.CAPITAL_RCY),
    (hip.p, antconc.SMALL_RCY),

    (hip.C, antconc.CAPITAL_SLOVO),
    (hip.c, antconc.SMALL_SLOVO),

    (hip.T, antconc.CAPITAL_TVERDO),
    (hip.t, antconc.SMALL_TVERDO),

    (hip.X, antconc.CAPITAL_XER),
    (hip.x, antconc.SMALL_XER),

    (hip.V_double_gravis, antconc.CAPITAL_IZHICA),
    (hip.v_double_gravis, antconc.SMALL_IZHICA),

    (hip.Ole, antconc.CAPITAL_OLE),
    (hip.ole, antconc.SMALL_OLE),

    (hip.Wide_E, antconc.CAPITAL_WIDE_ESTJ),
    (hip.wide_e, antconc.SMALL_WIDE_ESTJ),

    (hip.Yat, antconc.CAPITAL_JATJ),
    (hip.yat, antconc.SMALL_JATJ),

    (hip.V, antconc.CAPITAL_IZHICA),
    (hip.v, antconc.SMALL_IZHICA),

    (hip.Ksi, antconc.CAPITAL_KSI),
    (hip.ksi, antconc.SMALL_KSI),

    (hip.Wide_O, antconc.CAPITAL_WIDE_ON),
    (hip.wide_o, antconc.SMALL_WIDE_ON),

    (hip.Ot, antconc.CAPITAL_OT),
    (hip.ot, antconc.SMALL_OT),

    (hip.Psi, antconc.CAPITAL_PSI),
    (hip.psi, antconc.SMALL_PSI),

    (hip.F, antconc.CAPITAL_FITA),
    (hip.f, antconc.SMALL_FITA),

    (hip.J_a, antconc.CAPITAL_I_AZ),
    (hip.j_a, antconc.SMALL_I_AZ),

    (hip.Ja, antconc.CAPITAL_JUS_MALYJ),
    (hip.ja, antconc.SMALL_JUS_MALYJ),

    (hip.equal_sign, r''), # ur'’', # U+2019 RIGHT SINGLE QUOTATION MARK : single comma quotation mark
#    (hip.single_quote, antconc.acute),
#    (hip.back_single_quote, antconc.gravis),
#    (hip.caret, antconc.circumflex),
#    (hip.tilde, antconc.titlo),

    (r'\\[бБ]', 'Б'),
    (r'\\[вВ]', 'В'),
    (r'\\[гГ]', 'Г'),
    (r'\\[дД]', 'Д'),
    (r'\\[жЖ]', 'Ж'),
    (r'\\[зЗ]', 'З'),
    (r'\\[кК]', 'К'),
    (r'\\[лЛ]', 'Л'),
    (r'\\[мМ]', 'М'),
    (r'\\[нН]', 'Н'),
    (r'\\[оО]', 'О'),
    (r'\\[пП]', 'П'),
    (r'\\[рР]', 'Р'),
    (r'\\[сС]', 'С'),
    (r'\\[тТ]', 'Т'),
    (r'\\[%s%s]' % (antconc.SMALL_FITA, antconc.CAPITAL_FITA), antconc.CAPITAL_FITA),
    # ^ нельзя писать ur'\\[fF]', т.к. они уже ранее были заменены на антконковские фиты.
    (r'\\[хХ]', 'Х'),
    (r'\\[цЦ]', 'Ц'),
    (r'\\[чЧ]', 'Ч'),
    (r'\\[шШ]', 'Ш'),
    (r'\\[ъЪ]', 'Ъ'),

    (hip.Oy, antconc.CAPITAL_DIGRAPH_UK),
    (hip.oy, antconc.SMALL_DIGRAPH_UK),

    (hip.W, antconc.CAPITAL_OMEGA),
    (hip.w, antconc.SMALL_OMEGA),

    (r'(?<!_)' + hip.Y, antconc.CAPITAL_MONOGRAPH_UK),
    (r'(?<!_)' + hip.y, antconc.SMALL_MONOGRAPH_UK),

    ('i', '\u0456'),
    ('I', '\u0406'),

    ('_у', 'у'),
    ('#', '\u0482'), # знак тысячи

    (r'\ {2,}',    ' '), # два и более пробелов заменяем на один
)
