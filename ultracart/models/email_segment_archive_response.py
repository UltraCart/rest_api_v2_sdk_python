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


class EmailSegmentArchiveResponse(object):
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
        'metadata': 'ResponseMetadata',
        'segment_in_use': 'bool',
        'success': 'bool'
    }

    attribute_map = {
        'error': 'error',
        'metadata': 'metadata',
        'segment_in_use': 'segment_in_use',
        'success': 'success'
    }

    def __init__(self, error=None, metadata=None, segment_in_use=None, success=None):
        """
        EmailSegmentArchiveResponse - a model defined in Swagger
        """

        self._error = None
        self._metadata = None
        self._segment_in_use = None
        self._success = None
        self.discriminator = None

        if error is not None:
          self.error = error
        if metadata is not None:
          self.metadata = metadata
        if segment_in_use is not None:
          self.segment_in_use = segment_in_use
        if success is not None:
          self.success = success

    @property
    def error(self):
        """
        Gets the error of this EmailSegmentArchiveResponse.

        :return: The error of this EmailSegmentArchiveResponse.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this EmailSegmentArchiveResponse.

        :param error: The error of this EmailSegmentArchiveResponse.
        :type: Error
        """

        self._error = error

    @property
    def metadata(self):
        """
        Gets the metadata of this EmailSegmentArchiveResponse.

        :return: The metadata of this EmailSegmentArchiveResponse.
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this EmailSegmentArchiveResponse.

        :param metadata: The metadata of this EmailSegmentArchiveResponse.
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def segment_in_use(self):
        """
        Gets the segment_in_use of this EmailSegmentArchiveResponse.

        :return: The segment_in_use of this EmailSegmentArchiveResponse.
        :rtype: bool
        """
        return self._segment_in_use

    @segment_in_use.setter
    def segment_in_use(self, segment_in_use):
        """
        Sets the segment_in_use of this EmailSegmentArchiveResponse.

        :param segment_in_use: The segment_in_use of this EmailSegmentArchiveResponse.
        :type: bool
        """

        self._segment_in_use = segment_in_use

    @property
    def success(self):
        """
        Gets the success of this EmailSegmentArchiveResponse.
        Indicates if API call was successful

        :return: The success of this EmailSegmentArchiveResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this EmailSegmentArchiveResponse.
        Indicates if API call was successful

        :param success: The success of this EmailSegmentArchiveResponse.
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
        if not isinstance(other, EmailSegmentArchiveResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
