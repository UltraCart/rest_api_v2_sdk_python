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


class EmailSettings(object):
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
        'emails_per_day': 'int',
        'emails_per_hour': 'int',
        'emails_per_month': 'int',
        'marketing_esp_domain_user': 'str',
        'marketing_esp_domain_uuid': 'str',
        'marketing_esp_friendly_name': 'str',
        'postcard_from_address1': 'str',
        'postcard_from_address2': 'str',
        'postcard_from_city': 'str',
        'postcard_from_name': 'str',
        'postcard_from_postal_code': 'str',
        'postcard_from_state': 'str',
        'require_order_within_last': 'int',
        'reviews_io_configured': 'bool',
        'sms_esp_twilio_uuid': 'str',
        'sms_phone_number': 'str',
        'transactional_esp_domain_user': 'str',
        'transactional_esp_domain_uuid': 'str',
        'transactional_esp_friendly_name': 'str'
    }

    attribute_map = {
        'emails_per_day': 'emails_per_day',
        'emails_per_hour': 'emails_per_hour',
        'emails_per_month': 'emails_per_month',
        'marketing_esp_domain_user': 'marketing_esp_domain_user',
        'marketing_esp_domain_uuid': 'marketing_esp_domain_uuid',
        'marketing_esp_friendly_name': 'marketing_esp_friendly_name',
        'postcard_from_address1': 'postcard_from_address1',
        'postcard_from_address2': 'postcard_from_address2',
        'postcard_from_city': 'postcard_from_city',
        'postcard_from_name': 'postcard_from_name',
        'postcard_from_postal_code': 'postcard_from_postal_code',
        'postcard_from_state': 'postcard_from_state',
        'require_order_within_last': 'require_order_within_last',
        'reviews_io_configured': 'reviews_io_configured',
        'sms_esp_twilio_uuid': 'sms_esp_twilio_uuid',
        'sms_phone_number': 'sms_phone_number',
        'transactional_esp_domain_user': 'transactional_esp_domain_user',
        'transactional_esp_domain_uuid': 'transactional_esp_domain_uuid',
        'transactional_esp_friendly_name': 'transactional_esp_friendly_name'
    }

    def __init__(self, emails_per_day=None, emails_per_hour=None, emails_per_month=None, marketing_esp_domain_user=None, marketing_esp_domain_uuid=None, marketing_esp_friendly_name=None, postcard_from_address1=None, postcard_from_address2=None, postcard_from_city=None, postcard_from_name=None, postcard_from_postal_code=None, postcard_from_state=None, require_order_within_last=None, reviews_io_configured=None, sms_esp_twilio_uuid=None, sms_phone_number=None, transactional_esp_domain_user=None, transactional_esp_domain_uuid=None, transactional_esp_friendly_name=None):  # noqa: E501
        """EmailSettings - a model defined in Swagger"""  # noqa: E501

        self._emails_per_day = None
        self._emails_per_hour = None
        self._emails_per_month = None
        self._marketing_esp_domain_user = None
        self._marketing_esp_domain_uuid = None
        self._marketing_esp_friendly_name = None
        self._postcard_from_address1 = None
        self._postcard_from_address2 = None
        self._postcard_from_city = None
        self._postcard_from_name = None
        self._postcard_from_postal_code = None
        self._postcard_from_state = None
        self._require_order_within_last = None
        self._reviews_io_configured = None
        self._sms_esp_twilio_uuid = None
        self._sms_phone_number = None
        self._transactional_esp_domain_user = None
        self._transactional_esp_domain_uuid = None
        self._transactional_esp_friendly_name = None
        self.discriminator = None

        if emails_per_day is not None:
            self.emails_per_day = emails_per_day
        if emails_per_hour is not None:
            self.emails_per_hour = emails_per_hour
        if emails_per_month is not None:
            self.emails_per_month = emails_per_month
        if marketing_esp_domain_user is not None:
            self.marketing_esp_domain_user = marketing_esp_domain_user
        if marketing_esp_domain_uuid is not None:
            self.marketing_esp_domain_uuid = marketing_esp_domain_uuid
        if marketing_esp_friendly_name is not None:
            self.marketing_esp_friendly_name = marketing_esp_friendly_name
        if postcard_from_address1 is not None:
            self.postcard_from_address1 = postcard_from_address1
        if postcard_from_address2 is not None:
            self.postcard_from_address2 = postcard_from_address2
        if postcard_from_city is not None:
            self.postcard_from_city = postcard_from_city
        if postcard_from_name is not None:
            self.postcard_from_name = postcard_from_name
        if postcard_from_postal_code is not None:
            self.postcard_from_postal_code = postcard_from_postal_code
        if postcard_from_state is not None:
            self.postcard_from_state = postcard_from_state
        if require_order_within_last is not None:
            self.require_order_within_last = require_order_within_last
        if reviews_io_configured is not None:
            self.reviews_io_configured = reviews_io_configured
        if sms_esp_twilio_uuid is not None:
            self.sms_esp_twilio_uuid = sms_esp_twilio_uuid
        if sms_phone_number is not None:
            self.sms_phone_number = sms_phone_number
        if transactional_esp_domain_user is not None:
            self.transactional_esp_domain_user = transactional_esp_domain_user
        if transactional_esp_domain_uuid is not None:
            self.transactional_esp_domain_uuid = transactional_esp_domain_uuid
        if transactional_esp_friendly_name is not None:
            self.transactional_esp_friendly_name = transactional_esp_friendly_name

    @property
    def emails_per_day(self):
        """Gets the emails_per_day of this EmailSettings.  # noqa: E501

        Emails per day allowed  # noqa: E501

        :return: The emails_per_day of this EmailSettings.  # noqa: E501
        :rtype: int
        """
        return self._emails_per_day

    @emails_per_day.setter
    def emails_per_day(self, emails_per_day):
        """Sets the emails_per_day of this EmailSettings.

        Emails per day allowed  # noqa: E501

        :param emails_per_day: The emails_per_day of this EmailSettings.  # noqa: E501
        :type: int
        """

        self._emails_per_day = emails_per_day

    @property
    def emails_per_hour(self):
        """Gets the emails_per_hour of this EmailSettings.  # noqa: E501

        Emails per hour allowed  # noqa: E501

        :return: The emails_per_hour of this EmailSettings.  # noqa: E501
        :rtype: int
        """
        return self._emails_per_hour

    @emails_per_hour.setter
    def emails_per_hour(self, emails_per_hour):
        """Sets the emails_per_hour of this EmailSettings.

        Emails per hour allowed  # noqa: E501

        :param emails_per_hour: The emails_per_hour of this EmailSettings.  # noqa: E501
        :type: int
        """

        self._emails_per_hour = emails_per_hour

    @property
    def emails_per_month(self):
        """Gets the emails_per_month of this EmailSettings.  # noqa: E501

        Emails per month allowed  # noqa: E501

        :return: The emails_per_month of this EmailSettings.  # noqa: E501
        :rtype: int
        """
        return self._emails_per_month

    @emails_per_month.setter
    def emails_per_month(self, emails_per_month):
        """Sets the emails_per_month of this EmailSettings.

        Emails per month allowed  # noqa: E501

        :param emails_per_month: The emails_per_month of this EmailSettings.  # noqa: E501
        :type: int
        """

        self._emails_per_month = emails_per_month

    @property
    def marketing_esp_domain_user(self):
        """Gets the marketing_esp_domain_user of this EmailSettings.  # noqa: E501


        :return: The marketing_esp_domain_user of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._marketing_esp_domain_user

    @marketing_esp_domain_user.setter
    def marketing_esp_domain_user(self, marketing_esp_domain_user):
        """Sets the marketing_esp_domain_user of this EmailSettings.


        :param marketing_esp_domain_user: The marketing_esp_domain_user of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._marketing_esp_domain_user = marketing_esp_domain_user

    @property
    def marketing_esp_domain_uuid(self):
        """Gets the marketing_esp_domain_uuid of this EmailSettings.  # noqa: E501


        :return: The marketing_esp_domain_uuid of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._marketing_esp_domain_uuid

    @marketing_esp_domain_uuid.setter
    def marketing_esp_domain_uuid(self, marketing_esp_domain_uuid):
        """Sets the marketing_esp_domain_uuid of this EmailSettings.


        :param marketing_esp_domain_uuid: The marketing_esp_domain_uuid of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._marketing_esp_domain_uuid = marketing_esp_domain_uuid

    @property
    def marketing_esp_friendly_name(self):
        """Gets the marketing_esp_friendly_name of this EmailSettings.  # noqa: E501


        :return: The marketing_esp_friendly_name of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._marketing_esp_friendly_name

    @marketing_esp_friendly_name.setter
    def marketing_esp_friendly_name(self, marketing_esp_friendly_name):
        """Sets the marketing_esp_friendly_name of this EmailSettings.


        :param marketing_esp_friendly_name: The marketing_esp_friendly_name of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._marketing_esp_friendly_name = marketing_esp_friendly_name

    @property
    def postcard_from_address1(self):
        """Gets the postcard_from_address1 of this EmailSettings.  # noqa: E501


        :return: The postcard_from_address1 of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._postcard_from_address1

    @postcard_from_address1.setter
    def postcard_from_address1(self, postcard_from_address1):
        """Sets the postcard_from_address1 of this EmailSettings.


        :param postcard_from_address1: The postcard_from_address1 of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._postcard_from_address1 = postcard_from_address1

    @property
    def postcard_from_address2(self):
        """Gets the postcard_from_address2 of this EmailSettings.  # noqa: E501


        :return: The postcard_from_address2 of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._postcard_from_address2

    @postcard_from_address2.setter
    def postcard_from_address2(self, postcard_from_address2):
        """Sets the postcard_from_address2 of this EmailSettings.


        :param postcard_from_address2: The postcard_from_address2 of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._postcard_from_address2 = postcard_from_address2

    @property
    def postcard_from_city(self):
        """Gets the postcard_from_city of this EmailSettings.  # noqa: E501


        :return: The postcard_from_city of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._postcard_from_city

    @postcard_from_city.setter
    def postcard_from_city(self, postcard_from_city):
        """Sets the postcard_from_city of this EmailSettings.


        :param postcard_from_city: The postcard_from_city of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._postcard_from_city = postcard_from_city

    @property
    def postcard_from_name(self):
        """Gets the postcard_from_name of this EmailSettings.  # noqa: E501


        :return: The postcard_from_name of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._postcard_from_name

    @postcard_from_name.setter
    def postcard_from_name(self, postcard_from_name):
        """Sets the postcard_from_name of this EmailSettings.


        :param postcard_from_name: The postcard_from_name of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._postcard_from_name = postcard_from_name

    @property
    def postcard_from_postal_code(self):
        """Gets the postcard_from_postal_code of this EmailSettings.  # noqa: E501


        :return: The postcard_from_postal_code of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._postcard_from_postal_code

    @postcard_from_postal_code.setter
    def postcard_from_postal_code(self, postcard_from_postal_code):
        """Sets the postcard_from_postal_code of this EmailSettings.


        :param postcard_from_postal_code: The postcard_from_postal_code of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._postcard_from_postal_code = postcard_from_postal_code

    @property
    def postcard_from_state(self):
        """Gets the postcard_from_state of this EmailSettings.  # noqa: E501


        :return: The postcard_from_state of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._postcard_from_state

    @postcard_from_state.setter
    def postcard_from_state(self, postcard_from_state):
        """Sets the postcard_from_state of this EmailSettings.


        :param postcard_from_state: The postcard_from_state of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._postcard_from_state = postcard_from_state

    @property
    def require_order_within_last(self):
        """Gets the require_order_within_last of this EmailSettings.  # noqa: E501

        Require order within last  # noqa: E501

        :return: The require_order_within_last of this EmailSettings.  # noqa: E501
        :rtype: int
        """
        return self._require_order_within_last

    @require_order_within_last.setter
    def require_order_within_last(self, require_order_within_last):
        """Sets the require_order_within_last of this EmailSettings.

        Require order within last  # noqa: E501

        :param require_order_within_last: The require_order_within_last of this EmailSettings.  # noqa: E501
        :type: int
        """

        self._require_order_within_last = require_order_within_last

    @property
    def reviews_io_configured(self):
        """Gets the reviews_io_configured of this EmailSettings.  # noqa: E501

        True if the Reviews.io integration is configured  # noqa: E501

        :return: The reviews_io_configured of this EmailSettings.  # noqa: E501
        :rtype: bool
        """
        return self._reviews_io_configured

    @reviews_io_configured.setter
    def reviews_io_configured(self, reviews_io_configured):
        """Sets the reviews_io_configured of this EmailSettings.

        True if the Reviews.io integration is configured  # noqa: E501

        :param reviews_io_configured: The reviews_io_configured of this EmailSettings.  # noqa: E501
        :type: bool
        """

        self._reviews_io_configured = reviews_io_configured

    @property
    def sms_esp_twilio_uuid(self):
        """Gets the sms_esp_twilio_uuid of this EmailSettings.  # noqa: E501


        :return: The sms_esp_twilio_uuid of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._sms_esp_twilio_uuid

    @sms_esp_twilio_uuid.setter
    def sms_esp_twilio_uuid(self, sms_esp_twilio_uuid):
        """Sets the sms_esp_twilio_uuid of this EmailSettings.


        :param sms_esp_twilio_uuid: The sms_esp_twilio_uuid of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._sms_esp_twilio_uuid = sms_esp_twilio_uuid

    @property
    def sms_phone_number(self):
        """Gets the sms_phone_number of this EmailSettings.  # noqa: E501


        :return: The sms_phone_number of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._sms_phone_number

    @sms_phone_number.setter
    def sms_phone_number(self, sms_phone_number):
        """Sets the sms_phone_number of this EmailSettings.


        :param sms_phone_number: The sms_phone_number of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._sms_phone_number = sms_phone_number

    @property
    def transactional_esp_domain_user(self):
        """Gets the transactional_esp_domain_user of this EmailSettings.  # noqa: E501


        :return: The transactional_esp_domain_user of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._transactional_esp_domain_user

    @transactional_esp_domain_user.setter
    def transactional_esp_domain_user(self, transactional_esp_domain_user):
        """Sets the transactional_esp_domain_user of this EmailSettings.


        :param transactional_esp_domain_user: The transactional_esp_domain_user of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._transactional_esp_domain_user = transactional_esp_domain_user

    @property
    def transactional_esp_domain_uuid(self):
        """Gets the transactional_esp_domain_uuid of this EmailSettings.  # noqa: E501


        :return: The transactional_esp_domain_uuid of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._transactional_esp_domain_uuid

    @transactional_esp_domain_uuid.setter
    def transactional_esp_domain_uuid(self, transactional_esp_domain_uuid):
        """Sets the transactional_esp_domain_uuid of this EmailSettings.


        :param transactional_esp_domain_uuid: The transactional_esp_domain_uuid of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._transactional_esp_domain_uuid = transactional_esp_domain_uuid

    @property
    def transactional_esp_friendly_name(self):
        """Gets the transactional_esp_friendly_name of this EmailSettings.  # noqa: E501


        :return: The transactional_esp_friendly_name of this EmailSettings.  # noqa: E501
        :rtype: str
        """
        return self._transactional_esp_friendly_name

    @transactional_esp_friendly_name.setter
    def transactional_esp_friendly_name(self, transactional_esp_friendly_name):
        """Sets the transactional_esp_friendly_name of this EmailSettings.


        :param transactional_esp_friendly_name: The transactional_esp_friendly_name of this EmailSettings.  # noqa: E501
        :type: str
        """

        self._transactional_esp_friendly_name = transactional_esp_friendly_name

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
        if issubclass(EmailSettings, dict):
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
        if not isinstance(other, EmailSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
