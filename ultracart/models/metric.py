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


class Metric(object):
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
        'all_time': 'float',
        'all_time_formatted': 'str',
        'last_30': 'float',
        'last_30_formatted': 'str',
        'name': 'str',
        'prior_30': 'float',
        'prior_30_formatted': 'str',
        'type': 'str'
    }

    attribute_map = {
        'all_time': 'all_time',
        'all_time_formatted': 'all_time_formatted',
        'last_30': 'last_30',
        'last_30_formatted': 'last_30_formatted',
        'name': 'name',
        'prior_30': 'prior_30',
        'prior_30_formatted': 'prior_30_formatted',
        'type': 'type'
    }

    def __init__(self, all_time=None, all_time_formatted=None, last_30=None, last_30_formatted=None, name=None, prior_30=None, prior_30_formatted=None, type=None):  # noqa: E501
        """Metric - a model defined in Swagger"""  # noqa: E501

        self._all_time = None
        self._all_time_formatted = None
        self._last_30 = None
        self._last_30_formatted = None
        self._name = None
        self._prior_30 = None
        self._prior_30_formatted = None
        self._type = None
        self.discriminator = None

        if all_time is not None:
            self.all_time = all_time
        if all_time_formatted is not None:
            self.all_time_formatted = all_time_formatted
        if last_30 is not None:
            self.last_30 = last_30
        if last_30_formatted is not None:
            self.last_30_formatted = last_30_formatted
        if name is not None:
            self.name = name
        if prior_30 is not None:
            self.prior_30 = prior_30
        if prior_30_formatted is not None:
            self.prior_30_formatted = prior_30_formatted
        if type is not None:
            self.type = type

    @property
    def all_time(self):
        """Gets the all_time of this Metric.  # noqa: E501


        :return: The all_time of this Metric.  # noqa: E501
        :rtype: float
        """
        return self._all_time

    @all_time.setter
    def all_time(self, all_time):
        """Sets the all_time of this Metric.


        :param all_time: The all_time of this Metric.  # noqa: E501
        :type: float
        """

        self._all_time = all_time

    @property
    def all_time_formatted(self):
        """Gets the all_time_formatted of this Metric.  # noqa: E501


        :return: The all_time_formatted of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._all_time_formatted

    @all_time_formatted.setter
    def all_time_formatted(self, all_time_formatted):
        """Sets the all_time_formatted of this Metric.


        :param all_time_formatted: The all_time_formatted of this Metric.  # noqa: E501
        :type: str
        """

        self._all_time_formatted = all_time_formatted

    @property
    def last_30(self):
        """Gets the last_30 of this Metric.  # noqa: E501


        :return: The last_30 of this Metric.  # noqa: E501
        :rtype: float
        """
        return self._last_30

    @last_30.setter
    def last_30(self, last_30):
        """Sets the last_30 of this Metric.


        :param last_30: The last_30 of this Metric.  # noqa: E501
        :type: float
        """

        self._last_30 = last_30

    @property
    def last_30_formatted(self):
        """Gets the last_30_formatted of this Metric.  # noqa: E501


        :return: The last_30_formatted of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._last_30_formatted

    @last_30_formatted.setter
    def last_30_formatted(self, last_30_formatted):
        """Sets the last_30_formatted of this Metric.


        :param last_30_formatted: The last_30_formatted of this Metric.  # noqa: E501
        :type: str
        """

        self._last_30_formatted = last_30_formatted

    @property
    def name(self):
        """Gets the name of this Metric.  # noqa: E501


        :return: The name of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Metric.


        :param name: The name of this Metric.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def prior_30(self):
        """Gets the prior_30 of this Metric.  # noqa: E501


        :return: The prior_30 of this Metric.  # noqa: E501
        :rtype: float
        """
        return self._prior_30

    @prior_30.setter
    def prior_30(self, prior_30):
        """Sets the prior_30 of this Metric.


        :param prior_30: The prior_30 of this Metric.  # noqa: E501
        :type: float
        """

        self._prior_30 = prior_30

    @property
    def prior_30_formatted(self):
        """Gets the prior_30_formatted of this Metric.  # noqa: E501


        :return: The prior_30_formatted of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._prior_30_formatted

    @prior_30_formatted.setter
    def prior_30_formatted(self, prior_30_formatted):
        """Sets the prior_30_formatted of this Metric.


        :param prior_30_formatted: The prior_30_formatted of this Metric.  # noqa: E501
        :type: str
        """

        self._prior_30_formatted = prior_30_formatted

    @property
    def type(self):
        """Gets the type of this Metric.  # noqa: E501


        :return: The type of this Metric.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Metric.


        :param type: The type of this Metric.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(Metric, dict):
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
        if not isinstance(other, Metric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
