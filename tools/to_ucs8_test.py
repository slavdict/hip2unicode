# -*- coding: utf-8 -*-
from hip2unicode.functions import all_hip_conversions, compile_conversion, hip2unicode
from hip2unicode.conversions import antconc_ucs8

compiled_conversion = compile_conversion(antconc_ucs8.conversion)
conversions = all_hip_conversions(slav=compiled_conversion)

txt=u"а~"

print hip2unicode(txt, conversions)
