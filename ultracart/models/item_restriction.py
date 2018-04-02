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


class ItemRestriction(object):
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
        'exclude_coupon': 'bool',
        'exclude_from_free_promotion': 'bool',
        'items': 'list[ItemRestrictionItem]',
        'maximum_quantity': 'int',
        'minimum_quantity': 'int',
        'multiple_quantity': 'int',
        'one_per_customer': 'bool',
        'purchase_separately': 'bool'
    }

    attribute_map = {
        'exclude_coupon': 'exclude_coupon',
        'exclude_from_free_promotion': 'exclude_from_free_promotion',
        'items': 'items',
        'maximum_quantity': 'maximum_quantity',
        'minimum_quantity': 'minimum_quantity',
        'multiple_quantity': 'multiple_quantity',
        'one_per_customer': 'one_per_customer',
        'purchase_separately': 'purchase_separately'
    }

    def __init__(self, exclude_coupon=None, exclude_from_free_promotion=None, items=None, maximum_quantity=None, minimum_quantity=None, multiple_quantity=None, one_per_customer=None, purchase_separately=None):
        """
        ItemRestriction - a model defined in Swagger
        """

        self._exclude_coupon = None
        self._exclude_from_free_promotion = None
        self._items = None
        self._maximum_quantity = None
        self._minimum_quantity = None
        self._multiple_quantity = None
        self._one_per_customer = None
        self._purchase_separately = None
        self.discriminator = None

        if exclude_coupon is not None:
          self.exclude_coupon = exclude_coupon
        if exclude_from_free_promotion is not None:
          self.exclude_from_free_promotion = exclude_from_free_promotion
        if items is not None:
          self.items = items
        if maximum_quantity is not None:
          self.maximum_quantity = maximum_quantity
        if minimum_quantity is not None:
          self.minimum_quantity = minimum_quantity
        if multiple_quantity is not None:
          self.multiple_quantity = multiple_quantity
        if one_per_customer is not None:
          self.one_per_customer = one_per_customer
        if purchase_separately is not None:
          self.purchase_separately = purchase_separately

    @property
    def exclude_coupon(self):
        """
        Gets the exclude_coupon of this ItemRestriction.
        Exclude coupons

        :return: The exclude_coupon of this ItemRestriction.
        :rtype: bool
        """
        return self._exclude_coupon

    @exclude_coupon.setter
    def exclude_coupon(self, exclude_coupon):
        """
        Sets the exclude_coupon of this ItemRestriction.
        Exclude coupons

        :param exclude_coupon: The exclude_coupon of this ItemRestriction.
        :type: bool
        """

        self._exclude_coupon = exclude_coupon

    @property
    def exclude_from_free_promotion(self):
        """
        Gets the exclude_from_free_promotion of this ItemRestriction.
        Exclude from free promotion

        :return: The exclude_from_free_promotion of this ItemRestriction.
        :rtype: bool
        """
        return self._exclude_from_free_promotion

    @exclude_from_free_promotion.setter
    def exclude_from_free_promotion(self, exclude_from_free_promotion):
        """
        Sets the exclude_from_free_promotion of this ItemRestriction.
        Exclude from free promotion

        :param exclude_from_free_promotion: The exclude_from_free_promotion of this ItemRestriction.
        :type: bool
        """

        self._exclude_from_free_promotion = exclude_from_free_promotion

    @property
    def items(self):
        """
        Gets the items of this ItemRestriction.
        Items

        :return: The items of this ItemRestriction.
        :rtype: list[ItemRestrictionItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ItemRestriction.
        Items

        :param items: The items of this ItemRestriction.
        :type: list[ItemRestrictionItem]
        """

        self._items = items

    @property
    def maximum_quantity(self):
        """
        Gets the maximum_quantity of this ItemRestriction.
        Maximum quantity

        :return: The maximum_quantity of this ItemRestriction.
        :rtype: int
        """
        return self._maximum_quantity

    @maximum_quantity.setter
    def maximum_quantity(self, maximum_quantity):
        """
        Sets the maximum_quantity of this ItemRestriction.
        Maximum quantity

        :param maximum_quantity: The maximum_quantity of this ItemRestriction.
        :type: int
        """

        self._maximum_quantity = maximum_quantity

    @property
    def minimum_quantity(self):
        """
        Gets the minimum_quantity of this ItemRestriction.
        Minimum quantity (defaults to 1)

        :return: The minimum_quantity of this ItemRestriction.
        :rtype: int
        """
        return self._minimum_quantity

    @minimum_quantity.setter
    def minimum_quantity(self, minimum_quantity):
        """
        Sets the minimum_quantity of this ItemRestriction.
        Minimum quantity (defaults to 1)

        :param minimum_quantity: The minimum_quantity of this ItemRestriction.
        :type: int
        """

        self._minimum_quantity = minimum_quantity

    @property
    def multiple_quantity(self):
        """
        Gets the multiple_quantity of this ItemRestriction.
        Multiple of quantity

        :return: The multiple_quantity of this ItemRestriction.
        :rtype: int
        """
        return self._multiple_quantity

    @multiple_quantity.setter
    def multiple_quantity(self, multiple_quantity):
        """
        Sets the multiple_quantity of this ItemRestriction.
        Multiple of quantity

        :param multiple_quantity: The multiple_quantity of this ItemRestriction.
        :type: int
        """

        self._multiple_quantity = multiple_quantity

    @property
    def one_per_customer(self):
        """
        Gets the one_per_customer of this ItemRestriction.
        One per customer

        :return: The one_per_customer of this ItemRestriction.
        :rtype: bool
        """
        return self._one_per_customer

    @one_per_customer.setter
    def one_per_customer(self, one_per_customer):
        """
        Sets the one_per_customer of this ItemRestriction.
        One per customer

        :param one_per_customer: The one_per_customer of this ItemRestriction.
        :type: bool
        """

        self._one_per_customer = one_per_customer

    @property
    def purchase_separately(self):
        """
        Gets the purchase_separately of this ItemRestriction.
        Purchase separately

        :return: The purchase_separately of this ItemRestriction.
        :rtype: bool
        """
        return self._purchase_separately

    @purchase_separately.setter
    def purchase_separately(self, purchase_separately):
        """
        Sets the purchase_separately of this ItemRestriction.
        Purchase separately

        :param purchase_separately: The purchase_separately of this ItemRestriction.
        :type: bool
        """

        self._purchase_separately = purchase_separately

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
        if not isinstance(other, ItemRestriction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
