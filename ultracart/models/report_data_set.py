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


class ReportDataSet(object):
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
        'data_set_query_uuid': 'str',
        'data_set_uuid': 'str',
        'destination_table_id': 'str',
        'error_message': 'str',
        'executed_sql': 'str',
        'for_object_id': 'str',
        'for_object_type': 'str',
        'initial_pages': 'list[ReportDataSetPage]',
        'max_results': 'int',
        'merchant_id': 'str',
        'page_count': 'int',
        'page_size': 'int',
        'schema': 'list[ReportDataSetSchema]',
        'security_level': 'str',
        'timezone': 'str',
        'user_data': 'str'
    }

    attribute_map = {
        'data_set_query_uuid': 'data_set_query_uuid',
        'data_set_uuid': 'data_set_uuid',
        'destination_table_id': 'destination_table_id',
        'error_message': 'error_message',
        'executed_sql': 'executed_sql',
        'for_object_id': 'for_object_id',
        'for_object_type': 'for_object_type',
        'initial_pages': 'initial_pages',
        'max_results': 'max_results',
        'merchant_id': 'merchant_id',
        'page_count': 'page_count',
        'page_size': 'page_size',
        'schema': 'schema',
        'security_level': 'security_level',
        'timezone': 'timezone',
        'user_data': 'user_data'
    }

    def __init__(self, data_set_query_uuid=None, data_set_uuid=None, destination_table_id=None, error_message=None, executed_sql=None, for_object_id=None, for_object_type=None, initial_pages=None, max_results=None, merchant_id=None, page_count=None, page_size=None, schema=None, security_level=None, timezone=None, user_data=None):  # noqa: E501
        """ReportDataSet - a model defined in Swagger"""  # noqa: E501

        self._data_set_query_uuid = None
        self._data_set_uuid = None
        self._destination_table_id = None
        self._error_message = None
        self._executed_sql = None
        self._for_object_id = None
        self._for_object_type = None
        self._initial_pages = None
        self._max_results = None
        self._merchant_id = None
        self._page_count = None
        self._page_size = None
        self._schema = None
        self._security_level = None
        self._timezone = None
        self._user_data = None
        self.discriminator = None

        if data_set_query_uuid is not None:
            self.data_set_query_uuid = data_set_query_uuid
        if data_set_uuid is not None:
            self.data_set_uuid = data_set_uuid
        if destination_table_id is not None:
            self.destination_table_id = destination_table_id
        if error_message is not None:
            self.error_message = error_message
        if executed_sql is not None:
            self.executed_sql = executed_sql
        if for_object_id is not None:
            self.for_object_id = for_object_id
        if for_object_type is not None:
            self.for_object_type = for_object_type
        if initial_pages is not None:
            self.initial_pages = initial_pages
        if max_results is not None:
            self.max_results = max_results
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if page_count is not None:
            self.page_count = page_count
        if page_size is not None:
            self.page_size = page_size
        if schema is not None:
            self.schema = schema
        if security_level is not None:
            self.security_level = security_level
        if timezone is not None:
            self.timezone = timezone
        if user_data is not None:
            self.user_data = user_data

    @property
    def data_set_query_uuid(self):
        """Gets the data_set_query_uuid of this ReportDataSet.  # noqa: E501

        A unique identifier assigned to the data set query that is returned.  # noqa: E501

        :return: The data_set_query_uuid of this ReportDataSet.  # noqa: E501
        :rtype: str
        """
        return self._data_set_query_uuid

    @data_set_query_uuid.setter
    def data_set_query_uuid(self, data_set_query_uuid):
        """Sets the data_set_query_uuid of this ReportDataSet.

        A unique identifier assigned to the data set query that is returned.  # noqa: E501

        :param data_set_query_uuid: The data_set_query_uuid of this ReportDataSet.  # noqa: E501
        :type: str
        """

        self._data_set_query_uuid = data_set_query_uuid

    @property
    def data_set_uuid(self):
        """Gets the data_set_uuid of this ReportDataSet.  # noqa: E501

        A unique identifier assigned to the data set that is returned.  # noqa: E501

        :return: The data_set_uuid of this ReportDataSet.  # noqa: E501
        :rtype: str
        """
        return self._data_set_uuid

    @data_set_uuid.setter
    def data_set_uuid(self, data_set_uuid):
        """Sets the data_set_uuid of this ReportDataSet.

        A unique identifier assigned to the data set that is returned.  # noqa: E501

        :param data_set_uuid: The data_set_uuid of this ReportDataSet.  # noqa: E501
        :type: str
        """

        self._data_set_uuid = data_set_uuid

    @property
    def destination_table_id(self):
        """Gets the destination_table_id of this ReportDataSet.  # noqa: E501

        The BigQuery destination table id that contains the result.  # noqa: E501

        :return: The destination_table_id of this ReportDataSet.  # noqa: E501
        :rtype: str
        """
        return self._destination_table_id

    @destination_table_id.setter
    def destination_table_id(self, destination_table_id):
        """Sets the destination_table_id of this ReportDataSet.

        The BigQuery destination table id that contains the result.  # noqa: E501

        :param destination_table_id: The destination_table_id of this ReportDataSet.  # noqa: E501
        :type: str
        """

        self._destination_table_id = destination_table_id

    @property
    def error_message(self):
        """Gets the error_message of this ReportDataSet.  # noqa: E501

        Error message if the query failed.  # noqa: E501

        :return: The error_message of this ReportDataSet.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ReportDataSet.

        Error message if the query failed.  # noqa: E501

        :param error_message: The error_message of this ReportDataSet.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def executed_sql(self):
        """Gets the executed_sql of this ReportDataSet.  # noqa: E501


        :return: The executed_sql of this ReportDataSet.  # noqa: E501
        :rtype: str
        """
        return self._executed_sql

    @executed_sql.setter
    def executed_sql(self, executed_sql):
        """Sets the executed_sql of this ReportDataSet.


        :param executed_sql: The executed_sql of this ReportDataSet.  # noqa: E501
        :type: str
        """

        self._executed_sql = executed_sql

    @property
    def for_object_id(self):
        """Gets the for_object_id of this ReportDataSet.  # noqa: E501

        An identifier that can be used to help match up the returned data set  # noqa: E501

        :return: The for_object_id of this ReportDataSet.  # noqa: E501
        :rtype: str
        """
        return self._for_object_id

    @for_object_id.setter
    def for_object_id(self, for_object_id):
        """Sets the for_object_id of this ReportDataSet.

        An identifier that can be used to help match up the returned data set  # noqa: E501

        :param for_object_id: The for_object_id of this ReportDataSet.  # noqa: E501
        :type: str
        """

        self._for_object_id = for_object_id

    @property
    def for_object_type(self):
        """Gets the for_object_type of this ReportDataSet.  # noqa: E501

        The type of object this data set is for  # noqa: E501

        :return: The for_object_type of this ReportDataSet.  # noqa: E501
        :rtype: str
        """
        return self._for_object_type

    @for_object_type.setter
    def for_object_type(self, for_object_type):
        """Sets the for_object_type of this ReportDataSet.

        The type of object this data set is for  # noqa: E501

        :param for_object_type: The for_object_type of this ReportDataSet.  # noqa: E501
        :type: str
        """
        allowed_values = ["schema", "filter", "visualization"]  # noqa: E501
        if for_object_type not in allowed_values:
            raise ValueError(
                "Invalid value for `for_object_type` ({0}), must be one of {1}"  # noqa: E501
                .format(for_object_type, allowed_values)
            )

        self._for_object_type = for_object_type

    @property
    def initial_pages(self):
        """Gets the initial_pages of this ReportDataSet.  # noqa: E501

        Initial pages returned in the dataset  # noqa: E501

        :return: The initial_pages of this ReportDataSet.  # noqa: E501
        :rtype: list[ReportDataSetPage]
        """
        return self._initial_pages

    @initial_pages.setter
    def initial_pages(self, initial_pages):
        """Sets the initial_pages of this ReportDataSet.

        Initial pages returned in the dataset  # noqa: E501

        :param initial_pages: The initial_pages of this ReportDataSet.  # noqa: E501
        :type: list[ReportDataSetPage]
        """

        self._initial_pages = initial_pages

    @property
    def max_results(self):
        """Gets the max_results of this ReportDataSet.  # noqa: E501

        The total number of results  # noqa: E501

        :return: The max_results of this ReportDataSet.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this ReportDataSet.

        The total number of results  # noqa: E501

        :param max_results: The max_results of this ReportDataSet.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def merchant_id(self):
        """Gets the merchant_id of this ReportDataSet.  # noqa: E501

        Merchant that owns this data set  # noqa: E501

        :return: The merchant_id of this ReportDataSet.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this ReportDataSet.

        Merchant that owns this data set  # noqa: E501

        :param merchant_id: The merchant_id of this ReportDataSet.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def page_count(self):
        """Gets the page_count of this ReportDataSet.  # noqa: E501

        The total number of pages in the result set  # noqa: E501

        :return: The page_count of this ReportDataSet.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this ReportDataSet.

        The total number of pages in the result set  # noqa: E501

        :param page_count: The page_count of this ReportDataSet.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def page_size(self):
        """Gets the page_size of this ReportDataSet.  # noqa: E501

        The size of the pages  # noqa: E501

        :return: The page_size of this ReportDataSet.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ReportDataSet.

        The size of the pages  # noqa: E501

        :param page_size: The page_size of this ReportDataSet.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def schema(self):
        """Gets the schema of this ReportDataSet.  # noqa: E501

        The schema associated with the data set.  # noqa: E501

        :return: The schema of this ReportDataSet.  # noqa: E501
        :rtype: list[ReportDataSetSchema]
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this ReportDataSet.

        The schema associated with the data set.  # noqa: E501

        :param schema: The schema of this ReportDataSet.  # noqa: E501
        :type: list[ReportDataSetSchema]
        """

        self._schema = schema

    @property
    def security_level(self):
        """Gets the security_level of this ReportDataSet.  # noqa: E501

        Security level this dataset was read from.  # noqa: E501

        :return: The security_level of this ReportDataSet.  # noqa: E501
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """Sets the security_level of this ReportDataSet.

        Security level this dataset was read from.  # noqa: E501

        :param security_level: The security_level of this ReportDataSet.  # noqa: E501
        :type: str
        """

        self._security_level = security_level

    @property
    def timezone(self):
        """Gets the timezone of this ReportDataSet.  # noqa: E501


        :return: The timezone of this ReportDataSet.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ReportDataSet.


        :param timezone: The timezone of this ReportDataSet.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def user_data(self):
        """Gets the user_data of this ReportDataSet.  # noqa: E501

        Any other data that needs to be returned with the response to help the UI  # noqa: E501

        :return: The user_data of this ReportDataSet.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ReportDataSet.

        Any other data that needs to be returned with the response to help the UI  # noqa: E501

        :param user_data: The user_data of this ReportDataSet.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

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
        if issubclass(ReportDataSet, dict):
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
        if not isinstance(other, ReportDataSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
