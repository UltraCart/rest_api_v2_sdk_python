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


class CartProfileLoginRequest(object):
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
        'cart': 'Cart',
        'customer_profile_oid': 'int',
        'password': 'str'
    }

    attribute_map = {
        'cart': 'cart',
        'customer_profile_oid': 'customer_profile_oid',
        'password': 'password'
    }

    def __init__(self, cart=None, customer_profile_oid=None, password=None):
        """
        CartProfileLoginRequest - a model defined in Swagger
        """

        self._cart = None
        self._customer_profile_oid = None
        self._password = None
        self.discriminator = None

        if cart is not None:
          self.cart = cart
        if customer_profile_oid is not None:
          self.customer_profile_oid = customer_profile_oid
        if password is not None:
          self.password = password

    @property
    def cart(self):
        """
        Gets the cart of this CartProfileLoginRequest.

        :return: The cart of this CartProfileLoginRequest.
        :rtype: Cart
        """
        return self._cart

    @cart.setter
    def cart(self, cart):
        """
        Sets the cart of this CartProfileLoginRequest.

        :param cart: The cart of this CartProfileLoginRequest.
        :type: Cart
        """

        self._cart = cart

    @property
    def customer_profile_oid(self):
        """
        Gets the customer_profile_oid of this CartProfileLoginRequest.
        Unique identifier for customer profile.  Can not be used with browser key authentication type.

        :return: The customer_profile_oid of this CartProfileLoginRequest.
        :rtype: int
        """
        return self._customer_profile_oid

    @customer_profile_oid.setter
    def customer_profile_oid(self, customer_profile_oid):
        """
        Sets the customer_profile_oid of this CartProfileLoginRequest.
        Unique identifier for customer profile.  Can not be used with browser key authentication type.

        :param customer_profile_oid: The customer_profile_oid of this CartProfileLoginRequest.
        :type: int
        """

        self._customer_profile_oid = customer_profile_oid

    @property
    def password(self):
        """
        Gets the password of this CartProfileLoginRequest.
        Password for the profile

        :return: The password of this CartProfileLoginRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CartProfileLoginRequest.
        Password for the profile

        :param password: The password of this CartProfileLoginRequest.
        :type: str
        """

        self._password = password

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
        if not isinstance(other, CartProfileLoginRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
