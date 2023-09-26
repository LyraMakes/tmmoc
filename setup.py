#from distutils.core import setup, Extension

from setuptools import setup, Extension

tmmoc_module = Extension('tmmoc', sources=['tmmocmodule.c'])

setup(ext_modules=[tmmoc_module])
