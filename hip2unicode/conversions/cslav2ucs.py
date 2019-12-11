from hip2unicode.representations import cslav

cslav2ucs = (
{
    # Regular expressions for character replacement
    # in text marked as being typed in Church Slavonic script
    # (script tag <::слав> or without any script tag
    # if no script tag is in the document)

    cslav.Izhica_double_gravis: 'm',
    cslav.izhica_double_gravis: 'M' ,
},
{
    cslav.Wide_E: 'Е' ,
    cslav.wide_e: 'є' ,

    cslav.Yat: 'Э' ,
    cslav.yat: 'э' ,

    cslav.Ksi: 'X' ,
    cslav.ksi: 'x' ,

    cslav.Wide_O : 'O',
    cslav.wide_o: 'o' ,

    cslav.Omega: 'W' ,
    cslav.omega: 'w' ,

    cslav.Ole: 'Q' ,
    cslav.ole: 'q',

    cslav.Ot: 'T' ,
    cslav.ot: 't' ,

    cslav.Psi: 'P' ,
    cslav.psi: 'p' ,

    cslav.Fita: 'F',
    cslav.fita: 'f',

    cslav.Ja: 'Я' ,
    cslav.ja: 'я',

    cslav.Small_Yus: 'Z' ,
    cslav.small_yus: 'z' ,
},
{
    cslav.aspiration + cslav.acute: '4' ,
    cslav.acute + cslav.aspiration: '4' ,
    cslav.aspiration + cslav.gravis: '5' ,
    cslav.gravis + cslav.aspiration: '5' ,
},
{
    cslav.aspiration: '3' ,
    cslav.acute: '1' ,
    cslav.gravis: '2' ,
    cslav.circumflex: '6' ,
    cslav.titlo: '7' ,

    cslav.paerok: '8' ,
    cslav.glagol_titlo: 'g' ,
    cslav.dobro_titlo: 'd' ,
    cslav.on_titlo: 'b' ,
    cslav.rcy_titlo: '>' ,
    cslav.slovo_titlo : 'c',
    cslav.kher_titlo: '<' ,
    cslav.cherv_titlo: '?' ,
},
{
    cslav.Oy: 'U' ,
    cslav.oy: 'u' ,
},
{
    cslav.Uk: 'У' ,
    cslav.uk: 'у' ,

    '\u0131': 'i', # U+0131 LATIN SMALL LETTER DOTLESS I
},
)
