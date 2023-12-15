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


class CouponPercentMoreLoyaltyPoints(object):
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
        'percent_more_loyalty_points': 'float'
    }

    attribute_map = {
        'percent_more_loyalty_points': 'percent_more_loyalty_points'
    }

    def __init__(self, percent_more_loyalty_points=None):  # noqa: E501
        """CouponPercentMoreLoyaltyPoints - a model defined in Swagger"""  # noqa: E501

        self._percent_more_loyalty_points = None
        self.discriminator = None

        if percent_more_loyalty_points is not None:
            self.percent_more_loyalty_points = percent_more_loyalty_points

    @property
    def percent_more_loyalty_points(self):
        """Gets the percent_more_loyalty_points of this CouponPercentMoreLoyaltyPoints.  # noqa: E501

        The percentage of additional loyalty points  # noqa: E501

        :return: The percent_more_loyalty_points of this CouponPercentMoreLoyaltyPoints.  # noqa: E501
        :rtype: float
        """
        return self._percent_more_loyalty_points

    @percent_more_loyalty_points.setter
    def percent_more_loyalty_points(self, percent_more_loyalty_points):
        """Sets the percent_more_loyalty_points of this CouponPercentMoreLoyaltyPoints.

        The percentage of additional loyalty points  # noqa: E501

        :param percent_more_loyalty_points: The percent_more_loyalty_points of this CouponPercentMoreLoyaltyPoints.  # noqa: E501
        :type: float
        """

        self._percent_more_loyalty_points = percent_more_loyalty_points

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
        if issubclass(CouponPercentMoreLoyaltyPoints, dict):
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
        if not isinstance(other, CouponPercentMoreLoyaltyPoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
