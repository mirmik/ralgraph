#!/usr/bin/env python3

import os
import shutil
import licant 

licant.include("ralgraph", "ralgraph.g.py")

target = "libralgraph.so"

install_include_path = '/usr/local/include/ralgraph' 
install_directory_path = '/usr/lib/'
install_library_path = os.path.join(install_directory_path, target)

licant.cxx_shared_library(target,
	mdepends=["ralgraph"],
	libs=["Qt5Core", "Qt5Widgets", "Qt5Charts", "nos", "igris"],
	include_paths=[
		".",
		"/usr/include/x86_64-linux-gnu/qt5/", 
		"/usr/include/x86_64-linux-gnu/qt5/QtCore",
		"/usr/include/x86_64-linux-gnu/qt5/QtWidgets",
		"/usr/include/x86_64-linux-gnu/qt5/QtCharts"
	],
	cxx_flags="-fPIC"
)

@licant.routine(deps=["libralgraph.so"])
def install():
	os.system("cp {0} {1}".format(target, install_directory_path))
	
	shutil.rmtree(install_include_path, True)
	shutil.copytree("ralgraph", install_include_path, 
		symlinks=False, ignore=shutil.ignore_patterns('*.cpp', '*.c'))
	
	print("successfully installed")


licant.ex("libralgraph.so")