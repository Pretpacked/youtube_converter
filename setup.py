#!/usr/bin/env python
import sys
from cx_Freeze import setup, Executable

application_name = "youtube converting"
application_version = "1.0"
application_description = "Linux first realease."

dependecies = [
	"youtube_dl",
	"BeautifulSoup4",
	"requests",
	"lxml",
	"wheel"
]

setup(name = application_name ,
	version = application_version ,
    description = application_description  ,
	requires = dependecies ,
    executables = [Executable("start.py", base = None)]
)