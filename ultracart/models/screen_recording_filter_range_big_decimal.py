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


class ScreenRecordingFilterRangeBigDecimal(object):
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
        'eq': 'float',
        'gt': 'float',
        'gte': 'float',
        'lt': 'float',
        'lte': 'float'
    }

    attribute_map = {
        'eq': 'eq',
        'gt': 'gt',
        'gte': 'gte',
        'lt': 'lt',
        'lte': 'lte'
    }

    def __init__(self, eq=None, gt=None, gte=None, lt=None, lte=None):  # noqa: E501
        """ScreenRecordingFilterRangeBigDecimal - a model defined in Swagger"""  # noqa: E501

        self._eq = None
        self._gt = None
        self._gte = None
        self._lt = None
        self._lte = None
        self.discriminator = None

        if eq is not None:
            self.eq = eq
        if gt is not None:
            self.gt = gt
        if gte is not None:
            self.gte = gte
        if lt is not None:
            self.lt = lt
        if lte is not None:
            self.lte = lte

    @property
    def eq(self):
        """Gets the eq of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501


        :return: The eq of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._eq

    @eq.setter
    def eq(self, eq):
        """Sets the eq of this ScreenRecordingFilterRangeBigDecimal.


        :param eq: The eq of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501
        :type: float
        """

        self._eq = eq

    @property
    def gt(self):
        """Gets the gt of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501


        :return: The gt of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._gt

    @gt.setter
    def gt(self, gt):
        """Sets the gt of this ScreenRecordingFilterRangeBigDecimal.


        :param gt: The gt of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501
        :type: float
        """

        self._gt = gt

    @property
    def gte(self):
        """Gets the gte of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501


        :return: The gte of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._gte

    @gte.setter
    def gte(self, gte):
        """Sets the gte of this ScreenRecordingFilterRangeBigDecimal.


        :param gte: The gte of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501
        :type: float
        """

        self._gte = gte

    @property
    def lt(self):
        """Gets the lt of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501


        :return: The lt of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._lt

    @lt.setter
    def lt(self, lt):
        """Sets the lt of this ScreenRecordingFilterRangeBigDecimal.


        :param lt: The lt of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501
        :type: float
        """

        self._lt = lt

    @property
    def lte(self):
        """Gets the lte of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501


        :return: The lte of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501
        :rtype: float
        """
        return self._lte

    @lte.setter
    def lte(self, lte):
        """Sets the lte of this ScreenRecordingFilterRangeBigDecimal.


        :param lte: The lte of this ScreenRecordingFilterRangeBigDecimal.  # noqa: E501
        :type: float
        """

        self._lte = lte

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
        if issubclass(ScreenRecordingFilterRangeBigDecimal, dict):
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
        if not isinstance(other, ScreenRecordingFilterRangeBigDecimal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other