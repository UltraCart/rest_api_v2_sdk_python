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


class OrderItemEdiLot(object):
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
        'lot_expiration': 'str',
        'lot_number': 'str',
        'lot_quantity': 'int'
    }

    attribute_map = {
        'lot_expiration': 'lot_expiration',
        'lot_number': 'lot_number',
        'lot_quantity': 'lot_quantity'
    }

    def __init__(self, lot_expiration=None, lot_number=None, lot_quantity=None):  # noqa: E501
        """OrderItemEdiLot - a model defined in Swagger"""  # noqa: E501

        self._lot_expiration = None
        self._lot_number = None
        self._lot_quantity = None
        self.discriminator = None

        if lot_expiration is not None:
            self.lot_expiration = lot_expiration
        if lot_number is not None:
            self.lot_number = lot_number
        if lot_quantity is not None:
            self.lot_quantity = lot_quantity

    @property
    def lot_expiration(self):
        """Gets the lot_expiration of this OrderItemEdiLot.  # noqa: E501

        Log expiration  # noqa: E501

        :return: The lot_expiration of this OrderItemEdiLot.  # noqa: E501
        :rtype: str
        """
        return self._lot_expiration

    @lot_expiration.setter
    def lot_expiration(self, lot_expiration):
        """Sets the lot_expiration of this OrderItemEdiLot.

        Log expiration  # noqa: E501

        :param lot_expiration: The lot_expiration of this OrderItemEdiLot.  # noqa: E501
        :type: str
        """

        self._lot_expiration = lot_expiration

    @property
    def lot_number(self):
        """Gets the lot_number of this OrderItemEdiLot.  # noqa: E501

        Lot number  # noqa: E501

        :return: The lot_number of this OrderItemEdiLot.  # noqa: E501
        :rtype: str
        """
        return self._lot_number

    @lot_number.setter
    def lot_number(self, lot_number):
        """Sets the lot_number of this OrderItemEdiLot.

        Lot number  # noqa: E501

        :param lot_number: The lot_number of this OrderItemEdiLot.  # noqa: E501
        :type: str
        """

        self._lot_number = lot_number

    @property
    def lot_quantity(self):
        """Gets the lot_quantity of this OrderItemEdiLot.  # noqa: E501

        Lot quantity  # noqa: E501

        :return: The lot_quantity of this OrderItemEdiLot.  # noqa: E501
        :rtype: int
        """
        return self._lot_quantity

    @lot_quantity.setter
    def lot_quantity(self, lot_quantity):
        """Sets the lot_quantity of this OrderItemEdiLot.

        Lot quantity  # noqa: E501

        :param lot_quantity: The lot_quantity of this OrderItemEdiLot.  # noqa: E501
        :type: int
        """

        self._lot_quantity = lot_quantity

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
        if issubclass(OrderItemEdiLot, dict):
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
        if not isinstance(other, OrderItemEdiLot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
