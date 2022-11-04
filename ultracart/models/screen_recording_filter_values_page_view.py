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


class ScreenRecordingFilterValuesPageView(object):
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
        'domains': 'list[str]',
        'events': 'list[ScreenRecordingFilterValuesEvent]',
        'page_params': 'list[ScreenRecordingFilterValuesPageParam]',
        'time_on_page_max': 'int',
        'time_on_page_min': 'int',
        'urls': 'list[str]'
    }

    attribute_map = {
        'domains': 'domains',
        'events': 'events',
        'page_params': 'page_params',
        'time_on_page_max': 'time_on_page_max',
        'time_on_page_min': 'time_on_page_min',
        'urls': 'urls'
    }

    def __init__(self, domains=None, events=None, page_params=None, time_on_page_max=None, time_on_page_min=None, urls=None):  # noqa: E501
        """ScreenRecordingFilterValuesPageView - a model defined in Swagger"""  # noqa: E501

        self._domains = None
        self._events = None
        self._page_params = None
        self._time_on_page_max = None
        self._time_on_page_min = None
        self._urls = None
        self.discriminator = None

        if domains is not None:
            self.domains = domains
        if events is not None:
            self.events = events
        if page_params is not None:
            self.page_params = page_params
        if time_on_page_max is not None:
            self.time_on_page_max = time_on_page_max
        if time_on_page_min is not None:
            self.time_on_page_min = time_on_page_min
        if urls is not None:
            self.urls = urls

    @property
    def domains(self):
        """Gets the domains of this ScreenRecordingFilterValuesPageView.  # noqa: E501


        :return: The domains of this ScreenRecordingFilterValuesPageView.  # noqa: E501
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this ScreenRecordingFilterValuesPageView.


        :param domains: The domains of this ScreenRecordingFilterValuesPageView.  # noqa: E501
        :type: list[str]
        """

        self._domains = domains

    @property
    def events(self):
        """Gets the events of this ScreenRecordingFilterValuesPageView.  # noqa: E501


        :return: The events of this ScreenRecordingFilterValuesPageView.  # noqa: E501
        :rtype: list[ScreenRecordingFilterValuesEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ScreenRecordingFilterValuesPageView.


        :param events: The events of this ScreenRecordingFilterValuesPageView.  # noqa: E501
        :type: list[ScreenRecordingFilterValuesEvent]
        """

        self._events = events

    @property
    def page_params(self):
        """Gets the page_params of this ScreenRecordingFilterValuesPageView.  # noqa: E501


        :return: The page_params of this ScreenRecordingFilterValuesPageView.  # noqa: E501
        :rtype: list[ScreenRecordingFilterValuesPageParam]
        """
        return self._page_params

    @page_params.setter
    def page_params(self, page_params):
        """Sets the page_params of this ScreenRecordingFilterValuesPageView.


        :param page_params: The page_params of this ScreenRecordingFilterValuesPageView.  # noqa: E501
        :type: list[ScreenRecordingFilterValuesPageParam]
        """

        self._page_params = page_params

    @property
    def time_on_page_max(self):
        """Gets the time_on_page_max of this ScreenRecordingFilterValuesPageView.  # noqa: E501


        :return: The time_on_page_max of this ScreenRecordingFilterValuesPageView.  # noqa: E501
        :rtype: int
        """
        return self._time_on_page_max

    @time_on_page_max.setter
    def time_on_page_max(self, time_on_page_max):
        """Sets the time_on_page_max of this ScreenRecordingFilterValuesPageView.


        :param time_on_page_max: The time_on_page_max of this ScreenRecordingFilterValuesPageView.  # noqa: E501
        :type: int
        """

        self._time_on_page_max = time_on_page_max

    @property
    def time_on_page_min(self):
        """Gets the time_on_page_min of this ScreenRecordingFilterValuesPageView.  # noqa: E501


        :return: The time_on_page_min of this ScreenRecordingFilterValuesPageView.  # noqa: E501
        :rtype: int
        """
        return self._time_on_page_min

    @time_on_page_min.setter
    def time_on_page_min(self, time_on_page_min):
        """Sets the time_on_page_min of this ScreenRecordingFilterValuesPageView.


        :param time_on_page_min: The time_on_page_min of this ScreenRecordingFilterValuesPageView.  # noqa: E501
        :type: int
        """

        self._time_on_page_min = time_on_page_min

    @property
    def urls(self):
        """Gets the urls of this ScreenRecordingFilterValuesPageView.  # noqa: E501


        :return: The urls of this ScreenRecordingFilterValuesPageView.  # noqa: E501
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this ScreenRecordingFilterValuesPageView.


        :param urls: The urls of this ScreenRecordingFilterValuesPageView.  # noqa: E501
        :type: list[str]
        """

        self._urls = urls

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
        if issubclass(ScreenRecordingFilterValuesPageView, dict):
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
        if not isinstance(other, ScreenRecordingFilterValuesPageView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other