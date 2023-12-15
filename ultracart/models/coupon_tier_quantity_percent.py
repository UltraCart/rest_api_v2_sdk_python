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


class CouponTierQuantityPercent(object):
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
        'item_quantity': 'int',
        'quickbooks_code': 'str'
    }

    attribute_map = {
        'discount_percent': 'discount_percent',
        'item_quantity': 'item_quantity',
        'quickbooks_code': 'quickbooks_code'
    }

    def __init__(self, discount_percent=None, item_quantity=None, quickbooks_code=None):  # noqa: E501
        """CouponTierQuantityPercent - a model defined in Swagger"""  # noqa: E501

        self._discount_percent = None
        self._item_quantity = None
        self._quickbooks_code = None
        self.discriminator = None

        if discount_percent is not None:
            self.discount_percent = discount_percent
        if item_quantity is not None:
            self.item_quantity = item_quantity
        if quickbooks_code is not None:
            self.quickbooks_code = quickbooks_code

    @property
    def discount_percent(self):
        """Gets the discount_percent of this CouponTierQuantityPercent.  # noqa: E501

        The percent of discount per item.  # noqa: E501

        :return: The discount_percent of this CouponTierQuantityPercent.  # noqa: E501
        :rtype: float
        """
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, discount_percent):
        """Sets the discount_percent of this CouponTierQuantityPercent.

        The percent of discount per item.  # noqa: E501

        :param discount_percent: The discount_percent of this CouponTierQuantityPercent.  # noqa: E501
        :type: float
        """

        self._discount_percent = discount_percent

    @property
    def item_quantity(self):
        """Gets the item_quantity of this CouponTierQuantityPercent.  # noqa: E501

        The quantity of item purchased (in units)  # noqa: E501

        :return: The item_quantity of this CouponTierQuantityPercent.  # noqa: E501
        :rtype: int
        """
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, item_quantity):
        """Sets the item_quantity of this CouponTierQuantityPercent.

        The quantity of item purchased (in units)  # noqa: E501

        :param item_quantity: The item_quantity of this CouponTierQuantityPercent.  # noqa: E501
        :type: int
        """

        self._item_quantity = item_quantity

    @property
    def quickbooks_code(self):
        """Gets the quickbooks_code of this CouponTierQuantityPercent.  # noqa: E501

        Quickbooks accounting code.  # noqa: E501

        :return: The quickbooks_code of this CouponTierQuantityPercent.  # noqa: E501
        :rtype: str
        """
        return self._quickbooks_code

    @quickbooks_code.setter
    def quickbooks_code(self, quickbooks_code):
        """Sets the quickbooks_code of this CouponTierQuantityPercent.

        Quickbooks accounting code.  # noqa: E501

        :param quickbooks_code: The quickbooks_code of this CouponTierQuantityPercent.  # noqa: E501
        :type: str
        """
        if quickbooks_code is not None and len(quickbooks_code) > 20:
            raise ValueError("Invalid value for `quickbooks_code`, length must be less than or equal to `20`")  # noqa: E501

        self._quickbooks_code = quickbooks_code

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
        if issubclass(CouponTierQuantityPercent, dict):
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
        if not isinstance(other, CouponTierQuantityPercent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
