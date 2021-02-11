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


class OrderQuery(object):
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
        'cc_email': 'str',
        'channel_partner_code': 'str',
        'channel_partner_order_id': 'str',
        'city': 'str',
        'company': 'str',
        'country_code': 'str',
        'creation_date_begin': 'str',
        'creation_date_end': 'str',
        'current_stage': 'str',
        'customer_profile_oid': 'int',
        'email': 'str',
        'first_name': 'str',
        'item_id': 'str',
        'last_name': 'str',
        'order_id': 'str',
        'payment_date_begin': 'str',
        'payment_date_end': 'str',
        'payment_method': 'str',
        'phone': 'str',
        'postal_code': 'str',
        'purchase_order_number': 'str',
        'refund_date_begin': 'str',
        'refund_date_end': 'str',
        'rma': 'str',
        'screen_branding_theme_code': 'str',
        'shipment_date_begin': 'str',
        'shipment_date_end': 'str',
        'state_region': 'str',
        'storefront_host_name': 'str',
        'total': 'float'
    }

    attribute_map = {
        'cc_email': 'cc_email',
        'channel_partner_code': 'channel_partner_code',
        'channel_partner_order_id': 'channel_partner_order_id',
        'city': 'city',
        'company': 'company',
        'country_code': 'country_code',
        'creation_date_begin': 'creation_date_begin',
        'creation_date_end': 'creation_date_end',
        'current_stage': 'current_stage',
        'customer_profile_oid': 'customer_profile_oid',
        'email': 'email',
        'first_name': 'first_name',
        'item_id': 'item_id',
        'last_name': 'last_name',
        'order_id': 'order_id',
        'payment_date_begin': 'payment_date_begin',
        'payment_date_end': 'payment_date_end',
        'payment_method': 'payment_method',
        'phone': 'phone',
        'postal_code': 'postal_code',
        'purchase_order_number': 'purchase_order_number',
        'refund_date_begin': 'refund_date_begin',
        'refund_date_end': 'refund_date_end',
        'rma': 'rma',
        'screen_branding_theme_code': 'screen_branding_theme_code',
        'shipment_date_begin': 'shipment_date_begin',
        'shipment_date_end': 'shipment_date_end',
        'state_region': 'state_region',
        'storefront_host_name': 'storefront_host_name',
        'total': 'total'
    }

    def __init__(self, cc_email=None, channel_partner_code=None, channel_partner_order_id=None, city=None, company=None, country_code=None, creation_date_begin=None, creation_date_end=None, current_stage=None, customer_profile_oid=None, email=None, first_name=None, item_id=None, last_name=None, order_id=None, payment_date_begin=None, payment_date_end=None, payment_method=None, phone=None, postal_code=None, purchase_order_number=None, refund_date_begin=None, refund_date_end=None, rma=None, screen_branding_theme_code=None, shipment_date_begin=None, shipment_date_end=None, state_region=None, storefront_host_name=None, total=None):  # noqa: E501
        """OrderQuery - a model defined in Swagger"""  # noqa: E501

        self._cc_email = None
        self._channel_partner_code = None
        self._channel_partner_order_id = None
        self._city = None
        self._company = None
        self._country_code = None
        self._creation_date_begin = None
        self._creation_date_end = None
        self._current_stage = None
        self._customer_profile_oid = None
        self._email = None
        self._first_name = None
        self._item_id = None
        self._last_name = None
        self._order_id = None
        self._payment_date_begin = None
        self._payment_date_end = None
        self._payment_method = None
        self._phone = None
        self._postal_code = None
        self._purchase_order_number = None
        self._refund_date_begin = None
        self._refund_date_end = None
        self._rma = None
        self._screen_branding_theme_code = None
        self._shipment_date_begin = None
        self._shipment_date_end = None
        self._state_region = None
        self._storefront_host_name = None
        self._total = None
        self.discriminator = None

        if cc_email is not None:
            self.cc_email = cc_email
        if channel_partner_code is not None:
            self.channel_partner_code = channel_partner_code
        if channel_partner_order_id is not None:
            self.channel_partner_order_id = channel_partner_order_id
        if city is not None:
            self.city = city
        if company is not None:
            self.company = company
        if country_code is not None:
            self.country_code = country_code
        if creation_date_begin is not None:
            self.creation_date_begin = creation_date_begin
        if creation_date_end is not None:
            self.creation_date_end = creation_date_end
        if current_stage is not None:
            self.current_stage = current_stage
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
        if order_id is not None:
            self.order_id = order_id
        if payment_date_begin is not None:
            self.payment_date_begin = payment_date_begin
        if payment_date_end is not None:
            self.payment_date_end = payment_date_end
        if payment_method is not None:
            self.payment_method = payment_method
        if phone is not None:
            self.phone = phone
        if postal_code is not None:
            self.postal_code = postal_code
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if refund_date_begin is not None:
            self.refund_date_begin = refund_date_begin
        if refund_date_end is not None:
            self.refund_date_end = refund_date_end
        if rma is not None:
            self.rma = rma
        if screen_branding_theme_code is not None:
            self.screen_branding_theme_code = screen_branding_theme_code
        if shipment_date_begin is not None:
            self.shipment_date_begin = shipment_date_begin
        if shipment_date_end is not None:
            self.shipment_date_end = shipment_date_end
        if state_region is not None:
            self.state_region = state_region
        if storefront_host_name is not None:
            self.storefront_host_name = storefront_host_name
        if total is not None:
            self.total = total

    @property
    def cc_email(self):
        """Gets the cc_email of this OrderQuery.  # noqa: E501

        CC Email  # noqa: E501

        :return: The cc_email of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._cc_email

    @cc_email.setter
    def cc_email(self, cc_email):
        """Sets the cc_email of this OrderQuery.

        CC Email  # noqa: E501

        :param cc_email: The cc_email of this OrderQuery.  # noqa: E501
        :type: str
        """
        if cc_email is not None and len(cc_email) > 100:
            raise ValueError("Invalid value for `cc_email`, length must be less than or equal to `100`")  # noqa: E501

        self._cc_email = cc_email

    @property
    def channel_partner_code(self):
        """Gets the channel_partner_code of this OrderQuery.  # noqa: E501

        The code of the channel partner  # noqa: E501

        :return: The channel_partner_code of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._channel_partner_code

    @channel_partner_code.setter
    def channel_partner_code(self, channel_partner_code):
        """Sets the channel_partner_code of this OrderQuery.

        The code of the channel partner  # noqa: E501

        :param channel_partner_code: The channel_partner_code of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._channel_partner_code = channel_partner_code

    @property
    def channel_partner_order_id(self):
        """Gets the channel_partner_order_id of this OrderQuery.  # noqa: E501

        The order ID assigned by the channel partner for this order  # noqa: E501

        :return: The channel_partner_order_id of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._channel_partner_order_id

    @channel_partner_order_id.setter
    def channel_partner_order_id(self, channel_partner_order_id):
        """Sets the channel_partner_order_id of this OrderQuery.

        The order ID assigned by the channel partner for this order  # noqa: E501

        :param channel_partner_order_id: The channel_partner_order_id of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._channel_partner_order_id = channel_partner_order_id

    @property
    def city(self):
        """Gets the city of this OrderQuery.  # noqa: E501

        City  # noqa: E501

        :return: The city of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this OrderQuery.

        City  # noqa: E501

        :param city: The city of this OrderQuery.  # noqa: E501
        :type: str
        """
        if city is not None and len(city) > 32:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `32`")  # noqa: E501

        self._city = city

    @property
    def company(self):
        """Gets the company of this OrderQuery.  # noqa: E501

        Company  # noqa: E501

        :return: The company of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this OrderQuery.

        Company  # noqa: E501

        :param company: The company of this OrderQuery.  # noqa: E501
        :type: str
        """
        if company is not None and len(company) > 50:
            raise ValueError("Invalid value for `company`, length must be less than or equal to `50`")  # noqa: E501

        self._company = company

    @property
    def country_code(self):
        """Gets the country_code of this OrderQuery.  # noqa: E501

        ISO-3166 two letter country code  # noqa: E501

        :return: The country_code of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this OrderQuery.

        ISO-3166 two letter country code  # noqa: E501

        :param country_code: The country_code of this OrderQuery.  # noqa: E501
        :type: str
        """
        if country_code is not None and len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `2`")  # noqa: E501

        self._country_code = country_code

    @property
    def creation_date_begin(self):
        """Gets the creation_date_begin of this OrderQuery.  # noqa: E501

        Date/time that the order was created  # noqa: E501

        :return: The creation_date_begin of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._creation_date_begin

    @creation_date_begin.setter
    def creation_date_begin(self, creation_date_begin):
        """Sets the creation_date_begin of this OrderQuery.

        Date/time that the order was created  # noqa: E501

        :param creation_date_begin: The creation_date_begin of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._creation_date_begin = creation_date_begin

    @property
    def creation_date_end(self):
        """Gets the creation_date_end of this OrderQuery.  # noqa: E501

        Date/time that the order was created  # noqa: E501

        :return: The creation_date_end of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._creation_date_end

    @creation_date_end.setter
    def creation_date_end(self, creation_date_end):
        """Sets the creation_date_end of this OrderQuery.

        Date/time that the order was created  # noqa: E501

        :param creation_date_end: The creation_date_end of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._creation_date_end = creation_date_end

    @property
    def current_stage(self):
        """Gets the current_stage of this OrderQuery.  # noqa: E501

        Current stage that the order is in.  # noqa: E501

        :return: The current_stage of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._current_stage

    @current_stage.setter
    def current_stage(self, current_stage):
        """Sets the current_stage of this OrderQuery.

        Current stage that the order is in.  # noqa: E501

        :param current_stage: The current_stage of this OrderQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["Accounts Receivable", "Pending Clearance", "Fraud Review", "Rejected", "Shipping Department", "Completed Order", "Quote Request", "Quote Sent", "Least Cost Routing", "Unknown"]  # noqa: E501
        if current_stage not in allowed_values:
            raise ValueError(
                "Invalid value for `current_stage` ({0}), must be one of {1}"  # noqa: E501
                .format(current_stage, allowed_values)
            )

        self._current_stage = current_stage

    @property
    def customer_profile_oid(self):
        """Gets the customer_profile_oid of this OrderQuery.  # noqa: E501

        The customer profile to find associated orders for  # noqa: E501

        :return: The customer_profile_oid of this OrderQuery.  # noqa: E501
        :rtype: int
        """
        return self._customer_profile_oid

    @customer_profile_oid.setter
    def customer_profile_oid(self, customer_profile_oid):
        """Sets the customer_profile_oid of this OrderQuery.

        The customer profile to find associated orders for  # noqa: E501

        :param customer_profile_oid: The customer_profile_oid of this OrderQuery.  # noqa: E501
        :type: int
        """

        self._customer_profile_oid = customer_profile_oid

    @property
    def email(self):
        """Gets the email of this OrderQuery.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this OrderQuery.

        Email  # noqa: E501

        :param email: The email of this OrderQuery.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) > 100:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `100`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this OrderQuery.  # noqa: E501

        First name  # noqa: E501

        :return: The first_name of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this OrderQuery.

        First name  # noqa: E501

        :param first_name: The first_name of this OrderQuery.  # noqa: E501
        :type: str
        """
        if first_name is not None and len(first_name) > 30:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `30`")  # noqa: E501

        self._first_name = first_name

    @property
    def item_id(self):
        """Gets the item_id of this OrderQuery.  # noqa: E501

        Item ID  # noqa: E501

        :return: The item_id of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this OrderQuery.

        Item ID  # noqa: E501

        :param item_id: The item_id of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def last_name(self):
        """Gets the last_name of this OrderQuery.  # noqa: E501

        Last name  # noqa: E501

        :return: The last_name of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this OrderQuery.

        Last name  # noqa: E501

        :param last_name: The last_name of this OrderQuery.  # noqa: E501
        :type: str
        """
        if last_name is not None and len(last_name) > 30:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `30`")  # noqa: E501

        self._last_name = last_name

    @property
    def order_id(self):
        """Gets the order_id of this OrderQuery.  # noqa: E501

        Order ID  # noqa: E501

        :return: The order_id of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderQuery.

        Order ID  # noqa: E501

        :param order_id: The order_id of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def payment_date_begin(self):
        """Gets the payment_date_begin of this OrderQuery.  # noqa: E501

        Date/time that the order was successfully processed  # noqa: E501

        :return: The payment_date_begin of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._payment_date_begin

    @payment_date_begin.setter
    def payment_date_begin(self, payment_date_begin):
        """Sets the payment_date_begin of this OrderQuery.

        Date/time that the order was successfully processed  # noqa: E501

        :param payment_date_begin: The payment_date_begin of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._payment_date_begin = payment_date_begin

    @property
    def payment_date_end(self):
        """Gets the payment_date_end of this OrderQuery.  # noqa: E501

        Date/time that the order was successfully processed  # noqa: E501

        :return: The payment_date_end of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._payment_date_end

    @payment_date_end.setter
    def payment_date_end(self, payment_date_end):
        """Sets the payment_date_end of this OrderQuery.

        Date/time that the order was successfully processed  # noqa: E501

        :param payment_date_end: The payment_date_end of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._payment_date_end = payment_date_end

    @property
    def payment_method(self):
        """Gets the payment_method of this OrderQuery.  # noqa: E501

        Payment method  # noqa: E501

        :return: The payment_method of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this OrderQuery.

        Payment method  # noqa: E501

        :param payment_method: The payment_method of this OrderQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["Affirm", "Amazon", "Amazon SC", "Cash", "Check", "COD", "Credit Card", "eCheck", "LoanHero", "Money Order", "PayPal", "Purchase Order", "Quote Request", "Unknown", "Wire Transfer"]  # noqa: E501
        if payment_method not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_method` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_method, allowed_values)
            )

        self._payment_method = payment_method

    @property
    def phone(self):
        """Gets the phone of this OrderQuery.  # noqa: E501

        Phone  # noqa: E501

        :return: The phone of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this OrderQuery.

        Phone  # noqa: E501

        :param phone: The phone of this OrderQuery.  # noqa: E501
        :type: str
        """
        if phone is not None and len(phone) > 25:
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `25`")  # noqa: E501

        self._phone = phone

    @property
    def postal_code(self):
        """Gets the postal_code of this OrderQuery.  # noqa: E501

        Postal code  # noqa: E501

        :return: The postal_code of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this OrderQuery.

        Postal code  # noqa: E501

        :param postal_code: The postal_code of this OrderQuery.  # noqa: E501
        :type: str
        """
        if postal_code is not None and len(postal_code) > 20:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `20`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this OrderQuery.  # noqa: E501

        Purchase order number  # noqa: E501

        :return: The purchase_order_number of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this OrderQuery.

        Purchase order number  # noqa: E501

        :param purchase_order_number: The purchase_order_number of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._purchase_order_number = purchase_order_number

    @property
    def refund_date_begin(self):
        """Gets the refund_date_begin of this OrderQuery.  # noqa: E501

        Date/time that the order was refunded  # noqa: E501

        :return: The refund_date_begin of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._refund_date_begin

    @refund_date_begin.setter
    def refund_date_begin(self, refund_date_begin):
        """Sets the refund_date_begin of this OrderQuery.

        Date/time that the order was refunded  # noqa: E501

        :param refund_date_begin: The refund_date_begin of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._refund_date_begin = refund_date_begin

    @property
    def refund_date_end(self):
        """Gets the refund_date_end of this OrderQuery.  # noqa: E501

        Date/time that the order was refunded  # noqa: E501

        :return: The refund_date_end of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._refund_date_end

    @refund_date_end.setter
    def refund_date_end(self, refund_date_end):
        """Sets the refund_date_end of this OrderQuery.

        Date/time that the order was refunded  # noqa: E501

        :param refund_date_end: The refund_date_end of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._refund_date_end = refund_date_end

    @property
    def rma(self):
        """Gets the rma of this OrderQuery.  # noqa: E501

        RMA number  # noqa: E501

        :return: The rma of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._rma

    @rma.setter
    def rma(self, rma):
        """Sets the rma of this OrderQuery.

        RMA number  # noqa: E501

        :param rma: The rma of this OrderQuery.  # noqa: E501
        :type: str
        """
        if rma is not None and len(rma) > 30:
            raise ValueError("Invalid value for `rma`, length must be less than or equal to `30`")  # noqa: E501

        self._rma = rma

    @property
    def screen_branding_theme_code(self):
        """Gets the screen_branding_theme_code of this OrderQuery.  # noqa: E501

        Screen branding theme code associated with the order (legacy checkout)  # noqa: E501

        :return: The screen_branding_theme_code of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._screen_branding_theme_code

    @screen_branding_theme_code.setter
    def screen_branding_theme_code(self, screen_branding_theme_code):
        """Sets the screen_branding_theme_code of this OrderQuery.

        Screen branding theme code associated with the order (legacy checkout)  # noqa: E501

        :param screen_branding_theme_code: The screen_branding_theme_code of this OrderQuery.  # noqa: E501
        :type: str
        """
        if screen_branding_theme_code is not None and len(screen_branding_theme_code) > 10:
            raise ValueError("Invalid value for `screen_branding_theme_code`, length must be less than or equal to `10`")  # noqa: E501

        self._screen_branding_theme_code = screen_branding_theme_code

    @property
    def shipment_date_begin(self):
        """Gets the shipment_date_begin of this OrderQuery.  # noqa: E501

        Date/time that the order was shipping  # noqa: E501

        :return: The shipment_date_begin of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._shipment_date_begin

    @shipment_date_begin.setter
    def shipment_date_begin(self, shipment_date_begin):
        """Sets the shipment_date_begin of this OrderQuery.

        Date/time that the order was shipping  # noqa: E501

        :param shipment_date_begin: The shipment_date_begin of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._shipment_date_begin = shipment_date_begin

    @property
    def shipment_date_end(self):
        """Gets the shipment_date_end of this OrderQuery.  # noqa: E501

        Date/time that the order was shipped  # noqa: E501

        :return: The shipment_date_end of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._shipment_date_end

    @shipment_date_end.setter
    def shipment_date_end(self, shipment_date_end):
        """Sets the shipment_date_end of this OrderQuery.

        Date/time that the order was shipped  # noqa: E501

        :param shipment_date_end: The shipment_date_end of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._shipment_date_end = shipment_date_end

    @property
    def state_region(self):
        """Gets the state_region of this OrderQuery.  # noqa: E501

        State for United States otherwise region or province for other countries  # noqa: E501

        :return: The state_region of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._state_region

    @state_region.setter
    def state_region(self, state_region):
        """Sets the state_region of this OrderQuery.

        State for United States otherwise region or province for other countries  # noqa: E501

        :param state_region: The state_region of this OrderQuery.  # noqa: E501
        :type: str
        """
        if state_region is not None and len(state_region) > 32:
            raise ValueError("Invalid value for `state_region`, length must be less than or equal to `32`")  # noqa: E501

        self._state_region = state_region

    @property
    def storefront_host_name(self):
        """Gets the storefront_host_name of this OrderQuery.  # noqa: E501

        StoreFront host name associated with the order  # noqa: E501

        :return: The storefront_host_name of this OrderQuery.  # noqa: E501
        :rtype: str
        """
        return self._storefront_host_name

    @storefront_host_name.setter
    def storefront_host_name(self, storefront_host_name):
        """Sets the storefront_host_name of this OrderQuery.

        StoreFront host name associated with the order  # noqa: E501

        :param storefront_host_name: The storefront_host_name of this OrderQuery.  # noqa: E501
        :type: str
        """

        self._storefront_host_name = storefront_host_name

    @property
    def total(self):
        """Gets the total of this OrderQuery.  # noqa: E501

        Total  # noqa: E501

        :return: The total of this OrderQuery.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this OrderQuery.

        Total  # noqa: E501

        :param total: The total of this OrderQuery.  # noqa: E501
        :type: float
        """

        self._total = total

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
        if issubclass(OrderQuery, dict):
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
        if not isinstance(other, OrderQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other