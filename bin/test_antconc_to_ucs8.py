# -*- coding: utf-8 -*-
import sys

from hip2unicode.functions import all_hip_conversions, compile_conversion, hip2unicode
from hip2unicode.conversions import antconc_ucs8

compiled_conversion = compile_conversion(antconc_ucs8.conversion)
conversions = all_hip_conversions(slav=compiled_conversion)

if len(sys.argv) < 2:
    print 'Необходимо передать текст для конвертации в виде аргументов.'
    sys.exit(1)

text = ' '.join(sys.argv[1:]).decode('utf-8')
print hip2unicode(text, conversions)
