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


class PaymentsConfigurationEcheck(object):
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
        'accept_e_check': 'bool',
        'e_check_accounting_code': 'str',
        'e_check_deposit_to_account': 'str',
        'restrictions': 'PaymentsConfigurationRestrictions'
    }

    attribute_map = {
        'accept_e_check': 'acceptECheck',
        'e_check_accounting_code': 'eCheckAccountingCode',
        'e_check_deposit_to_account': 'eCheckDepositToAccount',
        'restrictions': 'restrictions'
    }

    def __init__(self, accept_e_check=None, e_check_accounting_code=None, e_check_deposit_to_account=None, restrictions=None):  # noqa: E501
        """PaymentsConfigurationEcheck - a model defined in Swagger"""  # noqa: E501

        self._accept_e_check = None
        self._e_check_accounting_code = None
        self._e_check_deposit_to_account = None
        self._restrictions = None
        self.discriminator = None

        if accept_e_check is not None:
            self.accept_e_check = accept_e_check
        if e_check_accounting_code is not None:
            self.e_check_accounting_code = e_check_accounting_code
        if e_check_deposit_to_account is not None:
            self.e_check_deposit_to_account = e_check_deposit_to_account
        if restrictions is not None:
            self.restrictions = restrictions

    @property
    def accept_e_check(self):
        """Gets the accept_e_check of this PaymentsConfigurationEcheck.  # noqa: E501


        :return: The accept_e_check of this PaymentsConfigurationEcheck.  # noqa: E501
        :rtype: bool
        """
        return self._accept_e_check

    @accept_e_check.setter
    def accept_e_check(self, accept_e_check):
        """Sets the accept_e_check of this PaymentsConfigurationEcheck.


        :param accept_e_check: The accept_e_check of this PaymentsConfigurationEcheck.  # noqa: E501
        :type: bool
        """

        self._accept_e_check = accept_e_check

    @property
    def e_check_accounting_code(self):
        """Gets the e_check_accounting_code of this PaymentsConfigurationEcheck.  # noqa: E501


        :return: The e_check_accounting_code of this PaymentsConfigurationEcheck.  # noqa: E501
        :rtype: str
        """
        return self._e_check_accounting_code

    @e_check_accounting_code.setter
    def e_check_accounting_code(self, e_check_accounting_code):
        """Sets the e_check_accounting_code of this PaymentsConfigurationEcheck.


        :param e_check_accounting_code: The e_check_accounting_code of this PaymentsConfigurationEcheck.  # noqa: E501
        :type: str
        """

        self._e_check_accounting_code = e_check_accounting_code

    @property
    def e_check_deposit_to_account(self):
        """Gets the e_check_deposit_to_account of this PaymentsConfigurationEcheck.  # noqa: E501


        :return: The e_check_deposit_to_account of this PaymentsConfigurationEcheck.  # noqa: E501
        :rtype: str
        """
        return self._e_check_deposit_to_account

    @e_check_deposit_to_account.setter
    def e_check_deposit_to_account(self, e_check_deposit_to_account):
        """Sets the e_check_deposit_to_account of this PaymentsConfigurationEcheck.


        :param e_check_deposit_to_account: The e_check_deposit_to_account of this PaymentsConfigurationEcheck.  # noqa: E501
        :type: str
        """

        self._e_check_deposit_to_account = e_check_deposit_to_account

    @property
    def restrictions(self):
        """Gets the restrictions of this PaymentsConfigurationEcheck.  # noqa: E501


        :return: The restrictions of this PaymentsConfigurationEcheck.  # noqa: E501
        :rtype: PaymentsConfigurationRestrictions
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this PaymentsConfigurationEcheck.


        :param restrictions: The restrictions of this PaymentsConfigurationEcheck.  # noqa: E501
        :type: PaymentsConfigurationRestrictions
        """

        self._restrictions = restrictions

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
        if issubclass(PaymentsConfigurationEcheck, dict):
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
        if not isinstance(other, PaymentsConfigurationEcheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
