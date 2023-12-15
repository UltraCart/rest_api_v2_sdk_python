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


class OrderValidationResponse(object):
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
        'errors': 'list[str]',
        'messages': 'list[str]',
        'order_was_updated': 'bool'
    }

    attribute_map = {
        'errors': 'errors',
        'messages': 'messages',
        'order_was_updated': 'order_was_updated'
    }

    def __init__(self, errors=None, messages=None, order_was_updated=None):  # noqa: E501
        """OrderValidationResponse - a model defined in Swagger"""  # noqa: E501

        self._errors = None
        self._messages = None
        self._order_was_updated = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors
        if messages is not None:
            self.messages = messages
        if order_was_updated is not None:
            self.order_was_updated = order_was_updated

    @property
    def errors(self):
        """Gets the errors of this OrderValidationResponse.  # noqa: E501

        Errors to display to the merchant if they failed any of the validations checked  # noqa: E501

        :return: The errors of this OrderValidationResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this OrderValidationResponse.

        Errors to display to the merchant if they failed any of the validations checked  # noqa: E501

        :param errors: The errors of this OrderValidationResponse.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

    @property
    def messages(self):
        """Gets the messages of this OrderValidationResponse.  # noqa: E501

        Informational messages  # noqa: E501

        :return: The messages of this OrderValidationResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this OrderValidationResponse.

        Informational messages  # noqa: E501

        :param messages: The messages of this OrderValidationResponse.  # noqa: E501
        :type: list[str]
        """

        self._messages = messages

    @property
    def order_was_updated(self):
        """Gets the order_was_updated of this OrderValidationResponse.  # noqa: E501

        If true, this order was updated during the validation call.  This may happen during address standardization fixes.  # noqa: E501

        :return: The order_was_updated of this OrderValidationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._order_was_updated

    @order_was_updated.setter
    def order_was_updated(self, order_was_updated):
        """Sets the order_was_updated of this OrderValidationResponse.

        If true, this order was updated during the validation call.  This may happen during address standardization fixes.  # noqa: E501

        :param order_was_updated: The order_was_updated of this OrderValidationResponse.  # noqa: E501
        :type: bool
        """

        self._order_was_updated = order_was_updated

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
        if issubclass(OrderValidationResponse, dict):
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
        if not isinstance(other, OrderValidationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
