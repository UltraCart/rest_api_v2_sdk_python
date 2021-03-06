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


class CartSettingsGiftWrap(object):
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
        'cost': 'Currency',
        'title': 'str',
        'url': 'str'
    }

    attribute_map = {
        'cost': 'cost',
        'title': 'title',
        'url': 'url'
    }

    def __init__(self, cost=None, title=None, url=None):  # noqa: E501
        """CartSettingsGiftWrap - a model defined in Swagger"""  # noqa: E501

        self._cost = None
        self._title = None
        self._url = None
        self.discriminator = None

        if cost is not None:
            self.cost = cost
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url

    @property
    def cost(self):
        """Gets the cost of this CartSettingsGiftWrap.  # noqa: E501


        :return: The cost of this CartSettingsGiftWrap.  # noqa: E501
        :rtype: Currency
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this CartSettingsGiftWrap.


        :param cost: The cost of this CartSettingsGiftWrap.  # noqa: E501
        :type: Currency
        """

        self._cost = cost

    @property
    def title(self):
        """Gets the title of this CartSettingsGiftWrap.  # noqa: E501

        Title of the gift wrap  # noqa: E501

        :return: The title of this CartSettingsGiftWrap.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CartSettingsGiftWrap.

        Title of the gift wrap  # noqa: E501

        :param title: The title of this CartSettingsGiftWrap.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def url(self):
        """Gets the url of this CartSettingsGiftWrap.  # noqa: E501

        URL for the sample of the gift wrap  # noqa: E501

        :return: The url of this CartSettingsGiftWrap.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CartSettingsGiftWrap.

        URL for the sample of the gift wrap  # noqa: E501

        :param url: The url of this CartSettingsGiftWrap.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(CartSettingsGiftWrap, dict):
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
        if not isinstance(other, CartSettingsGiftWrap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
