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


class PaymentsConfigurationCOD(object):
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
        'accept_cod': 'bool',
        'approved_customers_only': 'bool',
        'restrictions': 'PaymentsConfigurationRestrictions',
        'surcharge_accounting_code': 'str',
        'surcharge_fee': 'float',
        'surcharge_percentage': 'float'
    }

    attribute_map = {
        'accept_cod': 'accept_cod',
        'approved_customers_only': 'approved_customers_only',
        'restrictions': 'restrictions',
        'surcharge_accounting_code': 'surcharge_accounting_code',
        'surcharge_fee': 'surcharge_fee',
        'surcharge_percentage': 'surcharge_percentage'
    }

    def __init__(self, accept_cod=None, approved_customers_only=None, restrictions=None, surcharge_accounting_code=None, surcharge_fee=None, surcharge_percentage=None):  # noqa: E501
        """PaymentsConfigurationCOD - a model defined in Swagger"""  # noqa: E501

        self._accept_cod = None
        self._approved_customers_only = None
        self._restrictions = None
        self._surcharge_accounting_code = None
        self._surcharge_fee = None
        self._surcharge_percentage = None
        self.discriminator = None

        if accept_cod is not None:
            self.accept_cod = accept_cod
        if approved_customers_only is not None:
            self.approved_customers_only = approved_customers_only
        if restrictions is not None:
            self.restrictions = restrictions
        if surcharge_accounting_code is not None:
            self.surcharge_accounting_code = surcharge_accounting_code
        if surcharge_fee is not None:
            self.surcharge_fee = surcharge_fee
        if surcharge_percentage is not None:
            self.surcharge_percentage = surcharge_percentage

    @property
    def accept_cod(self):
        """Gets the accept_cod of this PaymentsConfigurationCOD.  # noqa: E501

        Master flag indicating this merchant accepts COD  # noqa: E501

        :return: The accept_cod of this PaymentsConfigurationCOD.  # noqa: E501
        :rtype: bool
        """
        return self._accept_cod

    @accept_cod.setter
    def accept_cod(self, accept_cod):
        """Sets the accept_cod of this PaymentsConfigurationCOD.

        Master flag indicating this merchant accepts COD  # noqa: E501

        :param accept_cod: The accept_cod of this PaymentsConfigurationCOD.  # noqa: E501
        :type: bool
        """

        self._accept_cod = accept_cod

    @property
    def approved_customers_only(self):
        """Gets the approved_customers_only of this PaymentsConfigurationCOD.  # noqa: E501

        If true, only approved customers may pay with COD  # noqa: E501

        :return: The approved_customers_only of this PaymentsConfigurationCOD.  # noqa: E501
        :rtype: bool
        """
        return self._approved_customers_only

    @approved_customers_only.setter
    def approved_customers_only(self, approved_customers_only):
        """Sets the approved_customers_only of this PaymentsConfigurationCOD.

        If true, only approved customers may pay with COD  # noqa: E501

        :param approved_customers_only: The approved_customers_only of this PaymentsConfigurationCOD.  # noqa: E501
        :type: bool
        """

        self._approved_customers_only = approved_customers_only

    @property
    def restrictions(self):
        """Gets the restrictions of this PaymentsConfigurationCOD.  # noqa: E501


        :return: The restrictions of this PaymentsConfigurationCOD.  # noqa: E501
        :rtype: PaymentsConfigurationRestrictions
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this PaymentsConfigurationCOD.


        :param restrictions: The restrictions of this PaymentsConfigurationCOD.  # noqa: E501
        :type: PaymentsConfigurationRestrictions
        """

        self._restrictions = restrictions

    @property
    def surcharge_accounting_code(self):
        """Gets the surcharge_accounting_code of this PaymentsConfigurationCOD.  # noqa: E501

        Optional field, if surcharge is set, this is the accounting code the surcharge is tagged with when sent to Quickbooks  # noqa: E501

        :return: The surcharge_accounting_code of this PaymentsConfigurationCOD.  # noqa: E501
        :rtype: str
        """
        return self._surcharge_accounting_code

    @surcharge_accounting_code.setter
    def surcharge_accounting_code(self, surcharge_accounting_code):
        """Sets the surcharge_accounting_code of this PaymentsConfigurationCOD.

        Optional field, if surcharge is set, this is the accounting code the surcharge is tagged with when sent to Quickbooks  # noqa: E501

        :param surcharge_accounting_code: The surcharge_accounting_code of this PaymentsConfigurationCOD.  # noqa: E501
        :type: str
        """

        self._surcharge_accounting_code = surcharge_accounting_code

    @property
    def surcharge_fee(self):
        """Gets the surcharge_fee of this PaymentsConfigurationCOD.  # noqa: E501

        Additional cost for using COD  # noqa: E501

        :return: The surcharge_fee of this PaymentsConfigurationCOD.  # noqa: E501
        :rtype: float
        """
        return self._surcharge_fee

    @surcharge_fee.setter
    def surcharge_fee(self, surcharge_fee):
        """Sets the surcharge_fee of this PaymentsConfigurationCOD.

        Additional cost for using COD  # noqa: E501

        :param surcharge_fee: The surcharge_fee of this PaymentsConfigurationCOD.  # noqa: E501
        :type: float
        """

        self._surcharge_fee = surcharge_fee

    @property
    def surcharge_percentage(self):
        """Gets the surcharge_percentage of this PaymentsConfigurationCOD.  # noqa: E501

        Additional percentage cost for using COD  # noqa: E501

        :return: The surcharge_percentage of this PaymentsConfigurationCOD.  # noqa: E501
        :rtype: float
        """
        return self._surcharge_percentage

    @surcharge_percentage.setter
    def surcharge_percentage(self, surcharge_percentage):
        """Sets the surcharge_percentage of this PaymentsConfigurationCOD.

        Additional percentage cost for using COD  # noqa: E501

        :param surcharge_percentage: The surcharge_percentage of this PaymentsConfigurationCOD.  # noqa: E501
        :type: float
        """

        self._surcharge_percentage = surcharge_percentage

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
        if issubclass(PaymentsConfigurationCOD, dict):
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
        if not isinstance(other, PaymentsConfigurationCOD):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
