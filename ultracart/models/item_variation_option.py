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


class ItemVariationOption(object):
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
        'default_option': 'bool',
        'merchant_item_multimedia_oid': 'int',
        'translated_text_instance_oid': 'int',
        'value': 'str'
    }

    attribute_map = {
        'default_option': 'default_option',
        'merchant_item_multimedia_oid': 'merchant_item_multimedia_oid',
        'translated_text_instance_oid': 'translated_text_instance_oid',
        'value': 'value'
    }

    def __init__(self, default_option=None, merchant_item_multimedia_oid=None, translated_text_instance_oid=None, value=None):  # noqa: E501
        """ItemVariationOption - a model defined in Swagger"""  # noqa: E501

        self._default_option = None
        self._merchant_item_multimedia_oid = None
        self._translated_text_instance_oid = None
        self._value = None
        self.discriminator = None

        if default_option is not None:
            self.default_option = default_option
        if merchant_item_multimedia_oid is not None:
            self.merchant_item_multimedia_oid = merchant_item_multimedia_oid
        if translated_text_instance_oid is not None:
            self.translated_text_instance_oid = translated_text_instance_oid
        if value is not None:
            self.value = value

    @property
    def default_option(self):
        """Gets the default_option of this ItemVariationOption.  # noqa: E501

        True if default option  # noqa: E501

        :return: The default_option of this ItemVariationOption.  # noqa: E501
        :rtype: bool
        """
        return self._default_option

    @default_option.setter
    def default_option(self, default_option):
        """Sets the default_option of this ItemVariationOption.

        True if default option  # noqa: E501

        :param default_option: The default_option of this ItemVariationOption.  # noqa: E501
        :type: bool
        """

        self._default_option = default_option

    @property
    def merchant_item_multimedia_oid(self):
        """Gets the merchant_item_multimedia_oid of this ItemVariationOption.  # noqa: E501

        Multimedia object identifier  # noqa: E501

        :return: The merchant_item_multimedia_oid of this ItemVariationOption.  # noqa: E501
        :rtype: int
        """
        return self._merchant_item_multimedia_oid

    @merchant_item_multimedia_oid.setter
    def merchant_item_multimedia_oid(self, merchant_item_multimedia_oid):
        """Sets the merchant_item_multimedia_oid of this ItemVariationOption.

        Multimedia object identifier  # noqa: E501

        :param merchant_item_multimedia_oid: The merchant_item_multimedia_oid of this ItemVariationOption.  # noqa: E501
        :type: int
        """

        self._merchant_item_multimedia_oid = merchant_item_multimedia_oid

    @property
    def translated_text_instance_oid(self):
        """Gets the translated_text_instance_oid of this ItemVariationOption.  # noqa: E501

        Translated text instance id  # noqa: E501

        :return: The translated_text_instance_oid of this ItemVariationOption.  # noqa: E501
        :rtype: int
        """
        return self._translated_text_instance_oid

    @translated_text_instance_oid.setter
    def translated_text_instance_oid(self, translated_text_instance_oid):
        """Sets the translated_text_instance_oid of this ItemVariationOption.

        Translated text instance id  # noqa: E501

        :param translated_text_instance_oid: The translated_text_instance_oid of this ItemVariationOption.  # noqa: E501
        :type: int
        """

        self._translated_text_instance_oid = translated_text_instance_oid

    @property
    def value(self):
        """Gets the value of this ItemVariationOption.  # noqa: E501

        Value  # noqa: E501

        :return: The value of this ItemVariationOption.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ItemVariationOption.

        Value  # noqa: E501

        :param value: The value of this ItemVariationOption.  # noqa: E501
        :type: str
        """
        if value is not None and len(value) > 50:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `50`")  # noqa: E501

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
        if issubclass(ItemVariationOption, dict):
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
        if not isinstance(other, ItemVariationOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other