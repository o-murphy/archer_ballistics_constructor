REM venv\Scripts\pyuic5 ui_templates\profiles_table.ui -o gui\profiles_tab\templates\profiles_table.py
REM venv\Scripts\pyuic5 ui_templates\profile_item.ui -o gui\profiles_tab\templates\profile_item.py
REM venv\Scripts\pyuic5 ui_templates\add_btn.ui -o gui\profiles_tab\templates\add_btn.py
REM venv\Scripts\pyuic5 ui_templates\profile_current.ui -o gui\profiles_tab\templates\profile_current.py
REM venv\Scripts\pyuic5 ui_templates\profiles_tab.ui -o gui\profiles_tab\templates\profiles_tab.py
REM venv\Scripts\pyuic5 ui_templates\profiles_tools.ui -o gui\profiles_tab\templates\profiles_tools.py
REM venv\Scripts\pyuic5 ui_templates\drag_func_edit.ui -o gui\drag_func_editor\templates\drag_func_edit.py
REM venv\Scripts\pyuic5 ui_templates\current_atmo_dialog.ui -o gui\drag_func_editor\templates\current_atmo_dialog.py
REM venv\Scripts\pyuic5 ui_templates\footer.ui -o gui\templates\footer.py
REM venv\Scripts\pyuic5 ui_templates\main_gui.ui -o gui\templates\main_gui.py

venv\Scripts\pyuic5 ui_templates\catalog_tab.ui -o gui\catalog_tab\templates\catalog_tab.py
venv\Scripts\pyuic5 ui_templates\catalog_selector.ui -o gui\catalog_tab\templates\catalog_selector.py
venv\Scripts\pyuic5 ui_templates\catalog_info.ui -o gui\catalog_tab\templates\catalog_info.py
venv\Scripts\pyuic5 ui_templates\catalog_rifle.ui -o gui\catalog_tab\templates\catalog_rifle.py
venv\Scripts\pyuic5 ui_templates\catalog_bullet.ui -o gui\catalog_tab\templates\catalog_bullet.py
venv\Scripts\pyuic5 ui_templates\catalog_cartridge.ui -o gui\catalog_tab\templates\catalog_cartridge.py
venv\Scripts\pyuic5 ui_templates\catalog_item_edit.ui -o gui\catalog_tab\templates\catalog_item_edit.py
venv\Scripts\pyuic5 ui_templates\catalog_rifle_list.ui -o gui\catalog_tab\templates\catalog_rifle_list.py
venv\Scripts\pyuic5 ui_templates\catalog_cartridge_list.ui -o gui\catalog_tab\templates\catalog_cartridge_list.py
venv\Scripts\pyuic5 ui_templates\catalog_bullet_list.ui -o gui\catalog_tab\templates\catalog_bullet_list.py
venv\Scripts\pyuic5 ui_templates\catalog_rifle_info.ui -o gui\catalog_tab\templates\catalog_rifle_info.py
venv\Scripts\pyuic5 ui_templates\catalog_cartridge_info.ui -o gui\catalog_tab\templates\catalog_cartridge_info.py
venv\Scripts\pyuic5 ui_templates\catalog_bullet_info.ui -o gui\catalog_tab\templates\catalog_bullet_info.py
venv\Scripts\pyuic5 ui_templates\selectorBtns.ui -o gui\catalog_tab\templates\selectorBtns.py
venv\Scripts\pyuic5 ui_templates\catalog_caliber_list.ui -o gui\catalog_tab\templates\catalog_caliber_list.py
venv\Scripts\pyuic5 ui_templates\caliber_edit.ui -o gui\catalog_tab\templates\caliber_edit.py
REM venv\Scripts\pyuic5 ui_templates\bc_edit.ui -o gui\catalog_tab\templates\bc_edit.py
venv\Scripts\pyuic5 ui_templates\mbc_edit.ui -o gui\catalog_tab\drag_func_settings\templates\mbc_edit.py
venv\Scripts\pyuic5 ui_templates\cdf_edit.ui -o gui\catalog_tab\drag_func_settings\templates\cdf_edit.py

venv\Scripts\pyrcc5 .rsrc\res.qrc -o res_rc.py
