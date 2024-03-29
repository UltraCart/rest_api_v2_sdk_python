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


class CouponNoDiscount(object):
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
        'ignore_this_property': 'bool'
    }

    attribute_map = {
        'ignore_this_property': 'ignore_this_property'
    }

    def __init__(self, ignore_this_property=None):  # noqa: E501
        """CouponNoDiscount - a model defined in Swagger"""  # noqa: E501

        self._ignore_this_property = None
        self.discriminator = None

        if ignore_this_property is not None:
            self.ignore_this_property = ignore_this_property

    @property
    def ignore_this_property(self):
        """Gets the ignore_this_property of this CouponNoDiscount.  # noqa: E501

        This property does nothing but is included in this object to ensure the object is generated by our sdk builders.  # noqa: E501

        :return: The ignore_this_property of this CouponNoDiscount.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_this_property

    @ignore_this_property.setter
    def ignore_this_property(self, ignore_this_property):
        """Sets the ignore_this_property of this CouponNoDiscount.

        This property does nothing but is included in this object to ensure the object is generated by our sdk builders.  # noqa: E501

        :param ignore_this_property: The ignore_this_property of this CouponNoDiscount.  # noqa: E501
        :type: bool
        """

        self._ignore_this_property = ignore_this_property

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
        if issubclass(CouponNoDiscount, dict):
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
        if not isinstance(other, CouponNoDiscount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
