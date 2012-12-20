# -*- coding: utf-8 -*-
import os
import sys

from hip2unicode.functions import hip2unicode


def corpus_converter(path=None, corpus_folder='corpus',
        converted_corpus_folder='converted_corpus', conversions=None):

    if not path:
        path = os.path.abspath(os.getcwd())

    print '\nCurrent folder is {0}'.format(path)

    corpus_path = os.path.join(path, corpus_folder)
    converted_corpus_path = os.path.join(path, converted_corpus_folder)

    # проверяем наличие папки corpus в текущем каталоге
    if not os.path.exists(corpus_path):
        print ('Corpus folder with the name "{0}" '
               'does not exist.').format(corpus_folder)
        raw_input('Press ENTER to exit program.')
        sys.exit(-1)

    def all_files(path):
        result = []
        for dirpath, subdirs, filenames in os.walk(path):
            if filenames:
                result.extend(
                          os.path.join(dirpath, filename)
                          for filename in filenames)
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
        sys.exit(-1)

    # Проверяем, существует ли папка converted_corpus
    # если не существует, создаём её.
    if os.path.exists(converted_corpus_path):
        # Проверяем, есть ли в ней файлы. Если да, удаляем их.
        for f in all_files(converted_corpus_path):
            os.remove(f)
    else:
        make_all_folders(converted_corpus_path)

    enc_list = ('utf-8', 'cp1251', 'koi8-r')
    print '\nConverting files '
    for file_path in file_list:
        with open(file_path) as f:
            contents = f.read()
            for enc in enc_list:
                try:
                    text = contents.decode(enc)
                except UnicodeDecodeError:
                    continue
                else:
                    print '{0}\t{1}'.format(enc,
                                  os.path.relpath(file_path, corpus_path))
                    break
            else:
                print 'File "%s" is encoded with unknown encoding.' % file_path
                print 'Known encodings are', enc_list
                raw_input('Press ENTER to exit program.')
                sys.exit(-1)

        converted_text = hip2unicode(text, conversions).encode('utf-8')
        new_path = os.path.relpath(file_path, corpus_path)
        new_path = os.path.splitext(new_path)[0] + '.txt'
        new_path = os.path.join(converted_corpus_path, new_path)
        make_all_folders(new_path)
        with open(new_path, 'w') as fu:
            fu.write(converted_text)
