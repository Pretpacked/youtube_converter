#!/usr/bin/env python
from cx_Freeze import setup, Executable

setup(name = "reandurllib" ,
      version = "0.1" ,
      description = "testing" ,
      executables = [Executable("start.py")])