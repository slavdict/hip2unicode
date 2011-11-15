# -*- coding: UTF-8 -*-

conversion = ()

NOTLTR = u'[^a-uw-zA-UW-Z`\\^_@"\'\u0080-\u0095\u0098-\u009f\u00a1-\u00a3\u00a5-\u00ab\u00ad-\u00b5\u00b8-\u00ff]'

    # make sigma into final form if not followed by a letter
    (u's' + NOTLTR, u'v'),


    (u'\u00CF'            ,  u'Hr'),
    (u'\u00BF'            ,  u'hr'),

    (u'\u00ADA'        ,  u"HA'"),
    (u'\u00AEA'        ,  u'HA`'),
    (u'\u00AFA'        ,  u'HA^'),
    (u'\u00A9A'        ,  u"hA'"),
    (u'\u00AAA'        ,  u'hA`'),
    (u'\u00ABA'        ,  u'hA^'),

    (u'\u00ADE'        ,  u"HE'"),
    (u'\u00A9E'        ,  u"hE'"),
    (u'\u00AAE'        ,  u'hE`'),

    (u'\u00ADJ'        ,  u"HJ'"),
    (u'\u00AEJ'        ,  u'HJ`'),
    (u'\u00AFJ'        ,  u'HJ^'),
    (u'\u00A9J'        ,  u"hJ'"),
    (u'\u00AAJ'        ,  u'hJ`'),
    (u'\u00ABJ'        ,  u'hJ^'),

    (u'\u00ADI'        ,  u"HI'"),
    (u'\u00AFI'        ,  u'HI^'),
    (u'\u00A9I'        ,  u"hI'"),
    (u'\u00AAI'        ,  u'hI`'),
    (u'\u00ABI'        ,  u'hI^'),

    (u'\u00ADO'        ,  u"HO'"),
    (u'\u00AEO'        ,  u'HO`'),
    (u'\u00A9O'        ,  u"hO'"),
    (u'\u00AAO'        ,  u'hO`'),

    (u'\u00ADU'        ,  u"HU'"),
    (u'\u00AEU'        ,  u'HU`'),
    (u'\u00AFU'        ,  u'HU^'),
    (u'\u00A9U'        ,  u"hU'"),
    (u'\u00AAU'        ,  u'hU`'),
    (u'\u00ABU'        ,  u'hU^'),

    (u'\u00ADW'        ,  u"HW'"),
    (u'\u00AEW'        ,  u'HW`'),
    (u'\u00AFW'        ,  u'HW^'),
    (u'\u00A9W'        ,  u"hW'"),
    (u'\u00AAW'        ,  u'hW`'),
    (u'\u00ABW'        ,  u'hW^'),

    (u'\u0087'            ,  u'Ha'),
    (u'\u0080'            ,  u"a'"),
    (u'\u0088'            ,  u"Ha'"),
    (u'\u0081'            ,  u'a`'),
    (u'\u0089'            ,  u'Ha`'),
    (u'\u0082'            ,  u'a^'),
    (u'\u008A'            ,  u'Ha^'),
    (u'\u0083'            ,  u'ha'),
    (u'\u0084'            ,  u"ha'"),
    (u'\u0085'            ,  u'ha`'),
    (u'\u0086'            ,  u'ha^'),

    (u'\u009D'            ,  u'He'),
    (u'\u0099'            ,  u"e'"),
    (u'\u009E'            ,  u"He'"),
    (u'\u009A'            ,  u'e`'),
    (u'\u009B'            ,  u'he'),
    (u'\u009C'            ,  u"he'"),
    (u'\u009F'            ,  u'he`'),

    (u'\u00D7'            ,  u'Hj'),
    (u'\u00D0'            ,  u"j'"),
    (u'\u00D8'            ,  u"Hj'"),
    (u'\u00D1'            ,  u'j`'),
    (u'\u00D9'            ,  u'Hj`'),
    (u'\u00D2'            ,  u'j^'),
    (u'\u00DA'            ,  u'Hj^'),
    (u'\u00D3'            ,  u'hj'),
    (u'\u00D4'            ,  u"hj'"),
    (u'\u00D5'            ,  u'hj`'),
    (u'\u00D6'            ,  u'hj^'),

    (u'\u00B8'            ,  u'Hi'),
    (u'\u00B0'            ,  u"i'"),
    (u'\u00B9'            ,  u"Hi'"),
    (u'\u00B1'            ,  u'i`'),
    (u'\u00B2'            ,  u'i^'),
    (u'\u00BA'            ,  u'Hi^'),
    (u'\u00B3'            ,  u'hi'),
    (u'\u00B4'            ,  u"hi'"),
    (u'\u00BE'            ,  u'hi`'),
    (u'\u00B5'            ,  u'hi^'),

    (u'\u00EC'            ,  u'Ho'),
    (u'\u00E7'            ,  u"o'"),
    (u'\u00ED'            ,  u"Ho'"),
    (u'\u00E8'            ,  u'o`'),
    (u'\u00CE'            ,  u'Ho`'),
    (u'\u00E9'            ,  u'ho'),
    (u'\u00EA'            ,  u"ho'"),
    (u'\u00EB'            ,  u'ho`'),

    (u'\u00C7'            ,  u'Hu'),
    (u'\u00C0'            ,  u"u'"),
    (u'\u00C8'            ,  u"Hu'"),
    (u'\u00C1'            ,  u'u`'),
    (u'\u00C9'            ,  u'Hu`'),
    (u'\u00C2'            ,  u'u^'),
    (u'\u00CA'            ,  u'Hu^'),
    (u'\u00C3'            ,  u'hu'),
    (u'\u00C4'            ,  u"hu'"),
    (u'\u00C5'            ,  u'hu`'),
    (u'\u00C6'            ,  u'hu^'),

    (u'\u00F7'            ,  u'Hw'),
    (u'\u00F0'            ,  u"w'"),
    (u'\u00F8'            ,  u"Hw'"),
    (u'\u00F1'            ,  u'w`'),
    (u'\u00F9'            ,  u'Hw`'),
    (u'\u00F2'            ,  u'w^'),
    (u'\u00FA'            ,  u'Hw^'),
    (u'\u00F3'            ,  u'hw'),
    (u'\u00F4'            ,  u"hw'"),
    (u'\u00F5'            ,  u'hw`'),
    (u'\u00F6'            ,  u'hw^'),

    (u'\u008B'            ,  u'a_'),
    (u'\u0093'            ,  u'Ha_'),
    (u'\u008C'            ,  u"a_'"),
    (u'\u0094'            ,  u"Ha_'"),
    (u'\u008D'            ,  u'a_`'),
    (u'\u0095'            ,  u'Ha_`'),
    (u'\u008E'            ,  u'a_^'),
    (u'\u0098'            ,  u'Ha_^'),
    (u'\u008F'            ,  u'ha_'),
    (u'\u0090'            ,  u"ha_'"),
    (u'\u0091'            ,  u'ha_`'),
    (u'\u0092'            ,  u'ha_^'),

    (u'\u00DB'            ,  u'j_'),
    (u'\u00E3'            ,  u'Hj_'),
    (u'\u00DC'            ,  u"j_'"),
    (u'\u00E4'            ,  u"Hj_'"),
    (u'\u00DD'            ,  u'j_`'),
    (u'\u00E5'            ,  u'Hj_`'),
    (u'\u00DE'            ,  u'j_^'),
    (u'\u00E6'            ,  u'Hj_^'),
    (u'\u00DF'            ,  u'hj_'),
    (u'\u00E0'            ,  u"hj_'"),
    (u'\u00E1'            ,  u'hj_`'),
    (u'\u00E2'            ,  u'hj_^'),

    (u'\u00FB'            ,  u'w_'),
    (u'\u00A5'            ,  u'Hw_'),
    (u'\u00FC'            ,  u"w_'"),
    (u'\u00A6'            ,  u"Hw_'"),
    (u'\u00FD'            ,  u'w_`'),
    (u'\u00A7'            ,  u'Hw_`'),
    (u'\u00FE'            ,  u'w_^'),
    (u'\u00A8'            ,  u'Hw_^'),
    (u'\u00FF'            ,  u'hw_'),
    (u'\u00A1'            ,  u"hw_'"),
    (u'\u00A2'            ,  u'hw_`'),
    (u'\u00A3'            ,  u'hw_^'),

    (u'\u00BB'            ,  u'i"'),
    (u'\u00BC'            ,  u"i\"'"),
    (u'\u00BD'            ,  u'i"`'),

    (u'\u00CB'            ,  u'u"'),
    (u'\u00CC'            ,  u"u"'"),
    (u'\u00CD'            ,  u'u"`'),

    (u'A\u00B8'        ,  u'HAi'),
    (u'A\u00B9'        ,  u"HAi'"),
    (u'A\u00BA'        ,  u'HAi^'),
    (u'A\u00B3'        ,  u'hAi'),
    (u'A\u00B4'        ,  u"hAi'"),
    (u'A\u00BE'        ,  u'hAi`'),
    (u'A\u00B5'        ,  u'hAi^'),

    (u'a\u00B8'        ,  u'Hai'),
    (u'a\u00B0'        ,  u"ai'"),
    (u'a\u00B9'        ,  u"Hai'"),
    (u'a\u00B1'        ,  u'ai`'),
    (u'a\u00B2'        ,  u'ai^'),
    (u'a\u00BA'        ,  u'Hai^'),
    (u'a\u00B3'        ,  u'hai'),
    (u'a\u00B4'        ,  u"hai'"),
    (u'a\u00BE'        ,  u'hai`'),
    (u'a\u00B5'        ,  u'hai^'),

    (u'E\u00B8'        ,  u'HEi'),
    (u'E\u00B9'        ,  u"HEi'"),
    (u'E\u00BA'        ,  u'HEi^'),
    (u'E\u00B3'        ,  u'hEi'),
    (u'E\u00B4'        ,  u"hEi'"),
    (u'E\u00BE'        ,  u'hEi`'),
    (u'E\u00B5'        ,  u'hEi^'),

    (u'e\u00B8'        ,  u'Hei'),
    (u'e\u00B0'        ,  u"ei'"),
    (u'e\u00B9'        ,  u"Hei'"),
    (u'e\u00B1'        ,  u'ei`'),
    (u'e\u00B2'        ,  u'ei^'),
    (u'e\u00BA'        ,  u'Hei^'),
    (u'e\u00B3'        ,  u'hei'),
    (u'e\u00B4'        ,  u"hei'"),
    (u'e\u00BE'        ,  u'hei`'),
    (u'e\u00B5'        ,  u'hei^'),

    (u'O\u00B8'        ,  u'HOi'),
    (u'O\u00B9'        ,  u"HOi'"),
    (u'O\u00BA'        ,  u'HOi^'),
    (u'O\u00B3'        ,  u'hOi'),
    (u'O\u00B4'        ,  u"hOi'"),
    (u'O\u00BE'        ,  u'hOi`'),
    (u'O\u00B5'        ,  u'hOi^'),

    (u'o\u00B8'        ,  u'Hoi'),
    (u'o\u00B0'        ,  u"oi'"),
    (u'o\u00B9'        ,  u"Hoi'"),
    (u'o\u00B1'        ,  u'oi`'),
    (u'o\u00B2'        ,  u'oi^'),
    (u'o\u00BA'        ,  u'Hoi^'),
    (u'o\u00B3'        ,  u'hoi'),
    (u'o\u00B4'        ,  u"hoi'"),
    (u'o\u00BE'        ,  u'hoi`'),
    (u'o\u00B5'        ,  u'hoi^'),

    (u'U\u00B8'        ,  u'HUi'),
    (u'U\u00B9'        ,  u"HUi'"),
    (u'U\u00BA'        ,  u'HUi^'),
    (u'U\u00B3'        ,  u'hUi'),
    (u'U\u00B4'        ,  u"hUi'"),
    (u'U\u00BE'        ,  u'hUi`'),
    (u'U\u00B5'        ,  u'hUi^'),

    (u'u\u00B8'        ,  u'Hui'),
    (u'u\u00B0'        ,  u"ui'"),
    (u'u\u00B9'        ,  u"Hui'"),
    (u'u\u00B1'        ,  u'ui`'),
    (u'u\u00B2'        ,  u'ui^'),
    (u'u\u00BA'        ,  u'Hui^'),
    (u'u\u00B3'        ,  u'hui'),
    (u'u\u00B4'        ,  u"hui'"),
    (u'u\u00BE'        ,  u'hui`'),
    (u'u\u00B5'        ,  u'hui^'),

    (u'A\u00C7'        ,  u'HAu'),
    (u'A\u00C8'        ,  u"HAu'"),
    (u'A\u00C9'        ,  u'HAu`'),
    (u'A\u00CA'        ,  u'HAu^'),
    (u'A\u00C3'        ,  u'hAu'),
    (u'A\u00C4'        ,  u"hAu'"),
    (u'A\u00C5'        ,  u'hAu`'),
    (u'A\u00C6'        ,  u'hAu^'),

    (u'a\u00C7'        ,  u'Hau'),
    (u'a\u00C0'        ,  u"au'"),
    (u'a\u00C8'        ,  u"Hau'"),
    (u'a\u00C1'        ,  u'au`'),
    (u'a\u00C9'        ,  u'Hau`'),
    (u'a\u00C2'        ,  u'au^'),
    (u'a\u00CA'        ,  u'Hau^'),
    (u'a\u00C3'        ,  u'hau'),
    (u'a\u00C4'        ,  u"hau'"),
    (u'a\u00C5'        ,  u'hau`'),
    (u'a\u00C6'        ,  u'hau^'),

    (u'E\u00C7'        ,  u'HEu'),
    (u'E\u00C8'        ,  u"HEu'"),
    (u'E\u00C9'        ,  u'HEu`'),
    (u'E\u00CA'        ,  u'HEu^'),
    (u'E\u00C3'        ,  u'hEu'),
    (u'E\u00C4'        ,  u"hEu'"),
    (u'E\u00C5'        ,  u'hEu`'),
    (u'E\u00C6'        ,  u'hEu^'),

    (u'e\u00C7'        ,  u'Heu'),
    (u'e\u00C0'        ,  u"eu'"),
    (u'e\u00C8'        ,  u"Heu'"),
    (u'e\u00C1'        ,  u'eu`'),
    (u'e\u00C9'        ,  u'Heu`'),
    (u'e\u00C2'        ,  u'eu^'),
    (u'e\u00CA'        ,  u'Heu^'),
    (u'e\u00C3'        ,  u'heu'),
    (u'e\u00C4'        ,  u"heu'"),
    (u'e\u00C5'        ,  u'heu`'),
    (u'e\u00C6'        ,  u'heu^'),

    (u'J\u00C7'        ,  u'HJu'),
    (u'J\u00C8'        ,  u"HJu'"),
    (u'J\u00C9'        ,  u'HJu`'),
    (u'J\u00CA'        ,  u'HJu^'),
    (u'J\u00C3'        ,  u'hJu'),
    (u'J\u00C4'        ,  u"hJu'"),
    (u'J\u00C5'        ,  u'hJu`'),
    (u'J\u00C6'        ,  u'hJu^'),

    (u'j\u00C7'        ,  u'Hju'),
    (u'j\u00C0'        ,  u"ju'"),
    (u'j\u00C8'        ,  u"Hju'"),
    (u'j\u00C1'        ,  u'ju`'),
    (u'j\u00C9'        ,  u'Hju`'),
    (u'j\u00C2'        ,  u'ju^'),
    (u'j\u00CA'        ,  u'Hju^'),
    (u'j\u00C3'        ,  u'hju'),
    (u'j\u00C4'        ,  u"hju'"),
    (u'j\u00C5'        ,  u'hju`'),
    (u'j\u00C6'        ,  u'hju^'),

    (u'O\u00C7'        ,  u'HOu'),
    (u'O\u00C8'        ,  u"HOu'"),
    (u'O\u00C9'        ,  u'HOu`'),
    (u'O\u00CA'        ,  u'HOu^'),
    (u'O\u00C3'        ,  u'hOu'),
    (u'O\u00C4'        ,  u"hOu'"),
    (u'O\u00C5'        ,  u'hOu`'),
    (u'O\u00C6'        ,  u'hOu^'),

    (u'o\u00C7'        ,  u'Hou'),
    (u'o\u00C0'        ,  u"ou'"),
    (u'o\u00C8'        ,  u"Hou'"),
    (u'o\u00C1'        ,  u'ou`'),
    (u'o\u00C9'        ,  u'Hou`'),
    (u'o\u00C2'        ,  u'ou^'),
    (u'o\u00CA'        ,  u'Hou^'),
    (u'o\u00C3'        ,  u'hou'),
    (u'o\u00C4'        ,  u"hou'"),
    (u'o\u00C5'        ,  u'hou`'),
    (u'o\u00C6'        ,  u'hou^'),

    (u'HA\u00BB'       ,  u'HAi"'),
    (u'HA\u00BC'       ,  u"HAi\"'"),
    (u'HA\u00BD'       ,  u'HAi"`'),
    (u'hA\u00BB'       ,  u'hAi"'),
    (u'hA\u00BC'       ,  u"hAi\"'"),
    (u'hA\u00BD'       ,  u'hAi"`'),
    (u'a\u00BB'        ,  u'ai"'),
    (u'\u0087\u00BB'       ,  u'Hai"'),
    (u'a\u00BC'        ,  u"ai\"'"),
    (u'\u0087\u00BC'       ,  u"Hai\"'"),
    (u'a\u00BD'        ,  u'ai"`'),
    (u'\u0087\u00BD'       ,  u'Hai"`'),
    (u'\u0083\u00BB'       ,  u'hai"'),
    (u'\u0083\u00BC'       ,  u"hai\"'"),
    (u'\u0083\u00BD'       ,  u'hai"`'),

    (u'HE\u00BB'       ,  u'HEi"'),
    (u'HE\u00BC'       ,  u"HEi\"'"),
    (u'HE\u00BD'       ,  u'HEi"`'),
    (u'hE\u00BB'       ,  u'hEi"'),
    (u'hE\u00BC'       ,  u"hEi\"'"),
    (u'hE\u00BD'       ,  u'hEi"`'),
    (u'e\u00BB'        ,  u'ei"'),
    (u'\u009D\u00BB'       ,  u'Hei"'),
    (u'e\u00BC'        ,  u"ei\"'"),
    (u'\u009D\u00BC'       ,  u"Hei\"'"),
    (u'e\u00BD'        ,  u'ei"`'),
    (u'\u009D\u00BD'       ,  u'Hei"`'),
    (u'\u009B\u00BB'       ,  u'hei"'),
    (u'\u009B\u00BC'       ,  u"hei\"'"),
    (u'\u009B\u00BD'       ,  u'hei"`'),

>>>>>>>
    (u''HO' \u00BB'       ,  u'HOi"'),
    (u''HO' \u00BC'       ,  u"HOi"'"),
    (u''HO' \u00BD'       ,  u'HOi"`'),
    (u''hO' \u00BB'       ,  u'hOi"'),
    (u''hO' \u00BC'       ,  u"hOi"'"),
    (u''hO' \u00BD'       ,  u'hOi"`'),
    (u''o' \u00BB'        ,  u'oi"'),
    (u'\u00EC \u00BB'       ,  u'Hoi"'),
    (u''o' \u00BC'        ,  u"oi"'"),
    (u'\u00EC \u00BC'       ,  u"Hoi"'"),
    (u''o' \u00BD'        ,  u'oi"`'),
    (u'\u00EC \u00BD'       ,  u'Hoi"`'),
    (u'\u00E9 \u00BB'       ,  u'hoi"'),
    (u'\u00E9 \u00BC'       ,  u"hoi"'"),
    (u'\u00E9 \u00BD'       ,  u'hoi"`'),

    (u''HU' \u00BB'       ,  u'HUi"'),
    (u''HU' \u00BC'       ,  u"HUi"'"),
    (u''HU' \u00BD'       ,  u'HUi"`'),
    (u''hU' \u00BB'       ,  u'hUi"'),
    (u''hU' \u00BC'       ,  u"hUi"'"),
    (u''hU' \u00BD'       ,  u'hUi"`'),
    (u''u' \u00BB'        ,  u'ui"'),
    (u'\u00C7 \u00BB'       ,  u'Hui"'),
    (u''u' \u00BC'        ,  u"ui"'"),
    (u'\u00C7 \u00BC'       ,  u"Hui"'"),
    (u''u' \u00BD'        ,  u'ui"`'),
    (u'\u00C7 \u00BD'       ,  u'Hui"`'),
    (u'\u00C3 \u00BB'       ,  u'hui"'),
    (u'\u00C3 \u00BC'       ,  u"hui"'"),
    (u'\u00C3 \u00BD'       ,  u'hui"`'),

    (u''HA' \u00CB'       ,  u'HAu"'),
    (u''HA' \u00CC'       ,  u"HAu"'"),
    (u''HA' \u00CD'       ,  u'HAu"`'),
    (u''hA' \u00CB'       ,  u'hAu"'),
    (u''hA' \u00CC'       ,  u"hAu"'"),
    (u''hA' \u00CD'       ,  u'hAu"`'),
    (u''a' \u00CB'        ,  u'au"'),
    (u'\u0087 \u00CB'       ,  u'Hau"'),
    (u''a' \u00CC'        ,  u"au"'"),
    (u'\u0087 \u00CC'       ,  u"Hau"'"),
    (u''a' \u00CD'        ,  u'au"`'),
    (u'\u0087 \u00CD'       ,  u'Hau"`'),
    (u'\u0083 \u00CB'       ,  u'hau"'),
    (u'\u0083 \u00CC'       ,  u"hau"'"),
    (u'\u0083 \u00CD'       ,  u'hau"`'),

    (u''HE' \u00CB'       ,  u'HEu"'),
    (u''HE' \u00CC'       ,  u"HEu"'"),
    (u''HE' \u00CD'       ,  u'HEu"`'),
    (u''hE' \u00CB'       ,  u'hEu"'),
    (u''hE' \u00CC'       ,  u"hEu"'"),
    (u''hE' \u00CD'       ,  u'hEu"`'),
    (u''e' \u00CB'        ,  u'eu"'),
    (u'\u009D \u00CB'       ,  u'Heu"'),
    (u''e' \u00CC'        ,  u"eu"'"),
    (u'\u009D \u00CC'       ,  u"Heu"'"),
    (u''e' \u00CD'        ,  u'eu"`'),
    (u'\u009D \u00CD'       ,  u'Heu"`'),
    (u'\u009B \u00CB'       ,  u'heu"'),
    (u'\u009B \u00CC'       ,  u"heu"'"),
    (u'\u009B \u00CD'       ,  u'heu"`'),

    (u''HJ' \u00CB'       ,  u'HJu"'),
    (u''HJ' \u00CC'       ,  u"HJu"'"),
    (u''HJ' \u00CD'       ,  u'HJu"`'),
    (u''hJ' \u00CB'       ,  u'hJu"'),
    (u''hJ' \u00CC'       ,  u"hJu"'"),
    (u''hJ' \u00CD'       ,  u'hJu"`'),
    (u''j' \u00CB'        ,  u'ju"'),
    (u'\u00D7 \u00CB'       ,  u'Hju"'),
    (u''j' \u00CC'        ,  u"ju"'"),
    (u'\u00D7 \u00CC'       ,  u"Hju"'"),
    (u''j' \u00CD'        ,  u'ju"`'),
    (u'\u00D7 \u00CD'       ,  u'Hju"`'),
    (u'\u00D3 \u00CB'       ,  u'hju"'),
    (u'\u00D3 \u00CC'       ,  u"hju"'"),
    (u'\u00D3 \u00CD'       ,  u'hju"`'),

    (u''HO' \u00CB'       ,  u'HOu"'),
    (u''HO' \u00CC'       ,  u"HOu"'"),
    (u''HO' \u00CD'       ,  u'HOu"`'),
    (u''hO' \u00CB'       ,  u'hOu"'),
    (u''hO' \u00CC'       ,  u"hOu"'"),
    (u''hO' \u00CD'       ,  u'hOu"`'),
    (u''o' \u00CB'        ,  u'ou"'),
    (u'\u00EC \u00CB'       ,  u'Hou"'),
    (u''o' \u00CC'        ,  u"ou"'"),
    (u'\u00EC \u00CC'       ,  u"Hou"'"),
    (u''o' \u00CD'        ,  u'ou"`'),
    (u'\u00EC \u00CD'       ,  u'Hou"`'),
    (u'\u00E9 \u00CB'       ,  u'hou"'),
    (u'\u00E9 \u00CC'       ,  u"hou"'"),
    (u'\u00E9 \u00CD'       ,  u'hou"`'),

    (u'\u00AD'            ,  u"H'"),
    (u'\u00AE'            ,  u'H`'),
    (u'\u00AF'            ,  u'H^'),
    (u'\u00A9'            ,  u"h'"),
    (u'\u00AA'            ,  u'h`'),
    (u'\u00AB'            ,  u'h^'),

    (u'\u00EE'            ,  u"\"'"),
    (u'\u00EF'            ,  u'"`'),

; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Pass(Byte)
; shuffle marks, as Unicode canonical order does not correspond to Galatia order

Class[dia] = ('`' "'" '^' '"')

'_' ([dia]+)=dias	<>	@dias '_'

; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Pass(Byte_Unicode)

; Now make the jump from byte to Unicode space.
; Here, we deal only with the decomposed forms, not precomposed.

ByteDefault			183			; 183 is "bullet" in the SIL Greek Display encoding
								; (note that this is actually a valid character code,
								; though probably not often used in legacy Greek text)
UniDefault			replacement_character

; there are separate namespaces for Byte and Unicode classes,
; allowing us to use the same name for classes with corresponding content

ByteClass	[CTL] = (   0x00 .. 0x1f     0x7f )
UniClass	[CTL] =	( U+0000 .. U+001f U+007f )

[CTL]	<>	[CTL]

' '		<>	space
'!'		<>	exclamation_mark
'"'		<>	combining_diaeresis
'#'		<>	no_break_space
'$'		<>	left_pointing_double_angle_quotation_mark
'%'		<>	right_pointing_double_angle_quotation_mark
'&'		<>	ampersand
"'"		<>	combining_acute_accent
'('		<>	left_parenthesis
')'		<>	right_parenthesis
'*'		<>	asterisk
'+'		<>	plus_sign
','		<>	comma
'-'		<>	hyphen_minus
'.'		<>	full_stop
'/'		<>	solidus

'0'		<>	digit_zero
'1'		<>	digit_one
'2'		<>	digit_two
'3'		<>	digit_three
'4'		<>	digit_four
'5'		<>	digit_five
'6'		<>	digit_six
'7'		<>	digit_seven
'8'		<>	digit_eight
'9'		<>	digit_nine
':'		<>	colon
';'		< 	greek_ano_teleia				; greek semicolon
';'		<>	middle_dot						; canonical decomposition of greek semicolon
'<'		<>	less_than_sign
'='		<>	equals_sign
'>'		<>	greater_than_sign
'?'		<	greek_question_mark
'?'		<>	semicolon						; canonical decomposition of greek question mark

'@'		<>	right_single_quotation_mark
'@'		<	modifier_letter_apostrophe		; mapping of '@' in earlier draft of this file
'A'		<>	greek_capital_letter_alpha
'B'		<>	greek_capital_letter_beta
'C'		<>	greek_capital_letter_chi
'D'		<>	greek_capital_letter_delta
'E'		<>	greek_capital_letter_epsilon
'F'		<>	greek_capital_letter_phi
'G'		<>	greek_capital_letter_gamma
'H'		<>	combining_comma_above
'I'		<>	greek_capital_letter_iota
'J'		<>	greek_capital_letter_eta
'K'		<>	greek_capital_letter_kappa
'L'		<>	greek_capital_letter_lamda
'M'		<>	greek_capital_letter_mu
'N'		<>	greek_capital_letter_nu
'O'		<>	greek_capital_letter_omicron

'P'		<>	greek_capital_letter_pi
'Q'		<>	greek_capital_letter_theta
'R'		<>	greek_capital_letter_rho
'S'		<>	greek_capital_letter_sigma
'T'		<>	greek_capital_letter_tau
'U'		<>	greek_capital_letter_upsilon
; 'V'			; <unused>
'W'		<>	greek_capital_letter_omega
'X'		<>	greek_capital_letter_xi
'Y'		<>	greek_capital_letter_psi
'Z'		<>	greek_capital_letter_zeta
'['		<>	left_square_bracket
'\'		<>	reverse_solidus
']'		<>	right_square_bracket
'^'		<>	combining_greek_perispomeni		; circumflex
'_'		<>	combining_greek_ypogegrammeni	; iota subscript

'`'		<>	combining_grave_accent
'a'		<>	greek_small_letter_alpha
'b'		<>	greek_small_letter_beta
'c'		<>	greek_small_letter_chi
'd'		<>	greek_small_letter_delta
'e'		<>	greek_small_letter_epsilon
'f'		<>	greek_small_letter_phi
'g'		<>	greek_small_letter_gamma
'h'		<>	combining_reversed_comma_above
'i'		<>	greek_small_letter_iota
'j'		<>	greek_small_letter_eta
'k'		<>	greek_small_letter_kappa
'l'		<>	greek_small_letter_lamda
'm'		<>	greek_small_letter_mu
'n'		<>	greek_small_letter_nu
'o'		<>	greek_small_letter_omicron

'p'		<>	greek_small_letter_pi
'q'		<>	greek_small_letter_theta
'r'		<>	greek_small_letter_rho
's'		<>	greek_small_letter_sigma
't'		<>	greek_small_letter_tau
'u'		<>	greek_small_letter_upsilon
'v'		<>	greek_small_letter_final_sigma
'w'		<>	greek_small_letter_omega
'x'		<>	greek_small_letter_xi
'y'		<>	greek_small_letter_psi
'z'		<>	greek_small_letter_zeta
'{'		<>	left_curly_bracket

'|'		<>	vertical_line
'|b'	<>	greek_beta_symbol				; curly beta
'|f'	<>	greek_small_letter_digamma		; digamma
'|G'	<>	greek_letter_digamma			; Digamma
'|g'	 >	greek_small_letter_digamma		; digamma (which SIL forms should have priority?)
'|w'	<>	greek_pi_symbol					; omega pi
'|q'	<>	greek_small_letter_koppa		; qoppa
'|Q'	<>	greek_letter_koppa				; Qoppa
'|R'	 >	greek_letter_koppa				; Qoppa
'|k'	 >	greek_small_letter_koppa		; qoppa
'|K'	 >	greek_letter_koppa				; Qoppa
'|p'	<>	greek_small_letter_sampi		; sampi
'|P'	<>	greek_letter_sampi				; Sampi
'|m'	 >	greek_small_letter_sampi		; sampi
'|M'	 >	greek_letter_sampi				; Sampi
'|s'	<>	greek_lunate_sigma_symbol		; lunate sigma
'|S'	 >	greek_lunate_sigma_symbol		; lunate sigma uppercase not available in Unicode
'|t'	<>	greek_small_letter_stigma		; stigma
'|T'	<>	greek_letter_stigma				; Stigma
'|i'	<>	turned_greek_small_letter_iota combining_tilde_below	; turned iota tilde below
'|U'	<>	greek_upsilon_with_hook_symbol	; Upsilon hook
'|h'	<>	greek_numeral_sign				; upper numeral sign
'|H'	<>	greek_lower_numeral_sign		; lower numeral sign
'|n'	<>	zero_width_joiner
'|#'	<>	zero_width_non_joiner

'}'		<>	right_curly_bracket
'~'		<>	em_dash

150		<>	en_dash
151		 >	em_dash
160		<>	no_break_space
164		<>	currency_sign
172		<>	not_sign
182		<>	pilcrow_sign
183		<>	bullet

; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Pass(Unicode)

; In Unicode space, reorder breathing/vowel sequences from SIL Basic to Unicode order

Class	[BR]		=	( combining_comma_above combining_reversed_comma_above )
Class	[aeo]		=	( U+0391 U+0395 U+039f U+03b1 U+03b5 U+03bf ) ; Unicode names are so verbose!
Class	[iu]		=	( U+0399 U+03a5 U+03b9 U+03c5 )
Class	[j]			=	( U+0397 U+03b7 )
Class	[u]			=	( U+03a5 U+03c5 )
Class	[i]			=	( U+0399 U+03b9 )
Class	[vowelrho]	=	( U+0391 U+0395 U+0399 U+039f U+03a5 U+0397 U+03a9 U+03a1 \
						  U+03b1 U+03b5 U+03b9 U+03bf U+03c5 U+03b7 U+03c9 U+03c1 )

[BR]=b [aeo]=v1 [iu]=v2 / _ combining_diaeresis	<>	@v1 @b @v2 / _ combining_diaeresis
[BR]=b [aeo]=v1 [iu]=v2							<>	@v1 @v2 @b
[BR]=b [j]=v1 [u]=v2 / _ combining_diaeresis	<>	@v1 @b @v2 / _ combining_diaeresis
[BR]=b [j]=v1 [u]=v2							<>	@v1 @v2 @b
[BR]=b [u]=v1 [i]=v2 / _ combining_diaeresis	<>	@v1 @b @v2 / _ combining_diaeresis
[BR]=b [u]=v1 [i]=v2							<>	@v1 @v2 @b
[BR]=b [vowelrho]=v								<>	@v @b


; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
; (end of file)
