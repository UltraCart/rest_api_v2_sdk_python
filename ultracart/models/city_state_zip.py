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


class CityStateZip(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, city=None, error=None, state=None, valid_zip=None, zip=None):
        """
        CityStateZip - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'city': 'str',
            'error': 'str',
            'state': 'str',
            'valid_zip': 'bool',
            'zip': 'str'
        }

        self.attribute_map = {
            'city': 'city',
            'error': 'error',
            'state': 'state',
            'valid_zip': 'validZip',
            'zip': 'zip'
        }

        self._city = city
        self._error = error
        self._state = state
        self._valid_zip = valid_zip
        self._zip = zip

    @property
    def city(self):
        """
        Gets the city of this CityStateZip.


        :return: The city of this CityStateZip.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this CityStateZip.


        :param city: The city of this CityStateZip.
        :type: str
        """

        self._city = city

    @property
    def error(self):
        """
        Gets the error of this CityStateZip.


        :return: The error of this CityStateZip.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this CityStateZip.


        :param error: The error of this CityStateZip.
        :type: str
        """

        self._error = error

    @property
    def state(self):
        """
        Gets the state of this CityStateZip.


        :return: The state of this CityStateZip.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this CityStateZip.


        :param state: The state of this CityStateZip.
        :type: str
        """

        self._state = state

    @property
    def valid_zip(self):
        """
        Gets the valid_zip of this CityStateZip.


        :return: The valid_zip of this CityStateZip.
        :rtype: bool
        """
        return self._valid_zip

    @valid_zip.setter
    def valid_zip(self, valid_zip):
        """
        Sets the valid_zip of this CityStateZip.


        :param valid_zip: The valid_zip of this CityStateZip.
        :type: bool
        """

        self._valid_zip = valid_zip

    @property
    def zip(self):
        """
        Gets the zip of this CityStateZip.


        :return: The zip of this CityStateZip.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """
        Sets the zip of this CityStateZip.


        :param zip: The zip of this CityStateZip.
        :type: str
        """

        self._zip = zip

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
