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
        'accounting_code': 'str',
        'business_id': 'str',
        'deposit_to_account': 'str',
        'environment': 'str',
        'environments': 'object',
        'private_api_key': 'str',
        'public_api_key': 'str',
        'restrictions': 'PaymentsConfigurationRestrictions'
    }

    attribute_map = {
        'accept_sezzle': 'accept_sezzle',
        'accounting_code': 'accounting_code',
        'business_id': 'business_id',
        'deposit_to_account': 'deposit_to_account',
        'environment': 'environment',
        'environments': 'environments',
        'private_api_key': 'private_api_key',
        'public_api_key': 'public_api_key',
        'restrictions': 'restrictions'
    }

    def __init__(self, accept_sezzle=None, accounting_code=None, business_id=None, deposit_to_account=None, environment=None, environments=None, private_api_key=None, public_api_key=None, restrictions=None):  # noqa: E501
        """PaymentsConfigurationSezzle - a model defined in Swagger"""  # noqa: E501

        self._accept_sezzle = None
        self._accounting_code = None
        self._business_id = None
        self._deposit_to_account = None
        self._environment = None
        self._environments = None
        self._private_api_key = None
        self._public_api_key = None
        self._restrictions = None
        self.discriminator = None

        if accept_sezzle is not None:
            self.accept_sezzle = accept_sezzle
        if accounting_code is not None:
            self.accounting_code = accounting_code
        if business_id is not None:
            self.business_id = business_id
        if deposit_to_account is not None:
            self.deposit_to_account = deposit_to_account
        if environment is not None:
            self.environment = environment
        if environments is not None:
            self.environments = environments
        if private_api_key is not None:
            self.private_api_key = private_api_key
        if public_api_key is not None:
            self.public_api_key = public_api_key
        if restrictions is not None:
            self.restrictions = restrictions

    @property
    def accept_sezzle(self):
        """Gets the accept_sezzle of this PaymentsConfigurationSezzle.  # noqa: E501

        Master flag for this merchant accepting Sezzle payments  # noqa: E501

        :return: The accept_sezzle of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: bool
        """
        return self._accept_sezzle

    @accept_sezzle.setter
    def accept_sezzle(self, accept_sezzle):
        """Sets the accept_sezzle of this PaymentsConfigurationSezzle.

        Master flag for this merchant accepting Sezzle payments  # noqa: E501

        :param accept_sezzle: The accept_sezzle of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: bool
        """

        self._accept_sezzle = accept_sezzle

    @property
    def accounting_code(self):
        """Gets the accounting_code of this PaymentsConfigurationSezzle.  # noqa: E501

        Optional Quickbooks code for this payment method  # noqa: E501

        :return: The accounting_code of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: str
        """
        return self._accounting_code

    @accounting_code.setter
    def accounting_code(self, accounting_code):
        """Sets the accounting_code of this PaymentsConfigurationSezzle.

        Optional Quickbooks code for this payment method  # noqa: E501

        :param accounting_code: The accounting_code of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: str
        """

        self._accounting_code = accounting_code

    @property
    def business_id(self):
        """Gets the business_id of this PaymentsConfigurationSezzle.  # noqa: E501

        Business ID  # noqa: E501

        :return: The business_id of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: str
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this PaymentsConfigurationSezzle.

        Business ID  # noqa: E501

        :param business_id: The business_id of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: str
        """

        self._business_id = business_id

    @property
    def deposit_to_account(self):
        """Gets the deposit_to_account of this PaymentsConfigurationSezzle.  # noqa: E501

        Optional Quickbooks Deposit to Account value  # noqa: E501

        :return: The deposit_to_account of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: str
        """
        return self._deposit_to_account

    @deposit_to_account.setter
    def deposit_to_account(self, deposit_to_account):
        """Sets the deposit_to_account of this PaymentsConfigurationSezzle.

        Optional Quickbooks Deposit to Account value  # noqa: E501

        :param deposit_to_account: The deposit_to_account of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: str
        """

        self._deposit_to_account = deposit_to_account

    @property
    def environment(self):
        """Gets the environment of this PaymentsConfigurationSezzle.  # noqa: E501

        Sezzle environment  # noqa: E501

        :return: The environment of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this PaymentsConfigurationSezzle.

        Sezzle environment  # noqa: E501

        :param environment: The environment of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: str
        """
        allowed_values = ["Live", "Sandbox"]  # noqa: E501
        if environment not in allowed_values:
            raise ValueError(
                "Invalid value for `environment` ({0}), must be one of {1}"  # noqa: E501
                .format(environment, allowed_values)
            )

        self._environment = environment

    @property
    def environments(self):
        """Gets the environments of this PaymentsConfigurationSezzle.  # noqa: E501

        List of environments possible  # noqa: E501

        :return: The environments of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: object
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """Sets the environments of this PaymentsConfigurationSezzle.

        List of environments possible  # noqa: E501

        :param environments: The environments of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: object
        """

        self._environments = environments

    @property
    def private_api_key(self):
        """Gets the private_api_key of this PaymentsConfigurationSezzle.  # noqa: E501

        Private API key  # noqa: E501

        :return: The private_api_key of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: str
        """
        return self._private_api_key

    @private_api_key.setter
    def private_api_key(self, private_api_key):
        """Sets the private_api_key of this PaymentsConfigurationSezzle.

        Private API key  # noqa: E501

        :param private_api_key: The private_api_key of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: str
        """

        self._private_api_key = private_api_key

    @property
    def public_api_key(self):
        """Gets the public_api_key of this PaymentsConfigurationSezzle.  # noqa: E501

        Public API key  # noqa: E501

        :return: The public_api_key of this PaymentsConfigurationSezzle.  # noqa: E501
        :rtype: str
        """
        return self._public_api_key

    @public_api_key.setter
    def public_api_key(self, public_api_key):
        """Sets the public_api_key of this PaymentsConfigurationSezzle.

        Public API key  # noqa: E501

        :param public_api_key: The public_api_key of this PaymentsConfigurationSezzle.  # noqa: E501
        :type: str
        """

        self._public_api_key = public_api_key

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
