#!/usr/bin/env python3

from wheel.bdist_wheel import bdist_wheel as bdist_wheel_
from setuptools import setup, Extension, Command
from distutils.util import get_platform

import glob
import sys
import os

directory = os.path.dirname(os.path.realpath(__file__))

requires = [
        "evalcache>=1.11.0",
        "PyQt5!=5.14.1",
        "psutil"
    ] 

setup(
    name="ralgraph",
    packages=["ralgraph"],
    version="0.0.1",
    license="MIT",
    description="Sandbox for computationally-graphical scripts",
    author="mirmik",
    author_email="netricks@protonmail.com",
    url="https://github.com/mirmik/ralgraph",
    long_description=open(os.path.join(directory, "README.md"), "r").read(),
    long_description_content_type="text/markdown",
    keywords=["sandbox"],
    classifiers=[],
    package_data={
        "ralgraph": []
    },
    include_package_data=True,
    install_requires=requires,
    entry_points={"console_scripts": ["ralgraph=ralgraph.__main__:main"]},
)
