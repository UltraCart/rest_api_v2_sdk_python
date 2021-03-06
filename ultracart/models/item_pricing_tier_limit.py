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


class ItemPricingTierLimit(object):
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
        'cumulative_order_limit': 'int',
        'individual_order_limit': 'int',
        'multiple_quantity': 'int'
    }

    attribute_map = {
        'cumulative_order_limit': 'cumulative_order_limit',
        'individual_order_limit': 'individual_order_limit',
        'multiple_quantity': 'multiple_quantity'
    }

    def __init__(self, cumulative_order_limit=None, individual_order_limit=None, multiple_quantity=None):  # noqa: E501
        """ItemPricingTierLimit - a model defined in Swagger"""  # noqa: E501

        self._cumulative_order_limit = None
        self._individual_order_limit = None
        self._multiple_quantity = None
        self.discriminator = None

        if cumulative_order_limit is not None:
            self.cumulative_order_limit = cumulative_order_limit
        if individual_order_limit is not None:
            self.individual_order_limit = individual_order_limit
        if multiple_quantity is not None:
            self.multiple_quantity = multiple_quantity

    @property
    def cumulative_order_limit(self):
        """Gets the cumulative_order_limit of this ItemPricingTierLimit.  # noqa: E501

        Cumulative order limit  # noqa: E501

        :return: The cumulative_order_limit of this ItemPricingTierLimit.  # noqa: E501
        :rtype: int
        """
        return self._cumulative_order_limit

    @cumulative_order_limit.setter
    def cumulative_order_limit(self, cumulative_order_limit):
        """Sets the cumulative_order_limit of this ItemPricingTierLimit.

        Cumulative order limit  # noqa: E501

        :param cumulative_order_limit: The cumulative_order_limit of this ItemPricingTierLimit.  # noqa: E501
        :type: int
        """

        self._cumulative_order_limit = cumulative_order_limit

    @property
    def individual_order_limit(self):
        """Gets the individual_order_limit of this ItemPricingTierLimit.  # noqa: E501

        Individual order limit  # noqa: E501

        :return: The individual_order_limit of this ItemPricingTierLimit.  # noqa: E501
        :rtype: int
        """
        return self._individual_order_limit

    @individual_order_limit.setter
    def individual_order_limit(self, individual_order_limit):
        """Sets the individual_order_limit of this ItemPricingTierLimit.

        Individual order limit  # noqa: E501

        :param individual_order_limit: The individual_order_limit of this ItemPricingTierLimit.  # noqa: E501
        :type: int
        """

        self._individual_order_limit = individual_order_limit

    @property
    def multiple_quantity(self):
        """Gets the multiple_quantity of this ItemPricingTierLimit.  # noqa: E501

        Multiple quantity  # noqa: E501

        :return: The multiple_quantity of this ItemPricingTierLimit.  # noqa: E501
        :rtype: int
        """
        return self._multiple_quantity

    @multiple_quantity.setter
    def multiple_quantity(self, multiple_quantity):
        """Sets the multiple_quantity of this ItemPricingTierLimit.

        Multiple quantity  # noqa: E501

        :param multiple_quantity: The multiple_quantity of this ItemPricingTierLimit.  # noqa: E501
        :type: int
        """

        self._multiple_quantity = multiple_quantity

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
        if issubclass(ItemPricingTierLimit, dict):
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
        if not isinstance(other, ItemPricingTierLimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
