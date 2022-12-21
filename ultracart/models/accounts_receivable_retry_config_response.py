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


class AccountsReceivableRetryConfigResponse(object):
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
        'config': 'AccountsReceivableRetryConfig',
        'coupon_codes': 'list[str]',
        'emails': 'list[str]',
        'error': 'Error',
        'has_linked_accounts': 'bool',
        'metadata': 'ResponseMetadata',
        'success': 'bool',
        'warning': 'Warning'
    }

    attribute_map = {
        'config': 'config',
        'coupon_codes': 'coupon_codes',
        'emails': 'emails',
        'error': 'error',
        'has_linked_accounts': 'has_linked_accounts',
        'metadata': 'metadata',
        'success': 'success',
        'warning': 'warning'
    }

    def __init__(self, config=None, coupon_codes=None, emails=None, error=None, has_linked_accounts=None, metadata=None, success=None, warning=None):  # noqa: E501
        """AccountsReceivableRetryConfigResponse - a model defined in Swagger"""  # noqa: E501

        self._config = None
        self._coupon_codes = None
        self._emails = None
        self._error = None
        self._has_linked_accounts = None
        self._metadata = None
        self._success = None
        self._warning = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if coupon_codes is not None:
            self.coupon_codes = coupon_codes
        if emails is not None:
            self.emails = emails
        if error is not None:
            self.error = error
        if has_linked_accounts is not None:
            self.has_linked_accounts = has_linked_accounts
        if metadata is not None:
            self.metadata = metadata
        if success is not None:
            self.success = success
        if warning is not None:
            self.warning = warning

    @property
    def config(self):
        """Gets the config of this AccountsReceivableRetryConfigResponse.  # noqa: E501


        :return: The config of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :rtype: AccountsReceivableRetryConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this AccountsReceivableRetryConfigResponse.


        :param config: The config of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :type: AccountsReceivableRetryConfig
        """

        self._config = config

    @property
    def coupon_codes(self):
        """Gets the coupon_codes of this AccountsReceivableRetryConfigResponse.  # noqa: E501


        :return: The coupon_codes of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._coupon_codes

    @coupon_codes.setter
    def coupon_codes(self, coupon_codes):
        """Sets the coupon_codes of this AccountsReceivableRetryConfigResponse.


        :param coupon_codes: The coupon_codes of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :type: list[str]
        """

        self._coupon_codes = coupon_codes

    @property
    def emails(self):
        """Gets the emails of this AccountsReceivableRetryConfigResponse.  # noqa: E501


        :return: The emails of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this AccountsReceivableRetryConfigResponse.


        :param emails: The emails of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :type: list[str]
        """

        self._emails = emails

    @property
    def error(self):
        """Gets the error of this AccountsReceivableRetryConfigResponse.  # noqa: E501


        :return: The error of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AccountsReceivableRetryConfigResponse.


        :param error: The error of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def has_linked_accounts(self):
        """Gets the has_linked_accounts of this AccountsReceivableRetryConfigResponse.  # noqa: E501


        :return: The has_linked_accounts of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_linked_accounts

    @has_linked_accounts.setter
    def has_linked_accounts(self, has_linked_accounts):
        """Sets the has_linked_accounts of this AccountsReceivableRetryConfigResponse.


        :param has_linked_accounts: The has_linked_accounts of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :type: bool
        """

        self._has_linked_accounts = has_linked_accounts

    @property
    def metadata(self):
        """Gets the metadata of this AccountsReceivableRetryConfigResponse.  # noqa: E501


        :return: The metadata of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AccountsReceivableRetryConfigResponse.


        :param metadata: The metadata of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def success(self):
        """Gets the success of this AccountsReceivableRetryConfigResponse.  # noqa: E501

        Indicates if API call was successful  # noqa: E501

        :return: The success of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this AccountsReceivableRetryConfigResponse.

        Indicates if API call was successful  # noqa: E501

        :param success: The success of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def warning(self):
        """Gets the warning of this AccountsReceivableRetryConfigResponse.  # noqa: E501


        :return: The warning of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :rtype: Warning
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this AccountsReceivableRetryConfigResponse.


        :param warning: The warning of this AccountsReceivableRetryConfigResponse.  # noqa: E501
        :type: Warning
        """

        self._warning = warning

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
        if issubclass(AccountsReceivableRetryConfigResponse, dict):
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
        if not isinstance(other, AccountsReceivableRetryConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other