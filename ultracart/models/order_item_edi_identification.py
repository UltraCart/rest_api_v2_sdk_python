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


class OrderItemEdiIdentification(object):
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
        'identification': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'identification': 'identification',
        'quantity': 'quantity'
    }

    def __init__(self, identification=None, quantity=None):  # noqa: E501
        """OrderItemEdiIdentification - a model defined in Swagger"""  # noqa: E501

        self._identification = None
        self._quantity = None
        self.discriminator = None

        if identification is not None:
            self.identification = identification
        if quantity is not None:
            self.quantity = quantity

    @property
    def identification(self):
        """Gets the identification of this OrderItemEdiIdentification.  # noqa: E501

        Identification value  # noqa: E501

        :return: The identification of this OrderItemEdiIdentification.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this OrderItemEdiIdentification.

        Identification value  # noqa: E501

        :param identification: The identification of this OrderItemEdiIdentification.  # noqa: E501
        :type: str
        """

        self._identification = identification

    @property
    def quantity(self):
        """Gets the quantity of this OrderItemEdiIdentification.  # noqa: E501

        Quantity associated with this identifier  # noqa: E501

        :return: The quantity of this OrderItemEdiIdentification.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderItemEdiIdentification.

        Quantity associated with this identifier  # noqa: E501

        :param quantity: The quantity of this OrderItemEdiIdentification.  # noqa: E501
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
        if issubclass(OrderItemEdiIdentification, dict):
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
        if not isinstance(other, OrderItemEdiIdentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
