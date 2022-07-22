import fnmatch
import os
import sys
from re import search


# try:
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


templates.append(r'gui\my_tab\templates_selector.py')
templates.append(r'gui\bc_table\bc_table.py')
templates.append(r'gui\profiles_tab\profile_item_contents\prof_rifle.py')
templates.append(r'gui\profiles_tab\profile_item_contents\prof_bullet.py')
templates.append(r'gui\profiles_tab\profile_item_contents\prof_rifle.py')
templates.append(r'gui\my_tab\templates_selector.py')
templates.append(r'gui\lpc_install_dialog\lpc_dlg.py')
templates.append(r'gui\db_widgets\contexts\catalog_menu.py')
templates.append(r'gui\db_widgets\contexts\templates_menu.py')
templates.append(r'gui\db_widgets\edit\catalog_bullet.py')
templates.append(r'gui\db_widgets\edit\catalog_cartridge.py')
templates.append(r'gui\db_widgets\edit\catalog_rifle.py')
templates.append(r'gui\db_widgets\edit\drag_func_settings\bc_edit.py')
templates.append(r'gui\db_widgets\edit\drag_func_settings\mbc_edit.py')
templates.append(r'gui\db_widgets\info\catalog_bullet_info.py')
templates.append(r'gui\db_widgets\info\catalog_cartridge_info.py')
templates.append(r'gui\db_widgets\info\catalog_rifle_info.py')
templates.append(r'gui\db_widgets\tables\catalog_bullet_list.py')
templates.append(r'gui\db_widgets\tables\catalog_cartridge_list.py')
templates.append(r'gui\db_widgets\tables\catalog_rifle_list.py')
templates.append(r'gui\close_dialog\close_dlg.py')
templates.append(r'gui\catalog_tab\catalog_selector.py')
templates.append(r'gui\app_settings.py')
templates.append(r'gui\db_widgets\edit\df_type_dlg\df_type.py')
templates.append(r'archerbc.py')

[print(i) for i in templates]

os.system('pylupdate5 ' + ' '.join(templates) + ' -ts ' + filepath + '.ts')
# except IndexError as err:
#     print(err)
    # print('wrong file path')
