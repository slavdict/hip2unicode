# -*- coding: utf-8 -*-
from hip2unicode.tools import corpus_converter
from hip2unicode.functions import all_hip_conversions as ahc
from hip2unicode.functions import make_conversion as mc
from hip2unicode.conversions import hip2antconc

# def corpus_converter(path=None, corpus_folder='corpus', converted_corpus_folder='converted_corpus', conversions=None):

corpus_converter.corpus_converter(
    converted_corpus_folder = 'corpus-antconc',
    conversions             =  ahc(
                                    slav=mc(hip2antconc.hip2antconc),
                                    rus='delete',
                                    lat='delete',
                                  ),
    )
