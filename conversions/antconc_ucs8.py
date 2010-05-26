# -*- coding: UTF-8 -*-

"""
AntConc to UCS8 conversion

AntConc encoding is specialized ad-hoc
unicode + UTF-8 based encoding designed
for use in AntConc concordancer program
while working with Old Church Slavonic
texts corpus.

"""
from hip2unicode.hip2unicode.representations import antconc

LEFT_LETTER     = u'(?<=%s)'
INITIAL_LETTER  = u'(?<=((^%s)|(%s%s))' % (
                u'%(initial_letter)s',
                antconc.ANTCONC_NON_LETTERS,
                u'%(initial_letter)s',
                )

SMALL_LETTER            = LEFT_LETTER % antconc.ANTCONC_SMALL_LETTERS
CAPITAL_LETTER          = LEFT_LETTER % antconc.ANTCONC_CAPITAL_LETTERS 
INITIAL_SMALL_VOWEL     = INITIAL_LETTER % {
                        'initial_letter': antconc.ANTCONC_SMALL_VOWELS,
                        }
INITIAL_CAPITAL_VOWEL   = INITIAL_LETTER % {
                        'initial_letter': antconc.ANTCONC_CAPITAL_VOWELS,
                        }

conversion = (
    (u'%s%s' % (SMALL_LETTER, antconc.AKUT),      u'1'),
    (u'%s%s' % (SMALL_LETTER, antconc.GRAVIS),    u'2'),
    (u'%s%s' % (INITIAL_SMALL_VOWEL, u'%s%s' % antconc. #TODO),



    (antconc.CAPITAL_FITA,          u'F'),
    (antconc.CAPITAL_I,             u'I'),
    (antconc.CAPITAL_WIDE_ON,       u'O'),
    (antconc.CAPITAL_PSI,           u'P'),
    (antconc.CAPITAL_OLE,           u'Q'),
    (antconc.CAPITAL_OT,            u'T'),
    (antconc.CAPITAL_DIGRAPH_UK,    u'U'),
    (antconc.CAPITAL_IZHICA,        u'V'),
    (antconc.CAPITAL_OMEGA,         u'W'),
    (antconc.CAPITAL_KSI,           u'X'),
    (antconc.CAPITAL_JUS_MALYJ,     u'Z'),

    (antconc.SMALL_FITA,            u'f'),
    (antconc.SMALL_I,               u'i'),
    (antconc.SMALL_WIDE_ON,         u'o'),
    (antconc.SMALL_PSI,             u'p'),
    (antconc.SMALL_OLE,             u'q'),
    (antconc.SMALL_OT,              u't'),
    (antconc.SMALL_DIGRAPH_UK,      u'u'),
    (antconc.SMALL_IZHICA,          u'v'),
    (antconc.SMALL_OMEGA,           u'w'),
    (antconc.SMALL_KSI,             u'x'),
    (antconc.SMALL_JUS_MALYJ,       u'z'),

    (antconc.SMALL_UK,              u'\u00B5'),

    (antconc.CAPITAL_MONOGRAPH_UK,  u'У'),
    (antconc.CAPITAL_JATJ,          u'Э'),
    (antconc.CAPITAL_I_AZ,          u'Я'),

    (antconc.SMALL_MONOGRAPH_UK,    u'у'),
    (antconc.SMALL_JATJ,            u'э'),
    (antconc.SMALL_I_AZ,            u'я'),

)

"""
конвертация не требуется для 8-битных диапазонов:

...
C0-D2, D4-DC, DE,
E0-F2, F4-FC, FE

"""
