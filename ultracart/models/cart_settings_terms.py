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


class CartSettingsTerms(object):
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
        'html': 'str',
        'text': 'str'
    }

    attribute_map = {
        'html': 'html',
        'text': 'text'
    }

    def __init__(self, html=None, text=None):  # noqa: E501
        """CartSettingsTerms - a model defined in Swagger"""  # noqa: E501

        self._html = None
        self._text = None
        self.discriminator = None

        if html is not None:
            self.html = html
        if text is not None:
            self.text = text

    @property
    def html(self):
        """Gets the html of this CartSettingsTerms.  # noqa: E501

        HTML version of the terms  # noqa: E501

        :return: The html of this CartSettingsTerms.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this CartSettingsTerms.

        HTML version of the terms  # noqa: E501

        :param html: The html of this CartSettingsTerms.  # noqa: E501
        :type: str
        """

        self._html = html

    @property
    def text(self):
        """Gets the text of this CartSettingsTerms.  # noqa: E501

        Text version of the terms.  # noqa: E501

        :return: The text of this CartSettingsTerms.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CartSettingsTerms.

        Text version of the terms.  # noqa: E501

        :param text: The text of this CartSettingsTerms.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(CartSettingsTerms, dict):
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
        if not isinstance(other, CartSettingsTerms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
