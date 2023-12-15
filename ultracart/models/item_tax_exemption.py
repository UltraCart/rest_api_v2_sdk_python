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


class ItemTaxExemption(object):
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
        'city': 'str',
        'country_code': 'str',
        'county': 'str',
        'postal_code': 'str',
        'state_code': 'str'
    }

    attribute_map = {
        'city': 'city',
        'country_code': 'country_code',
        'county': 'county',
        'postal_code': 'postal_code',
        'state_code': 'state_code'
    }

    def __init__(self, city=None, country_code=None, county=None, postal_code=None, state_code=None):  # noqa: E501
        """ItemTaxExemption - a model defined in Swagger"""  # noqa: E501

        self._city = None
        self._country_code = None
        self._county = None
        self._postal_code = None
        self._state_code = None
        self.discriminator = None

        if city is not None:
            self.city = city
        if country_code is not None:
            self.country_code = country_code
        if county is not None:
            self.county = county
        if postal_code is not None:
            self.postal_code = postal_code
        if state_code is not None:
            self.state_code = state_code

    @property
    def city(self):
        """Gets the city of this ItemTaxExemption.  # noqa: E501

        City  # noqa: E501

        :return: The city of this ItemTaxExemption.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ItemTaxExemption.

        City  # noqa: E501

        :param city: The city of this ItemTaxExemption.  # noqa: E501
        :type: str
        """
        if city is not None and len(city) > 32:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `32`")  # noqa: E501

        self._city = city

    @property
    def country_code(self):
        """Gets the country_code of this ItemTaxExemption.  # noqa: E501

        Country code (ISO-3166 two letter)  # noqa: E501

        :return: The country_code of this ItemTaxExemption.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this ItemTaxExemption.

        Country code (ISO-3166 two letter)  # noqa: E501

        :param country_code: The country_code of this ItemTaxExemption.  # noqa: E501
        :type: str
        """
        if country_code is not None and len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `2`")  # noqa: E501

        self._country_code = country_code

    @property
    def county(self):
        """Gets the county of this ItemTaxExemption.  # noqa: E501

        County  # noqa: E501

        :return: The county of this ItemTaxExemption.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this ItemTaxExemption.

        County  # noqa: E501

        :param county: The county of this ItemTaxExemption.  # noqa: E501
        :type: str
        """
        if county is not None and len(county) > 32:
            raise ValueError("Invalid value for `county`, length must be less than or equal to `32`")  # noqa: E501

        self._county = county

    @property
    def postal_code(self):
        """Gets the postal_code of this ItemTaxExemption.  # noqa: E501

        Postal code  # noqa: E501

        :return: The postal_code of this ItemTaxExemption.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ItemTaxExemption.

        Postal code  # noqa: E501

        :param postal_code: The postal_code of this ItemTaxExemption.  # noqa: E501
        :type: str
        """
        if postal_code is not None and len(postal_code) > 20:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `20`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def state_code(self):
        """Gets the state_code of this ItemTaxExemption.  # noqa: E501

        State code  # noqa: E501

        :return: The state_code of this ItemTaxExemption.  # noqa: E501
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """Sets the state_code of this ItemTaxExemption.

        State code  # noqa: E501

        :param state_code: The state_code of this ItemTaxExemption.  # noqa: E501
        :type: str
        """
        if state_code is not None and len(state_code) > 32:
            raise ValueError("Invalid value for `state_code`, length must be less than or equal to `32`")  # noqa: E501

        self._state_code = state_code

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
        if issubclass(ItemTaxExemption, dict):
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
        if not isinstance(other, ItemTaxExemption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
