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


class ChannelPartnerOrderTransaction(object):
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
        'details': 'list[ChannelPartnerOrderTransactionDetail]',
        'successful': 'bool'
    }

    attribute_map = {
        'details': 'details',
        'successful': 'successful'
    }

    def __init__(self, details=None, successful=None):  # noqa: E501
        """ChannelPartnerOrderTransaction - a model defined in Swagger"""  # noqa: E501

        self._details = None
        self._successful = None
        self.discriminator = None

        if details is not None:
            self.details = details
        if successful is not None:
            self.successful = successful

    @property
    def details(self):
        """Gets the details of this ChannelPartnerOrderTransaction.  # noqa: E501

        Transaction gateway details  # noqa: E501

        :return: The details of this ChannelPartnerOrderTransaction.  # noqa: E501
        :rtype: list[ChannelPartnerOrderTransactionDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ChannelPartnerOrderTransaction.

        Transaction gateway details  # noqa: E501

        :param details: The details of this ChannelPartnerOrderTransaction.  # noqa: E501
        :type: list[ChannelPartnerOrderTransactionDetail]
        """

        self._details = details

    @property
    def successful(self):
        """Gets the successful of this ChannelPartnerOrderTransaction.  # noqa: E501

        True if the transaction was successfully charged  # noqa: E501

        :return: The successful of this ChannelPartnerOrderTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this ChannelPartnerOrderTransaction.

        True if the transaction was successfully charged  # noqa: E501

        :param successful: The successful of this ChannelPartnerOrderTransaction.  # noqa: E501
        :type: bool
        """

        self._successful = successful

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
        if issubclass(ChannelPartnerOrderTransaction, dict):
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
        if not isinstance(other, ChannelPartnerOrderTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other