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


class EmailCommseqStepLog(object):
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
        'email': 'str',
        'log': 'str',
        'log_dts': 'str'
    }

    attribute_map = {
        'email': 'email',
        'log': 'log',
        'log_dts': 'log_dts'
    }

    def __init__(self, email=None, log=None, log_dts=None):  # noqa: E501
        """EmailCommseqStepLog - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._log = None
        self._log_dts = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if log is not None:
            self.log = log
        if log_dts is not None:
            self.log_dts = log_dts

    @property
    def email(self):
        """Gets the email of this EmailCommseqStepLog.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this EmailCommseqStepLog.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EmailCommseqStepLog.

        Email  # noqa: E501

        :param email: The email of this EmailCommseqStepLog.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def log(self):
        """Gets the log of this EmailCommseqStepLog.  # noqa: E501

        Log text  # noqa: E501

        :return: The log of this EmailCommseqStepLog.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this EmailCommseqStepLog.

        Log text  # noqa: E501

        :param log: The log of this EmailCommseqStepLog.  # noqa: E501
        :type: str
        """

        self._log = log

    @property
    def log_dts(self):
        """Gets the log_dts of this EmailCommseqStepLog.  # noqa: E501

        Log date/time  # noqa: E501

        :return: The log_dts of this EmailCommseqStepLog.  # noqa: E501
        :rtype: str
        """
        return self._log_dts

    @log_dts.setter
    def log_dts(self, log_dts):
        """Sets the log_dts of this EmailCommseqStepLog.

        Log date/time  # noqa: E501

        :param log_dts: The log_dts of this EmailCommseqStepLog.  # noqa: E501
        :type: str
        """

        self._log_dts = log_dts

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
        if issubclass(EmailCommseqStepLog, dict):
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
        if not isinstance(other, EmailCommseqStepLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
