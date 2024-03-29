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


class CouponPercentOffItemsAndFreeShipping(object):
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
        'discount_percent': 'float',
        'excluded_item_tags': 'list[str]',
        'excluded_items': 'list[str]',
        'item_tags': 'list[str]',
        'items': 'list[str]'
    }

    attribute_map = {
        'discount_percent': 'discount_percent',
        'excluded_item_tags': 'excluded_item_tags',
        'excluded_items': 'excluded_items',
        'item_tags': 'item_tags',
        'items': 'items'
    }

    def __init__(self, discount_percent=None, excluded_item_tags=None, excluded_items=None, item_tags=None, items=None):  # noqa: E501
        """CouponPercentOffItemsAndFreeShipping - a model defined in Swagger"""  # noqa: E501

        self._discount_percent = None
        self._excluded_item_tags = None
        self._excluded_items = None
        self._item_tags = None
        self._items = None
        self.discriminator = None

        if discount_percent is not None:
            self.discount_percent = discount_percent
        if excluded_item_tags is not None:
            self.excluded_item_tags = excluded_item_tags
        if excluded_items is not None:
            self.excluded_items = excluded_items
        if item_tags is not None:
            self.item_tags = item_tags
        if items is not None:
            self.items = items

    @property
    def discount_percent(self):
        """Gets the discount_percent of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501

        The percentage of subtotal discount  # noqa: E501

        :return: The discount_percent of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501
        :rtype: float
        """
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, discount_percent):
        """Sets the discount_percent of this CouponPercentOffItemsAndFreeShipping.

        The percentage of subtotal discount  # noqa: E501

        :param discount_percent: The discount_percent of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501
        :type: float
        """

        self._discount_percent = discount_percent

    @property
    def excluded_item_tags(self):
        """Gets the excluded_item_tags of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501

        A list of item tags which cannot be discounted.  # noqa: E501

        :return: The excluded_item_tags of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501
        :rtype: list[str]
        """
        return self._excluded_item_tags

    @excluded_item_tags.setter
    def excluded_item_tags(self, excluded_item_tags):
        """Sets the excluded_item_tags of this CouponPercentOffItemsAndFreeShipping.

        A list of item tags which cannot be discounted.  # noqa: E501

        :param excluded_item_tags: The excluded_item_tags of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501
        :type: list[str]
        """

        self._excluded_item_tags = excluded_item_tags

    @property
    def excluded_items(self):
        """Gets the excluded_items of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501

        A list of items which cannot be discounted.  # noqa: E501

        :return: The excluded_items of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501
        :rtype: list[str]
        """
        return self._excluded_items

    @excluded_items.setter
    def excluded_items(self, excluded_items):
        """Sets the excluded_items of this CouponPercentOffItemsAndFreeShipping.

        A list of items which cannot be discounted.  # noqa: E501

        :param excluded_items: The excluded_items of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501
        :type: list[str]
        """

        self._excluded_items = excluded_items

    @property
    def item_tags(self):
        """Gets the item_tags of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501

        An optional list of item tags which will receive a discount.  If blank, discount applies to all items except excluded items.  # noqa: E501

        :return: The item_tags of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501
        :rtype: list[str]
        """
        return self._item_tags

    @item_tags.setter
    def item_tags(self, item_tags):
        """Sets the item_tags of this CouponPercentOffItemsAndFreeShipping.

        An optional list of item tags which will receive a discount.  If blank, discount applies to all items except excluded items.  # noqa: E501

        :param item_tags: The item_tags of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501
        :type: list[str]
        """

        self._item_tags = item_tags

    @property
    def items(self):
        """Gets the items of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501

        An optional list of items which will receive a discount.  If blank, discount applies to all items except excluded items.  # noqa: E501

        :return: The items of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CouponPercentOffItemsAndFreeShipping.

        An optional list of items which will receive a discount.  If blank, discount applies to all items except excluded items.  # noqa: E501

        :param items: The items of this CouponPercentOffItemsAndFreeShipping.  # noqa: E501
        :type: list[str]
        """

        self._items = items

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
        if issubclass(CouponPercentOffItemsAndFreeShipping, dict):
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
        if not isinstance(other, CouponPercentOffItemsAndFreeShipping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
