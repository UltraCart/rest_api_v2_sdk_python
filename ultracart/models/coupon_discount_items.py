# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CouponDiscountItems(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'currency_code': 'str',
        'discount_price': 'float',
        'items': 'list[str]',
        'limit': 'int'
    }

    attribute_map = {
        'currency_code': 'currency_code',
        'discount_price': 'discount_price',
        'items': 'items',
        'limit': 'limit'
    }

    def __init__(self, currency_code=None, discount_price=None, items=None, limit=None):
        """
        CouponDiscountItems - a model defined in Swagger
        """

        self._currency_code = None
        self._discount_price = None
        self._items = None
        self._limit = None
        self.discriminator = None

        if currency_code is not None:
          self.currency_code = currency_code
        if discount_price is not None:
          self.discount_price = discount_price
        if items is not None:
          self.items = items
        if limit is not None:
          self.limit = limit

    @property
    def currency_code(self):
        """
        Gets the currency_code of this CouponDiscountItems.
        The ISO-4217 three letter currency code the customer is viewing prices in

        :return: The currency_code of this CouponDiscountItems.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this CouponDiscountItems.
        The ISO-4217 three letter currency code the customer is viewing prices in

        :param currency_code: The currency_code of this CouponDiscountItems.
        :type: str
        """
        if currency_code is not None and len(currency_code) > 3:
            raise ValueError("Invalid value for `currency_code`, length must be less than or equal to `3`")

        self._currency_code = currency_code

    @property
    def discount_price(self):
        """
        Gets the discount_price of this CouponDiscountItems.
        The price (unit cost) of the discounted item

        :return: The discount_price of this CouponDiscountItems.
        :rtype: float
        """
        return self._discount_price

    @discount_price.setter
    def discount_price(self, discount_price):
        """
        Sets the discount_price of this CouponDiscountItems.
        The price (unit cost) of the discounted item

        :param discount_price: The discount_price of this CouponDiscountItems.
        :type: float
        """

        self._discount_price = discount_price

    @property
    def items(self):
        """
        Gets the items of this CouponDiscountItems.
        A list of items that are eligible for this discount_price.

        :return: The items of this CouponDiscountItems.
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this CouponDiscountItems.
        A list of items that are eligible for this discount_price.

        :param items: The items of this CouponDiscountItems.
        :type: list[str]
        """

        self._items = items

    @property
    def limit(self):
        """
        Gets the limit of this CouponDiscountItems.
        The (optional) maximum quantity of discounted items.

        :return: The limit of this CouponDiscountItems.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this CouponDiscountItems.
        The (optional) maximum quantity of discounted items.

        :param limit: The limit of this CouponDiscountItems.
        :type: int
        """

        self._limit = limit

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CouponDiscountItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
