# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['archerbc.py'],
             pathex=[],
             binaries=[],
             datas=[('dbworker\\db.db', 'dbworker\\'), ('.rsrc', '.rsrc\\'), ('translate', 'translate\\'), ('qss', 'qss\\'), ('drv', 'drv\\')],
             hiddenimports=['py_ballisticcalc.lib.bmath.unit.temperature', 'py_ballisticcalc.lib.bmath.unit.pressure', 'py_ballisticcalc.lib.bmath.unit.velocity', 'py_ballisticcalc.lib.bmath.unit.distance', 'py_ballisticcalc.lib.bmath.unit.angular', 'py_ballisticcalc.lib.bmath.unit.weight', 'py_ballisticcalc.lib.atmosphere', 'py_ballisticcalc.lib.shot_parameters', 'py_ballisticcalc.lib.drag', 'py_ballisticcalc.lib.projectile', 'py_ballisticcalc.lib.trajectory_calculator', 'py_ballisticcalc.lib.trajectory_data', 'py_ballisticcalc.lib.weapon', 'py_ballisticcalc.lib.wind', 'py_ballisticcalc.lib.tools.multiple_bc', 'py_ballisticcalc.lib.profile', 'py_ballisticcalc.lib.drag_tables'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='archerbc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , version='version.txt', icon='.rsrc\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='archerbc')
