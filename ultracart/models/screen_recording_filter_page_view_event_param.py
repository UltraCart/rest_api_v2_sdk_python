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


class ScreenRecordingFilterPageViewEventParam(object):
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
        'name': 'str',
        'value_bd': 'ScreenRecordingFilterRangeBigDecimal',
        'value_bool': 'bool',
        'value_num': 'ScreenRecordingFilterRangeInteger',
        'value_text': 'ScreenRecordingFilterStringSearch'
    }

    attribute_map = {
        'name': 'name',
        'value_bd': 'value_bd',
        'value_bool': 'value_bool',
        'value_num': 'value_num',
        'value_text': 'value_text'
    }

    def __init__(self, name=None, value_bd=None, value_bool=None, value_num=None, value_text=None):  # noqa: E501
        """ScreenRecordingFilterPageViewEventParam - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._value_bd = None
        self._value_bool = None
        self._value_num = None
        self._value_text = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value_bd is not None:
            self.value_bd = value_bd
        if value_bool is not None:
            self.value_bool = value_bool
        if value_num is not None:
            self.value_num = value_num
        if value_text is not None:
            self.value_text = value_text

    @property
    def name(self):
        """Gets the name of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501


        :return: The name of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScreenRecordingFilterPageViewEventParam.


        :param name: The name of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value_bd(self):
        """Gets the value_bd of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501


        :return: The value_bd of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501
        :rtype: ScreenRecordingFilterRangeBigDecimal
        """
        return self._value_bd

    @value_bd.setter
    def value_bd(self, value_bd):
        """Sets the value_bd of this ScreenRecordingFilterPageViewEventParam.


        :param value_bd: The value_bd of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501
        :type: ScreenRecordingFilterRangeBigDecimal
        """

        self._value_bd = value_bd

    @property
    def value_bool(self):
        """Gets the value_bool of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501


        :return: The value_bool of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501
        :rtype: bool
        """
        return self._value_bool

    @value_bool.setter
    def value_bool(self, value_bool):
        """Sets the value_bool of this ScreenRecordingFilterPageViewEventParam.


        :param value_bool: The value_bool of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501
        :type: bool
        """

        self._value_bool = value_bool

    @property
    def value_num(self):
        """Gets the value_num of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501


        :return: The value_num of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501
        :rtype: ScreenRecordingFilterRangeInteger
        """
        return self._value_num

    @value_num.setter
    def value_num(self, value_num):
        """Sets the value_num of this ScreenRecordingFilterPageViewEventParam.


        :param value_num: The value_num of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501
        :type: ScreenRecordingFilterRangeInteger
        """

        self._value_num = value_num

    @property
    def value_text(self):
        """Gets the value_text of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501


        :return: The value_text of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501
        :rtype: ScreenRecordingFilterStringSearch
        """
        return self._value_text

    @value_text.setter
    def value_text(self, value_text):
        """Sets the value_text of this ScreenRecordingFilterPageViewEventParam.


        :param value_text: The value_text of this ScreenRecordingFilterPageViewEventParam.  # noqa: E501
        :type: ScreenRecordingFilterStringSearch
        """

        self._value_text = value_text

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
        if issubclass(ScreenRecordingFilterPageViewEventParam, dict):
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
        if not isinstance(other, ScreenRecordingFilterPageViewEventParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
