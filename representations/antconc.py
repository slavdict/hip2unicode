# -*- coding: UTF-8 -*-

"""
Файл описывает константы для удобства использования 
при построении регулярных выражений (NB).

"""
CAPITAL_AZ  = u'А'
SMALL_AZ    = u'а'

CAPITAL_BUKI    = u'Б'
SMALL_BUKI      = u'б'

CAPITAL_VEDI    = u'В'
SMALL_VEDI      = u'в'

CAPITAL_GLAGOLJ = u'Г'
SMALL_GLAGOLJ   = u'г'

CAPITAL_DOBRO   = u'Д'
SMALL_DOBRO     = u'д'

CAPITAL_ESTJ    = u'Е'
SMALL_ESTJ      = u'е'

# NB: \u0415 is used instead \u0404,
# because there is no difference 
# between normal and wide capital E
CAPITAL_WIDE_ESTJ   = CAPITAL_ESTJ    
SMALL_WIDE_ESTJ     = u'\u0454'   # CYRILLIC "є"

CAPITAL_ZHIVETE = u'Ж'
SMALL_ZHIVETE   = u'ж'

CAPITAL_ZELO    = u'\u0405' # CYRILLIC "Ѕ"
SMALL_ZELO      = u'\u0455' # CYRILLIC "ѕ"

CAPITAL_ZEMLJA  = u'З'
SMALL_ZEMLJA    = u'з'

CAPITAL_IZHE    = u'И'
SMALL_IZHE      = u'и'

CAPITAL_I   = u'\u0406' # CYRILLIC "І"
SMALL_I     = u'\u0456' # CYRILLIC "і"

CAPITAL_KAKO    = u'К'
SMALL_KAKO      = u'к'

CAPITAL_LJUDI   = u'Л'
SMALL_LJUDI     = u'л'

CAPITAL_MYSLETE = u'М'
SMALL_MYSLETE   = u'м'

CAPITAL_NASH    = u'Н'
SMALL_NASH      = u'н'

CAPITAL_ON  = u'О'
SMALL_ON    = u'о'

CAPITAL_POKOJ   = u'П'
SMALL_POKOJ     = u'п'

CAPITAL_RCY = u'Р'
SMALL_RCY   = u'р'

CAPITAL_SLOVO   = u'С'
SMALL_SLOVO     = u'с'

CAPITAL_TVERDO  = u'Т'
SMALL_TVERDO    = u'т'


CAPITAL_MONOGRAPH_UK    = u'\uA64A'  # "Ꙋ"
SMALL_MONOGRAPH_UK      = u'\uA64B'  # "ꙋ"

CAPITAL_DIGRAPH_UK  = u'\u0478' # "Ѹ"
SMALL_DIGRAPH_UK    = u'\u0479' # "ѹ"

SMALL_UK    = u'у'


CAPITAL_FERT    = u'Ф'
SMALL_FERT      = u'ф'

CAPITAL_XER    = u'Х'
SMALL_XER      = u'х'

CAPITAL_OMEGA   = u'\u0460'
SMALL_OMEGA     = u'\u0461'

CAPITAL_CY  = u'Ц'
SMALL_CY    = u'ц'

CAPITAL_CHERVJ  = u'Ч'
SMALL_CHERVJ    = u'ч'

CAPITAL_SHA = u'Ш'
SMALL_SHA   = u'ш'

CAPITAL_SHCHA   = u'Щ'
SMALL_SHCHA     = u'щ'

CAPITAL_ER  = u'Ъ'
SMALL_ER    = u'ъ'

CAPITAL_ERY = u'Ы'
SMALL_ERY   = u'ы'

CAPITAL_ERJ = u'Ь'
SMALL_ERJ   = u'ь'

CAPITAL_JATJ    = u'\u0462'
SMALL_JATJ      = u'\u0463'

CAPITAL_JU  = u'Ю'
SMALL_JU    = u'ю'

CAPITAL_I_AZ    = u'\uA656'
SMALL_I_AZ      = u'\uA657'

CAPITAL_JUS_MALYJ   = u'\u0466'
SMALL_JUS_MALYJ     = u'\u0467'

CAPITAL_KSI = u'\u046E'
SMALL_KSI   = u'\u046F'

CAPITAL_PSI = u'\u0470'
SMALL_PSI   = u'\u0471'

CAPITAL_FITA    = u'\u0472'
SMALL_FITA      = u'\u0473'

CAPITAL_IZHICA = u'\u0474'
SMALL_IZHICA = u'\u0475'



CAPITAL_WIDE_ON = u'\u047A'
SMALL_WIDE_ON = u'\u047B'

CAPITAL_OLE = u'\u047C'
SMALL_OLE = u'\u047D'

CAPITAL_OT = u'\u047E'
SMALL_OT = u'\u047F'


# Diacritics
AKUT        = u"'"
GRAVIS      = u'`'
CIRKUMFLEKS = ur'\^' # RegExp escaped CARET symbol
TITLO       = u'~' 

PAEROK      = u'Ъ'

VEDI_TITLO      = u'В'
GLAGOLJ_TITLO   = u'Г'
DOBRO_TITLO     = u'Д'
ZHIVETE_TITLO   = u'Ж'
ZEMLJA_TITLO    = u'З'
NASH_TITLO      = u'Н'
ON_TITLO        = u'О'
RCY_TITLO       = u'Р'
SLOVO_TITLO     = u'С'
XER_TITLO       = u'Х'
CHERVJ_TITLO    = u'Ч'


THOUSAND_SIGN   = u'\u0482'


# Strings containing groups of symbols
EMPTY_STRING = u''

CAPITAL_LETTERS = EMPTY_STRING.join(
        [ i for i in dir() if i.startswith('CAPITAL_') ]
    )

SMALL_LETTERS = EMPTY_STRING.join(
        [ i for i in dir() if i.startswith('SMALL_') ]
    )

DIACRITICS = EMPTY_STRING.join(
        [ AKUT, GRAVIS, CIRKUMFLEKS, TITLO, PAEROK, ] +
        [ i for  i in dir() if i.endswith('_TITLO') ]
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

