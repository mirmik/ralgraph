#!/usr/bin/env python3

import licant

licant.module("ralgraph",
	sources = [
		"ralgraph/show.cpp"
	],
	moc=["ralgraph/chart.h"],
	include_paths=["."]
)