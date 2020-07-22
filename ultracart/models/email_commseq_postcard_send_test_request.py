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


class EmailCommseqPostcardSendTestRequest(object):
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
        'esp_commseq_postcard_uuid': 'str',
        'esp_commseq_step_uuid': 'str',
        'esp_commseq_uuid': 'str',
        'name': 'str',
        'order_id': 'str',
        'postal_code': 'str',
        'state': 'str'
    }

    attribute_map = {
        'address_1': 'address_1',
        'address_2': 'address_2',
        'cart_id': 'cart_id',
        'cart_item_ids': 'cart_item_ids',
        'city': 'city',
        'esp_commseq_postcard_uuid': 'esp_commseq_postcard_uuid',
        'esp_commseq_step_uuid': 'esp_commseq_step_uuid',
        'esp_commseq_uuid': 'esp_commseq_uuid',
        'name': 'name',
        'order_id': 'order_id',
        'postal_code': 'postal_code',
        'state': 'state'
    }

    def __init__(self, address_1=None, address_2=None, cart_id=None, cart_item_ids=None, city=None, esp_commseq_postcard_uuid=None, esp_commseq_step_uuid=None, esp_commseq_uuid=None, name=None, order_id=None, postal_code=None, state=None):  # noqa: E501
        """EmailCommseqPostcardSendTestRequest - a model defined in Swagger"""  # noqa: E501

        self._address_1 = None
        self._address_2 = None
        self._cart_id = None
        self._cart_item_ids = None
        self._city = None
        self._esp_commseq_postcard_uuid = None
        self._esp_commseq_step_uuid = None
        self._esp_commseq_uuid = None
        self._name = None
        self._order_id = None
        self._postal_code = None
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
        if esp_commseq_postcard_uuid is not None:
            self.esp_commseq_postcard_uuid = esp_commseq_postcard_uuid
        if esp_commseq_step_uuid is not None:
            self.esp_commseq_step_uuid = esp_commseq_step_uuid
        if esp_commseq_uuid is not None:
            self.esp_commseq_uuid = esp_commseq_uuid
        if name is not None:
            self.name = name
        if order_id is not None:
            self.order_id = order_id
        if postal_code is not None:
            self.postal_code = postal_code
        if state is not None:
            self.state = state

    @property
    def address_1(self):
        """Gets the address_1 of this EmailCommseqPostcardSendTestRequest.  # noqa: E501


        :return: The address_1 of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_1

    @address_1.setter
    def address_1(self, address_1):
        """Sets the address_1 of this EmailCommseqPostcardSendTestRequest.


        :param address_1: The address_1 of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :type: str
        """

        self._address_1 = address_1

    @property
    def address_2(self):
        """Gets the address_2 of this EmailCommseqPostcardSendTestRequest.  # noqa: E501


        :return: The address_2 of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_2

    @address_2.setter
    def address_2(self, address_2):
        """Sets the address_2 of this EmailCommseqPostcardSendTestRequest.


        :param address_2: The address_2 of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :type: str
        """

        self._address_2 = address_2

    @property
    def cart_id(self):
        """Gets the cart_id of this EmailCommseqPostcardSendTestRequest.  # noqa: E501


        :return: The cart_id of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._cart_id

    @cart_id.setter
    def cart_id(self, cart_id):
        """Sets the cart_id of this EmailCommseqPostcardSendTestRequest.


        :param cart_id: The cart_id of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :type: str
        """

        self._cart_id = cart_id

    @property
    def cart_item_ids(self):
        """Gets the cart_item_ids of this EmailCommseqPostcardSendTestRequest.  # noqa: E501


        :return: The cart_item_ids of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cart_item_ids

    @cart_item_ids.setter
    def cart_item_ids(self, cart_item_ids):
        """Sets the cart_item_ids of this EmailCommseqPostcardSendTestRequest.


        :param cart_item_ids: The cart_item_ids of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :type: list[str]
        """

        self._cart_item_ids = cart_item_ids

    @property
    def city(self):
        """Gets the city of this EmailCommseqPostcardSendTestRequest.  # noqa: E501


        :return: The city of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this EmailCommseqPostcardSendTestRequest.


        :param city: The city of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def esp_commseq_postcard_uuid(self):
        """Gets the esp_commseq_postcard_uuid of this EmailCommseqPostcardSendTestRequest.  # noqa: E501


        :return: The esp_commseq_postcard_uuid of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._esp_commseq_postcard_uuid

    @esp_commseq_postcard_uuid.setter
    def esp_commseq_postcard_uuid(self, esp_commseq_postcard_uuid):
        """Sets the esp_commseq_postcard_uuid of this EmailCommseqPostcardSendTestRequest.


        :param esp_commseq_postcard_uuid: The esp_commseq_postcard_uuid of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :type: str
        """

        self._esp_commseq_postcard_uuid = esp_commseq_postcard_uuid

    @property
    def esp_commseq_step_uuid(self):
        """Gets the esp_commseq_step_uuid of this EmailCommseqPostcardSendTestRequest.  # noqa: E501


        :return: The esp_commseq_step_uuid of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._esp_commseq_step_uuid

    @esp_commseq_step_uuid.setter
    def esp_commseq_step_uuid(self, esp_commseq_step_uuid):
        """Sets the esp_commseq_step_uuid of this EmailCommseqPostcardSendTestRequest.


        :param esp_commseq_step_uuid: The esp_commseq_step_uuid of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :type: str
        """

        self._esp_commseq_step_uuid = esp_commseq_step_uuid

    @property
    def esp_commseq_uuid(self):
        """Gets the esp_commseq_uuid of this EmailCommseqPostcardSendTestRequest.  # noqa: E501


        :return: The esp_commseq_uuid of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._esp_commseq_uuid

    @esp_commseq_uuid.setter
    def esp_commseq_uuid(self, esp_commseq_uuid):
        """Sets the esp_commseq_uuid of this EmailCommseqPostcardSendTestRequest.


        :param esp_commseq_uuid: The esp_commseq_uuid of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :type: str
        """

        self._esp_commseq_uuid = esp_commseq_uuid

    @property
    def name(self):
        """Gets the name of this EmailCommseqPostcardSendTestRequest.  # noqa: E501


        :return: The name of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailCommseqPostcardSendTestRequest.


        :param name: The name of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order_id(self):
        """Gets the order_id of this EmailCommseqPostcardSendTestRequest.  # noqa: E501


        :return: The order_id of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this EmailCommseqPostcardSendTestRequest.


        :param order_id: The order_id of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def postal_code(self):
        """Gets the postal_code of this EmailCommseqPostcardSendTestRequest.  # noqa: E501


        :return: The postal_code of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this EmailCommseqPostcardSendTestRequest.


        :param postal_code: The postal_code of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """Gets the state of this EmailCommseqPostcardSendTestRequest.  # noqa: E501


        :return: The state of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EmailCommseqPostcardSendTestRequest.


        :param state: The state of this EmailCommseqPostcardSendTestRequest.  # noqa: E501
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
        if issubclass(EmailCommseqPostcardSendTestRequest, dict):
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
        if not isinstance(other, EmailCommseqPostcardSendTestRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
