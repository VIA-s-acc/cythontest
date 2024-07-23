from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sourceFiles = ['nogil.pyx']

ext_modules = [
    Extension("nogil", 
            sources=sourceFiles),
]

setup(name = 'test',
      cmdclass={'build_ext': build_ext},
      ext_modules=ext_modules)



#  python .\setup.py built_ext -b build