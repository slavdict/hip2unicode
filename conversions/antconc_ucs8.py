# -*- coding: UTF-8 -*-

"""
AntConc to UCS8 conversion

AntConc encoding is specialized ad-hoc
unicode + UTF-8 based encoding designed
for use in AntConc concordancer program
while working with Old Church Slavonic
texts corpus.

"""
from hip2unicode.hip2unicode.representations.antconc import *

conversion = (

    (u'%s%s' % (SMALL_LETTER, AKUT),      u'1'),
    (u'%s%s' % (SMALL_LETTER, GRAVIS),    u'2'),
    (u'%s%s' % (INITIAL_SMALL_VOWEL, u'%s%s' %  #TODO),



    (CAPITAL_FITA,          u'F'),
    (CAPITAL_I,             u'I'),
    (CAPITAL_WIDE_ON,       u'O'),
    (CAPITAL_PSI,           u'P'),
    (CAPITAL_OLE,           u'Q'),
    (CAPITAL_OT,            u'T'),
    (CAPITAL_DIGRAPH_UK,    u'U'),
    (CAPITAL_IZHICA,        u'V'),
    (CAPITAL_OMEGA,         u'W'),
    (CAPITAL_KSI,           u'X'),
    (CAPITAL_JUS_MALYJ,     u'Z'),

    (SMALL_FITA,            u'f'),
    (SMALL_I,               u'i'),
    (SMALL_WIDE_ON,         u'o'),
    (SMALL_PSI,             u'p'),
    (SMALL_OLE,             u'q'),
    (SMALL_OT,              u't'),
    (SMALL_DIGRAPH_UK,      u'u'),
    (SMALL_IZHICA,          u'v'),
    (SMALL_OMEGA,           u'w'),
    (SMALL_KSI,             u'x'),
    (SMALL_JUS_MALYJ,       u'z'),

    (SMALL_UK,              u'\u00B5'),

    (CAPITAL_MONOGRAPH_UK,  u'У'),
    (CAPITAL_JATJ,          u'Э'),
    (CAPITAL_I_AZ,          u'Я'),

    (SMALL_MONOGRAPH_UK,    u'у'),
    (SMALL_JATJ,            u'э'),
    (SMALL_I_AZ,            u'я'),

)

"""
конвертация не требуется для 8-битных диапазонов:

...
C0-D2, D4-DC, DE,
E0-F2, F4-FC, FE

"""
