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


class CartItemMultimediaThumbnail(object):
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
        'height': 'int',
        'png': 'bool',
        'square': 'bool',
        'url': 'str',
        'width': 'int'
    }

    attribute_map = {
        'height': 'height',
        'png': 'png',
        'square': 'square',
        'url': 'url',
        'width': 'width'
    }

    def __init__(self, height=None, png=None, square=None, url=None, width=None):  # noqa: E501
        """CartItemMultimediaThumbnail - a model defined in Swagger"""  # noqa: E501

        self._height = None
        self._png = None
        self._square = None
        self._url = None
        self._width = None
        self.discriminator = None

        if height is not None:
            self.height = height
        if png is not None:
            self.png = png
        if square is not None:
            self.square = square
        if url is not None:
            self.url = url
        if width is not None:
            self.width = width

    @property
    def height(self):
        """Gets the height of this CartItemMultimediaThumbnail.  # noqa: E501

        Height in pixels  # noqa: E501

        :return: The height of this CartItemMultimediaThumbnail.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CartItemMultimediaThumbnail.

        Height in pixels  # noqa: E501

        :param height: The height of this CartItemMultimediaThumbnail.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def png(self):
        """Gets the png of this CartItemMultimediaThumbnail.  # noqa: E501

        True if thumbnail is a PNG, otherwise its a JPEG  # noqa: E501

        :return: The png of this CartItemMultimediaThumbnail.  # noqa: E501
        :rtype: bool
        """
        return self._png

    @png.setter
    def png(self, png):
        """Sets the png of this CartItemMultimediaThumbnail.

        True if thumbnail is a PNG, otherwise its a JPEG  # noqa: E501

        :param png: The png of this CartItemMultimediaThumbnail.  # noqa: E501
        :type: bool
        """

        self._png = png

    @property
    def square(self):
        """Gets the square of this CartItemMultimediaThumbnail.  # noqa: E501

        True if the thumbnail is square  # noqa: E501

        :return: The square of this CartItemMultimediaThumbnail.  # noqa: E501
        :rtype: bool
        """
        return self._square

    @square.setter
    def square(self, square):
        """Sets the square of this CartItemMultimediaThumbnail.

        True if the thumbnail is square  # noqa: E501

        :param square: The square of this CartItemMultimediaThumbnail.  # noqa: E501
        :type: bool
        """

        self._square = square

    @property
    def url(self):
        """Gets the url of this CartItemMultimediaThumbnail.  # noqa: E501

        URL for the thumbnail  # noqa: E501

        :return: The url of this CartItemMultimediaThumbnail.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CartItemMultimediaThumbnail.

        URL for the thumbnail  # noqa: E501

        :param url: The url of this CartItemMultimediaThumbnail.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def width(self):
        """Gets the width of this CartItemMultimediaThumbnail.  # noqa: E501

        Width in pixels  # noqa: E501

        :return: The width of this CartItemMultimediaThumbnail.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this CartItemMultimediaThumbnail.

        Width in pixels  # noqa: E501

        :param width: The width of this CartItemMultimediaThumbnail.  # noqa: E501
        :type: int
        """

        self._width = width

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
        if issubclass(CartItemMultimediaThumbnail, dict):
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
        if not isinstance(other, CartItemMultimediaThumbnail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
