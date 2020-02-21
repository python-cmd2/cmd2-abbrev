#
# coding=utf-8

import os
import setuptools

#
# get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='cmd2-abbrev',
    use_scm_version=True,

    description='Plugin to add command abbreviation support to cmd2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='cmd2 plugin abbrev',

    author='Kotfu',
    author_email='kotfu@kotfu.net',
    url='https://github.com/python-cmd2/cmd2-abbrev',
    license='MIT',

    packages=['cmd2_abbrev'],

    python_requires='>=3.5',
    install_requires=['cmd2 >= 0.10.0, <=2'],

    setup_requires=['setuptools_scm'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    # dependencies for development and testing
    # $ pip install -e .[dev]
    extras_require={
        'dev': ['setuptools_scm', 'pytest', 'codecov', 'pytest-cov',
                'flake8', 'invoke', 'wheel', 'twine']
    },
)
