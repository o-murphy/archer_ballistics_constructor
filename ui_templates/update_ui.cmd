pyuic5 ui_templates\profiles_table.ui -o gui\profiles_tab\templates\profiles_table.py
pyuic5 ui_templates\profile_item.ui -o gui\profiles_tab\templates\profile_item.py
pyuic5 ui_templates\profile_current.ui -o gui\profiles_tab\templates\profile_current.py
pyuic5 ui_templates\profiles_tab.ui -o gui\profiles_tab\templates\profiles_tab.py
pyuic5 ui_templates\profiles_tools.ui -o gui\profiles_tab\templates\profiles_tools.py
pyuic5 ui_templates\drag_func_edit.ui -o gui\drag_func_editor\templates\drag_func_edit.py
pyuic5 ui_templates\footer.ui -o gui\templates\footer.py
pyrcc5 .rsrc\res.qrc -o res_rc.py

