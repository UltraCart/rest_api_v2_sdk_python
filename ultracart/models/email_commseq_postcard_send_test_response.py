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


class EmailCommseqPostcardSendTestResponse(object):
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
        'back_thumbnail': 'str',
        'error': 'Error',
        'front_thumbnail': 'str',
        'metadata': 'ResponseMetadata',
        'rendered_pdf': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'back_thumbnail': 'backThumbnail',
        'error': 'error',
        'front_thumbnail': 'frontThumbnail',
        'metadata': 'metadata',
        'rendered_pdf': 'renderedPdf',
        'success': 'success'
    }

    def __init__(self, back_thumbnail=None, error=None, front_thumbnail=None, metadata=None, rendered_pdf=None, success=None):  # noqa: E501
        """EmailCommseqPostcardSendTestResponse - a model defined in Swagger"""  # noqa: E501

        self._back_thumbnail = None
        self._error = None
        self._front_thumbnail = None
        self._metadata = None
        self._rendered_pdf = None
        self._success = None
        self.discriminator = None

        if back_thumbnail is not None:
            self.back_thumbnail = back_thumbnail
        if error is not None:
            self.error = error
        if front_thumbnail is not None:
            self.front_thumbnail = front_thumbnail
        if metadata is not None:
            self.metadata = metadata
        if rendered_pdf is not None:
            self.rendered_pdf = rendered_pdf
        if success is not None:
            self.success = success

    @property
    def back_thumbnail(self):
        """Gets the back_thumbnail of this EmailCommseqPostcardSendTestResponse.  # noqa: E501


        :return: The back_thumbnail of this EmailCommseqPostcardSendTestResponse.  # noqa: E501
        :rtype: str
        """
        return self._back_thumbnail

    @back_thumbnail.setter
    def back_thumbnail(self, back_thumbnail):
        """Sets the back_thumbnail of this EmailCommseqPostcardSendTestResponse.


        :param back_thumbnail: The back_thumbnail of this EmailCommseqPostcardSendTestResponse.  # noqa: E501
        :type: str
        """

        self._back_thumbnail = back_thumbnail

    @property
    def error(self):
        """Gets the error of this EmailCommseqPostcardSendTestResponse.  # noqa: E501


        :return: The error of this EmailCommseqPostcardSendTestResponse.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EmailCommseqPostcardSendTestResponse.


        :param error: The error of this EmailCommseqPostcardSendTestResponse.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def front_thumbnail(self):
        """Gets the front_thumbnail of this EmailCommseqPostcardSendTestResponse.  # noqa: E501


        :return: The front_thumbnail of this EmailCommseqPostcardSendTestResponse.  # noqa: E501
        :rtype: str
        """
        return self._front_thumbnail

    @front_thumbnail.setter
    def front_thumbnail(self, front_thumbnail):
        """Sets the front_thumbnail of this EmailCommseqPostcardSendTestResponse.


        :param front_thumbnail: The front_thumbnail of this EmailCommseqPostcardSendTestResponse.  # noqa: E501
        :type: str
        """

        self._front_thumbnail = front_thumbnail

    @property
    def metadata(self):
        """Gets the metadata of this EmailCommseqPostcardSendTestResponse.  # noqa: E501


        :return: The metadata of this EmailCommseqPostcardSendTestResponse.  # noqa: E501
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this EmailCommseqPostcardSendTestResponse.


        :param metadata: The metadata of this EmailCommseqPostcardSendTestResponse.  # noqa: E501
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def rendered_pdf(self):
        """Gets the rendered_pdf of this EmailCommseqPostcardSendTestResponse.  # noqa: E501


        :return: The rendered_pdf of this EmailCommseqPostcardSendTestResponse.  # noqa: E501
        :rtype: str
        """
        return self._rendered_pdf

    @rendered_pdf.setter
    def rendered_pdf(self, rendered_pdf):
        """Sets the rendered_pdf of this EmailCommseqPostcardSendTestResponse.


        :param rendered_pdf: The rendered_pdf of this EmailCommseqPostcardSendTestResponse.  # noqa: E501
        :type: str
        """

        self._rendered_pdf = rendered_pdf

    @property
    def success(self):
        """Gets the success of this EmailCommseqPostcardSendTestResponse.  # noqa: E501

        Indicates if API call was successful  # noqa: E501

        :return: The success of this EmailCommseqPostcardSendTestResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this EmailCommseqPostcardSendTestResponse.

        Indicates if API call was successful  # noqa: E501

        :param success: The success of this EmailCommseqPostcardSendTestResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(EmailCommseqPostcardSendTestResponse, dict):
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
        if not isinstance(other, EmailCommseqPostcardSendTestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
