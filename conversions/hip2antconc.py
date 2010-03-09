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
    ur''' \*\*{ .*?  \*\* .*?} ''' : u''
},

{   # звездочки для поющих на клиросе
    ur'\*': u'',
},
{
    
    # Regular expressions for character replacement
    # in text marked as being typed in Church Slavonic script
    # (script tag <::слав> or without any script tag
    # if no script tag is in the document)
    hip.A : antconc.Az ,
    hip.a : antconc.az ,
 
    hip.B : antconc.Vedi ,
    hip.b : antconc.vedi ,

    hip.E : antconc.Est ,
    hip.e : antconc.est ,

    u's'  : u'\u0455',
    u'S'  : u'\u0405',
    hip.i_without_dot : ur'\u0131', # U+0131 LATIN SMALL LETTER DOTLESS I

    hip.K : antconc.Kako ,
    hip.k : antconc.kako ,

    hip.M : antconc.Myslete ,
    hip.m : antconc.myslete ,

    hip.H : antconc.Nash ,
    hip.h : antconc.nash ,
    
    hip.O : antconc.On ,
    hip.o : antconc.on ,

    hip.P : antconc.Rcy ,
    hip.p : antconc.rcy ,

    hip.C : antconc.Slovo ,
    hip.c : antconc.slovo ,

    hip.T : antconc.Tverdo ,
    hip.t : antconc.tverdo ,

    hip.X : antconc.Kher ,
    hip.x : antconc.kher ,

    hip.V_double_gravis : antconc.Izhica,
    hip.v_double_gravis : antconc.izhica,

    hip.Ole : antconc.Ole ,
    hip.ole : antconc.ole ,
},
{
    hip.Wide_E : antconc.Wide_E ,
    hip.wide_e : antconc.wide_e ,

    hip.Yat : antconc.Yat ,
    hip.yat : antconc.yat ,

    hip.V : antconc.Izhica ,
    hip.v : antconc.izhica ,

    hip.Ksi : antconc.Ksi ,
    hip.ksi : antconc.ksi ,

    hip.Wide_O : antconc.Wide_O ,
    hip.wide_o : antconc.wide_o ,

    hip.Ot : antconc.Ot ,
    hip.ot : antconc.ot ,

    hip.Psi : antconc.Psi ,
    hip.psi : antconc.psi ,

    hip.F : antconc.Fita ,
    hip.f : antconc.fita ,

    hip.J_a : antconc.Ja ,
    hip.j_a : antconc.ja ,

    hip.Ja : antconc.Small_Yus ,
    hip.ja : antconc.small_yus ,

    hip.equal_sign : ur'', # ur'’' , # U+2019 RIGHT SINGLE QUOTATION MARK : single comma quotation mark
#    hip.single_quote : antconc.acute ,
#    hip.back_single_quote : antconc.gravis ,
#    hip.caret : antconc.circumflex ,
#    hip.tilde : antconc.titlo ,

    hip.paerok : u'Ъ',
    ur'\\б' : u'Б',
    hip.vedi_titlo : u'В' ,
    hip.glagol_titlo : u'Г' ,
    hip.dobro_titlo : u'Д' ,
    ur'\\к' : u'К',
    ur'\\л' : u'Л',
    hip.on_titlo : u'О' ,
    hip.rcy_titlo : u'Р' ,
    hip.slovo_titlo : u'С' ,
    hip.kher_titlo : u'Х' ,
    hip.cherv_titlo : u'Ч' ,
    
},
{
    hip.Oy : antconc.Oy ,
    hip.oy : antconc.oy ,

    hip.W : antconc.Omega ,
    hip.w : antconc.omega ,
},
{   
    ur'(?<!_)' + hip.Y : antconc.Uk ,
    ur'(?<!_)' + hip.y : antconc.uk ,

    u'i'  : u'\u0456',
    u'I'  : u'\u0406',
},
{
    u'_у' : u'у',

},
)
