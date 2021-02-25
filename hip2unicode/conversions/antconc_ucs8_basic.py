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
ASPIRATION_TIP = '\u4444'
CAPITAL_IZHICA_TIP = '\u4445'
SMALL_IZHICA_TIP = '\u4446'
CAPITAL_I_TIP = '\u4447'
SMALL_I_TIP = '\u4448'

lc_SMALL_LETTERS    = left_context( token( SMALL_LETTERS ) )
lc_CAPITAL_LETTERS  = left_context( token( CAPITAL_LETTERS ) )
ic_SMALL_VOWELS     = initial_context( token( SMALL_VOWELS ) )
ic_CAPITAL_VOWELS   = initial_context( token( CAPITAL_VOWELS ) )
nrc_ACCENTS         = neg_right_context( token( ASPIRATION_TIP + ACCENTS ) )
VOWELS_WITHOUT_ASP  = '[=]' + right_context( token(SMALL_VOWELS + CAPITAL_VOWELS) )

conversion = (
    # титло над строчными от, ферт и пси
    # преобразуется в обратный слеш
    # (экранированная запись для RegExp)
    (left_context( token( SMALL_OT, SMALL_FERT, SMALL_PSI ) ) + TITLO,  r'\\'),
    (THOUSAND_SIGN,                     '\u00A4'), # знак тысячи

    (VOWELS_WITHOUT_ASP,                ASPIRATION_TIP),
    (ic_SMALL_VOWELS + nrc_ACCENTS,     '3'), # придыхание
    (ic_SMALL_VOWELS + AKUT,            '4'), # придыхание и акут
    (ic_SMALL_VOWELS + GRAVIS,          '5'), # придыхание и гравис
    (ic_CAPITAL_VOWELS + nrc_ACCENTS,   '#'),
    (ic_CAPITAL_VOWELS + AKUT,          '$'),
    (ic_CAPITAL_VOWELS + GRAVIS,        '%'),

    (lc_SMALL_LETTERS + AKUT,           '1'), # акут
    (lc_SMALL_LETTERS + GRAVIS,         '2'), # гравис
    (lc_SMALL_LETTERS + CIRKUMFLEKS,    '6'), # циркумфлекс
    # Правило для устранения придыхания
    # над теми гласными, которые стоят
    # первыми в слове, но над которыми
    # должны стоять обычные титла
    # (= случай с цифрами):
    ('3~',                             '~'),
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
    (lc_SMALL_LETTERS + ZEMLJA_TITLO,   '\u20ac'),
    (lc_SMALL_LETTERS + ZHIVETE_TITLO,  '\u2022'),

    (lc_CAPITAL_LETTERS + GRAVIS,       '@'),
    (lc_CAPITAL_LETTERS + TITLO,        '&'),
    # след. преобразование обязательно должно идти
    # после всех преобразований, где выступает
    # TITLO, т.к. создаётся символ "~"
    (lc_CAPITAL_LETTERS + AKUT,         '~'),
    (lc_CAPITAL_LETTERS + CIRKUMFLEKS,  '^'),
    (lc_CAPITAL_LETTERS + PAEROK,       '_'),

    (lc_CAPITAL_LETTERS + SLOVO_TITLO,  'C'),

    (ASPIRATION_TIP + CAPITAL_IZHICA + '[3\#]?', CAPITAL_IZHICA_TIP),
    (ASPIRATION_TIP + SMALL_IZHICA + '[3\#]?', SMALL_IZHICA_TIP),
    (ASPIRATION_TIP + CAPITAL_I + '[3\#]?', CAPITAL_I_TIP),
    (ASPIRATION_TIP + SMALL_I + '[3\#]?', SMALL_I_TIP),
    (ASPIRATION_TIP + r'(?P<symb>.)[3\#]',  r'\g<symb>'),
    (ASPIRATION_TIP + r'(?P<symb>.)4',  r'\g<symb>1'),
    (ASPIRATION_TIP + r'(?P<symb>.)5',  r'\g<symb>2'),
    (ASPIRATION_TIP + r'(?P<symb>.)\$',  r'\g<symb>~'),
    (ASPIRATION_TIP + r'(?P<symb>.)\%',  r'\g<symb>@'),
    (ASPIRATION_TIP, ''),


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
