# -*- coding: UTF-8 -*-

from hip2unicode.representations import hip
from hip2unicode.representations import antconc, cslav

hip2antconc = (
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
    hip.paerok : antconc.paerok ,
    hip.vedi_titlo : antconc.vedi_titlo ,
    hip.glagol_titlo : antconc.glagolj_titlo ,
    hip.dobro_titlo : antconc.dobro_titlo ,
    hip.on_titlo : antconc.on_titlo ,
    hip.rcy_titlo : antconc.rcy_titlo ,
    hip.slovo_titlo : antconc.slovo_titlo ,
    hip.kher_titlo : antconc.kher_titlo ,
    hip.cherv_titlo : antconc.chervj_titlo ,
    
    hip.Oy : antconc.Uk_digraph ,
    hip.oy : antconc.uk_digraph ,


    hip.Ksi : antconc.Ksi ,
    hip.ksi : antconc.ksi ,

    hip.Wide_O : antconc.On_shirokoe ,
    hip.wide_o : antconc.on_shirokoe ,

    hip.Ot : antconc.Ot ,
    hip.ot : antconc.ot ,

    hip.Psi : antconc.Psi ,
    hip.psi : antconc.psi ,

    hip.J_a : antconc.A_jotirovannoe ,
    hip.j_a : antconc.a_jotirovannoe ,

},
{
    
    # Regular expressions for character replacement
    # in text marked as being typed in Church Slavonic script
    # (script tag <::слав> or without any script tag
    # if no script tag is in the document)
    hip.A : antconc.Az ,
    hip.a : antconc.az ,

    u'Б'  : antconc.Buki,
    u'б'  : antconc.buki,
 
    hip.B : antconc.Vedi ,
    hip.b : antconc.vedi ,

    u'Г'  : antconc.Glagolj,
    u'г'  : antconc.glagolj,

    u'Д'  : antconc.Dobro,
    u'д'  : antconc.dobro,

    u'Ж'  : antconc.Zhivete,
    u'ж'  : antconc.zhivete,
    
    u'З'  : antconc.Zemlja,
    u'з'  : antconc.zemlja,
    u'S'  : antconc.Zelo,
    u's'  : antconc.zelo,

    u'И'  : antconc.Izhe,
    u'и'  : antconc.izhe,
    hip.i_without_dot : antconc.i,

    u'Й'  : antconc.I_kratkoe,
    u'й'  : antconc.i_kratkoe,

    hip.K : antconc.Kako ,
    hip.k : antconc.kako ,

    u'Л'  : antconc.Ljudi,
    u'л'  : antconc.ljudi,

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

    hip.V_double_gravis : antconc.Izhica ,
    hip.v_double_gravis : antconc.izhica ,
},
{
    hip.Wide_E : antconc.Estj_shirokoe ,
    hip.wide_e : antconc.estj_shirokoe ,

    u'I'  : antconc.I,
    u'i'  : antconc.i,

    hip.Yat : antconc.Jatj ,
    hip.yat : antconc.jatj ,

    hip.V : antconc.Izhica ,
    hip.v : antconc.izhica ,

    hip.W : antconc.Omega ,
    hip.w : antconc.omega ,

    hip.Ole : antconc.Ole ,
    hip.ole : antconc.ole ,

    hip.F : antconc.Fita ,
    hip.f : antconc.fita ,

    hip.Ja : antconc.Jus_malyj ,
    hip.ja : antconc.jus_malyj ,

    hip.equal_sign : u'' ,
    hip.single_quote : antconc.udarenie_ostroe ,
    hip.back_single_quote : antconc.udarenie_tupoe ,
    hip.caret : antconc.udarenie_oblechennoe ,
    hip.tilde : antconc.titlo ,
},
{
    hip.E : antconc.Estj ,
    hip.e : antconc.estj ,
},
{   
    hip.Y : antconc.Uk ,
    hip.y : antconc.uk ,

},
)
