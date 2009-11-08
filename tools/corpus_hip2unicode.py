# -*- coding: utf-8 -*-
from hip2unicode.functions import hip2unicode as h2u
import os
import codecs

path = os.path.abspath(os.getcwd())
print '\nCurrent folder is "%s".' % path

corpus_folder = 'corpus'
corpus_unicode_folder = 'corpus_unicode'
corpus_path = os.path.join(path, corpus_folder)
corpus_unicode_path = os.path.join(path, corpus_unicode_folder)

# проверяем наличие папки corpus в текущем каталоге
corpus_folder_exists = os.path.exists(corpus_path)
if not corpus_folder_exists:
    print 'Corpus folder with the name "%s" does not exist.' % corpus_folder
    raw_input('Press ENTER to exit program.')
    quit()

def all_files(path):
    result = []
    for dirpath, subdirs, filenames in os.walk(path):
        if filenames:
            result.extend([os.path.join(dirpath, filename) for filename in filenames])
    return result

file_list = all_files(corpus_path)
if not file_list:
    print 'There is no file to convert in the corpus folder.'
    raw_input('Press ENTER to exit program.')
    quit()

# проверяем, существует ли папка corpus_unicode
# если не существует, создаём её
corpus_unicode_folder_exists = os.path.exists(corpus_unicode_path)
if corpus_unicode_folder_exists:
    # проверяем, есть ли в ней файлы, и при наличии, удаляем их
    file_list = all_files(corpus_unicode_path)
    for f in file_list:
        os.remove(f)
else:
    os.mkdir(corpus_unicode_path)

for old_path in file_list:

    f = open(old_path) # codecs.open(old_path, 'rb', 'utf-8')
    text = u''
    for line in f:
        text = u'%s%s' % (text, line)
    f.close()

    converted_text = h2u(text)

    new_path = old_path.replace(corpus_path, corpus_unicode_path)

    fu = open(new_path, 'w')
    fu.write(converted_text)
    fu.close()

    print 'File "%s" is converted.' % old_path.replace(corpus_path, '')
