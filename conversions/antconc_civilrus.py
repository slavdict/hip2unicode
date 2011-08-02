# -*- coding: UTF-8 -*-

"""
AntConc to Civil Russian

Перекодировка в русскую гражданку. Подразумевается,
что в тексте для перекодирования не будут втречаться
слова, состоящие только из заглавных букв. А также,
что заглавные буквы будут встречаться только на месте
титл. Иначе конвертация не будет правильной.

Также подразумевается, что на вход будет подаваться
не текст, а отдельное слово.

"""

from hip2unicode.representations.RE import *
from hip2unicode.representations.antconc import *

conversion = (
    (u'бг~о',           u'бого'),
    (u'бл~го',          u'благо'),
    (u'бжСтв',          u'божеств'),
    (u'бж~',            u'бож'),
    (u'блгДт',          u'благодат'),

    (SMALL_WIDE_ESTJ,   u'е'),
    (SMALL_ZELO,        u'з'),
    (SMALL_I,           u'и'),
    (SMALL_MONOGRAPH_UK,    u'у'),
    (SMALL_DIGRAPH_UK,      u'у'),
    (SMALL_OMEGA,       u'о'),
    (SMALL_JATJ,        u'е'),
    (SMALL_I_AZ,        u'я'),
    (SMALL_JUS_MALYJ,   u'я'),
    (SMALL_KSI,         u'кс'),
    (SMALL_PSI,         u'пс'),
    (SMALL_FITA,        u'ф'),
    (u'а' + SMALL_IZHICA,   u'ав'),
    (u'е' + SMALL_IZHICA,   u'ев'),
    (SMALL_WIDE_ESTJ + SMALL_IZHICA,    u'ев'),
    (SMALL_IZHICA,      u'и'),
    (SMALL_WIDE_ON,     u'о'),
    (SMALL_OLE,         u'о'),
    (SMALL_OT,          u'от'),
    (AKUT,          u''),
    (GRAVIS,        u''),
    (CIRKUMFLEKS,   u''),
    (TITLO,         u'*'),
    (PAEROK,        u'ъ'),
    (VEDI_TITLO,    u'*'),
    (GLAGOLJ_TITLO, u'*'),
    (DOBRO_TITLO,   u'*'),
    (ZHIVETE_TITLO, u'*'),
    (ZEMLJA_TITLO,  u'*'),
    (NASH_TITLO,    u'*'),
    (ON_TITLO,      u'*'),
    (RCY_TITLO,     u'*'),
    (SLOVO_TITLO,   u'*'),
    (XER_TITLO,     u'*'),
    (CHERVJ_TITLO,  u'*'),
    (u'ъ$',         u''),
    (u'ъа',         u'а'),
    (u'ъо',         u'о'),
    (u'ъу',         u'у'),
    (u'ъы',         u'ы'),
    (u'ъи',         u'ы'),
)
