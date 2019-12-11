import sys

import corpus_converter
from hip2unicode.functions import all_hip_conversions as ahc
from hip2unicode.functions import compile_conversion as cc
from hip2unicode.conversions import hip2antconc

if len(sys.argv) != 3:
    print('''

    Insufficient argument list. Please, specify paths
    for a corpus folder and for an output folder.

    ''')
    sys.exit(1)

conversions = ahc(slav=cc(hip2antconc.conversion),
                  rus='delete', lat='delete', grec='delete')
corpus_converter.corpus_converter(corpus_folder=sys.argv[1],
    converted_corpus_folder=sys.argv[2], conversions=conversions)
