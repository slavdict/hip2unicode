from hip2unicode.representations import hip
from hip2unicode.representations import cslav

hip2cslav = (
# hip-нормализация
# ...
# удаление ненужной разметки
{   # киноварь
    r'%<':   '',
    r'%>':   '',

    r'%\(':  '',
    r'%\)':  '',

    r'%\[':  '',
    r'%\]':  '',
},
{
    r'\([cсCС]\.\ *\d+\)':  '',
},
{   # сноски
    # <сноска 1> ::= *{  <текст сноски> *  <текст сноски> }
    r' \*{ .*? \* .*? } ': '',
    # <сноска 2> ::= **{ <текст сноски> ** <текст сноски> }
    r''' \*\*{ .*?  \*\* .*?} ''' : ''
},
{   # звездочки для поющих на клиросе
    r'\*': '',
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

    hip.equal_sign : cslav.aspiration ,
    hip.single_quote : cslav.acute ,
    hip.back_single_quote : cslav.gravis ,
    hip.caret : cslav.circumflex ,
    hip.tilde : cslav.titlo ,

    hip.paerok : cslav.paerok ,
    hip.vedi_titlo : cslav.vedi_titlo ,
    hip.glagol_titlo : cslav.glagol_titlo ,
    hip.dobro_titlo : cslav.dobro_titlo ,
    hip.on_titlo : cslav.on_titlo ,
    hip.rcy_titlo : cslav.rcy_titlo ,
    hip.slovo_titlo : cslav.slovo_titlo ,
    hip.kher_titlo : cslav.kher_titlo ,
    hip.cherv_titlo : cslav.cherv_titlo ,
},
{
    hip.Oy : cslav.Oy ,
    hip.oy : cslav.oy ,
},
{
    hip.Y : cslav.Uk ,
    hip.y : cslav.uk ,

    hip.i_without_dot : '\u0131', # U+0131 LATIN SMALL LETTER DOTLESS I
},
)
