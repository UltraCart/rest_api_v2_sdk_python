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


class ItemChargebackAddendum(object):
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
        'chargeback_addendum_oid': 'int',
        'description': 'str',
        'file_size': 'int',
        'pages': 'int'
    }

    attribute_map = {
        'chargeback_addendum_oid': 'chargeback_addendum_oid',
        'description': 'description',
        'file_size': 'file_size',
        'pages': 'pages'
    }

    def __init__(self, chargeback_addendum_oid=None, description=None, file_size=None, pages=None):  # noqa: E501
        """ItemChargebackAddendum - a model defined in Swagger"""  # noqa: E501

        self._chargeback_addendum_oid = None
        self._description = None
        self._file_size = None
        self._pages = None
        self.discriminator = None

        if chargeback_addendum_oid is not None:
            self.chargeback_addendum_oid = chargeback_addendum_oid
        if description is not None:
            self.description = description
        if file_size is not None:
            self.file_size = file_size
        if pages is not None:
            self.pages = pages

    @property
    def chargeback_addendum_oid(self):
        """Gets the chargeback_addendum_oid of this ItemChargebackAddendum.  # noqa: E501

        Chargeback addendum object identifier  # noqa: E501

        :return: The chargeback_addendum_oid of this ItemChargebackAddendum.  # noqa: E501
        :rtype: int
        """
        return self._chargeback_addendum_oid

    @chargeback_addendum_oid.setter
    def chargeback_addendum_oid(self, chargeback_addendum_oid):
        """Sets the chargeback_addendum_oid of this ItemChargebackAddendum.

        Chargeback addendum object identifier  # noqa: E501

        :param chargeback_addendum_oid: The chargeback_addendum_oid of this ItemChargebackAddendum.  # noqa: E501
        :type: int
        """

        self._chargeback_addendum_oid = chargeback_addendum_oid

    @property
    def description(self):
        """Gets the description of this ItemChargebackAddendum.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this ItemChargebackAddendum.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemChargebackAddendum.

        Description  # noqa: E501

        :param description: The description of this ItemChargebackAddendum.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file_size(self):
        """Gets the file_size of this ItemChargebackAddendum.  # noqa: E501

        Size of the file  # noqa: E501

        :return: The file_size of this ItemChargebackAddendum.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this ItemChargebackAddendum.

        Size of the file  # noqa: E501

        :param file_size: The file_size of this ItemChargebackAddendum.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def pages(self):
        """Gets the pages of this ItemChargebackAddendum.  # noqa: E501

        Number of pages  # noqa: E501

        :return: The pages of this ItemChargebackAddendum.  # noqa: E501
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this ItemChargebackAddendum.

        Number of pages  # noqa: E501

        :param pages: The pages of this ItemChargebackAddendum.  # noqa: E501
        :type: int
        """

        self._pages = pages

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
        if issubclass(ItemChargebackAddendum, dict):
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
        if not isinstance(other, ItemChargebackAddendum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
