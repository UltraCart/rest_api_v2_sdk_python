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


class CartFinalizeOrderResponse(object):
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
        'errors': 'list[str]',
        'next_cart': 'Cart',
        'order': 'Order',
        'order_id': 'str',
        'successful': 'bool'
    }

    attribute_map = {
        'errors': 'errors',
        'next_cart': 'next_cart',
        'order': 'order',
        'order_id': 'order_id',
        'successful': 'successful'
    }

    def __init__(self, errors=None, next_cart=None, order=None, order_id=None, successful=None):  # noqa: E501
        """CartFinalizeOrderResponse - a model defined in Swagger"""  # noqa: E501

        self._errors = None
        self._next_cart = None
        self._order = None
        self._order_id = None
        self._successful = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors
        if next_cart is not None:
            self.next_cart = next_cart
        if order is not None:
            self.order = order
        if order_id is not None:
            self.order_id = order_id
        if successful is not None:
            self.successful = successful

    @property
    def errors(self):
        """Gets the errors of this CartFinalizeOrderResponse.  # noqa: E501

        Error messages if the order could not be completed  # noqa: E501

        :return: The errors of this CartFinalizeOrderResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this CartFinalizeOrderResponse.

        Error messages if the order could not be completed  # noqa: E501

        :param errors: The errors of this CartFinalizeOrderResponse.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

    @property
    def next_cart(self):
        """Gets the next_cart of this CartFinalizeOrderResponse.  # noqa: E501


        :return: The next_cart of this CartFinalizeOrderResponse.  # noqa: E501
        :rtype: Cart
        """
        return self._next_cart

    @next_cart.setter
    def next_cart(self, next_cart):
        """Sets the next_cart of this CartFinalizeOrderResponse.


        :param next_cart: The next_cart of this CartFinalizeOrderResponse.  # noqa: E501
        :type: Cart
        """

        self._next_cart = next_cart

    @property
    def order(self):
        """Gets the order of this CartFinalizeOrderResponse.  # noqa: E501


        :return: The order of this CartFinalizeOrderResponse.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CartFinalizeOrderResponse.


        :param order: The order of this CartFinalizeOrderResponse.  # noqa: E501
        :type: Order
        """

        self._order = order

    @property
    def order_id(self):
        """Gets the order_id of this CartFinalizeOrderResponse.  # noqa: E501

        Order ID assigned to the order  # noqa: E501

        :return: The order_id of this CartFinalizeOrderResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CartFinalizeOrderResponse.

        Order ID assigned to the order  # noqa: E501

        :param order_id: The order_id of this CartFinalizeOrderResponse.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def successful(self):
        """Gets the successful of this CartFinalizeOrderResponse.  # noqa: E501

        True if the cart was converted successfully to an order  # noqa: E501

        :return: The successful of this CartFinalizeOrderResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this CartFinalizeOrderResponse.

        True if the cart was converted successfully to an order  # noqa: E501

        :param successful: The successful of this CartFinalizeOrderResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

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
        if issubclass(CartFinalizeOrderResponse, dict):
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
        if not isinstance(other, CartFinalizeOrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
