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


class LookupRequest(object):
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
        'category': 'str',
        'matches': 'str',
        'max_hits': 'int',
        'storefront_oid': 'int',
        'subcategory': 'str'
    }

    attribute_map = {
        'category': 'category',
        'matches': 'matches',
        'max_hits': 'max_hits',
        'storefront_oid': 'storefront_oid',
        'subcategory': 'subcategory'
    }

    def __init__(self, category=None, matches=None, max_hits=None, storefront_oid=None, subcategory=None):  # noqa: E501
        """LookupRequest - a model defined in Swagger"""  # noqa: E501

        self._category = None
        self._matches = None
        self._max_hits = None
        self._storefront_oid = None
        self._subcategory = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if matches is not None:
            self.matches = matches
        if max_hits is not None:
            self.max_hits = max_hits
        if storefront_oid is not None:
            self.storefront_oid = storefront_oid
        if subcategory is not None:
            self.subcategory = subcategory

    @property
    def category(self):
        """Gets the category of this LookupRequest.  # noqa: E501


        :return: The category of this LookupRequest.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this LookupRequest.


        :param category: The category of this LookupRequest.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def matches(self):
        """Gets the matches of this LookupRequest.  # noqa: E501


        :return: The matches of this LookupRequest.  # noqa: E501
        :rtype: str
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this LookupRequest.


        :param matches: The matches of this LookupRequest.  # noqa: E501
        :type: str
        """

        self._matches = matches

    @property
    def max_hits(self):
        """Gets the max_hits of this LookupRequest.  # noqa: E501


        :return: The max_hits of this LookupRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_hits

    @max_hits.setter
    def max_hits(self, max_hits):
        """Sets the max_hits of this LookupRequest.


        :param max_hits: The max_hits of this LookupRequest.  # noqa: E501
        :type: int
        """

        self._max_hits = max_hits

    @property
    def storefront_oid(self):
        """Gets the storefront_oid of this LookupRequest.  # noqa: E501


        :return: The storefront_oid of this LookupRequest.  # noqa: E501
        :rtype: int
        """
        return self._storefront_oid

    @storefront_oid.setter
    def storefront_oid(self, storefront_oid):
        """Sets the storefront_oid of this LookupRequest.


        :param storefront_oid: The storefront_oid of this LookupRequest.  # noqa: E501
        :type: int
        """

        self._storefront_oid = storefront_oid

    @property
    def subcategory(self):
        """Gets the subcategory of this LookupRequest.  # noqa: E501


        :return: The subcategory of this LookupRequest.  # noqa: E501
        :rtype: str
        """
        return self._subcategory

    @subcategory.setter
    def subcategory(self, subcategory):
        """Sets the subcategory of this LookupRequest.


        :param subcategory: The subcategory of this LookupRequest.  # noqa: E501
        :type: str
        """

        self._subcategory = subcategory

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
        if issubclass(LookupRequest, dict):
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
        if not isinstance(other, LookupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
