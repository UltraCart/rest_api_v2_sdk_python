# coding: utf-8

"""
    UltraCart Rest API V2

    This is the next generation UltraCart REST API...

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class CouponAmountOffSubtotalWithItemsPurchase(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, currency_code=None, discount_amount=None, items=None, required_purchase_quantity=None):
        """
        CouponAmountOffSubtotalWithItemsPurchase - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'currency_code': 'str',
            'discount_amount': 'float',
            'items': 'list[str]',
            'required_purchase_quantity': 'int'
        }

        self.attribute_map = {
            'currency_code': 'currency_code',
            'discount_amount': 'discount_amount',
            'items': 'items',
            'required_purchase_quantity': 'required_purchase_quantity'
        }

        self._currency_code = currency_code
        self._discount_amount = discount_amount
        self._items = items
        self._required_purchase_quantity = required_purchase_quantity

    @property
    def currency_code(self):
        """
        Gets the currency_code of this CouponAmountOffSubtotalWithItemsPurchase.
        The ISO-4217 three letter currency code the customer is viewing prices in

        :return: The currency_code of this CouponAmountOffSubtotalWithItemsPurchase.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this CouponAmountOffSubtotalWithItemsPurchase.
        The ISO-4217 three letter currency code the customer is viewing prices in

        :param currency_code: The currency_code of this CouponAmountOffSubtotalWithItemsPurchase.
        :type: str
        """

        if not currency_code:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")
        if len(currency_code) > 3:
            raise ValueError("Invalid value for `currency_code`, length must be less than `3`")

        self._currency_code = currency_code

    @property
    def discount_amount(self):
        """
        Gets the discount_amount of this CouponAmountOffSubtotalWithItemsPurchase.
        The amount of shipping discount

        :return: The discount_amount of this CouponAmountOffSubtotalWithItemsPurchase.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """
        Sets the discount_amount of this CouponAmountOffSubtotalWithItemsPurchase.
        The amount of shipping discount

        :param discount_amount: The discount_amount of this CouponAmountOffSubtotalWithItemsPurchase.
        :type: float
        """

        self._discount_amount = discount_amount

    @property
    def items(self):
        """
        Gets the items of this CouponAmountOffSubtotalWithItemsPurchase.
        A list of items of which a quantity of one or many must be purchased for coupon to be valid.

        :return: The items of this CouponAmountOffSubtotalWithItemsPurchase.
        :rtype: list[str]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this CouponAmountOffSubtotalWithItemsPurchase.
        A list of items of which a quantity of one or many must be purchased for coupon to be valid.

        :param items: The items of this CouponAmountOffSubtotalWithItemsPurchase.
        :type: list[str]
        """

        self._items = items

    @property
    def required_purchase_quantity(self):
        """
        Gets the required_purchase_quantity of this CouponAmountOffSubtotalWithItemsPurchase.
        The quantity of items that must be purchased for the discount to be applied.

        :return: The required_purchase_quantity of this CouponAmountOffSubtotalWithItemsPurchase.
        :rtype: int
        """
        return self._required_purchase_quantity

    @required_purchase_quantity.setter
    def required_purchase_quantity(self, required_purchase_quantity):
        """
        Sets the required_purchase_quantity of this CouponAmountOffSubtotalWithItemsPurchase.
        The quantity of items that must be purchased for the discount to be applied.

        :param required_purchase_quantity: The required_purchase_quantity of this CouponAmountOffSubtotalWithItemsPurchase.
        :type: int
        """

        self._required_purchase_quantity = required_purchase_quantity

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
