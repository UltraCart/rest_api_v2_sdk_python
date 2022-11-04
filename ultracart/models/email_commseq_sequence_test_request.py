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


class EmailCommseqSequenceTestRequest(object):
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
        'address_1': 'str',
        'address_2': 'str',
        'cart_id': 'str',
        'cart_item_ids': 'list[str]',
        'city': 'str',
        'esp_commseq_uuid': 'str',
        'mail_card': 'bool',
        'name': 'str',
        'order_id': 'str',
        'please_review': 'bool',
        'postal_code': 'str',
        'send_to_cellphone_e164': 'str',
        'send_to_email': 'str',
        'send_to_logged_in_user': 'bool',
        'state': 'str'
    }

    attribute_map = {
        'address_1': 'address_1',
        'address_2': 'address_2',
        'cart_id': 'cart_id',
        'cart_item_ids': 'cart_item_ids',
        'city': 'city',
        'esp_commseq_uuid': 'esp_commseq_uuid',
        'mail_card': 'mail_card',
        'name': 'name',
        'order_id': 'order_id',
        'please_review': 'please_review',
        'postal_code': 'postal_code',
        'send_to_cellphone_e164': 'send_to_cellphone_e164',
        'send_to_email': 'send_to_email',
        'send_to_logged_in_user': 'send_to_logged_in_user',
        'state': 'state'
    }

    def __init__(self, address_1=None, address_2=None, cart_id=None, cart_item_ids=None, city=None, esp_commseq_uuid=None, mail_card=None, name=None, order_id=None, please_review=None, postal_code=None, send_to_cellphone_e164=None, send_to_email=None, send_to_logged_in_user=None, state=None):  # noqa: E501
        """EmailCommseqSequenceTestRequest - a model defined in Swagger"""  # noqa: E501

        self._address_1 = None
        self._address_2 = None
        self._cart_id = None
        self._cart_item_ids = None
        self._city = None
        self._esp_commseq_uuid = None
        self._mail_card = None
        self._name = None
        self._order_id = None
        self._please_review = None
        self._postal_code = None
        self._send_to_cellphone_e164 = None
        self._send_to_email = None
        self._send_to_logged_in_user = None
        self._state = None
        self.discriminator = None

        if address_1 is not None:
            self.address_1 = address_1
        if address_2 is not None:
            self.address_2 = address_2
        if cart_id is not None:
            self.cart_id = cart_id
        if cart_item_ids is not None:
            self.cart_item_ids = cart_item_ids
        if city is not None:
            self.city = city
        if esp_commseq_uuid is not None:
            self.esp_commseq_uuid = esp_commseq_uuid
        if mail_card is not None:
            self.mail_card = mail_card
        if name is not None:
            self.name = name
        if order_id is not None:
            self.order_id = order_id
        if please_review is not None:
            self.please_review = please_review
        if postal_code is not None:
            self.postal_code = postal_code
        if send_to_cellphone_e164 is not None:
            self.send_to_cellphone_e164 = send_to_cellphone_e164
        if send_to_email is not None:
            self.send_to_email = send_to_email
        if send_to_logged_in_user is not None:
            self.send_to_logged_in_user = send_to_logged_in_user
        if state is not None:
            self.state = state

    @property
    def address_1(self):
        """Gets the address_1 of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The address_1 of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_1

    @address_1.setter
    def address_1(self, address_1):
        """Sets the address_1 of this EmailCommseqSequenceTestRequest.


        :param address_1: The address_1 of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._address_1 = address_1

    @property
    def address_2(self):
        """Gets the address_2 of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The address_2 of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_2

    @address_2.setter
    def address_2(self, address_2):
        """Sets the address_2 of this EmailCommseqSequenceTestRequest.


        :param address_2: The address_2 of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._address_2 = address_2

    @property
    def cart_id(self):
        """Gets the cart_id of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The cart_id of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._cart_id

    @cart_id.setter
    def cart_id(self, cart_id):
        """Sets the cart_id of this EmailCommseqSequenceTestRequest.


        :param cart_id: The cart_id of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._cart_id = cart_id

    @property
    def cart_item_ids(self):
        """Gets the cart_item_ids of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The cart_item_ids of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cart_item_ids

    @cart_item_ids.setter
    def cart_item_ids(self, cart_item_ids):
        """Sets the cart_item_ids of this EmailCommseqSequenceTestRequest.


        :param cart_item_ids: The cart_item_ids of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: list[str]
        """

        self._cart_item_ids = cart_item_ids

    @property
    def city(self):
        """Gets the city of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The city of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this EmailCommseqSequenceTestRequest.


        :param city: The city of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def esp_commseq_uuid(self):
        """Gets the esp_commseq_uuid of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The esp_commseq_uuid of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._esp_commseq_uuid

    @esp_commseq_uuid.setter
    def esp_commseq_uuid(self, esp_commseq_uuid):
        """Sets the esp_commseq_uuid of this EmailCommseqSequenceTestRequest.


        :param esp_commseq_uuid: The esp_commseq_uuid of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._esp_commseq_uuid = esp_commseq_uuid

    @property
    def mail_card(self):
        """Gets the mail_card of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The mail_card of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: bool
        """
        return self._mail_card

    @mail_card.setter
    def mail_card(self, mail_card):
        """Sets the mail_card of this EmailCommseqSequenceTestRequest.


        :param mail_card: The mail_card of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: bool
        """

        self._mail_card = mail_card

    @property
    def name(self):
        """Gets the name of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The name of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailCommseqSequenceTestRequest.


        :param name: The name of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order_id(self):
        """Gets the order_id of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The order_id of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this EmailCommseqSequenceTestRequest.


        :param order_id: The order_id of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def please_review(self):
        """Gets the please_review of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The please_review of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: bool
        """
        return self._please_review

    @please_review.setter
    def please_review(self, please_review):
        """Sets the please_review of this EmailCommseqSequenceTestRequest.


        :param please_review: The please_review of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: bool
        """

        self._please_review = please_review

    @property
    def postal_code(self):
        """Gets the postal_code of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The postal_code of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this EmailCommseqSequenceTestRequest.


        :param postal_code: The postal_code of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def send_to_cellphone_e164(self):
        """Gets the send_to_cellphone_e164 of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The send_to_cellphone_e164 of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._send_to_cellphone_e164

    @send_to_cellphone_e164.setter
    def send_to_cellphone_e164(self, send_to_cellphone_e164):
        """Sets the send_to_cellphone_e164 of this EmailCommseqSequenceTestRequest.


        :param send_to_cellphone_e164: The send_to_cellphone_e164 of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._send_to_cellphone_e164 = send_to_cellphone_e164

    @property
    def send_to_email(self):
        """Gets the send_to_email of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The send_to_email of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._send_to_email

    @send_to_email.setter
    def send_to_email(self, send_to_email):
        """Sets the send_to_email of this EmailCommseqSequenceTestRequest.


        :param send_to_email: The send_to_email of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._send_to_email = send_to_email

    @property
    def send_to_logged_in_user(self):
        """Gets the send_to_logged_in_user of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The send_to_logged_in_user of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_to_logged_in_user

    @send_to_logged_in_user.setter
    def send_to_logged_in_user(self, send_to_logged_in_user):
        """Sets the send_to_logged_in_user of this EmailCommseqSequenceTestRequest.


        :param send_to_logged_in_user: The send_to_logged_in_user of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: bool
        """

        self._send_to_logged_in_user = send_to_logged_in_user

    @property
    def state(self):
        """Gets the state of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The state of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EmailCommseqSequenceTestRequest.


        :param state: The state of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(EmailCommseqSequenceTestRequest, dict):
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
        if not isinstance(other, EmailCommseqSequenceTestRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other