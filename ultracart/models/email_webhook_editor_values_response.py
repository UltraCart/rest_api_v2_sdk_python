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


class EmailWebhookEditorValuesResponse(object):
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
        'available_expansions': 'list[str]',
        'available_tokens': 'list[str]',
        'error': 'Error',
        'metadata': 'ResponseMetadata',
        'rest_object_type': 'str',
        'success': 'bool',
        'warning': 'Warning'
    }

    attribute_map = {
        'available_expansions': 'available_expansions',
        'available_tokens': 'available_tokens',
        'error': 'error',
        'metadata': 'metadata',
        'rest_object_type': 'rest_object_type',
        'success': 'success',
        'warning': 'warning'
    }

    def __init__(self, available_expansions=None, available_tokens=None, error=None, metadata=None, rest_object_type=None, success=None, warning=None):  # noqa: E501
        """EmailWebhookEditorValuesResponse - a model defined in Swagger"""  # noqa: E501

        self._available_expansions = None
        self._available_tokens = None
        self._error = None
        self._metadata = None
        self._rest_object_type = None
        self._success = None
        self._warning = None
        self.discriminator = None

        if available_expansions is not None:
            self.available_expansions = available_expansions
        if available_tokens is not None:
            self.available_tokens = available_tokens
        if error is not None:
            self.error = error
        if metadata is not None:
            self.metadata = metadata
        if rest_object_type is not None:
            self.rest_object_type = rest_object_type
        if success is not None:
            self.success = success
        if warning is not None:
            self.warning = warning

    @property
    def available_expansions(self):
        """Gets the available_expansions of this EmailWebhookEditorValuesResponse.  # noqa: E501


        :return: The available_expansions of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_expansions

    @available_expansions.setter
    def available_expansions(self, available_expansions):
        """Sets the available_expansions of this EmailWebhookEditorValuesResponse.


        :param available_expansions: The available_expansions of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :type: list[str]
        """

        self._available_expansions = available_expansions

    @property
    def available_tokens(self):
        """Gets the available_tokens of this EmailWebhookEditorValuesResponse.  # noqa: E501


        :return: The available_tokens of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_tokens

    @available_tokens.setter
    def available_tokens(self, available_tokens):
        """Sets the available_tokens of this EmailWebhookEditorValuesResponse.


        :param available_tokens: The available_tokens of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :type: list[str]
        """

        self._available_tokens = available_tokens

    @property
    def error(self):
        """Gets the error of this EmailWebhookEditorValuesResponse.  # noqa: E501


        :return: The error of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EmailWebhookEditorValuesResponse.


        :param error: The error of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def metadata(self):
        """Gets the metadata of this EmailWebhookEditorValuesResponse.  # noqa: E501


        :return: The metadata of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this EmailWebhookEditorValuesResponse.


        :param metadata: The metadata of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def rest_object_type(self):
        """Gets the rest_object_type of this EmailWebhookEditorValuesResponse.  # noqa: E501


        :return: The rest_object_type of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :rtype: str
        """
        return self._rest_object_type

    @rest_object_type.setter
    def rest_object_type(self, rest_object_type):
        """Sets the rest_object_type of this EmailWebhookEditorValuesResponse.


        :param rest_object_type: The rest_object_type of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :type: str
        """

        self._rest_object_type = rest_object_type

    @property
    def success(self):
        """Gets the success of this EmailWebhookEditorValuesResponse.  # noqa: E501

        Indicates if API call was successful  # noqa: E501

        :return: The success of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this EmailWebhookEditorValuesResponse.

        Indicates if API call was successful  # noqa: E501

        :param success: The success of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def warning(self):
        """Gets the warning of this EmailWebhookEditorValuesResponse.  # noqa: E501


        :return: The warning of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :rtype: Warning
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this EmailWebhookEditorValuesResponse.


        :param warning: The warning of this EmailWebhookEditorValuesResponse.  # noqa: E501
        :type: Warning
        """

        self._warning = warning

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
        if issubclass(EmailWebhookEditorValuesResponse, dict):
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
        if not isinstance(other, EmailWebhookEditorValuesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
