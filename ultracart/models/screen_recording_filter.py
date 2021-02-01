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


class ScreenRecordingFilter(object):
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
        'email': 'ScreenRecordingFilterStringSearch',
        'email_identified': 'bool',
        'end_timestamp': 'ScreenRecordingFilterRangeDate',
        'esp_customer_uuid': 'str',
        'favorite': 'bool',
        'geolocation': 'ScreenRecordingFilterGeoDistance',
        'geolocation_country': 'ScreenRecordingFilterStringSearch',
        'geolocation_state': 'ScreenRecordingFilterStringSearch',
        'max_filter_values': 'int',
        'order_id': 'ScreenRecordingFilterStringSearch',
        'page_view_count': 'ScreenRecordingFilterRangeInteger',
        'page_views': 'list[ScreenRecordingFilterPageView]',
        'placed_order': 'bool',
        'screen_recording_uuids': 'list[str]',
        'screen_sizes': 'list[str]',
        'skip_filter_values': 'bool',
        'skip_hits': 'bool',
        'start_timestamp': 'ScreenRecordingFilterRangeDate',
        'tags': 'list[str]',
        'time_on_site': 'ScreenRecordingFilterRangeInteger',
        'user_agent_device_name': 'str',
        'user_agent_name': 'str',
        'user_agent_original': 'ScreenRecordingFilterStringSearch',
        'user_agent_os_name': 'str',
        'user_agent_os_version': 'str',
        'user_ip': 'ScreenRecordingFilterIpSearch',
        'watched': 'bool'
    }

    attribute_map = {
        'email': 'email',
        'email_identified': 'email_identified',
        'end_timestamp': 'end_timestamp',
        'esp_customer_uuid': 'esp_customer_uuid',
        'favorite': 'favorite',
        'geolocation': 'geolocation',
        'geolocation_country': 'geolocation_country',
        'geolocation_state': 'geolocation_state',
        'max_filter_values': 'max_filter_values',
        'order_id': 'order_id',
        'page_view_count': 'page_view_count',
        'page_views': 'page_views',
        'placed_order': 'placed_order',
        'screen_recording_uuids': 'screen_recording_uuids',
        'screen_sizes': 'screen_sizes',
        'skip_filter_values': 'skip_filter_values',
        'skip_hits': 'skip_hits',
        'start_timestamp': 'start_timestamp',
        'tags': 'tags',
        'time_on_site': 'time_on_site',
        'user_agent_device_name': 'user_agent_device_name',
        'user_agent_name': 'user_agent_name',
        'user_agent_original': 'user_agent_original',
        'user_agent_os_name': 'user_agent_os_name',
        'user_agent_os_version': 'user_agent_os_version',
        'user_ip': 'user_ip',
        'watched': 'watched'
    }

    def __init__(self, email=None, email_identified=None, end_timestamp=None, esp_customer_uuid=None, favorite=None, geolocation=None, geolocation_country=None, geolocation_state=None, max_filter_values=None, order_id=None, page_view_count=None, page_views=None, placed_order=None, screen_recording_uuids=None, screen_sizes=None, skip_filter_values=None, skip_hits=None, start_timestamp=None, tags=None, time_on_site=None, user_agent_device_name=None, user_agent_name=None, user_agent_original=None, user_agent_os_name=None, user_agent_os_version=None, user_ip=None, watched=None):  # noqa: E501
        """ScreenRecordingFilter - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._email_identified = None
        self._end_timestamp = None
        self._esp_customer_uuid = None
        self._favorite = None
        self._geolocation = None
        self._geolocation_country = None
        self._geolocation_state = None
        self._max_filter_values = None
        self._order_id = None
        self._page_view_count = None
        self._page_views = None
        self._placed_order = None
        self._screen_recording_uuids = None
        self._screen_sizes = None
        self._skip_filter_values = None
        self._skip_hits = None
        self._start_timestamp = None
        self._tags = None
        self._time_on_site = None
        self._user_agent_device_name = None
        self._user_agent_name = None
        self._user_agent_original = None
        self._user_agent_os_name = None
        self._user_agent_os_version = None
        self._user_ip = None
        self._watched = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if email_identified is not None:
            self.email_identified = email_identified
        if end_timestamp is not None:
            self.end_timestamp = end_timestamp
        if esp_customer_uuid is not None:
            self.esp_customer_uuid = esp_customer_uuid
        if favorite is not None:
            self.favorite = favorite
        if geolocation is not None:
            self.geolocation = geolocation
        if geolocation_country is not None:
            self.geolocation_country = geolocation_country
        if geolocation_state is not None:
            self.geolocation_state = geolocation_state
        if max_filter_values is not None:
            self.max_filter_values = max_filter_values
        if order_id is not None:
            self.order_id = order_id
        if page_view_count is not None:
            self.page_view_count = page_view_count
        if page_views is not None:
            self.page_views = page_views
        if placed_order is not None:
            self.placed_order = placed_order
        if screen_recording_uuids is not None:
            self.screen_recording_uuids = screen_recording_uuids
        if screen_sizes is not None:
            self.screen_sizes = screen_sizes
        if skip_filter_values is not None:
            self.skip_filter_values = skip_filter_values
        if skip_hits is not None:
            self.skip_hits = skip_hits
        if start_timestamp is not None:
            self.start_timestamp = start_timestamp
        if tags is not None:
            self.tags = tags
        if time_on_site is not None:
            self.time_on_site = time_on_site
        if user_agent_device_name is not None:
            self.user_agent_device_name = user_agent_device_name
        if user_agent_name is not None:
            self.user_agent_name = user_agent_name
        if user_agent_original is not None:
            self.user_agent_original = user_agent_original
        if user_agent_os_name is not None:
            self.user_agent_os_name = user_agent_os_name
        if user_agent_os_version is not None:
            self.user_agent_os_version = user_agent_os_version
        if user_ip is not None:
            self.user_ip = user_ip
        if watched is not None:
            self.watched = watched

    @property
    def email(self):
        """Gets the email of this ScreenRecordingFilter.  # noqa: E501


        :return: The email of this ScreenRecordingFilter.  # noqa: E501
        :rtype: ScreenRecordingFilterStringSearch
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ScreenRecordingFilter.


        :param email: The email of this ScreenRecordingFilter.  # noqa: E501
        :type: ScreenRecordingFilterStringSearch
        """

        self._email = email

    @property
    def email_identified(self):
        """Gets the email_identified of this ScreenRecordingFilter.  # noqa: E501


        :return: The email_identified of this ScreenRecordingFilter.  # noqa: E501
        :rtype: bool
        """
        return self._email_identified

    @email_identified.setter
    def email_identified(self, email_identified):
        """Sets the email_identified of this ScreenRecordingFilter.


        :param email_identified: The email_identified of this ScreenRecordingFilter.  # noqa: E501
        :type: bool
        """

        self._email_identified = email_identified

    @property
    def end_timestamp(self):
        """Gets the end_timestamp of this ScreenRecordingFilter.  # noqa: E501


        :return: The end_timestamp of this ScreenRecordingFilter.  # noqa: E501
        :rtype: ScreenRecordingFilterRangeDate
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """Sets the end_timestamp of this ScreenRecordingFilter.


        :param end_timestamp: The end_timestamp of this ScreenRecordingFilter.  # noqa: E501
        :type: ScreenRecordingFilterRangeDate
        """

        self._end_timestamp = end_timestamp

    @property
    def esp_customer_uuid(self):
        """Gets the esp_customer_uuid of this ScreenRecordingFilter.  # noqa: E501


        :return: The esp_customer_uuid of this ScreenRecordingFilter.  # noqa: E501
        :rtype: str
        """
        return self._esp_customer_uuid

    @esp_customer_uuid.setter
    def esp_customer_uuid(self, esp_customer_uuid):
        """Sets the esp_customer_uuid of this ScreenRecordingFilter.


        :param esp_customer_uuid: The esp_customer_uuid of this ScreenRecordingFilter.  # noqa: E501
        :type: str
        """

        self._esp_customer_uuid = esp_customer_uuid

    @property
    def favorite(self):
        """Gets the favorite of this ScreenRecordingFilter.  # noqa: E501


        :return: The favorite of this ScreenRecordingFilter.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this ScreenRecordingFilter.


        :param favorite: The favorite of this ScreenRecordingFilter.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

    @property
    def geolocation(self):
        """Gets the geolocation of this ScreenRecordingFilter.  # noqa: E501


        :return: The geolocation of this ScreenRecordingFilter.  # noqa: E501
        :rtype: ScreenRecordingFilterGeoDistance
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation):
        """Sets the geolocation of this ScreenRecordingFilter.


        :param geolocation: The geolocation of this ScreenRecordingFilter.  # noqa: E501
        :type: ScreenRecordingFilterGeoDistance
        """

        self._geolocation = geolocation

    @property
    def geolocation_country(self):
        """Gets the geolocation_country of this ScreenRecordingFilter.  # noqa: E501


        :return: The geolocation_country of this ScreenRecordingFilter.  # noqa: E501
        :rtype: ScreenRecordingFilterStringSearch
        """
        return self._geolocation_country

    @geolocation_country.setter
    def geolocation_country(self, geolocation_country):
        """Sets the geolocation_country of this ScreenRecordingFilter.


        :param geolocation_country: The geolocation_country of this ScreenRecordingFilter.  # noqa: E501
        :type: ScreenRecordingFilterStringSearch
        """

        self._geolocation_country = geolocation_country

    @property
    def geolocation_state(self):
        """Gets the geolocation_state of this ScreenRecordingFilter.  # noqa: E501


        :return: The geolocation_state of this ScreenRecordingFilter.  # noqa: E501
        :rtype: ScreenRecordingFilterStringSearch
        """
        return self._geolocation_state

    @geolocation_state.setter
    def geolocation_state(self, geolocation_state):
        """Sets the geolocation_state of this ScreenRecordingFilter.


        :param geolocation_state: The geolocation_state of this ScreenRecordingFilter.  # noqa: E501
        :type: ScreenRecordingFilterStringSearch
        """

        self._geolocation_state = geolocation_state

    @property
    def max_filter_values(self):
        """Gets the max_filter_values of this ScreenRecordingFilter.  # noqa: E501


        :return: The max_filter_values of this ScreenRecordingFilter.  # noqa: E501
        :rtype: int
        """
        return self._max_filter_values

    @max_filter_values.setter
    def max_filter_values(self, max_filter_values):
        """Sets the max_filter_values of this ScreenRecordingFilter.


        :param max_filter_values: The max_filter_values of this ScreenRecordingFilter.  # noqa: E501
        :type: int
        """

        self._max_filter_values = max_filter_values

    @property
    def order_id(self):
        """Gets the order_id of this ScreenRecordingFilter.  # noqa: E501


        :return: The order_id of this ScreenRecordingFilter.  # noqa: E501
        :rtype: ScreenRecordingFilterStringSearch
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ScreenRecordingFilter.


        :param order_id: The order_id of this ScreenRecordingFilter.  # noqa: E501
        :type: ScreenRecordingFilterStringSearch
        """

        self._order_id = order_id

    @property
    def page_view_count(self):
        """Gets the page_view_count of this ScreenRecordingFilter.  # noqa: E501


        :return: The page_view_count of this ScreenRecordingFilter.  # noqa: E501
        :rtype: ScreenRecordingFilterRangeInteger
        """
        return self._page_view_count

    @page_view_count.setter
    def page_view_count(self, page_view_count):
        """Sets the page_view_count of this ScreenRecordingFilter.


        :param page_view_count: The page_view_count of this ScreenRecordingFilter.  # noqa: E501
        :type: ScreenRecordingFilterRangeInteger
        """

        self._page_view_count = page_view_count

    @property
    def page_views(self):
        """Gets the page_views of this ScreenRecordingFilter.  # noqa: E501


        :return: The page_views of this ScreenRecordingFilter.  # noqa: E501
        :rtype: list[ScreenRecordingFilterPageView]
        """
        return self._page_views

    @page_views.setter
    def page_views(self, page_views):
        """Sets the page_views of this ScreenRecordingFilter.


        :param page_views: The page_views of this ScreenRecordingFilter.  # noqa: E501
        :type: list[ScreenRecordingFilterPageView]
        """

        self._page_views = page_views

    @property
    def placed_order(self):
        """Gets the placed_order of this ScreenRecordingFilter.  # noqa: E501


        :return: The placed_order of this ScreenRecordingFilter.  # noqa: E501
        :rtype: bool
        """
        return self._placed_order

    @placed_order.setter
    def placed_order(self, placed_order):
        """Sets the placed_order of this ScreenRecordingFilter.


        :param placed_order: The placed_order of this ScreenRecordingFilter.  # noqa: E501
        :type: bool
        """

        self._placed_order = placed_order

    @property
    def screen_recording_uuids(self):
        """Gets the screen_recording_uuids of this ScreenRecordingFilter.  # noqa: E501


        :return: The screen_recording_uuids of this ScreenRecordingFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._screen_recording_uuids

    @screen_recording_uuids.setter
    def screen_recording_uuids(self, screen_recording_uuids):
        """Sets the screen_recording_uuids of this ScreenRecordingFilter.


        :param screen_recording_uuids: The screen_recording_uuids of this ScreenRecordingFilter.  # noqa: E501
        :type: list[str]
        """

        self._screen_recording_uuids = screen_recording_uuids

    @property
    def screen_sizes(self):
        """Gets the screen_sizes of this ScreenRecordingFilter.  # noqa: E501


        :return: The screen_sizes of this ScreenRecordingFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._screen_sizes

    @screen_sizes.setter
    def screen_sizes(self, screen_sizes):
        """Sets the screen_sizes of this ScreenRecordingFilter.


        :param screen_sizes: The screen_sizes of this ScreenRecordingFilter.  # noqa: E501
        :type: list[str]
        """

        self._screen_sizes = screen_sizes

    @property
    def skip_filter_values(self):
        """Gets the skip_filter_values of this ScreenRecordingFilter.  # noqa: E501


        :return: The skip_filter_values of this ScreenRecordingFilter.  # noqa: E501
        :rtype: bool
        """
        return self._skip_filter_values

    @skip_filter_values.setter
    def skip_filter_values(self, skip_filter_values):
        """Sets the skip_filter_values of this ScreenRecordingFilter.


        :param skip_filter_values: The skip_filter_values of this ScreenRecordingFilter.  # noqa: E501
        :type: bool
        """

        self._skip_filter_values = skip_filter_values

    @property
    def skip_hits(self):
        """Gets the skip_hits of this ScreenRecordingFilter.  # noqa: E501


        :return: The skip_hits of this ScreenRecordingFilter.  # noqa: E501
        :rtype: bool
        """
        return self._skip_hits

    @skip_hits.setter
    def skip_hits(self, skip_hits):
        """Sets the skip_hits of this ScreenRecordingFilter.


        :param skip_hits: The skip_hits of this ScreenRecordingFilter.  # noqa: E501
        :type: bool
        """

        self._skip_hits = skip_hits

    @property
    def start_timestamp(self):
        """Gets the start_timestamp of this ScreenRecordingFilter.  # noqa: E501


        :return: The start_timestamp of this ScreenRecordingFilter.  # noqa: E501
        :rtype: ScreenRecordingFilterRangeDate
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """Sets the start_timestamp of this ScreenRecordingFilter.


        :param start_timestamp: The start_timestamp of this ScreenRecordingFilter.  # noqa: E501
        :type: ScreenRecordingFilterRangeDate
        """

        self._start_timestamp = start_timestamp

    @property
    def tags(self):
        """Gets the tags of this ScreenRecordingFilter.  # noqa: E501


        :return: The tags of this ScreenRecordingFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ScreenRecordingFilter.


        :param tags: The tags of this ScreenRecordingFilter.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def time_on_site(self):
        """Gets the time_on_site of this ScreenRecordingFilter.  # noqa: E501


        :return: The time_on_site of this ScreenRecordingFilter.  # noqa: E501
        :rtype: ScreenRecordingFilterRangeInteger
        """
        return self._time_on_site

    @time_on_site.setter
    def time_on_site(self, time_on_site):
        """Sets the time_on_site of this ScreenRecordingFilter.


        :param time_on_site: The time_on_site of this ScreenRecordingFilter.  # noqa: E501
        :type: ScreenRecordingFilterRangeInteger
        """

        self._time_on_site = time_on_site

    @property
    def user_agent_device_name(self):
        """Gets the user_agent_device_name of this ScreenRecordingFilter.  # noqa: E501


        :return: The user_agent_device_name of this ScreenRecordingFilter.  # noqa: E501
        :rtype: str
        """
        return self._user_agent_device_name

    @user_agent_device_name.setter
    def user_agent_device_name(self, user_agent_device_name):
        """Sets the user_agent_device_name of this ScreenRecordingFilter.


        :param user_agent_device_name: The user_agent_device_name of this ScreenRecordingFilter.  # noqa: E501
        :type: str
        """

        self._user_agent_device_name = user_agent_device_name

    @property
    def user_agent_name(self):
        """Gets the user_agent_name of this ScreenRecordingFilter.  # noqa: E501


        :return: The user_agent_name of this ScreenRecordingFilter.  # noqa: E501
        :rtype: str
        """
        return self._user_agent_name

    @user_agent_name.setter
    def user_agent_name(self, user_agent_name):
        """Sets the user_agent_name of this ScreenRecordingFilter.


        :param user_agent_name: The user_agent_name of this ScreenRecordingFilter.  # noqa: E501
        :type: str
        """

        self._user_agent_name = user_agent_name

    @property
    def user_agent_original(self):
        """Gets the user_agent_original of this ScreenRecordingFilter.  # noqa: E501


        :return: The user_agent_original of this ScreenRecordingFilter.  # noqa: E501
        :rtype: ScreenRecordingFilterStringSearch
        """
        return self._user_agent_original

    @user_agent_original.setter
    def user_agent_original(self, user_agent_original):
        """Sets the user_agent_original of this ScreenRecordingFilter.


        :param user_agent_original: The user_agent_original of this ScreenRecordingFilter.  # noqa: E501
        :type: ScreenRecordingFilterStringSearch
        """

        self._user_agent_original = user_agent_original

    @property
    def user_agent_os_name(self):
        """Gets the user_agent_os_name of this ScreenRecordingFilter.  # noqa: E501


        :return: The user_agent_os_name of this ScreenRecordingFilter.  # noqa: E501
        :rtype: str
        """
        return self._user_agent_os_name

    @user_agent_os_name.setter
    def user_agent_os_name(self, user_agent_os_name):
        """Sets the user_agent_os_name of this ScreenRecordingFilter.


        :param user_agent_os_name: The user_agent_os_name of this ScreenRecordingFilter.  # noqa: E501
        :type: str
        """

        self._user_agent_os_name = user_agent_os_name

    @property
    def user_agent_os_version(self):
        """Gets the user_agent_os_version of this ScreenRecordingFilter.  # noqa: E501


        :return: The user_agent_os_version of this ScreenRecordingFilter.  # noqa: E501
        :rtype: str
        """
        return self._user_agent_os_version

    @user_agent_os_version.setter
    def user_agent_os_version(self, user_agent_os_version):
        """Sets the user_agent_os_version of this ScreenRecordingFilter.


        :param user_agent_os_version: The user_agent_os_version of this ScreenRecordingFilter.  # noqa: E501
        :type: str
        """

        self._user_agent_os_version = user_agent_os_version

    @property
    def user_ip(self):
        """Gets the user_ip of this ScreenRecordingFilter.  # noqa: E501


        :return: The user_ip of this ScreenRecordingFilter.  # noqa: E501
        :rtype: ScreenRecordingFilterIpSearch
        """
        return self._user_ip

    @user_ip.setter
    def user_ip(self, user_ip):
        """Sets the user_ip of this ScreenRecordingFilter.


        :param user_ip: The user_ip of this ScreenRecordingFilter.  # noqa: E501
        :type: ScreenRecordingFilterIpSearch
        """

        self._user_ip = user_ip

    @property
    def watched(self):
        """Gets the watched of this ScreenRecordingFilter.  # noqa: E501


        :return: The watched of this ScreenRecordingFilter.  # noqa: E501
        :rtype: bool
        """
        return self._watched

    @watched.setter
    def watched(self, watched):
        """Sets the watched of this ScreenRecordingFilter.


        :param watched: The watched of this ScreenRecordingFilter.  # noqa: E501
        :type: bool
        """

        self._watched = watched

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
        if issubclass(ScreenRecordingFilter, dict):
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
        if not isinstance(other, ScreenRecordingFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
