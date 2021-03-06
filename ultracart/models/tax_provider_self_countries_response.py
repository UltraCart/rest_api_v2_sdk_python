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


class TaxProviderSelfCountriesResponse(object):
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
        'countries': 'list[TaxCountryCode]'
    }

    attribute_map = {
        'countries': 'countries'
    }

    def __init__(self, countries=None):  # noqa: E501
        """TaxProviderSelfCountriesResponse - a model defined in Swagger"""  # noqa: E501

        self._countries = None
        self.discriminator = None

        if countries is not None:
            self.countries = countries

    @property
    def countries(self):
        """Gets the countries of this TaxProviderSelfCountriesResponse.  # noqa: E501

        countries  # noqa: E501

        :return: The countries of this TaxProviderSelfCountriesResponse.  # noqa: E501
        :rtype: list[TaxCountryCode]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this TaxProviderSelfCountriesResponse.

        countries  # noqa: E501

        :param countries: The countries of this TaxProviderSelfCountriesResponse.  # noqa: E501
        :type: list[TaxCountryCode]
        """

        self._countries = countries

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
        if issubclass(TaxProviderSelfCountriesResponse, dict):
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
        if not isinstance(other, TaxProviderSelfCountriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
