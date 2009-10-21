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

    Ot = ur'W\\t' # W\t
    ot = ur'w\\t' # w\t

    Psi = ur'(?: _ П %(C)s | _ П %(c)s | < П %(C)s > | < П %(c)s > )' % { 'C': self.C, 'c': self.c } # Ksi = ur'(?: _ПС | _Пс | <ПС> | <Пс> )'
    psi = ur'(?: _ п %(c)s | < п %(c)s > )' % { 'kc': self.c } # ur'(?: _пс | <пс> )'

    Oy = ur'(?: %(O)s _ %(Y)s | %(O)s _ %(y)s | < %(O)s _ %(Y)s > | < %(O)s _ %(y)s > )' % { 'O': self.O, 'Y': self.Y, 'y': self.y }
    oy = ur'(?: %(o)s _ %(y)s | < %(o)s _ %(y)s > )' % { 'o': self.o, 'y': self.y }

    J_a = ur'(?: J %(A)s | J %(a)s )' % { 'A': self.A, 'a': self.a }
    j_a = ur'(?: j %(a)s )' % { 'a': self.a }

    Ja = u'Я'
    ja = u'я'

class CSlav:

    """ Variable (attributes) names are all in Latin """

    Az = ur'А'
    az = ur'а'
 
    Vedi = ur'В'
    vedi = ur'в'

    Est = ur'Е'
    est = ur'е'

    Wide_E = self.Est # NB: \u0415 is used instead \u0404, 
                      # because there is no difference 
                      # between normal and wide capital E
    wide_e = ur'є'    # \u0454
    
    Kako = ur'К'
    kako = ur'к'
    
    Myslete = ur'М'
    myslete = ur'м'
    
    Nash = ur'Н'
    nash = ur'н'
    
    On = ur'О'
    on = ur'о'
    
    Rcy = ur'Р'
    rcy = ur'р'
    
    Slovo = ur'С',
    slovo = ur'с',
    
    Tverdo = ur'Т'
    tverdo = ur'т'

    Uk = ur'У' # \u0423 [NB: it is possible to use \uA64A (monograph Uk) instead]
    uk = ur'у' # \u0443 [NB: it is possible to use \uA64B (monograph uk) instead]

    Kher = ur'Х'
    kher = ur'х'

    Yat = ur'\u0462'
    yat = ur'\u0463'

    Izhica = ur'\u0474'
    izhica = ur'\u0475'

    Ksi = ur'\u046E'
    ksi = ur'\u046F'

    Wide_O = ur'\u047A'
    wide_o = ur'\u047B'

    Omega = ur'\u0460'
    omega = ur'\u0461'

    Ole = ur'\u047C'
    ole = ur'\u047D'

    Ot = ur'\u047E'
    ot = ur'\u047F'

    Psi = ur'\u0470'
    psi = ur'\u0471'
    
    Oy = ur'\u0478'
    oy = ur'\u0479'

    Fita = ur'\u0472'
    fita = ur'\u0473'

    Ja = ur'\uA656'
    ja = ur'\uA657'

    Small_Yus = ur'\u0466'
    small_yus = ur'\u0467'

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
}

