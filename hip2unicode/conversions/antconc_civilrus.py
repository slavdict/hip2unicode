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
    ('##',         ''),
    ('=',          ''),
    (AKUT,         ''),
    (GRAVIS,       ''),
    (CIRKUMFLEKS,  ''),

    ('апСтл',  'апостол'),
    ('апСл',   'апостол'),
    ('апС',    'апос'),  # апостол...
    ('бг~',    'бог'),
    ('бж~тв',  'божеств'),
    ('бж~',    'бож'),
    ('бжСтв',  'божеств'),
    ('бз~',    'боз'),
    ('бл~г',   'благ'),
    ('бл~ж',   'блаж'),
    ('бл~з',   'блаз'),
    ('блГв',   'благов'),
    ('блгДт',  'благодат'),
    ('блгСв',  'благослов'),
    ('блгСл',  'благосл'),
    ('блгС',   'благос'),
    ('бцД',    'богородиц'),
    ('влДк',   'владык'),
    ('влДц',   'владыц'),
    ('влДчц',  'владычиц'),
    ('влДч',   'владыч'),
    ('ѵГл',    'вангел'), # Евангел...
    ('ѵГ',     'ванг'),   # Евангел...
    ('гг[еє~]л', 'нгел'), # ангел
    ('гл~г',   'глаг'),   # глагол...
    ('гл~',    'глагол'),
    ('глВ',    'глав'),
    ('гдСнь',  'господень'),
    ('гдСв',   'господев'),
    ('гдС',    'господ'),
    ('гпСж',   'госпож'),
    ('дв~д',   'давид'),
    ('дв~',    'дев'),
    ('двСтв',  'девств'),
    ('дс~',    'дус'),
    ('дх~',    'дух'),
    ('дш~',    'душ'),
    ('и~с',    'исус'),
    ('іи~л',   'израил'),
    ('кр~с',   'крес'),
    ('кр~ш',   'креш'),
    ('крСт',   'крест'),
    ('крСні',  'кресени'), # Это правило не 100%-ное. Слово ``воскрСнiи``
        # может быть как формой предл.п. сущ. ВОСКРЕСЕНИЕ, так и формой мн.ч.
        # прилагательного ВОСКРЕСНЫЙ, которая встречается, правда, достаточно
        # редко. Возможно, есть и другие формы, для которых это правило также
        # будет работать неправильно.
    ('крС',    'крес'),
    ('мДр',    'мудр'),
    ('мл~тв',  'молитв'),
    ('млДнцъ', 'младенец'),
    ('млДн',   'младен'),
    ('млСрд',  'милосерд'),
    ('млСт',   'милост'),
    ('млС',    'милос'),
    ('мт~р',   'матер'),
    ('мт~',    'мат'),
    ('мр~і',   'мари'),
    ('мРк',    'мярек'),  # Имярек
    ('мч~нк',  'мученик'),
    ('мч~нц',  'мучениц'),
    ('мч~нч',  'мученич'),
    ('мч~н',   'мучен'),
    ('мцС',    'месяц'),
    ('нб~с',   'небес'),
    ('нбСс',   'небес'),
    ('нбС',    'небес'),
    ('нб~',    'неб'),
    ('нлД',    'недел'),
    ('нн~',    'нын'),
    ("ѻ'ч~ь",  'отечь'),
    ("ѻ'ч~єс", 'отечес'),
    ("ѻ'ч~ес", 'отечес'),
    ("ѻ'ч~",   'отч'),
    ("ѻц~ъ",   'отец'),
    ("ѻц~",    'отц'),
    ('првДнъ', 'праведен'),
    ('првДн',  'праведн'),
    ('прДтч',  'предтеч'), # Предтеча
    ('прДт',   'предт'),   # Предтеча
    ('прпДб',  'преподоб'),
    ('прОр',   'прор'),    # Пророк
    ('прСн',   'присн'),
    ('прСт',   'прест'),
    ('прчСт',  'пречист'),
    ('пСкп',   'пископ'),  # епископ
    ('пСк',    'писк'),
    ('ржСтв',  'рождеств'),
    ('рСл',    'русал'),   # Иерусалим
    ('сл~нц',  'солнц'),
    ('сн~',    'сын'),
    ('сп~с',   'спас'),
    ('спСн',   'спасен'),
    ('срДц',   'сердц'),
    ('срДч',   'сердеч'),
    ('ст~',    'свят'),
    ('стрСт',  'страст'),
    ('сХ',     'стих'),
    ('стХр',   'стихир'),
    ('сщ~',    'свящ'),
    ('трОц',   'троиц'),
    ('трОч',   'троич'),
    ('трСт',   'трисвят'),
    ('хрСт',   'христ'),
    ('цр~к',   'церк'),
    ('цр~',    'цар'),
    ('црС',    'царс'),
    ('чл~в',   'челов'),
    ('ч~нк',   'ченик'),
    ('ч~нц',   'чениц'),
    ('ч~тл',   'чител'),
    ('чн~к',   'ченик'),
    ('чн~ц',   'чениц'),
    ('чн~',    'чен'),
    ('чСтн',   'честн'),
    ('чтСн',   'честн'),
    ('чСт',    'чист'),
    ('чтС',    'чист'),
    ('чт~л',   'чител'),

    (SMALL_WIDE_ESTJ,   'е'),
    (SMALL_ZELO,        'з'),
    (SMALL_I,           'и'),
    (SMALL_MONOGRAPH_UK,    'у'),
    (SMALL_DIGRAPH_UK,      'у'),
    (SMALL_OMEGA,       'о'),
    (SMALL_JATJ,        'е'),
    (SMALL_I_AZ,        'я'),
    (SMALL_JUS_MALYJ,   'я'),
    (SMALL_KSI,         'кс'),
    (SMALL_PSI,         'пс'),
    (SMALL_FITA,        'ф'),
    ('а' + SMALL_IZHICA,   'ав'),
    ('е' + SMALL_IZHICA,   'ев'),
    (SMALL_WIDE_ESTJ + SMALL_IZHICA,    'ев'),
    (SMALL_IZHICA,      'и'),
    (SMALL_WIDE_ON,     'о'),
    (SMALL_OLE,         'о'),
    (SMALL_OT,          'от'),

    (TITLO,         '*'),
    (PAEROK,        'ъ'),
    (VEDI_TITLO,    '*'),
    (GLAGOLJ_TITLO, '*'),
    (DOBRO_TITLO,   '*'),
    (ZHIVETE_TITLO, '*'),
    (ZEMLJA_TITLO,  '*'),
    (NASH_TITLO,    '*'),
    (ON_TITLO,      '*'),
    (RCY_TITLO,     '*'),
    (SLOVO_TITLO,   '*'),
    (XER_TITLO,     'х'),
    (CHERVJ_TITLO,  '*'),
    # Все случаи с паерками уже учтены (см. выше),
    # все паерки конвертируется в твёрдые знаки.
    ('ъ$', ''),
    ('ъа', 'а'),
    ('ъо', 'о'),
    ('ъу', 'у'),
    ('ъы', 'ы'),
    ('ъи', 'ы'),
)
