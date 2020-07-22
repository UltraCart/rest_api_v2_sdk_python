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


class ItemDigitalItem(object):
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
        'creation_dts': 'str',
        'description': 'str',
        'file_size': 'int',
        'mime_type': 'str',
        'original_filename': 'str'
    }

    attribute_map = {
        'creation_dts': 'creation_dts',
        'description': 'description',
        'file_size': 'file_size',
        'mime_type': 'mime_type',
        'original_filename': 'original_filename'
    }

    def __init__(self, creation_dts=None, description=None, file_size=None, mime_type=None, original_filename=None):  # noqa: E501
        """ItemDigitalItem - a model defined in Swagger"""  # noqa: E501

        self._creation_dts = None
        self._description = None
        self._file_size = None
        self._mime_type = None
        self._original_filename = None
        self.discriminator = None

        if creation_dts is not None:
            self.creation_dts = creation_dts
        if description is not None:
            self.description = description
        if file_size is not None:
            self.file_size = file_size
        if mime_type is not None:
            self.mime_type = mime_type
        if original_filename is not None:
            self.original_filename = original_filename

    @property
    def creation_dts(self):
        """Gets the creation_dts of this ItemDigitalItem.  # noqa: E501

        File creation date  # noqa: E501

        :return: The creation_dts of this ItemDigitalItem.  # noqa: E501
        :rtype: str
        """
        return self._creation_dts

    @creation_dts.setter
    def creation_dts(self, creation_dts):
        """Sets the creation_dts of this ItemDigitalItem.

        File creation date  # noqa: E501

        :param creation_dts: The creation_dts of this ItemDigitalItem.  # noqa: E501
        :type: str
        """

        self._creation_dts = creation_dts

    @property
    def description(self):
        """Gets the description of this ItemDigitalItem.  # noqa: E501

        Description of the digital item  # noqa: E501

        :return: The description of this ItemDigitalItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemDigitalItem.

        Description of the digital item  # noqa: E501

        :param description: The description of this ItemDigitalItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def file_size(self):
        """Gets the file_size of this ItemDigitalItem.  # noqa: E501

        File size  # noqa: E501

        :return: The file_size of this ItemDigitalItem.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this ItemDigitalItem.

        File size  # noqa: E501

        :param file_size: The file_size of this ItemDigitalItem.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def mime_type(self):
        """Gets the mime_type of this ItemDigitalItem.  # noqa: E501

        Mime type associated with the file  # noqa: E501

        :return: The mime_type of this ItemDigitalItem.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this ItemDigitalItem.

        Mime type associated with the file  # noqa: E501

        :param mime_type: The mime_type of this ItemDigitalItem.  # noqa: E501
        :type: str
        """
        if mime_type is not None and len(mime_type) > 100:
            raise ValueError("Invalid value for `mime_type`, length must be less than or equal to `100`")  # noqa: E501

        self._mime_type = mime_type

    @property
    def original_filename(self):
        """Gets the original_filename of this ItemDigitalItem.  # noqa: E501

        Original filename  # noqa: E501

        :return: The original_filename of this ItemDigitalItem.  # noqa: E501
        :rtype: str
        """
        return self._original_filename

    @original_filename.setter
    def original_filename(self, original_filename):
        """Sets the original_filename of this ItemDigitalItem.

        Original filename  # noqa: E501

        :param original_filename: The original_filename of this ItemDigitalItem.  # noqa: E501
        :type: str
        """
        if original_filename is not None and len(original_filename) > 250:
            raise ValueError("Invalid value for `original_filename`, length must be less than or equal to `250`")  # noqa: E501

        self._original_filename = original_filename

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
        if issubclass(ItemDigitalItem, dict):
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
        if not isinstance(other, ItemDigitalItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
