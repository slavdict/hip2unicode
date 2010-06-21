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


REPR_ENVIRON.NON_LETTERS = neg_token( LETTERS )

lc_SMALL_LETTERS    = left_context( token( SMALL_LETTERS ) )
lc_CAPITAL_LETTERS  = left_context( token( CAPITAL_LETTERS ) )
lc_LETTERS          = left_context( token( LETTERS ) )
ic_SMALL_VOWELS     = initial_context( token( SMALL_VOWELS ) )
ic_CAPITAL_VOWELS   = initial_context( token( CAPITAL_VOWELS ) )
nrc_ACCENTS         = neg_right_context( token( ACCENTS ) )

conversion = (
    
    (SMALL_JUS_MALYJ + SMALL_ASPIRATION_CIRKUMFLEX, u'\|'), # RegExp escaped pipe sign
    (CAPITAL_AZ + CAPITAL_ASPIRATION_AKUT,          u'\u0403'),
    (SMALL_AZ + SMALL_ASPIRATION_AKUT,              u'\u0453'),
    (CAPITAL_DIGRAPH_UK + CAPITAL_ASPIRATION_AKUT,  u'\u040C'),
    (CAPITAL_I_AZ + CAPITAL_ASPIRATION_AKUT,        u'\u040B'),
    (CAPITAL_WIDE_ON + CAPITAL_ASPIRATION_AKUT,     u'\u040F'),
    (SMALL_DIGRAPH_UK + SMALL_ASPIRATION_AKUT,      u'\u045C'),
    (SMALL_I_AZ + SMALL_ASPIRATION_AKUT,            u'\u045B'),
    (SMALL_WIDE_ON + SMALL_ASPIRATION_AKUT,         u'\u045F'),
    (CAPITAL_I + CAPITAL_ASPIRATION_AKUT,           u'\u0408'),
    (SMALL_I + SMALL_ASPIRATION_AKUT,               u'\u0458'),
    (SMALL_I_AZ + SMALL_ASPIRATION_CIRKUMFLEX,      u'\u00B1'),

    (SMALL_ON + SMALL_AKUT,                 u'0'),
    (SMALL_ZHIVETE + SMALL_TITLO,           u'9'),
    (SMALL_AZ + SMALL_GRAVIS,               u'A'),
    (SMALL_JATJ + SMALL_CIRKUMFLEKS,        u'B'),
    (SMALL_DOBRO + SLOVO_TITLO,             u'D'),
    (SMALL_ESTJ + SMALL_GRAVIS,             u'E'),
    (SMALL_GLAGOLJ + SMALL_TITLO,           u'G'),
    (SMALL_OMEGA + SMALL_AKUT,              u'H'),
    (SMALL_I + SMALL_GRAVIS,                u'J'),
    (CAPITAL_I_AZ + SMALL_ASPIRATION,       u'K'),
    (SMALL_LJUDI + DOBRO_TITLO,             u'L'),
    (CAPITAL_WIDE_ON + CAPITAL_ASPIRATION,  u'N'),
    (SMALL_RCY + SMALL_TITLO,               u'R'),
    (SMALL_JUS_MALYJ + SMALL_GRAVIS,        u'S'),
    (SMALL_MONOGRAPH_UK + SMALL_GRAVIS,     u'Y'),
    (SMALL_AZ + SMALL_AKUT,                 u'a'), # LATIN
    (SMALL_ESTJ + SMALL_AKUT,               u'e'), # LATIN
    (SMALL_ERY + SMALL_AKUT,                u'h'),
    (SMALL_I + SMALL_AKUT,                  u'j'),
    (SMALL_I_AZ + SMALL_ASPIRATION,         u'k'),
    (SMALL_LJUDI + SMALL_TITLO,             u'l'),
    (SMALL_WIDE_ON + SMALL_ASPIRATION,      u'n'),
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

)
