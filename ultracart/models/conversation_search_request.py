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


class ConversationSearchRequest(object):
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
        'date_end': 'str',
        'date_start': 'str',
        'email_filter': 'str',
        'language_filter': 'str',
        'medium_filter': 'str',
        'order_by_newest': 'bool',
        'order_by_oldest': 'bool',
        'range_begin': 'int',
        'range_end': 'int',
        'sms_phone_number_filter': 'str',
        'text_search': 'str',
        'visible_filter': 'bool'
    }

    attribute_map = {
        'date_end': 'date_end',
        'date_start': 'date_start',
        'email_filter': 'email_filter',
        'language_filter': 'language_filter',
        'medium_filter': 'medium_filter',
        'order_by_newest': 'order_by_newest',
        'order_by_oldest': 'order_by_oldest',
        'range_begin': 'range_begin',
        'range_end': 'range_end',
        'sms_phone_number_filter': 'sms_phone_number_filter',
        'text_search': 'text_search',
        'visible_filter': 'visible_filter'
    }

    def __init__(self, date_end=None, date_start=None, email_filter=None, language_filter=None, medium_filter=None, order_by_newest=None, order_by_oldest=None, range_begin=None, range_end=None, sms_phone_number_filter=None, text_search=None, visible_filter=None):  # noqa: E501
        """ConversationSearchRequest - a model defined in Swagger"""  # noqa: E501

        self._date_end = None
        self._date_start = None
        self._email_filter = None
        self._language_filter = None
        self._medium_filter = None
        self._order_by_newest = None
        self._order_by_oldest = None
        self._range_begin = None
        self._range_end = None
        self._sms_phone_number_filter = None
        self._text_search = None
        self._visible_filter = None
        self.discriminator = None

        if date_end is not None:
            self.date_end = date_end
        if date_start is not None:
            self.date_start = date_start
        if email_filter is not None:
            self.email_filter = email_filter
        if language_filter is not None:
            self.language_filter = language_filter
        if medium_filter is not None:
            self.medium_filter = medium_filter
        if order_by_newest is not None:
            self.order_by_newest = order_by_newest
        if order_by_oldest is not None:
            self.order_by_oldest = order_by_oldest
        if range_begin is not None:
            self.range_begin = range_begin
        if range_end is not None:
            self.range_end = range_end
        if sms_phone_number_filter is not None:
            self.sms_phone_number_filter = sms_phone_number_filter
        if text_search is not None:
            self.text_search = text_search
        if visible_filter is not None:
            self.visible_filter = visible_filter

    @property
    def date_end(self):
        """Gets the date_end of this ConversationSearchRequest.  # noqa: E501

        End of the range  # noqa: E501

        :return: The date_end of this ConversationSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this ConversationSearchRequest.

        End of the range  # noqa: E501

        :param date_end: The date_end of this ConversationSearchRequest.  # noqa: E501
        :type: str
        """

        self._date_end = date_end

    @property
    def date_start(self):
        """Gets the date_start of this ConversationSearchRequest.  # noqa: E501

        Start of the range  # noqa: E501

        :return: The date_start of this ConversationSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """Sets the date_start of this ConversationSearchRequest.

        Start of the range  # noqa: E501

        :param date_start: The date_start of this ConversationSearchRequest.  # noqa: E501
        :type: str
        """

        self._date_start = date_start

    @property
    def email_filter(self):
        """Gets the email_filter of this ConversationSearchRequest.  # noqa: E501


        :return: The email_filter of this ConversationSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_filter

    @email_filter.setter
    def email_filter(self, email_filter):
        """Sets the email_filter of this ConversationSearchRequest.


        :param email_filter: The email_filter of this ConversationSearchRequest.  # noqa: E501
        :type: str
        """

        self._email_filter = email_filter

    @property
    def language_filter(self):
        """Gets the language_filter of this ConversationSearchRequest.  # noqa: E501


        :return: The language_filter of this ConversationSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._language_filter

    @language_filter.setter
    def language_filter(self, language_filter):
        """Sets the language_filter of this ConversationSearchRequest.


        :param language_filter: The language_filter of this ConversationSearchRequest.  # noqa: E501
        :type: str
        """

        self._language_filter = language_filter

    @property
    def medium_filter(self):
        """Gets the medium_filter of this ConversationSearchRequest.  # noqa: E501


        :return: The medium_filter of this ConversationSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._medium_filter

    @medium_filter.setter
    def medium_filter(self, medium_filter):
        """Sets the medium_filter of this ConversationSearchRequest.


        :param medium_filter: The medium_filter of this ConversationSearchRequest.  # noqa: E501
        :type: str
        """

        self._medium_filter = medium_filter

    @property
    def order_by_newest(self):
        """Gets the order_by_newest of this ConversationSearchRequest.  # noqa: E501


        :return: The order_by_newest of this ConversationSearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._order_by_newest

    @order_by_newest.setter
    def order_by_newest(self, order_by_newest):
        """Sets the order_by_newest of this ConversationSearchRequest.


        :param order_by_newest: The order_by_newest of this ConversationSearchRequest.  # noqa: E501
        :type: bool
        """

        self._order_by_newest = order_by_newest

    @property
    def order_by_oldest(self):
        """Gets the order_by_oldest of this ConversationSearchRequest.  # noqa: E501


        :return: The order_by_oldest of this ConversationSearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._order_by_oldest

    @order_by_oldest.setter
    def order_by_oldest(self, order_by_oldest):
        """Sets the order_by_oldest of this ConversationSearchRequest.


        :param order_by_oldest: The order_by_oldest of this ConversationSearchRequest.  # noqa: E501
        :type: bool
        """

        self._order_by_oldest = order_by_oldest

    @property
    def range_begin(self):
        """Gets the range_begin of this ConversationSearchRequest.  # noqa: E501


        :return: The range_begin of this ConversationSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._range_begin

    @range_begin.setter
    def range_begin(self, range_begin):
        """Sets the range_begin of this ConversationSearchRequest.


        :param range_begin: The range_begin of this ConversationSearchRequest.  # noqa: E501
        :type: int
        """

        self._range_begin = range_begin

    @property
    def range_end(self):
        """Gets the range_end of this ConversationSearchRequest.  # noqa: E501


        :return: The range_end of this ConversationSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._range_end

    @range_end.setter
    def range_end(self, range_end):
        """Sets the range_end of this ConversationSearchRequest.


        :param range_end: The range_end of this ConversationSearchRequest.  # noqa: E501
        :type: int
        """

        self._range_end = range_end

    @property
    def sms_phone_number_filter(self):
        """Gets the sms_phone_number_filter of this ConversationSearchRequest.  # noqa: E501


        :return: The sms_phone_number_filter of this ConversationSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._sms_phone_number_filter

    @sms_phone_number_filter.setter
    def sms_phone_number_filter(self, sms_phone_number_filter):
        """Sets the sms_phone_number_filter of this ConversationSearchRequest.


        :param sms_phone_number_filter: The sms_phone_number_filter of this ConversationSearchRequest.  # noqa: E501
        :type: str
        """

        self._sms_phone_number_filter = sms_phone_number_filter

    @property
    def text_search(self):
        """Gets the text_search of this ConversationSearchRequest.  # noqa: E501


        :return: The text_search of this ConversationSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._text_search

    @text_search.setter
    def text_search(self, text_search):
        """Sets the text_search of this ConversationSearchRequest.


        :param text_search: The text_search of this ConversationSearchRequest.  # noqa: E501
        :type: str
        """

        self._text_search = text_search

    @property
    def visible_filter(self):
        """Gets the visible_filter of this ConversationSearchRequest.  # noqa: E501


        :return: The visible_filter of this ConversationSearchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._visible_filter

    @visible_filter.setter
    def visible_filter(self, visible_filter):
        """Sets the visible_filter of this ConversationSearchRequest.


        :param visible_filter: The visible_filter of this ConversationSearchRequest.  # noqa: E501
        :type: bool
        """

        self._visible_filter = visible_filter

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
        if issubclass(ConversationSearchRequest, dict):
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
        if not isinstance(other, ConversationSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
