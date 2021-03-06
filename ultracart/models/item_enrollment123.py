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


class ItemEnrollment123(object):
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
        'enrollment123_product_code': 'str'
    }

    attribute_map = {
        'enrollment123_product_code': 'enrollment123_product_code'
    }

    def __init__(self, enrollment123_product_code=None):  # noqa: E501
        """ItemEnrollment123 - a model defined in Swagger"""  # noqa: E501

        self._enrollment123_product_code = None
        self.discriminator = None

        if enrollment123_product_code is not None:
            self.enrollment123_product_code = enrollment123_product_code

    @property
    def enrollment123_product_code(self):
        """Gets the enrollment123_product_code of this ItemEnrollment123.  # noqa: E501

        Enrolment 123 product code  # noqa: E501

        :return: The enrollment123_product_code of this ItemEnrollment123.  # noqa: E501
        :rtype: str
        """
        return self._enrollment123_product_code

    @enrollment123_product_code.setter
    def enrollment123_product_code(self, enrollment123_product_code):
        """Sets the enrollment123_product_code of this ItemEnrollment123.

        Enrolment 123 product code  # noqa: E501

        :param enrollment123_product_code: The enrollment123_product_code of this ItemEnrollment123.  # noqa: E501
        :type: str
        """

        self._enrollment123_product_code = enrollment123_product_code

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
        if issubclass(ItemEnrollment123, dict):
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
        if not isinstance(other, ItemEnrollment123):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
