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


class ResponseMetadata(object):
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
        'payload_name': 'str',
        'result_set': 'ResultSet'
    }

    attribute_map = {
        'payload_name': 'payload_name',
        'result_set': 'result_set'
    }

    def __init__(self, payload_name=None, result_set=None):  # noqa: E501
        """ResponseMetadata - a model defined in Swagger"""  # noqa: E501

        self._payload_name = None
        self._result_set = None
        self.discriminator = None

        if payload_name is not None:
            self.payload_name = payload_name
        if result_set is not None:
            self.result_set = result_set

    @property
    def payload_name(self):
        """Gets the payload_name of this ResponseMetadata.  # noqa: E501

        Payload name  # noqa: E501

        :return: The payload_name of this ResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._payload_name

    @payload_name.setter
    def payload_name(self, payload_name):
        """Sets the payload_name of this ResponseMetadata.

        Payload name  # noqa: E501

        :param payload_name: The payload_name of this ResponseMetadata.  # noqa: E501
        :type: str
        """

        self._payload_name = payload_name

    @property
    def result_set(self):
        """Gets the result_set of this ResponseMetadata.  # noqa: E501


        :return: The result_set of this ResponseMetadata.  # noqa: E501
        :rtype: ResultSet
        """
        return self._result_set

    @result_set.setter
    def result_set(self, result_set):
        """Sets the result_set of this ResponseMetadata.


        :param result_set: The result_set of this ResponseMetadata.  # noqa: E501
        :type: ResultSet
        """

        self._result_set = result_set

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
        if issubclass(ResponseMetadata, dict):
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
        if not isinstance(other, ResponseMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
