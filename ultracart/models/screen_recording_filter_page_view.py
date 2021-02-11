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
        'events': 'list[ScreenRecordingFilterPageViewEvent]',
        'params': 'list[ScreenRecordingFilterPageViewParam]',
        'referrer': 'ScreenRecordingFilterStringSearch',
        'referrer_params': 'list[ScreenRecordingFilterPageViewReferrerParam]',
        'referrer_raw': 'ScreenRecordingFilterStringSearch',
        'time_on_page': 'ScreenRecordingFilterRangeInteger',
        'url': 'ScreenRecordingFilterStringSearch'
    }

    attribute_map = {
        'events': 'events',
        'params': 'params',
        'referrer': 'referrer',
        'referrer_params': 'referrer_params',
        'referrer_raw': 'referrer_raw',
        'time_on_page': 'time_on_page',
        'url': 'url'
    }

    def __init__(self, events=None, params=None, referrer=None, referrer_params=None, referrer_raw=None, time_on_page=None, url=None):  # noqa: E501
        """ScreenRecordingFilterPageView - a model defined in Swagger"""  # noqa: E501

        self._events = None
        self._params = None
        self._referrer = None
        self._referrer_params = None
        self._referrer_raw = None
        self._time_on_page = None
        self._url = None
        self.discriminator = None

        if events is not None:
            self.events = events
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
        if url is not None:
            self.url = url

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