#!/usr/bin/env python3

import os
import licant

licant.include("ralgraph", "../../ralgraph.g.py")

try:
	for root, dirs, files in os.walk("/usr/include"):
		for dr in dirs:
			if dr == "qt5":
				libqt_include_path = os.path.join(root, dr)
				raise Found()
except:
	pass
		

licant.cxx_application("target",
	sources = ["main.cpp"],
	mdepends=["ralgraph"],
	libs=["Qt5Core", "Qt5Widgets", "Qt5Charts", "nos", "igris"],
	include_paths=[
		libqt_include_path, 
		".",
		"/usr/include/x86_64-linux-gnu/qt5/", 
		"/usr/include/x86_64-linux-gnu/qt5/QtCore",
		"/usr/include/x86_64-linux-gnu/qt5/QtWidgets",
		"/usr/include/x86_64-linux-gnu/qt5/QtCharts"
	],
	cxx_flags="-fPIC"
)

licant.ex("target")