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

lc_SMALL_LETTERS    = left_context( token( SMALL_LETTERS ) )
lc_CAPITAL_LETTERS  = left_context( token( CAPITAL_LETTERS ) )

conversion = (
    (CAPITAL_WIDE_ESTJ,                 CAPITAL_ESTJ),

    # титло над строчными от, ферт и пси
    # преобразуется в обратный слеш
    # (экранированная запись для RegExp)
    (left_context( token( SMALL_OT, SMALL_FERT, SMALL_PSI ) ) + TITLO,  r'\\'),
    (THOUSAND_SIGN,                     '\u00A4'), # знак тысячи

    (lc_SMALL_LETTERS + AKUT,           '1'), # акут
    (lc_SMALL_LETTERS + GRAVIS,         '2'), # гравис
    (lc_SMALL_LETTERS + CIRKUMFLEKS,    '6'), # циркумфлекс
    (lc_SMALL_LETTERS + TITLO,          '7'), # титло
    (lc_SMALL_LETTERS + PAEROK,         '8'),

    (lc_SMALL_LETTERS + XER_TITLO,      '<'),
    (lc_SMALL_LETTERS + NASH_TITLO,     '='),
    (lc_SMALL_LETTERS + RCY_TITLO,      '>'),
    (lc_SMALL_LETTERS + CHERVJ_TITLO,   '?'),
    (lc_SMALL_LETTERS + VEDI_TITLO,     '+'),
    (lc_SMALL_LETTERS + ON_TITLO,       'b'),
    (lc_SMALL_LETTERS + SLOVO_TITLO,    'c'),
    (lc_SMALL_LETTERS + DOBRO_TITLO,    'd'),
    (lc_SMALL_LETTERS + GLAGOLJ_TITLO,  'g'),
    (lc_SMALL_LETTERS + ZEMLJA_TITLO,   '\u0088'),
    (lc_SMALL_LETTERS + ZHIVETE_TITLO,  '\u0095'),

    (lc_CAPITAL_LETTERS + GRAVIS,       '@'),
    (lc_CAPITAL_LETTERS + TITLO,        '&'),
    # след. преобразование обязательно должно идти
    # после всех преобразований, где выступает
    # TITLO, т.к. создаётся символ "~"
    (lc_CAPITAL_LETTERS + AKUT,         '~'),
    (lc_CAPITAL_LETTERS + CIRKUMFLEKS,  '^'),
    (lc_CAPITAL_LETTERS + PAEROK,       '_'),

    (lc_CAPITAL_LETTERS + SLOVO_TITLO,  'C'),


    (CAPITAL_FITA,          'F'),
    (CAPITAL_I,             'I'),
    (CAPITAL_WIDE_ON,       'O'),
    (CAPITAL_PSI,           'P'),
    (CAPITAL_OLE,           'Q'),
    (CAPITAL_OT,            'T'),
    (CAPITAL_DIGRAPH_UK,    'U'),
    (CAPITAL_IZHICA,        'V'),
    (CAPITAL_OMEGA,         'W'),
    (CAPITAL_KSI,           'X'),
    (CAPITAL_JUS_MALYJ,     'Z'),

    (SMALL_FITA,            'f'),
    (SMALL_I,               'i'), # LATIN
    (SMALL_WIDE_ON,         'o'),
    (SMALL_PSI,             'p'),
    (SMALL_OLE,             'q'),
    (SMALL_OT,              't'),
    (SMALL_DIGRAPH_UK,      'u'),
    (SMALL_IZHICA,          'v'),
    (SMALL_OMEGA,           'w'),
    (SMALL_KSI,             'x'),
    (SMALL_JUS_MALYJ,       'z'),

    (SMALL_UK,              '\u00B5'),

    (CAPITAL_MONOGRAPH_UK,  'У'),
    (CAPITAL_JATJ,          'Э'),
    (CAPITAL_I_AZ,          'Я'),

    (SMALL_MONOGRAPH_UK,    'у'),
    (SMALL_JATJ,            'э'),
    (SMALL_I_AZ,            'я'),

)

"""
конвертация не требуется для 8-битных диапазонов:

...
C0-D2, D4-DC, DE,
E0-F2, F4-FC, FE

"""
