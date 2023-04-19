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


class Report(object):
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
        'active': 'bool',
        'data_sources': 'list[ReportDataSource]',
        'default_dataset_id': 'str',
        'default_project_id': 'str',
        'filters': 'list[ReportFilter]',
        'merchant_id': 'str',
        'name': 'str',
        'pages': 'list[ReportPage]',
        'report_oid': 'int',
        'security_level': 'str'
    }

    attribute_map = {
        'active': 'active',
        'data_sources': 'data_sources',
        'default_dataset_id': 'default_dataset_id',
        'default_project_id': 'default_project_id',
        'filters': 'filters',
        'merchant_id': 'merchant_id',
        'name': 'name',
        'pages': 'pages',
        'report_oid': 'report_oid',
        'security_level': 'security_level'
    }

    def __init__(self, active=None, data_sources=None, default_dataset_id=None, default_project_id=None, filters=None, merchant_id=None, name=None, pages=None, report_oid=None, security_level=None):  # noqa: E501
        """Report - a model defined in Swagger"""  # noqa: E501

        self._active = None
        self._data_sources = None
        self._default_dataset_id = None
        self._default_project_id = None
        self._filters = None
        self._merchant_id = None
        self._name = None
        self._pages = None
        self._report_oid = None
        self._security_level = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if data_sources is not None:
            self.data_sources = data_sources
        if default_dataset_id is not None:
            self.default_dataset_id = default_dataset_id
        if default_project_id is not None:
            self.default_project_id = default_project_id
        if filters is not None:
            self.filters = filters
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if name is not None:
            self.name = name
        if pages is not None:
            self.pages = pages
        if report_oid is not None:
            self.report_oid = report_oid
        if security_level is not None:
            self.security_level = security_level

    @property
    def active(self):
        """Gets the active of this Report.  # noqa: E501


        :return: The active of this Report.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Report.


        :param active: The active of this Report.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def data_sources(self):
        """Gets the data_sources of this Report.  # noqa: E501


        :return: The data_sources of this Report.  # noqa: E501
        :rtype: list[ReportDataSource]
        """
        return self._data_sources

    @data_sources.setter
    def data_sources(self, data_sources):
        """Sets the data_sources of this Report.


        :param data_sources: The data_sources of this Report.  # noqa: E501
        :type: list[ReportDataSource]
        """

        self._data_sources = data_sources

    @property
    def default_dataset_id(self):
        """Gets the default_dataset_id of this Report.  # noqa: E501


        :return: The default_dataset_id of this Report.  # noqa: E501
        :rtype: str
        """
        return self._default_dataset_id

    @default_dataset_id.setter
    def default_dataset_id(self, default_dataset_id):
        """Sets the default_dataset_id of this Report.


        :param default_dataset_id: The default_dataset_id of this Report.  # noqa: E501
        :type: str
        """

        self._default_dataset_id = default_dataset_id

    @property
    def default_project_id(self):
        """Gets the default_project_id of this Report.  # noqa: E501


        :return: The default_project_id of this Report.  # noqa: E501
        :rtype: str
        """
        return self._default_project_id

    @default_project_id.setter
    def default_project_id(self, default_project_id):
        """Sets the default_project_id of this Report.


        :param default_project_id: The default_project_id of this Report.  # noqa: E501
        :type: str
        """

        self._default_project_id = default_project_id

    @property
    def filters(self):
        """Gets the filters of this Report.  # noqa: E501


        :return: The filters of this Report.  # noqa: E501
        :rtype: list[ReportFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this Report.


        :param filters: The filters of this Report.  # noqa: E501
        :type: list[ReportFilter]
        """

        self._filters = filters

    @property
    def merchant_id(self):
        """Gets the merchant_id of this Report.  # noqa: E501


        :return: The merchant_id of this Report.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this Report.


        :param merchant_id: The merchant_id of this Report.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def name(self):
        """Gets the name of this Report.  # noqa: E501


        :return: The name of this Report.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Report.


        :param name: The name of this Report.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pages(self):
        """Gets the pages of this Report.  # noqa: E501


        :return: The pages of this Report.  # noqa: E501
        :rtype: list[ReportPage]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this Report.


        :param pages: The pages of this Report.  # noqa: E501
        :type: list[ReportPage]
        """

        self._pages = pages

    @property
    def report_oid(self):
        """Gets the report_oid of this Report.  # noqa: E501

        Object identifier for this report.  # noqa: E501

        :return: The report_oid of this Report.  # noqa: E501
        :rtype: int
        """
        return self._report_oid

    @report_oid.setter
    def report_oid(self, report_oid):
        """Sets the report_oid of this Report.

        Object identifier for this report.  # noqa: E501

        :param report_oid: The report_oid of this Report.  # noqa: E501
        :type: int
        """

        self._report_oid = report_oid

    @property
    def security_level(self):
        """Gets the security_level of this Report.  # noqa: E501

        Security level to execute report under  # noqa: E501

        :return: The security_level of this Report.  # noqa: E501
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """Sets the security_level of this Report.

        Security level to execute report under  # noqa: E501

        :param security_level: The security_level of this Report.  # noqa: E501
        :type: str
        """
        allowed_values = ["standard", "low", "medium", "high"]  # noqa: E501
        if security_level not in allowed_values:
            raise ValueError(
                "Invalid value for `security_level` ({0}), must be one of {1}"  # noqa: E501
                .format(security_level, allowed_values)
            )

        self._security_level = security_level

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
        if issubclass(Report, dict):
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
        if not isinstance(other, Report):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
