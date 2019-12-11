EMPTY_STRING = ''

CAPITAL_AZ  = 'А'
SMALL_AZ    = 'а'

CAPITAL_BUKI    = 'Б'
SMALL_BUKI      = 'б'

CAPITAL_VEDI    = 'В'
SMALL_VEDI      = 'в'

CAPITAL_GLAGOLJ = 'Г'
SMALL_GLAGOLJ   = 'г'

CAPITAL_DOBRO   = 'Д'
SMALL_DOBRO     = 'д'

CAPITAL_ESTJ    = 'Е'
SMALL_ESTJ      = 'е'
SMALL_WIDE_ESTJ = '\u0454'

CAPITAL_ZHIVETE = 'Ж'
SMALL_ZHIVETE   = 'ж'

CAPITAL_ZELO    = '\u0405'
SMALL_ZELO      = '\u0455'

CAPITAL_ZEMLJA  = 'З'
SMALL_ZEMLJA    = 'з'

CAPITAL_IZHE    = 'И'
SMALL_IZHE      = 'и'

CAPITAL_I       = 'I' # LATIN "I"
SMALL_I         = 'i' # LATIN "i"

CAPITAL_KAKO    = 'К'
SMALL_KAKO      = 'к'

CAPITAL_LJUDI   = 'Л'
SMALL_LJUDI     = 'л'

CAPITAL_MYSLETE = 'М'
SMALL_MYSLETE   = 'м'

CAPITAL_NASH    = 'Н'
SMALL_NASH      = 'н'

CAPITAL_ON      = 'О' # CYRILLIC
SMALL_ON        = 'о' # CYRILLIC

CAPITAL_POKOJ   = 'П'
SMALL_POKOJ     = 'п'

CAPITAL_RCY     = 'Р'
SMALL_RCY       = 'р'

CAPITAL_SLOVO   = 'С'
SMALL_SLOVO     = 'с'

CAPITAL_TVERDO  = 'Т'
SMALL_TVERDO    = 'т'

CAPITAL_MONOGRAPH_UK    = 'У'
SMALL_MONOGRAPH_UK      = 'у'

CAPITAL_DIGRAPH_UK      = 'U'
SMALL_DIGRAPH_UK        = 'u'

SMALL_UK        = '\u00B5'

CAPITAL_FERT    = 'Ф'
SMALL_FERT      = 'ф'

CAPITAL_XER     = 'Х'
SMALL_XER       = 'х'

CAPITAL_OMEGA   = 'W' # LATIN
SMALL_OMEGA     = 'w' # LATIN

CAPITAL_CY      = 'Ц'
SMALL_CY        = 'ц'

CAPITAL_CHERVJ  = 'Ч'
SMALL_CHERVJ    = 'ч'

CAPITAL_SHA     = 'Ш'
SMALL_SHA       = 'ш'

CAPITAL_SHCHA   = 'Щ'
SMALL_SHCHA     = 'щ'

CAPITAL_ER      = 'Ъ'
SMALL_ER        = 'ъ'

CAPITAL_ERY     = 'Ы'
SMALL_ERY       = 'ы'

CAPITAL_ERJ     = 'Ь'
SMALL_ERJ       = 'ь'

CAPITAL_JATJ    = 'Э'
SMALL_JATJ      = 'э'

CAPITAL_JU      = 'Ю'
SMALL_JU        = 'ю'

CAPITAL_I_AZ    = 'Я'
SMALL_I_AZ      = 'я'

CAPITAL_JUS_MALYJ   = 'Z'
SMALL_JUS_MALYJ     = 'z'

CAPITAL_KSI     = 'X' # LATIN
SMALL_KSI       = 'x' # LATIN

CAPITAL_PSI     = 'P' # LATIN
SMALL_PSI       = 'p' # LATIN

CAPITAL_FITA    = 'F'
SMALL_FITA      = 'f'

CAPITAL_IZHICA  = 'V' # LATIN "V"
SMALL_IZHICA    = 'v' # LATIN "v"
CAPITAL_IZHICA_DOUBLE_GRAVIS    = 'M' # LATIN
SMALL_IZHICA_DOUBLE_GRAVIS      = 'm'

CAPITAL_WIDE_ON = 'O' # LATIN
SMALL_WIDE_ON   = 'o' # LATIN

CAPITAL_OLE     = 'Q'
SMALL_OLE       = 'q'

CAPITAL_OT      = 'T' # LATIN
SMALL_OT        = 't' # LATIN


# Diacritics

CAPITAL_AKUT    = '~'
SMALL_AKUT      = '1'

CAPITAL_GRAVIS  = '@'
SMALL_GRAVIS    = '2'

CAPITAL_CIRKUMFLEKS = r'\^' # RegExp escaped CARET symbol
SMALL_CIRKUMFLEKS   = '6'

CAPITAL_ASPIRATION  = '#'
SMALL_ASPIRATION    = '3'

CAPITAL_ASPIRATION_AKUT = '\$'  # RegExp escaped DOLAR symbol
SMALL_ASPIRATION_AKUT   = '4'

CAPITAL_ASPIRATION_CIRKUMFLEX   = '%'
SMALL_ASPIRATION_CIRKUMFLEX     = '5'

CAPITAL_TITLO   = '&'
SMALL_TITLO     = '7'
MIDDLE_TITLO    = r'\\' # RegExp escaped BACK SLASH symbol

CAPITAL_PAEROK  = '_'
SMALL_PAEROK    = '8'

VEDI_TITLO      = r'\+' # RegExp escaped plus sign
GLAGOLJ_TITLO   = 'g'
DOBRO_TITLO     = 'd'
ZHIVETE_TITLO   = '\u2022'
ZEMLJA_TITLO    = '\u20AC'
NASH_TITLO      = '='
ON_TITLO        = 'b'
RCY_TITLO       = '>'
SLOVO_TITLO     = 'c' # LATIN c
XER_TITLO       = '<'
CHERVJ_TITLO    = r'\?' # RegExp escaped question mark

CAPITAL_SLOVO_TITLO = 'C' # LATIN C

LETTERS = EMPTY_STRING.join(
    [ eval(i) for i in dir() \
        if i.startswith('CAPITAL_') \
        or i.startswith('SMALL_') \
        or i.endswith('_TITLO') ]
)

AE = EMPTY_STRING.join(
    (
        CAPITAL_AZ,
        SMALL_AZ,
        CAPITAL_ESTJ,
        SMALL_ESTJ,
        SMALL_WIDE_ESTJ,
    )
)

CAPITAL_CONSONANTS  = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ' + 'FPX' + '\u0405'
SMALL_CONSONANTS    = 'бвгджзйклмнпрстфхцчшщъь' + 'fpx' + '\u0455'

# VOWEL_DIACRITICS -- диакритика над гласными,
# CONSONANT_DIACRITICS -- диакритика над согласными буквами.
CAPITAL_VOWEL_DIACRITICS  = '#\$%&' + '@' + '\^' + '~'
SMALL_VOWEL_DIACRITICS    = '1234567'

CAPITAL_CONSONANT_DIACRITICS    = CAPITAL_SLOVO_TITLO
SMALL_CONSONANT_DIACRITICS      = EMPTY_STRING.join(
    (
        VEDI_TITLO,
        GLAGOLJ_TITLO,
        DOBRO_TITLO,
        ZHIVETE_TITLO,
        ZEMLJA_TITLO,
        NASH_TITLO,
        ON_TITLO,
        RCY_TITLO,
        SLOVO_TITLO,
        XER_TITLO,
        CHERVJ_TITLO,
    )
)

CAPITAL_DIACRITICS  = CAPITAL_VOWEL_DIACRITICS + CAPITAL_CONSONANT_DIACRITICS
SMALL_DIACRITICS    = SMALL_VOWEL_DIACRITICS + SMALL_CONSONANT_DIACRITICS

VOWEL_DIACRITICS     = CAPITAL_VOWEL_DIACRITICS + SMALL_VOWEL_DIACRITICS
CONSONANT_DIACRITICS = CAPITAL_CONSONANT_DIACRITICS + SMALL_CONSONANT_DIACRITICS

DIACRITICS = CAPITAL_DIACRITICS + SMALL_DIACRITICS
