#!/usr/bin/env python3

import licant

licant.include("ralgraph")

licant.cxx_application("target",
	sources=["main.cpp"],
	mdepends=["ralgraph"],
	libs = [ "glfw3", "vulkan", "dl", "pthread", "GLEW", "GL", "GLU"]
	# "glfw3", "vulkan", "dl", "pthread", "GLEW", "GL", "GLU"
)

licant.ex("target")