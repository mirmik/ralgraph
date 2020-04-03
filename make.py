#!/usr/bin/env python3
#coding:utf-8

import os
import licant
import licant.install

licant.execute("ralgraph.g.py")

licant.cxx_shared_library("libralgraph.so",
	mdepends=[
		"ralgraph",
	],
	cxx_flags="-fPIC",
	cc_flags="-fPIC"
)

licant.install.install_library(
	tgt="install",
	uninstall="uninstall",
	libtgt="libralgraph.so",
	hroot="ralgraph",
	headers="ralgraph")

licant.ex("libralgraph.so")