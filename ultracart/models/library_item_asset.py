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


class LibraryItemAsset(object):
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
        'mime_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'mime_type': 'mime_type',
        'url': 'url'
    }

    def __init__(self, mime_type=None, url=None):  # noqa: E501
        """LibraryItemAsset - a model defined in Swagger"""  # noqa: E501

        self._mime_type = None
        self._url = None
        self.discriminator = None

        if mime_type is not None:
            self.mime_type = mime_type
        if url is not None:
            self.url = url

    @property
    def mime_type(self):
        """Gets the mime_type of this LibraryItemAsset.  # noqa: E501


        :return: The mime_type of this LibraryItemAsset.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this LibraryItemAsset.


        :param mime_type: The mime_type of this LibraryItemAsset.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def url(self):
        """Gets the url of this LibraryItemAsset.  # noqa: E501


        :return: The url of this LibraryItemAsset.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LibraryItemAsset.


        :param url: The url of this LibraryItemAsset.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(LibraryItemAsset, dict):
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
        if not isinstance(other, LibraryItemAsset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
