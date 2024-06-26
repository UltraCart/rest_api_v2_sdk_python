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


class Twilio(object):
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
        'account_sid': 'str',
        'api_key_id': 'str',
        'api_key_name': 'str',
        'auth_token': 'str',
        'esp_twilio_uuid': 'str',
        'inbound_twiml_app_sid': 'str',
        'outbound_twiml_app_sid': 'str',
        'phone_numbers': 'list[str]',
        'twilio_workspace_sid': 'str'
    }

    attribute_map = {
        'account_sid': 'account_sid',
        'api_key_id': 'api_key_id',
        'api_key_name': 'api_key_name',
        'auth_token': 'auth_token',
        'esp_twilio_uuid': 'esp_twilio_uuid',
        'inbound_twiml_app_sid': 'inbound_twiml_app_sid',
        'outbound_twiml_app_sid': 'outbound_twiml_app_sid',
        'phone_numbers': 'phone_numbers',
        'twilio_workspace_sid': 'twilio_workspace_sid'
    }

    def __init__(self, account_sid=None, api_key_id=None, api_key_name=None, auth_token=None, esp_twilio_uuid=None, inbound_twiml_app_sid=None, outbound_twiml_app_sid=None, phone_numbers=None, twilio_workspace_sid=None):  # noqa: E501
        """Twilio - a model defined in Swagger"""  # noqa: E501

        self._account_sid = None
        self._api_key_id = None
        self._api_key_name = None
        self._auth_token = None
        self._esp_twilio_uuid = None
        self._inbound_twiml_app_sid = None
        self._outbound_twiml_app_sid = None
        self._phone_numbers = None
        self._twilio_workspace_sid = None
        self.discriminator = None

        if account_sid is not None:
            self.account_sid = account_sid
        if api_key_id is not None:
            self.api_key_id = api_key_id
        if api_key_name is not None:
            self.api_key_name = api_key_name
        if auth_token is not None:
            self.auth_token = auth_token
        if esp_twilio_uuid is not None:
            self.esp_twilio_uuid = esp_twilio_uuid
        if inbound_twiml_app_sid is not None:
            self.inbound_twiml_app_sid = inbound_twiml_app_sid
        if outbound_twiml_app_sid is not None:
            self.outbound_twiml_app_sid = outbound_twiml_app_sid
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if twilio_workspace_sid is not None:
            self.twilio_workspace_sid = twilio_workspace_sid

    @property
    def account_sid(self):
        """Gets the account_sid of this Twilio.  # noqa: E501


        :return: The account_sid of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._account_sid

    @account_sid.setter
    def account_sid(self, account_sid):
        """Sets the account_sid of this Twilio.


        :param account_sid: The account_sid of this Twilio.  # noqa: E501
        :type: str
        """

        self._account_sid = account_sid

    @property
    def api_key_id(self):
        """Gets the api_key_id of this Twilio.  # noqa: E501


        :return: The api_key_id of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._api_key_id

    @api_key_id.setter
    def api_key_id(self, api_key_id):
        """Sets the api_key_id of this Twilio.


        :param api_key_id: The api_key_id of this Twilio.  # noqa: E501
        :type: str
        """

        self._api_key_id = api_key_id

    @property
    def api_key_name(self):
        """Gets the api_key_name of this Twilio.  # noqa: E501


        :return: The api_key_name of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._api_key_name

    @api_key_name.setter
    def api_key_name(self, api_key_name):
        """Sets the api_key_name of this Twilio.


        :param api_key_name: The api_key_name of this Twilio.  # noqa: E501
        :type: str
        """

        self._api_key_name = api_key_name

    @property
    def auth_token(self):
        """Gets the auth_token of this Twilio.  # noqa: E501


        :return: The auth_token of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """Sets the auth_token of this Twilio.


        :param auth_token: The auth_token of this Twilio.  # noqa: E501
        :type: str
        """

        self._auth_token = auth_token

    @property
    def esp_twilio_uuid(self):
        """Gets the esp_twilio_uuid of this Twilio.  # noqa: E501


        :return: The esp_twilio_uuid of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._esp_twilio_uuid

    @esp_twilio_uuid.setter
    def esp_twilio_uuid(self, esp_twilio_uuid):
        """Sets the esp_twilio_uuid of this Twilio.


        :param esp_twilio_uuid: The esp_twilio_uuid of this Twilio.  # noqa: E501
        :type: str
        """

        self._esp_twilio_uuid = esp_twilio_uuid

    @property
    def inbound_twiml_app_sid(self):
        """Gets the inbound_twiml_app_sid of this Twilio.  # noqa: E501


        :return: The inbound_twiml_app_sid of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._inbound_twiml_app_sid

    @inbound_twiml_app_sid.setter
    def inbound_twiml_app_sid(self, inbound_twiml_app_sid):
        """Sets the inbound_twiml_app_sid of this Twilio.


        :param inbound_twiml_app_sid: The inbound_twiml_app_sid of this Twilio.  # noqa: E501
        :type: str
        """

        self._inbound_twiml_app_sid = inbound_twiml_app_sid

    @property
    def outbound_twiml_app_sid(self):
        """Gets the outbound_twiml_app_sid of this Twilio.  # noqa: E501


        :return: The outbound_twiml_app_sid of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._outbound_twiml_app_sid

    @outbound_twiml_app_sid.setter
    def outbound_twiml_app_sid(self, outbound_twiml_app_sid):
        """Sets the outbound_twiml_app_sid of this Twilio.


        :param outbound_twiml_app_sid: The outbound_twiml_app_sid of this Twilio.  # noqa: E501
        :type: str
        """

        self._outbound_twiml_app_sid = outbound_twiml_app_sid

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this Twilio.  # noqa: E501


        :return: The phone_numbers of this Twilio.  # noqa: E501
        :rtype: list[str]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this Twilio.


        :param phone_numbers: The phone_numbers of this Twilio.  # noqa: E501
        :type: list[str]
        """

        self._phone_numbers = phone_numbers

    @property
    def twilio_workspace_sid(self):
        """Gets the twilio_workspace_sid of this Twilio.  # noqa: E501


        :return: The twilio_workspace_sid of this Twilio.  # noqa: E501
        :rtype: str
        """
        return self._twilio_workspace_sid

    @twilio_workspace_sid.setter
    def twilio_workspace_sid(self, twilio_workspace_sid):
        """Sets the twilio_workspace_sid of this Twilio.


        :param twilio_workspace_sid: The twilio_workspace_sid of this Twilio.  # noqa: E501
        :type: str
        """

        self._twilio_workspace_sid = twilio_workspace_sid

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
        if issubclass(Twilio, dict):
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
        if not isinstance(other, Twilio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
