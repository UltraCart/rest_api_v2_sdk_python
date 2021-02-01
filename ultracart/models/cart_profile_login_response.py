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


class CartProfileLoginResponse(object):
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
        'cart': 'Cart',
        'errors': 'list[str]'
    }

    attribute_map = {
        'cart': 'cart',
        'errors': 'errors'
    }

    def __init__(self, cart=None, errors=None):  # noqa: E501
        """CartProfileLoginResponse - a model defined in Swagger"""  # noqa: E501

        self._cart = None
        self._errors = None
        self.discriminator = None

        if cart is not None:
            self.cart = cart
        if errors is not None:
            self.errors = errors

    @property
    def cart(self):
        """Gets the cart of this CartProfileLoginResponse.  # noqa: E501


        :return: The cart of this CartProfileLoginResponse.  # noqa: E501
        :rtype: Cart
        """
        return self._cart

    @cart.setter
    def cart(self, cart):
        """Sets the cart of this CartProfileLoginResponse.


        :param cart: The cart of this CartProfileLoginResponse.  # noqa: E501
        :type: Cart
        """

        self._cart = cart

    @property
    def errors(self):
        """Gets the errors of this CartProfileLoginResponse.  # noqa: E501

        Errors to display to the customer if they failed any of the validations checked  # noqa: E501

        :return: The errors of this CartProfileLoginResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this CartProfileLoginResponse.

        Errors to display to the customer if they failed any of the validations checked  # noqa: E501

        :param errors: The errors of this CartProfileLoginResponse.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

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
        if issubclass(CartProfileLoginResponse, dict):
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
        if not isinstance(other, CartProfileLoginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
