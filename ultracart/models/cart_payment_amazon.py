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


class CartPaymentAmazon(object):
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
        'amazon_order_reference_id': 'str'
    }

    attribute_map = {
        'amazon_order_reference_id': 'amazon_order_reference_id'
    }

    def __init__(self, amazon_order_reference_id=None):  # noqa: E501
        """CartPaymentAmazon - a model defined in Swagger"""  # noqa: E501

        self._amazon_order_reference_id = None
        self.discriminator = None

        if amazon_order_reference_id is not None:
            self.amazon_order_reference_id = amazon_order_reference_id

    @property
    def amazon_order_reference_id(self):
        """Gets the amazon_order_reference_id of this CartPaymentAmazon.  # noqa: E501

        Amazon order reference id  # noqa: E501

        :return: The amazon_order_reference_id of this CartPaymentAmazon.  # noqa: E501
        :rtype: str
        """
        return self._amazon_order_reference_id

    @amazon_order_reference_id.setter
    def amazon_order_reference_id(self, amazon_order_reference_id):
        """Sets the amazon_order_reference_id of this CartPaymentAmazon.

        Amazon order reference id  # noqa: E501

        :param amazon_order_reference_id: The amazon_order_reference_id of this CartPaymentAmazon.  # noqa: E501
        :type: str
        """

        self._amazon_order_reference_id = amazon_order_reference_id

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
        if issubclass(CartPaymentAmazon, dict):
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
        if not isinstance(other, CartPaymentAmazon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other