# -*- coding: utf-8 -*-
import sys

from hip2unicode.conversions import hip_civilrus
from hip2unicode.functions import all_hip_conversions
from hip2unicode.functions import compile_conversion
from hip2unicode.tools import corpus_converter

conversions = {
    'slav': compile_conversion(hip_civilrus.conversion),
    'rus': 'delete',
    'lat': 'delete',
    'grec': 'delete',
}
args = {
    'converted_corpus_folder': 'corpus-civilrus',
    'conversions': all_hip_conversions(**conversions),
}
corpus_folder = None

if len(sys.argv) == 2:
    corpus_folder = sys.argv[1]

if corpus_folder:
    args['corpus_folder'] = corpus_folder

corpus_converter.corpus_converter(**args)
