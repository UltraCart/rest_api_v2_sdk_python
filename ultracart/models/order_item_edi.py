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


class OrderItemEdi(object):
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
        'identifications': 'list[OrderItemEdiIdentification]',
        'lots': 'list[OrderItemEdiLot]'
    }

    attribute_map = {
        'identifications': 'identifications',
        'lots': 'lots'
    }

    def __init__(self, identifications=None, lots=None):  # noqa: E501
        """OrderItemEdi - a model defined in Swagger"""  # noqa: E501

        self._identifications = None
        self._lots = None
        self.discriminator = None

        if identifications is not None:
            self.identifications = identifications
        if lots is not None:
            self.lots = lots

    @property
    def identifications(self):
        """Gets the identifications of this OrderItemEdi.  # noqa: E501

        Identification information receives on the EDI purchase order  # noqa: E501

        :return: The identifications of this OrderItemEdi.  # noqa: E501
        :rtype: list[OrderItemEdiIdentification]
        """
        return self._identifications

    @identifications.setter
    def identifications(self, identifications):
        """Sets the identifications of this OrderItemEdi.

        Identification information receives on the EDI purchase order  # noqa: E501

        :param identifications: The identifications of this OrderItemEdi.  # noqa: E501
        :type: list[OrderItemEdiIdentification]
        """

        self._identifications = identifications

    @property
    def lots(self):
        """Gets the lots of this OrderItemEdi.  # noqa: E501

        Lot information  # noqa: E501

        :return: The lots of this OrderItemEdi.  # noqa: E501
        :rtype: list[OrderItemEdiLot]
        """
        return self._lots

    @lots.setter
    def lots(self, lots):
        """Sets the lots of this OrderItemEdi.

        Lot information  # noqa: E501

        :param lots: The lots of this OrderItemEdi.  # noqa: E501
        :type: list[OrderItemEdiLot]
        """

        self._lots = lots

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
        if issubclass(OrderItemEdi, dict):
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
        if not isinstance(other, OrderItemEdi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
