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


class CouponTieredAmountOffSubtotal(object):
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
        'items': 'list[str]',
        'tiers': 'list[CouponTierAmount]'
    }

    attribute_map = {
        'items': 'items',
        'tiers': 'tiers'
    }

    def __init__(self, items=None, tiers=None):  # noqa: E501
        """CouponTieredAmountOffSubtotal - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._tiers = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if tiers is not None:
            self.tiers = tiers

    @property
    def items(self):
        """Gets the items of this CouponTieredAmountOffSubtotal.  # noqa: E501

        An optional list of items of which a quantity of one or many must be purchased for coupon to be valid.  If empty, all items apply toward subtotal amount.  # noqa: E501

        :return: The items of this CouponTieredAmountOffSubtotal.  # noqa: E501
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CouponTieredAmountOffSubtotal.

        An optional list of items of which a quantity of one or many must be purchased for coupon to be valid.  If empty, all items apply toward subtotal amount.  # noqa: E501

        :param items: The items of this CouponTieredAmountOffSubtotal.  # noqa: E501
        :type: list[str]
        """

        self._items = items

    @property
    def tiers(self):
        """Gets the tiers of this CouponTieredAmountOffSubtotal.  # noqa: E501

        A list of discount tiers.  # noqa: E501

        :return: The tiers of this CouponTieredAmountOffSubtotal.  # noqa: E501
        :rtype: list[CouponTierAmount]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this CouponTieredAmountOffSubtotal.

        A list of discount tiers.  # noqa: E501

        :param tiers: The tiers of this CouponTieredAmountOffSubtotal.  # noqa: E501
        :type: list[CouponTierAmount]
        """

        self._tiers = tiers

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
        if issubclass(CouponTieredAmountOffSubtotal, dict):
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
        if not isinstance(other, CouponTieredAmountOffSubtotal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
