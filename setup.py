# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.0'


setup(
    name='graphic-verification-code',
    version=version,
    keywords='Graphic Verification Code',
    description='Graphic Verification Code',
    long_description=open('README.rst').read(),

    url='https://github.com/Brightcells/graphic-verification-code',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['gvcode'],
    py_modules=[],
    install_requires=['Pillow'],
    package_data={
        '': ['*.ttc', '*.ttf'],
        'resource/images': ['*.png']
    },
    include_package_data=True,

    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
