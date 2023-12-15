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


class CustomerAttachment(object):
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
        'customer_profile_attachment_oid': 'int',
        'description': 'str',
        'file_name': 'str',
        'mime_type': 'str',
        'upload_dts': 'str'
    }

    attribute_map = {
        'customer_profile_attachment_oid': 'customer_profile_attachment_oid',
        'description': 'description',
        'file_name': 'file_name',
        'mime_type': 'mime_type',
        'upload_dts': 'upload_dts'
    }

    def __init__(self, customer_profile_attachment_oid=None, description=None, file_name=None, mime_type=None, upload_dts=None):  # noqa: E501
        """CustomerAttachment - a model defined in Swagger"""  # noqa: E501

        self._customer_profile_attachment_oid = None
        self._description = None
        self._file_name = None
        self._mime_type = None
        self._upload_dts = None
        self.discriminator = None

        if customer_profile_attachment_oid is not None:
            self.customer_profile_attachment_oid = customer_profile_attachment_oid
        if description is not None:
            self.description = description
        if file_name is not None:
            self.file_name = file_name
        if mime_type is not None:
            self.mime_type = mime_type
        if upload_dts is not None:
            self.upload_dts = upload_dts

    @property
    def customer_profile_attachment_oid(self):
        """Gets the customer_profile_attachment_oid of this CustomerAttachment.  # noqa: E501

        Attachment identifier  # noqa: E501

        :return: The customer_profile_attachment_oid of this CustomerAttachment.  # noqa: E501
        :rtype: int
        """
        return self._customer_profile_attachment_oid

    @customer_profile_attachment_oid.setter
    def customer_profile_attachment_oid(self, customer_profile_attachment_oid):
        """Sets the customer_profile_attachment_oid of this CustomerAttachment.

        Attachment identifier  # noqa: E501

        :param customer_profile_attachment_oid: The customer_profile_attachment_oid of this CustomerAttachment.  # noqa: E501
        :type: int
        """

        self._customer_profile_attachment_oid = customer_profile_attachment_oid

    @property
    def description(self):
        """Gets the description of this CustomerAttachment.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this CustomerAttachment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomerAttachment.

        Description  # noqa: E501

        :param description: The description of this CustomerAttachment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file_name(self):
        """Gets the file_name of this CustomerAttachment.  # noqa: E501

        File name  # noqa: E501

        :return: The file_name of this CustomerAttachment.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CustomerAttachment.

        File name  # noqa: E501

        :param file_name: The file_name of this CustomerAttachment.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def mime_type(self):
        """Gets the mime_type of this CustomerAttachment.  # noqa: E501

        Mime typoe  # noqa: E501

        :return: The mime_type of this CustomerAttachment.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this CustomerAttachment.

        Mime typoe  # noqa: E501

        :param mime_type: The mime_type of this CustomerAttachment.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def upload_dts(self):
        """Gets the upload_dts of this CustomerAttachment.  # noqa: E501

        Upload date/time  # noqa: E501

        :return: The upload_dts of this CustomerAttachment.  # noqa: E501
        :rtype: str
        """
        return self._upload_dts

    @upload_dts.setter
    def upload_dts(self, upload_dts):
        """Sets the upload_dts of this CustomerAttachment.

        Upload date/time  # noqa: E501

        :param upload_dts: The upload_dts of this CustomerAttachment.  # noqa: E501
        :type: str
        """

        self._upload_dts = upload_dts

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
        if issubclass(CustomerAttachment, dict):
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
        if not isinstance(other, CustomerAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
