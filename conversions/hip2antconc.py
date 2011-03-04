# -*- coding: UTF-8 -*-

from hip2unicode.representations import hip
from hip2unicode.representations import antconc

conversion = (
    (u'<\(\(>', u'«'),      # замена кавычек <((>
    (u'<\)\)>', u'»'),      # <))>
    (u'<->',    u'\u2014'), # тире EM DASH

    # удаление ненужных html-тегов 
    (u'<p>',    u''),
    (u'<a.*?>', u''),
    (u'</a>',   u''),
    (u'<br>',   u''),
    (u'<hip>',  u''),
    (u'</hip>',     u''),
    (u'<title>',    u''),
    (u'</title>',   u''),
    (u'<pre>',      u''),
    # hip-нормализация
    # ...
    # удаление ненужной разметки
    # киноварь
    (ur'%<',    u''),
    (ur'%>',    u''),

    (ur'%\(',   u''),
    (ur'%\)',   u''),

    (ur'%\[',   u''),
    (ur'%\]',   u''),

    (ur'\([cсCС]\.\ *\d+\)',    u''),

    (ur'%{![^{}]+?{[^{}]*?}[^{}]*?}',   u''),
    (ur'%{![^{}]+?}',                   u''),
    (ur'%{Глава`}',                     u'Глава` '),
    (ur'%t',                            u''),

    # сноски
    # <сноска 1> ::= *{  <текст сноски> *  <текст сноски> }
    (ur'\*{.*?\*.*?}',          u''),
    # <сноска 2> ::= **{ <текст сноски> ** <текст сноски> }
    (ur'\*\*{.*?\*\*.*?}',      u''),

    # Знаки типикона для обозначения разных типов служб (шестеричная,
    # полиелейная и т.п.)
    (ur'<\(\+\)>',  u''), #     <(+)>   Бдение под великие праздники
    (ur'<\\\+/>',   u''), #     <\+/>   Бдение
    (ur'<\+>',      u''), #      <+>    Полиелей
    (ur'<\(:\.>',   u''), #     <(:.>   Славословие или шестеричная служба
    (ur'<М\\р>',    u''), #     <М\р>

    # символ "бреве" над буквой, иногда кавыка (?)
    (ur'\\\@',      u''), #     \@
    (ur'\\\[\@\]',  u''), #     \[@]

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
    (ur'\{',        u' { '),
    (ur'\}',        u' } '),
    (ur'(\@{1,2})', ur' \1 '),

    (ur'\[',        u' [ '),
    (ur'\(',        u' ( '),
    (ur'\]',        u' ] '),
    (ur'\)',        u' ) '),

    (ur'\{\s+\@',   u'{@'),
    (ur'\@\s+\}',   u'@}'),

    # звездочки для поющих на клиросе
    (ur'\*',    u''),
    # разделения на строки
    (ur'//',    u''),
    # широкая омега
    (ur'<_w>',  antconc.SMALL_OMEGA),
    # (сверх)узкое о
    (ur'<о_>',  u'о'), # кирил.
    (ur'<o_>',  u'о'), # лат.
    # разные зело и земли
    (u'<з>',    u'з'),
    (u'<_з>',   u'з'),

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

    (u's', u'\u0455'),
    (u'S', u'\u0405'),
    (hip.i_without_dot, ur'\u0131'), # U+0131 LATIN SMALL LETTER DOTLESS I

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

    (hip.equal_sign, ur''), # ur'’', # U+2019 RIGHT SINGLE QUOTATION MARK : single comma quotation mark
#    (hip.single_quote, antconc.acute),
#    (hip.back_single_quote, antconc.gravis),
#    (hip.caret, antconc.circumflex),
#    (hip.tilde, antconc.titlo),

    (ur'\\[ъЪ]', u'Ъ'),
    (ur'\\[бБ]', u'Б'),
    (ur'\\[вВ]', u'В'),
    (ur'\\[гГ]', u'Г'),
    (ur'\\[дД]', u'Д'),
    (ur'\\[жЖ]', u'Ж'),
    (ur'\\[зЗ]', u'З'),
    (ur'\\[кК]', u'К'),
    (ur'\\[лЛ]', u'Л'),
    (ur'\\[мМ]', u'М'),
    (ur'\\[нН]', u'Н'),
    (ur'\\[оО]', u'О'),
    (ur'\\[рР]', u'Р'),
    (ur'\\[сС]', u'С'),
    (ur'\\[тТ]', u'Т'),
    (ur'\\[%s%s]' % (antconc.SMALL_FITA, antconc.CAPITAL_FITA), antconc.CAPITAL_FITA),
    # ^ нельзя писать ur'\\[fF]', т.к. они уже ранее были заменены на антконковские фиты.
    (ur'\\[хХ]', u'Х'),
    (ur'\\[цЦ]', u'Ц'),
    (ur'\\[чЧ]', u'Ч'),
    (ur'\\[шШ]', u'Ш'),

    (hip.Oy, antconc.CAPITAL_DIGRAPH_UK),
    (hip.oy, antconc.SMALL_DIGRAPH_UK),

    (hip.W, antconc.CAPITAL_OMEGA),
    (hip.w, antconc.SMALL_OMEGA),

    (ur'(?<!_)' + hip.Y, antconc.CAPITAL_MONOGRAPH_UK),
    (ur'(?<!_)' + hip.y, antconc.SMALL_MONOGRAPH_UK),

    (u'i', u'\u0456'),
    (u'I', u'\u0406'),

    (u'_у', u'у'),
    (u'#', u'\u0482'), # знак тысячи

    (ur'\ {2,}',    u' '), # два и более пробелов заменяем на один
)
