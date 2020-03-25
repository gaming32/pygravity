import setuptools
from Cython.Build import cythonize

setuptools.setup(
    name = 'python-gravity',
    version = '0.1.0',
    url = 'https://github.com/gaming32/pygravity',
    author = 'Gaming32',
    author_email = 'gaming32i64@gmail.com',
    license = 'License :: OSI Approved :: MIT License',
    description = 'Library for calculating stuff having to do with gravity',
    long_description = '',
    long_description_content_type = 'text/markdown',
    packages = [
        'pygravity',
        'pygravity.2d',
    ],
    ext_modules = cythonize('pygravity/math.pyx'),
    zip_safe = False,
)