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


class CouponItemSearchResultsResponse(object):
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
        'search_results': 'list[CouponItemSearchResult]',
        'success': 'bool',
        'warning': 'Warning'
    }

    attribute_map = {
        'error': 'error',
        'metadata': 'metadata',
        'search_results': 'search_results',
        'success': 'success',
        'warning': 'warning'
    }

    def __init__(self, error=None, metadata=None, search_results=None, success=None, warning=None):  # noqa: E501
        """CouponItemSearchResultsResponse - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._metadata = None
        self._search_results = None
        self._success = None
        self._warning = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if metadata is not None:
            self.metadata = metadata
        if search_results is not None:
            self.search_results = search_results
        if success is not None:
            self.success = success
        if warning is not None:
            self.warning = warning

    @property
    def error(self):
        """Gets the error of this CouponItemSearchResultsResponse.  # noqa: E501


        :return: The error of this CouponItemSearchResultsResponse.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this CouponItemSearchResultsResponse.


        :param error: The error of this CouponItemSearchResultsResponse.  # noqa: E501
        :type: Error
        """

        self._error = error

    @property
    def metadata(self):
        """Gets the metadata of this CouponItemSearchResultsResponse.  # noqa: E501


        :return: The metadata of this CouponItemSearchResultsResponse.  # noqa: E501
        :rtype: ResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CouponItemSearchResultsResponse.


        :param metadata: The metadata of this CouponItemSearchResultsResponse.  # noqa: E501
        :type: ResponseMetadata
        """

        self._metadata = metadata

    @property
    def search_results(self):
        """Gets the search_results of this CouponItemSearchResultsResponse.  # noqa: E501

        search_results  # noqa: E501

        :return: The search_results of this CouponItemSearchResultsResponse.  # noqa: E501
        :rtype: list[CouponItemSearchResult]
        """
        return self._search_results

    @search_results.setter
    def search_results(self, search_results):
        """Sets the search_results of this CouponItemSearchResultsResponse.

        search_results  # noqa: E501

        :param search_results: The search_results of this CouponItemSearchResultsResponse.  # noqa: E501
        :type: list[CouponItemSearchResult]
        """

        self._search_results = search_results

    @property
    def success(self):
        """Gets the success of this CouponItemSearchResultsResponse.  # noqa: E501

        Indicates if API call was successful  # noqa: E501

        :return: The success of this CouponItemSearchResultsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CouponItemSearchResultsResponse.

        Indicates if API call was successful  # noqa: E501

        :param success: The success of this CouponItemSearchResultsResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def warning(self):
        """Gets the warning of this CouponItemSearchResultsResponse.  # noqa: E501


        :return: The warning of this CouponItemSearchResultsResponse.  # noqa: E501
        :rtype: Warning
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this CouponItemSearchResultsResponse.


        :param warning: The warning of this CouponItemSearchResultsResponse.  # noqa: E501
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
        if issubclass(CouponItemSearchResultsResponse, dict):
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
        if not isinstance(other, CouponItemSearchResultsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other