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


class CustomerResponse(object):
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
        'customer': 'Customer',
        'error': 'Error',
        'metadata': 'ResponseMetadata',
        'success': 'bool'
    }

    attribute_map = {
        'customer': 'customer',
        'error': 'error',
        'metadata': 'metadata',
        'success': 'success'
    }

    def __init__(self, customer=None, error=None, metadata=None, success=None):  # noqa: E501
        """CustomerResponse - a model defined in Swagger"""  # noqa: E501

        self._customer = None
        self._error = None
        self._metadata = None
        self._success = None
        self.discriminator = None

        if customer is not None:
            self.customer = customer
        if error is not None:
            self.error = error
        if metadata is not None:
            self.metadata = metadata
        if success is not None:
            self.success = success

    @property
    def customer(self):
        """Gets the customer of this CustomerResponse.  # noqa: E501


        :return: The customer of this CustomerResponse.  # noqa: E501
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this CustomerResponse.


        :param customer: The customer of this CustomerResponse.  # noqa: E501
        :type: Customer
        """

        self._customer = customer

    @property
    def error(self):
        """Gets the error of this CustomerResponse.  # noqa: E501


        :return: The error of this CustomerResponse.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this CustomerResponse.


        :param error: The error of this CustomerResponse.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def metadata(self):
        """Gets the metadata of this CustomerResponse.  # noqa: E501


        :return: The metadata of this CustomerResponse.  # noqa: E501
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CustomerResponse.


        :param metadata: The metadata of this CustomerResponse.  # noqa: E501
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def success(self):
        """Gets the success of this CustomerResponse.  # noqa: E501

        Indicates if API call was successful  # noqa: E501

        :return: The success of this CustomerResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CustomerResponse.

        Indicates if API call was successful  # noqa: E501

        :param success: The success of this CustomerResponse.  # noqa: E501
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
        if issubclass(CustomerResponse, dict):
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
        if not isinstance(other, CustomerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
