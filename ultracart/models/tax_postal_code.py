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


class TaxPostalCode(object):
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
        'city_oid': 'int',
        'dont_collect_postal_code': 'bool',
        'postal_code': 'str',
        'postal_code_oid': 'int',
        'tax_rate': 'float',
        'tax_rate_formatted': 'str'
    }

    attribute_map = {
        'accounting_code': 'accounting_code',
        'city_oid': 'city_oid',
        'dont_collect_postal_code': 'dont_collect_postal_code',
        'postal_code': 'postal_code',
        'postal_code_oid': 'postal_code_oid',
        'tax_rate': 'tax_rate',
        'tax_rate_formatted': 'tax_rate_formatted'
    }

    def __init__(self, accounting_code=None, city_oid=None, dont_collect_postal_code=None, postal_code=None, postal_code_oid=None, tax_rate=None, tax_rate_formatted=None):
        """
        TaxPostalCode - a model defined in Swagger
        """

        self._accounting_code = None
        self._city_oid = None
        self._dont_collect_postal_code = None
        self._postal_code = None
        self._postal_code_oid = None
        self._tax_rate = None
        self._tax_rate_formatted = None
        self.discriminator = None

        if accounting_code is not None:
          self.accounting_code = accounting_code
        if city_oid is not None:
          self.city_oid = city_oid
        if dont_collect_postal_code is not None:
          self.dont_collect_postal_code = dont_collect_postal_code
        if postal_code is not None:
          self.postal_code = postal_code
        if postal_code_oid is not None:
          self.postal_code_oid = postal_code_oid
        if tax_rate is not None:
          self.tax_rate = tax_rate
        if tax_rate_formatted is not None:
          self.tax_rate_formatted = tax_rate_formatted

    @property
    def accounting_code(self):
        """
        Gets the accounting_code of this TaxPostalCode.
        Accounting code for programs such as QuickBooks

        :return: The accounting_code of this TaxPostalCode.
        :rtype: str
        """
        return self._accounting_code

    @accounting_code.setter
    def accounting_code(self, accounting_code):
        """
        Sets the accounting_code of this TaxPostalCode.
        Accounting code for programs such as QuickBooks

        :param accounting_code: The accounting_code of this TaxPostalCode.
        :type: str
        """

        self._accounting_code = accounting_code

    @property
    def city_oid(self):
        """
        Gets the city_oid of this TaxPostalCode.
        Tax record object identifier used internally by database

        :return: The city_oid of this TaxPostalCode.
        :rtype: int
        """
        return self._city_oid

    @city_oid.setter
    def city_oid(self, city_oid):
        """
        Sets the city_oid of this TaxPostalCode.
        Tax record object identifier used internally by database

        :param city_oid: The city_oid of this TaxPostalCode.
        :type: int
        """

        self._city_oid = city_oid

    @property
    def dont_collect_postal_code(self):
        """
        Gets the dont_collect_postal_code of this TaxPostalCode.
        Flag instructing engine to not collect postal code tax for this postal code

        :return: The dont_collect_postal_code of this TaxPostalCode.
        :rtype: bool
        """
        return self._dont_collect_postal_code

    @dont_collect_postal_code.setter
    def dont_collect_postal_code(self, dont_collect_postal_code):
        """
        Sets the dont_collect_postal_code of this TaxPostalCode.
        Flag instructing engine to not collect postal code tax for this postal code

        :param dont_collect_postal_code: The dont_collect_postal_code of this TaxPostalCode.
        :type: bool
        """

        self._dont_collect_postal_code = dont_collect_postal_code

    @property
    def postal_code(self):
        """
        Gets the postal_code of this TaxPostalCode.
        Postal Code (5 digits)

        :return: The postal_code of this TaxPostalCode.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this TaxPostalCode.
        Postal Code (5 digits)

        :param postal_code: The postal_code of this TaxPostalCode.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def postal_code_oid(self):
        """
        Gets the postal_code_oid of this TaxPostalCode.
        Tax record object identifier used internally by database

        :return: The postal_code_oid of this TaxPostalCode.
        :rtype: int
        """
        return self._postal_code_oid

    @postal_code_oid.setter
    def postal_code_oid(self, postal_code_oid):
        """
        Sets the postal_code_oid of this TaxPostalCode.
        Tax record object identifier used internally by database

        :param postal_code_oid: The postal_code_oid of this TaxPostalCode.
        :type: int
        """

        self._postal_code_oid = postal_code_oid

    @property
    def tax_rate(self):
        """
        Gets the tax_rate of this TaxPostalCode.
        Tax Rate

        :return: The tax_rate of this TaxPostalCode.
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """
        Sets the tax_rate of this TaxPostalCode.
        Tax Rate

        :param tax_rate: The tax_rate of this TaxPostalCode.
        :type: float
        """

        self._tax_rate = tax_rate

    @property
    def tax_rate_formatted(self):
        """
        Gets the tax_rate_formatted of this TaxPostalCode.
        Tax rate formatted

        :return: The tax_rate_formatted of this TaxPostalCode.
        :rtype: str
        """
        return self._tax_rate_formatted

    @tax_rate_formatted.setter
    def tax_rate_formatted(self, tax_rate_formatted):
        """
        Sets the tax_rate_formatted of this TaxPostalCode.
        Tax rate formatted

        :param tax_rate_formatted: The tax_rate_formatted of this TaxPostalCode.
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
        if not isinstance(other, TaxPostalCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
