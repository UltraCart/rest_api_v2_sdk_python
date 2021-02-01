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


class CouponDiscountItemWithItemPurchase(object):
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
        'currency_code': 'str',
        'discount_item': 'str',
        'discount_price': 'float',
        'limit': 'int',
        'required_purchase_item': 'str'
    }

    attribute_map = {
        'currency_code': 'currency_code',
        'discount_item': 'discount_item',
        'discount_price': 'discount_price',
        'limit': 'limit',
        'required_purchase_item': 'required_purchase_item'
    }

    def __init__(self, currency_code=None, discount_item=None, discount_price=None, limit=None, required_purchase_item=None):  # noqa: E501
        """CouponDiscountItemWithItemPurchase - a model defined in Swagger"""  # noqa: E501

        self._currency_code = None
        self._discount_item = None
        self._discount_price = None
        self._limit = None
        self._required_purchase_item = None
        self.discriminator = None

        if currency_code is not None:
            self.currency_code = currency_code
        if discount_item is not None:
            self.discount_item = discount_item
        if discount_price is not None:
            self.discount_price = discount_price
        if limit is not None:
            self.limit = limit
        if required_purchase_item is not None:
            self.required_purchase_item = required_purchase_item

    @property
    def currency_code(self):
        """Gets the currency_code of this CouponDiscountItemWithItemPurchase.  # noqa: E501

        The ISO-4217 three letter currency code the customer is viewing prices in  # noqa: E501

        :return: The currency_code of this CouponDiscountItemWithItemPurchase.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this CouponDiscountItemWithItemPurchase.

        The ISO-4217 three letter currency code the customer is viewing prices in  # noqa: E501

        :param currency_code: The currency_code of this CouponDiscountItemWithItemPurchase.  # noqa: E501
        :type: str
        """
        if currency_code is not None and len(currency_code) > 3:
            raise ValueError("Invalid value for `currency_code`, length must be less than or equal to `3`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def discount_item(self):
        """Gets the discount_item of this CouponDiscountItemWithItemPurchase.  # noqa: E501

        The item that will be sold at the discount_price when required_purchase_item is purchased.  # noqa: E501

        :return: The discount_item of this CouponDiscountItemWithItemPurchase.  # noqa: E501
        :rtype: str
        """
        return self._discount_item

    @discount_item.setter
    def discount_item(self, discount_item):
        """Sets the discount_item of this CouponDiscountItemWithItemPurchase.

        The item that will be sold at the discount_price when required_purchase_item is purchased.  # noqa: E501

        :param discount_item: The discount_item of this CouponDiscountItemWithItemPurchase.  # noqa: E501
        :type: str
        """

        self._discount_item = discount_item

    @property
    def discount_price(self):
        """Gets the discount_price of this CouponDiscountItemWithItemPurchase.  # noqa: E501

        The price (unit cost) of the discounted item  # noqa: E501

        :return: The discount_price of this CouponDiscountItemWithItemPurchase.  # noqa: E501
        :rtype: float
        """
        return self._discount_price

    @discount_price.setter
    def discount_price(self, discount_price):
        """Sets the discount_price of this CouponDiscountItemWithItemPurchase.

        The price (unit cost) of the discounted item  # noqa: E501

        :param discount_price: The discount_price of this CouponDiscountItemWithItemPurchase.  # noqa: E501
        :type: float
        """

        self._discount_price = discount_price

    @property
    def limit(self):
        """Gets the limit of this CouponDiscountItemWithItemPurchase.  # noqa: E501

        The (optional) maximum quantity of discounted items.  # noqa: E501

        :return: The limit of this CouponDiscountItemWithItemPurchase.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CouponDiscountItemWithItemPurchase.

        The (optional) maximum quantity of discounted items.  # noqa: E501

        :param limit: The limit of this CouponDiscountItemWithItemPurchase.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def required_purchase_item(self):
        """Gets the required_purchase_item of this CouponDiscountItemWithItemPurchase.  # noqa: E501

        The item that must be purchased for the discount to be applied to the discount item.  # noqa: E501

        :return: The required_purchase_item of this CouponDiscountItemWithItemPurchase.  # noqa: E501
        :rtype: str
        """
        return self._required_purchase_item

    @required_purchase_item.setter
    def required_purchase_item(self, required_purchase_item):
        """Sets the required_purchase_item of this CouponDiscountItemWithItemPurchase.

        The item that must be purchased for the discount to be applied to the discount item.  # noqa: E501

        :param required_purchase_item: The required_purchase_item of this CouponDiscountItemWithItemPurchase.  # noqa: E501
        :type: str
        """

        self._required_purchase_item = required_purchase_item

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
        if issubclass(CouponDiscountItemWithItemPurchase, dict):
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
        if not isinstance(other, CouponDiscountItemWithItemPurchase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
