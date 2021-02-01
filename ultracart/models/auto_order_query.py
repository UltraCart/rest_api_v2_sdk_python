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


class AutoOrderQuery(object):
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
        'auto_order_code': 'str',
        'card_type': 'str',
        'city': 'str',
        'company': 'str',
        'country_code': 'str',
        'customer_profile_oid': 'int',
        'email': 'str',
        'first_name': 'str',
        'item_id': 'str',
        'last_name': 'str',
        'next_shipment_date_begin': 'str',
        'next_shipment_date_end': 'str',
        'original_order_date_begin': 'str',
        'original_order_date_end': 'str',
        'original_order_id': 'str',
        'phone': 'str',
        'postal_code': 'str',
        'state': 'str',
        'status': 'str'
    }

    attribute_map = {
        'auto_order_code': 'auto_order_code',
        'card_type': 'card_type',
        'city': 'city',
        'company': 'company',
        'country_code': 'country_code',
        'customer_profile_oid': 'customer_profile_oid',
        'email': 'email',
        'first_name': 'first_name',
        'item_id': 'item_id',
        'last_name': 'last_name',
        'next_shipment_date_begin': 'next_shipment_date_begin',
        'next_shipment_date_end': 'next_shipment_date_end',
        'original_order_date_begin': 'original_order_date_begin',
        'original_order_date_end': 'original_order_date_end',
        'original_order_id': 'original_order_id',
        'phone': 'phone',
        'postal_code': 'postal_code',
        'state': 'state',
        'status': 'status'
    }

    def __init__(self, auto_order_code=None, card_type=None, city=None, company=None, country_code=None, customer_profile_oid=None, email=None, first_name=None, item_id=None, last_name=None, next_shipment_date_begin=None, next_shipment_date_end=None, original_order_date_begin=None, original_order_date_end=None, original_order_id=None, phone=None, postal_code=None, state=None, status=None):  # noqa: E501
        """AutoOrderQuery - a model defined in Swagger"""  # noqa: E501

        self._auto_order_code = None
        self._card_type = None
        self._city = None
        self._company = None
        self._country_code = None
        self._customer_profile_oid = None
        self._email = None
        self._first_name = None
        self._item_id = None
        self._last_name = None
        self._next_shipment_date_begin = None
        self._next_shipment_date_end = None
        self._original_order_date_begin = None
        self._original_order_date_end = None
        self._original_order_id = None
        self._phone = None
        self._postal_code = None
        self._state = None
        self._status = None
        self.discriminator = None

        if auto_order_code is not None:
            self.auto_order_code = auto_order_code
        if card_type is not None:
            self.card_type = card_type
        if city is not None:
            self.city = city
        if company is not None:
            self.company = company
        if country_code is not None:
            self.country_code = country_code
        if customer_profile_oid is not None:
            self.customer_profile_oid = customer_profile_oid
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if item_id is not None:
            self.item_id = item_id
        if last_name is not None:
            self.last_name = last_name
        if next_shipment_date_begin is not None:
            self.next_shipment_date_begin = next_shipment_date_begin
        if next_shipment_date_end is not None:
            self.next_shipment_date_end = next_shipment_date_end
        if original_order_date_begin is not None:
            self.original_order_date_begin = original_order_date_begin
        if original_order_date_end is not None:
            self.original_order_date_end = original_order_date_end
        if original_order_id is not None:
            self.original_order_id = original_order_id
        if phone is not None:
            self.phone = phone
        if postal_code is not None:
            self.postal_code = postal_code
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status

    @property
    def auto_order_code(self):
        """Gets the auto_order_code of this AutoOrderQuery.  # noqa: E501

        Auto order code  # noqa: E501

        :return: The auto_order_code of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._auto_order_code

    @auto_order_code.setter
    def auto_order_code(self, auto_order_code):
        """Sets the auto_order_code of this AutoOrderQuery.

        Auto order code  # noqa: E501

        :param auto_order_code: The auto_order_code of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._auto_order_code = auto_order_code

    @property
    def card_type(self):
        """Gets the card_type of this AutoOrderQuery.  # noqa: E501

        Card type  # noqa: E501

        :return: The card_type of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this AutoOrderQuery.

        Card type  # noqa: E501

        :param card_type: The card_type of this AutoOrderQuery.  # noqa: E501
        :type: str
        """
        if card_type is not None and len(card_type) > 100:
            raise ValueError("Invalid value for `card_type`, length must be less than or equal to `100`")  # noqa: E501

        self._card_type = card_type

    @property
    def city(self):
        """Gets the city of this AutoOrderQuery.  # noqa: E501

        City  # noqa: E501

        :return: The city of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AutoOrderQuery.

        City  # noqa: E501

        :param city: The city of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def company(self):
        """Gets the company of this AutoOrderQuery.  # noqa: E501

        Company  # noqa: E501

        :return: The company of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this AutoOrderQuery.

        Company  # noqa: E501

        :param company: The company of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def country_code(self):
        """Gets the country_code of this AutoOrderQuery.  # noqa: E501

        ISO-3166 two letter country code  # noqa: E501

        :return: The country_code of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this AutoOrderQuery.

        ISO-3166 two letter country code  # noqa: E501

        :param country_code: The country_code of this AutoOrderQuery.  # noqa: E501
        :type: str
        """
        if country_code is not None and len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `2`")  # noqa: E501

        self._country_code = country_code

    @property
    def customer_profile_oid(self):
        """Gets the customer_profile_oid of this AutoOrderQuery.  # noqa: E501

        Customer profile object identifier  # noqa: E501

        :return: The customer_profile_oid of this AutoOrderQuery.  # noqa: E501
        :rtype: int
        """
        return self._customer_profile_oid

    @customer_profile_oid.setter
    def customer_profile_oid(self, customer_profile_oid):
        """Sets the customer_profile_oid of this AutoOrderQuery.

        Customer profile object identifier  # noqa: E501

        :param customer_profile_oid: The customer_profile_oid of this AutoOrderQuery.  # noqa: E501
        :type: int
        """

        self._customer_profile_oid = customer_profile_oid

    @property
    def email(self):
        """Gets the email of this AutoOrderQuery.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AutoOrderQuery.

        Email  # noqa: E501

        :param email: The email of this AutoOrderQuery.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) > 100:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `100`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this AutoOrderQuery.  # noqa: E501

        First name  # noqa: E501

        :return: The first_name of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AutoOrderQuery.

        First name  # noqa: E501

        :param first_name: The first_name of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def item_id(self):
        """Gets the item_id of this AutoOrderQuery.  # noqa: E501

        Item ID  # noqa: E501

        :return: The item_id of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this AutoOrderQuery.

        Item ID  # noqa: E501

        :param item_id: The item_id of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def last_name(self):
        """Gets the last_name of this AutoOrderQuery.  # noqa: E501

        Last name  # noqa: E501

        :return: The last_name of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AutoOrderQuery.

        Last name  # noqa: E501

        :param last_name: The last_name of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def next_shipment_date_begin(self):
        """Gets the next_shipment_date_begin of this AutoOrderQuery.  # noqa: E501

        Next shipment date begin  # noqa: E501

        :return: The next_shipment_date_begin of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._next_shipment_date_begin

    @next_shipment_date_begin.setter
    def next_shipment_date_begin(self, next_shipment_date_begin):
        """Sets the next_shipment_date_begin of this AutoOrderQuery.

        Next shipment date begin  # noqa: E501

        :param next_shipment_date_begin: The next_shipment_date_begin of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._next_shipment_date_begin = next_shipment_date_begin

    @property
    def next_shipment_date_end(self):
        """Gets the next_shipment_date_end of this AutoOrderQuery.  # noqa: E501

        Next shipment date end  # noqa: E501

        :return: The next_shipment_date_end of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._next_shipment_date_end

    @next_shipment_date_end.setter
    def next_shipment_date_end(self, next_shipment_date_end):
        """Sets the next_shipment_date_end of this AutoOrderQuery.

        Next shipment date end  # noqa: E501

        :param next_shipment_date_end: The next_shipment_date_end of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._next_shipment_date_end = next_shipment_date_end

    @property
    def original_order_date_begin(self):
        """Gets the original_order_date_begin of this AutoOrderQuery.  # noqa: E501

        Original order date begin  # noqa: E501

        :return: The original_order_date_begin of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._original_order_date_begin

    @original_order_date_begin.setter
    def original_order_date_begin(self, original_order_date_begin):
        """Sets the original_order_date_begin of this AutoOrderQuery.

        Original order date begin  # noqa: E501

        :param original_order_date_begin: The original_order_date_begin of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._original_order_date_begin = original_order_date_begin

    @property
    def original_order_date_end(self):
        """Gets the original_order_date_end of this AutoOrderQuery.  # noqa: E501

        Original order date end  # noqa: E501

        :return: The original_order_date_end of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._original_order_date_end

    @original_order_date_end.setter
    def original_order_date_end(self, original_order_date_end):
        """Sets the original_order_date_end of this AutoOrderQuery.

        Original order date end  # noqa: E501

        :param original_order_date_end: The original_order_date_end of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._original_order_date_end = original_order_date_end

    @property
    def original_order_id(self):
        """Gets the original_order_id of this AutoOrderQuery.  # noqa: E501

        Original order ID  # noqa: E501

        :return: The original_order_id of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._original_order_id

    @original_order_id.setter
    def original_order_id(self, original_order_id):
        """Sets the original_order_id of this AutoOrderQuery.

        Original order ID  # noqa: E501

        :param original_order_id: The original_order_id of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._original_order_id = original_order_id

    @property
    def phone(self):
        """Gets the phone of this AutoOrderQuery.  # noqa: E501

        Phone  # noqa: E501

        :return: The phone of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AutoOrderQuery.

        Phone  # noqa: E501

        :param phone: The phone of this AutoOrderQuery.  # noqa: E501
        :type: str
        """
        if phone is not None and len(phone) > 25:
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `25`")  # noqa: E501

        self._phone = phone

    @property
    def postal_code(self):
        """Gets the postal_code of this AutoOrderQuery.  # noqa: E501

        Postal code  # noqa: E501

        :return: The postal_code of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this AutoOrderQuery.

        Postal code  # noqa: E501

        :param postal_code: The postal_code of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """Gets the state of this AutoOrderQuery.  # noqa: E501

        State  # noqa: E501

        :return: The state of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AutoOrderQuery.

        State  # noqa: E501

        :param state: The state of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def status(self):
        """Gets the status of this AutoOrderQuery.  # noqa: E501

        Status  # noqa: E501

        :return: The status of this AutoOrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AutoOrderQuery.

        Status  # noqa: E501

        :param status: The status of this AutoOrderQuery.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(AutoOrderQuery, dict):
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
        if not isinstance(other, AutoOrderQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
