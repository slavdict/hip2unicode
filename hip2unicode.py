#!/usr/bin/env python
# -*- coding: UTF-8 -*-

cslav_regexps = {
    
    """ Regular expressions for character replacement
    in text marked as being typed in Church Slavonic script
    (script tag <::слав> or without any script tag
    if no script tag is in the document) """

    # А -- \u0410 -- CYRILLIC CAPITAL LETTER A
    ur'[AА]'    # \u0041 LATIN CAPITAL LETTER A
    :           # \u0410 CYRILLIC CAPITAL LETTER A
    ur'А',

    # а -- \u0430 -- CYRILLIC SMALL LETTER A
    ur'[aа]'    # \u0061 LATIN SMALL LETTER A
                # \u0430 CYRILLIC SMALL LETTER A
    :
    ur'а',
 
}

