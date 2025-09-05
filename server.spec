# -*- mode: python ; coding: utf-8 -*-
block_cipher = None
a = Analysis(['server.py'], pathex=['./'], binaries=[], datas=[('soap', 'soap')], hiddenimports=['twisted','ZSI', 'ZSI.generate', 'ZSI.wstools'], cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas, [], name='server_exe', debug=False, bootloader_ignore_signals=False, strip=False, upx=True, upx_exclude=[], runtime_tmpdir=None, console=True)
coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, strip=False, upx=True, upx_exclude=[], name='server_coll')