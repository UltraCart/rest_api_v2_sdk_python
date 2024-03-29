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


class ScreenRecordingFilterPageView(object):
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
        'domain': 'ScreenRecordingFilterStringSearch',
        'domain_filter': 'bool',
        'event_name_filter': 'bool',
        'event_param_name_filter': 'bool',
        'event_param_value_filter': 'bool',
        'events': 'list[ScreenRecordingFilterPageViewEvent]',
        'param_name_filter': 'bool',
        'param_value_filter': 'bool',
        'params': 'list[ScreenRecordingFilterPageViewParam]',
        'referrer': 'ScreenRecordingFilterStringSearch',
        'referrer_params': 'list[ScreenRecordingFilterPageViewReferrerParam]',
        'referrer_raw': 'ScreenRecordingFilterStringSearch',
        'time_on_page': 'ScreenRecordingFilterRangeInteger',
        'time_on_page_max_filter': 'bool',
        'time_on_page_min_filter': 'bool',
        'url': 'ScreenRecordingFilterStringSearch',
        'url_filter': 'bool'
    }

    attribute_map = {
        'domain': 'domain',
        'domain_filter': 'domain_filter',
        'event_name_filter': 'event_name_filter',
        'event_param_name_filter': 'event_param_name_filter',
        'event_param_value_filter': 'event_param_value_filter',
        'events': 'events',
        'param_name_filter': 'param_name_filter',
        'param_value_filter': 'param_value_filter',
        'params': 'params',
        'referrer': 'referrer',
        'referrer_params': 'referrer_params',
        'referrer_raw': 'referrer_raw',
        'time_on_page': 'time_on_page',
        'time_on_page_max_filter': 'time_on_page_max_filter',
        'time_on_page_min_filter': 'time_on_page_min_filter',
        'url': 'url',
        'url_filter': 'url_filter'
    }

    def __init__(self, domain=None, domain_filter=None, event_name_filter=None, event_param_name_filter=None, event_param_value_filter=None, events=None, param_name_filter=None, param_value_filter=None, params=None, referrer=None, referrer_params=None, referrer_raw=None, time_on_page=None, time_on_page_max_filter=None, time_on_page_min_filter=None, url=None, url_filter=None):  # noqa: E501
        """ScreenRecordingFilterPageView - a model defined in Swagger"""  # noqa: E501

        self._domain = None
        self._domain_filter = None
        self._event_name_filter = None
        self._event_param_name_filter = None
        self._event_param_value_filter = None
        self._events = None
        self._param_name_filter = None
        self._param_value_filter = None
        self._params = None
        self._referrer = None
        self._referrer_params = None
        self._referrer_raw = None
        self._time_on_page = None
        self._time_on_page_max_filter = None
        self._time_on_page_min_filter = None
        self._url = None
        self._url_filter = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if domain_filter is not None:
            self.domain_filter = domain_filter
        if event_name_filter is not None:
            self.event_name_filter = event_name_filter
        if event_param_name_filter is not None:
            self.event_param_name_filter = event_param_name_filter
        if event_param_value_filter is not None:
            self.event_param_value_filter = event_param_value_filter
        if events is not None:
            self.events = events
        if param_name_filter is not None:
            self.param_name_filter = param_name_filter
        if param_value_filter is not None:
            self.param_value_filter = param_value_filter
        if params is not None:
            self.params = params
        if referrer is not None:
            self.referrer = referrer
        if referrer_params is not None:
            self.referrer_params = referrer_params
        if referrer_raw is not None:
            self.referrer_raw = referrer_raw
        if time_on_page is not None:
            self.time_on_page = time_on_page
        if time_on_page_max_filter is not None:
            self.time_on_page_max_filter = time_on_page_max_filter
        if time_on_page_min_filter is not None:
            self.time_on_page_min_filter = time_on_page_min_filter
        if url is not None:
            self.url = url
        if url_filter is not None:
            self.url_filter = url_filter

    @property
    def domain(self):
        """Gets the domain of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The domain of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: ScreenRecordingFilterStringSearch
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ScreenRecordingFilterPageView.


        :param domain: The domain of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: ScreenRecordingFilterStringSearch
        """

        self._domain = domain

    @property
    def domain_filter(self):
        """Gets the domain_filter of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The domain_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: bool
        """
        return self._domain_filter

    @domain_filter.setter
    def domain_filter(self, domain_filter):
        """Sets the domain_filter of this ScreenRecordingFilterPageView.


        :param domain_filter: The domain_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: bool
        """

        self._domain_filter = domain_filter

    @property
    def event_name_filter(self):
        """Gets the event_name_filter of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The event_name_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: bool
        """
        return self._event_name_filter

    @event_name_filter.setter
    def event_name_filter(self, event_name_filter):
        """Sets the event_name_filter of this ScreenRecordingFilterPageView.


        :param event_name_filter: The event_name_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: bool
        """

        self._event_name_filter = event_name_filter

    @property
    def event_param_name_filter(self):
        """Gets the event_param_name_filter of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The event_param_name_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: bool
        """
        return self._event_param_name_filter

    @event_param_name_filter.setter
    def event_param_name_filter(self, event_param_name_filter):
        """Sets the event_param_name_filter of this ScreenRecordingFilterPageView.


        :param event_param_name_filter: The event_param_name_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: bool
        """

        self._event_param_name_filter = event_param_name_filter

    @property
    def event_param_value_filter(self):
        """Gets the event_param_value_filter of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The event_param_value_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: bool
        """
        return self._event_param_value_filter

    @event_param_value_filter.setter
    def event_param_value_filter(self, event_param_value_filter):
        """Sets the event_param_value_filter of this ScreenRecordingFilterPageView.


        :param event_param_value_filter: The event_param_value_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: bool
        """

        self._event_param_value_filter = event_param_value_filter

    @property
    def events(self):
        """Gets the events of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The events of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: list[ScreenRecordingFilterPageViewEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ScreenRecordingFilterPageView.


        :param events: The events of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: list[ScreenRecordingFilterPageViewEvent]
        """

        self._events = events

    @property
    def param_name_filter(self):
        """Gets the param_name_filter of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The param_name_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: bool
        """
        return self._param_name_filter

    @param_name_filter.setter
    def param_name_filter(self, param_name_filter):
        """Sets the param_name_filter of this ScreenRecordingFilterPageView.


        :param param_name_filter: The param_name_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: bool
        """

        self._param_name_filter = param_name_filter

    @property
    def param_value_filter(self):
        """Gets the param_value_filter of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The param_value_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: bool
        """
        return self._param_value_filter

    @param_value_filter.setter
    def param_value_filter(self, param_value_filter):
        """Sets the param_value_filter of this ScreenRecordingFilterPageView.


        :param param_value_filter: The param_value_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: bool
        """

        self._param_value_filter = param_value_filter

    @property
    def params(self):
        """Gets the params of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The params of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: list[ScreenRecordingFilterPageViewParam]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ScreenRecordingFilterPageView.


        :param params: The params of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: list[ScreenRecordingFilterPageViewParam]
        """

        self._params = params

    @property
    def referrer(self):
        """Gets the referrer of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The referrer of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: ScreenRecordingFilterStringSearch
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """Sets the referrer of this ScreenRecordingFilterPageView.


        :param referrer: The referrer of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: ScreenRecordingFilterStringSearch
        """

        self._referrer = referrer

    @property
    def referrer_params(self):
        """Gets the referrer_params of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The referrer_params of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: list[ScreenRecordingFilterPageViewReferrerParam]
        """
        return self._referrer_params

    @referrer_params.setter
    def referrer_params(self, referrer_params):
        """Sets the referrer_params of this ScreenRecordingFilterPageView.


        :param referrer_params: The referrer_params of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: list[ScreenRecordingFilterPageViewReferrerParam]
        """

        self._referrer_params = referrer_params

    @property
    def referrer_raw(self):
        """Gets the referrer_raw of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The referrer_raw of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: ScreenRecordingFilterStringSearch
        """
        return self._referrer_raw

    @referrer_raw.setter
    def referrer_raw(self, referrer_raw):
        """Sets the referrer_raw of this ScreenRecordingFilterPageView.


        :param referrer_raw: The referrer_raw of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: ScreenRecordingFilterStringSearch
        """

        self._referrer_raw = referrer_raw

    @property
    def time_on_page(self):
        """Gets the time_on_page of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The time_on_page of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: ScreenRecordingFilterRangeInteger
        """
        return self._time_on_page

    @time_on_page.setter
    def time_on_page(self, time_on_page):
        """Sets the time_on_page of this ScreenRecordingFilterPageView.


        :param time_on_page: The time_on_page of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: ScreenRecordingFilterRangeInteger
        """

        self._time_on_page = time_on_page

    @property
    def time_on_page_max_filter(self):
        """Gets the time_on_page_max_filter of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The time_on_page_max_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: bool
        """
        return self._time_on_page_max_filter

    @time_on_page_max_filter.setter
    def time_on_page_max_filter(self, time_on_page_max_filter):
        """Sets the time_on_page_max_filter of this ScreenRecordingFilterPageView.


        :param time_on_page_max_filter: The time_on_page_max_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: bool
        """

        self._time_on_page_max_filter = time_on_page_max_filter

    @property
    def time_on_page_min_filter(self):
        """Gets the time_on_page_min_filter of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The time_on_page_min_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: bool
        """
        return self._time_on_page_min_filter

    @time_on_page_min_filter.setter
    def time_on_page_min_filter(self, time_on_page_min_filter):
        """Sets the time_on_page_min_filter of this ScreenRecordingFilterPageView.


        :param time_on_page_min_filter: The time_on_page_min_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: bool
        """

        self._time_on_page_min_filter = time_on_page_min_filter

    @property
    def url(self):
        """Gets the url of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The url of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: ScreenRecordingFilterStringSearch
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ScreenRecordingFilterPageView.


        :param url: The url of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: ScreenRecordingFilterStringSearch
        """

        self._url = url

    @property
    def url_filter(self):
        """Gets the url_filter of this ScreenRecordingFilterPageView.  # noqa: E501


        :return: The url_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :rtype: bool
        """
        return self._url_filter

    @url_filter.setter
    def url_filter(self, url_filter):
        """Sets the url_filter of this ScreenRecordingFilterPageView.


        :param url_filter: The url_filter of this ScreenRecordingFilterPageView.  # noqa: E501
        :type: bool
        """

        self._url_filter = url_filter

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
        if issubclass(ScreenRecordingFilterPageView, dict):
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
        if not isinstance(other, ScreenRecordingFilterPageView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
