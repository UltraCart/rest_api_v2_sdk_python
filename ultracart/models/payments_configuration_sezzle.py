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


class PaymentsConfigurationSezzle(object):
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
        'accept_sezzle': 'bool',
        'restrictions': 'PaymentsConfigurationRestrictions',
        'sezzle_accounting_code': 'str',
        'sezzle_business_id': 'str',
        'sezzle_deposit_to_account': 'str',
        'sezzle_environment': 'str',
        'sezzle_private_api_key': 'str',
        'sezzle_public_api_key': 'str'
    }

    attribute_map = {
        'accept_sezzle': 'acceptSezzle',
        'restrictions': 'restrictions',
        'sezzle_accounting_code': 'sezzleAccountingCode',
        'sezzle_business_id': 'sezzleBusinessId',
        'sezzle_deposit_to_account': 'sezzleDepositToAccount',
        'sezzle_environment': 'sezzleEnvironment',
        'sezzle_private_api_key': 'sezzlePrivateApiKey',
        'sezzle_public_api_key': 'sezzlePublicApiKey'
    }

    def __init__(self, accept_sezzle=None, restrictions=None, sezzle_accounting_code=None, sezzle_business_id=None, sezzle_deposit_to_account=None, sezzle_environment=None, sezzle_private_api_key=None, sezzle_public_api_key=None):  # noqa: E501
        """PaymentsConfigurationSezzle - a model defined in Swagger"""  # noqa: E501

        self._accept_sezzle = None
        self._restrictions = None
        self._sezzle_accounting_code = None
        self._sezzle_business_id = None
        self._sezzle_deposit_to_account = None
        self._sezzle_environment = None
        self._sezzle_private_api_key = None
        self._sezzle_public_api_key = None
        self.discriminator = None

        if accept_sezzle is not None:
            self.accept_sezzle = accept_sezzle
        if restrictions is not None:
            self.restrictions = restrictions
        if sezzle_accounting_code is not None:
            self.sezzle_accounting_code = sezzle_accounting_code
        if sezzle_business_id is not None:
            self.sezzle_business_id = sezzle_business_id
        if sezzle_deposit_to_account is not None:
            self.sezzle_deposit_to_account = sezzle_deposit_to_account
        if sezzle_environment is not None:
            self.sezzle_environment = sezzle_environment
        if sezzle_private_api_key is not None:
            self.sezzle_private_api_key = sezzle_private_api_key
        if sezzle_public_api_key is not None:
            self.sezzle_public_api_key = sezzle_public_api_key

    @property
    def accept_sezzle(self):
        """Gets the accept_sezzle of this PaymentsConfigurationSezzle.  # noqa: E501


        :return: The accept_sezzle of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: bool
        """
        return self._accept_sezzle

    @accept_sezzle.setter
    def accept_sezzle(self, accept_sezzle):
        """Sets the accept_sezzle of this PaymentsConfigurationSezzle.


        :param accept_sezzle: The accept_sezzle of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: bool
        """

        self._accept_sezzle = accept_sezzle

    @property
    def restrictions(self):
        """Gets the restrictions of this PaymentsConfigurationSezzle.  # noqa: E501


        :return: The restrictions of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: PaymentsConfigurationRestrictions
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this PaymentsConfigurationSezzle.


        :param restrictions: The restrictions of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: PaymentsConfigurationRestrictions
        """

        self._restrictions = restrictions

    @property
    def sezzle_accounting_code(self):
        """Gets the sezzle_accounting_code of this PaymentsConfigurationSezzle.  # noqa: E501


        :return: The sezzle_accounting_code of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: str
        """
        return self._sezzle_accounting_code

    @sezzle_accounting_code.setter
    def sezzle_accounting_code(self, sezzle_accounting_code):
        """Sets the sezzle_accounting_code of this PaymentsConfigurationSezzle.


        :param sezzle_accounting_code: The sezzle_accounting_code of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: str
        """

        self._sezzle_accounting_code = sezzle_accounting_code

    @property
    def sezzle_business_id(self):
        """Gets the sezzle_business_id of this PaymentsConfigurationSezzle.  # noqa: E501


        :return: The sezzle_business_id of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: str
        """
        return self._sezzle_business_id

    @sezzle_business_id.setter
    def sezzle_business_id(self, sezzle_business_id):
        """Sets the sezzle_business_id of this PaymentsConfigurationSezzle.


        :param sezzle_business_id: The sezzle_business_id of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: str
        """

        self._sezzle_business_id = sezzle_business_id

    @property
    def sezzle_deposit_to_account(self):
        """Gets the sezzle_deposit_to_account of this PaymentsConfigurationSezzle.  # noqa: E501


        :return: The sezzle_deposit_to_account of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: str
        """
        return self._sezzle_deposit_to_account

    @sezzle_deposit_to_account.setter
    def sezzle_deposit_to_account(self, sezzle_deposit_to_account):
        """Sets the sezzle_deposit_to_account of this PaymentsConfigurationSezzle.


        :param sezzle_deposit_to_account: The sezzle_deposit_to_account of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: str
        """

        self._sezzle_deposit_to_account = sezzle_deposit_to_account

    @property
    def sezzle_environment(self):
        """Gets the sezzle_environment of this PaymentsConfigurationSezzle.  # noqa: E501


        :return: The sezzle_environment of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: str
        """
        return self._sezzle_environment

    @sezzle_environment.setter
    def sezzle_environment(self, sezzle_environment):
        """Sets the sezzle_environment of this PaymentsConfigurationSezzle.


        :param sezzle_environment: The sezzle_environment of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: str
        """

        self._sezzle_environment = sezzle_environment

    @property
    def sezzle_private_api_key(self):
        """Gets the sezzle_private_api_key of this PaymentsConfigurationSezzle.  # noqa: E501


        :return: The sezzle_private_api_key of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: str
        """
        return self._sezzle_private_api_key

    @sezzle_private_api_key.setter
    def sezzle_private_api_key(self, sezzle_private_api_key):
        """Sets the sezzle_private_api_key of this PaymentsConfigurationSezzle.


        :param sezzle_private_api_key: The sezzle_private_api_key of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: str
        """

        self._sezzle_private_api_key = sezzle_private_api_key

    @property
    def sezzle_public_api_key(self):
        """Gets the sezzle_public_api_key of this PaymentsConfigurationSezzle.  # noqa: E501


        :return: The sezzle_public_api_key of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: str
        """
        return self._sezzle_public_api_key

    @sezzle_public_api_key.setter
    def sezzle_public_api_key(self, sezzle_public_api_key):
        """Sets the sezzle_public_api_key of this PaymentsConfigurationSezzle.


        :param sezzle_public_api_key: The sezzle_public_api_key of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: str
        """

        self._sezzle_public_api_key = sezzle_public_api_key

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
        if issubclass(PaymentsConfigurationSezzle, dict):
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
        if not isinstance(other, PaymentsConfigurationSezzle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
