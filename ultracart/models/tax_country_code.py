# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TaxCountryCode(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'accounting_code': 'str',
        'country_code': 'str',
        'country_name': 'str',
        'tax_rate': 'float',
        'tax_rate_formatted': 'str'
    }

    attribute_map = {
        'accounting_code': 'accounting_code',
        'country_code': 'country_code',
        'country_name': 'country_name',
        'tax_rate': 'tax_rate',
        'tax_rate_formatted': 'tax_rate_formatted'
    }

    def __init__(self, accounting_code=None, country_code=None, country_name=None, tax_rate=None, tax_rate_formatted=None):
        """
        TaxCountryCode - a model defined in Swagger
        """

        self._accounting_code = None
        self._country_code = None
        self._country_name = None
        self._tax_rate = None
        self._tax_rate_formatted = None
        self.discriminator = None

        if accounting_code is not None:
          self.accounting_code = accounting_code
        if country_code is not None:
          self.country_code = country_code
        if country_name is not None:
          self.country_name = country_name
        if tax_rate is not None:
          self.tax_rate = tax_rate
        if tax_rate_formatted is not None:
          self.tax_rate_formatted = tax_rate_formatted

    @property
    def accounting_code(self):
        """
        Gets the accounting_code of this TaxCountryCode.
        Accounting code for programs such as QuickBooks

        :return: The accounting_code of this TaxCountryCode.
        :rtype: str
        """
        return self._accounting_code

    @accounting_code.setter
    def accounting_code(self, accounting_code):
        """
        Sets the accounting_code of this TaxCountryCode.
        Accounting code for programs such as QuickBooks

        :param accounting_code: The accounting_code of this TaxCountryCode.
        :type: str
        """

        self._accounting_code = accounting_code

    @property
    def country_code(self):
        """
        Gets the country_code of this TaxCountryCode.
        Country code (2 characters

        :return: The country_code of this TaxCountryCode.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this TaxCountryCode.
        Country code (2 characters

        :param country_code: The country_code of this TaxCountryCode.
        :type: str
        """

        self._country_code = country_code

    @property
    def country_name(self):
        """
        Gets the country_name of this TaxCountryCode.
        Country name

        :return: The country_name of this TaxCountryCode.
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """
        Sets the country_name of this TaxCountryCode.
        Country name

        :param country_name: The country_name of this TaxCountryCode.
        :type: str
        """

        self._country_name = country_name

    @property
    def tax_rate(self):
        """
        Gets the tax_rate of this TaxCountryCode.
        Tax Rate

        :return: The tax_rate of this TaxCountryCode.
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """
        Sets the tax_rate of this TaxCountryCode.
        Tax Rate

        :param tax_rate: The tax_rate of this TaxCountryCode.
        :type: float
        """

        self._tax_rate = tax_rate

    @property
    def tax_rate_formatted(self):
        """
        Gets the tax_rate_formatted of this TaxCountryCode.
        Tax rate formatted

        :return: The tax_rate_formatted of this TaxCountryCode.
        :rtype: str
        """
        return self._tax_rate_formatted

    @tax_rate_formatted.setter
    def tax_rate_formatted(self, tax_rate_formatted):
        """
        Sets the tax_rate_formatted of this TaxCountryCode.
        Tax rate formatted

        :param tax_rate_formatted: The tax_rate_formatted of this TaxCountryCode.
        :type: str
        """

        self._tax_rate_formatted = tax_rate_formatted

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TaxCountryCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
