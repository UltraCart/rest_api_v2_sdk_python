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


class TempMultimedia(object):
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
        'filename': 'str',
        'height': 'int',
        'multimedia_type': 'str',
        'size': 'int',
        'temp_multimedia_oid': 'int',
        'url': 'str',
        'width': 'int'
    }

    attribute_map = {
        'filename': 'filename',
        'height': 'height',
        'multimedia_type': 'multimedia_type',
        'size': 'size',
        'temp_multimedia_oid': 'temp_multimedia_oid',
        'url': 'url',
        'width': 'width'
    }

    def __init__(self, filename=None, height=None, multimedia_type=None, size=None, temp_multimedia_oid=None, url=None, width=None):  # noqa: E501
        """TempMultimedia - a model defined in Swagger"""  # noqa: E501

        self._filename = None
        self._height = None
        self._multimedia_type = None
        self._size = None
        self._temp_multimedia_oid = None
        self._url = None
        self._width = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if height is not None:
            self.height = height
        if multimedia_type is not None:
            self.multimedia_type = multimedia_type
        if size is not None:
            self.size = size
        if temp_multimedia_oid is not None:
            self.temp_multimedia_oid = temp_multimedia_oid
        if url is not None:
            self.url = url
        if width is not None:
            self.width = width

    @property
    def filename(self):
        """Gets the filename of this TempMultimedia.  # noqa: E501

        Filename  # noqa: E501

        :return: The filename of this TempMultimedia.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this TempMultimedia.

        Filename  # noqa: E501

        :param filename: The filename of this TempMultimedia.  # noqa: E501
        :type: str
        """
        if filename is not None and len(filename) > 75:
            raise ValueError("Invalid value for `filename`, length must be less than or equal to `75`")  # noqa: E501

        self._filename = filename

    @property
    def height(self):
        """Gets the height of this TempMultimedia.  # noqa: E501

        Height  # noqa: E501

        :return: The height of this TempMultimedia.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this TempMultimedia.

        Height  # noqa: E501

        :param height: The height of this TempMultimedia.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def multimedia_type(self):
        """Gets the multimedia_type of this TempMultimedia.  # noqa: E501

        Multimedia type  # noqa: E501

        :return: The multimedia_type of this TempMultimedia.  # noqa: E501
        :rtype: str
        """
        return self._multimedia_type

    @multimedia_type.setter
    def multimedia_type(self, multimedia_type):
        """Sets the multimedia_type of this TempMultimedia.

        Multimedia type  # noqa: E501

        :param multimedia_type: The multimedia_type of this TempMultimedia.  # noqa: E501
        :type: str
        """
        allowed_values = ["Image", "PDF", "Text", "Video"]  # noqa: E501
        if multimedia_type not in allowed_values:
            raise ValueError(
                "Invalid value for `multimedia_type` ({0}), must be one of {1}"  # noqa: E501
                .format(multimedia_type, allowed_values)
            )

        self._multimedia_type = multimedia_type

    @property
    def size(self):
        """Gets the size of this TempMultimedia.  # noqa: E501

        Size  # noqa: E501

        :return: The size of this TempMultimedia.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TempMultimedia.

        Size  # noqa: E501

        :param size: The size of this TempMultimedia.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def temp_multimedia_oid(self):
        """Gets the temp_multimedia_oid of this TempMultimedia.  # noqa: E501

        Temporary multimedia object identifier  # noqa: E501

        :return: The temp_multimedia_oid of this TempMultimedia.  # noqa: E501
        :rtype: int
        """
        return self._temp_multimedia_oid

    @temp_multimedia_oid.setter
    def temp_multimedia_oid(self, temp_multimedia_oid):
        """Sets the temp_multimedia_oid of this TempMultimedia.

        Temporary multimedia object identifier  # noqa: E501

        :param temp_multimedia_oid: The temp_multimedia_oid of this TempMultimedia.  # noqa: E501
        :type: int
        """

        self._temp_multimedia_oid = temp_multimedia_oid

    @property
    def url(self):
        """Gets the url of this TempMultimedia.  # noqa: E501

        URL  # noqa: E501

        :return: The url of this TempMultimedia.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TempMultimedia.

        URL  # noqa: E501

        :param url: The url of this TempMultimedia.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def width(self):
        """Gets the width of this TempMultimedia.  # noqa: E501

        Width  # noqa: E501

        :return: The width of this TempMultimedia.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this TempMultimedia.

        Width  # noqa: E501

        :param width: The width of this TempMultimedia.  # noqa: E501
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
        if issubclass(TempMultimedia, dict):
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
        if not isinstance(other, TempMultimedia):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other