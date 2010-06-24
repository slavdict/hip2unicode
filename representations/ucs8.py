# -*- coding: UTF-8 -*-

EMPTY_STRING = u''

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
SMALL_WIDE_ESTJ = u'\u0454'

CAPITAL_ZHIVETE = u'Ж'
SMALL_ZHIVETE   = u'ж'

CAPITAL_ZELO    = u'\u0405'
SMALL_ZELO      = u'\u0455'

CAPITAL_ZEMLJA  = u'З'
SMALL_ZEMLJA    = u'з'

CAPITAL_IZHE    = u'И'
SMALL_IZHE      = u'и'

CAPITAL_I       = u'I' # LATIN "I"
SMALL_I         = u'i' # LATIN "i"

CAPITAL_KAKO    = u'К'
SMALL_KAKO      = u'к'

CAPITAL_LJUDI   = u'Л'
SMALL_LJUDI     = u'л'

CAPITAL_MYSLETE = u'М'
SMALL_MYSLETE   = u'м'

CAPITAL_NASH    = u'Н'
SMALL_NASH      = u'н'

CAPITAL_ON      = u'О' # CYRILLIC
SMALL_ON        = u'о' # CYRILLIC

CAPITAL_POKOJ   = u'П'
SMALL_POKOJ     = u'п'

CAPITAL_RCY     = u'Р'
SMALL_RCY       = u'р'

CAPITAL_SLOVO   = u'С'
SMALL_SLOVO     = u'с'

CAPITAL_TVERDO  = u'Т'
SMALL_TVERDO    = u'т'

CAPITAL_MONOGRAPH_UK    = u'У'
SMALL_MONOGRAPH_UK      = u'у'

CAPITAL_DIGRAPH_UK      = u'U'
SMALL_DIGRAPH_UK        = u'u'

SMALL_UK        = u'\u00B5'

CAPITAL_FERT    = u'Ф'
SMALL_FERT      = u'ф'

CAPITAL_XER     = u'Х'
SMALL_XER       = u'х'

CAPITAL_OMEGA   = u'W' # LATIN 
SMALL_OMEGA     = u'w' # LATIN

CAPITAL_CY      = u'Ц'
SMALL_CY        = u'ц'

CAPITAL_CHERVJ  = u'Ч'
SMALL_CHERVJ    = u'ч'

CAPITAL_SHA     = u'Ш'
SMALL_SHA       = u'ш'

CAPITAL_SHCHA   = u'Щ'
SMALL_SHCHA     = u'щ'

CAPITAL_ER      = u'Ъ'
SMALL_ER        = u'ъ'

CAPITAL_ERY     = u'Ы'
SMALL_ERY       = u'ы'

CAPITAL_ERJ     = u'Ь'
SMALL_ERJ       = u'ь'

CAPITAL_JATJ    = u'Э'
SMALL_JATJ      = u'э'

CAPITAL_JU      = u'Ю'
SMALL_JU        = u'ю'

CAPITAL_I_AZ    = u'Я'
SMALL_I_AZ      = u'я'

CAPITAL_JUS_MALYJ   = u'Z'
SMALL_JUS_MALYJ     = u'z'

CAPITAL_KSI     = u'X' # LATIN
SMALL_KSI       = u'x' # LATIN

CAPITAL_PSI     = u'P' # LATIN
SMALL_PSI       = u'p' # LATIN

CAPITAL_FITA    = u'F'
SMALL_FITA      = u'f'

CAPITAL_IZHICA  = u'V' # LATIN "V"
SMALL_IZHICA    = u'v' # LATIN "v"  
CAPITAL_IZHICA_DOUBLE_GRAVIS    = u'M' # LATIN
SMALL_IZHICA_DOUBLE_GRAVIS      = u'm'

CAPITAL_WIDE_ON = u'O' # LATIN
SMALL_WIDE_ON   = u'o' # LATIN

CAPITAL_OLE     = u'Q'
SMALL_OLE       = u'q'

CAPITAL_OT      = u'T' # LATIN
SMALL_OT        = u't' # LATIN


# Diacritics

CAPITAL_AKUT    = u'~'
SMALL_AKUT      = u'1'

CAPITAL_GRAVIS  = u'@'
SMALL_GRAVIS    = u'2'

CAPITAL_CIRKUMFLEKS = ur'\^' # RegExp escaped CARET symbol
SMALL_CIRKUMFLEKS   = u'6'

CAPITAL_ASPIRATION  = u'#'
SMALL_ASPIRATION    = u'3'

CAPITAL_ASPIRATION_AKUT = u'$'
SMALL_ASPIRATION_AKUT   = u'4'

CAPITAL_ASPIRATION_CIRKUMFLEX   = u'%'
SMALL_ASPIRATION_CIRKUMFLEX     = u'5'

CAPITAL_TITLO   = u'&'
SMALL_TITLO     = u'7'
MIDDLE_TITLO    = ur'\\' # RegExp escaped BACK SLASH symbol

CAPITAL_PAEROK  = u'_'
SMALL_PAEROK    = u'8'

VEDI_TITLO      = ur'\+' # RegExp escaped plus sign
GLAGOLJ_TITLO   = u'g'
DOBRO_TITLO     = u'd'
ZHIVETE_TITLO   = u'\u2022'
ZEMLJA_TITLO    = u'\u20AC'
NASH_TITLO      = u'='
ON_TITLO        = u'b'
RCY_TITLO       = u'>'
SLOVO_TITLO     = u'c' # LATIN c
XER_TITLO       = u'<'
CHERVJ_TITLO    = ur'\?' # RegExp escaped question mark

CAPITAL_SLOVO_TITLO = u'C' # LATIN C


AE = EMPTY_STRING.join(
    (
        CAPITAL_AZ,
        SMALL_AZ,
        CAPITAL_ESTJ,
        SMALL_ESTJ,
        SMALL_WIDE_ESTJ,
    )
)

CAPITAL_CONSONANTS  = u'БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ' + u'FPX' + u'\u0405'
SMALL_CONSONANTS    = u'бвгджзйклмнпрстфхцчшщъь' + u'fpx' + u'\u0455'

# VOWEL_DIACRITICS -- диакритика над гласными,
# CONSONANT_DIACRITICS -- диакритика над согласными буквами.
CAPITAL_VOWEL_DIACRITICS  = u'#$%&' + u'@' + u'\^' + u'~'
SMALL_VOWEL_DIACRITICS    = u'1234567'

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

VOWEL_DIACRITICS        = CAPITAL_VOWEL_DIACRITICS + SMALL_VOWEL_DIACRITICS
CONSONANT_DIACRITICS    = CAPITAL_CONSONANT_DIACRITICS + SMALL_CONSONANT_DIACRITICS

DIACRITICS = CAPITAL_DIACRITICS + SMALL_DIACRITICS
