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


class CartFinalizeOrderResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, errors=None, next_cart=None, order=None, order_id=None, successful=None):
        """
        CartFinalizeOrderResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'errors': 'list[str]',
            'next_cart': 'Cart',
            'order': 'Order',
            'order_id': 'str',
            'successful': 'bool'
        }

        self.attribute_map = {
            'errors': 'errors',
            'next_cart': 'next_cart',
            'order': 'order',
            'order_id': 'order_id',
            'successful': 'successful'
        }

        self._errors = errors
        self._next_cart = next_cart
        self._order = order
        self._order_id = order_id
        self._successful = successful

    @property
    def errors(self):
        """
        Gets the errors of this CartFinalizeOrderResponse.
        Error messages if the order could not be completed

        :return: The errors of this CartFinalizeOrderResponse.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this CartFinalizeOrderResponse.
        Error messages if the order could not be completed

        :param errors: The errors of this CartFinalizeOrderResponse.
        :type: list[str]
        """

        self._errors = errors

    @property
    def next_cart(self):
        """
        Gets the next_cart of this CartFinalizeOrderResponse.


        :return: The next_cart of this CartFinalizeOrderResponse.
        :rtype: Cart
        """
        return self._next_cart

    @next_cart.setter
    def next_cart(self, next_cart):
        """
        Sets the next_cart of this CartFinalizeOrderResponse.


        :param next_cart: The next_cart of this CartFinalizeOrderResponse.
        :type: Cart
        """

        self._next_cart = next_cart

    @property
    def order(self):
        """
        Gets the order of this CartFinalizeOrderResponse.


        :return: The order of this CartFinalizeOrderResponse.
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this CartFinalizeOrderResponse.


        :param order: The order of this CartFinalizeOrderResponse.
        :type: Order
        """

        self._order = order

    @property
    def order_id(self):
        """
        Gets the order_id of this CartFinalizeOrderResponse.
        Order ID assigned to the order

        :return: The order_id of this CartFinalizeOrderResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """
        Sets the order_id of this CartFinalizeOrderResponse.
        Order ID assigned to the order

        :param order_id: The order_id of this CartFinalizeOrderResponse.
        :type: str
        """

        self._order_id = order_id

    @property
    def successful(self):
        """
        Gets the successful of this CartFinalizeOrderResponse.
        True if the cart was converted successfully to an order

        :return: The successful of this CartFinalizeOrderResponse.
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """
        Sets the successful of this CartFinalizeOrderResponse.
        True if the cart was converted successfully to an order

        :param successful: The successful of this CartFinalizeOrderResponse.
        :type: bool
        """

        self._successful = successful

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
