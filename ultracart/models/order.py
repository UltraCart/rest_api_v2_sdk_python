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


class Order(object):
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
        'affiliates': 'list[OrderAffiliate]',
        'auto_order': 'OrderAutoOrder',
        'billing': 'OrderBilling',
        'buysafe': 'OrderBuysafe',
        'channel_partner': 'OrderChannelPartner',
        'checkout': 'OrderCheckout',
        'coupons': 'list[OrderCoupon]',
        'creation_dts': 'str',
        'currency_code': 'str',
        'current_stage': 'str',
        'current_stage_histories': 'list[OrderCurrentStageHistory]',
        'customer_profile': 'Customer',
        'digital_order': 'OrderDigitalOrder',
        'edi': 'OrderEdi',
        'exchange_rate': 'float',
        'fraud_score': 'OrderFraudScore',
        'gift': 'OrderGift',
        'gift_certificate': 'OrderGiftCertificate',
        'internal': 'OrderInternal',
        'items': 'list[OrderItem]',
        'language_iso_code': 'str',
        'linked_shipment': 'OrderLinkedShipment',
        'marketing': 'OrderMarketing',
        'merchant_id': 'str',
        'order_id': 'str',
        'payment': 'OrderPayment',
        'point_of_sale': 'OrderPointOfSale',
        'properties': 'list[OrderProperty]',
        'quote': 'OrderQuote',
        'refund_dts': 'str',
        'refund_reason': 'str',
        'reject_dts': 'str',
        'reject_reason': 'str',
        'salesforce': 'OrderSalesforce',
        'shipping': 'OrderShipping',
        'summary': 'OrderSummary',
        'tags': 'list[OrderTag]',
        'taxes': 'OrderTaxes',
        'utms': 'list[OrderUtm]'
    }

    attribute_map = {
        'affiliates': 'affiliates',
        'auto_order': 'auto_order',
        'billing': 'billing',
        'buysafe': 'buysafe',
        'channel_partner': 'channel_partner',
        'checkout': 'checkout',
        'coupons': 'coupons',
        'creation_dts': 'creation_dts',
        'currency_code': 'currency_code',
        'current_stage': 'current_stage',
        'current_stage_histories': 'current_stage_histories',
        'customer_profile': 'customer_profile',
        'digital_order': 'digital_order',
        'edi': 'edi',
        'exchange_rate': 'exchange_rate',
        'fraud_score': 'fraud_score',
        'gift': 'gift',
        'gift_certificate': 'gift_certificate',
        'internal': 'internal',
        'items': 'items',
        'language_iso_code': 'language_iso_code',
        'linked_shipment': 'linked_shipment',
        'marketing': 'marketing',
        'merchant_id': 'merchant_id',
        'order_id': 'order_id',
        'payment': 'payment',
        'point_of_sale': 'point_of_sale',
        'properties': 'properties',
        'quote': 'quote',
        'refund_dts': 'refund_dts',
        'refund_reason': 'refund_reason',
        'reject_dts': 'reject_dts',
        'reject_reason': 'reject_reason',
        'salesforce': 'salesforce',
        'shipping': 'shipping',
        'summary': 'summary',
        'tags': 'Tags',
        'taxes': 'taxes',
        'utms': 'utms'
    }

    def __init__(self, affiliates=None, auto_order=None, billing=None, buysafe=None, channel_partner=None, checkout=None, coupons=None, creation_dts=None, currency_code=None, current_stage=None, current_stage_histories=None, customer_profile=None, digital_order=None, edi=None, exchange_rate=None, fraud_score=None, gift=None, gift_certificate=None, internal=None, items=None, language_iso_code=None, linked_shipment=None, marketing=None, merchant_id=None, order_id=None, payment=None, point_of_sale=None, properties=None, quote=None, refund_dts=None, refund_reason=None, reject_dts=None, reject_reason=None, salesforce=None, shipping=None, summary=None, tags=None, taxes=None, utms=None):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501

        self._affiliates = None
        self._auto_order = None
        self._billing = None
        self._buysafe = None
        self._channel_partner = None
        self._checkout = None
        self._coupons = None
        self._creation_dts = None
        self._currency_code = None
        self._current_stage = None
        self._current_stage_histories = None
        self._customer_profile = None
        self._digital_order = None
        self._edi = None
        self._exchange_rate = None
        self._fraud_score = None
        self._gift = None
        self._gift_certificate = None
        self._internal = None
        self._items = None
        self._language_iso_code = None
        self._linked_shipment = None
        self._marketing = None
        self._merchant_id = None
        self._order_id = None
        self._payment = None
        self._point_of_sale = None
        self._properties = None
        self._quote = None
        self._refund_dts = None
        self._refund_reason = None
        self._reject_dts = None
        self._reject_reason = None
        self._salesforce = None
        self._shipping = None
        self._summary = None
        self._tags = None
        self._taxes = None
        self._utms = None
        self.discriminator = None

        if affiliates is not None:
            self.affiliates = affiliates
        if auto_order is not None:
            self.auto_order = auto_order
        if billing is not None:
            self.billing = billing
        if buysafe is not None:
            self.buysafe = buysafe
        if channel_partner is not None:
            self.channel_partner = channel_partner
        if checkout is not None:
            self.checkout = checkout
        if coupons is not None:
            self.coupons = coupons
        if creation_dts is not None:
            self.creation_dts = creation_dts
        if currency_code is not None:
            self.currency_code = currency_code
        if current_stage is not None:
            self.current_stage = current_stage
        if current_stage_histories is not None:
            self.current_stage_histories = current_stage_histories
        if customer_profile is not None:
            self.customer_profile = customer_profile
        if digital_order is not None:
            self.digital_order = digital_order
        if edi is not None:
            self.edi = edi
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if fraud_score is not None:
            self.fraud_score = fraud_score
        if gift is not None:
            self.gift = gift
        if gift_certificate is not None:
            self.gift_certificate = gift_certificate
        if internal is not None:
            self.internal = internal
        if items is not None:
            self.items = items
        if language_iso_code is not None:
            self.language_iso_code = language_iso_code
        if linked_shipment is not None:
            self.linked_shipment = linked_shipment
        if marketing is not None:
            self.marketing = marketing
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if order_id is not None:
            self.order_id = order_id
        if payment is not None:
            self.payment = payment
        if point_of_sale is not None:
            self.point_of_sale = point_of_sale
        if properties is not None:
            self.properties = properties
        if quote is not None:
            self.quote = quote
        if refund_dts is not None:
            self.refund_dts = refund_dts
        if refund_reason is not None:
            self.refund_reason = refund_reason
        if reject_dts is not None:
            self.reject_dts = reject_dts
        if reject_reason is not None:
            self.reject_reason = reject_reason
        if salesforce is not None:
            self.salesforce = salesforce
        if shipping is not None:
            self.shipping = shipping
        if summary is not None:
            self.summary = summary
        if tags is not None:
            self.tags = tags
        if taxes is not None:
            self.taxes = taxes
        if utms is not None:
            self.utms = utms

    @property
    def affiliates(self):
        """Gets the affiliates of this Order.  # noqa: E501

        Affiliates if any were associated with the order.  The first one in the array sent the order and each subsequent affiliate is the recruiter that earns a downline commission.  # noqa: E501

        :return: The affiliates of this Order.  # noqa: E501
        :rtype: list[OrderAffiliate]
        """
        return self._affiliates

    @affiliates.setter
    def affiliates(self, affiliates):
        """Sets the affiliates of this Order.

        Affiliates if any were associated with the order.  The first one in the array sent the order and each subsequent affiliate is the recruiter that earns a downline commission.  # noqa: E501

        :param affiliates: The affiliates of this Order.  # noqa: E501
        :type: list[OrderAffiliate]
        """

        self._affiliates = affiliates

    @property
    def auto_order(self):
        """Gets the auto_order of this Order.  # noqa: E501


        :return: The auto_order of this Order.  # noqa: E501
        :rtype: OrderAutoOrder
        """
        return self._auto_order

    @auto_order.setter
    def auto_order(self, auto_order):
        """Sets the auto_order of this Order.


        :param auto_order: The auto_order of this Order.  # noqa: E501
        :type: OrderAutoOrder
        """

        self._auto_order = auto_order

    @property
    def billing(self):
        """Gets the billing of this Order.  # noqa: E501


        :return: The billing of this Order.  # noqa: E501
        :rtype: OrderBilling
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this Order.


        :param billing: The billing of this Order.  # noqa: E501
        :type: OrderBilling
        """

        self._billing = billing

    @property
    def buysafe(self):
        """Gets the buysafe of this Order.  # noqa: E501


        :return: The buysafe of this Order.  # noqa: E501
        :rtype: OrderBuysafe
        """
        return self._buysafe

    @buysafe.setter
    def buysafe(self, buysafe):
        """Sets the buysafe of this Order.


        :param buysafe: The buysafe of this Order.  # noqa: E501
        :type: OrderBuysafe
        """

        self._buysafe = buysafe

    @property
    def channel_partner(self):
        """Gets the channel_partner of this Order.  # noqa: E501


        :return: The channel_partner of this Order.  # noqa: E501
        :rtype: OrderChannelPartner
        """
        return self._channel_partner

    @channel_partner.setter
    def channel_partner(self, channel_partner):
        """Sets the channel_partner of this Order.


        :param channel_partner: The channel_partner of this Order.  # noqa: E501
        :type: OrderChannelPartner
        """

        self._channel_partner = channel_partner

    @property
    def checkout(self):
        """Gets the checkout of this Order.  # noqa: E501


        :return: The checkout of this Order.  # noqa: E501
        :rtype: OrderCheckout
        """
        return self._checkout

    @checkout.setter
    def checkout(self, checkout):
        """Sets the checkout of this Order.


        :param checkout: The checkout of this Order.  # noqa: E501
        :type: OrderCheckout
        """

        self._checkout = checkout

    @property
    def coupons(self):
        """Gets the coupons of this Order.  # noqa: E501

        Coupons  # noqa: E501

        :return: The coupons of this Order.  # noqa: E501
        :rtype: list[OrderCoupon]
        """
        return self._coupons

    @coupons.setter
    def coupons(self, coupons):
        """Sets the coupons of this Order.

        Coupons  # noqa: E501

        :param coupons: The coupons of this Order.  # noqa: E501
        :type: list[OrderCoupon]
        """

        self._coupons = coupons

    @property
    def creation_dts(self):
        """Gets the creation_dts of this Order.  # noqa: E501

        Date/time that the order was created  # noqa: E501

        :return: The creation_dts of this Order.  # noqa: E501
        :rtype: str
        """
        return self._creation_dts

    @creation_dts.setter
    def creation_dts(self, creation_dts):
        """Sets the creation_dts of this Order.

        Date/time that the order was created  # noqa: E501

        :param creation_dts: The creation_dts of this Order.  # noqa: E501
        :type: str
        """

        self._creation_dts = creation_dts

    @property
    def currency_code(self):
        """Gets the currency_code of this Order.  # noqa: E501

        Currency code that the customer used if different than the merchant's base currency code  # noqa: E501

        :return: The currency_code of this Order.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Order.

        Currency code that the customer used if different than the merchant's base currency code  # noqa: E501

        :param currency_code: The currency_code of this Order.  # noqa: E501
        :type: str
        """
        if currency_code is not None and len(currency_code) > 3:
            raise ValueError("Invalid value for `currency_code`, length must be less than or equal to `3`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def current_stage(self):
        """Gets the current_stage of this Order.  # noqa: E501

        Current stage that the order is in.  # noqa: E501

        :return: The current_stage of this Order.  # noqa: E501
        :rtype: str
        """
        return self._current_stage

    @current_stage.setter
    def current_stage(self, current_stage):
        """Sets the current_stage of this Order.

        Current stage that the order is in.  # noqa: E501

        :param current_stage: The current_stage of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["Accounts Receivable", "Pending Clearance", "Fraud Review", "Rejected", "Shipping Department", "Completed Order", "Quote Request", "Quote Sent", "Least Cost Routing", "Unknown", "Pre-ordered", "Advanced Order Routing", "Hold"]  # noqa: E501
        if current_stage not in allowed_values:
            raise ValueError(
                "Invalid value for `current_stage` ({0}), must be one of {1}"  # noqa: E501
                .format(current_stage, allowed_values)
            )

        self._current_stage = current_stage

    @property
    def current_stage_histories(self):
        """Gets the current_stage_histories of this Order.  # noqa: E501

        History of the changes to the current_stage field  # noqa: E501

        :return: The current_stage_histories of this Order.  # noqa: E501
        :rtype: list[OrderCurrentStageHistory]
        """
        return self._current_stage_histories

    @current_stage_histories.setter
    def current_stage_histories(self, current_stage_histories):
        """Sets the current_stage_histories of this Order.

        History of the changes to the current_stage field  # noqa: E501

        :param current_stage_histories: The current_stage_histories of this Order.  # noqa: E501
        :type: list[OrderCurrentStageHistory]
        """

        self._current_stage_histories = current_stage_histories

    @property
    def customer_profile(self):
        """Gets the customer_profile of this Order.  # noqa: E501


        :return: The customer_profile of this Order.  # noqa: E501
        :rtype: Customer
        """
        return self._customer_profile

    @customer_profile.setter
    def customer_profile(self, customer_profile):
        """Sets the customer_profile of this Order.


        :param customer_profile: The customer_profile of this Order.  # noqa: E501
        :type: Customer
        """

        self._customer_profile = customer_profile

    @property
    def digital_order(self):
        """Gets the digital_order of this Order.  # noqa: E501


        :return: The digital_order of this Order.  # noqa: E501
        :rtype: OrderDigitalOrder
        """
        return self._digital_order

    @digital_order.setter
    def digital_order(self, digital_order):
        """Sets the digital_order of this Order.


        :param digital_order: The digital_order of this Order.  # noqa: E501
        :type: OrderDigitalOrder
        """

        self._digital_order = digital_order

    @property
    def edi(self):
        """Gets the edi of this Order.  # noqa: E501


        :return: The edi of this Order.  # noqa: E501
        :rtype: OrderEdi
        """
        return self._edi

    @edi.setter
    def edi(self, edi):
        """Sets the edi of this Order.


        :param edi: The edi of this Order.  # noqa: E501
        :type: OrderEdi
        """

        self._edi = edi

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this Order.  # noqa: E501

        Exchange rate at the time the order was placed if currency code is different than the base currency  # noqa: E501

        :return: The exchange_rate of this Order.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this Order.

        Exchange rate at the time the order was placed if currency code is different than the base currency  # noqa: E501

        :param exchange_rate: The exchange_rate of this Order.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def fraud_score(self):
        """Gets the fraud_score of this Order.  # noqa: E501


        :return: The fraud_score of this Order.  # noqa: E501
        :rtype: OrderFraudScore
        """
        return self._fraud_score

    @fraud_score.setter
    def fraud_score(self, fraud_score):
        """Sets the fraud_score of this Order.


        :param fraud_score: The fraud_score of this Order.  # noqa: E501
        :type: OrderFraudScore
        """

        self._fraud_score = fraud_score

    @property
    def gift(self):
        """Gets the gift of this Order.  # noqa: E501


        :return: The gift of this Order.  # noqa: E501
        :rtype: OrderGift
        """
        return self._gift

    @gift.setter
    def gift(self, gift):
        """Sets the gift of this Order.


        :param gift: The gift of this Order.  # noqa: E501
        :type: OrderGift
        """

        self._gift = gift

    @property
    def gift_certificate(self):
        """Gets the gift_certificate of this Order.  # noqa: E501


        :return: The gift_certificate of this Order.  # noqa: E501
        :rtype: OrderGiftCertificate
        """
        return self._gift_certificate

    @gift_certificate.setter
    def gift_certificate(self, gift_certificate):
        """Sets the gift_certificate of this Order.


        :param gift_certificate: The gift_certificate of this Order.  # noqa: E501
        :type: OrderGiftCertificate
        """

        self._gift_certificate = gift_certificate

    @property
    def internal(self):
        """Gets the internal of this Order.  # noqa: E501


        :return: The internal of this Order.  # noqa: E501
        :rtype: OrderInternal
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this Order.


        :param internal: The internal of this Order.  # noqa: E501
        :type: OrderInternal
        """

        self._internal = internal

    @property
    def items(self):
        """Gets the items of this Order.  # noqa: E501

        Items  # noqa: E501

        :return: The items of this Order.  # noqa: E501
        :rtype: list[OrderItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Order.

        Items  # noqa: E501

        :param items: The items of this Order.  # noqa: E501
        :type: list[OrderItem]
        """

        self._items = items

    @property
    def language_iso_code(self):
        """Gets the language_iso_code of this Order.  # noqa: E501

        Three letter ISO-639 language code used by the customer during the checkout if different than the default language  # noqa: E501

        :return: The language_iso_code of this Order.  # noqa: E501
        :rtype: str
        """
        return self._language_iso_code

    @language_iso_code.setter
    def language_iso_code(self, language_iso_code):
        """Sets the language_iso_code of this Order.

        Three letter ISO-639 language code used by the customer during the checkout if different than the default language  # noqa: E501

        :param language_iso_code: The language_iso_code of this Order.  # noqa: E501
        :type: str
        """
        if language_iso_code is not None and len(language_iso_code) > 3:
            raise ValueError("Invalid value for `language_iso_code`, length must be less than or equal to `3`")  # noqa: E501

        self._language_iso_code = language_iso_code

    @property
    def linked_shipment(self):
        """Gets the linked_shipment of this Order.  # noqa: E501


        :return: The linked_shipment of this Order.  # noqa: E501
        :rtype: OrderLinkedShipment
        """
        return self._linked_shipment

    @linked_shipment.setter
    def linked_shipment(self, linked_shipment):
        """Sets the linked_shipment of this Order.


        :param linked_shipment: The linked_shipment of this Order.  # noqa: E501
        :type: OrderLinkedShipment
        """

        self._linked_shipment = linked_shipment

    @property
    def marketing(self):
        """Gets the marketing of this Order.  # noqa: E501


        :return: The marketing of this Order.  # noqa: E501
        :rtype: OrderMarketing
        """
        return self._marketing

    @marketing.setter
    def marketing(self, marketing):
        """Sets the marketing of this Order.


        :param marketing: The marketing of this Order.  # noqa: E501
        :type: OrderMarketing
        """

        self._marketing = marketing

    @property
    def merchant_id(self):
        """Gets the merchant_id of this Order.  # noqa: E501

        UltraCart merchant ID owning this order  # noqa: E501

        :return: The merchant_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this Order.

        UltraCart merchant ID owning this order  # noqa: E501

        :param merchant_id: The merchant_id of this Order.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def order_id(self):
        """Gets the order_id of this Order.  # noqa: E501

        Order ID  # noqa: E501

        :return: The order_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Order.

        Order ID  # noqa: E501

        :param order_id: The order_id of this Order.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def payment(self):
        """Gets the payment of this Order.  # noqa: E501


        :return: The payment of this Order.  # noqa: E501
        :rtype: OrderPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this Order.


        :param payment: The payment of this Order.  # noqa: E501
        :type: OrderPayment
        """

        self._payment = payment

    @property
    def point_of_sale(self):
        """Gets the point_of_sale of this Order.  # noqa: E501


        :return: The point_of_sale of this Order.  # noqa: E501
        :rtype: OrderPointOfSale
        """
        return self._point_of_sale

    @point_of_sale.setter
    def point_of_sale(self, point_of_sale):
        """Sets the point_of_sale of this Order.


        :param point_of_sale: The point_of_sale of this Order.  # noqa: E501
        :type: OrderPointOfSale
        """

        self._point_of_sale = point_of_sale

    @property
    def properties(self):
        """Gets the properties of this Order.  # noqa: E501

        Properties, available only through update, not through insert due to the nature of how properties are handled internally  # noqa: E501

        :return: The properties of this Order.  # noqa: E501
        :rtype: list[OrderProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Order.

        Properties, available only through update, not through insert due to the nature of how properties are handled internally  # noqa: E501

        :param properties: The properties of this Order.  # noqa: E501
        :type: list[OrderProperty]
        """

        self._properties = properties

    @property
    def quote(self):
        """Gets the quote of this Order.  # noqa: E501


        :return: The quote of this Order.  # noqa: E501
        :rtype: OrderQuote
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this Order.


        :param quote: The quote of this Order.  # noqa: E501
        :type: OrderQuote
        """

        self._quote = quote

    @property
    def refund_dts(self):
        """Gets the refund_dts of this Order.  # noqa: E501

        If the order was refunded, the date/time that the last refund occurred  # noqa: E501

        :return: The refund_dts of this Order.  # noqa: E501
        :rtype: str
        """
        return self._refund_dts

    @refund_dts.setter
    def refund_dts(self, refund_dts):
        """Sets the refund_dts of this Order.

        If the order was refunded, the date/time that the last refund occurred  # noqa: E501

        :param refund_dts: The refund_dts of this Order.  # noqa: E501
        :type: str
        """

        self._refund_dts = refund_dts

    @property
    def refund_reason(self):
        """Gets the refund_reason of this Order.  # noqa: E501

        Refund reason code.  This can only be written during a refund operation otherwise this field is read only.  # noqa: E501

        :return: The refund_reason of this Order.  # noqa: E501
        :rtype: str
        """
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, refund_reason):
        """Sets the refund_reason of this Order.

        Refund reason code.  This can only be written during a refund operation otherwise this field is read only.  # noqa: E501

        :param refund_reason: The refund_reason of this Order.  # noqa: E501
        :type: str
        """

        self._refund_reason = refund_reason

    @property
    def reject_dts(self):
        """Gets the reject_dts of this Order.  # noqa: E501

        If the order was rejected, the date/time that the rejection occurred  # noqa: E501

        :return: The reject_dts of this Order.  # noqa: E501
        :rtype: str
        """
        return self._reject_dts

    @reject_dts.setter
    def reject_dts(self, reject_dts):
        """Sets the reject_dts of this Order.

        If the order was rejected, the date/time that the rejection occurred  # noqa: E501

        :param reject_dts: The reject_dts of this Order.  # noqa: E501
        :type: str
        """

        self._reject_dts = reject_dts

    @property
    def reject_reason(self):
        """Gets the reject_reason of this Order.  # noqa: E501

        Reject reason code.  This can only be written during a reject operation otherwise this field is read only.  # noqa: E501

        :return: The reject_reason of this Order.  # noqa: E501
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """Sets the reject_reason of this Order.

        Reject reason code.  This can only be written during a reject operation otherwise this field is read only.  # noqa: E501

        :param reject_reason: The reject_reason of this Order.  # noqa: E501
        :type: str
        """

        self._reject_reason = reject_reason

    @property
    def salesforce(self):
        """Gets the salesforce of this Order.  # noqa: E501


        :return: The salesforce of this Order.  # noqa: E501
        :rtype: OrderSalesforce
        """
        return self._salesforce

    @salesforce.setter
    def salesforce(self, salesforce):
        """Sets the salesforce of this Order.


        :param salesforce: The salesforce of this Order.  # noqa: E501
        :type: OrderSalesforce
        """

        self._salesforce = salesforce

    @property
    def shipping(self):
        """Gets the shipping of this Order.  # noqa: E501


        :return: The shipping of this Order.  # noqa: E501
        :rtype: OrderShipping
        """
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        """Sets the shipping of this Order.


        :param shipping: The shipping of this Order.  # noqa: E501
        :type: OrderShipping
        """

        self._shipping = shipping

    @property
    def summary(self):
        """Gets the summary of this Order.  # noqa: E501


        :return: The summary of this Order.  # noqa: E501
        :rtype: OrderSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Order.


        :param summary: The summary of this Order.  # noqa: E501
        :type: OrderSummary
        """

        self._summary = summary

    @property
    def tags(self):
        """Gets the tags of this Order.  # noqa: E501

        tags, available only through update, not through insert due to the nature of how tags are handled internally  # noqa: E501

        :return: The tags of this Order.  # noqa: E501
        :rtype: list[OrderTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Order.

        tags, available only through update, not through insert due to the nature of how tags are handled internally  # noqa: E501

        :param tags: The tags of this Order.  # noqa: E501
        :type: list[OrderTag]
        """

        self._tags = tags

    @property
    def taxes(self):
        """Gets the taxes of this Order.  # noqa: E501


        :return: The taxes of this Order.  # noqa: E501
        :rtype: OrderTaxes
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this Order.


        :param taxes: The taxes of this Order.  # noqa: E501
        :type: OrderTaxes
        """

        self._taxes = taxes

    @property
    def utms(self):
        """Gets the utms of this Order.  # noqa: E501

        UTM clicks.  The zero index is the most recent (last) UTM click  # noqa: E501

        :return: The utms of this Order.  # noqa: E501
        :rtype: list[OrderUtm]
        """
        return self._utms

    @utms.setter
    def utms(self, utms):
        """Sets the utms of this Order.

        UTM clicks.  The zero index is the most recent (last) UTM click  # noqa: E501

        :param utms: The utms of this Order.  # noqa: E501
        :type: list[OrderUtm]
        """

        self._utms = utms

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
