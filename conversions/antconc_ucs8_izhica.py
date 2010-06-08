# -*- coding: UTF-8 -*-

"""
Данное промежуточное преобразование ориентировано 
на церковно-славянскую орфографию с чётким противопоставлением 
"согласной" и "гласной" ижиц. 

Имеется в виду те случаи, когда над ижицей 
в значении "в" не ставится ничего, 
а над ижицей в значении "и" обязательно ставится 
какой-нибудь диакритический знак 
(в том числе придыхание в начале слова 
или двойной гравис при безударной позиции 
внутри слова).
"""
from hip2unicode.representations.RE import *
from hip2unicode.representations.ucs8 import *

# REPR_ENVIRON.NON_LETTERS = neg_token( LETTERS )

nrc_DIACRITICS  = neg_right_context( token( DIACRITICS ) )
nlc_AE          = neg_left_context( token( AE ) )
nlc_AE_DIA      = neg_left_context( token( AE ), token( VOWEL_DIACRITICS ) )

conversion = (

    (nlc_AE + CAPITAL_IZHICA + nrc_DIACRITICS,      CAPITAL_IZHICA_DOUBLE_GRAVIS),
    (nlc_AE_DIA + CAPITAL_IZHICA + nrc_DIACRITICS,  CAPITAL_IZHICA_DOUBLE_GRAVIS),

    (nlc_AE + SMALL_IZHICA + nrc_DIACRITICS,        SMALL_IZHICA_DOUBLE_GRAVIS),
    (nlc_AE_DIA + SMALL_IZHICA + nrc_DIACRITICS,    SMALL_IZHICA_DOUBLE_GRAVIS),

)
