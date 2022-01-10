import fnmatch
import os
import sys
from re import search


try:
    filepath = sys.argv[1]

    matches = []
    for root, dirnames, filenames in os.walk('gui'):
        if 'templates' in root.split('\\'):
            for filename in fnmatch.filter(filenames, '*.py'):
                if filename not in ['main_gui.py', 'profiles_tab.py']:
                    matches.append(os.path.join(root, filename))

    templates = []
    for file in matches:
        with open(file, 'r') as f:
            if search('_translate', f.read()):
                templates.append(file)

    [print(i) for i in templates]

    os.system('pylupdate5 ' + ' '.join(templates) + ' -ts ' + filepath + '.ts')
except IndexError:
    print('wrong file path')
