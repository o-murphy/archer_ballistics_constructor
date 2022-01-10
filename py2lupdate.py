import fnmatch
import os
import sys
from re import search


try:
    filepath = sys.argv[1]

    matches = []
    for root, dirnames, filenames in os.walk('gui'):
        for filename in fnmatch.filter(filenames, '*.py'):
            matches.append(os.path.join(root, filename))

    templates = []
    for file in matches:
        with open(file, 'r') as f:
            if search('def retranslateUi', f.read()):
                templates.append(file)

    os.system('pylupdate5 ' + ' '.join(templates) + ' -ts ' + filepath + '.ts')
except IndexError:
    print('wrong file path')
