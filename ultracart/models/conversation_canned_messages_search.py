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


class ConversationCannedMessagesSearch(object):
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
        'max_results': 'int',
        'short_code': 'str'
    }

    attribute_map = {
        'max_results': 'max_results',
        'short_code': 'short_code'
    }

    def __init__(self, max_results=None, short_code=None):  # noqa: E501
        """ConversationCannedMessagesSearch - a model defined in Swagger"""  # noqa: E501

        self._max_results = None
        self._short_code = None
        self.discriminator = None

        if max_results is not None:
            self.max_results = max_results
        if short_code is not None:
            self.short_code = short_code

    @property
    def max_results(self):
        """Gets the max_results of this ConversationCannedMessagesSearch.  # noqa: E501


        :return: The max_results of this ConversationCannedMessagesSearch.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this ConversationCannedMessagesSearch.


        :param max_results: The max_results of this ConversationCannedMessagesSearch.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def short_code(self):
        """Gets the short_code of this ConversationCannedMessagesSearch.  # noqa: E501


        :return: The short_code of this ConversationCannedMessagesSearch.  # noqa: E501
        :rtype: str
        """
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        """Sets the short_code of this ConversationCannedMessagesSearch.


        :param short_code: The short_code of this ConversationCannedMessagesSearch.  # noqa: E501
        :type: str
        """

        self._short_code = short_code

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
        if issubclass(ConversationCannedMessagesSearch, dict):
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
        if not isinstance(other, ConversationCannedMessagesSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
