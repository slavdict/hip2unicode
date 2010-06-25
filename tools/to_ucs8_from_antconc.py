# -*- coding: utf-8 -*-
from hip2unicode.tools import corpus_converter
from hip2unicode.functions import all_hip_conversions
from hip2unicode.functions import compile_conversion
from hip2unicode.conversions import antconc_ucs8

# def corpus_converter(path=None, corpus_folder='corpus', converted_corpus_folder='converted_corpus', conversions=None):

compiled_conversion = compile_conversion(antconc_ucs8.conversion)
kwargs = {
    'converted_corpus_folder': 'corpus-ucs8',
    'conversions': all_hip_conversions(slav=compiled_conversion)
} 

corpus_converter.corpus_converter(**kwargs)
