"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ultracart.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from ultracart.exceptions import ApiAttributeError


def lazy_import():
    from ultracart.model.customer_activity import CustomerActivity
    from ultracart.model.customer_attachment import CustomerAttachment
    from ultracart.model.customer_billing import CustomerBilling
    from ultracart.model.customer_card import CustomerCard
    from ultracart.model.customer_edi import CustomerEDI
    from ultracart.model.customer_email import CustomerEmail
    from ultracart.model.customer_loyalty import CustomerLoyalty
    from ultracart.model.customer_orders_summary import CustomerOrdersSummary
    from ultracart.model.customer_pricing_tier import CustomerPricingTier
    from ultracart.model.customer_privacy import CustomerPrivacy
    from ultracart.model.customer_property import CustomerProperty
    from ultracart.model.customer_quotes_summary import CustomerQuotesSummary
    from ultracart.model.customer_reviewer import CustomerReviewer
    from ultracart.model.customer_shipping import CustomerShipping
    from ultracart.model.customer_software_entitlement import CustomerSoftwareEntitlement
    from ultracart.model.customer_tag import CustomerTag
    from ultracart.model.customer_tax_codes import CustomerTaxCodes
    from ultracart.model.order import Order
    globals()['CustomerActivity'] = CustomerActivity
    globals()['CustomerAttachment'] = CustomerAttachment
    globals()['CustomerBilling'] = CustomerBilling
    globals()['CustomerCard'] = CustomerCard
    globals()['CustomerEDI'] = CustomerEDI
    globals()['CustomerEmail'] = CustomerEmail
    globals()['CustomerLoyalty'] = CustomerLoyalty
    globals()['CustomerOrdersSummary'] = CustomerOrdersSummary
    globals()['CustomerPricingTier'] = CustomerPricingTier
    globals()['CustomerPrivacy'] = CustomerPrivacy
    globals()['CustomerProperty'] = CustomerProperty
    globals()['CustomerQuotesSummary'] = CustomerQuotesSummary
    globals()['CustomerReviewer'] = CustomerReviewer
    globals()['CustomerShipping'] = CustomerShipping
    globals()['CustomerSoftwareEntitlement'] = CustomerSoftwareEntitlement
    globals()['CustomerTag'] = CustomerTag
    globals()['CustomerTaxCodes'] = CustomerTaxCodes
    globals()['Order'] = Order


class Customer(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('business_notes',): {
            'max_length': 2000,
        },
        ('dhl_account_number',): {
            'max_length': 20,
        },
        ('dhl_duty_account_number',): {
            'max_length': 20,
        },
        ('fedex_account_number',): {
            'max_length': 20,
        },
        ('last_modified_by',): {
            'max_length': 100,
        },
        ('password',): {
            'max_length': 30,
        },
        ('referral_source',): {
            'max_length': 50,
        },
        ('sales_rep_code',): {
            'max_length': 10,
        },
        ('tax_id',): {
            'max_length': 15,
        },
        ('ups_account_number',): {
            'max_length': 20,
        },
        ('website_url',): {
            'max_length': 100,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'activity': (CustomerActivity,),  # noqa: E501
            'affiliate_oid': (int,),  # noqa: E501
            'allow_3rd_party_billing': (bool,),  # noqa: E501
            'allow_cod': (bool,),  # noqa: E501
            'allow_drop_shipping': (bool,),  # noqa: E501
            'allow_purchase_order': (bool,),  # noqa: E501
            'allow_quote_request': (bool,),  # noqa: E501
            'allow_selection_of_address_type': (bool,),  # noqa: E501
            'attachments': ([CustomerAttachment],),  # noqa: E501
            'auto_approve_cod': (bool,),  # noqa: E501
            'auto_approve_purchase_order': (bool,),  # noqa: E501
            'automatic_merchant_notes': (str,),  # noqa: E501
            'billing': ([CustomerBilling],),  # noqa: E501
            'business_notes': (str,),  # noqa: E501
            'cards': ([CustomerCard],),  # noqa: E501
            'cc_emails': ([CustomerEmail],),  # noqa: E501
            'customer_profile_oid': (int,),  # noqa: E501
            'dhl_account_number': (str,),  # noqa: E501
            'dhl_duty_account_number': (str,),  # noqa: E501
            'do_not_send_mail': (bool,),  # noqa: E501
            'edi': (CustomerEDI,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'exempt_shipping_handling_charge': (bool,),  # noqa: E501
            'fedex_account_number': (str,),  # noqa: E501
            'free_shipping': (bool,),  # noqa: E501
            'free_shipping_minimum': (float,),  # noqa: E501
            'last_modified_by': (str,),  # noqa: E501
            'last_modified_dts': (str,),  # noqa: E501
            'loyalty': (CustomerLoyalty,),  # noqa: E501
            'maximum_item_count': (int,),  # noqa: E501
            'merchant_id': (str,),  # noqa: E501
            'minimum_item_count': (int,),  # noqa: E501
            'minimum_subtotal': (float,),  # noqa: E501
            'no_coupons': (bool,),  # noqa: E501
            'no_free_shipping': (bool,),  # noqa: E501
            'no_realtime_charge': (bool,),  # noqa: E501
            'orders': ([Order],),  # noqa: E501
            'orders_summary': (CustomerOrdersSummary,),  # noqa: E501
            'password': (str,),  # noqa: E501
            'pricing_tiers': ([CustomerPricingTier],),  # noqa: E501
            'privacy': (CustomerPrivacy,),  # noqa: E501
            'properties': ([CustomerProperty],),  # noqa: E501
            'qb_class': (str,),  # noqa: E501
            'qb_code': (str,),  # noqa: E501
            'qb_tax_exemption_reason_code': (int,),  # noqa: E501
            'quotes': ([Order],),  # noqa: E501
            'quotes_summary': (CustomerQuotesSummary,),  # noqa: E501
            'referral_source': (str,),  # noqa: E501
            'reviewer': (CustomerReviewer,),  # noqa: E501
            'sales_rep_code': (str,),  # noqa: E501
            'send_signup_notification': (bool,),  # noqa: E501
            'shipping': ([CustomerShipping],),  # noqa: E501
            'signup_dts': (str,),  # noqa: E501
            'software_entitlements': ([CustomerSoftwareEntitlement],),  # noqa: E501
            'suppress_buysafe': (bool,),  # noqa: E501
            'tags': ([CustomerTag],),  # noqa: E501
            'tax_codes': (CustomerTaxCodes,),  # noqa: E501
            'tax_exempt': (bool,),  # noqa: E501
            'tax_id': (str,),  # noqa: E501
            'terms': (str,),  # noqa: E501
            'track_separately': (bool,),  # noqa: E501
            'unapproved': (bool,),  # noqa: E501
            'ups_account_number': (str,),  # noqa: E501
            'website_url': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'activity': 'activity',  # noqa: E501
        'affiliate_oid': 'affiliate_oid',  # noqa: E501
        'allow_3rd_party_billing': 'allow_3rd_party_billing',  # noqa: E501
        'allow_cod': 'allow_cod',  # noqa: E501
        'allow_drop_shipping': 'allow_drop_shipping',  # noqa: E501
        'allow_purchase_order': 'allow_purchase_order',  # noqa: E501
        'allow_quote_request': 'allow_quote_request',  # noqa: E501
        'allow_selection_of_address_type': 'allow_selection_of_address_type',  # noqa: E501
        'attachments': 'attachments',  # noqa: E501
        'auto_approve_cod': 'auto_approve_cod',  # noqa: E501
        'auto_approve_purchase_order': 'auto_approve_purchase_order',  # noqa: E501
        'automatic_merchant_notes': 'automatic_merchant_notes',  # noqa: E501
        'billing': 'billing',  # noqa: E501
        'business_notes': 'business_notes',  # noqa: E501
        'cards': 'cards',  # noqa: E501
        'cc_emails': 'cc_emails',  # noqa: E501
        'customer_profile_oid': 'customer_profile_oid',  # noqa: E501
        'dhl_account_number': 'dhl_account_number',  # noqa: E501
        'dhl_duty_account_number': 'dhl_duty_account_number',  # noqa: E501
        'do_not_send_mail': 'do_not_send_mail',  # noqa: E501
        'edi': 'edi',  # noqa: E501
        'email': 'email',  # noqa: E501
        'exempt_shipping_handling_charge': 'exempt_shipping_handling_charge',  # noqa: E501
        'fedex_account_number': 'fedex_account_number',  # noqa: E501
        'free_shipping': 'free_shipping',  # noqa: E501
        'free_shipping_minimum': 'free_shipping_minimum',  # noqa: E501
        'last_modified_by': 'last_modified_by',  # noqa: E501
        'last_modified_dts': 'last_modified_dts',  # noqa: E501
        'loyalty': 'loyalty',  # noqa: E501
        'maximum_item_count': 'maximum_item_count',  # noqa: E501
        'merchant_id': 'merchant_id',  # noqa: E501
        'minimum_item_count': 'minimum_item_count',  # noqa: E501
        'minimum_subtotal': 'minimum_subtotal',  # noqa: E501
        'no_coupons': 'no_coupons',  # noqa: E501
        'no_free_shipping': 'no_free_shipping',  # noqa: E501
        'no_realtime_charge': 'no_realtime_charge',  # noqa: E501
        'orders': 'orders',  # noqa: E501
        'orders_summary': 'orders_summary',  # noqa: E501
        'password': 'password',  # noqa: E501
        'pricing_tiers': 'pricing_tiers',  # noqa: E501
        'privacy': 'privacy',  # noqa: E501
        'properties': 'properties',  # noqa: E501
        'qb_class': 'qb_class',  # noqa: E501
        'qb_code': 'qb_code',  # noqa: E501
        'qb_tax_exemption_reason_code': 'qb_tax_exemption_reason_code',  # noqa: E501
        'quotes': 'quotes',  # noqa: E501
        'quotes_summary': 'quotes_summary',  # noqa: E501
        'referral_source': 'referral_source',  # noqa: E501
        'reviewer': 'reviewer',  # noqa: E501
        'sales_rep_code': 'sales_rep_code',  # noqa: E501
        'send_signup_notification': 'send_signup_notification',  # noqa: E501
        'shipping': 'shipping',  # noqa: E501
        'signup_dts': 'signup_dts',  # noqa: E501
        'software_entitlements': 'software_entitlements',  # noqa: E501
        'suppress_buysafe': 'suppress_buysafe',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'tax_codes': 'tax_codes',  # noqa: E501
        'tax_exempt': 'tax_exempt',  # noqa: E501
        'tax_id': 'tax_id',  # noqa: E501
        'terms': 'terms',  # noqa: E501
        'track_separately': 'track_separately',  # noqa: E501
        'unapproved': 'unapproved',  # noqa: E501
        'ups_account_number': 'ups_account_number',  # noqa: E501
        'website_url': 'website_url',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Customer - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            activity (CustomerActivity): [optional]  # noqa: E501
            affiliate_oid (int): Affiliate oid. [optional]  # noqa: E501
            allow_3rd_party_billing (bool): Allow 3rd party billing. [optional]  # noqa: E501
            allow_cod (bool): Allow COD. [optional]  # noqa: E501
            allow_drop_shipping (bool): Allow Drop Shipping. [optional]  # noqa: E501
            allow_purchase_order (bool): Allow purchase orders by this customer. [optional]  # noqa: E501
            allow_quote_request (bool): Allow quote request. [optional]  # noqa: E501
            allow_selection_of_address_type (bool): Allow selection of residential or business address type. [optional]  # noqa: E501
            attachments ([CustomerAttachment]): Attachments. [optional]  # noqa: E501
            auto_approve_cod (bool): Auto approve COD. [optional]  # noqa: E501
            auto_approve_purchase_order (bool): Auto approve purchase orders by this customer. [optional]  # noqa: E501
            automatic_merchant_notes (str): Automatic merchant notes are added to every order placed. [optional]  # noqa: E501
            billing ([CustomerBilling]): Billing addresses for this customer. [optional]  # noqa: E501
            business_notes (str): Business notes (internally visible only). [optional]  # noqa: E501
            cards ([CustomerCard]): Credit Cards for this customer. [optional]  # noqa: E501
            cc_emails ([CustomerEmail]): Additional emails to CC notification. [optional]  # noqa: E501
            customer_profile_oid (int): Customer profile object identifier. [optional]  # noqa: E501
            dhl_account_number (str): DHL account number. [optional]  # noqa: E501
            dhl_duty_account_number (str): DHL duty account number. [optional]  # noqa: E501
            do_not_send_mail (bool): Do not send mail (null will not update). [optional]  # noqa: E501
            edi (CustomerEDI): [optional]  # noqa: E501
            email (str): Email address of this customer profile. [optional]  # noqa: E501
            exempt_shipping_handling_charge (bool): Exempt shipping handling charge. [optional]  # noqa: E501
            fedex_account_number (str): FedEx account number. [optional]  # noqa: E501
            free_shipping (bool): This customer always receives free shipping. [optional]  # noqa: E501
            free_shipping_minimum (float): If free_shipping is true, this is the minimum subtotal required for free shipping. [optional]  # noqa: E501
            last_modified_by (str): Last modified by. [optional]  # noqa: E501
            last_modified_dts (str): Last modified date. [optional]  # noqa: E501
            loyalty (CustomerLoyalty): [optional]  # noqa: E501
            maximum_item_count (int): Maximum item count. [optional]  # noqa: E501
            merchant_id (str): Merchant ID. [optional]  # noqa: E501
            minimum_item_count (int): Minimum item count. [optional]  # noqa: E501
            minimum_subtotal (float): Minimum subtotal. [optional]  # noqa: E501
            no_coupons (bool): No coupons. [optional]  # noqa: E501
            no_free_shipping (bool): No free shipping regardless of coupons or item level settings. [optional]  # noqa: E501
            no_realtime_charge (bool): No realtime charge. [optional]  # noqa: E501
            orders ([Order]): Orders associated with this customer profile. [optional]  # noqa: E501
            orders_summary (CustomerOrdersSummary): [optional]  # noqa: E501
            password (str): Password (may only be set, never read). [optional]  # noqa: E501
            pricing_tiers ([CustomerPricingTier]): Pricing tiers for this customer. [optional]  # noqa: E501
            privacy (CustomerPrivacy): [optional]  # noqa: E501
            properties ([CustomerProperty]): Properties for this customer. [optional]  # noqa: E501
            qb_class (str): QuickBooks class to import this customer as. [optional]  # noqa: E501
            qb_code (str): QuickBooks name to import this customer as. [optional]  # noqa: E501
            qb_tax_exemption_reason_code (int): QuickBooks tax exemption reason code. [optional]  # noqa: E501
            quotes ([Order]): Quotes associated with this customer profile. [optional]  # noqa: E501
            quotes_summary (CustomerQuotesSummary): [optional]  # noqa: E501
            referral_source (str): Referral Source. [optional]  # noqa: E501
            reviewer (CustomerReviewer): [optional]  # noqa: E501
            sales_rep_code (str): Sales rep code. [optional]  # noqa: E501
            send_signup_notification (bool): Send signup notification, if true during customer creation, will send a notification.. [optional]  # noqa: E501
            shipping ([CustomerShipping]): Shipping addresses for this customer. [optional]  # noqa: E501
            signup_dts (str): Signup date. [optional]  # noqa: E501
            software_entitlements ([CustomerSoftwareEntitlement]): Software entitlements owned by this customer. [optional]  # noqa: E501
            suppress_buysafe (bool): Suppress buySAFE (deprecated). [optional]  # noqa: E501
            tags ([CustomerTag]): Tags for this customer. [optional]  # noqa: E501
            tax_codes (CustomerTaxCodes): [optional]  # noqa: E501
            tax_exempt (bool): True if the customer is tax exempt. [optional]  # noqa: E501
            tax_id (str): Tax ID. [optional]  # noqa: E501
            terms (str): Terms for this customer. [optional]  # noqa: E501
            track_separately (bool): True if the customer should be tracked separately in QuickBooks. [optional]  # noqa: E501
            unapproved (bool): Unapproved. [optional]  # noqa: E501
            ups_account_number (str): UPS account number. [optional]  # noqa: E501
            website_url (str): Website url. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Customer - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            activity (CustomerActivity): [optional]  # noqa: E501
            affiliate_oid (int): Affiliate oid. [optional]  # noqa: E501
            allow_3rd_party_billing (bool): Allow 3rd party billing. [optional]  # noqa: E501
            allow_cod (bool): Allow COD. [optional]  # noqa: E501
            allow_drop_shipping (bool): Allow Drop Shipping. [optional]  # noqa: E501
            allow_purchase_order (bool): Allow purchase orders by this customer. [optional]  # noqa: E501
            allow_quote_request (bool): Allow quote request. [optional]  # noqa: E501
            allow_selection_of_address_type (bool): Allow selection of residential or business address type. [optional]  # noqa: E501
            attachments ([CustomerAttachment]): Attachments. [optional]  # noqa: E501
            auto_approve_cod (bool): Auto approve COD. [optional]  # noqa: E501
            auto_approve_purchase_order (bool): Auto approve purchase orders by this customer. [optional]  # noqa: E501
            automatic_merchant_notes (str): Automatic merchant notes are added to every order placed. [optional]  # noqa: E501
            billing ([CustomerBilling]): Billing addresses for this customer. [optional]  # noqa: E501
            business_notes (str): Business notes (internally visible only). [optional]  # noqa: E501
            cards ([CustomerCard]): Credit Cards for this customer. [optional]  # noqa: E501
            cc_emails ([CustomerEmail]): Additional emails to CC notification. [optional]  # noqa: E501
            customer_profile_oid (int): Customer profile object identifier. [optional]  # noqa: E501
            dhl_account_number (str): DHL account number. [optional]  # noqa: E501
            dhl_duty_account_number (str): DHL duty account number. [optional]  # noqa: E501
            do_not_send_mail (bool): Do not send mail (null will not update). [optional]  # noqa: E501
            edi (CustomerEDI): [optional]  # noqa: E501
            email (str): Email address of this customer profile. [optional]  # noqa: E501
            exempt_shipping_handling_charge (bool): Exempt shipping handling charge. [optional]  # noqa: E501
            fedex_account_number (str): FedEx account number. [optional]  # noqa: E501
            free_shipping (bool): This customer always receives free shipping. [optional]  # noqa: E501
            free_shipping_minimum (float): If free_shipping is true, this is the minimum subtotal required for free shipping. [optional]  # noqa: E501
            last_modified_by (str): Last modified by. [optional]  # noqa: E501
            last_modified_dts (str): Last modified date. [optional]  # noqa: E501
            loyalty (CustomerLoyalty): [optional]  # noqa: E501
            maximum_item_count (int): Maximum item count. [optional]  # noqa: E501
            merchant_id (str): Merchant ID. [optional]  # noqa: E501
            minimum_item_count (int): Minimum item count. [optional]  # noqa: E501
            minimum_subtotal (float): Minimum subtotal. [optional]  # noqa: E501
            no_coupons (bool): No coupons. [optional]  # noqa: E501
            no_free_shipping (bool): No free shipping regardless of coupons or item level settings. [optional]  # noqa: E501
            no_realtime_charge (bool): No realtime charge. [optional]  # noqa: E501
            orders ([Order]): Orders associated with this customer profile. [optional]  # noqa: E501
            orders_summary (CustomerOrdersSummary): [optional]  # noqa: E501
            password (str): Password (may only be set, never read). [optional]  # noqa: E501
            pricing_tiers ([CustomerPricingTier]): Pricing tiers for this customer. [optional]  # noqa: E501
            privacy (CustomerPrivacy): [optional]  # noqa: E501
            properties ([CustomerProperty]): Properties for this customer. [optional]  # noqa: E501
            qb_class (str): QuickBooks class to import this customer as. [optional]  # noqa: E501
            qb_code (str): QuickBooks name to import this customer as. [optional]  # noqa: E501
            qb_tax_exemption_reason_code (int): QuickBooks tax exemption reason code. [optional]  # noqa: E501
            quotes ([Order]): Quotes associated with this customer profile. [optional]  # noqa: E501
            quotes_summary (CustomerQuotesSummary): [optional]  # noqa: E501
            referral_source (str): Referral Source. [optional]  # noqa: E501
            reviewer (CustomerReviewer): [optional]  # noqa: E501
            sales_rep_code (str): Sales rep code. [optional]  # noqa: E501
            send_signup_notification (bool): Send signup notification, if true during customer creation, will send a notification.. [optional]  # noqa: E501
            shipping ([CustomerShipping]): Shipping addresses for this customer. [optional]  # noqa: E501
            signup_dts (str): Signup date. [optional]  # noqa: E501
            software_entitlements ([CustomerSoftwareEntitlement]): Software entitlements owned by this customer. [optional]  # noqa: E501
            suppress_buysafe (bool): Suppress buySAFE (deprecated). [optional]  # noqa: E501
            tags ([CustomerTag]): Tags for this customer. [optional]  # noqa: E501
            tax_codes (CustomerTaxCodes): [optional]  # noqa: E501
            tax_exempt (bool): True if the customer is tax exempt. [optional]  # noqa: E501
            tax_id (str): Tax ID. [optional]  # noqa: E501
            terms (str): Terms for this customer. [optional]  # noqa: E501
            track_separately (bool): True if the customer should be tracked separately in QuickBooks. [optional]  # noqa: E501
            unapproved (bool): Unapproved. [optional]  # noqa: E501
            ups_account_number (str): UPS account number. [optional]  # noqa: E501
            website_url (str): Website url. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
