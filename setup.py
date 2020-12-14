#!/usr/bin/env python

from setuptools import setup


def long_description():
    with open('README.md') as fd:
        return fd.read()


setup(
    name='gwcli',
    version='0.1.0',
    author='Rigel Di Scala',
    author_email='zedr@zedr.com',
    description='',
    license='MIT',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/zedr/gwcli',
    install_requires=[
    ],
    package_dir={'': 'src'},
    packages=['gwcli'],
    py_modules=['gwcli'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['gwcli=gwcli.main:main']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7'
)
