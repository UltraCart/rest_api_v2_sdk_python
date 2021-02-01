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


class ScreenRecordingMultifield(object):
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
        'bd': 'float',
        'bool': 'bool',
        'json': 'str',
        'num': 'int',
        'text': 'str'
    }

    attribute_map = {
        'bd': 'bd',
        'bool': 'bool',
        'json': 'json',
        'num': 'num',
        'text': 'text'
    }

    def __init__(self, bd=None, bool=None, json=None, num=None, text=None):  # noqa: E501
        """ScreenRecordingMultifield - a model defined in Swagger"""  # noqa: E501

        self._bd = None
        self._bool = None
        self._json = None
        self._num = None
        self._text = None
        self.discriminator = None

        if bd is not None:
            self.bd = bd
        if bool is not None:
            self.bool = bool
        if json is not None:
            self.json = json
        if num is not None:
            self.num = num
        if text is not None:
            self.text = text

    @property
    def bd(self):
        """Gets the bd of this ScreenRecordingMultifield.  # noqa: E501


        :return: The bd of this ScreenRecordingMultifield.  # noqa: E501
        :rtype: float
        """
        return self._bd

    @bd.setter
    def bd(self, bd):
        """Sets the bd of this ScreenRecordingMultifield.


        :param bd: The bd of this ScreenRecordingMultifield.  # noqa: E501
        :type: float
        """

        self._bd = bd

    @property
    def bool(self):
        """Gets the bool of this ScreenRecordingMultifield.  # noqa: E501


        :return: The bool of this ScreenRecordingMultifield.  # noqa: E501
        :rtype: bool
        """
        return self._bool

    @bool.setter
    def bool(self, bool):
        """Sets the bool of this ScreenRecordingMultifield.


        :param bool: The bool of this ScreenRecordingMultifield.  # noqa: E501
        :type: bool
        """

        self._bool = bool

    @property
    def json(self):
        """Gets the json of this ScreenRecordingMultifield.  # noqa: E501


        :return: The json of this ScreenRecordingMultifield.  # noqa: E501
        :rtype: str
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this ScreenRecordingMultifield.


        :param json: The json of this ScreenRecordingMultifield.  # noqa: E501
        :type: str
        """

        self._json = json

    @property
    def num(self):
        """Gets the num of this ScreenRecordingMultifield.  # noqa: E501


        :return: The num of this ScreenRecordingMultifield.  # noqa: E501
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this ScreenRecordingMultifield.


        :param num: The num of this ScreenRecordingMultifield.  # noqa: E501
        :type: int
        """

        self._num = num

    @property
    def text(self):
        """Gets the text of this ScreenRecordingMultifield.  # noqa: E501


        :return: The text of this ScreenRecordingMultifield.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ScreenRecordingMultifield.


        :param text: The text of this ScreenRecordingMultifield.  # noqa: E501
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
        if issubclass(ScreenRecordingMultifield, dict):
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
        if not isinstance(other, ScreenRecordingMultifield):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
