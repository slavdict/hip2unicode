"""
Файл описывает константы для удобства использования
при построении регулярных выражений (NB).

"""
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

# NB: \u0415 is used instead \u0404,
# because there is no difference
# between normal and wide capital E
CAPITAL_WIDE_ESTJ   = CAPITAL_ESTJ
SMALL_WIDE_ESTJ     = '\u0454'   # CYRILLIC "є"

CAPITAL_ZHIVETE = 'Ж'
SMALL_ZHIVETE   = 'ж'

CAPITAL_ZELO    = '\u0405' # CYRILLIC "Ѕ"
SMALL_ZELO      = '\u0455' # CYRILLIC "ѕ"

CAPITAL_ZEMLJA  = 'З'
SMALL_ZEMLJA    = 'з'

CAPITAL_IZHE    = 'И'
SMALL_IZHE      = 'и'

CAPITAL_I       = '\u0406' # CYRILLIC "І"
SMALL_I         = '\u0456' # CYRILLIC "і"
SMALL_DOTLESS_I = '\u0131'

CAPITAL_KAKO    = 'К'
SMALL_KAKO      = 'к'

CAPITAL_LJUDI   = 'Л'
SMALL_LJUDI     = 'л'

CAPITAL_MYSLETE = 'М'
SMALL_MYSLETE   = 'м'

CAPITAL_NASH    = 'Н'
SMALL_NASH      = 'н'

CAPITAL_ON  = 'О'
SMALL_ON    = 'о'

CAPITAL_POKOJ   = 'П'
SMALL_POKOJ     = 'п'

CAPITAL_RCY = 'Р'
SMALL_RCY   = 'р'

CAPITAL_SLOVO   = 'С'
SMALL_SLOVO     = 'с'

CAPITAL_TVERDO  = 'Т'
SMALL_TVERDO    = 'т'


CAPITAL_MONOGRAPH_UK    = '\uA64A'  # "Ꙋ"
SMALL_MONOGRAPH_UK      = '\uA64B'  # "ꙋ"

CAPITAL_DIGRAPH_UK  = '\u0478' # "Ѹ"
SMALL_DIGRAPH_UK    = '\u0479' # "ѹ"

SMALL_UK    = 'у'


CAPITAL_FERT    = 'Ф'
SMALL_FERT      = 'ф'

CAPITAL_XER    = 'Х'
SMALL_XER      = 'х'

CAPITAL_OMEGA   = '\u0460'
SMALL_OMEGA     = '\u0461'

CAPITAL_CY  = 'Ц'
SMALL_CY    = 'ц'

CAPITAL_CHERVJ  = 'Ч'
SMALL_CHERVJ    = 'ч'

CAPITAL_SHA = 'Ш'
SMALL_SHA   = 'ш'

CAPITAL_SHCHA   = 'Щ'
SMALL_SHCHA     = 'щ'

CAPITAL_ER  = 'Ъ'
SMALL_ER    = 'ъ'

CAPITAL_ERY = 'Ы'
SMALL_ERY   = 'ы'

CAPITAL_ERJ = 'Ь'
SMALL_ERJ   = 'ь'

CAPITAL_JATJ    = '\u0462'
SMALL_JATJ      = '\u0463'

CAPITAL_JU  = 'Ю'
SMALL_JU    = 'ю'

CAPITAL_I_AZ    = '\uA656'
SMALL_I_AZ      = '\uA657'

CAPITAL_JUS_MALYJ   = '\u0466'
SMALL_JUS_MALYJ     = '\u0467'

CAPITAL_KSI = '\u046E'
SMALL_KSI   = '\u046F'

CAPITAL_PSI = '\u0470'
SMALL_PSI   = '\u0471'

CAPITAL_FITA    = '\u0472'
SMALL_FITA      = '\u0473'

CAPITAL_IZHICA = '\u0474'
SMALL_IZHICA = '\u0475'



CAPITAL_WIDE_ON = '\u047A'
SMALL_WIDE_ON = '\u047B'

CAPITAL_OLE = '\u047C'
SMALL_OLE = '\u047D'

CAPITAL_OT = '\u047E'
SMALL_OT = '\u047F'


# Diacritics
AKUT        = "'"
GRAVIS      = '`'
CIRKUMFLEKS = r'\^' # RegExp escaped CARET symbol
TITLO       = '~'

PAEROK      = 'Ъ'

VEDI_TITLO      = 'В'
GLAGOLJ_TITLO   = 'Г'
DOBRO_TITLO     = 'Д'
ZHIVETE_TITLO   = 'Ж'
ZEMLJA_TITLO    = 'З'
NASH_TITLO      = 'Н'
ON_TITLO        = 'О'
RCY_TITLO       = 'Р'
SLOVO_TITLO     = 'С'
XER_TITLO       = 'Х'
CHERVJ_TITLO    = 'Ч'


THOUSAND_SIGN   = '\u0482'


# Strings containing groups of symbols
EMPTY_STRING = ''

CAPITAL_LETTERS = EMPTY_STRING.join(
        [ eval(i) for i in dir() if i.startswith('CAPITAL_') ]
    )

SMALL_LETTERS = EMPTY_STRING.join(
        [ eval(i) for i in dir() if i.startswith('SMALL_') ]
    )

DIACRITICS = EMPTY_STRING.join(
        [ AKUT, GRAVIS, CIRKUMFLEKS, TITLO, PAEROK, ] +
        [ eval(i) for i in dir() if i.endswith('_TITLO') ]
    )

CAPITAL_VOWELS  = EMPTY_STRING.join(
    (
        CAPITAL_AZ,
        CAPITAL_ESTJ,
    #   CAPITAL_WIDE_ESTJ,
        CAPITAL_IZHE,
        CAPITAL_I,
        CAPITAL_ON,
        CAPITAL_MONOGRAPH_UK,
        CAPITAL_DIGRAPH_UK,
    #   SMALL_UK,
        CAPITAL_OMEGA,
        CAPITAL_ERY,
        CAPITAL_JATJ,
        CAPITAL_JU,
        CAPITAL_I_AZ,
        CAPITAL_JUS_MALYJ,
        CAPITAL_IZHICA,
        CAPITAL_WIDE_ON,
    #   CAPITAL_OLE,
    )
)

SMALL_VOWELS  = EMPTY_STRING.join(
    (
        SMALL_AZ,
        SMALL_ESTJ,
        SMALL_WIDE_ESTJ,
        SMALL_IZHE,
        SMALL_I,
        SMALL_ON,
        SMALL_MONOGRAPH_UK,
        SMALL_DIGRAPH_UK,
        SMALL_UK,
        SMALL_OMEGA,
        SMALL_ERY,
        SMALL_JATJ,
        SMALL_JU,
        SMALL_I_AZ,
        SMALL_JUS_MALYJ,
        SMALL_IZHICA,
        SMALL_WIDE_ON,
    #   SMALL_OLE,
    )
)

LETTERS = EMPTY_STRING.join(
    (
        CAPITAL_LETTERS,
        SMALL_LETTERS,
        DIACRITICS,
    )
)

ACCENTS = EMPTY_STRING.join(
    (
        AKUT,
        GRAVIS,
        CIRKUMFLEKS,
    )
)
