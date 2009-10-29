import os, csv

path = os.getcwd()

def all_files(path):
    result = []
    for dirpath, subdirs, filenames in os.walk(path):
        if filenames:
            result.extend([os.path.join(dirpath, filename) for filename in filenames])
    return result

file_list = all_files(path)
word_forms = []

for f in file_list:
    for line in open(f):
        word_forms.extend(line.split())

forms_with_frequency = dict()

for word_form in word_forms:
    forms_with_frequency[word_form] = forms_with_frequency.get(word_form, 0) + 1

forms_with_frequency = forms_with_frequency.items()
forms_with_frequency.sort()
frequency = [(b, a) for a, b in forms_with_frequency]
frequency.sort()
frequency.reverse()

f = open(os.path.join(os.getcwd(), 'forms--sorted.by.alphabet.csv'), 'wb')
writer = csv.writer(f)

for key, value in forms_with_frequency:
    writer.writerow((key, value))

f.close()

f = open(os.path.join(os.getcwd(), 'forms--sorted.by.frequency.csv'), 'wb')
writer = csv.writer(f)

for key, value in frequency:
    writer.writerow((key, value))

f.close()
