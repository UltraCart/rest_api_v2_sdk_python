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


class OrderReplacementItem(object):
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
        'arbitrary_unit_cost': 'float',
        'merchant_item_id': 'str',
        'quantity': 'float'
    }

    attribute_map = {
        'arbitrary_unit_cost': 'arbitrary_unit_cost',
        'merchant_item_id': 'merchant_item_id',
        'quantity': 'quantity'
    }

    def __init__(self, arbitrary_unit_cost=None, merchant_item_id=None, quantity=None):
        """
        OrderReplacementItem - a model defined in Swagger
        """

        self._arbitrary_unit_cost = None
        self._merchant_item_id = None
        self._quantity = None
        self.discriminator = None

        if arbitrary_unit_cost is not None:
          self.arbitrary_unit_cost = arbitrary_unit_cost
        if merchant_item_id is not None:
          self.merchant_item_id = merchant_item_id
        if quantity is not None:
          self.quantity = quantity

    @property
    def arbitrary_unit_cost(self):
        """
        Gets the arbitrary_unit_cost of this OrderReplacementItem.
        Cost to charge the customer if specified.  If not specified then the default item cost is used.

        :return: The arbitrary_unit_cost of this OrderReplacementItem.
        :rtype: float
        """
        return self._arbitrary_unit_cost

    @arbitrary_unit_cost.setter
    def arbitrary_unit_cost(self, arbitrary_unit_cost):
        """
        Sets the arbitrary_unit_cost of this OrderReplacementItem.
        Cost to charge the customer if specified.  If not specified then the default item cost is used.

        :param arbitrary_unit_cost: The arbitrary_unit_cost of this OrderReplacementItem.
        :type: float
        """

        self._arbitrary_unit_cost = arbitrary_unit_cost

    @property
    def merchant_item_id(self):
        """
        Gets the merchant_item_id of this OrderReplacementItem.
        Item ID

        :return: The merchant_item_id of this OrderReplacementItem.
        :rtype: str
        """
        return self._merchant_item_id

    @merchant_item_id.setter
    def merchant_item_id(self, merchant_item_id):
        """
        Sets the merchant_item_id of this OrderReplacementItem.
        Item ID

        :param merchant_item_id: The merchant_item_id of this OrderReplacementItem.
        :type: str
        """
        if merchant_item_id is not None and len(merchant_item_id) > 20:
            raise ValueError("Invalid value for `merchant_item_id`, length must be less than or equal to `20`")

        self._merchant_item_id = merchant_item_id

    @property
    def quantity(self):
        """
        Gets the quantity of this OrderReplacementItem.
        Quantity

        :return: The quantity of this OrderReplacementItem.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this OrderReplacementItem.
        Quantity

        :param quantity: The quantity of this OrderReplacementItem.
        :type: float
        """

        self._quantity = quantity

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
        if not isinstance(other, OrderReplacementItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
