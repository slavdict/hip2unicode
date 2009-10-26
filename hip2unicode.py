#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def hip2unicode(str):
    
    """ Преобразует символы, 
    закодированные HIP, в Unicode """

    # глобальные тэги переключения систем письма
    script_tags = (
        u'<::слав>',
        u'<::греч>',
        u'<::рус>',
        u'<::лат>',
        u'<::глаг>',
    )
    
    # разбиваем текст на части по глобальным 
    # тэгам указания письменности
    marked_text_fragments = [(u'<::слав>', str),] # по умолчанию предполагаем, что передаваемая строка представляет собой текст на церковно-славянском/старославянском языке
    for tag in script_tags:
        _marked_text_fragments = marked_text_fragments[:]
        for fragment_number, (fragment_tag, fragment) in enumerate(_marked_text_fragments):
            new_fragments = fragment.split(tag)
            new_marked_fragments = [(tag, new_fragments[0]),]
            new_marked_fragments.extend(
                [ (fragment_tag, f) for f in new_fragments[1:] ]
            )
            marked_text_fragments[fragment_number : fragment_number + 1] = new_marked_fragments 


    return marked_text_fragments
