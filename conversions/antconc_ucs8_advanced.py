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

)
