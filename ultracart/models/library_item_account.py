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


class LibraryItemAccount(object):
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
        'library_item_account_oid': 'int',
        'library_item_oid': 'int',
        'other_merchant_id': 'str'
    }

    attribute_map = {
        'library_item_account_oid': 'library_item_account_oid',
        'library_item_oid': 'library_item_oid',
        'other_merchant_id': 'other_merchant_id'
    }

    def __init__(self, library_item_account_oid=None, library_item_oid=None, other_merchant_id=None):  # noqa: E501
        """LibraryItemAccount - a model defined in Swagger"""  # noqa: E501

        self._library_item_account_oid = None
        self._library_item_oid = None
        self._other_merchant_id = None
        self.discriminator = None

        if library_item_account_oid is not None:
            self.library_item_account_oid = library_item_account_oid
        if library_item_oid is not None:
            self.library_item_oid = library_item_oid
        if other_merchant_id is not None:
            self.other_merchant_id = other_merchant_id

    @property
    def library_item_account_oid(self):
        """Gets the library_item_account_oid of this LibraryItemAccount.  # noqa: E501


        :return: The library_item_account_oid of this LibraryItemAccount.  # noqa: E501
        :rtype: int
        """
        return self._library_item_account_oid

    @library_item_account_oid.setter
    def library_item_account_oid(self, library_item_account_oid):
        """Sets the library_item_account_oid of this LibraryItemAccount.


        :param library_item_account_oid: The library_item_account_oid of this LibraryItemAccount.  # noqa: E501
        :type: int
        """

        self._library_item_account_oid = library_item_account_oid

    @property
    def library_item_oid(self):
        """Gets the library_item_oid of this LibraryItemAccount.  # noqa: E501


        :return: The library_item_oid of this LibraryItemAccount.  # noqa: E501
        :rtype: int
        """
        return self._library_item_oid

    @library_item_oid.setter
    def library_item_oid(self, library_item_oid):
        """Sets the library_item_oid of this LibraryItemAccount.


        :param library_item_oid: The library_item_oid of this LibraryItemAccount.  # noqa: E501
        :type: int
        """

        self._library_item_oid = library_item_oid

    @property
    def other_merchant_id(self):
        """Gets the other_merchant_id of this LibraryItemAccount.  # noqa: E501


        :return: The other_merchant_id of this LibraryItemAccount.  # noqa: E501
        :rtype: str
        """
        return self._other_merchant_id

    @other_merchant_id.setter
    def other_merchant_id(self, other_merchant_id):
        """Sets the other_merchant_id of this LibraryItemAccount.


        :param other_merchant_id: The other_merchant_id of this LibraryItemAccount.  # noqa: E501
        :type: str
        """

        self._other_merchant_id = other_merchant_id

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
        if issubclass(LibraryItemAccount, dict):
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
        if not isinstance(other, LibraryItemAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other