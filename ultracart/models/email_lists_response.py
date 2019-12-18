# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EmailListsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'error': 'Error',
        'lists': 'list[EmailList]',
        'metadata': 'ResponseMetadata',
        'success': 'bool'
    }

    attribute_map = {
        'error': 'error',
        'lists': 'lists',
        'metadata': 'metadata',
        'success': 'success'
    }

    def __init__(self, error=None, lists=None, metadata=None, success=None):
        """
        EmailListsResponse - a model defined in Swagger
        """

        self._error = None
        self._lists = None
        self._metadata = None
        self._success = None
        self.discriminator = None

        if error is not None:
          self.error = error
        if lists is not None:
          self.lists = lists
        if metadata is not None:
          self.metadata = metadata
        if success is not None:
          self.success = success

    @property
    def error(self):
        """
        Gets the error of this EmailListsResponse.

        :return: The error of this EmailListsResponse.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this EmailListsResponse.

        :param error: The error of this EmailListsResponse.
        :type: Error
        """

        self._error = error

    @property
    def lists(self):
        """
        Gets the lists of this EmailListsResponse.

        :return: The lists of this EmailListsResponse.
        :rtype: list[EmailList]
        """
        return self._lists

    @lists.setter
    def lists(self, lists):
        """
        Sets the lists of this EmailListsResponse.

        :param lists: The lists of this EmailListsResponse.
        :type: list[EmailList]
        """

        self._lists = lists

    @property
    def metadata(self):
        """
        Gets the metadata of this EmailListsResponse.

        :return: The metadata of this EmailListsResponse.
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this EmailListsResponse.

        :param metadata: The metadata of this EmailListsResponse.
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def success(self):
        """
        Gets the success of this EmailListsResponse.
        Indicates if API call was successful

        :return: The success of this EmailListsResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this EmailListsResponse.
        Indicates if API call was successful

        :param success: The success of this EmailListsResponse.
        :type: bool
        """

        self._success = success

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
        if not isinstance(other, EmailListsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
