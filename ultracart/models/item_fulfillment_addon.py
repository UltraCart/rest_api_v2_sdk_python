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


class ItemFulfillmentAddon(object):
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
        'add_item_id': 'str',
        'add_item_oid': 'int',
        'initial_order_only': 'bool',
        'once_per_order': 'bool',
        'quantity': 'int'
    }

    attribute_map = {
        'add_item_id': 'add_item_id',
        'add_item_oid': 'add_item_oid',
        'initial_order_only': 'initial_order_only',
        'once_per_order': 'once_per_order',
        'quantity': 'quantity'
    }

    def __init__(self, add_item_id=None, add_item_oid=None, initial_order_only=None, once_per_order=None, quantity=None):  # noqa: E501
        """ItemFulfillmentAddon - a model defined in Swagger"""  # noqa: E501

        self._add_item_id = None
        self._add_item_oid = None
        self._initial_order_only = None
        self._once_per_order = None
        self._quantity = None
        self.discriminator = None

        if add_item_id is not None:
            self.add_item_id = add_item_id
        if add_item_oid is not None:
            self.add_item_oid = add_item_oid
        if initial_order_only is not None:
            self.initial_order_only = initial_order_only
        if once_per_order is not None:
            self.once_per_order = once_per_order
        if quantity is not None:
            self.quantity = quantity

    @property
    def add_item_id(self):
        """Gets the add_item_id of this ItemFulfillmentAddon.  # noqa: E501

        Add Item Id  # noqa: E501

        :return: The add_item_id of this ItemFulfillmentAddon.  # noqa: E501
        :rtype: str
        """
        return self._add_item_id

    @add_item_id.setter
    def add_item_id(self, add_item_id):
        """Sets the add_item_id of this ItemFulfillmentAddon.

        Add Item Id  # noqa: E501

        :param add_item_id: The add_item_id of this ItemFulfillmentAddon.  # noqa: E501
        :type: str
        """

        self._add_item_id = add_item_id

    @property
    def add_item_oid(self):
        """Gets the add_item_oid of this ItemFulfillmentAddon.  # noqa: E501

        Add Item object identifier  # noqa: E501

        :return: The add_item_oid of this ItemFulfillmentAddon.  # noqa: E501
        :rtype: int
        """
        return self._add_item_oid

    @add_item_oid.setter
    def add_item_oid(self, add_item_oid):
        """Sets the add_item_oid of this ItemFulfillmentAddon.

        Add Item object identifier  # noqa: E501

        :param add_item_oid: The add_item_oid of this ItemFulfillmentAddon.  # noqa: E501
        :type: int
        """

        self._add_item_oid = add_item_oid

    @property
    def initial_order_only(self):
        """Gets the initial_order_only of this ItemFulfillmentAddon.  # noqa: E501

        Initial Order Only  # noqa: E501

        :return: The initial_order_only of this ItemFulfillmentAddon.  # noqa: E501
        :rtype: bool
        """
        return self._initial_order_only

    @initial_order_only.setter
    def initial_order_only(self, initial_order_only):
        """Sets the initial_order_only of this ItemFulfillmentAddon.

        Initial Order Only  # noqa: E501

        :param initial_order_only: The initial_order_only of this ItemFulfillmentAddon.  # noqa: E501
        :type: bool
        """

        self._initial_order_only = initial_order_only

    @property
    def once_per_order(self):
        """Gets the once_per_order of this ItemFulfillmentAddon.  # noqa: E501

        Once Per Order  # noqa: E501

        :return: The once_per_order of this ItemFulfillmentAddon.  # noqa: E501
        :rtype: bool
        """
        return self._once_per_order

    @once_per_order.setter
    def once_per_order(self, once_per_order):
        """Sets the once_per_order of this ItemFulfillmentAddon.

        Once Per Order  # noqa: E501

        :param once_per_order: The once_per_order of this ItemFulfillmentAddon.  # noqa: E501
        :type: bool
        """

        self._once_per_order = once_per_order

    @property
    def quantity(self):
        """Gets the quantity of this ItemFulfillmentAddon.  # noqa: E501

        Quantity  # noqa: E501

        :return: The quantity of this ItemFulfillmentAddon.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ItemFulfillmentAddon.

        Quantity  # noqa: E501

        :param quantity: The quantity of this ItemFulfillmentAddon.  # noqa: E501
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
        if issubclass(ItemFulfillmentAddon, dict):
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
        if not isinstance(other, ItemFulfillmentAddon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
