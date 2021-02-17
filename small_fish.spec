# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['small_fish.py'],
             pathex=['bloodboard.py', 'end.py', 'game_functions.py', 'game_stats.py', 'old_words.py', 'oldbig.py', 'settings.py', 'small_words.py', 'smallfish.py', 'wechat.py', 'C:\\Python37\\python_work\\small_fish'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='small_fish',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
