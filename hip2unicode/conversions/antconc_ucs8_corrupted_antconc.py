"""
Устранение вставленных авторами в текст Антконка символов UCS8

"""

conversion = (
    ('A', 'а`'),
    ('B', 'ѣ^'),
    ('C', 'С'),
    ('D', 'дС'),
    ('E', 'е`'),
    ('F', 'Ѳ'),
    ('G', 'г~'),
    ('H', "ѡ'"),
    ('I', 'І'),
    ('J', 'і`'),
    ('K', 'ٖٖٖꙖ'),
    ('L', 'лД'),
    ('M', 'Ѵ'),
    ('N', 'Ѻ'),
    ('O', 'Ѻ'),
    ('P', 'Ѱ'),
    ('Q', 'Ѽ'),
    ('R', 'р~'),
    ('S', 'ѧ`'),
    ('T', 'Ѿ'),
    ('U', 'Ѹ'),
    ('V', 'Ѵ'),
    ('W', 'Ѡ'),
    ('X', 'Ѯ'),
    ('Y', 'ꙋ`'),
    ('Z', 'Ѧ'),
    ('a', "а'"),
    ('b', 'О'),
    ('c', 'С'),
    ('d', 'Д'),
    ('e', "е'"),
    ('f', 'ѳ'),
    ('g', 'Г'),
    ('h', "ы'"),
    ('i', 'і'),
    ('j', "і'"),
    ('k', 'ꙗ'),
    ('l', 'л~'),
    ('m', 'ѵ'),
    ('n', 'ѻ'),
    ('o', 'ѻ'),
    ('p', 'ѱ'),
    ('q', 'ѽ'),
    ('r', 'рС'),
    ('s', "ѧ'"),
    ('t', 'ѿ'),
    ('u', 'ѹ'),
    ('v', 'ѵ'),
    ('w', 'ѡ'),
    ('x', 'ѯ'),
    ('y', "ꙋ'"),
    ('z', 'ѧ'),
    ('Ё', 'ѣ`'),
    ('Э', 'Ѣ'),
    ('Я', 'Ꙗ'),
    ('ё', "ѣ'"),
    ('э', 'ѣ'),
    ('я', 'ꙗ'),
)
