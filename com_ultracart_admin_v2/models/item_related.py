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


class ItemRelated(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, no_system_calculated_related_items=None, not_relatable=None, related_items=None):
        """
        ItemRelated - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'no_system_calculated_related_items': 'bool',
            'not_relatable': 'bool',
            'related_items': 'list[ItemRelatedItem]'
        }

        self.attribute_map = {
            'no_system_calculated_related_items': 'no_system_calculated_related_items',
            'not_relatable': 'not_relatable',
            'related_items': 'related_items'
        }

        self._no_system_calculated_related_items = no_system_calculated_related_items
        self._not_relatable = not_relatable
        self._related_items = related_items

    @property
    def no_system_calculated_related_items(self):
        """
        Gets the no_system_calculated_related_items of this ItemRelated.
        True to suppress system calculated relationships

        :return: The no_system_calculated_related_items of this ItemRelated.
        :rtype: bool
        """
        return self._no_system_calculated_related_items

    @no_system_calculated_related_items.setter
    def no_system_calculated_related_items(self, no_system_calculated_related_items):
        """
        Sets the no_system_calculated_related_items of this ItemRelated.
        True to suppress system calculated relationships

        :param no_system_calculated_related_items: The no_system_calculated_related_items of this ItemRelated.
        :type: bool
        """

        self._no_system_calculated_related_items = no_system_calculated_related_items

    @property
    def not_relatable(self):
        """
        Gets the not_relatable of this ItemRelated.
        Not relatable

        :return: The not_relatable of this ItemRelated.
        :rtype: bool
        """
        return self._not_relatable

    @not_relatable.setter
    def not_relatable(self, not_relatable):
        """
        Sets the not_relatable of this ItemRelated.
        Not relatable

        :param not_relatable: The not_relatable of this ItemRelated.
        :type: bool
        """

        self._not_relatable = not_relatable

    @property
    def related_items(self):
        """
        Gets the related_items of this ItemRelated.
        Related items

        :return: The related_items of this ItemRelated.
        :rtype: list[ItemRelatedItem]
        """
        return self._related_items

    @related_items.setter
    def related_items(self, related_items):
        """
        Sets the related_items of this ItemRelated.
        Related items

        :param related_items: The related_items of this ItemRelated.
        :type: list[ItemRelatedItem]
        """

        self._related_items = related_items

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
