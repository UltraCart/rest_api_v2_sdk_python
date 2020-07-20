# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "UltraCart REST SDK"
VERSION = "2.4.123"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="UltraCart Rest API V2",
    author_email="support@ultracart.com",
    url="",
    keywords=["Swagger", "UltraCart Rest API V2"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    UltraCart REST API Version 2
    """
)
