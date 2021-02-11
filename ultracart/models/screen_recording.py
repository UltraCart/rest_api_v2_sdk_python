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


class ScreenRecording(object):
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
        'analytics_client_oid': 'int',
        'analytics_session_dts': 'int',
        'analytics_session_oid': 'int',
        'email': 'str',
        'end_timestamp': 'str',
        'esp_customer_uuid': 'str',
        'events_gz_size': 'int',
        'events_json_key': 'str',
        'favorite': 'bool',
        'favorites': 'list[int]',
        'geolocation': 'GeoPoint',
        'geolocation_country': 'str',
        'geolocation_state': 'str',
        'merchant_id': 'str',
        'order_id': 'str',
        'page_view_count': 'int',
        'page_views': 'list[ScreenRecordingPageView]',
        'rrweb_version': 'str',
        'screen_recording_uuid': 'str',
        'signed_download_url': 'str',
        'start_timestamp': 'str',
        'storefront_oids': 'list[int]',
        'storefronts': 'list[ScreenRecordingStoreFront]',
        'tags': 'list[str]',
        'time_on_site': 'int',
        'ucacid': 'str',
        'user_agent': 'ScreenRecordingUserAgent',
        'user_agent_raw': 'str',
        'user_ip': 'str',
        'user_properties': 'list[ScreenRecordingUserProperty]',
        'watched': 'bool',
        'window_height': 'int',
        'window_width': 'int'
    }

    attribute_map = {
        'analytics_client_oid': 'analytics_client_oid',
        'analytics_session_dts': 'analytics_session_dts',
        'analytics_session_oid': 'analytics_session_oid',
        'email': 'email',
        'end_timestamp': 'end_timestamp',
        'esp_customer_uuid': 'esp_customer_uuid',
        'events_gz_size': 'events_gz_size',
        'events_json_key': 'events_json_key',
        'favorite': 'favorite',
        'favorites': 'favorites',
        'geolocation': 'geolocation',
        'geolocation_country': 'geolocation_country',
        'geolocation_state': 'geolocation_state',
        'merchant_id': 'merchant_id',
        'order_id': 'order_id',
        'page_view_count': 'page_view_count',
        'page_views': 'page_views',
        'rrweb_version': 'rrweb_version',
        'screen_recording_uuid': 'screen_recording_uuid',
        'signed_download_url': 'signed_download_url',
        'start_timestamp': 'start_timestamp',
        'storefront_oids': 'storefront_oids',
        'storefronts': 'storefronts',
        'tags': 'tags',
        'time_on_site': 'time_on_site',
        'ucacid': 'ucacid',
        'user_agent': 'user_agent',
        'user_agent_raw': 'user_agent_raw',
        'user_ip': 'user_ip',
        'user_properties': 'user_properties',
        'watched': 'watched',
        'window_height': 'window_height',
        'window_width': 'window_width'
    }

    def __init__(self, analytics_client_oid=None, analytics_session_dts=None, analytics_session_oid=None, email=None, end_timestamp=None, esp_customer_uuid=None, events_gz_size=None, events_json_key=None, favorite=None, favorites=None, geolocation=None, geolocation_country=None, geolocation_state=None, merchant_id=None, order_id=None, page_view_count=None, page_views=None, rrweb_version=None, screen_recording_uuid=None, signed_download_url=None, start_timestamp=None, storefront_oids=None, storefronts=None, tags=None, time_on_site=None, ucacid=None, user_agent=None, user_agent_raw=None, user_ip=None, user_properties=None, watched=None, window_height=None, window_width=None):  # noqa: E501
        """ScreenRecording - a model defined in Swagger"""  # noqa: E501

        self._analytics_client_oid = None
        self._analytics_session_dts = None
        self._analytics_session_oid = None
        self._email = None
        self._end_timestamp = None
        self._esp_customer_uuid = None
        self._events_gz_size = None
        self._events_json_key = None
        self._favorite = None
        self._favorites = None
        self._geolocation = None
        self._geolocation_country = None
        self._geolocation_state = None
        self._merchant_id = None
        self._order_id = None
        self._page_view_count = None
        self._page_views = None
        self._rrweb_version = None
        self._screen_recording_uuid = None
        self._signed_download_url = None
        self._start_timestamp = None
        self._storefront_oids = None
        self._storefronts = None
        self._tags = None
        self._time_on_site = None
        self._ucacid = None
        self._user_agent = None
        self._user_agent_raw = None
        self._user_ip = None
        self._user_properties = None
        self._watched = None
        self._window_height = None
        self._window_width = None
        self.discriminator = None

        if analytics_client_oid is not None:
            self.analytics_client_oid = analytics_client_oid
        if analytics_session_dts is not None:
            self.analytics_session_dts = analytics_session_dts
        if analytics_session_oid is not None:
            self.analytics_session_oid = analytics_session_oid
        if email is not None:
            self.email = email
        if end_timestamp is not None:
            self.end_timestamp = end_timestamp
        if esp_customer_uuid is not None:
            self.esp_customer_uuid = esp_customer_uuid
        if events_gz_size is not None:
            self.events_gz_size = events_gz_size
        if events_json_key is not None:
            self.events_json_key = events_json_key
        if favorite is not None:
            self.favorite = favorite
        if favorites is not None:
            self.favorites = favorites
        if geolocation is not None:
            self.geolocation = geolocation
        if geolocation_country is not None:
            self.geolocation_country = geolocation_country
        if geolocation_state is not None:
            self.geolocation_state = geolocation_state
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if order_id is not None:
            self.order_id = order_id
        if page_view_count is not None:
            self.page_view_count = page_view_count
        if page_views is not None:
            self.page_views = page_views
        if rrweb_version is not None:
            self.rrweb_version = rrweb_version
        if screen_recording_uuid is not None:
            self.screen_recording_uuid = screen_recording_uuid
        if signed_download_url is not None:
            self.signed_download_url = signed_download_url
        if start_timestamp is not None:
            self.start_timestamp = start_timestamp
        if storefront_oids is not None:
            self.storefront_oids = storefront_oids
        if storefronts is not None:
            self.storefronts = storefronts
        if tags is not None:
            self.tags = tags
        if time_on_site is not None:
            self.time_on_site = time_on_site
        if ucacid is not None:
            self.ucacid = ucacid
        if user_agent is not None:
            self.user_agent = user_agent
        if user_agent_raw is not None:
            self.user_agent_raw = user_agent_raw
        if user_ip is not None:
            self.user_ip = user_ip
        if user_properties is not None:
            self.user_properties = user_properties
        if watched is not None:
            self.watched = watched
        if window_height is not None:
            self.window_height = window_height
        if window_width is not None:
            self.window_width = window_width

    @property
    def analytics_client_oid(self):
        """Gets the analytics_client_oid of this ScreenRecording.  # noqa: E501


        :return: The analytics_client_oid of this ScreenRecording.  # noqa: E501
        :rtype: int
        """
        return self._analytics_client_oid

    @analytics_client_oid.setter
    def analytics_client_oid(self, analytics_client_oid):
        """Sets the analytics_client_oid of this ScreenRecording.


        :param analytics_client_oid: The analytics_client_oid of this ScreenRecording.  # noqa: E501
        :type: int
        """

        self._analytics_client_oid = analytics_client_oid

    @property
    def analytics_session_dts(self):
        """Gets the analytics_session_dts of this ScreenRecording.  # noqa: E501


        :return: The analytics_session_dts of this ScreenRecording.  # noqa: E501
        :rtype: int
        """
        return self._analytics_session_dts

    @analytics_session_dts.setter
    def analytics_session_dts(self, analytics_session_dts):
        """Sets the analytics_session_dts of this ScreenRecording.


        :param analytics_session_dts: The analytics_session_dts of this ScreenRecording.  # noqa: E501
        :type: int
        """

        self._analytics_session_dts = analytics_session_dts

    @property
    def analytics_session_oid(self):
        """Gets the analytics_session_oid of this ScreenRecording.  # noqa: E501


        :return: The analytics_session_oid of this ScreenRecording.  # noqa: E501
        :rtype: int
        """
        return self._analytics_session_oid

    @analytics_session_oid.setter
    def analytics_session_oid(self, analytics_session_oid):
        """Sets the analytics_session_oid of this ScreenRecording.


        :param analytics_session_oid: The analytics_session_oid of this ScreenRecording.  # noqa: E501
        :type: int
        """

        self._analytics_session_oid = analytics_session_oid

    @property
    def email(self):
        """Gets the email of this ScreenRecording.  # noqa: E501


        :return: The email of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ScreenRecording.


        :param email: The email of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def end_timestamp(self):
        """Gets the end_timestamp of this ScreenRecording.  # noqa: E501

        Ending timestamp  # noqa: E501

        :return: The end_timestamp of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """Sets the end_timestamp of this ScreenRecording.

        Ending timestamp  # noqa: E501

        :param end_timestamp: The end_timestamp of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._end_timestamp = end_timestamp

    @property
    def esp_customer_uuid(self):
        """Gets the esp_customer_uuid of this ScreenRecording.  # noqa: E501


        :return: The esp_customer_uuid of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._esp_customer_uuid

    @esp_customer_uuid.setter
    def esp_customer_uuid(self, esp_customer_uuid):
        """Sets the esp_customer_uuid of this ScreenRecording.


        :param esp_customer_uuid: The esp_customer_uuid of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._esp_customer_uuid = esp_customer_uuid

    @property
    def events_gz_size(self):
        """Gets the events_gz_size of this ScreenRecording.  # noqa: E501


        :return: The events_gz_size of this ScreenRecording.  # noqa: E501
        :rtype: int
        """
        return self._events_gz_size

    @events_gz_size.setter
    def events_gz_size(self, events_gz_size):
        """Sets the events_gz_size of this ScreenRecording.


        :param events_gz_size: The events_gz_size of this ScreenRecording.  # noqa: E501
        :type: int
        """

        self._events_gz_size = events_gz_size

    @property
    def events_json_key(self):
        """Gets the events_json_key of this ScreenRecording.  # noqa: E501


        :return: The events_json_key of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._events_json_key

    @events_json_key.setter
    def events_json_key(self, events_json_key):
        """Sets the events_json_key of this ScreenRecording.


        :param events_json_key: The events_json_key of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._events_json_key = events_json_key

    @property
    def favorite(self):
        """Gets the favorite of this ScreenRecording.  # noqa: E501

        True if the user calling the API has favorited this particular screen recording.  # noqa: E501

        :return: The favorite of this ScreenRecording.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this ScreenRecording.

        True if the user calling the API has favorited this particular screen recording.  # noqa: E501

        :param favorite: The favorite of this ScreenRecording.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

    @property
    def favorites(self):
        """Gets the favorites of this ScreenRecording.  # noqa: E501

        Array of user ids that favorited this particular screen recording.  # noqa: E501

        :return: The favorites of this ScreenRecording.  # noqa: E501
        :rtype: list[int]
        """
        return self._favorites

    @favorites.setter
    def favorites(self, favorites):
        """Sets the favorites of this ScreenRecording.

        Array of user ids that favorited this particular screen recording.  # noqa: E501

        :param favorites: The favorites of this ScreenRecording.  # noqa: E501
        :type: list[int]
        """

        self._favorites = favorites

    @property
    def geolocation(self):
        """Gets the geolocation of this ScreenRecording.  # noqa: E501


        :return: The geolocation of this ScreenRecording.  # noqa: E501
        :rtype: GeoPoint
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation):
        """Sets the geolocation of this ScreenRecording.


        :param geolocation: The geolocation of this ScreenRecording.  # noqa: E501
        :type: GeoPoint
        """

        self._geolocation = geolocation

    @property
    def geolocation_country(self):
        """Gets the geolocation_country of this ScreenRecording.  # noqa: E501


        :return: The geolocation_country of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._geolocation_country

    @geolocation_country.setter
    def geolocation_country(self, geolocation_country):
        """Sets the geolocation_country of this ScreenRecording.


        :param geolocation_country: The geolocation_country of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._geolocation_country = geolocation_country

    @property
    def geolocation_state(self):
        """Gets the geolocation_state of this ScreenRecording.  # noqa: E501


        :return: The geolocation_state of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._geolocation_state

    @geolocation_state.setter
    def geolocation_state(self, geolocation_state):
        """Sets the geolocation_state of this ScreenRecording.


        :param geolocation_state: The geolocation_state of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._geolocation_state = geolocation_state

    @property
    def merchant_id(self):
        """Gets the merchant_id of this ScreenRecording.  # noqa: E501


        :return: The merchant_id of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this ScreenRecording.


        :param merchant_id: The merchant_id of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def order_id(self):
        """Gets the order_id of this ScreenRecording.  # noqa: E501


        :return: The order_id of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ScreenRecording.


        :param order_id: The order_id of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def page_view_count(self):
        """Gets the page_view_count of this ScreenRecording.  # noqa: E501


        :return: The page_view_count of this ScreenRecording.  # noqa: E501
        :rtype: int
        """
        return self._page_view_count

    @page_view_count.setter
    def page_view_count(self, page_view_count):
        """Sets the page_view_count of this ScreenRecording.


        :param page_view_count: The page_view_count of this ScreenRecording.  # noqa: E501
        :type: int
        """

        self._page_view_count = page_view_count

    @property
    def page_views(self):
        """Gets the page_views of this ScreenRecording.  # noqa: E501


        :return: The page_views of this ScreenRecording.  # noqa: E501
        :rtype: list[ScreenRecordingPageView]
        """
        return self._page_views

    @page_views.setter
    def page_views(self, page_views):
        """Sets the page_views of this ScreenRecording.


        :param page_views: The page_views of this ScreenRecording.  # noqa: E501
        :type: list[ScreenRecordingPageView]
        """

        self._page_views = page_views

    @property
    def rrweb_version(self):
        """Gets the rrweb_version of this ScreenRecording.  # noqa: E501


        :return: The rrweb_version of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._rrweb_version

    @rrweb_version.setter
    def rrweb_version(self, rrweb_version):
        """Sets the rrweb_version of this ScreenRecording.


        :param rrweb_version: The rrweb_version of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._rrweb_version = rrweb_version

    @property
    def screen_recording_uuid(self):
        """Gets the screen_recording_uuid of this ScreenRecording.  # noqa: E501


        :return: The screen_recording_uuid of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._screen_recording_uuid

    @screen_recording_uuid.setter
    def screen_recording_uuid(self, screen_recording_uuid):
        """Sets the screen_recording_uuid of this ScreenRecording.


        :param screen_recording_uuid: The screen_recording_uuid of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._screen_recording_uuid = screen_recording_uuid

    @property
    def signed_download_url(self):
        """Gets the signed_download_url of this ScreenRecording.  # noqa: E501


        :return: The signed_download_url of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._signed_download_url

    @signed_download_url.setter
    def signed_download_url(self, signed_download_url):
        """Sets the signed_download_url of this ScreenRecording.


        :param signed_download_url: The signed_download_url of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._signed_download_url = signed_download_url

    @property
    def start_timestamp(self):
        """Gets the start_timestamp of this ScreenRecording.  # noqa: E501

        Starting timestamp  # noqa: E501

        :return: The start_timestamp of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """Sets the start_timestamp of this ScreenRecording.

        Starting timestamp  # noqa: E501

        :param start_timestamp: The start_timestamp of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._start_timestamp = start_timestamp

    @property
    def storefront_oids(self):
        """Gets the storefront_oids of this ScreenRecording.  # noqa: E501


        :return: The storefront_oids of this ScreenRecording.  # noqa: E501
        :rtype: list[int]
        """
        return self._storefront_oids

    @storefront_oids.setter
    def storefront_oids(self, storefront_oids):
        """Sets the storefront_oids of this ScreenRecording.


        :param storefront_oids: The storefront_oids of this ScreenRecording.  # noqa: E501
        :type: list[int]
        """

        self._storefront_oids = storefront_oids

    @property
    def storefronts(self):
        """Gets the storefronts of this ScreenRecording.  # noqa: E501


        :return: The storefronts of this ScreenRecording.  # noqa: E501
        :rtype: list[ScreenRecordingStoreFront]
        """
        return self._storefronts

    @storefronts.setter
    def storefronts(self, storefronts):
        """Sets the storefronts of this ScreenRecording.


        :param storefronts: The storefronts of this ScreenRecording.  # noqa: E501
        :type: list[ScreenRecordingStoreFront]
        """

        self._storefronts = storefronts

    @property
    def tags(self):
        """Gets the tags of this ScreenRecording.  # noqa: E501


        :return: The tags of this ScreenRecording.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ScreenRecording.


        :param tags: The tags of this ScreenRecording.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def time_on_site(self):
        """Gets the time_on_site of this ScreenRecording.  # noqa: E501


        :return: The time_on_site of this ScreenRecording.  # noqa: E501
        :rtype: int
        """
        return self._time_on_site

    @time_on_site.setter
    def time_on_site(self, time_on_site):
        """Sets the time_on_site of this ScreenRecording.


        :param time_on_site: The time_on_site of this ScreenRecording.  # noqa: E501
        :type: int
        """

        self._time_on_site = time_on_site

    @property
    def ucacid(self):
        """Gets the ucacid of this ScreenRecording.  # noqa: E501


        :return: The ucacid of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._ucacid

    @ucacid.setter
    def ucacid(self, ucacid):
        """Sets the ucacid of this ScreenRecording.


        :param ucacid: The ucacid of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._ucacid = ucacid

    @property
    def user_agent(self):
        """Gets the user_agent of this ScreenRecording.  # noqa: E501


        :return: The user_agent of this ScreenRecording.  # noqa: E501
        :rtype: ScreenRecordingUserAgent
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this ScreenRecording.


        :param user_agent: The user_agent of this ScreenRecording.  # noqa: E501
        :type: ScreenRecordingUserAgent
        """

        self._user_agent = user_agent

    @property
    def user_agent_raw(self):
        """Gets the user_agent_raw of this ScreenRecording.  # noqa: E501


        :return: The user_agent_raw of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._user_agent_raw

    @user_agent_raw.setter
    def user_agent_raw(self, user_agent_raw):
        """Sets the user_agent_raw of this ScreenRecording.


        :param user_agent_raw: The user_agent_raw of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._user_agent_raw = user_agent_raw

    @property
    def user_ip(self):
        """Gets the user_ip of this ScreenRecording.  # noqa: E501


        :return: The user_ip of this ScreenRecording.  # noqa: E501
        :rtype: str
        """
        return self._user_ip

    @user_ip.setter
    def user_ip(self, user_ip):
        """Sets the user_ip of this ScreenRecording.


        :param user_ip: The user_ip of this ScreenRecording.  # noqa: E501
        :type: str
        """

        self._user_ip = user_ip

    @property
    def user_properties(self):
        """Gets the user_properties of this ScreenRecording.  # noqa: E501


        :return: The user_properties of this ScreenRecording.  # noqa: E501
        :rtype: list[ScreenRecordingUserProperty]
        """
        return self._user_properties

    @user_properties.setter
    def user_properties(self, user_properties):
        """Sets the user_properties of this ScreenRecording.


        :param user_properties: The user_properties of this ScreenRecording.  # noqa: E501
        :type: list[ScreenRecordingUserProperty]
        """

        self._user_properties = user_properties

    @property
    def watched(self):
        """Gets the watched of this ScreenRecording.  # noqa: E501


        :return: The watched of this ScreenRecording.  # noqa: E501
        :rtype: bool
        """
        return self._watched

    @watched.setter
    def watched(self, watched):
        """Sets the watched of this ScreenRecording.


        :param watched: The watched of this ScreenRecording.  # noqa: E501
        :type: bool
        """

        self._watched = watched

    @property
    def window_height(self):
        """Gets the window_height of this ScreenRecording.  # noqa: E501


        :return: The window_height of this ScreenRecording.  # noqa: E501
        :rtype: int
        """
        return self._window_height

    @window_height.setter
    def window_height(self, window_height):
        """Sets the window_height of this ScreenRecording.


        :param window_height: The window_height of this ScreenRecording.  # noqa: E501
        :type: int
        """

        self._window_height = window_height

    @property
    def window_width(self):
        """Gets the window_width of this ScreenRecording.  # noqa: E501


        :return: The window_width of this ScreenRecording.  # noqa: E501
        :rtype: int
        """
        return self._window_width

    @window_width.setter
    def window_width(self, window_width):
        """Sets the window_width of this ScreenRecording.


        :param window_width: The window_width of this ScreenRecording.  # noqa: E501
        :type: int
        """

        self._window_width = window_width

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
        if issubclass(ScreenRecording, dict):
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
        if not isinstance(other, ScreenRecording):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
