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


class ReportDryRunQueryResult(object):
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
        'error_message': 'str',
        'total_bytes_processed': 'int'
    }

    attribute_map = {
        'error_message': 'error_message',
        'total_bytes_processed': 'total_bytes_processed'
    }

    def __init__(self, error_message=None, total_bytes_processed=None):  # noqa: E501
        """ReportDryRunQueryResult - a model defined in Swagger"""  # noqa: E501

        self._error_message = None
        self._total_bytes_processed = None
        self.discriminator = None

        if error_message is not None:
            self.error_message = error_message
        if total_bytes_processed is not None:
            self.total_bytes_processed = total_bytes_processed

    @property
    def error_message(self):
        """Gets the error_message of this ReportDryRunQueryResult.  # noqa: E501


        :return: The error_message of this ReportDryRunQueryResult.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ReportDryRunQueryResult.


        :param error_message: The error_message of this ReportDryRunQueryResult.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def total_bytes_processed(self):
        """Gets the total_bytes_processed of this ReportDryRunQueryResult.  # noqa: E501


        :return: The total_bytes_processed of this ReportDryRunQueryResult.  # noqa: E501
        :rtype: int
        """
        return self._total_bytes_processed

    @total_bytes_processed.setter
    def total_bytes_processed(self, total_bytes_processed):
        """Sets the total_bytes_processed of this ReportDryRunQueryResult.


        :param total_bytes_processed: The total_bytes_processed of this ReportDryRunQueryResult.  # noqa: E501
        :type: int
        """

        self._total_bytes_processed = total_bytes_processed

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
        if issubclass(ReportDryRunQueryResult, dict):
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
        if not isinstance(other, ReportDryRunQueryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
