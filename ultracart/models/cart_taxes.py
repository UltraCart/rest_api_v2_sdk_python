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


class CartTaxes(object):
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
        'county': 'str',
        'exempt': 'bool',
        'rate': 'float'
    }

    attribute_map = {
        'county': 'county',
        'exempt': 'exempt',
        'rate': 'rate'
    }

    def __init__(self, county=None, exempt=None, rate=None):  # noqa: E501
        """CartTaxes - a model defined in Swagger"""  # noqa: E501

        self._county = None
        self._exempt = None
        self._rate = None
        self.discriminator = None

        if county is not None:
            self.county = county
        if exempt is not None:
            self.exempt = exempt
        if rate is not None:
            self.rate = rate

    @property
    def county(self):
        """Gets the county of this CartTaxes.  # noqa: E501

        Tax county if the state requires it.  # noqa: E501

        :return: The county of this CartTaxes.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this CartTaxes.

        Tax county if the state requires it.  # noqa: E501

        :param county: The county of this CartTaxes.  # noqa: E501
        :type: str
        """
        if county is not None and len(county) > 32:
            raise ValueError("Invalid value for `county`, length must be less than or equal to `32`")  # noqa: E501

        self._county = county

    @property
    def exempt(self):
        """Gets the exempt of this CartTaxes.  # noqa: E501

        True if tax exempt  # noqa: E501

        :return: The exempt of this CartTaxes.  # noqa: E501
        :rtype: bool
        """
        return self._exempt

    @exempt.setter
    def exempt(self, exempt):
        """Sets the exempt of this CartTaxes.

        True if tax exempt  # noqa: E501

        :param exempt: The exempt of this CartTaxes.  # noqa: E501
        :type: bool
        """

        self._exempt = exempt

    @property
    def rate(self):
        """Gets the rate of this CartTaxes.  # noqa: E501

        Tax rate  # noqa: E501

        :return: The rate of this CartTaxes.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this CartTaxes.

        Tax rate  # noqa: E501

        :param rate: The rate of this CartTaxes.  # noqa: E501
        :type: float
        """

        self._rate = rate

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
        if issubclass(CartTaxes, dict):
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
        if not isinstance(other, CartTaxes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other