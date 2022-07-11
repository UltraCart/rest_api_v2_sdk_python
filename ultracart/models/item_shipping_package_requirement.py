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


class ItemShippingPackageRequirement(object):
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
        'package_name': 'str',
        'package_oid': 'int'
    }

    attribute_map = {
        'package_name': 'package_name',
        'package_oid': 'package_oid'
    }

    def __init__(self, package_name=None, package_oid=None):  # noqa: E501
        """ItemShippingPackageRequirement - a model defined in Swagger"""  # noqa: E501

        self._package_name = None
        self._package_oid = None
        self.discriminator = None

        if package_name is not None:
            self.package_name = package_name
        if package_oid is not None:
            self.package_oid = package_oid

    @property
    def package_name(self):
        """Gets the package_name of this ItemShippingPackageRequirement.  # noqa: E501

        Package name  # noqa: E501

        :return: The package_name of this ItemShippingPackageRequirement.  # noqa: E501
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this ItemShippingPackageRequirement.

        Package name  # noqa: E501

        :param package_name: The package_name of this ItemShippingPackageRequirement.  # noqa: E501
        :type: str
        """

        self._package_name = package_name

    @property
    def package_oid(self):
        """Gets the package_oid of this ItemShippingPackageRequirement.  # noqa: E501

        Package object identifier  # noqa: E501

        :return: The package_oid of this ItemShippingPackageRequirement.  # noqa: E501
        :rtype: int
        """
        return self._package_oid

    @package_oid.setter
    def package_oid(self, package_oid):
        """Sets the package_oid of this ItemShippingPackageRequirement.

        Package object identifier  # noqa: E501

        :param package_oid: The package_oid of this ItemShippingPackageRequirement.  # noqa: E501
        :type: int
        """

        self._package_oid = package_oid

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
        if issubclass(ItemShippingPackageRequirement, dict):
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
        if not isinstance(other, ItemShippingPackageRequirement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other