"""
AntConc to UCS8 conversion

AntConc encoding is specialized ad-hoc
unicode + UTF-8 based encoding designed
for use in AntConc concordancer program
while working with Old Church Slavonic
texts corpus.

"""

from hip2unicode.conversions.antconc_ucs8_pre import conversion as pre_conversion
from hip2unicode.conversions.antconc_ucs8_basic import conversion as basic_conversion
from hip2unicode.conversions.antconc_ucs8_izhica import conversion as izhica_conversion
from hip2unicode.conversions.antconc_ucs8_advanced import conversion as advanced_conversion

conversion =    pre_conversion +    \
                basic_conversion +  \
                izhica_conversion + \
                advanced_conversion
