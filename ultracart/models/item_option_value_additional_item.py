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


class ItemOptionValueAdditionalItem(object):
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
        'additional_merchant_item_id': 'str',
        'additional_merchant_item_oid': 'int'
    }

    attribute_map = {
        'additional_merchant_item_id': 'additional_merchant_item_id',
        'additional_merchant_item_oid': 'additional_merchant_item_oid'
    }

    def __init__(self, additional_merchant_item_id=None, additional_merchant_item_oid=None):  # noqa: E501
        """ItemOptionValueAdditionalItem - a model defined in Swagger"""  # noqa: E501

        self._additional_merchant_item_id = None
        self._additional_merchant_item_oid = None
        self.discriminator = None

        if additional_merchant_item_id is not None:
            self.additional_merchant_item_id = additional_merchant_item_id
        if additional_merchant_item_oid is not None:
            self.additional_merchant_item_oid = additional_merchant_item_oid

    @property
    def additional_merchant_item_id(self):
        """Gets the additional_merchant_item_id of this ItemOptionValueAdditionalItem.  # noqa: E501

        Additional item id  # noqa: E501

        :return: The additional_merchant_item_id of this ItemOptionValueAdditionalItem.  # noqa: E501
        :rtype: str
        """
        return self._additional_merchant_item_id

    @additional_merchant_item_id.setter
    def additional_merchant_item_id(self, additional_merchant_item_id):
        """Sets the additional_merchant_item_id of this ItemOptionValueAdditionalItem.

        Additional item id  # noqa: E501

        :param additional_merchant_item_id: The additional_merchant_item_id of this ItemOptionValueAdditionalItem.  # noqa: E501
        :type: str
        """

        self._additional_merchant_item_id = additional_merchant_item_id

    @property
    def additional_merchant_item_oid(self):
        """Gets the additional_merchant_item_oid of this ItemOptionValueAdditionalItem.  # noqa: E501

        Additional item object identifier  # noqa: E501

        :return: The additional_merchant_item_oid of this ItemOptionValueAdditionalItem.  # noqa: E501
        :rtype: int
        """
        return self._additional_merchant_item_oid

    @additional_merchant_item_oid.setter
    def additional_merchant_item_oid(self, additional_merchant_item_oid):
        """Sets the additional_merchant_item_oid of this ItemOptionValueAdditionalItem.

        Additional item object identifier  # noqa: E501

        :param additional_merchant_item_oid: The additional_merchant_item_oid of this ItemOptionValueAdditionalItem.  # noqa: E501
        :type: int
        """

        self._additional_merchant_item_oid = additional_merchant_item_oid

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
        if issubclass(ItemOptionValueAdditionalItem, dict):
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
        if not isinstance(other, ItemOptionValueAdditionalItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other