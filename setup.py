"""
This file holds all the information that setuptools need mae a package out of this module
"""

from setuptools import setup, find_packages
setup(
name="world-timer",
version="0.3.0",
author="Ezequiel Panzarasa",
author_email="ezequiel.panzarasa@gmail.com",
url="https://github.com/panza238/py_dev_ops",
description="A world-timer example package",
packages=find_packages(),
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
)