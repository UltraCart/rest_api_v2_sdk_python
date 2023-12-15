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


class CartProperty(object):
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
        'display': 'bool',
        'expiration_dts': 'str',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'display': 'display',
        'expiration_dts': 'expiration_dts',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, display=None, expiration_dts=None, name=None, value=None):  # noqa: E501
        """CartProperty - a model defined in Swagger"""  # noqa: E501

        self._display = None
        self._expiration_dts = None
        self._name = None
        self._value = None
        self.discriminator = None

        if display is not None:
            self.display = display
        if expiration_dts is not None:
            self.expiration_dts = expiration_dts
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def display(self):
        """Gets the display of this CartProperty.  # noqa: E501

        True if this property is displayed to the customer  # noqa: E501

        :return: The display of this CartProperty.  # noqa: E501
        :rtype: bool
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this CartProperty.

        True if this property is displayed to the customer  # noqa: E501

        :param display: The display of this CartProperty.  # noqa: E501
        :type: bool
        """

        self._display = display

    @property
    def expiration_dts(self):
        """Gets the expiration_dts of this CartProperty.  # noqa: E501

        The date/time that the property expires and is deleted  # noqa: E501

        :return: The expiration_dts of this CartProperty.  # noqa: E501
        :rtype: str
        """
        return self._expiration_dts

    @expiration_dts.setter
    def expiration_dts(self, expiration_dts):
        """Sets the expiration_dts of this CartProperty.

        The date/time that the property expires and is deleted  # noqa: E501

        :param expiration_dts: The expiration_dts of this CartProperty.  # noqa: E501
        :type: str
        """

        self._expiration_dts = expiration_dts

    @property
    def name(self):
        """Gets the name of this CartProperty.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this CartProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CartProperty.

        Name  # noqa: E501

        :param name: The name of this CartProperty.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this CartProperty.  # noqa: E501

        Value  # noqa: E501

        :return: The value of this CartProperty.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CartProperty.

        Value  # noqa: E501

        :param value: The value of this CartProperty.  # noqa: E501
        :type: str
        """
        if value is not None and len(value) > 3800:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `3800`")  # noqa: E501

        self._value = value

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
        if issubclass(CartProperty, dict):
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
        if not isinstance(other, CartProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
