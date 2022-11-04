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


class WebhookSampleRequestResponse(object):
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
        'error': 'Error',
        'metadata': 'ResponseMetadata',
        'success': 'bool',
        'warning': 'Warning',
        'webhook_sample_request': 'WebhookSampleRequest'
    }

    attribute_map = {
        'error': 'error',
        'metadata': 'metadata',
        'success': 'success',
        'warning': 'warning',
        'webhook_sample_request': 'webhook_sample_request'
    }

    def __init__(self, error=None, metadata=None, success=None, warning=None, webhook_sample_request=None):  # noqa: E501
        """WebhookSampleRequestResponse - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._metadata = None
        self._success = None
        self._warning = None
        self._webhook_sample_request = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if metadata is not None:
            self.metadata = metadata
        if success is not None:
            self.success = success
        if warning is not None:
            self.warning = warning
        if webhook_sample_request is not None:
            self.webhook_sample_request = webhook_sample_request

    @property
    def error(self):
        """Gets the error of this WebhookSampleRequestResponse.  # noqa: E501


        :return: The error of this WebhookSampleRequestResponse.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this WebhookSampleRequestResponse.


        :param error: The error of this WebhookSampleRequestResponse.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def metadata(self):
        """Gets the metadata of this WebhookSampleRequestResponse.  # noqa: E501


        :return: The metadata of this WebhookSampleRequestResponse.  # noqa: E501
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this WebhookSampleRequestResponse.


        :param metadata: The metadata of this WebhookSampleRequestResponse.  # noqa: E501
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def success(self):
        """Gets the success of this WebhookSampleRequestResponse.  # noqa: E501

        Indicates if API call was successful  # noqa: E501

        :return: The success of this WebhookSampleRequestResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this WebhookSampleRequestResponse.

        Indicates if API call was successful  # noqa: E501

        :param success: The success of this WebhookSampleRequestResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def warning(self):
        """Gets the warning of this WebhookSampleRequestResponse.  # noqa: E501


        :return: The warning of this WebhookSampleRequestResponse.  # noqa: E501
        :rtype: Warning
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this WebhookSampleRequestResponse.


        :param warning: The warning of this WebhookSampleRequestResponse.  # noqa: E501
        :type: Warning
        """

        self._warning = warning

    @property
    def webhook_sample_request(self):
        """Gets the webhook_sample_request of this WebhookSampleRequestResponse.  # noqa: E501


        :return: The webhook_sample_request of this WebhookSampleRequestResponse.  # noqa: E501
        :rtype: WebhookSampleRequest
        """
        return self._webhook_sample_request

    @webhook_sample_request.setter
    def webhook_sample_request(self, webhook_sample_request):
        """Sets the webhook_sample_request of this WebhookSampleRequestResponse.


        :param webhook_sample_request: The webhook_sample_request of this WebhookSampleRequestResponse.  # noqa: E501
        :type: WebhookSampleRequest
        """

        self._webhook_sample_request = webhook_sample_request

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
        if issubclass(WebhookSampleRequestResponse, dict):
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
        if not isinstance(other, WebhookSampleRequestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other