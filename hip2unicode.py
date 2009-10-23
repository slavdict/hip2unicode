#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class HIP:
    
    """ Variable (attributes) names are all in Latin """

    A = ur'[AА]' # \u0041 + \u0410 (latin A + cyrillic A)
    a = ur'[aа]' # \u0061 + \u0430

    B = ur'[BВ]' # \u0042 + \u0412 (latin B + cyrillic VE)
    b = ur'[bв]'

    E = ur'[EЕ]'
    e = ur'[eе]'

    F = 'F'
    f = 'f'

    Wide_E = ur'(?: _ %(E)s | < %(E)s > )' % {'E': self.E}
    wide_e = ur'(?: _ %(e)s | < %(e)s > )' % {'e': self.e}
    
    K = ur'[KК]'
    k = ur'[kк]'
    
    M = ur'[MМ]'
    m = ur'[mм]'
    
    H = ur'[HН]'
    h = ur'[hн]'
    
    O = ur'[OО]'
    o = ur'[oо]'

    Wide_O = ur'(?: _ %(O)s | < %(O)s > )' % {'O': self.O } # ur'(?: _О | <О> )'
    wide_o = ur'(?: _ %(o)s | < %(o)s > )' % {'o': self.o } # ur'(?: _о | <о> )'
    
    P = ur'[PР]'
    p = ur'[pр]'
    
    C = ur'[CС]'
    c = ur'[cс]'
    
    T = ur'[TТ]'
    t = ur'[tт]'

    V = ur'V'
    v = ur'v'

    V_double_gravis = ur'V"'
    v_double_gravis = ur'v"'

    W = ur'W'
    w = ur'w'

    Y = ur'[YУ]'
    y = ur'[yу]'

    X = ur'[XХ]'
    x = ur'[xх]'

    Yat = ur'(?: JЬ | Jь )'
    yat = ur'jь'

    Ksi = ur'(?: _ %(KC)s | _ %(Kc)s | < %(KC)s > | < %(Kc)s > )' % { 'KC': self.K + self.C, 'Kc': self.K + self.c } # Ksi = ur'(?: _КС | _Кс | <КС> | <Кс> )'
    ksi = ur'(?: _ %(kc)s | < %(kc)s > )' % { 'kc': self.k + self.c } # ur'(?: _кс | <кс> )'

    Ole = ur'(?: _W | <W> )'
    ole = ur'(?: _w | <w> )'

    Ot = ur'W\\т'
    ot = ur'w\\т'

    Psi = ur'(?: _ П %(C)s | _ П %(c)s | < П %(C)s > | < П %(c)s > )' % { 'C': self.C, 'c': self.c } # Ksi = ur'(?: _ПС | _Пс | <ПС> | <Пс> )'
    psi = ur'(?: _ п %(c)s | < п %(c)s > )' % { 'kc': self.c } # ur'(?: _пс | <пс> )'

    Oy = ur'(?: %(O)s _ %(Y)s | %(O)s _ %(y)s | < %(O)s _ %(Y)s > | < %(O)s _ %(y)s > )' % { 'O': self.O, 'Y': self.Y, 'y': self.y }
    oy = ur'(?: %(o)s _ %(y)s | < %(o)s _ %(y)s > )' % { 'o': self.o, 'y': self.y }

    J_a = ur'(?: J %(A)s | J %(a)s )' % { 'A': self.A, 'a': self.a }
    j_a = ur'(?: j %(a)s )' % { 'a': self.a }

    Ja = u'Я'
    ja = u'я'

    single_quote = "'"
    back_single_quote = '`'
    equal_sign = '='
    caret = '^'
    tilde = '~'

    paerok = ur'\\ъ'
    vedi_titlo = ur'\\в'
    glagol_titlo = ur'\\г'
    dobro_titlo = ur'\\д'
    on_titlo = ur'\\о'
    rcy_titlo = ur'\\р'
    slovo_titlo = ur'\\с'
    kher_titlo = ur'\\х'
    cherv_titlo = ur'\\ч'


class CSlav:

    """ Variable (attributes) names are all in Latin """

    Az = u'А'
    az = u'а'
 
    Vedi = u'В'
    vedi = u'в'

    Est = u'Е'
    est = u'е'

    Wide_E = self.Est # NB: \u0415 is used instead \u0404, 
                      # because there is no difference 
                      # between normal and wide capital E
    wide_e = u'є'    # \u0454
    
    Kako = u'К'
    kako = u'к'
    
    Myslete = u'М'
    myslete = u'м'
    
    Nash = u'Н'
    nash = u'н'
    
    On = u'О'
    on = u'о'
    
    Rcy = u'Р'
    rcy = u'р'
    
    Slovo = u'С',
    slovo = u'с',
    
    Tverdo = u'Т'
    tverdo = u'т'

    Uk = u'У' # \u0423 [NB: it is possible to use \uA64A (monograph Uk) instead]
    uk = u'у' # \u0443 [NB: it is possible to use \uA64B (monograph uk) instead]

    Kher = u'Х'
    kher = u'х'

    Yat = u'\u0462'
    yat = u'\u0463'

    Izhica = u'\u0474'
    izhica = u'\u0475'

    Izhica_double_gravis = u'\u0476'
    izhica_double_gravis = u'\u0477'

    Ksi = u'\u046E'
    ksi = u'\u046F'

    Wide_O = u'\u047A'
    wide_o = u'\u047B'

    Omega = u'\u0460'
    omega = u'\u0461'

    Ole = u'\u047C'
    ole = u'\u047D'

    Ot = u'\u047E'
    ot = u'\u047F'

    Psi = u'\u0470'
    psi = u'\u0471'
    
    Oy = u'\u0478'
    oy = u'\u0479'

    Fita = u'\u0472'
    fita = u'\u0473'

    Ja = u'\uA656'
    ja = u'\uA657'

    Small_Yus = u'\u0466'
    small_yus = u'\u0467'
   
    # Diacritics
    aspiration = u'\u0486'
    acute = u'\u0301'   # U+0301 combining acute accent
    gravis = u'\u0300'
    circumflex = u'\u0311'  # U+0311 COMBINING INVERTED BREVE
                            # NB: There is also U+0302 COMBINING CIRCUMFLEX ACCENT
    titlo = u'\u0483' 
    paerok = u'\uA67F'  # U+A67F CYRILLIC PAYEROK
                        # NB: there is also U+A67D COMBINING CYRILLIC PAYEROK

    vedi_titlo      = u'\u2DE1'
    glagol_titlo    = u'\u2DE2'
    dobro_titlo     = u'\u2DE3'
    on_titlo        = u'\u2DEA'
    rcy_titlo       = u'\u2DEC'
    slovo_titlo     = u'\u2DED'
    kher_titlo      = u'\u2DEF'
    cherv_titlo     = u'\u2DF1'


cslav_regexps = {
    
    """ Regular expressions for character replacement
    in text marked as being typed in Church Slavonic script
    (script tag <::слав> or without any script tag
    if no script tag is in the document) """

    HIP.A : CSlav.Az ,
    HIP.a : CSlav.az ,
 
    HIP.B : CSlav.Vedi ,
    HIP.b : CSlav.vedi ,

    HIP.E : CSlav.Est ,
    HIP.e : CSlav.est ,

    HIP.K : CSlav.Kako ,
    HIP.k : CSlav.kako ,

    HIP.M : CSlav.Myslete ,
    HIP.m : CSlav.myslete ,

    HIP.N : CSlav.Nash ,
    HIP.n : CSlav.nash ,
    
    HIP.O : CSlav.On ,
    HIP.o : CSlav.on ,

    HIP.P : CSlav.Rcy ,
    HIP.p : CSlav.rcy ,

    HIP.C : CSlav.Slovo ,
    HIP.c : CSlav.slovo ,

    HIP.T : CSlav.Tverdo ,
    HIP.t : CSlav.tverdo ,

    HIP.Y : CSlav.Uk ,
    HIP.y : CSlav.uk ,

    HIP.X : CSlav.Kher ,
    HIP.x : CSlav.kher ,

    HIP.Wide_E : CSlav.Wide_E ,
    HIP.wide_e : CSlav.wide_e ,

    HIP.Yat : CSlav.Yat ,
    HIP.yat : CSlav.yat ,

    HIP.V : CSlav.Izhica ,
    HIP.v : CSlav.izhica ,

    HIP.Ksi : CSlav.Ksi ,
    HIP.ksi : CSlav.ksi ,

    HIP.Wide_O : CSlav.Wide_O ,
    HIP.wide_o : CSlav.wide_o ,

    HIP.Omega : CSlav.Omega ,
    HIP.omega : CSlav.omega ,

    HIP.Ole : CSlav.Ole ,
    HIP.ole : CSlav.ole ,

    HIP.Ot : CSlav.Ot ,
    HIP.ot : CSlav.ot ,

    HIP.Psi : CSlav.Psi ,
    HIP.psi : CSlav.psi ,

    HIP.Oy : CSlav.Oy ,
    HIP.oy : CSlav.oy ,

    HIP.F : CSlav.Fita ,
    HIP.f : CSlav.fita ,

    HIP.J_a : CSlav.Ja ,
    HIP.j_a : CSlav.ja ,

    HIP.Ja : CSlav.Small_Yus ,
    HIP.ja : CSlav.small_yus ,

    HIP.V_double_gravis : CSlav.Izhica_double_gravis ,
    HIP.v_double_gravis : CSlav.izhica_double_gravis ,

    HIP.equal_sign : CSlav.aspiration ,
    HIP.single_quote : CSlav.acute ,
    HIP.back_single_quote : CSlav.gravis ,
    HIP.caret : CSlav.circumflex ,
    HIP.tilde : CSlav.titlo ,

    HIP.paerok : CSlav.paerok ,
    HIP.vedi_titlo : CSlav.vedi_titlo ,
    HIP.glagol_titlo : CSlav.glagol_titlo ,
    HIP.dobro_titlo : CSlav.dobro_titlo ,
    HIP.on_titlo : CSlav.on_titlo ,
    HIP.rcy_titlo : CSlav.rcy_titlo ,
    HIP.slovo_titlo : CSlav.slovo_titlo ,
    HIP.kher_titlo : CSlav.kher_titlo ,
    HIP.cherv_titlo : CSlav.cherv_titlo ,
    
}

def hip2unicode(str):
    
    """ Преобразует символы, 
    закодированные HIP, в Unicode """

    # глобальные тэги переключения систем письма
    script_tags = (
        u'<::слав>',
        u'<::греч>',
        u'<::рус>',
        u'<::лат>',
        u'<::глаг>',
    )
    
    # разбиваем текст на части по глобальным 
    # тэгам указания письменности
    marked_text_fragments = [(u'<::слав>', str),] # по умолчанию предполагаем, что передаваемая строка представляет собой текст на церковно-славянском/старославянском языке
    for tag in script_tags:
        for fragment_tag, fragment in enumerate(marked_text_fragments):
            new_fragments = fragment.split(tag)
            new_marked_fragments = [(tag, new_fragments[0]),]
            new_marked_fragments.extend(
                [ (fragment_tag, f) for f in new_fragments[1:] ]
            )
            


    return unicode_str
