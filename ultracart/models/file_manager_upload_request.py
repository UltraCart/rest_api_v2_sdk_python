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


class FileManagerUploadRequest(object):
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
        'filename': 'str',
        'key': 'str',
        'parent_storefront_fs_directory_oid': 'int'
    }

    attribute_map = {
        'filename': 'filename',
        'key': 'key',
        'parent_storefront_fs_directory_oid': 'parent_storefront_fs_directory_oid'
    }

    def __init__(self, filename=None, key=None, parent_storefront_fs_directory_oid=None):  # noqa: E501
        """FileManagerUploadRequest - a model defined in Swagger"""  # noqa: E501

        self._filename = None
        self._key = None
        self._parent_storefront_fs_directory_oid = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if key is not None:
            self.key = key
        if parent_storefront_fs_directory_oid is not None:
            self.parent_storefront_fs_directory_oid = parent_storefront_fs_directory_oid

    @property
    def filename(self):
        """Gets the filename of this FileManagerUploadRequest.  # noqa: E501


        :return: The filename of this FileManagerUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this FileManagerUploadRequest.


        :param filename: The filename of this FileManagerUploadRequest.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def key(self):
        """Gets the key of this FileManagerUploadRequest.  # noqa: E501


        :return: The key of this FileManagerUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FileManagerUploadRequest.


        :param key: The key of this FileManagerUploadRequest.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def parent_storefront_fs_directory_oid(self):
        """Gets the parent_storefront_fs_directory_oid of this FileManagerUploadRequest.  # noqa: E501


        :return: The parent_storefront_fs_directory_oid of this FileManagerUploadRequest.  # noqa: E501
        :rtype: int
        """
        return self._parent_storefront_fs_directory_oid

    @parent_storefront_fs_directory_oid.setter
    def parent_storefront_fs_directory_oid(self, parent_storefront_fs_directory_oid):
        """Sets the parent_storefront_fs_directory_oid of this FileManagerUploadRequest.


        :param parent_storefront_fs_directory_oid: The parent_storefront_fs_directory_oid of this FileManagerUploadRequest.  # noqa: E501
        :type: int
        """

        self._parent_storefront_fs_directory_oid = parent_storefront_fs_directory_oid

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
        if issubclass(FileManagerUploadRequest, dict):
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
        if not isinstance(other, FileManagerUploadRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other