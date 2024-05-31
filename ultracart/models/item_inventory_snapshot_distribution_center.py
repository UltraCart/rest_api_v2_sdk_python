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


class ItemInventorySnapshotDistributionCenter(object):
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
        'allocated_to_placed_orders': 'int',
        'allocated_to_shopping_carts': 'int',
        'available_to_allocate': 'int',
        'code': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'allocated_to_placed_orders': 'allocated_to_placed_orders',
        'allocated_to_shopping_carts': 'allocated_to_shopping_carts',
        'available_to_allocate': 'available_to_allocate',
        'code': 'code',
        'quantity': 'quantity'
    }

    def __init__(self, allocated_to_placed_orders=None, allocated_to_shopping_carts=None, available_to_allocate=None, code=None, quantity=None):  # noqa: E501
        """ItemInventorySnapshotDistributionCenter - a model defined in Swagger"""  # noqa: E501

        self._allocated_to_placed_orders = None
        self._allocated_to_shopping_carts = None
        self._available_to_allocate = None
        self._code = None
        self._quantity = None
        self.discriminator = None

        if allocated_to_placed_orders is not None:
            self.allocated_to_placed_orders = allocated_to_placed_orders
        if allocated_to_shopping_carts is not None:
            self.allocated_to_shopping_carts = allocated_to_shopping_carts
        if available_to_allocate is not None:
            self.available_to_allocate = available_to_allocate
        if code is not None:
            self.code = code
        if quantity is not None:
            self.quantity = quantity

    @property
    def allocated_to_placed_orders(self):
        """Gets the allocated_to_placed_orders of this ItemInventorySnapshotDistributionCenter.  # noqa: E501


        :return: The allocated_to_placed_orders of this ItemInventorySnapshotDistributionCenter.  # noqa: E501
        :rtype: int
        """
        return self._allocated_to_placed_orders

    @allocated_to_placed_orders.setter
    def allocated_to_placed_orders(self, allocated_to_placed_orders):
        """Sets the allocated_to_placed_orders of this ItemInventorySnapshotDistributionCenter.


        :param allocated_to_placed_orders: The allocated_to_placed_orders of this ItemInventorySnapshotDistributionCenter.  # noqa: E501
        :type: int
        """

        self._allocated_to_placed_orders = allocated_to_placed_orders

    @property
    def allocated_to_shopping_carts(self):
        """Gets the allocated_to_shopping_carts of this ItemInventorySnapshotDistributionCenter.  # noqa: E501


        :return: The allocated_to_shopping_carts of this ItemInventorySnapshotDistributionCenter.  # noqa: E501
        :rtype: int
        """
        return self._allocated_to_shopping_carts

    @allocated_to_shopping_carts.setter
    def allocated_to_shopping_carts(self, allocated_to_shopping_carts):
        """Sets the allocated_to_shopping_carts of this ItemInventorySnapshotDistributionCenter.


        :param allocated_to_shopping_carts: The allocated_to_shopping_carts of this ItemInventorySnapshotDistributionCenter.  # noqa: E501
        :type: int
        """

        self._allocated_to_shopping_carts = allocated_to_shopping_carts

    @property
    def available_to_allocate(self):
        """Gets the available_to_allocate of this ItemInventorySnapshotDistributionCenter.  # noqa: E501


        :return: The available_to_allocate of this ItemInventorySnapshotDistributionCenter.  # noqa: E501
        :rtype: int
        """
        return self._available_to_allocate

    @available_to_allocate.setter
    def available_to_allocate(self, available_to_allocate):
        """Sets the available_to_allocate of this ItemInventorySnapshotDistributionCenter.


        :param available_to_allocate: The available_to_allocate of this ItemInventorySnapshotDistributionCenter.  # noqa: E501
        :type: int
        """

        self._available_to_allocate = available_to_allocate

    @property
    def code(self):
        """Gets the code of this ItemInventorySnapshotDistributionCenter.  # noqa: E501


        :return: The code of this ItemInventorySnapshotDistributionCenter.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ItemInventorySnapshotDistributionCenter.


        :param code: The code of this ItemInventorySnapshotDistributionCenter.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def quantity(self):
        """Gets the quantity of this ItemInventorySnapshotDistributionCenter.  # noqa: E501


        :return: The quantity of this ItemInventorySnapshotDistributionCenter.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ItemInventorySnapshotDistributionCenter.


        :param quantity: The quantity of this ItemInventorySnapshotDistributionCenter.  # noqa: E501
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
        if issubclass(ItemInventorySnapshotDistributionCenter, dict):
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
        if not isinstance(other, ItemInventorySnapshotDistributionCenter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
