#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" Variable (attributes) names are all in Latin """

A = ur'[AА]' # \u0041 + \u0410 (latin A + cyrillic A)
a = ur'[aа]' # \u0061 + \u0430

B = ur'[BВ]' # \u0042 + \u0412 (latin B + cyrillic VE)
b = ur'[bв]'

E = ur'[EЕ]'
e = ur'[eе]'

F = u'F'
f = u'f'

Wide_E = ur'(?:_%(E)s|<%(E)s>)' % {'E': E}
wide_e = ur'(?:_%(e)s|<%(e)s>)' % {'e': e}

i_without_dot = ur'_i'

K = ur'[KК]'
k = ur'[kк]'

M = ur'[MМ]'
m = ur'[mм]'

H = ur'[HН]'
h = ur'[hн]'

O = ur'[OО]'
o = ur'[oо]'

Wide_O = ur'(?:_%(O)s|<%(O)s>)' % {'O': O } # ur'(?: _О | <О> )'
wide_o = ur'(?:_%(o)s|<%(o)s>)' % {'o': o } # ur'(?: _о | <о> )'

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

Yat = ur'(?:JЬ|Jь)'
yat = ur'jь'

Ksi = ur'(?:_%(KC)s|_%(Kc)s|<%(KC)s>|<%(Kc)s>)' % { 'KC': K + C, 'Kc': K + c } # Ksi = ur'(?:_КС|_Кс|<КС>|<Кс>)'
ksi = ur'(?:_%(kc)s|<%(kc)s>)' % { 'kc': k + c } # ur'(?:_кс|<кс>)'

Ole = ur'(?:_W|<W>)'
ole = ur'(?:_w|<w>)'

Ot = ur'W\\т'
ot = ur'w\\т'

Psi = ur'(?:_П%(C)s|_П%(c)s|<П%(C)s>|<П%(c)s>)' % { 'C': C, 'c': c } # Ksi = ur'(?:_ПС|_Пс|<ПС>|<Пс>)'
psi = ur'(?:_п%(c)s|<п%(c)s>)' % { 'c': c } # ur'(?: _пс | <пс> )'

Oy = ur'(?:%(O)s_%(Y)s|%(O)s_%(y)s|<%(O)s_%(Y)s>|<%(O)s_%(y)s>)' % { 'O': O, 'Y': Y, 'y': y }
oy = ur'(?:%(o)s_%(y)s|<%(o)s_%(y)s>)' % { 'o': o, 'y': y }

J_a = ur'(?:J%(A)s|J%(a)s)' % { 'A': A, 'a': a }
j_a = ur'(?:j%(a)s)' % { 'a': a }

Ja = u'Я'
ja = u'я'

single_quote = u"'"
back_single_quote = u'`'
equal_sign = u'='
caret = ur'\^' # ^
tilde = u'~'

paerok = ur'\\ъ'
vedi_titlo = ur'\\в'
glagol_titlo = ur'\\г'
dobro_titlo = ur'\\д'
on_titlo = ur'\\о'
rcy_titlo = ur'\\р'
slovo_titlo = ur'\\с'
kher_titlo = ur'\\х'
cherv_titlo = ur'\\ч'


