# -*- coding: utf-8 -*-
from hip2unicode.tools import corpus_converter
from hip2unicode.functions import all_hip_conversions as ahc
from hip2unicode.functions import make_conversion as mc
from hip2unicode.conversions import hip2cslav

# def corpus_converter(path=None, corpus_folder='corpus', converted_corpus_folder='converted_corpus', conversions=None):

corpus_converter.corpus_converter(
    converted_corpus_folder = 'corpus-unicode-0',
    conversions             =  ahc(
                                    slav=mc(hip2cslav.hip2cslav),
                                    rus='delete',
                                    lat='delete',
                                  ),
    )
