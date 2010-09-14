# -*- coding: UTF-8 -*-

"""
AntConc to UCS8 conversion

AntConc encoding is specialized ad-hoc
unicode + UTF-8 based encoding designed
for use in AntConc concordancer program
while working with Old Church Slavonic
texts corpus.

"""
from hip2unicode.representations.RE import *
from hip2unicode.representations.ucs8 import *

conversion = (

    (SMALL_ON + SMALL_AKUT,                 u'0'),
    (SMALL_ZHIVETE + SMALL_TITLO,           u'9'),
    (SMALL_AZ + SMALL_GRAVIS,               u'A'),
    (SMALL_JATJ + SMALL_CIRKUMFLEKS,        u'B'),
    (SMALL_DOBRO + SLOVO_TITLO,             u'D'),
    (SMALL_ESTJ + SMALL_GRAVIS,             u'E'),
    (SMALL_GLAGOLJ + SMALL_TITLO,           u'G'),
    (SMALL_OMEGA + SMALL_AKUT,              u'H'),
    (SMALL_I + SMALL_GRAVIS,                u'J'),
    (SMALL_LJUDI + DOBRO_TITLO,             u'L'),
    (SMALL_RCY + SMALL_TITLO,               u'R'),
    (SMALL_JUS_MALYJ + SMALL_GRAVIS,        u'S'),
    (SMALL_MONOGRAPH_UK + SMALL_GRAVIS,     u'Y'),
    (SMALL_AZ + SMALL_AKUT,                 u'a'), # LATIN
    (SMALL_ESTJ + SMALL_AKUT,               u'e'), # LATIN
    (SMALL_ERY + SMALL_AKUT,                u'h'),
    (SMALL_I + SMALL_AKUT,                  u'j'),
    (SMALL_LJUDI + SMALL_TITLO,             u'l'),
    (SMALL_RCY + SLOVO_TITLO,               u'r'),
    (SMALL_JUS_MALYJ + SMALL_AKUT,          u's'),
    (SMALL_MONOGRAPH_UK + SMALL_AKUT,       u'y'), # LATIN
    (SMALL_MONOGRAPH_UK + SMALL_CIRKUMFLEKS,u'{'),
    (SMALL_IZHE + SMALL_TITLO,              u'}'),
    (SMALL_IZHICA + SMALL_AKUT,             u'\u0402'),
    (SMALL_KSI + SMALL_TITLO,               u'\u2026'),
    (SMALL_AZ + SMALL_CIRKUMFLEKS,          u'\u2020'),
    (SMALL_I + SMALL_CIRKUMFLEKS,           u'\u2021'),
    (SMALL_JUS_MALYJ + SMALL_CIRKUMFLEKS,   u'\u2030'),
    (SMALL_I + SMALL_TITLO,                 u'\u2039'),
    (SMALL_IZHICA + GLAGOLJ_TITLO,          u'\u0452'),
    (SMALL_TVERDO + SMALL_TITLO,            u'\u2122'),
    (SMALL_IZHICA + SMALL_CIRKUMFLEKS,      u'\u203A'),
    (SMALL_XER + SMALL_TITLO,               u'\u00A6'),
    (SMALL_CHERVJ + SMALL_TITLO,            u'\u00A7'),
    (SMALL_JATJ + SMALL_GRAVIS,             u'Ё'),
    (SMALL_SLOVO + SMALL_TITLO,             u'\u00a9'),
    (SMALL_RCY + DOBRO_TITLO,               u'\u00ae'),
    (SMALL_JATJ + SMALL_AKUT,               u'ё'),
    (SMALL_AZ + SMALL_TITLO,                u'№'),

)
