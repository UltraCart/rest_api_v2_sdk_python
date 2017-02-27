# coding: utf-8

"""
    UltraCart Rest API V2

    This is the next generation UltraCart REST API...

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Currency(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, localized=None, localized_formatted=None, value=None):
        """
        Currency - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'localized': 'float',
            'localized_formatted': 'str',
            'value': 'float'
        }

        self.attribute_map = {
            'localized': 'localized',
            'localized_formatted': 'localized_formatted',
            'value': 'value'
        }

        self._localized = localized
        self._localized_formatted = localized_formatted
        self._value = value

    @property
    def localized(self):
        """
        Gets the localized of this Currency.
        Value localized to the customer

        :return: The localized of this Currency.
        :rtype: float
        """
        return self._localized

    @localized.setter
    def localized(self, localized):
        """
        Sets the localized of this Currency.
        Value localized to the customer

        :param localized: The localized of this Currency.
        :type: float
        """

        self._localized = localized

    @property
    def localized_formatted(self):
        """
        Gets the localized_formatted of this Currency.
        Value localized and formatted for the customer

        :return: The localized_formatted of this Currency.
        :rtype: str
        """
        return self._localized_formatted

    @localized_formatted.setter
    def localized_formatted(self, localized_formatted):
        """
        Sets the localized_formatted of this Currency.
        Value localized and formatted for the customer

        :param localized_formatted: The localized_formatted of this Currency.
        :type: str
        """

        self._localized_formatted = localized_formatted

    @property
    def value(self):
        """
        Gets the value of this Currency.
        Value in base currency

        :return: The value of this Currency.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Currency.
        Value in base currency

        :param value: The value of this Currency.
        :type: float
        """

        self._value = value

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
