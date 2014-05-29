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
from hip2unicode.representations.antconc import *
from hip2unicode.representations.ucs8 import LETTERS as ucs8_LETTERS

REPR_ENVIRON.NON_LETTERS = neg_token( LETTERS, ucs8_LETTERS )
ASPIRATION_TIP = u'\u4444'

lc_SMALL_LETTERS    = left_context( token( SMALL_LETTERS ) )
lc_CAPITAL_LETTERS  = left_context( token( CAPITAL_LETTERS ) )
ic_SMALL_VOWELS     = initial_context( token( SMALL_VOWELS ) )
ic_CAPITAL_VOWELS   = initial_context( token( CAPITAL_VOWELS ) )
ic_VOWELS_WITHOUT_ASP = initial_context('[=]' + token(SMALL_VOWELS + CAPITAL_VOWELS))
nrc_ACCENTS         = neg_right_context( token( ASPIRATION_TIP + ACCENTS ) )

conversion = (
    # титло над строчными от, ферт и пси
    # преобразуется в обратный слеш
    # (экранированная запись для RegExp)
    (left_context( token( SMALL_OT, SMALL_FERT, SMALL_PSI ) ) + TITLO,  ur'\\'),
    (THOUSAND_SIGN,                     u'\u00A4'), # знак тысячи

    (ic_VOWELS_WITHOUT_ASP + '(?P<symb>.)',  ur'\g<symb>' + ASPIRATION_TIP),
    (ic_SMALL_VOWELS + nrc_ACCENTS,     u'3'), # придыхание
    (ic_SMALL_VOWELS + AKUT,            u'4'), # придыхание и акут
    (ic_SMALL_VOWELS + GRAVIS,          u'5'), # придыхание и гравис
    (ic_CAPITAL_VOWELS + nrc_ACCENTS,   u'#'),
    (ic_CAPITAL_VOWELS + AKUT,          u'$'),
    (ic_CAPITAL_VOWELS + GRAVIS,        u'%'),
    ('[=](?P<symb>.)' + ASPIRATION_TIP, ur'\g<symb>'),
    (ASPIRATION_TIP, u''),

    (lc_SMALL_LETTERS + AKUT,           u'1'), # акут
    (lc_SMALL_LETTERS + GRAVIS,         u'2'), # гравис
    (lc_SMALL_LETTERS + CIRKUMFLEKS,    u'6'), # циркумфлекс
    # Правило для устранения придыхания
    # над теми гласными, которые стоят
    # первыми в слове, но над которыми
    # должны стоять обычные титла
    # (= случай с цифрами):
    (u'3~',                             u'~'),
    (lc_SMALL_LETTERS + TITLO,          u'7'), # титло
    (lc_SMALL_LETTERS + PAEROK,         u'8'),

    (lc_SMALL_LETTERS + XER_TITLO,      u'<'),
    (lc_SMALL_LETTERS + NASH_TITLO,     u'='),
    (lc_SMALL_LETTERS + RCY_TITLO,      u'>'),
    (lc_SMALL_LETTERS + CHERVJ_TITLO,   u'?'),
    (lc_SMALL_LETTERS + VEDI_TITLO,     u'+'),
    (lc_SMALL_LETTERS + ON_TITLO,       u'b'),
    (lc_SMALL_LETTERS + SLOVO_TITLO,    u'c'),
    (lc_SMALL_LETTERS + DOBRO_TITLO,    u'd'),
    (lc_SMALL_LETTERS + GLAGOLJ_TITLO,  u'g'),
    (lc_SMALL_LETTERS + ZEMLJA_TITLO,   u'\u20ac'),
    (lc_SMALL_LETTERS + ZHIVETE_TITLO,  u'\u2022'),

    (lc_CAPITAL_LETTERS + GRAVIS,       u'@'),
    (lc_CAPITAL_LETTERS + TITLO,        u'&'),
    # след. преобразование обязательно должно идти
    # после всех преобразований, где выступает
    # TITLO, т.к. создаётся символ "~"
    (lc_CAPITAL_LETTERS + AKUT,         u'~'),
    (lc_CAPITAL_LETTERS + CIRKUMFLEKS,  u'^'),
    (lc_CAPITAL_LETTERS + PAEROK,       u'_'),

    (lc_CAPITAL_LETTERS + SLOVO_TITLO,  u'C'),


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
    (SMALL_I,               u'i'), # LATIN
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
