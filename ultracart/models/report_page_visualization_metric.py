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


class ReportPageVisualizationMetric(object):
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
        'aggregation': 'str',
        '_as': 'str',
        'column': 'str',
        'round': 'int'
    }

    attribute_map = {
        'aggregation': 'aggregation',
        '_as': 'as',
        'column': 'column',
        'round': 'round'
    }

    def __init__(self, aggregation=None, _as=None, column=None, round=None):  # noqa: E501
        """ReportPageVisualizationMetric - a model defined in Swagger"""  # noqa: E501

        self._aggregation = None
        self.__as = None
        self._column = None
        self._round = None
        self.discriminator = None

        if aggregation is not None:
            self.aggregation = aggregation
        if _as is not None:
            self._as = _as
        if column is not None:
            self.column = column
        if round is not None:
            self.round = round

    @property
    def aggregation(self):
        """Gets the aggregation of this ReportPageVisualizationMetric.  # noqa: E501

        Aggregation to perform  # noqa: E501

        :return: The aggregation of this ReportPageVisualizationMetric.  # noqa: E501
        :rtype: str
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this ReportPageVisualizationMetric.

        Aggregation to perform  # noqa: E501

        :param aggregation: The aggregation of this ReportPageVisualizationMetric.  # noqa: E501
        :type: str
        """
        allowed_values = ["sum", "count", "min", "max", "avg"]  # noqa: E501
        if aggregation not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation, allowed_values)
            )

        self._aggregation = aggregation

    @property
    def _as(self):
        """Gets the _as of this ReportPageVisualizationMetric.  # noqa: E501

        Return the column as a different name  # noqa: E501

        :return: The _as of this ReportPageVisualizationMetric.  # noqa: E501
        :rtype: str
        """
        return self.__as

    @_as.setter
    def _as(self, _as):
        """Sets the _as of this ReportPageVisualizationMetric.

        Return the column as a different name  # noqa: E501

        :param _as: The _as of this ReportPageVisualizationMetric.  # noqa: E501
        :type: str
        """

        self.__as = _as

    @property
    def column(self):
        """Gets the column of this ReportPageVisualizationMetric.  # noqa: E501


        :return: The column of this ReportPageVisualizationMetric.  # noqa: E501
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this ReportPageVisualizationMetric.


        :param column: The column of this ReportPageVisualizationMetric.  # noqa: E501
        :type: str
        """

        self._column = column

    @property
    def round(self):
        """Gets the round of this ReportPageVisualizationMetric.  # noqa: E501

        Number of places after the decimal point to round the number to.  # noqa: E501

        :return: The round of this ReportPageVisualizationMetric.  # noqa: E501
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this ReportPageVisualizationMetric.

        Number of places after the decimal point to round the number to.  # noqa: E501

        :param round: The round of this ReportPageVisualizationMetric.  # noqa: E501
        :type: int
        """

        self._round = round

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
        if issubclass(ReportPageVisualizationMetric, dict):
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
        if not isinstance(other, ReportPageVisualizationMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
