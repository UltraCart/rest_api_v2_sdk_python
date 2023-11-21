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


class CouponTieredAmountOffItems(object):
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
        'item_tags': 'list[str]',
        'items': 'list[str]',
        'limit': 'float',
        'tiers': 'list[CouponTierQuantityAmount]'
    }

    attribute_map = {
        'item_tags': 'item_tags',
        'items': 'items',
        'limit': 'limit',
        'tiers': 'tiers'
    }

    def __init__(self, item_tags=None, items=None, limit=None, tiers=None):  # noqa: E501
        """CouponTieredAmountOffItems - a model defined in Swagger"""  # noqa: E501

        self._item_tags = None
        self._items = None
        self._limit = None
        self._tiers = None
        self.discriminator = None

        if item_tags is not None:
            self.item_tags = item_tags
        if items is not None:
            self.items = items
        if limit is not None:
            self.limit = limit
        if tiers is not None:
            self.tiers = tiers

    @property
    def item_tags(self):
        """Gets the item_tags of this CouponTieredAmountOffItems.  # noqa: E501

        An optional list of item tags which will receive a discount.  If blank, discount applies to all items except excluded items.  # noqa: E501

        :return: The item_tags of this CouponTieredAmountOffItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._item_tags

    @item_tags.setter
    def item_tags(self, item_tags):
        """Sets the item_tags of this CouponTieredAmountOffItems.

        An optional list of item tags which will receive a discount.  If blank, discount applies to all items except excluded items.  # noqa: E501

        :param item_tags: The item_tags of this CouponTieredAmountOffItems.  # noqa: E501
        :type: list[str]
        """

        self._item_tags = item_tags

    @property
    def items(self):
        """Gets the items of this CouponTieredAmountOffItems.  # noqa: E501

        The items being discounted by this coupon.  # noqa: E501

        :return: The items of this CouponTieredAmountOffItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CouponTieredAmountOffItems.

        The items being discounted by this coupon.  # noqa: E501

        :param items: The items of this CouponTieredAmountOffItems.  # noqa: E501
        :type: list[str]
        """

        self._items = items

    @property
    def limit(self):
        """Gets the limit of this CouponTieredAmountOffItems.  # noqa: E501

        The maximum number of discounted items.  # noqa: E501

        :return: The limit of this CouponTieredAmountOffItems.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CouponTieredAmountOffItems.

        The maximum number of discounted items.  # noqa: E501

        :param limit: The limit of this CouponTieredAmountOffItems.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def tiers(self):
        """Gets the tiers of this CouponTieredAmountOffItems.  # noqa: E501

        A list of discount tiers.  # noqa: E501

        :return: The tiers of this CouponTieredAmountOffItems.  # noqa: E501
        :rtype: list[CouponTierQuantityAmount]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this CouponTieredAmountOffItems.

        A list of discount tiers.  # noqa: E501

        :param tiers: The tiers of this CouponTieredAmountOffItems.  # noqa: E501
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
        if issubclass(CouponTieredAmountOffItems, dict):
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
        if not isinstance(other, CouponTieredAmountOffItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
