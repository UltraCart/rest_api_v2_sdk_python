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


class AutoOrderAddonItem(object):
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
        'arbitrary_unit_cost': 'float',
        'free_shipping': 'bool',
        'item_id': 'str',
        'next_x_orders': 'int',
        'options': 'list[AutoOrderAddonItemOption]',
        'quantity': 'int'
    }

    attribute_map = {
        'arbitrary_unit_cost': 'arbitrary_unit_cost',
        'free_shipping': 'free_shipping',
        'item_id': 'item_id',
        'next_x_orders': 'next_x_orders',
        'options': 'options',
        'quantity': 'quantity'
    }

    def __init__(self, arbitrary_unit_cost=None, free_shipping=None, item_id=None, next_x_orders=None, options=None, quantity=None):  # noqa: E501
        """AutoOrderAddonItem - a model defined in Swagger"""  # noqa: E501

        self._arbitrary_unit_cost = None
        self._free_shipping = None
        self._item_id = None
        self._next_x_orders = None
        self._options = None
        self._quantity = None
        self.discriminator = None

        if arbitrary_unit_cost is not None:
            self.arbitrary_unit_cost = arbitrary_unit_cost
        if free_shipping is not None:
            self.free_shipping = free_shipping
        if item_id is not None:
            self.item_id = item_id
        if next_x_orders is not None:
            self.next_x_orders = next_x_orders
        if options is not None:
            self.options = options
        if quantity is not None:
            self.quantity = quantity

    @property
    def arbitrary_unit_cost(self):
        """Gets the arbitrary_unit_cost of this AutoOrderAddonItem.  # noqa: E501


        :return: The arbitrary_unit_cost of this AutoOrderAddonItem.  # noqa: E501
        :rtype: float
        """
        return self._arbitrary_unit_cost

    @arbitrary_unit_cost.setter
    def arbitrary_unit_cost(self, arbitrary_unit_cost):
        """Sets the arbitrary_unit_cost of this AutoOrderAddonItem.


        :param arbitrary_unit_cost: The arbitrary_unit_cost of this AutoOrderAddonItem.  # noqa: E501
        :type: float
        """

        self._arbitrary_unit_cost = arbitrary_unit_cost

    @property
    def free_shipping(self):
        """Gets the free_shipping of this AutoOrderAddonItem.  # noqa: E501


        :return: The free_shipping of this AutoOrderAddonItem.  # noqa: E501
        :rtype: bool
        """
        return self._free_shipping

    @free_shipping.setter
    def free_shipping(self, free_shipping):
        """Sets the free_shipping of this AutoOrderAddonItem.


        :param free_shipping: The free_shipping of this AutoOrderAddonItem.  # noqa: E501
        :type: bool
        """

        self._free_shipping = free_shipping

    @property
    def item_id(self):
        """Gets the item_id of this AutoOrderAddonItem.  # noqa: E501


        :return: The item_id of this AutoOrderAddonItem.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this AutoOrderAddonItem.


        :param item_id: The item_id of this AutoOrderAddonItem.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def next_x_orders(self):
        """Gets the next_x_orders of this AutoOrderAddonItem.  # noqa: E501


        :return: The next_x_orders of this AutoOrderAddonItem.  # noqa: E501
        :rtype: int
        """
        return self._next_x_orders

    @next_x_orders.setter
    def next_x_orders(self, next_x_orders):
        """Sets the next_x_orders of this AutoOrderAddonItem.


        :param next_x_orders: The next_x_orders of this AutoOrderAddonItem.  # noqa: E501
        :type: int
        """

        self._next_x_orders = next_x_orders

    @property
    def options(self):
        """Gets the options of this AutoOrderAddonItem.  # noqa: E501

        Options associated with this item  # noqa: E501

        :return: The options of this AutoOrderAddonItem.  # noqa: E501
        :rtype: list[AutoOrderAddonItemOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this AutoOrderAddonItem.

        Options associated with this item  # noqa: E501

        :param options: The options of this AutoOrderAddonItem.  # noqa: E501
        :type: list[AutoOrderAddonItemOption]
        """

        self._options = options

    @property
    def quantity(self):
        """Gets the quantity of this AutoOrderAddonItem.  # noqa: E501


        :return: The quantity of this AutoOrderAddonItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this AutoOrderAddonItem.


        :param quantity: The quantity of this AutoOrderAddonItem.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if issubclass(AutoOrderAddonItem, dict):
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
        if not isinstance(other, AutoOrderAddonItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
