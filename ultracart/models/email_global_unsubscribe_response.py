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


class EmailGlobalUnsubscribeResponse(object):
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
        'lists_unsubscribed': 'int'
    }

    attribute_map = {
        'lists_unsubscribed': 'listsUnsubscribed'
    }

    def __init__(self, lists_unsubscribed=None):  # noqa: E501
        """EmailGlobalUnsubscribeResponse - a model defined in Swagger"""  # noqa: E501

        self._lists_unsubscribed = None
        self.discriminator = None

        if lists_unsubscribed is not None:
            self.lists_unsubscribed = lists_unsubscribed

    @property
    def lists_unsubscribed(self):
        """Gets the lists_unsubscribed of this EmailGlobalUnsubscribeResponse.  # noqa: E501


        :return: The lists_unsubscribed of this EmailGlobalUnsubscribeResponse.  # noqa: E501
        :rtype: int
        """
        return self._lists_unsubscribed

    @lists_unsubscribed.setter
    def lists_unsubscribed(self, lists_unsubscribed):
        """Sets the lists_unsubscribed of this EmailGlobalUnsubscribeResponse.


        :param lists_unsubscribed: The lists_unsubscribed of this EmailGlobalUnsubscribeResponse.  # noqa: E501
        :type: int
        """

        self._lists_unsubscribed = lists_unsubscribed

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
        if issubclass(EmailGlobalUnsubscribeResponse, dict):
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
        if not isinstance(other, EmailGlobalUnsubscribeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
