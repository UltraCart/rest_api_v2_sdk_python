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


class CouponTierQuantityAmount(object):
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
        'discount_amount': 'float',
        'item_quantity': 'int'
    }

    attribute_map = {
        'discount_amount': 'discount_amount',
        'item_quantity': 'item_quantity'
    }

    def __init__(self, discount_amount=None, item_quantity=None):  # noqa: E501
        """CouponTierQuantityAmount - a model defined in Swagger"""  # noqa: E501

        self._discount_amount = None
        self._item_quantity = None
        self.discriminator = None

        if discount_amount is not None:
            self.discount_amount = discount_amount
        if item_quantity is not None:
            self.item_quantity = item_quantity

    @property
    def discount_amount(self):
        """Gets the discount_amount of this CouponTierQuantityAmount.  # noqa: E501

        The amount of discount per item.  # noqa: E501

        :return: The discount_amount of this CouponTierQuantityAmount.  # noqa: E501
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this CouponTierQuantityAmount.

        The amount of discount per item.  # noqa: E501

        :param discount_amount: The discount_amount of this CouponTierQuantityAmount.  # noqa: E501
        :type: float
        """

        self._discount_amount = discount_amount

    @property
    def item_quantity(self):
        """Gets the item_quantity of this CouponTierQuantityAmount.  # noqa: E501

        The quantity of item purchased (in units)  # noqa: E501

        :return: The item_quantity of this CouponTierQuantityAmount.  # noqa: E501
        :rtype: int
        """
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, item_quantity):
        """Sets the item_quantity of this CouponTierQuantityAmount.

        The quantity of item purchased (in units)  # noqa: E501

        :param item_quantity: The item_quantity of this CouponTierQuantityAmount.  # noqa: E501
        :type: int
        """

        self._item_quantity = item_quantity

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
        if issubclass(CouponTierQuantityAmount, dict):
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
        if not isinstance(other, CouponTierQuantityAmount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
