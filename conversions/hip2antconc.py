# -*- coding: UTF-8 -*-

from hip2unicode.representations import hip
from hip2unicode.representations import antconc

hip2antconc = (
{
    u'<\(\(>' : u'«', # замена кавычек <((>
    u'<\)\)>' : u'»', # <))>
    u'<->': u'\u2014', # тире EM DASH
# удаление ненужных html-тегов 
    u'<p>': u'',
    u'<a.*?>': u'',
    u'</a>': u'',
    u'<br>': u'',
    u'<hip>': u'',
    u'</hip>': u'',
    u'<title>': u'',
    u'</title>': u'',
    u'<pre>': u'',
},
# hip-нормализация
# ...
# удаление ненужной разметки
{   # киноварь
    ur'%<':   u'',
    ur'%>':   u'',

    ur'%\(':  u'',
    ur'%\)':  u'',

    ur'%\[':  u'',
    ur'%\]':  u'',
},
{
    ur'\([cсCС]\.\ *\d+\)':  u'', 
},
{   # сноски
    # <сноска 1> ::= *{  <текст сноски> *  <текст сноски> }
    ur' \*{ .*? \* .*? } ': u'', 
    # <сноска 2> ::= **{ <текст сноски> ** <текст сноски> } 
    ur''' \*\*{ .*?  \*\* .*?} ''' : u'',
},
{
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
    ur'\{': u' { ',
    ur'\}': u' } ',
    ur'(\@{1,2})': ur' \1 ',

    ur'\[': u' [ ',
    ur'\(': u' ( ',
    ur'\]': u' ] ',
    ur'\)': u' ) ',
},
{
    ur'\ {2,}': u' ', # два и более пробелов заменяем на один
},
{
    ur'\{ \@': u'{@',
    ur'\@ \}': u'@}',
},
{   # звездочки для поющих на клиросе
    ur'\*': u'',
    # разделения на строки
    ur'//': u'',
    # широкая омега
    ur'<_w>' : antconc.SMALL_OMEGA,
    # (сверх)узкое о
    ur'<о_>' : u'о', # кирил.
    ur'<o_>' : u'о', # лат.
},
{
    
    # Regular expressions for character replacement
    # in text marked as being typed in Church Slavonic script
    # (script tag <::слав> or without any script tag
    # if no script tag is in the document)
    hip.A : antconc.CAPITAL_AZ ,
    hip.a : antconc.SMALL_AZ ,
 
    hip.B : antconc.CAPITAL_VEDI ,
    hip.b : antconc.SMALL_VEDI ,

    hip.E : antconc.CAPITAL_ESTJ ,
    hip.e : antconc.SMALL_ESTJ ,

    u's'  : u'\u0455',
    u'S'  : u'\u0405',
    hip.i_without_dot : ur'\u0131', # U+0131 LATIN SMALL LETTER DOTLESS I

    hip.K : antconc.CAPITAL_KAKO ,
    hip.k : antconc.SMALL_KAKO ,

    hip.M : antconc.CAPITAL_MYSLETE ,
    hip.m : antconc.SMALL_MYSLETE ,

    hip.H : antconc.CAPITAL_NASH ,
    hip.h : antconc.SMALL_NASH ,
    
    hip.O : antconc.CAPITAL_ON ,
    hip.o : antconc.SMALL_ON ,

    hip.P : antconc.CAPITAL_RCY ,
    hip.p : antconc.SMALL_RCY ,

    hip.C : antconc.CAPITAL_SLOVO ,
    hip.c : antconc.SMALL_SLOVO ,

    hip.T : antconc.CAPITAL_TVERDO ,
    hip.t : antconc.SMALL_TVERDO ,

    hip.X : antconc.CAPITAL_XER ,
    hip.x : antconc.SMALL_XER ,

    hip.V_double_gravis : antconc.CAPITAL_IZHICA ,
    hip.v_double_gravis : antconc.SMALL_IZHICA ,

    hip.Ole : antconc.CAPITAL_OLE ,
    hip.ole : antconc.SMALL_OLE ,
},
{
    hip.Wide_E : antconc.CAPITAL_WIDE_ESTJ ,
    hip.wide_e : antconc.SMALL_WIDE_ESTJ ,

    hip.Yat : antconc.CAPITAL_JATJ ,
    hip.yat : antconc.SMALL_JATJ ,

    hip.V : antconc.CAPITAL_IZHICA ,
    hip.v : antconc.SMALL_IZHICA ,

    hip.Ksi : antconc.CAPITAL_KSI ,
    hip.ksi : antconc.SMALL_KSI ,

    hip.Wide_O : antconc.CAPITAL_WIDE_ON ,
    hip.wide_o : antconc.SMALL_WIDE_ON ,

    hip.Ot : antconc.CAPITAL_OT ,
    hip.ot : antconc.SMALL_OT ,

    hip.Psi : antconc.CAPITAL_PSI ,
    hip.psi : antconc.SMALL_PSI ,

    hip.F : antconc.CAPITAL_FITA ,
    hip.f : antconc.SMALL_FITA ,

    hip.J_a : antconc.CAPITAL_I_AZ ,
    hip.j_a : antconc.SMALL_I_AZ ,

    hip.Ja : antconc.CAPITAL_JUS_MALYJ ,
    hip.ja : antconc.SMALL_JUS_MALYJ ,

    hip.equal_sign : ur'', # ur'’' , # U+2019 RIGHT SINGLE QUOTATION MARK : single comma quotation mark
#    hip.single_quote : antconc.acute ,
#    hip.back_single_quote : antconc.gravis ,
#    hip.caret : antconc.circumflex ,
#    hip.tilde : antconc.titlo ,

    hip.paerok : u'Ъ',
    ur'\\Ъ'    : u'Ъ', 
    ur'\\б' : u'Б',
    ur'\\Б' : u'Б',
    hip.vedi_titlo : u'В' ,
    ur'\\В'        : u'В' ,
    hip.glagol_titlo : u'Г' ,
    ur'\\Г'          : u'Г' ,
    hip.dobro_titlo : u'Д' ,
    ur'\\Д'         : u'Д',
    ur'\\к' : u'К',
    ur'\\К' : u'К',
    ur'\\л' : u'Л',
    ur'\\Л' : u'Л',
    ur'\\н' : u'Н',
    ur'\\Н' : u'Н',
    hip.on_titlo : u'О' ,
    ur'\\О'      : u'О',
    hip.rcy_titlo : u'Р' ,
    ur'\\Р'       : u'Р',
    hip.slovo_titlo : u'С' ,
    ur'\\С'         : u'С',
    hip.kher_titlo : u'Х' ,
    ur'\\Х'        : u'Х',
    hip.cherv_titlo : u'Ч' ,
    ur'\\Ч'         : u'Ч',
    
},
{
    hip.Oy : antconc.CAPITAL_DIGRAPH_UK ,
    hip.oy : antconc.SMALL_DIGRAPH_UK ,

    hip.W : antconc.CAPITAL_OMEGA ,
    hip.w : antconc.SMALL_OMEGA ,
},
{   
    ur'(?<!_)' + hip.Y : antconc.CAPITAL_MONOGRAPH_UK ,
    ur'(?<!_)' + hip.y : antconc.SMALL_MONOGRAPH_UK ,

    u'i'  : u'\u0456',
    u'I'  : u'\u0406',
},
{
    u'_у' : u'у',
    u'#' : u'\u0482', # знак тысячи
},
)
