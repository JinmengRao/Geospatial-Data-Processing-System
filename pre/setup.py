# setup.py
from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(ext_modules = cythonize(Extension(
    'CY_stdAttImpl_worker',
    sources=['CY_stdAttImpl_worker.pyx'],
    language='c',
    include_dirs=[],
    library_dirs=[],
    libraries=[],
    extra_compile_args=[],
    extra_link_args=[]
)))