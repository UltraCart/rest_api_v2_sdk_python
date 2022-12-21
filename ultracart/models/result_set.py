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


class ResultSet(object):
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
        'count': 'int',
        'limit': 'int',
        'more': 'bool',
        'next_offset': 'int',
        'offset': 'int',
        'total_records': 'int'
    }

    attribute_map = {
        'count': 'count',
        'limit': 'limit',
        'more': 'more',
        'next_offset': 'next_offset',
        'offset': 'offset',
        'total_records': 'total_records'
    }

    def __init__(self, count=None, limit=None, more=None, next_offset=None, offset=None, total_records=None):  # noqa: E501
        """ResultSet - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._limit = None
        self._more = None
        self._next_offset = None
        self._offset = None
        self._total_records = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if limit is not None:
            self.limit = limit
        if more is not None:
            self.more = more
        if next_offset is not None:
            self.next_offset = next_offset
        if offset is not None:
            self.offset = offset
        if total_records is not None:
            self.total_records = total_records

    @property
    def count(self):
        """Gets the count of this ResultSet.  # noqa: E501

        Number of results in this set  # noqa: E501

        :return: The count of this ResultSet.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ResultSet.

        Number of results in this set  # noqa: E501

        :param count: The count of this ResultSet.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def limit(self):
        """Gets the limit of this ResultSet.  # noqa: E501

        Maximum number of results that can be returned in a set  # noqa: E501

        :return: The limit of this ResultSet.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ResultSet.

        Maximum number of results that can be returned in a set  # noqa: E501

        :param limit: The limit of this ResultSet.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def more(self):
        """Gets the more of this ResultSet.  # noqa: E501

        True if there are more results to query  # noqa: E501

        :return: The more of this ResultSet.  # noqa: E501
        :rtype: bool
        """
        return self._more

    @more.setter
    def more(self, more):
        """Sets the more of this ResultSet.

        True if there are more results to query  # noqa: E501

        :param more: The more of this ResultSet.  # noqa: E501
        :type: bool
        """

        self._more = more

    @property
    def next_offset(self):
        """Gets the next_offset of this ResultSet.  # noqa: E501

        The next offset that you should query to retrieve more results  # noqa: E501

        :return: The next_offset of this ResultSet.  # noqa: E501
        :rtype: int
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        """Sets the next_offset of this ResultSet.

        The next offset that you should query to retrieve more results  # noqa: E501

        :param next_offset: The next_offset of this ResultSet.  # noqa: E501
        :type: int
        """

        self._next_offset = next_offset

    @property
    def offset(self):
        """Gets the offset of this ResultSet.  # noqa: E501

        Offset of this result set (zero based)  # noqa: E501

        :return: The offset of this ResultSet.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ResultSet.

        Offset of this result set (zero based)  # noqa: E501

        :param offset: The offset of this ResultSet.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def total_records(self):
        """Gets the total_records of this ResultSet.  # noqa: E501

        The total number of records in the result set.  May be null if the number is not known and the client should continue iterating as long as more is true.  # noqa: E501

        :return: The total_records of this ResultSet.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this ResultSet.

        The total number of records in the result set.  May be null if the number is not known and the client should continue iterating as long as more is true.  # noqa: E501

        :param total_records: The total_records of this ResultSet.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

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
        if issubclass(ResultSet, dict):
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
        if not isinstance(other, ResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other