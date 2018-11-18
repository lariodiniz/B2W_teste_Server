#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from setuptools import find_packages, setup

setup(
    name='sw_server',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)