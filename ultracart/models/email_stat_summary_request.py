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


class EmailStatSummaryRequest(object):
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
        'commseq_email_uuids': 'list[str]',
        'commseq_step_uuids': 'list[str]',
        'days': 'int'
    }

    attribute_map = {
        'commseq_email_uuids': 'commseq_email_uuids',
        'commseq_step_uuids': 'commseq_step_uuids',
        'days': 'days'
    }

    def __init__(self, commseq_email_uuids=None, commseq_step_uuids=None, days=None):  # noqa: E501
        """EmailStatSummaryRequest - a model defined in Swagger"""  # noqa: E501

        self._commseq_email_uuids = None
        self._commseq_step_uuids = None
        self._days = None
        self.discriminator = None

        if commseq_email_uuids is not None:
            self.commseq_email_uuids = commseq_email_uuids
        if commseq_step_uuids is not None:
            self.commseq_step_uuids = commseq_step_uuids
        if days is not None:
            self.days = days

    @property
    def commseq_email_uuids(self):
        """Gets the commseq_email_uuids of this EmailStatSummaryRequest.  # noqa: E501


        :return: The commseq_email_uuids of this EmailStatSummaryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._commseq_email_uuids

    @commseq_email_uuids.setter
    def commseq_email_uuids(self, commseq_email_uuids):
        """Sets the commseq_email_uuids of this EmailStatSummaryRequest.


        :param commseq_email_uuids: The commseq_email_uuids of this EmailStatSummaryRequest.  # noqa: E501
        :type: list[str]
        """

        self._commseq_email_uuids = commseq_email_uuids

    @property
    def commseq_step_uuids(self):
        """Gets the commseq_step_uuids of this EmailStatSummaryRequest.  # noqa: E501


        :return: The commseq_step_uuids of this EmailStatSummaryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._commseq_step_uuids

    @commseq_step_uuids.setter
    def commseq_step_uuids(self, commseq_step_uuids):
        """Sets the commseq_step_uuids of this EmailStatSummaryRequest.


        :param commseq_step_uuids: The commseq_step_uuids of this EmailStatSummaryRequest.  # noqa: E501
        :type: list[str]
        """

        self._commseq_step_uuids = commseq_step_uuids

    @property
    def days(self):
        """Gets the days of this EmailStatSummaryRequest.  # noqa: E501


        :return: The days of this EmailStatSummaryRequest.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this EmailStatSummaryRequest.


        :param days: The days of this EmailStatSummaryRequest.  # noqa: E501
        :type: int
        """

        self._days = days

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
        if issubclass(EmailStatSummaryRequest, dict):
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
        if not isinstance(other, EmailStatSummaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
