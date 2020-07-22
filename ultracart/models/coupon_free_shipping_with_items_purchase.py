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


class CouponFreeShippingWithItemsPurchase(object):
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
        'shipping_methods': 'list[str]'
    }

    attribute_map = {
        'items': 'items',
        'shipping_methods': 'shipping_methods'
    }

    def __init__(self, items=None, shipping_methods=None):  # noqa: E501
        """CouponFreeShippingWithItemsPurchase - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._shipping_methods = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if shipping_methods is not None:
            self.shipping_methods = shipping_methods

    @property
    def items(self):
        """Gets the items of this CouponFreeShippingWithItemsPurchase.  # noqa: E501

        A list of items of which at least one must be purchased for coupon to be valid.  # noqa: E501

        :return: The items of this CouponFreeShippingWithItemsPurchase.  # noqa: E501
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CouponFreeShippingWithItemsPurchase.

        A list of items of which at least one must be purchased for coupon to be valid.  # noqa: E501

        :param items: The items of this CouponFreeShippingWithItemsPurchase.  # noqa: E501
        :type: list[str]
        """

        self._items = items

    @property
    def shipping_methods(self):
        """Gets the shipping_methods of this CouponFreeShippingWithItemsPurchase.  # noqa: E501

        One or more shipping methods that may receive this discount  # noqa: E501

        :return: The shipping_methods of this CouponFreeShippingWithItemsPurchase.  # noqa: E501
        :rtype: list[str]
        """
        return self._shipping_methods

    @shipping_methods.setter
    def shipping_methods(self, shipping_methods):
        """Sets the shipping_methods of this CouponFreeShippingWithItemsPurchase.

        One or more shipping methods that may receive this discount  # noqa: E501

        :param shipping_methods: The shipping_methods of this CouponFreeShippingWithItemsPurchase.  # noqa: E501
        :type: list[str]
        """

        self._shipping_methods = shipping_methods

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
        if issubclass(CouponFreeShippingWithItemsPurchase, dict):
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
        if not isinstance(other, CouponFreeShippingWithItemsPurchase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
