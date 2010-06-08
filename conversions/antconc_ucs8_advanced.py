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

    (lc_LETTERS + SMALL_ON + AKUT,          u'0'),
    (SMALL_ZHIVETE + TITLO,                 u'9'),
    (lc_LETTERS + SMALL_AZ + GRAVIS,        u'A'),
    (lc_LETTERS + SMALL_JATJ + CIRKUMFLEKS, u'B'),
    (SMALL_DOBRO + SLOVO_TITLO,             u'D'),
    (lc_LETTERS + SMALL_ESTJ + GRAVIS,      u'E'),
    (SMALL_GLAGOLJ + TITLO,                 u'G'),
    (lc_LETTERS + SMALL_OMEGA + AKUT,       u'H'),
    (lc_LETTERS + SMALL_I + GRAVIS,         u'J'),
    (initial(CAPITAL_I_AZ) + nrc_ACCENTS,   u'K'),
    (SMALL_LJUDI + DOBRO_TITLO,             u'L'),

)
