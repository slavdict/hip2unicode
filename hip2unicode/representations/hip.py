#!/usr/bin/env python
""" Variable (attributes) names are all in Latin """

A = r'[AА]'  # \u0041 + \u0410 (latin A + cyrillic A)
a = r'[aа]'  # \u0061 + \u0430

B = r'[BВ]'  # \u0042 + \u0412 (latin B + cyrillic VE)
b = r'[bв]'

E = r'[EЕ]'
e = r'[eе]'

F = 'F'
f = 'f'

Wide_E = r'(?:_%(E)s|<%(E)s>)' % {'E': E}
wide_e = r'(?:_%(e)s|<%(e)s>)' % {'e': e}

i_without_dot = r'_i'

K = r'[KК]'
k = r'[kк]'

M = r'[MМ]'
m = r'[mм]'

H = r'[HН]'
h = r'[hн]'

O = r'[OО]'
o = r'[oо]'

Wide_O = r'(?:_%(O)s|<%(O)s>)' % {'O': O } # ur'(?: _О | <О> )'
wide_o = r'(?:_%(o)s|<%(o)s>)' % {'o': o } # ur'(?: _о | <о> )'

P = r'[PР]'
p = r'[pр]'

C = r'[CС]'
c = r'[cс]'

T = r'[TТ]'
t = r'[tт]'

V = r'V'
v = r'v'

V_double_gravis = r'V"'
v_double_gravis = r'v"'

W = r'W'
w = r'w'

Y = r'[YУ]'
y = r'[yу]'

X = r'[XХ]'
x = r'[xх]'

Yat = r'(?:JЬ|Jь)'
yat = r'jь'

Ksi = r'(?:_%(KC)s|_%(Kc)s|<%(KC)s>|<%(Kc)s>)' % { 'KC': K + C, 'Kc': K + c } # Ksi = ur'(?:_КС|_Кс|<КС>|<Кс>)'
ksi = r'(?:_%(kc)s|<%(kc)s>)' % { 'kc': k + c } # ur'(?:_кс|<кс>)'

Ole = r'(?:_W|<W>)'
ole = r'(?:_w|<w>)'

Ot = r'W\\[тТ]'
ot = r'w\\[тТ]'

Psi = r'(?:_П%(C)s|_П%(c)s|<П%(C)s>|<П%(c)s>)' % { 'C': C, 'c': c }
# Psi = ur'(?:_ПС|_Пс|<ПС>|<Пс>)'
psi = r'(?:_п%(c)s|<п%(c)s>)' % { 'c': c }
# ur'(?: _пс | <пс> )'

Oy = r'(?:{O}_{Y}|{O}_{y}|<{O}_{Y}>|<{O}_{y}>|{O}<{Y}>|{O}<{y}>)' \
        .format(O=O, Y=Y, y=y)
oy = r'(?:{o}_{y}|<{o}_{y}>|{o}<{y}>)'.format(o=o, y=y)

J_a = r'(?:J%(A)s|J%(a)s)' % { 'A': A, 'a': a }
j_a = r'(?:j%(a)s)' % { 'a': a }

Ja = 'Я'
ja = 'я'

single_quote = "'"
back_single_quote = '`'
equal_sign = '='
caret = r'\^'  # ^
tilde = '~'

paerok = r'\\ъ'
vedi_titlo = r'\\в'
glagol_titlo = r'\\г'
dobro_titlo = r'\\д'
on_titlo = r'\\о'
rcy_titlo = r'\\р'
slovo_titlo = r'\\с'
kher_titlo = r'\\х'
cherv_titlo = r'\\ч'
