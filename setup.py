"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "ultracart_rest_sdk"
VERSION = "4.0.134"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="UltraCart Rest API V2",
    author="UltraCart Support",
    author_email="support@ultracart.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "UltraCart Rest API V2"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    UltraCart REST API Version 2  # noqa: E501
    """
)
