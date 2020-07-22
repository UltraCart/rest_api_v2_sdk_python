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


class ItemContentAttribute(object):
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
        'translated_text_instance_oid': 'int',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'translated_text_instance_oid': 'translated_text_instance_oid',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, name=None, translated_text_instance_oid=None, type=None, value=None):  # noqa: E501
        """ItemContentAttribute - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._translated_text_instance_oid = None
        self._type = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if translated_text_instance_oid is not None:
            self.translated_text_instance_oid = translated_text_instance_oid
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this ItemContentAttribute.  # noqa: E501

        Attribute name  # noqa: E501

        :return: The name of this ItemContentAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemContentAttribute.

        Attribute name  # noqa: E501

        :param name: The name of this ItemContentAttribute.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 400:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `400`")  # noqa: E501

        self._name = name

    @property
    def translated_text_instance_oid(self):
        """Gets the translated_text_instance_oid of this ItemContentAttribute.  # noqa: E501

        Attribute translated text instance identifier  # noqa: E501

        :return: The translated_text_instance_oid of this ItemContentAttribute.  # noqa: E501
        :rtype: int
        """
        return self._translated_text_instance_oid

    @translated_text_instance_oid.setter
    def translated_text_instance_oid(self, translated_text_instance_oid):
        """Sets the translated_text_instance_oid of this ItemContentAttribute.

        Attribute translated text instance identifier  # noqa: E501

        :param translated_text_instance_oid: The translated_text_instance_oid of this ItemContentAttribute.  # noqa: E501
        :type: int
        """

        self._translated_text_instance_oid = translated_text_instance_oid

    @property
    def type(self):
        """Gets the type of this ItemContentAttribute.  # noqa: E501

        Attribute type  # noqa: E501

        :return: The type of this ItemContentAttribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ItemContentAttribute.

        Attribute type  # noqa: E501

        :param type: The type of this ItemContentAttribute.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this ItemContentAttribute.  # noqa: E501

        Attribute value  # noqa: E501

        :return: The value of this ItemContentAttribute.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ItemContentAttribute.

        Attribute value  # noqa: E501

        :param value: The value of this ItemContentAttribute.  # noqa: E501
        :type: str
        """
        if value is not None and len(value) > 100000:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `100000`")  # noqa: E501

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
        if issubclass(ItemContentAttribute, dict):
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
        if not isinstance(other, ItemContentAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
