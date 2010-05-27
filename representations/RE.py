# -*- coding: UTF-8 -*-

"""
Модуль содержит набор функций
для формирования строк,
представляющих собой регулрные выражения

"""

EMPTY_STRING = u''

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

def initial_letter(letters, *list_of_strings):
    x = EMPTY_STRING.join(list_of_strings)
    y = letters
    return u'(^[%s])|([^%s][%s]))' % (x, y, x)

def RE_right_letter_non(string_of_letters):
    return u'((?![%s])|$)' % string_of_letters

