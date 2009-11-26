# -*- coding: utf-8 -*-
from hip2unicode.functions import hip2unicode as h2u
from hip2unicode.functions import all_hip_conversions as ahc
from hip2unicode.functions import make_conversion as mc
from hip2unicode.conversions import hip2hipcslav
from hip2unicode.tools.binary_converter import binary_converter
import os
import codecs


def corpus_converter(path=None, corpus_folder='corpus', converted_corpus_folder='converted_corpus', conversions=None):

    if not path:
        path = os.path.abspath(os.getcwd())
    
    print '\nCurrent folder is "%s".' % path

    corpus_path = os.path.join(path, corpus_folder)
    converted_corpus_path = os.path.join(path, converted_corpus_folder)

    # проверяем наличие папки corpus в текущем каталоге
    
    if not os.path.exists(corpus_path):
        print 'Corpus folder with the name "%s" does not exist.' % corpus_folder
        raw_input('Press ENTER to exit program.')
        quit()

    def all_files(path):
        result = []
        for dirpath, subdirs, filenames in os.walk(path):
            if filenames:
                result.extend([os.path.join(dirpath, filename) for filename in filenames])
        return result

    def make_all_folders(path):
        p = os.path.dirname(path)
        if not os.path.exists(p):
            make_all_folders(p)
            os.mkdir(p)

    file_list = all_files(corpus_path)
    if not file_list:
        print 'There is no file to convert in the corpus folder.'
        raw_input('Press ENTER to exit program.')
        quit()

    # проверяем, существует ли папка converted_corpus
    # если не существует, создаём её
    converted_corpus_folder_exists = os.path.exists(converted_corpus_path)

    if converted_corpus_folder_exists:
        # проверяем, есть ли в ней файлы, и при наличии, удаляем их
        stuff_file_list = all_files(converted_corpus_path)
        for f in stuff_file_list:
            os.remove(f)
    else:
        os.mkdir(converted_corpus_path)

    enc_list = ['cp1251', 'koi8-r', 'utf-8',]
    print 'Converting files ',
    for file_path in file_list:

        # binary_converter(file_path)
        
        for enc in enc_list:
            with open(file_path) as f:
                try:
                    text = f.read().decode(enc)
                except UnicodeDecodeError:
                    e = True
                    continue
                else:
                    print enc,
                    e = False
                    break
        if e:
            print 'File "%s" is encoded with unknown encoding.' % file_path
            print 'Known encodings are', enc_list 
            raw_input('Press ENTER to exit program.')
            quit()

        f.close()

        conversions = None # unicode
        conversions = ahc(slav=mc(hip2hipcslav.hip2hipcslav)) # unicode, но вся диакритка заменена символами положительной ширины

        converted_text = h2u(text, conversions).encode('utf-8')

        new_path = file_path.replace(corpus_path, converted_corpus_path)

        make_all_folders(new_path)
        fu = open(new_path, 'w')
        fu.write(converted_text)
        fu.close()
