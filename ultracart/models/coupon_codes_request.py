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


class CouponCodesRequest(object):
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
        'expiration_dts': 'str',
        'expiration_seconds': 'int',
        'metadata': 'ResponseMetadata',
        'quantity': 'int',
        'success': 'bool'
    }

    attribute_map = {
        'error': 'error',
        'expiration_dts': 'expiration_dts',
        'expiration_seconds': 'expiration_seconds',
        'metadata': 'metadata',
        'quantity': 'quantity',
        'success': 'success'
    }

    def __init__(self, error=None, expiration_dts=None, expiration_seconds=None, metadata=None, quantity=None, success=None):  # noqa: E501
        """CouponCodesRequest - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._expiration_dts = None
        self._expiration_seconds = None
        self._metadata = None
        self._quantity = None
        self._success = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if expiration_dts is not None:
            self.expiration_dts = expiration_dts
        if expiration_seconds is not None:
            self.expiration_seconds = expiration_seconds
        if metadata is not None:
            self.metadata = metadata
        if quantity is not None:
            self.quantity = quantity
        if success is not None:
            self.success = success

    @property
    def error(self):
        """Gets the error of this CouponCodesRequest.  # noqa: E501


        :return: The error of this CouponCodesRequest.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this CouponCodesRequest.


        :param error: The error of this CouponCodesRequest.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def expiration_dts(self):
        """Gets the expiration_dts of this CouponCodesRequest.  # noqa: E501

        Expiration Date  # noqa: E501

        :return: The expiration_dts of this CouponCodesRequest.  # noqa: E501
        :rtype: str
        """
        return self._expiration_dts

    @expiration_dts.setter
    def expiration_dts(self, expiration_dts):
        """Sets the expiration_dts of this CouponCodesRequest.

        Expiration Date  # noqa: E501

        :param expiration_dts: The expiration_dts of this CouponCodesRequest.  # noqa: E501
        :type: str
        """

        self._expiration_dts = expiration_dts

    @property
    def expiration_seconds(self):
        """Gets the expiration_seconds of this CouponCodesRequest.  # noqa: E501

        Expiration seconds  # noqa: E501

        :return: The expiration_seconds of this CouponCodesRequest.  # noqa: E501
        :rtype: int
        """
        return self._expiration_seconds

    @expiration_seconds.setter
    def expiration_seconds(self, expiration_seconds):
        """Sets the expiration_seconds of this CouponCodesRequest.

        Expiration seconds  # noqa: E501

        :param expiration_seconds: The expiration_seconds of this CouponCodesRequest.  # noqa: E501
        :type: int
        """

        self._expiration_seconds = expiration_seconds

    @property
    def metadata(self):
        """Gets the metadata of this CouponCodesRequest.  # noqa: E501


        :return: The metadata of this CouponCodesRequest.  # noqa: E501
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CouponCodesRequest.


        :param metadata: The metadata of this CouponCodesRequest.  # noqa: E501
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def quantity(self):
        """Gets the quantity of this CouponCodesRequest.  # noqa: E501

        Quantity  # noqa: E501

        :return: The quantity of this CouponCodesRequest.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CouponCodesRequest.

        Quantity  # noqa: E501

        :param quantity: The quantity of this CouponCodesRequest.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def success(self):
        """Gets the success of this CouponCodesRequest.  # noqa: E501

        Indicates if API call was successful  # noqa: E501

        :return: The success of this CouponCodesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CouponCodesRequest.

        Indicates if API call was successful  # noqa: E501

        :param success: The success of this CouponCodesRequest.  # noqa: E501
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
        if issubclass(CouponCodesRequest, dict):
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
        if not isinstance(other, CouponCodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
