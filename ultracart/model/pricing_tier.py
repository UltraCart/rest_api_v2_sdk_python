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
    from ultracart.model.pricing_tier_notification import PricingTierNotification
    globals()['PricingTierNotification'] = PricingTierNotification


class PricingTier(ModelNormal):
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
        ('name',): {
            'max_length': 50,
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
            'allow_3rd_party_billing': (bool,),  # noqa: E501
            'allow_cod': (bool,),  # noqa: E501
            'allow_purchase_order': (bool,),  # noqa: E501
            'allow_quote_request': (bool,),  # noqa: E501
            'approval_notification': (PricingTierNotification,),  # noqa: E501
            'auto_approve_cod': (bool,),  # noqa: E501
            'auto_approve_purchase_order': (bool,),  # noqa: E501
            'currency_code': (str,),  # noqa: E501
            'default_on_wholesale_signup': (bool,),  # noqa: E501
            'default_percentage_discount': (float,),  # noqa: E501
            'default_shipping_method_oid': (int,),  # noqa: E501
            'default_tier': (bool,),  # noqa: E501
            'display_on_wholesale_signup': (bool,),  # noqa: E501
            'exclude_from_free_promotion': (bool,),  # noqa: E501
            'exempt_loyalty_rewards': (bool,),  # noqa: E501
            'exempt_shipping_handling_charge': (bool,),  # noqa: E501
            'free_shipping': (bool,),  # noqa: E501
            'free_shipping_minimum': (float,),  # noqa: E501
            'maximum_item_count': (int,),  # noqa: E501
            'minimum_item_count': (int,),  # noqa: E501
            'minimum_subtotal': (float,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'no_coupons': (bool,),  # noqa: E501
            'no_free_shipping': (bool,),  # noqa: E501
            'no_realtime_charge': (bool,),  # noqa: E501
            'not_valid_when_coupon_present': (bool,),  # noqa: E501
            'pricing_tier_oid': (int,),  # noqa: E501
            'realtime_percentage_discount': (float,),  # noqa: E501
            'restrict_to_distribution_center_oid': (int,),  # noqa: E501
            'signup_notification': (PricingTierNotification,),  # noqa: E501
            'suppress_buysafe': (bool,),  # noqa: E501
            'suppress_mailing_list': (bool,),  # noqa: E501
            'tax_exempt': (bool,),  # noqa: E501
            'track_separately': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'allow_3rd_party_billing': 'allow_3rd_party_billing',  # noqa: E501
        'allow_cod': 'allow_cod',  # noqa: E501
        'allow_purchase_order': 'allow_purchase_order',  # noqa: E501
        'allow_quote_request': 'allow_quote_request',  # noqa: E501
        'approval_notification': 'approval_notification',  # noqa: E501
        'auto_approve_cod': 'auto_approve_cod',  # noqa: E501
        'auto_approve_purchase_order': 'auto_approve_purchase_order',  # noqa: E501
        'currency_code': 'currency_code',  # noqa: E501
        'default_on_wholesale_signup': 'default_on_wholesale_signup',  # noqa: E501
        'default_percentage_discount': 'default_percentage_discount',  # noqa: E501
        'default_shipping_method_oid': 'default_shipping_method_oid',  # noqa: E501
        'default_tier': 'default_tier',  # noqa: E501
        'display_on_wholesale_signup': 'display_on_wholesale_signup',  # noqa: E501
        'exclude_from_free_promotion': 'exclude_from_free_promotion',  # noqa: E501
        'exempt_loyalty_rewards': 'exempt_loyalty_rewards',  # noqa: E501
        'exempt_shipping_handling_charge': 'exempt_shipping_handling_charge',  # noqa: E501
        'free_shipping': 'free_shipping',  # noqa: E501
        'free_shipping_minimum': 'free_shipping_minimum',  # noqa: E501
        'maximum_item_count': 'maximum_item_count',  # noqa: E501
        'minimum_item_count': 'minimum_item_count',  # noqa: E501
        'minimum_subtotal': 'minimum_subtotal',  # noqa: E501
        'name': 'name',  # noqa: E501
        'no_coupons': 'no_coupons',  # noqa: E501
        'no_free_shipping': 'no_free_shipping',  # noqa: E501
        'no_realtime_charge': 'no_realtime_charge',  # noqa: E501
        'not_valid_when_coupon_present': 'not_valid_when_coupon_present',  # noqa: E501
        'pricing_tier_oid': 'pricing_tier_oid',  # noqa: E501
        'realtime_percentage_discount': 'realtime_percentage_discount',  # noqa: E501
        'restrict_to_distribution_center_oid': 'restrict_to_distribution_center_oid',  # noqa: E501
        'signup_notification': 'signup_notification',  # noqa: E501
        'suppress_buysafe': 'suppress_buysafe',  # noqa: E501
        'suppress_mailing_list': 'suppress_mailing_list',  # noqa: E501
        'tax_exempt': 'tax_exempt',  # noqa: E501
        'track_separately': 'track_separately',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """PricingTier - a model defined in OpenAPI

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
            allow_3rd_party_billing (bool): Allow 3rd party billing. [optional]  # noqa: E501
            allow_cod (bool): Allow COD. [optional]  # noqa: E501
            allow_purchase_order (bool): Allow purchase order. [optional]  # noqa: E501
            allow_quote_request (bool): Allow quote request. [optional]  # noqa: E501
            approval_notification (PricingTierNotification): [optional]  # noqa: E501
            auto_approve_cod (bool): Auto approve COD. [optional]  # noqa: E501
            auto_approve_purchase_order (bool): Auto approve purchase order. [optional]  # noqa: E501
            currency_code (str): Any currency code specified on this pricing tier will force a shopping cart into that currency. [optional]  # noqa: E501
            default_on_wholesale_signup (bool): Default on wholesale signup. [optional]  # noqa: E501
            default_percentage_discount (float): Default percentage discount. [optional]  # noqa: E501
            default_shipping_method_oid (int): Default shipping method oid. [optional]  # noqa: E501
            default_tier (bool): Default tier. [optional]  # noqa: E501
            display_on_wholesale_signup (bool): Display on wholesale signup. [optional]  # noqa: E501
            exclude_from_free_promotion (bool): Exclude from free promotion. [optional]  # noqa: E501
            exempt_loyalty_rewards (bool): Exempt from Loyalty Rewards. [optional]  # noqa: E501
            exempt_shipping_handling_charge (bool): Exempt shipping handling charge. [optional]  # noqa: E501
            free_shipping (bool): Free shipping. [optional]  # noqa: E501
            free_shipping_minimum (float): Free shipping minimum. [optional]  # noqa: E501
            maximum_item_count (int): Maximum item count. [optional]  # noqa: E501
            minimum_item_count (int): Minimum item count. [optional]  # noqa: E501
            minimum_subtotal (float): Minimum subtotal. [optional]  # noqa: E501
            name (str): Name. [optional]  # noqa: E501
            no_coupons (bool): No coupons. [optional]  # noqa: E501
            no_free_shipping (bool): No free shipping. [optional]  # noqa: E501
            no_realtime_charge (bool): No realtime charge. [optional]  # noqa: E501
            not_valid_when_coupon_present (bool): Not valid when coupon present. [optional]  # noqa: E501
            pricing_tier_oid (int): Pricing Tier Oid. [optional]  # noqa: E501
            realtime_percentage_discount (float): Realtime percentage discount. [optional]  # noqa: E501
            restrict_to_distribution_center_oid (int): Restrict inventory to this distribution center oid. [optional]  # noqa: E501
            signup_notification (PricingTierNotification): [optional]  # noqa: E501
            suppress_buysafe (bool): Suppress buySAFE (deprecated). [optional]  # noqa: E501
            suppress_mailing_list (bool): Suppress mailing list. [optional]  # noqa: E501
            tax_exempt (bool): Tax Exempt. [optional]  # noqa: E501
            track_separately (bool): Track separately. [optional]  # noqa: E501
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
        """PricingTier - a model defined in OpenAPI

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
            allow_3rd_party_billing (bool): Allow 3rd party billing. [optional]  # noqa: E501
            allow_cod (bool): Allow COD. [optional]  # noqa: E501
            allow_purchase_order (bool): Allow purchase order. [optional]  # noqa: E501
            allow_quote_request (bool): Allow quote request. [optional]  # noqa: E501
            approval_notification (PricingTierNotification): [optional]  # noqa: E501
            auto_approve_cod (bool): Auto approve COD. [optional]  # noqa: E501
            auto_approve_purchase_order (bool): Auto approve purchase order. [optional]  # noqa: E501
            currency_code (str): Any currency code specified on this pricing tier will force a shopping cart into that currency. [optional]  # noqa: E501
            default_on_wholesale_signup (bool): Default on wholesale signup. [optional]  # noqa: E501
            default_percentage_discount (float): Default percentage discount. [optional]  # noqa: E501
            default_shipping_method_oid (int): Default shipping method oid. [optional]  # noqa: E501
            default_tier (bool): Default tier. [optional]  # noqa: E501
            display_on_wholesale_signup (bool): Display on wholesale signup. [optional]  # noqa: E501
            exclude_from_free_promotion (bool): Exclude from free promotion. [optional]  # noqa: E501
            exempt_loyalty_rewards (bool): Exempt from Loyalty Rewards. [optional]  # noqa: E501
            exempt_shipping_handling_charge (bool): Exempt shipping handling charge. [optional]  # noqa: E501
            free_shipping (bool): Free shipping. [optional]  # noqa: E501
            free_shipping_minimum (float): Free shipping minimum. [optional]  # noqa: E501
            maximum_item_count (int): Maximum item count. [optional]  # noqa: E501
            minimum_item_count (int): Minimum item count. [optional]  # noqa: E501
            minimum_subtotal (float): Minimum subtotal. [optional]  # noqa: E501
            name (str): Name. [optional]  # noqa: E501
            no_coupons (bool): No coupons. [optional]  # noqa: E501
            no_free_shipping (bool): No free shipping. [optional]  # noqa: E501
            no_realtime_charge (bool): No realtime charge. [optional]  # noqa: E501
            not_valid_when_coupon_present (bool): Not valid when coupon present. [optional]  # noqa: E501
            pricing_tier_oid (int): Pricing Tier Oid. [optional]  # noqa: E501
            realtime_percentage_discount (float): Realtime percentage discount. [optional]  # noqa: E501
            restrict_to_distribution_center_oid (int): Restrict inventory to this distribution center oid. [optional]  # noqa: E501
            signup_notification (PricingTierNotification): [optional]  # noqa: E501
            suppress_buysafe (bool): Suppress buySAFE (deprecated). [optional]  # noqa: E501
            suppress_mailing_list (bool): Suppress mailing list. [optional]  # noqa: E501
            tax_exempt (bool): Tax Exempt. [optional]  # noqa: E501
            track_separately (bool): Track separately. [optional]  # noqa: E501
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
