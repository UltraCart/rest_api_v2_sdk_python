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


class CouponTieredAmountOffItem(object):
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
        'item': 'str',
        'limit': 'float',
        'tiers': 'list[CouponTierQuantityAmount]'
    }

    attribute_map = {
        'item': 'item',
        'limit': 'limit',
        'tiers': 'tiers'
    }

    def __init__(self, item=None, limit=None, tiers=None):  # noqa: E501
        """CouponTieredAmountOffItem - a model defined in Swagger"""  # noqa: E501

        self._item = None
        self._limit = None
        self._tiers = None
        self.discriminator = None

        if item is not None:
            self.item = item
        if limit is not None:
            self.limit = limit
        if tiers is not None:
            self.tiers = tiers

    @property
    def item(self):
        """Gets the item of this CouponTieredAmountOffItem.  # noqa: E501

        The item being discounted by this coupon.  # noqa: E501

        :return: The item of this CouponTieredAmountOffItem.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this CouponTieredAmountOffItem.

        The item being discounted by this coupon.  # noqa: E501

        :param item: The item of this CouponTieredAmountOffItem.  # noqa: E501
        :type: str
        """

        self._item = item

    @property
    def limit(self):
        """Gets the limit of this CouponTieredAmountOffItem.  # noqa: E501

        The maximum amount of total discount by this coupon.  # noqa: E501

        :return: The limit of this CouponTieredAmountOffItem.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CouponTieredAmountOffItem.

        The maximum amount of total discount by this coupon.  # noqa: E501

        :param limit: The limit of this CouponTieredAmountOffItem.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def tiers(self):
        """Gets the tiers of this CouponTieredAmountOffItem.  # noqa: E501

        A list of discount tiers.  # noqa: E501

        :return: The tiers of this CouponTieredAmountOffItem.  # noqa: E501
        :rtype: list[CouponTierQuantityAmount]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this CouponTieredAmountOffItem.

        A list of discount tiers.  # noqa: E501

        :param tiers: The tiers of this CouponTieredAmountOffItem.  # noqa: E501
        :type: list[CouponTierQuantityAmount]
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
        if issubclass(CouponTieredAmountOffItem, dict):
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
        if not isinstance(other, CouponTieredAmountOffItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
