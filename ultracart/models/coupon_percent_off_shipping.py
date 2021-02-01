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


class CouponPercentOffShipping(object):
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
        'discount_percent': 'float',
        'shipping_methods': 'list[str]'
    }

    attribute_map = {
        'discount_percent': 'discount_percent',
        'shipping_methods': 'shipping_methods'
    }

    def __init__(self, discount_percent=None, shipping_methods=None):  # noqa: E501
        """CouponPercentOffShipping - a model defined in Swagger"""  # noqa: E501

        self._discount_percent = None
        self._shipping_methods = None
        self.discriminator = None

        if discount_percent is not None:
            self.discount_percent = discount_percent
        if shipping_methods is not None:
            self.shipping_methods = shipping_methods

    @property
    def discount_percent(self):
        """Gets the discount_percent of this CouponPercentOffShipping.  # noqa: E501

        The percentage of subtotal discount  # noqa: E501

        :return: The discount_percent of this CouponPercentOffShipping.  # noqa: E501
        :rtype: float
        """
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, discount_percent):
        """Sets the discount_percent of this CouponPercentOffShipping.

        The percentage of subtotal discount  # noqa: E501

        :param discount_percent: The discount_percent of this CouponPercentOffShipping.  # noqa: E501
        :type: float
        """

        self._discount_percent = discount_percent

    @property
    def shipping_methods(self):
        """Gets the shipping_methods of this CouponPercentOffShipping.  # noqa: E501

        One or more shipping methods that may be used with this coupon  # noqa: E501

        :return: The shipping_methods of this CouponPercentOffShipping.  # noqa: E501
        :rtype: list[str]
        """
        return self._shipping_methods

    @shipping_methods.setter
    def shipping_methods(self, shipping_methods):
        """Sets the shipping_methods of this CouponPercentOffShipping.

        One or more shipping methods that may be used with this coupon  # noqa: E501

        :param shipping_methods: The shipping_methods of this CouponPercentOffShipping.  # noqa: E501
        :type: list[str]
        """

        self._shipping_methods = shipping_methods

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
        if issubclass(CouponPercentOffShipping, dict):
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
        if not isinstance(other, CouponPercentOffShipping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
