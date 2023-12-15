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


class CustomerProperty(object):
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
        'customer_profile_property_oid': 'int',
        'expiration_dts': 'str',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'customer_profile_property_oid': 'customer_profile_property_oid',
        'expiration_dts': 'expiration_dts',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, customer_profile_property_oid=None, expiration_dts=None, name=None, value=None):  # noqa: E501
        """CustomerProperty - a model defined in Swagger"""  # noqa: E501

        self._customer_profile_property_oid = None
        self._expiration_dts = None
        self._name = None
        self._value = None
        self.discriminator = None

        if customer_profile_property_oid is not None:
            self.customer_profile_property_oid = customer_profile_property_oid
        if expiration_dts is not None:
            self.expiration_dts = expiration_dts
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def customer_profile_property_oid(self):
        """Gets the customer_profile_property_oid of this CustomerProperty.  # noqa: E501

        Customer profile property oid  # noqa: E501

        :return: The customer_profile_property_oid of this CustomerProperty.  # noqa: E501
        :rtype: int
        """
        return self._customer_profile_property_oid

    @customer_profile_property_oid.setter
    def customer_profile_property_oid(self, customer_profile_property_oid):
        """Sets the customer_profile_property_oid of this CustomerProperty.

        Customer profile property oid  # noqa: E501

        :param customer_profile_property_oid: The customer_profile_property_oid of this CustomerProperty.  # noqa: E501
        :type: int
        """

        self._customer_profile_property_oid = customer_profile_property_oid

    @property
    def expiration_dts(self):
        """Gets the expiration_dts of this CustomerProperty.  # noqa: E501

        The date/time that the property expires and is deleted  # noqa: E501

        :return: The expiration_dts of this CustomerProperty.  # noqa: E501
        :rtype: str
        """
        return self._expiration_dts

    @expiration_dts.setter
    def expiration_dts(self, expiration_dts):
        """Sets the expiration_dts of this CustomerProperty.

        The date/time that the property expires and is deleted  # noqa: E501

        :param expiration_dts: The expiration_dts of this CustomerProperty.  # noqa: E501
        :type: str
        """

        self._expiration_dts = expiration_dts

    @property
    def name(self):
        """Gets the name of this CustomerProperty.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this CustomerProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerProperty.

        Name  # noqa: E501

        :param name: The name of this CustomerProperty.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this CustomerProperty.  # noqa: E501

        Value  # noqa: E501

        :return: The value of this CustomerProperty.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomerProperty.

        Value  # noqa: E501

        :param value: The value of this CustomerProperty.  # noqa: E501
        :type: str
        """
        if value is not None and len(value) > 1500:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `1500`")  # noqa: E501

        self._value = value

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
        if issubclass(CustomerProperty, dict):
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
        if not isinstance(other, CustomerProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
