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


class PricingTier(object):
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
        'allow_3rd_party_billing': 'bool',
        'allow_cod': 'bool',
        'allow_purchase_order': 'bool',
        'allow_quote_request': 'bool',
        'approval_notification': 'PricingTierNotification',
        'auto_approve_cod': 'bool',
        'auto_approve_purchase_order': 'bool',
        'default_on_wholesale_signup': 'bool',
        'default_percentage_discount': 'float',
        'default_shipping_method_oid': 'int',
        'default_tier': 'bool',
        'display_on_wholesale_signup': 'bool',
        'exclude_from_free_promotion': 'bool',
        'exempt_shipping_handling_charge': 'bool',
        'free_shipping': 'bool',
        'free_shipping_minimum': 'float',
        'maximum_item_count': 'int',
        'minimum_item_count': 'int',
        'minimum_subtotal': 'float',
        'name': 'str',
        'no_coupons': 'bool',
        'no_free_shipping': 'bool',
        'no_realtime_charge': 'bool',
        'not_valid_when_coupon_present': 'bool',
        'pricing_tier_oid': 'int',
        'realtime_percentage_discount': 'float',
        'signup_notification': 'PricingTierNotification',
        'suppress_buysafe': 'bool',
        'suppress_mailing_list': 'bool',
        'tax_exempt': 'bool',
        'track_separately': 'bool'
    }

    attribute_map = {
        'allow_3rd_party_billing': 'allow_3rd_party_billing',
        'allow_cod': 'allow_cod',
        'allow_purchase_order': 'allow_purchase_order',
        'allow_quote_request': 'allow_quote_request',
        'approval_notification': 'approval_notification',
        'auto_approve_cod': 'auto_approve_cod',
        'auto_approve_purchase_order': 'auto_approve_purchase_order',
        'default_on_wholesale_signup': 'default_on_wholesale_signup',
        'default_percentage_discount': 'default_percentage_discount',
        'default_shipping_method_oid': 'default_shipping_method_oid',
        'default_tier': 'default_tier',
        'display_on_wholesale_signup': 'display_on_wholesale_signup',
        'exclude_from_free_promotion': 'exclude_from_free_promotion',
        'exempt_shipping_handling_charge': 'exempt_shipping_handling_charge',
        'free_shipping': 'free_shipping',
        'free_shipping_minimum': 'free_shipping_minimum',
        'maximum_item_count': 'maximum_item_count',
        'minimum_item_count': 'minimum_item_count',
        'minimum_subtotal': 'minimum_subtotal',
        'name': 'name',
        'no_coupons': 'no_coupons',
        'no_free_shipping': 'no_free_shipping',
        'no_realtime_charge': 'no_realtime_charge',
        'not_valid_when_coupon_present': 'not_valid_when_coupon_present',
        'pricing_tier_oid': 'pricing_tier_oid',
        'realtime_percentage_discount': 'realtime_percentage_discount',
        'signup_notification': 'signup_notification',
        'suppress_buysafe': 'suppress_buysafe',
        'suppress_mailing_list': 'suppress_mailing_list',
        'tax_exempt': 'tax_exempt',
        'track_separately': 'track_separately'
    }

    def __init__(self, allow_3rd_party_billing=None, allow_cod=None, allow_purchase_order=None, allow_quote_request=None, approval_notification=None, auto_approve_cod=None, auto_approve_purchase_order=None, default_on_wholesale_signup=None, default_percentage_discount=None, default_shipping_method_oid=None, default_tier=None, display_on_wholesale_signup=None, exclude_from_free_promotion=None, exempt_shipping_handling_charge=None, free_shipping=None, free_shipping_minimum=None, maximum_item_count=None, minimum_item_count=None, minimum_subtotal=None, name=None, no_coupons=None, no_free_shipping=None, no_realtime_charge=None, not_valid_when_coupon_present=None, pricing_tier_oid=None, realtime_percentage_discount=None, signup_notification=None, suppress_buysafe=None, suppress_mailing_list=None, tax_exempt=None, track_separately=None):  # noqa: E501
        """PricingTier - a model defined in Swagger"""  # noqa: E501

        self._allow_3rd_party_billing = None
        self._allow_cod = None
        self._allow_purchase_order = None
        self._allow_quote_request = None
        self._approval_notification = None
        self._auto_approve_cod = None
        self._auto_approve_purchase_order = None
        self._default_on_wholesale_signup = None
        self._default_percentage_discount = None
        self._default_shipping_method_oid = None
        self._default_tier = None
        self._display_on_wholesale_signup = None
        self._exclude_from_free_promotion = None
        self._exempt_shipping_handling_charge = None
        self._free_shipping = None
        self._free_shipping_minimum = None
        self._maximum_item_count = None
        self._minimum_item_count = None
        self._minimum_subtotal = None
        self._name = None
        self._no_coupons = None
        self._no_free_shipping = None
        self._no_realtime_charge = None
        self._not_valid_when_coupon_present = None
        self._pricing_tier_oid = None
        self._realtime_percentage_discount = None
        self._signup_notification = None
        self._suppress_buysafe = None
        self._suppress_mailing_list = None
        self._tax_exempt = None
        self._track_separately = None
        self.discriminator = None

        if allow_3rd_party_billing is not None:
            self.allow_3rd_party_billing = allow_3rd_party_billing
        if allow_cod is not None:
            self.allow_cod = allow_cod
        if allow_purchase_order is not None:
            self.allow_purchase_order = allow_purchase_order
        if allow_quote_request is not None:
            self.allow_quote_request = allow_quote_request
        if approval_notification is not None:
            self.approval_notification = approval_notification
        if auto_approve_cod is not None:
            self.auto_approve_cod = auto_approve_cod
        if auto_approve_purchase_order is not None:
            self.auto_approve_purchase_order = auto_approve_purchase_order
        if default_on_wholesale_signup is not None:
            self.default_on_wholesale_signup = default_on_wholesale_signup
        if default_percentage_discount is not None:
            self.default_percentage_discount = default_percentage_discount
        if default_shipping_method_oid is not None:
            self.default_shipping_method_oid = default_shipping_method_oid
        if default_tier is not None:
            self.default_tier = default_tier
        if display_on_wholesale_signup is not None:
            self.display_on_wholesale_signup = display_on_wholesale_signup
        if exclude_from_free_promotion is not None:
            self.exclude_from_free_promotion = exclude_from_free_promotion
        if exempt_shipping_handling_charge is not None:
            self.exempt_shipping_handling_charge = exempt_shipping_handling_charge
        if free_shipping is not None:
            self.free_shipping = free_shipping
        if free_shipping_minimum is not None:
            self.free_shipping_minimum = free_shipping_minimum
        if maximum_item_count is not None:
            self.maximum_item_count = maximum_item_count
        if minimum_item_count is not None:
            self.minimum_item_count = minimum_item_count
        if minimum_subtotal is not None:
            self.minimum_subtotal = minimum_subtotal
        if name is not None:
            self.name = name
        if no_coupons is not None:
            self.no_coupons = no_coupons
        if no_free_shipping is not None:
            self.no_free_shipping = no_free_shipping
        if no_realtime_charge is not None:
            self.no_realtime_charge = no_realtime_charge
        if not_valid_when_coupon_present is not None:
            self.not_valid_when_coupon_present = not_valid_when_coupon_present
        if pricing_tier_oid is not None:
            self.pricing_tier_oid = pricing_tier_oid
        if realtime_percentage_discount is not None:
            self.realtime_percentage_discount = realtime_percentage_discount
        if signup_notification is not None:
            self.signup_notification = signup_notification
        if suppress_buysafe is not None:
            self.suppress_buysafe = suppress_buysafe
        if suppress_mailing_list is not None:
            self.suppress_mailing_list = suppress_mailing_list
        if tax_exempt is not None:
            self.tax_exempt = tax_exempt
        if track_separately is not None:
            self.track_separately = track_separately

    @property
    def allow_3rd_party_billing(self):
        """Gets the allow_3rd_party_billing of this PricingTier.  # noqa: E501

        Allow 3rd party billing  # noqa: E501

        :return: The allow_3rd_party_billing of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._allow_3rd_party_billing

    @allow_3rd_party_billing.setter
    def allow_3rd_party_billing(self, allow_3rd_party_billing):
        """Sets the allow_3rd_party_billing of this PricingTier.

        Allow 3rd party billing  # noqa: E501

        :param allow_3rd_party_billing: The allow_3rd_party_billing of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._allow_3rd_party_billing = allow_3rd_party_billing

    @property
    def allow_cod(self):
        """Gets the allow_cod of this PricingTier.  # noqa: E501

        Allow COD  # noqa: E501

        :return: The allow_cod of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._allow_cod

    @allow_cod.setter
    def allow_cod(self, allow_cod):
        """Sets the allow_cod of this PricingTier.

        Allow COD  # noqa: E501

        :param allow_cod: The allow_cod of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._allow_cod = allow_cod

    @property
    def allow_purchase_order(self):
        """Gets the allow_purchase_order of this PricingTier.  # noqa: E501

        Allow purchase order  # noqa: E501

        :return: The allow_purchase_order of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._allow_purchase_order

    @allow_purchase_order.setter
    def allow_purchase_order(self, allow_purchase_order):
        """Sets the allow_purchase_order of this PricingTier.

        Allow purchase order  # noqa: E501

        :param allow_purchase_order: The allow_purchase_order of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._allow_purchase_order = allow_purchase_order

    @property
    def allow_quote_request(self):
        """Gets the allow_quote_request of this PricingTier.  # noqa: E501

        Allow quote request  # noqa: E501

        :return: The allow_quote_request of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._allow_quote_request

    @allow_quote_request.setter
    def allow_quote_request(self, allow_quote_request):
        """Sets the allow_quote_request of this PricingTier.

        Allow quote request  # noqa: E501

        :param allow_quote_request: The allow_quote_request of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._allow_quote_request = allow_quote_request

    @property
    def approval_notification(self):
        """Gets the approval_notification of this PricingTier.  # noqa: E501


        :return: The approval_notification of this PricingTier.  # noqa: E501
        :rtype: PricingTierNotification
        """
        return self._approval_notification

    @approval_notification.setter
    def approval_notification(self, approval_notification):
        """Sets the approval_notification of this PricingTier.


        :param approval_notification: The approval_notification of this PricingTier.  # noqa: E501
        :type: PricingTierNotification
        """

        self._approval_notification = approval_notification

    @property
    def auto_approve_cod(self):
        """Gets the auto_approve_cod of this PricingTier.  # noqa: E501

        Auto approve COD  # noqa: E501

        :return: The auto_approve_cod of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._auto_approve_cod

    @auto_approve_cod.setter
    def auto_approve_cod(self, auto_approve_cod):
        """Sets the auto_approve_cod of this PricingTier.

        Auto approve COD  # noqa: E501

        :param auto_approve_cod: The auto_approve_cod of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._auto_approve_cod = auto_approve_cod

    @property
    def auto_approve_purchase_order(self):
        """Gets the auto_approve_purchase_order of this PricingTier.  # noqa: E501

        Auto approve purchase order  # noqa: E501

        :return: The auto_approve_purchase_order of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._auto_approve_purchase_order

    @auto_approve_purchase_order.setter
    def auto_approve_purchase_order(self, auto_approve_purchase_order):
        """Sets the auto_approve_purchase_order of this PricingTier.

        Auto approve purchase order  # noqa: E501

        :param auto_approve_purchase_order: The auto_approve_purchase_order of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._auto_approve_purchase_order = auto_approve_purchase_order

    @property
    def default_on_wholesale_signup(self):
        """Gets the default_on_wholesale_signup of this PricingTier.  # noqa: E501

        Default on wholesale signup  # noqa: E501

        :return: The default_on_wholesale_signup of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._default_on_wholesale_signup

    @default_on_wholesale_signup.setter
    def default_on_wholesale_signup(self, default_on_wholesale_signup):
        """Sets the default_on_wholesale_signup of this PricingTier.

        Default on wholesale signup  # noqa: E501

        :param default_on_wholesale_signup: The default_on_wholesale_signup of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._default_on_wholesale_signup = default_on_wholesale_signup

    @property
    def default_percentage_discount(self):
        """Gets the default_percentage_discount of this PricingTier.  # noqa: E501

        Default percentage discount  # noqa: E501

        :return: The default_percentage_discount of this PricingTier.  # noqa: E501
        :rtype: float
        """
        return self._default_percentage_discount

    @default_percentage_discount.setter
    def default_percentage_discount(self, default_percentage_discount):
        """Sets the default_percentage_discount of this PricingTier.

        Default percentage discount  # noqa: E501

        :param default_percentage_discount: The default_percentage_discount of this PricingTier.  # noqa: E501
        :type: float
        """

        self._default_percentage_discount = default_percentage_discount

    @property
    def default_shipping_method_oid(self):
        """Gets the default_shipping_method_oid of this PricingTier.  # noqa: E501

        Default shipping method oid  # noqa: E501

        :return: The default_shipping_method_oid of this PricingTier.  # noqa: E501
        :rtype: int
        """
        return self._default_shipping_method_oid

    @default_shipping_method_oid.setter
    def default_shipping_method_oid(self, default_shipping_method_oid):
        """Sets the default_shipping_method_oid of this PricingTier.

        Default shipping method oid  # noqa: E501

        :param default_shipping_method_oid: The default_shipping_method_oid of this PricingTier.  # noqa: E501
        :type: int
        """

        self._default_shipping_method_oid = default_shipping_method_oid

    @property
    def default_tier(self):
        """Gets the default_tier of this PricingTier.  # noqa: E501

        Default tier  # noqa: E501

        :return: The default_tier of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._default_tier

    @default_tier.setter
    def default_tier(self, default_tier):
        """Sets the default_tier of this PricingTier.

        Default tier  # noqa: E501

        :param default_tier: The default_tier of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._default_tier = default_tier

    @property
    def display_on_wholesale_signup(self):
        """Gets the display_on_wholesale_signup of this PricingTier.  # noqa: E501

        Display on wholesale signup  # noqa: E501

        :return: The display_on_wholesale_signup of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._display_on_wholesale_signup

    @display_on_wholesale_signup.setter
    def display_on_wholesale_signup(self, display_on_wholesale_signup):
        """Sets the display_on_wholesale_signup of this PricingTier.

        Display on wholesale signup  # noqa: E501

        :param display_on_wholesale_signup: The display_on_wholesale_signup of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._display_on_wholesale_signup = display_on_wholesale_signup

    @property
    def exclude_from_free_promotion(self):
        """Gets the exclude_from_free_promotion of this PricingTier.  # noqa: E501

        Exclude from free promotion  # noqa: E501

        :return: The exclude_from_free_promotion of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_from_free_promotion

    @exclude_from_free_promotion.setter
    def exclude_from_free_promotion(self, exclude_from_free_promotion):
        """Sets the exclude_from_free_promotion of this PricingTier.

        Exclude from free promotion  # noqa: E501

        :param exclude_from_free_promotion: The exclude_from_free_promotion of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._exclude_from_free_promotion = exclude_from_free_promotion

    @property
    def exempt_shipping_handling_charge(self):
        """Gets the exempt_shipping_handling_charge of this PricingTier.  # noqa: E501

        Exempt shipping handling charge  # noqa: E501

        :return: The exempt_shipping_handling_charge of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._exempt_shipping_handling_charge

    @exempt_shipping_handling_charge.setter
    def exempt_shipping_handling_charge(self, exempt_shipping_handling_charge):
        """Sets the exempt_shipping_handling_charge of this PricingTier.

        Exempt shipping handling charge  # noqa: E501

        :param exempt_shipping_handling_charge: The exempt_shipping_handling_charge of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._exempt_shipping_handling_charge = exempt_shipping_handling_charge

    @property
    def free_shipping(self):
        """Gets the free_shipping of this PricingTier.  # noqa: E501

        Free shipping  # noqa: E501

        :return: The free_shipping of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._free_shipping

    @free_shipping.setter
    def free_shipping(self, free_shipping):
        """Sets the free_shipping of this PricingTier.

        Free shipping  # noqa: E501

        :param free_shipping: The free_shipping of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._free_shipping = free_shipping

    @property
    def free_shipping_minimum(self):
        """Gets the free_shipping_minimum of this PricingTier.  # noqa: E501

        Free shipping minimum  # noqa: E501

        :return: The free_shipping_minimum of this PricingTier.  # noqa: E501
        :rtype: float
        """
        return self._free_shipping_minimum

    @free_shipping_minimum.setter
    def free_shipping_minimum(self, free_shipping_minimum):
        """Sets the free_shipping_minimum of this PricingTier.

        Free shipping minimum  # noqa: E501

        :param free_shipping_minimum: The free_shipping_minimum of this PricingTier.  # noqa: E501
        :type: float
        """

        self._free_shipping_minimum = free_shipping_minimum

    @property
    def maximum_item_count(self):
        """Gets the maximum_item_count of this PricingTier.  # noqa: E501

        Maximum item count  # noqa: E501

        :return: The maximum_item_count of this PricingTier.  # noqa: E501
        :rtype: int
        """
        return self._maximum_item_count

    @maximum_item_count.setter
    def maximum_item_count(self, maximum_item_count):
        """Sets the maximum_item_count of this PricingTier.

        Maximum item count  # noqa: E501

        :param maximum_item_count: The maximum_item_count of this PricingTier.  # noqa: E501
        :type: int
        """

        self._maximum_item_count = maximum_item_count

    @property
    def minimum_item_count(self):
        """Gets the minimum_item_count of this PricingTier.  # noqa: E501

        Minimum item count  # noqa: E501

        :return: The minimum_item_count of this PricingTier.  # noqa: E501
        :rtype: int
        """
        return self._minimum_item_count

    @minimum_item_count.setter
    def minimum_item_count(self, minimum_item_count):
        """Sets the minimum_item_count of this PricingTier.

        Minimum item count  # noqa: E501

        :param minimum_item_count: The minimum_item_count of this PricingTier.  # noqa: E501
        :type: int
        """

        self._minimum_item_count = minimum_item_count

    @property
    def minimum_subtotal(self):
        """Gets the minimum_subtotal of this PricingTier.  # noqa: E501

        Minimum subtotal  # noqa: E501

        :return: The minimum_subtotal of this PricingTier.  # noqa: E501
        :rtype: float
        """
        return self._minimum_subtotal

    @minimum_subtotal.setter
    def minimum_subtotal(self, minimum_subtotal):
        """Sets the minimum_subtotal of this PricingTier.

        Minimum subtotal  # noqa: E501

        :param minimum_subtotal: The minimum_subtotal of this PricingTier.  # noqa: E501
        :type: float
        """

        self._minimum_subtotal = minimum_subtotal

    @property
    def name(self):
        """Gets the name of this PricingTier.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this PricingTier.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PricingTier.

        Name  # noqa: E501

        :param name: The name of this PricingTier.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501

        self._name = name

    @property
    def no_coupons(self):
        """Gets the no_coupons of this PricingTier.  # noqa: E501

        No coupons  # noqa: E501

        :return: The no_coupons of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._no_coupons

    @no_coupons.setter
    def no_coupons(self, no_coupons):
        """Sets the no_coupons of this PricingTier.

        No coupons  # noqa: E501

        :param no_coupons: The no_coupons of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._no_coupons = no_coupons

    @property
    def no_free_shipping(self):
        """Gets the no_free_shipping of this PricingTier.  # noqa: E501

        No free shipping  # noqa: E501

        :return: The no_free_shipping of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._no_free_shipping

    @no_free_shipping.setter
    def no_free_shipping(self, no_free_shipping):
        """Sets the no_free_shipping of this PricingTier.

        No free shipping  # noqa: E501

        :param no_free_shipping: The no_free_shipping of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._no_free_shipping = no_free_shipping

    @property
    def no_realtime_charge(self):
        """Gets the no_realtime_charge of this PricingTier.  # noqa: E501

        No realtime charge  # noqa: E501

        :return: The no_realtime_charge of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._no_realtime_charge

    @no_realtime_charge.setter
    def no_realtime_charge(self, no_realtime_charge):
        """Sets the no_realtime_charge of this PricingTier.

        No realtime charge  # noqa: E501

        :param no_realtime_charge: The no_realtime_charge of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._no_realtime_charge = no_realtime_charge

    @property
    def not_valid_when_coupon_present(self):
        """Gets the not_valid_when_coupon_present of this PricingTier.  # noqa: E501

        Not valid when coupon present  # noqa: E501

        :return: The not_valid_when_coupon_present of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._not_valid_when_coupon_present

    @not_valid_when_coupon_present.setter
    def not_valid_when_coupon_present(self, not_valid_when_coupon_present):
        """Sets the not_valid_when_coupon_present of this PricingTier.

        Not valid when coupon present  # noqa: E501

        :param not_valid_when_coupon_present: The not_valid_when_coupon_present of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._not_valid_when_coupon_present = not_valid_when_coupon_present

    @property
    def pricing_tier_oid(self):
        """Gets the pricing_tier_oid of this PricingTier.  # noqa: E501

        Pricing Tier Oid  # noqa: E501

        :return: The pricing_tier_oid of this PricingTier.  # noqa: E501
        :rtype: int
        """
        return self._pricing_tier_oid

    @pricing_tier_oid.setter
    def pricing_tier_oid(self, pricing_tier_oid):
        """Sets the pricing_tier_oid of this PricingTier.

        Pricing Tier Oid  # noqa: E501

        :param pricing_tier_oid: The pricing_tier_oid of this PricingTier.  # noqa: E501
        :type: int
        """

        self._pricing_tier_oid = pricing_tier_oid

    @property
    def realtime_percentage_discount(self):
        """Gets the realtime_percentage_discount of this PricingTier.  # noqa: E501

        Realtime percentage discount  # noqa: E501

        :return: The realtime_percentage_discount of this PricingTier.  # noqa: E501
        :rtype: float
        """
        return self._realtime_percentage_discount

    @realtime_percentage_discount.setter
    def realtime_percentage_discount(self, realtime_percentage_discount):
        """Sets the realtime_percentage_discount of this PricingTier.

        Realtime percentage discount  # noqa: E501

        :param realtime_percentage_discount: The realtime_percentage_discount of this PricingTier.  # noqa: E501
        :type: float
        """

        self._realtime_percentage_discount = realtime_percentage_discount

    @property
    def signup_notification(self):
        """Gets the signup_notification of this PricingTier.  # noqa: E501


        :return: The signup_notification of this PricingTier.  # noqa: E501
        :rtype: PricingTierNotification
        """
        return self._signup_notification

    @signup_notification.setter
    def signup_notification(self, signup_notification):
        """Sets the signup_notification of this PricingTier.


        :param signup_notification: The signup_notification of this PricingTier.  # noqa: E501
        :type: PricingTierNotification
        """

        self._signup_notification = signup_notification

    @property
    def suppress_buysafe(self):
        """Gets the suppress_buysafe of this PricingTier.  # noqa: E501

        Suppress buySAFE (deprecated)  # noqa: E501

        :return: The suppress_buysafe of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_buysafe

    @suppress_buysafe.setter
    def suppress_buysafe(self, suppress_buysafe):
        """Sets the suppress_buysafe of this PricingTier.

        Suppress buySAFE (deprecated)  # noqa: E501

        :param suppress_buysafe: The suppress_buysafe of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._suppress_buysafe = suppress_buysafe

    @property
    def suppress_mailing_list(self):
        """Gets the suppress_mailing_list of this PricingTier.  # noqa: E501

        Suppress mailing list  # noqa: E501

        :return: The suppress_mailing_list of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_mailing_list

    @suppress_mailing_list.setter
    def suppress_mailing_list(self, suppress_mailing_list):
        """Sets the suppress_mailing_list of this PricingTier.

        Suppress mailing list  # noqa: E501

        :param suppress_mailing_list: The suppress_mailing_list of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._suppress_mailing_list = suppress_mailing_list

    @property
    def tax_exempt(self):
        """Gets the tax_exempt of this PricingTier.  # noqa: E501

        Tax Exempt  # noqa: E501

        :return: The tax_exempt of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._tax_exempt

    @tax_exempt.setter
    def tax_exempt(self, tax_exempt):
        """Sets the tax_exempt of this PricingTier.

        Tax Exempt  # noqa: E501

        :param tax_exempt: The tax_exempt of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._tax_exempt = tax_exempt

    @property
    def track_separately(self):
        """Gets the track_separately of this PricingTier.  # noqa: E501

        Track separately  # noqa: E501

        :return: The track_separately of this PricingTier.  # noqa: E501
        :rtype: bool
        """
        return self._track_separately

    @track_separately.setter
    def track_separately(self, track_separately):
        """Sets the track_separately of this PricingTier.

        Track separately  # noqa: E501

        :param track_separately: The track_separately of this PricingTier.  # noqa: E501
        :type: bool
        """

        self._track_separately = track_separately

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
        if issubclass(PricingTier, dict):
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
        if not isinstance(other, PricingTier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
