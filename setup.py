import sys, os
from cx_Freeze import setup, Executable


includefiles = ['Images']

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
                    "packages": ['os'],
                    "path": sys.path + ['Images'],
                    'include_files': includefiles
                    }

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Project water mark",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("PWMain.py",
                                  base=base,
                                  icon="Images\water.ico",
                                  targetName="PWMark.exe",
                                  )
                       ],

    )