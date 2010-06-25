# -*- coding: UTF-8 -*-

"""
Модуль содержит набор функций
для формирования строк,
представляющих собой регулрные выражения

"""

EMPTY_STRING = u''

class REPR_ENVIRON:
    # следующую переменную необходимо инициализровать
    # при подключении модуля RE выражением вроде
    # [<символы, которые не могут входить в слово>]
    # либо [^<символы, составляющие слова>]
    NON_LETTERS = u''

def cat(*list_of_strings):
    return EMPTY_STRING.join(list_of_strings)

def token(*list_of_strings):
    return ur'[%s]' % EMPTY_STRING.join(list_of_strings)
    
def neg_token(*list_of_strings):
    return ur'[^%s]' % EMPTY_STRING.join(list_of_strings)

def left_context(*list_of_strings):
    return ur'(?<=%s)' % EMPTY_STRING.join(list_of_strings)
    
def neg_left_context(*list_of_strings):
    return u'(?<!%s)' % EMPTY_STRING.join(list_of_strings)

def right_context(*list_of_strings):
    return ur'(?=%s)' % EMPTY_STRING.join(list_of_strings)
    
def neg_right_context(*list_of_strings):
    return u'(?!%s)' % EMPTY_STRING.join(list_of_strings)

def initial(*list_of_strings):
    x = cat(*list_of_strings)
    return u'((^%s)|(%s%s))' % (x, REPR_ENVIRON.NON_LETTERS, x)

def initial_context(*list_of_strings):
    x = cat(*list_of_strings)
    return u'((?<=^%s)|(?<=%s%s))' % (x, REPR_ENVIRON.NON_LETTERS, x)
