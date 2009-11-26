# -*- coding: UTF-8 -*-

from hip2unicode.representations import hip
from hip2unicode.representations import cslav

hip2hipcslav = (
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

{
    
    # Regular expressions for character replacement
    # in text marked as being typed in Church Slavonic script
    # (script tag <::слав> or without any script tag
    # if no script tag is in the document)
    hip.A : cslav.Az ,
    hip.a : cslav.az ,
 
    hip.B : cslav.Vedi ,
    hip.b : cslav.vedi ,

    hip.E : cslav.Est ,
    hip.e : cslav.est ,

    hip.K : cslav.Kako ,
    hip.k : cslav.kako ,

    hip.M : cslav.Myslete ,
    hip.m : cslav.myslete ,

    hip.H : cslav.Nash ,
    hip.h : cslav.nash ,
    
    hip.O : cslav.On ,
    hip.o : cslav.on ,

    hip.P : cslav.Rcy ,
    hip.p : cslav.rcy ,

    hip.C : cslav.Slovo ,
    hip.c : cslav.slovo ,

    hip.T : cslav.Tverdo ,
    hip.t : cslav.tverdo ,

    hip.X : cslav.Kher ,
    hip.x : cslav.kher ,

    hip.V_double_gravis : cslav.Izhica_double_gravis ,
    hip.v_double_gravis : cslav.izhica_double_gravis ,
},
{
    hip.Wide_E : cslav.Wide_E ,
    hip.wide_e : cslav.wide_e ,

    hip.Yat : cslav.Yat ,
    hip.yat : cslav.yat ,

    hip.V : cslav.Izhica ,
    hip.v : cslav.izhica ,

    hip.Ksi : cslav.Ksi ,
    hip.ksi : cslav.ksi ,

    hip.Wide_O : cslav.Wide_O ,
    hip.wide_o : cslav.wide_o ,

    hip.W : cslav.Omega ,
    hip.w : cslav.omega ,

    hip.Ole : cslav.Ole ,
    hip.ole : cslav.ole ,

    hip.Ot : cslav.Ot ,
    hip.ot : cslav.ot ,

    hip.Psi : cslav.Psi ,
    hip.psi : cslav.psi ,

    hip.F : cslav.Fita ,
    hip.f : cslav.fita ,

    hip.J_a : cslav.Ja ,
    hip.j_a : cslav.ja ,

    hip.Ja : cslav.Small_Yus ,
    hip.ja : cslav.small_yus ,

    hip.equal_sign : ur'’' , # U+2019 RIGHT SINGLE QUOTATION MARK : single comma quotation mark
#    hip.single_quote : cslav.acute ,
#    hip.back_single_quote : cslav.gravis ,
#    hip.caret : cslav.circumflex ,
#    hip.tilde : cslav.titlo ,

    hip.paerok : cslav.paerok ,
    hip.vedi_titlo : ur'В' ,
    hip.glagol_titlo : ur'Г' ,
    hip.dobro_titlo : ur'Д' ,
    hip.on_titlo : ur'О' ,
    hip.rcy_titlo : ur'Р' ,
    hip.slovo_titlo : ur'С' ,
    hip.kher_titlo : ur'Х' ,
    hip.cherv_titlo : ur'Ч' ,
    
},
{
    hip.Oy : cslav.Oy ,
    hip.oy : cslav.oy ,
},
{   
    hip.Y : cslav.Uk ,
    hip.y : cslav.uk ,
},
)
