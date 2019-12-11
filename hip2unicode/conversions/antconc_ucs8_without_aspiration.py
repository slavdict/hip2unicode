"""
AntConc to UCS8 conversion
without creating aspiration marks
after initial vowels.

Intentended use is converting affixes.

"""

from hip2unicode.conversions.antconc_ucs8_basic_without_aspiration import conversion as basic_conversion_without_aspiration
from hip2unicode.conversions.antconc_ucs8_izhica import conversion as izhica_conversion
from hip2unicode.conversions.antconc_ucs8_advanced_without_aspiration import conversion as advanced_conversion_without_aspiration

conversion =    basic_conversion_without_aspiration +  \
                izhica_conversion + \
                advanced_conversion_without_aspiration
