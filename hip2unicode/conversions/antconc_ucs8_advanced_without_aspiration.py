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

    (SMALL_ON + SMALL_AKUT,                 '0'),
    (SMALL_ZHIVETE + SMALL_TITLO,           '9'),
    (SMALL_AZ + SMALL_GRAVIS,               'A'),
    (SMALL_JATJ + SMALL_CIRKUMFLEKS,        'B'),
    (SMALL_DOBRO + SLOVO_TITLO,             'D'),
    (SMALL_ESTJ + SMALL_GRAVIS,             'E'),
    (SMALL_GLAGOLJ + SMALL_TITLO,           'G'),
    (SMALL_OMEGA + SMALL_AKUT,              'H'),
    (SMALL_I + SMALL_GRAVIS,                'J'),
    (SMALL_LJUDI + DOBRO_TITLO,             'L'),
    (SMALL_RCY + SMALL_TITLO,               'R'),
    (SMALL_JUS_MALYJ + SMALL_GRAVIS,        'S'),
    (SMALL_MONOGRAPH_UK + SMALL_GRAVIS,     'Y'),
    (SMALL_AZ + SMALL_AKUT,                 'a'), # LATIN
    (SMALL_ESTJ + SMALL_AKUT,               'e'), # LATIN
    (SMALL_ERY + SMALL_AKUT,                'h'),
    (SMALL_I + SMALL_AKUT,                  'j'),
    (SMALL_LJUDI + SMALL_TITLO,             'l'),
    (SMALL_RCY + SLOVO_TITLO,               'r'),
    (SMALL_JUS_MALYJ + SMALL_AKUT,          's'),
    (SMALL_MONOGRAPH_UK + SMALL_AKUT,       'y'), # LATIN
    (SMALL_MONOGRAPH_UK + SMALL_CIRKUMFLEKS,'{'),
    (SMALL_IZHE + SMALL_TITLO,              '}'),
    (SMALL_IZHICA + SMALL_AKUT,             '\u0402'),
    (SMALL_KSI + SMALL_TITLO,               '\u2026'),
    (SMALL_AZ + SMALL_CIRKUMFLEKS,          '\u2020'),
    (SMALL_I + SMALL_CIRKUMFLEKS,           '\u2021'),
    (SMALL_JUS_MALYJ + SMALL_CIRKUMFLEKS,   '\u2030'),
    (SMALL_I + SMALL_TITLO,                 '\u2039'),
    (SMALL_IZHICA + GLAGOLJ_TITLO,          '\u0452'),
    (SMALL_TVERDO + SMALL_TITLO,            '\u2122'),
    (SMALL_IZHICA + SMALL_CIRKUMFLEKS,      '\u203A'),
    (SMALL_XER + SMALL_TITLO,               '\u00A6'),
    (SMALL_CHERVJ + SMALL_TITLO,            '\u00A7'),
    (SMALL_JATJ + SMALL_GRAVIS,             'Ё'),
    (SMALL_SLOVO + SMALL_TITLO,             '\u00a9'),
    (SMALL_RCY + DOBRO_TITLO,               '\u00ae'),
    (SMALL_JATJ + SMALL_AKUT,               'ё'),
    (SMALL_AZ + SMALL_TITLO,                '№'),

)
