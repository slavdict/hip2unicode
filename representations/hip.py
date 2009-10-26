#!/usr/bin/env python
# -*- coding: UTF-8 -*-

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


