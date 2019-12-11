#NOTLTR = u'[^a-uw-zA-UW-Z`\\^_@"\'\u0080-\u0095\u0098-\u009f\u00a1-\u00a3\u00a5-\u00ab\u00ad-\u00b5\u00b8-\u00ff]'


conversion = (

    # make sigma into final form if not followed by a letter
    #(u's' + NOTLTR, u'v'),
    ('s($|(?=[\s.,;\]\)\?\!:]))', 'v'),

    ('\u00CF'            ,  'Hr'),
    ('\u00BF'            ,  'hr'),

    ('\u00ADA'        ,  "HA'"),
    ('\u00AEA'        ,  'HA`'),
    ('\u00AFA'        ,  'HA^'),
    ('\u00A9A'        ,  "hA'"),
    ('\u00AAA'        ,  'hA`'),
    ('\u00ABA'        ,  'hA^'),

    ('\u00ADE'        ,  "HE'"),
    ('\u00A9E'        ,  "hE'"),
    ('\u00AAE'        ,  'hE`'),

    ('\u00ADJ'        ,  "HJ'"),
    ('\u00AEJ'        ,  'HJ`'),
    ('\u00AFJ'        ,  'HJ^'),
    ('\u00A9J'        ,  "hJ'"),
    ('\u00AAJ'        ,  'hJ`'),
    ('\u00ABJ'        ,  'hJ^'),

    ('\u00ADI'        ,  "HI'"),
    ('\u00AFI'        ,  'HI^'),
    ('\u00A9I'        ,  "hI'"),
    ('\u00AAI'        ,  'hI`'),
    ('\u00ABI'        ,  'hI^'),

    ('\u00ADO'        ,  "HO'"),
    ('\u00AEO'        ,  'HO`'),
    ('\u00A9O'        ,  "hO'"),
    ('\u00AAO'        ,  'hO`'),

    ('\u00ADU'        ,  "HU'"),
    ('\u00AEU'        ,  'HU`'),
    ('\u00AFU'        ,  'HU^'),
    ('\u00A9U'        ,  "hU'"),
    ('\u00AAU'        ,  'hU`'),
    ('\u00ABU'        ,  'hU^'),

    ('\u00ADW'        ,  "HW'"),
    ('\u00AEW'        ,  'HW`'),
    ('\u00AFW'        ,  'HW^'),
    ('\u00A9W'        ,  "hW'"),
    ('\u00AAW'        ,  'hW`'),
    ('\u00ABW'        ,  'hW^'),

    ('\u0087'            ,  'Ha'),
    ('\u0080'            ,  "a'"),
    ('\u0088'            ,  "Ha'"),
    ('\u0081'            ,  'a`'),
    ('\u0089'            ,  'Ha`'),
    ('\u0082'            ,  'a^'),
    ('\u008A'            ,  'Ha^'),
    ('\u0083'            ,  'ha'),
    ('\u0084'            ,  "ha'"),
    ('\u0085'            ,  'ha`'),
    ('\u0086'            ,  'ha^'),

    ('\u009D'            ,  'He'),
    ('\u0099'            ,  "e'"),
    ('\u009E'            ,  "He'"),
    ('\u009A'            ,  'e`'),
    ('\u009B'            ,  'he'),
    ('\u009C'            ,  "he'"),
    ('\u009F'            ,  'he`'),

    ('\u00D7'            ,  'Hj'),
    ('\u00D0'            ,  "j'"),
    ('\u00D8'            ,  "Hj'"),
    ('\u00D1'            ,  'j`'),
    ('\u00D9'            ,  'Hj`'),
    ('\u00D2'            ,  'j^'),
    ('\u00DA'            ,  'Hj^'),
    ('\u00D3'            ,  'hj'),
    ('\u00D4'            ,  "hj'"),
    ('\u00D5'            ,  'hj`'),
    ('\u00D6'            ,  'hj^'),

    ('\u00B8'            ,  'Hi'),
    ('\u00B0'            ,  "i'"),
    ('\u00B9'            ,  "Hi'"),
    ('\u00B1'            ,  'i`'),
    ('\u00B2'            ,  'i^'),
    ('\u00BA'            ,  'Hi^'),
    ('\u00B3'            ,  'hi'),
    ('\u00B4'            ,  "hi'"),
    ('\u00BE'            ,  'hi`'),
    ('\u00B5'            ,  'hi^'),

    ('\u00EC'            ,  'Ho'),
    ('\u00E7'            ,  "o'"),
    ('\u00ED'            ,  "Ho'"),
    ('\u00E8'            ,  'o`'),
    ('\u00CE'            ,  'Ho`'),
    ('\u00E9'            ,  'ho'),
    ('\u00EA'            ,  "ho'"),
    ('\u00EB'            ,  'ho`'),

    ('\u00C7'            ,  'Hu'),
    ('\u00C0'            ,  "u'"),
    ('\u00C8'            ,  "Hu'"),
    ('\u00C1'            ,  'u`'),
    ('\u00C9'            ,  'Hu`'),
    ('\u00C2'            ,  'u^'),
    ('\u00CA'            ,  'Hu^'),
    ('\u00C3'            ,  'hu'),
    ('\u00C4'            ,  "hu'"),
    ('\u00C5'            ,  'hu`'),
    ('\u00C6'            ,  'hu^'),

    ('\u00F7'            ,  'Hw'),
    ('\u00F0'            ,  "w'"),
    ('\u00F8'            ,  "Hw'"),
    ('\u00F1'            ,  'w`'),
    ('\u00F9'            ,  'Hw`'),
    ('\u00F2'            ,  'w^'),
    ('\u00FA'            ,  'Hw^'),
    ('\u00F3'            ,  'hw'),
    ('\u00F4'            ,  "hw'"),
    ('\u00F5'            ,  'hw`'),
    ('\u00F6'            ,  'hw^'),

    ('\u008B'            ,  'a_'),
    ('\u0093'            ,  'Ha_'),
    ('\u008C'            ,  "a_'"),
    ('\u0094'            ,  "Ha_'"),
    ('\u008D'            ,  'a_`'),
    ('\u0095'            ,  'Ha_`'),
    ('\u008E'            ,  'a_^'),
    ('\u0098'            ,  'Ha_^'),
    ('\u008F'            ,  'ha_'),
    ('\u0090'            ,  "ha_'"),
    ('\u0091'            ,  'ha_`'),
    ('\u0092'            ,  'ha_^'),

    ('\u00DB'            ,  'j_'),
    ('\u00E3'            ,  'Hj_'),
    ('\u00DC'            ,  "j_'"),
    ('\u00E4'            ,  "Hj_'"),
    ('\u00DD'            ,  'j_`'),
    ('\u00E5'            ,  'Hj_`'),
    ('\u00DE'            ,  'j_^'),
    ('\u00E6'            ,  'Hj_^'),
    ('\u00DF'            ,  'hj_'),
    ('\u00E0'            ,  "hj_'"),
    ('\u00E1'            ,  'hj_`'),
    ('\u00E2'            ,  'hj_^'),

    ('\u00FB'            ,  'w_'),
    ('\u00A5'            ,  'Hw_'),
    ('\u00FC'            ,  "w_'"),
    ('\u00A6'            ,  "Hw_'"),
    ('\u00FD'            ,  'w_`'),
    ('\u00A7'            ,  'Hw_`'),
    ('\u00FE'            ,  'w_^'),
    ('\u00A8'            ,  'Hw_^'),
    ('\u00FF'            ,  'hw_'),
    ('\u00A1'            ,  "hw_'"),
    ('\u00A2'            ,  'hw_`'),
    ('\u00A3'            ,  'hw_^'),

    ('\u00BB'            ,  'i"'),
    ('\u00BC'            ,  "i\"'"),
    ('\u00BD'            ,  'i"`'),

    ('\u00CB'            ,  'u"'),
    ('\u00CC'            ,  "u\"'"),
    ('\u00CD'            ,  'u"`'),

    ('A\u00B8'        ,  'HAi'),
    ('A\u00B9'        ,  "HAi'"),
    ('A\u00BA'        ,  'HAi^'),
    ('A\u00B3'        ,  'hAi'),
    ('A\u00B4'        ,  "hAi'"),
    ('A\u00BE'        ,  'hAi`'),
    ('A\u00B5'        ,  'hAi^'),

    ('a\u00B8'        ,  'Hai'),
    ('a\u00B0'        ,  "ai'"),
    ('a\u00B9'        ,  "Hai'"),
    ('a\u00B1'        ,  'ai`'),
    ('a\u00B2'        ,  'ai^'),
    ('a\u00BA'        ,  'Hai^'),
    ('a\u00B3'        ,  'hai'),
    ('a\u00B4'        ,  "hai'"),
    ('a\u00BE'        ,  'hai`'),
    ('a\u00B5'        ,  'hai^'),

    ('E\u00B8'        ,  'HEi'),
    ('E\u00B9'        ,  "HEi'"),
    ('E\u00BA'        ,  'HEi^'),
    ('E\u00B3'        ,  'hEi'),
    ('E\u00B4'        ,  "hEi'"),
    ('E\u00BE'        ,  'hEi`'),
    ('E\u00B5'        ,  'hEi^'),

    ('e\u00B8'        ,  'Hei'),
    ('e\u00B0'        ,  "ei'"),
    ('e\u00B9'        ,  "Hei'"),
    ('e\u00B1'        ,  'ei`'),
    ('e\u00B2'        ,  'ei^'),
    ('e\u00BA'        ,  'Hei^'),
    ('e\u00B3'        ,  'hei'),
    ('e\u00B4'        ,  "hei'"),
    ('e\u00BE'        ,  'hei`'),
    ('e\u00B5'        ,  'hei^'),

    ('O\u00B8'        ,  'HOi'),
    ('O\u00B9'        ,  "HOi'"),
    ('O\u00BA'        ,  'HOi^'),
    ('O\u00B3'        ,  'hOi'),
    ('O\u00B4'        ,  "hOi'"),
    ('O\u00BE'        ,  'hOi`'),
    ('O\u00B5'        ,  'hOi^'),

    ('o\u00B8'        ,  'Hoi'),
    ('o\u00B0'        ,  "oi'"),
    ('o\u00B9'        ,  "Hoi'"),
    ('o\u00B1'        ,  'oi`'),
    ('o\u00B2'        ,  'oi^'),
    ('o\u00BA'        ,  'Hoi^'),
    ('o\u00B3'        ,  'hoi'),
    ('o\u00B4'        ,  "hoi'"),
    ('o\u00BE'        ,  'hoi`'),
    ('o\u00B5'        ,  'hoi^'),

    ('U\u00B8'        ,  'HUi'),
    ('U\u00B9'        ,  "HUi'"),
    ('U\u00BA'        ,  'HUi^'),
    ('U\u00B3'        ,  'hUi'),
    ('U\u00B4'        ,  "hUi'"),
    ('U\u00BE'        ,  'hUi`'),
    ('U\u00B5'        ,  'hUi^'),

    ('u\u00B8'        ,  'Hui'),
    ('u\u00B0'        ,  "ui'"),
    ('u\u00B9'        ,  "Hui'"),
    ('u\u00B1'        ,  'ui`'),
    ('u\u00B2'        ,  'ui^'),
    ('u\u00BA'        ,  'Hui^'),
    ('u\u00B3'        ,  'hui'),
    ('u\u00B4'        ,  "hui'"),
    ('u\u00BE'        ,  'hui`'),
    ('u\u00B5'        ,  'hui^'),

    ('A\u00C7'        ,  'HAu'),
    ('A\u00C8'        ,  "HAu'"),
    ('A\u00C9'        ,  'HAu`'),
    ('A\u00CA'        ,  'HAu^'),
    ('A\u00C3'        ,  'hAu'),
    ('A\u00C4'        ,  "hAu'"),
    ('A\u00C5'        ,  'hAu`'),
    ('A\u00C6'        ,  'hAu^'),

    ('a\u00C7'        ,  'Hau'),
    ('a\u00C0'        ,  "au'"),
    ('a\u00C8'        ,  "Hau'"),
    ('a\u00C1'        ,  'au`'),
    ('a\u00C9'        ,  'Hau`'),
    ('a\u00C2'        ,  'au^'),
    ('a\u00CA'        ,  'Hau^'),
    ('a\u00C3'        ,  'hau'),
    ('a\u00C4'        ,  "hau'"),
    ('a\u00C5'        ,  'hau`'),
    ('a\u00C6'        ,  'hau^'),

    ('E\u00C7'        ,  'HEu'),
    ('E\u00C8'        ,  "HEu'"),
    ('E\u00C9'        ,  'HEu`'),
    ('E\u00CA'        ,  'HEu^'),
    ('E\u00C3'        ,  'hEu'),
    ('E\u00C4'        ,  "hEu'"),
    ('E\u00C5'        ,  'hEu`'),
    ('E\u00C6'        ,  'hEu^'),

    ('e\u00C7'        ,  'Heu'),
    ('e\u00C0'        ,  "eu'"),
    ('e\u00C8'        ,  "Heu'"),
    ('e\u00C1'        ,  'eu`'),
    ('e\u00C9'        ,  'Heu`'),
    ('e\u00C2'        ,  'eu^'),
    ('e\u00CA'        ,  'Heu^'),
    ('e\u00C3'        ,  'heu'),
    ('e\u00C4'        ,  "heu'"),
    ('e\u00C5'        ,  'heu`'),
    ('e\u00C6'        ,  'heu^'),

    ('J\u00C7'        ,  'HJu'),
    ('J\u00C8'        ,  "HJu'"),
    ('J\u00C9'        ,  'HJu`'),
    ('J\u00CA'        ,  'HJu^'),
    ('J\u00C3'        ,  'hJu'),
    ('J\u00C4'        ,  "hJu'"),
    ('J\u00C5'        ,  'hJu`'),
    ('J\u00C6'        ,  'hJu^'),

    ('j\u00C7'        ,  'Hju'),
    ('j\u00C0'        ,  "ju'"),
    ('j\u00C8'        ,  "Hju'"),
    ('j\u00C1'        ,  'ju`'),
    ('j\u00C9'        ,  'Hju`'),
    ('j\u00C2'        ,  'ju^'),
    ('j\u00CA'        ,  'Hju^'),
    ('j\u00C3'        ,  'hju'),
    ('j\u00C4'        ,  "hju'"),
    ('j\u00C5'        ,  'hju`'),
    ('j\u00C6'        ,  'hju^'),

    ('O\u00C7'        ,  'HOu'),
    ('O\u00C8'        ,  "HOu'"),
    ('O\u00C9'        ,  'HOu`'),
    ('O\u00CA'        ,  'HOu^'),
    ('O\u00C3'        ,  'hOu'),
    ('O\u00C4'        ,  "hOu'"),
    ('O\u00C5'        ,  'hOu`'),
    ('O\u00C6'        ,  'hOu^'),

    ('o\u00C7'        ,  'Hou'),
    ('o\u00C0'        ,  "ou'"),
    ('o\u00C8'        ,  "Hou'"),
    ('o\u00C1'        ,  'ou`'),
    ('o\u00C9'        ,  'Hou`'),
    ('o\u00C2'        ,  'ou^'),
    ('o\u00CA'        ,  'Hou^'),
    ('o\u00C3'        ,  'hou'),
    ('o\u00C4'        ,  "hou'"),
    ('o\u00C5'        ,  'hou`'),
    ('o\u00C6'        ,  'hou^'),

    ('HA\u00BB'       ,  'HAi"'),
    ('HA\u00BC'       ,  "HAi\"'"),
    ('HA\u00BD'       ,  'HAi"`'),
    ('hA\u00BB'       ,  'hAi"'),
    ('hA\u00BC'       ,  "hAi\"'"),
    ('hA\u00BD'       ,  'hAi"`'),
    ('a\u00BB'        ,  'ai"'),
    ('\u0087\u00BB'       ,  'Hai"'),
    ('a\u00BC'        ,  "ai\"'"),
    ('\u0087\u00BC'       ,  "Hai\"'"),
    ('a\u00BD'        ,  'ai"`'),
    ('\u0087\u00BD'       ,  'Hai"`'),
    ('\u0083\u00BB'       ,  'hai"'),
    ('\u0083\u00BC'       ,  "hai\"'"),
    ('\u0083\u00BD'       ,  'hai"`'),

    ('HE\u00BB'       ,  'HEi"'),
    ('HE\u00BC'       ,  "HEi\"'"),
    ('HE\u00BD'       ,  'HEi"`'),
    ('hE\u00BB'       ,  'hEi"'),
    ('hE\u00BC'       ,  "hEi\"'"),
    ('hE\u00BD'       ,  'hEi"`'),
    ('e\u00BB'        ,  'ei"'),
    ('\u009D\u00BB'       ,  'Hei"'),
    ('e\u00BC'        ,  "ei\"'"),
    ('\u009D\u00BC'       ,  "Hei\"'"),
    ('e\u00BD'        ,  'ei"`'),
    ('\u009D\u00BD'       ,  'Hei"`'),
    ('\u009B\u00BB'       ,  'hei"'),
    ('\u009B\u00BC'       ,  "hei\"'"),
    ('\u009B\u00BD'       ,  'hei"`'),

    ('HO\u00BB'       ,  'HOi"'),
    ('HO\u00BC'       ,  "HOi\"'"),
    ('HO\u00BD'       ,  'HOi"`'),
    ('hO\u00BB'       ,  'hOi"'),
    ('hO\u00BC'       ,  "hOi\"'"),
    ('hO\u00BD'       ,  'hOi"`'),
    ('o\u00BB'        ,  'oi"'),
    ('\u00EC\u00BB'   ,  'Hoi"'),
    ('o\u00BC'        ,  "oi\"'"),
    ('\u00EC\u00BC'   ,  "Hoi\"'"),
    ('o\u00BD'        ,  'oi"`'),
    ('\u00EC\u00BD'       ,  'Hoi"`'),
    ('\u00E9\u00BB'       ,  'hoi"'),
    ('\u00E9\u00BC'       ,  "hoi\"'"),
    ('\u00E9\u00BD'       ,  'hoi"`'),

    ('HU\u00BB'       ,  'HUi"'),
    ('HU\u00BC'       ,  "HUi\"'"),
    ('HU\u00BD'       ,  'HUi"`'),
    ('hU\u00BB'       ,  'hUi"'),
    ('hU\u00BC'       ,  "hUi\"'"),
    ('hU\u00BD'       ,  'hUi"`'),
    ('u\u00BB'        ,  'ui"'),
    ('\u00C7\u00BB'   ,  'Hui"'),
    ('u\u00BC'        ,  "ui\"'"),
    ('\u00C7\u00BC'   ,  "Hui\"'"),
    ('u\u00BD'        ,  'ui"`'),
    ('\u00C7\u00BD'       ,  'Hui"`'),
    ('\u00C3\u00BB'       ,  'hui"'),
    ('\u00C3\u00BC'       ,  "hui\"'"),
    ('\u00C3\u00BD'       ,  'hui"`'),

    ('HA\u00CB'       ,  'HAu"'),
    ('HA\u00CC'       ,  "HAu\"'"),
    ('HA\u00CD'       ,  'HAu"`'),
    ('hA\u00CB'       ,  'hAu"'),
    ('hA\u00CC'       ,  "hAu\"'"),
    ('hA\u00CD'       ,  'hAu"`'),
    ('a\u00CB'        ,  'au"'),
    ('\u0087\u00CB'   ,  'Hau"'),
    ('a\u00CC'        ,  "au\"'"),
    ('\u0087\u00CC'   ,  "Hau\"'"),
    ('a\u00CD'        ,  'au"`'),
    ('\u0087\u00CD'       ,  'Hau"`'),
    ('\u0083\u00CB'       ,  'hau"'),
    ('\u0083\u00CC'       ,  "hau\"'"),
    ('\u0083\u00CD'       ,  'hau"`'),

    ('HE\u00CB'       ,  'HEu"'),
    ('HE\u00CC'       ,  "HEu\"'"),
    ('HE\u00CD'       ,  'HEu"`'),
    ('hE\u00CB'       ,  'hEu"'),
    ('hE\u00CC'       ,  "hEu\"'"),
    ('hE\u00CD'       ,  'hEu"`'),
    ('e\u00CB'        ,  'eu"'),
    ('\u009D\u00CB'   ,  'Heu"'),
    ('e\u00CC'        ,  "eu\"'"),
    ('\u009D\u00CC'   ,  "Heu\"'"),
    ('e\u00CD'        ,  'eu"`'),
    ('\u009D\u00CD'       ,  'Heu"`'),
    ('\u009B\u00CB'       ,  'heu"'),
    ('\u009B\u00CC'       ,  "heu\"'"),
    ('\u009B\u00CD'       ,  'heu"`'),

    ('HJ\u00CB'       ,  'HJu"'),
    ('HJ\u00CC'       ,  "HJu\"'"),
    ('HJ\u00CD'       ,  'HJu"`'),
    ('hJ\u00CB'       ,  'hJu"'),
    ('hJ\u00CC'       ,  "hJu\"'"),
    ('hJ\u00CD'       ,  'hJu"`'),
    ('j\u00CB'        ,  'ju"'),
    ('\u00D7\u00CB'   ,  'Hju"'),
    ('j\u00CC'        ,  "ju\"'"),
    ('\u00D7\u00CC'   ,  "Hju\"'"),
    ('j\u00CD'        ,  'ju"`'),
    ('\u00D7\u00CD'       ,  'Hju"`'),
    ('\u00D3\u00CB'       ,  'hju"'),
    ('\u00D3\u00CC'       ,  "hju\"'"),
    ('\u00D3\u00CD'       ,  'hju"`'),

    ('HO\u00CB'       ,  'HOu"'),
    ('HO\u00CC'       ,  "HOu\"'"),
    ('HO\u00CD'       ,  'HOu"`'),
    ('hO\u00CB'       ,  'hOu"'),
    ('hO\u00CC'       ,  "hOu\"'"),
    ('hO\u00CD'       ,  'hOu"`'),
    ('o\u00CB'        ,  'ou"'),
    ('\u00EC\u00CB'   ,  'Hou"'),
    ('o\u00CC'        ,  "ou\"'"),
    ('\u00EC\u00CC'   ,  "Hou\"'"),
    ('o\u00CD'        ,  'ou"`'),
    ('\u00EC\u00CD'       ,  'Hou"`'),
    ('\u00E9\u00CB'       ,  'hou"'),
    ('\u00E9\u00CC'       ,  "hou\"'"),
    ('\u00E9\u00CD'       ,  'hou"`'),

    ('\u00AD'            ,  "H'"),
    ('\u00AE'            ,  'H`'),
    ('\u00AF'            ,  'H^'),
    ('\u00A9'            ,  "h'"),
    ('\u00AA'            ,  'h`'),
    ('\u00AB'            ,  'h^'),

    ('\u00EE'            ,  "\"'"),
    ('\u00EF'            ,  '"`'),


# shuffle marks, as Unicode canonical order does not correspond to Galatia order

    ('(.)([`\'\\^"]+)'   ,  r"\2\1"),

# Now make the jump from byte to Unicode space.
# Here, we deal only with the decomposed forms, not precomposed.

#ByteDefault			183			; 183 is "bullet" in the SIL Greek Display encoding
#								; (note that this is actually a valid character code,
#								; though probably not often used in legacy Greek text)
#UniDefault			replacement_character

    ('"',      '\u0308'), # combining_diaeresis
    ('#',      '\u00a0'), # no_break_space
    (r'\$',      '\u00ab'), # left_pointing_double_angle_quotation_markleft
    ('%',      '\u00bb'), # right_pointing_double_angle_quotation_mark
    ("'",      '\u0301'), #combining_acute_accent

    (';',      '\u0387'), #greek_ano_teleia				; greek semicolon
    (r'\?',      ';'), #semicolon						; canonical decomposition of greek question mark

    ('@',      '\u2019'), #right_single_quotation_mark

    ('A',      '\u0391'), #greek_capital_letter_alpha
    ('B',      '\u0392'), #greek_capital_letter_beta
    ('C',      '\u03a7'), #greek_capital_letter_chi
    ('D',      '\u0394'), #greek_capital_letter_delta
    ('E',      '\u0395'), #greek_capital_letter_epsilon
    ('F',      '\u03a6'), #greek_capital_letter_phi
    ('G',      '\u0393'), #greek_capital_letter_gamma
    ('H',      '\u0313'), #combining_comma_above
    ('I',      '\u0399'), #greek_capital_letter_iota
    ('J',      '\u0397'), #greek_capital_letter_eta
    ('K',      '\u039a'), #greek_capital_letter_kappa
    ('L',      '\u039b'), #greek_capital_letter_lamda
    ('M',      '\u039c'), #greek_capital_letter_mu
    ('N',      '\u039d'), #greek_capital_letter_nu
    ('O',      '\u039f'), #greek_capital_letter_omicron
    ('P',      '\u03a0'), #greek_capital_letter_pi
    ('Q',      '\u0398'), #greek_capital_letter_theta
    ('R',      '\u03a1'), #greek_capital_letter_rho
    ('S',      '\u03a3'), #greek_capital_letter_sigma
    ('T',      '\u03a4'), #greek_capital_letter_tau
    ('U',      '\u03a5'), #greek_capital_letter_upsilon
    ('W',      '\u03a9'), #greek_capital_letter_omega
    ('X',      '\u039e'), #greek_capital_letter_xi
    ('Y',      '\u03a8'), #greek_capital_letter_psi
    ('Z',      '\u0396'), #greek_capital_letter_zeta

    (r'\^',     '\u0342'), #combining_greek_perispomeni		; circumflex
    ('_',      '\u0345'), #combining_greek_ypogegrammeni	; iota subscript
    ('`',      '\u0300'), #combining_grave_accent

    ('a',      '\u03b1'), #greek_small_letter_alpha
    ('b',      '\u03b2'), #greek_small_letter_beta
    ('c',      '\u03c7'), #greek_small_letter_chi
    ('d',      '\u03b4'), #greek_small_letter_delta
    ('e',      '\u03b5'), #greek_small_letter_epsilon
    ('f',      '\u03c6'), #greek_small_letter_phi
    ('g',      '\u03b3'), #greek_small_letter_gamma
    ('h',      '\u0314'), #combining_reversed_comma_above
    ('i',      '\u03b9'), #greek_small_letter_iota
    ('j',      '\u03b7'), #greek_small_letter_eta
    ('k',      '\u03ba'), #greek_small_letter_kappa
    ('l',      '\u03bb'), #greek_small_letter_lamda
    ('m',      '\u03bc'), #greek_small_letter_mu
    ('n',      '\u03bd'), #greek_small_letter_nu
    ('o',      '\u03bf'), #greek_small_letter_omicron
    ('p',      '\u03c0'), #greek_small_letter_pi
    ('q',      '\u03b8'), #greek_small_letter_theta
    ('r',      '\u03c1'), #greek_small_letter_rho
    ('s',      '\u03c3'), #greek_small_letter_sigma
    ('t',      '\u03c4'), #greek_small_letter_tau
    ('u',      '\u03c5'), #greek_small_letter_upsilon
    ('v',      '\u03c2'), #greek_small_letter_final_sigma
    ('w',      '\u03c9'), #greek_small_letter_omega
    ('x',      '\u03be'), #greek_small_letter_xi
    ('y',      '\u03c8'), #greek_small_letter_psi
    ('z',      '\u03b6'), #greek_small_letter_zeta

    (r'\|b',      '\u03d0'), #greek_beta_symbol				; curly beta
    (r'\|f',      '\u03dd'), #greek_small_letter_digamma		; digamma
    (r'\|G',      '\u03dc'), #greek_letter_digamma			; Digamma
    (r'\|g',      '\u03dd'), #greek_small_letter_digamma		; digamma (which SIL forms should have priority?)
    (r'\|w',      '\u03d6'), #greek_pi_symbol					; omega pi
    (r'\|q',      '\u03df'), #greek_small_letter_koppa		; qoppa
    (r'\|Q',      '\u03de'), #greek_letter_koppa				; Qoppa
    (r'\|R',      '\u03de'), #greek_letter_koppa				; Qoppa
    (r'\|k',      '\u03df'), #greek_small_letter_koppa		; qoppa
    (r'\|K',      '\u03de'), #greek_letter_koppa				; Qoppa
    (r'\|p',      '\u03e1'), #greek_small_letter_sampi		; sampi
    (r'\|P',      '\u03e0'), #greek_letter_sampi				; Sampi
    (r'\|m',      '\u03e1'), #greek_small_letter_sampi		; sampi
    (r'\|M',      '\u03e0'), #greek_letter_sampi				; Sampi
    (r'\|s',      '\u03f2'), #greek_lunate_sigma_symbol		; lunate sigma
    (r'\|S',      '\u03f2'), #greek_lunate_sigma_symbol		; lunate sigma uppercase not available in Unicode
    (r'\|t',      '\u03db'), #greek_small_letter_stigma		; stigma
    (r'\|T',      '\u03da'), #greek_letter_stigma				; Stigma
    (r'\|i',      '\u2129\u0330'), #turned_greek_small_letter_iota combining_tilde_below	; turned iota tilde below
    (r'\|U',      '\u03d2'), #greek_upsilon_with_hook_symbol	; Upsilon hook
    (r'\|h',      '\u0374'), #greek_numeral_sign				; upper numeral sign
    (r'\|H',      '\u0375'), #greek_lower_numeral_sign		; lower numeral sign
    (r'\|n',      '\u200d'), #zero_width_joiner
    (r'\|#',      '\u200c'), #zero_width_non_joiner

    ('~',      '\u2014'), #em_dash
    ('\u0096', '\u2013'), # en_dash
    ('\u0097', '\u2014'), # em_dash
    ('\u00b7', '\u2022'), # bullet
)

# In Unicode space, reorder breathing/vowel sequences from SIL Basic to Unicode order

BR = '([\u0313\u0314])'
aeo = '([\u0391\u0395\u039f\u03b1\u03b5\u03bf])'
iu = '([\u0399\u03a5\u03b9\u03c5])'
j = '([\u0397\u03b7])'
u = '([\u03a5\u03c5])'
i = '([\u0399\u03b9])'
vowelrho = '([\u0391\u0395\u0399\u039f\u03a5\u0397\u03a9\u03a1\u03b1\u03b5\u03b9\u03bf\u03c5\u03b7\u03c9\u03c1])'

conversion += (

    (BR + aeo + iu + '(?=\u0308)',     r'\2\1\3'),
    (BR + aeo + iu,                     r'\2\3\1'),
    (BR + j + u + '(?=\u0308)',        r'\2\1\3'),
    (BR + j + u,                        r'\2\3\1'),
    (BR + u + i + '(?=\u0308)',        r'\2\1\3'),
    (BR + u + i,                        r'\2\3\1'),
    (BR + vowelrho,                     r'\2\1'),

)
