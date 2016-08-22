# -*- coding: UTF-8 -*-

"""
Раскрытие титл для кодировки АнтКонк.

Подразумевается, что в тексте для перекодирования не будут втречаться слова,
состоящие только из заглавных букв. А также, что заглавные буквы будут
встречаться только на месте титл. Иначе конвертация не будет правильной.

Также подразумевается, что на вход будет подаваться не текст, а отдельное
слово.

"""

from hip2unicode.representations.RE import *
from hip2unicode.representations.antconc import *

conversion = (
    (u'апСтл',  u"апо'стол"),
    (u'апСл',   u"апо'стол"),
    (u'апС',    u"апо'с"),  # апостол...
    (u'бг~',    u'бог'),
    (u'бж~тв',  u'божеств'),
    (u'бж~',    u"бо'ж"),
    (u'бжСтв',  u'божеств'),
    (u'бз~',    u"бо'з"),
    (u'бл~г',   u'благ'),
    (u'бл~ж',   u'блаж'),
    (u'бл~з',   u'блаз'),
    (u'блГв',   u'благов'),
    (u'блгДт',  u"благода'т"),
    (u'блгСв',  u'благослов'),
    (u'блгСл',  u'благосл'),
    (u'блгС',   u'благос'),
    (u'бцД',    u"богоро'диц"),
    (u'влДк',   u"влады'к"),
    (u'влДц',   u"влады'ц"),
    (u'влДчц',  u"влады'чиц"),
    (u'влДч',   u"влады'ч"),
    (u'ѵГл',    u'вангел'), # Евангел...
    (u'ѵГ',     u'ванг'),   # Евангел...
    (u'гг~л', u'нгел'), # ангел
    (u'гл~г',   u'глаг'),   # глагол...
    (u'гл~',    u'глагол'),
    (u'глВ',    u'глав'),
    (u'гдСнь',  u'господень'),
    (u'гдСв',   u'господев'),
    (u'гдС',    u'господ'),
    (u'гпСж',   u'госпож'),
    (u'дв~д',   u'давид'),
    (u'дв~',    u'дев'),
    (u'двСтв',  u'девств'),
    (u'дс~',    u'дꙋс'),
    (u'дх~',    u'дꙋх'),
    (u'дш~',    u'дꙋш'),
    (u'и~с',    u'исꙋс'),
    (u'іи~л',   u'израил'),
    (u'кр~с',   u'крес'),
    (u'кр~ш',   u'креш'),
    (u'крСт',   u'крест'),
    (u'крСні',  u'кресени'), # Это правило не 100%-ное. Слово ``воскрСнiи``
                             # может быть как формой предл.п. сущ. ВОСКРЕСЕНИЕ,
                             # так и формой мн.ч. прилагательного ВОСКРЕСНЫЙ,
                             # которая встречается, правда, достаточно редко.
                             # Возможно, есть и другие формы, для которых это правило
                             # также будет работать неправильно.
    (u'крС',    u'крес'),
    (u'мДр',    u'мꙋдр'),
    (u'мл~тв',  u'молитв'),
    (u'млДнцъ', u'младенец'),
    (u'млДн',   u'младен'),
    (u'млСрд',  u'милосерд'),
    (u'млСт',   u'милост'),
    (u'млС',    u'милос'),
    (u'мт~р',   u"ма'тер"),
    (u'мт~',    u"ма'т"),
    (u'мр~і',   u'мари'),
    (u'мРк',    u'мѧрек'),   # Имярек
    (u'мч~нк',  u"мꙋ'ченик"),
    (u'мч~нц',  u"мꙋ'чениц"),
    (u'мч~нч',  u"мꙋ'ченич"),
    (u'мч~н',   u"мꙋ'чен"),
    (u'мцС',    u"ме'сѧц"),
    (u'нб~с',   u'небес'),
    (u'нбСс',   u'небес'),
    (u'нбС',    u'небес'),
    (u'нб~',    u'неб'),
    (u'нлД',    u'недел'),
    (u'нн~',    u'нын'),
    (u'ѻч~ь',   u"ѻте'чь"),
    (u'ѻч~[єе]с', u"ѻте'чес"),
    (u"ѻ'ч~",   u"ѻ'тч"),
    (u"ѻц~ъ",   u"ѻте'цъ"),
    (u"ѻц~",    u'ѻтц'),
    (u'првДнъ', u'праведенъ'),
    (u'првДн',  u'праведн'),
    (u'прДтч',  u'предтеч'), # Предтеча
    (u'прДт',   u'предт'),   # Предтеча
    (u'прпДб',  u'преподоб'),
    (u'прОр',   u'прор'),    # Пророк
    (u'прСн',   u'присн'),
    (u'прСт',   u'прест'),
    (u'прчСт',  u'пречист'),
    (u'пСкп',   u'пископ'),  # епископ
    (u'пСк',    u'писк'),
    (u'ржСтв',  u'рождеств'),
    (u'рСл',    u'рꙋсал'),   # Иерусалим
    (u'сл~нц',  u'солнц'),
    (u'сн~',    u'сын'),
    (u'сп~с',   u'спас'),
    (u'спСн',   u'спасен'),
    (u'срДц',   u'сердц'),
    (u'срДч',   u'сердеч'),
    (u'ст~',    u'свѧт'),
    (u'стрСт',  u'страст'),
    (u'сХ',     u'стих'),
    (u'стХр',   u'стихир'),
    (u'сщ~',    u'свѧщ'),
    (u'трОц',   u'троиц'),
    (u'трОч',   u'троич'),
    (u'трСт',   u'трисвѧт'),
    (u'хрСт',   u'христ'),
    (u'цр~к',   u'церк'),
    (u'цр~',    u'цар'),
    (u'црС',    u'царс'),
    (u'чл~в',   u'челов'),
    (u'ч~нк',   u'ченик'),
    (u'ч~нц',   u'чениц'),
    (u'ч~тл',   u'чител'),
    (u'чн~к',   u'ченик'),
    (u'чн~ц',   u'чениц'),
    (u'чн~',    u'чен'),
    (u'чСтн',   u'честн'),
    (u'чтСн',   u'честн'),
    (u'чСт',    u'чист'),
    (u'чтС',    u'чист'),
    (u'чт~л',   u'чител'),
)
