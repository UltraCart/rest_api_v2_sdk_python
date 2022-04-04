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


class Cart(object):
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
        'affiliate': 'CartAffiliate',
        'affiliate_network_pixel_oid': 'int',
        'base_currency_code': 'str',
        'billing': 'CartBilling',
        'buysafe': 'CartBuysafe',
        'cart_id': 'str',
        'checkout': 'CartCheckout',
        'coupons': 'list[CartCoupon]',
        'currency_code': 'str',
        'currency_conversion': 'CartCurrencyConversion',
        'customer_profile': 'CartCustomerProfile',
        'exchange_rate': 'float',
        'gift': 'CartGift',
        'gift_certificate': 'CartGiftCertificate',
        'items': 'list[CartItem]',
        'language_iso_code': 'str',
        'logged_in': 'bool',
        'marketing': 'CartMarketing',
        'merchant_id': 'str',
        'payment': 'CartPayment',
        'properties': 'list[CartProperty]',
        'settings': 'CartSettings',
        'shipping': 'CartShipping',
        'summary': 'CartSummary',
        'taxes': 'CartTaxes',
        'upsell_after': 'CartUpsellAfter'
    }

    attribute_map = {
        'affiliate': 'affiliate',
        'affiliate_network_pixel_oid': 'affiliate_network_pixel_oid',
        'base_currency_code': 'base_currency_code',
        'billing': 'billing',
        'buysafe': 'buysafe',
        'cart_id': 'cart_id',
        'checkout': 'checkout',
        'coupons': 'coupons',
        'currency_code': 'currency_code',
        'currency_conversion': 'currency_conversion',
        'customer_profile': 'customer_profile',
        'exchange_rate': 'exchange_rate',
        'gift': 'gift',
        'gift_certificate': 'gift_certificate',
        'items': 'items',
        'language_iso_code': 'language_iso_code',
        'logged_in': 'logged_in',
        'marketing': 'marketing',
        'merchant_id': 'merchant_id',
        'payment': 'payment',
        'properties': 'properties',
        'settings': 'settings',
        'shipping': 'shipping',
        'summary': 'summary',
        'taxes': 'taxes',
        'upsell_after': 'upsell_after'
    }

    def __init__(self, affiliate=None, affiliate_network_pixel_oid=None, base_currency_code=None, billing=None, buysafe=None, cart_id=None, checkout=None, coupons=None, currency_code=None, currency_conversion=None, customer_profile=None, exchange_rate=None, gift=None, gift_certificate=None, items=None, language_iso_code=None, logged_in=None, marketing=None, merchant_id=None, payment=None, properties=None, settings=None, shipping=None, summary=None, taxes=None, upsell_after=None):  # noqa: E501
        """Cart - a model defined in Swagger"""  # noqa: E501

        self._affiliate = None
        self._affiliate_network_pixel_oid = None
        self._base_currency_code = None
        self._billing = None
        self._buysafe = None
        self._cart_id = None
        self._checkout = None
        self._coupons = None
        self._currency_code = None
        self._currency_conversion = None
        self._customer_profile = None
        self._exchange_rate = None
        self._gift = None
        self._gift_certificate = None
        self._items = None
        self._language_iso_code = None
        self._logged_in = None
        self._marketing = None
        self._merchant_id = None
        self._payment = None
        self._properties = None
        self._settings = None
        self._shipping = None
        self._summary = None
        self._taxes = None
        self._upsell_after = None
        self.discriminator = None

        if affiliate is not None:
            self.affiliate = affiliate
        if affiliate_network_pixel_oid is not None:
            self.affiliate_network_pixel_oid = affiliate_network_pixel_oid
        if base_currency_code is not None:
            self.base_currency_code = base_currency_code
        if billing is not None:
            self.billing = billing
        if buysafe is not None:
            self.buysafe = buysafe
        if cart_id is not None:
            self.cart_id = cart_id
        if checkout is not None:
            self.checkout = checkout
        if coupons is not None:
            self.coupons = coupons
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_conversion is not None:
            self.currency_conversion = currency_conversion
        if customer_profile is not None:
            self.customer_profile = customer_profile
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if gift is not None:
            self.gift = gift
        if gift_certificate is not None:
            self.gift_certificate = gift_certificate
        if items is not None:
            self.items = items
        if language_iso_code is not None:
            self.language_iso_code = language_iso_code
        if logged_in is not None:
            self.logged_in = logged_in
        if marketing is not None:
            self.marketing = marketing
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if payment is not None:
            self.payment = payment
        if properties is not None:
            self.properties = properties
        if settings is not None:
            self.settings = settings
        if shipping is not None:
            self.shipping = shipping
        if summary is not None:
            self.summary = summary
        if taxes is not None:
            self.taxes = taxes
        if upsell_after is not None:
            self.upsell_after = upsell_after

    @property
    def affiliate(self):
        """Gets the affiliate of this Cart.  # noqa: E501


        :return: The affiliate of this Cart.  # noqa: E501
        :rtype: CartAffiliate
        """
        return self._affiliate

    @affiliate.setter
    def affiliate(self, affiliate):
        """Sets the affiliate of this Cart.


        :param affiliate: The affiliate of this Cart.  # noqa: E501
        :type: CartAffiliate
        """

        self._affiliate = affiliate

    @property
    def affiliate_network_pixel_oid(self):
        """Gets the affiliate_network_pixel_oid of this Cart.  # noqa: E501

        The affiliate network pixel identifier associated with the cart  # noqa: E501

        :return: The affiliate_network_pixel_oid of this Cart.  # noqa: E501
        :rtype: int
        """
        return self._affiliate_network_pixel_oid

    @affiliate_network_pixel_oid.setter
    def affiliate_network_pixel_oid(self, affiliate_network_pixel_oid):
        """Sets the affiliate_network_pixel_oid of this Cart.

        The affiliate network pixel identifier associated with the cart  # noqa: E501

        :param affiliate_network_pixel_oid: The affiliate_network_pixel_oid of this Cart.  # noqa: E501
        :type: int
        """

        self._affiliate_network_pixel_oid = affiliate_network_pixel_oid

    @property
    def base_currency_code(self):
        """Gets the base_currency_code of this Cart.  # noqa: E501

        The ISO-4217 three letter base currency code of the account  # noqa: E501

        :return: The base_currency_code of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._base_currency_code

    @base_currency_code.setter
    def base_currency_code(self, base_currency_code):
        """Sets the base_currency_code of this Cart.

        The ISO-4217 three letter base currency code of the account  # noqa: E501

        :param base_currency_code: The base_currency_code of this Cart.  # noqa: E501
        :type: str
        """
        if base_currency_code is not None and len(base_currency_code) > 3:
            raise ValueError("Invalid value for `base_currency_code`, length must be less than or equal to `3`")  # noqa: E501

        self._base_currency_code = base_currency_code

    @property
    def billing(self):
        """Gets the billing of this Cart.  # noqa: E501


        :return: The billing of this Cart.  # noqa: E501
        :rtype: CartBilling
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this Cart.


        :param billing: The billing of this Cart.  # noqa: E501
        :type: CartBilling
        """

        self._billing = billing

    @property
    def buysafe(self):
        """Gets the buysafe of this Cart.  # noqa: E501


        :return: The buysafe of this Cart.  # noqa: E501
        :rtype: CartBuysafe
        """
        return self._buysafe

    @buysafe.setter
    def buysafe(self, buysafe):
        """Sets the buysafe of this Cart.


        :param buysafe: The buysafe of this Cart.  # noqa: E501
        :type: CartBuysafe
        """

        self._buysafe = buysafe

    @property
    def cart_id(self):
        """Gets the cart_id of this Cart.  # noqa: E501

        Unique identifier for this cart  # noqa: E501

        :return: The cart_id of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._cart_id

    @cart_id.setter
    def cart_id(self, cart_id):
        """Sets the cart_id of this Cart.

        Unique identifier for this cart  # noqa: E501

        :param cart_id: The cart_id of this Cart.  # noqa: E501
        :type: str
        """

        self._cart_id = cart_id

    @property
    def checkout(self):
        """Gets the checkout of this Cart.  # noqa: E501


        :return: The checkout of this Cart.  # noqa: E501
        :rtype: CartCheckout
        """
        return self._checkout

    @checkout.setter
    def checkout(self, checkout):
        """Sets the checkout of this Cart.


        :param checkout: The checkout of this Cart.  # noqa: E501
        :type: CartCheckout
        """

        self._checkout = checkout

    @property
    def coupons(self):
        """Gets the coupons of this Cart.  # noqa: E501

        Coupons  # noqa: E501

        :return: The coupons of this Cart.  # noqa: E501
        :rtype: list[CartCoupon]
        """
        return self._coupons

    @coupons.setter
    def coupons(self, coupons):
        """Sets the coupons of this Cart.

        Coupons  # noqa: E501

        :param coupons: The coupons of this Cart.  # noqa: E501
        :type: list[CartCoupon]
        """

        self._coupons = coupons

    @property
    def currency_code(self):
        """Gets the currency_code of this Cart.  # noqa: E501

        The ISO-4217 three letter currency code the customer is viewing prices in  # noqa: E501

        :return: The currency_code of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Cart.

        The ISO-4217 three letter currency code the customer is viewing prices in  # noqa: E501

        :param currency_code: The currency_code of this Cart.  # noqa: E501
        :type: str
        """
        if currency_code is not None and len(currency_code) > 3:
            raise ValueError("Invalid value for `currency_code`, length must be less than or equal to `3`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def currency_conversion(self):
        """Gets the currency_conversion of this Cart.  # noqa: E501


        :return: The currency_conversion of this Cart.  # noqa: E501
        :rtype: CartCurrencyConversion
        """
        return self._currency_conversion

    @currency_conversion.setter
    def currency_conversion(self, currency_conversion):
        """Sets the currency_conversion of this Cart.


        :param currency_conversion: The currency_conversion of this Cart.  # noqa: E501
        :type: CartCurrencyConversion
        """

        self._currency_conversion = currency_conversion

    @property
    def customer_profile(self):
        """Gets the customer_profile of this Cart.  # noqa: E501


        :return: The customer_profile of this Cart.  # noqa: E501
        :rtype: CartCustomerProfile
        """
        return self._customer_profile

    @customer_profile.setter
    def customer_profile(self, customer_profile):
        """Sets the customer_profile of this Cart.


        :param customer_profile: The customer_profile of this Cart.  # noqa: E501
        :type: CartCustomerProfile
        """

        self._customer_profile = customer_profile

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this Cart.  # noqa: E501

        The exchange rate if the customer is viewing a different currency than the base  # noqa: E501

        :return: The exchange_rate of this Cart.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this Cart.

        The exchange rate if the customer is viewing a different currency than the base  # noqa: E501

        :param exchange_rate: The exchange_rate of this Cart.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def gift(self):
        """Gets the gift of this Cart.  # noqa: E501


        :return: The gift of this Cart.  # noqa: E501
        :rtype: CartGift
        """
        return self._gift

    @gift.setter
    def gift(self, gift):
        """Sets the gift of this Cart.


        :param gift: The gift of this Cart.  # noqa: E501
        :type: CartGift
        """

        self._gift = gift

    @property
    def gift_certificate(self):
        """Gets the gift_certificate of this Cart.  # noqa: E501


        :return: The gift_certificate of this Cart.  # noqa: E501
        :rtype: CartGiftCertificate
        """
        return self._gift_certificate

    @gift_certificate.setter
    def gift_certificate(self, gift_certificate):
        """Sets the gift_certificate of this Cart.


        :param gift_certificate: The gift_certificate of this Cart.  # noqa: E501
        :type: CartGiftCertificate
        """

        self._gift_certificate = gift_certificate

    @property
    def items(self):
        """Gets the items of this Cart.  # noqa: E501

        Items  # noqa: E501

        :return: The items of this Cart.  # noqa: E501
        :rtype: list[CartItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Cart.

        Items  # noqa: E501

        :param items: The items of this Cart.  # noqa: E501
        :type: list[CartItem]
        """

        self._items = items

    @property
    def language_iso_code(self):
        """Gets the language_iso_code of this Cart.  # noqa: E501

        The ISO-631 three letter code the customer would like to checkout with  # noqa: E501

        :return: The language_iso_code of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._language_iso_code

    @language_iso_code.setter
    def language_iso_code(self, language_iso_code):
        """Sets the language_iso_code of this Cart.

        The ISO-631 three letter code the customer would like to checkout with  # noqa: E501

        :param language_iso_code: The language_iso_code of this Cart.  # noqa: E501
        :type: str
        """
        if language_iso_code is not None and len(language_iso_code) > 3:
            raise ValueError("Invalid value for `language_iso_code`, length must be less than or equal to `3`")  # noqa: E501

        self._language_iso_code = language_iso_code

    @property
    def logged_in(self):
        """Gets the logged_in of this Cart.  # noqa: E501

        True if the customer is logged into their profile  # noqa: E501

        :return: The logged_in of this Cart.  # noqa: E501
        :rtype: bool
        """
        return self._logged_in

    @logged_in.setter
    def logged_in(self, logged_in):
        """Sets the logged_in of this Cart.

        True if the customer is logged into their profile  # noqa: E501

        :param logged_in: The logged_in of this Cart.  # noqa: E501
        :type: bool
        """

        self._logged_in = logged_in

    @property
    def marketing(self):
        """Gets the marketing of this Cart.  # noqa: E501


        :return: The marketing of this Cart.  # noqa: E501
        :rtype: CartMarketing
        """
        return self._marketing

    @marketing.setter
    def marketing(self, marketing):
        """Sets the marketing of this Cart.


        :param marketing: The marketing of this Cart.  # noqa: E501
        :type: CartMarketing
        """

        self._marketing = marketing

    @property
    def merchant_id(self):
        """Gets the merchant_id of this Cart.  # noqa: E501

        Merchant ID this cart is associated with  # noqa: E501

        :return: The merchant_id of this Cart.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this Cart.

        Merchant ID this cart is associated with  # noqa: E501

        :param merchant_id: The merchant_id of this Cart.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def payment(self):
        """Gets the payment of this Cart.  # noqa: E501


        :return: The payment of this Cart.  # noqa: E501
        :rtype: CartPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this Cart.


        :param payment: The payment of this Cart.  # noqa: E501
        :type: CartPayment
        """

        self._payment = payment

    @property
    def properties(self):
        """Gets the properties of this Cart.  # noqa: E501

        Properties associated with the cart  # noqa: E501

        :return: The properties of this Cart.  # noqa: E501
        :rtype: list[CartProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Cart.

        Properties associated with the cart  # noqa: E501

        :param properties: The properties of this Cart.  # noqa: E501
        :type: list[CartProperty]
        """

        self._properties = properties

    @property
    def settings(self):
        """Gets the settings of this Cart.  # noqa: E501


        :return: The settings of this Cart.  # noqa: E501
        :rtype: CartSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Cart.


        :param settings: The settings of this Cart.  # noqa: E501
        :type: CartSettings
        """

        self._settings = settings

    @property
    def shipping(self):
        """Gets the shipping of this Cart.  # noqa: E501


        :return: The shipping of this Cart.  # noqa: E501
        :rtype: CartShipping
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this Cart.


        :param shipping: The shipping of this Cart.  # noqa: E501
        :type: CartShipping
        """

        self._shipping = shipping

    @property
    def summary(self):
        """Gets the summary of this Cart.  # noqa: E501


        :return: The summary of this Cart.  # noqa: E501
        :rtype: CartSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Cart.


        :param summary: The summary of this Cart.  # noqa: E501
        :type: CartSummary
        """

        self._summary = summary

    @property
    def taxes(self):
        """Gets the taxes of this Cart.  # noqa: E501


        :return: The taxes of this Cart.  # noqa: E501
        :rtype: CartTaxes
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this Cart.


        :param taxes: The taxes of this Cart.  # noqa: E501
        :type: CartTaxes
        """

        self._taxes = taxes

    @property
    def upsell_after(self):
        """Gets the upsell_after of this Cart.  # noqa: E501


        :return: The upsell_after of this Cart.  # noqa: E501
        :rtype: CartUpsellAfter
        """
        return self._upsell_after

    @upsell_after.setter
    def upsell_after(self, upsell_after):
        """Sets the upsell_after of this Cart.


        :param upsell_after: The upsell_after of this Cart.  # noqa: E501
        :type: CartUpsellAfter
        """

        self._upsell_after = upsell_after

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
        if issubclass(Cart, dict):
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
        if not isinstance(other, Cart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
