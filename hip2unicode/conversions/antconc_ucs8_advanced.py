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
    (SMALL_JUS_MALYJ + SMALL_ASPIRATION_CIRKUMFLEX, '|'),
    (CAPITAL_AZ + CAPITAL_ASPIRATION_AKUT,          '\u0403'),
    (SMALL_AZ + SMALL_ASPIRATION_AKUT,              '\u0453'),
    (CAPITAL_DIGRAPH_UK + CAPITAL_ASPIRATION_AKUT,  '\u040C'),
    (CAPITAL_DIGRAPH_UK + SMALL_ASPIRATION_AKUT,    '\u040C'),
    (CAPITAL_I_AZ + CAPITAL_ASPIRATION_AKUT,        '\u040B'),
    (CAPITAL_WIDE_ON + CAPITAL_ASPIRATION_AKUT,     '\u040F'),
    (SMALL_DIGRAPH_UK + SMALL_ASPIRATION_AKUT,      '\u045C'),
    (SMALL_I_AZ + SMALL_ASPIRATION_AKUT,            '\u045B'),
    (SMALL_WIDE_ON + SMALL_ASPIRATION_AKUT,         '\u045F'),
    (CAPITAL_I + CAPITAL_ASPIRATION_AKUT,           '\u0408'),
    (SMALL_I + SMALL_ASPIRATION_AKUT,               '\u0458'),
    (SMALL_I_AZ + SMALL_ASPIRATION_CIRKUMFLEX,      '\u00B1'),

    (SMALL_ON + SMALL_AKUT,                 '0'),
    (SMALL_ZHIVETE + SMALL_TITLO,           '9'),
    (SMALL_AZ + SMALL_GRAVIS,               'A'),
    (SMALL_JATJ + SMALL_CIRKUMFLEKS,        'B'),
    (SMALL_DOBRO + SLOVO_TITLO,             'D'),
    (SMALL_ESTJ + SMALL_GRAVIS,             'E'),
    (SMALL_GLAGOLJ + SMALL_TITLO,           'G'),
    (SMALL_OMEGA + SMALL_AKUT,              'H'),
    (SMALL_I + SMALL_GRAVIS,                'J'),
    (CAPITAL_I_AZ + SMALL_ASPIRATION,       'K'),
    (SMALL_LJUDI + DOBRO_TITLO,             'L'),
    (CAPITAL_WIDE_ON + CAPITAL_ASPIRATION,  'N'),
    (SMALL_RCY + SMALL_TITLO,               'R'),
    (SMALL_JUS_MALYJ + SMALL_GRAVIS,        'S'),
    (SMALL_MONOGRAPH_UK + SMALL_GRAVIS,     'Y'),
    (SMALL_AZ + SMALL_AKUT,                 'a'), # LATIN
    (SMALL_ESTJ + SMALL_AKUT,               'e'), # LATIN
    (SMALL_ERY + SMALL_AKUT,                'h'),
    (SMALL_I + SMALL_AKUT,                  'j'),
    (SMALL_I_AZ + SMALL_ASPIRATION,         'k'),
    (SMALL_LJUDI + SMALL_TITLO,             'l'),
    (SMALL_WIDE_ON + SMALL_ASPIRATION,      'n'),
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
    (CAPITAL_JUS_MALYJ + CAPITAL_ASPIRATION,'\u0409'),
    (SMALL_I + SMALL_TITLO,                 '\u2039'),
    (CAPITAL_OMEGA + CAPITAL_ASPIRATION,    '\u040A'),
    (SMALL_IZHICA + GLAGOLJ_TITLO,          '\u0452'),
    (SMALL_TVERDO + SMALL_TITLO,            '\u2122'),
    (SMALL_JUS_MALYJ + SMALL_ASPIRATION,    '\u0459'),
    (SMALL_IZHICA + SMALL_CIRKUMFLEKS,      '\u203A'),
    (SMALL_OMEGA + SMALL_ASPIRATION,        '\u045A'),
    (CAPITAL_DIGRAPH_UK + CAPITAL_ASPIRATION,   '\u040E'),
    (CAPITAL_DIGRAPH_UK + SMALL_ASPIRATION, '\u040E'),
    (SMALL_DIGRAPH_UK + SMALL_ASPIRATION,   '\u045E'),
    (CAPITAL_AZ + CAPITAL_ASPIRATION,       '\u0490'),
    (SMALL_XER + SMALL_TITLO,               '\u00A6'),
    (SMALL_CHERVJ + SMALL_TITLO,            '\u00A7'),
    (SMALL_JATJ + SMALL_GRAVIS,             'Ё'),
    (SMALL_SLOVO + SMALL_TITLO,             '\u00a9'),
    (SMALL_RCY + DOBRO_TITLO,               '\u00ae'),
    (CAPITAL_I + CAPITAL_ASPIRATION,        '\u0407'),
    (SMALL_AZ + SMALL_ASPIRATION,           '\u0491'),
    (SMALL_JATJ + SMALL_AKUT,               'ё'),
    (SMALL_AZ + SMALL_TITLO,                '№'),
    (SMALL_I + SMALL_ASPIRATION,            '\u0457'),
)
