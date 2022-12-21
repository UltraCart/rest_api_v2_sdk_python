# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TaxStateCode(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'state_code': 'str',
        'state_name': 'str',
        'tax_rate': 'float',
        'tax_rate_formatted': 'str'
    }

    attribute_map = {
        'accounting_code': 'accounting_code',
        'state_code': 'state_code',
        'state_name': 'state_name',
        'tax_rate': 'tax_rate',
        'tax_rate_formatted': 'tax_rate_formatted'
    }

    def __init__(self, accounting_code=None, state_code=None, state_name=None, tax_rate=None, tax_rate_formatted=None):  # noqa: E501
        """TaxStateCode - a model defined in Swagger"""  # noqa: E501

        self._accounting_code = None
        self._state_code = None
        self._state_name = None
        self._tax_rate = None
        self._tax_rate_formatted = None
        self.discriminator = None

        if accounting_code is not None:
            self.accounting_code = accounting_code
        if state_code is not None:
            self.state_code = state_code
        if state_name is not None:
            self.state_name = state_name
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if tax_rate_formatted is not None:
            self.tax_rate_formatted = tax_rate_formatted

    @property
    def accounting_code(self):
        """Gets the accounting_code of this TaxStateCode.  # noqa: E501

        Accounting code for programs such as QuickBooks  # noqa: E501

        :return: The accounting_code of this TaxStateCode.  # noqa: E501
        :rtype: str
        """
        return self._accounting_code

    @accounting_code.setter
    def accounting_code(self, accounting_code):
        """Sets the accounting_code of this TaxStateCode.

        Accounting code for programs such as QuickBooks  # noqa: E501

        :param accounting_code: The accounting_code of this TaxStateCode.  # noqa: E501
        :type: str
        """

        self._accounting_code = accounting_code

    @property
    def state_code(self):
        """Gets the state_code of this TaxStateCode.  # noqa: E501

        State code (2 characters  # noqa: E501

        :return: The state_code of this TaxStateCode.  # noqa: E501
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """Sets the state_code of this TaxStateCode.

        State code (2 characters  # noqa: E501

        :param state_code: The state_code of this TaxStateCode.  # noqa: E501
        :type: str
        """

        self._state_code = state_code

    @property
    def state_name(self):
        """Gets the state_name of this TaxStateCode.  # noqa: E501

        State name  # noqa: E501

        :return: The state_name of this TaxStateCode.  # noqa: E501
        :rtype: str
        """
        return self._state_name

    @state_name.setter
    def state_name(self, state_name):
        """Sets the state_name of this TaxStateCode.

        State name  # noqa: E501

        :param state_name: The state_name of this TaxStateCode.  # noqa: E501
        :type: str
        """

        self._state_name = state_name

    @property
    def tax_rate(self):
        """Gets the tax_rate of this TaxStateCode.  # noqa: E501

        Tax Rate  # noqa: E501

        :return: The tax_rate of this TaxStateCode.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this TaxStateCode.

        Tax Rate  # noqa: E501

        :param tax_rate: The tax_rate of this TaxStateCode.  # noqa: E501
        :type: float
        """

        self._tax_rate = tax_rate

    @property
    def tax_rate_formatted(self):
        """Gets the tax_rate_formatted of this TaxStateCode.  # noqa: E501

        Tax rate formatted  # noqa: E501

        :return: The tax_rate_formatted of this TaxStateCode.  # noqa: E501
        :rtype: str
        """
        return self._tax_rate_formatted

    @tax_rate_formatted.setter
    def tax_rate_formatted(self, tax_rate_formatted):
        """Sets the tax_rate_formatted of this TaxStateCode.

        Tax rate formatted  # noqa: E501

        :param tax_rate_formatted: The tax_rate_formatted of this TaxStateCode.  # noqa: E501
        :type: str
        """

        self._tax_rate_formatted = tax_rate_formatted

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(TaxStateCode, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaxStateCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other