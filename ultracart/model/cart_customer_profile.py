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
    from ultracart.model.cart_customer_profile_address import CartCustomerProfileAddress
    from ultracart.model.cart_customer_profile_credit_card import CartCustomerProfileCreditCard
    globals()['CartCustomerProfileAddress'] = CartCustomerProfileAddress
    globals()['CartCustomerProfileCreditCard'] = CartCustomerProfileCreditCard


class CartCustomerProfile(ModelNormal):
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
            'billing_addresses': ([CartCustomerProfileAddress],),  # noqa: E501
            'credit_cards': ([CartCustomerProfileCreditCard],),  # noqa: E501
            'customer_profile_oid': (int,),  # noqa: E501
            'dhl_account_number': (str,),  # noqa: E501
            'dhl_duty_account_number': (str,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'fedex_account_number': (str,),  # noqa: E501
            'free_shipping': (bool,),  # noqa: E501
            'free_shipping_minimum': (float,),  # noqa: E501
            'maximum_item_count': (int,),  # noqa: E501
            'minimum_item_count': (int,),  # noqa: E501
            'minimum_subtotal': (float,),  # noqa: E501
            'no_coupons': (bool,),  # noqa: E501
            'no_free_shipping': (bool,),  # noqa: E501
            'no_realtime_charge': (bool,),  # noqa: E501
            'pricing_tiers': ([str],),  # noqa: E501
            'shipping_addresses': ([CartCustomerProfileAddress],),  # noqa: E501
            'tax_exempt': (bool,),  # noqa: E501
            'ups_account_number': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'allow_3rd_party_billing': 'allow_3rd_party_billing',  # noqa: E501
        'allow_cod': 'allow_cod',  # noqa: E501
        'allow_purchase_order': 'allow_purchase_order',  # noqa: E501
        'billing_addresses': 'billing_addresses',  # noqa: E501
        'credit_cards': 'credit_cards',  # noqa: E501
        'customer_profile_oid': 'customer_profile_oid',  # noqa: E501
        'dhl_account_number': 'dhl_account_number',  # noqa: E501
        'dhl_duty_account_number': 'dhl_duty_account_number',  # noqa: E501
        'email': 'email',  # noqa: E501
        'fedex_account_number': 'fedex_account_number',  # noqa: E501
        'free_shipping': 'free_shipping',  # noqa: E501
        'free_shipping_minimum': 'free_shipping_minimum',  # noqa: E501
        'maximum_item_count': 'maximum_item_count',  # noqa: E501
        'minimum_item_count': 'minimum_item_count',  # noqa: E501
        'minimum_subtotal': 'minimum_subtotal',  # noqa: E501
        'no_coupons': 'no_coupons',  # noqa: E501
        'no_free_shipping': 'no_free_shipping',  # noqa: E501
        'no_realtime_charge': 'no_realtime_charge',  # noqa: E501
        'pricing_tiers': 'pricing_tiers',  # noqa: E501
        'shipping_addresses': 'shipping_addresses',  # noqa: E501
        'tax_exempt': 'tax_exempt',  # noqa: E501
        'ups_account_number': 'ups_account_number',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """CartCustomerProfile - a model defined in OpenAPI

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
            allow_3rd_party_billing (bool): True if profile is allowed to bill to their 3rd party shipping account. [optional]  # noqa: E501
            allow_cod (bool): True if this profile is allowed to use a COD. [optional]  # noqa: E501
            allow_purchase_order (bool): True if this profile is allowed to use a purchase order. [optional]  # noqa: E501
            billing_addresses ([CartCustomerProfileAddress]): Billing addresses on file for this profile. [optional]  # noqa: E501
            credit_cards ([CartCustomerProfileCreditCard]): Credit cards on file for this profile (masked). [optional]  # noqa: E501
            customer_profile_oid (int): Unique identifier. [optional]  # noqa: E501
            dhl_account_number (str): DHL account number on file. [optional]  # noqa: E501
            dhl_duty_account_number (str): DHL duty account number on file. [optional]  # noqa: E501
            email (str): Email. [optional]  # noqa: E501
            fedex_account_number (str): FedEx account number on file. [optional]  # noqa: E501
            free_shipping (bool): True if this profile always qualifies for free shipping. [optional]  # noqa: E501
            free_shipping_minimum (float): The minimum aount that this profile has to purchase to qualify for free shipping. [optional]  # noqa: E501
            maximum_item_count (int): Maximum item count this profile can purchase. [optional]  # noqa: E501
            minimum_item_count (int): Minimum item count this profile must purchase. [optional]  # noqa: E501
            minimum_subtotal (float): Minimum subtotal this profile must purchase. [optional]  # noqa: E501
            no_coupons (bool): True if this profile is prevented from using coupons. [optional]  # noqa: E501
            no_free_shipping (bool): True if this profile is never given free shipping. [optional]  # noqa: E501
            no_realtime_charge (bool): True if this customers orders are not charged in real-time. [optional]  # noqa: E501
            pricing_tiers ([str]): Pricing tier names this profile qualifies for. [optional]  # noqa: E501
            shipping_addresses ([CartCustomerProfileAddress]): Shipping addresses on file for this profile. [optional]  # noqa: E501
            tax_exempt (bool): True if this profile is exempt from sales tax. [optional]  # noqa: E501
            ups_account_number (str): UPS account number on file. [optional]  # noqa: E501
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
        """CartCustomerProfile - a model defined in OpenAPI

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
            allow_3rd_party_billing (bool): True if profile is allowed to bill to their 3rd party shipping account. [optional]  # noqa: E501
            allow_cod (bool): True if this profile is allowed to use a COD. [optional]  # noqa: E501
            allow_purchase_order (bool): True if this profile is allowed to use a purchase order. [optional]  # noqa: E501
            billing_addresses ([CartCustomerProfileAddress]): Billing addresses on file for this profile. [optional]  # noqa: E501
            credit_cards ([CartCustomerProfileCreditCard]): Credit cards on file for this profile (masked). [optional]  # noqa: E501
            customer_profile_oid (int): Unique identifier. [optional]  # noqa: E501
            dhl_account_number (str): DHL account number on file. [optional]  # noqa: E501
            dhl_duty_account_number (str): DHL duty account number on file. [optional]  # noqa: E501
            email (str): Email. [optional]  # noqa: E501
            fedex_account_number (str): FedEx account number on file. [optional]  # noqa: E501
            free_shipping (bool): True if this profile always qualifies for free shipping. [optional]  # noqa: E501
            free_shipping_minimum (float): The minimum aount that this profile has to purchase to qualify for free shipping. [optional]  # noqa: E501
            maximum_item_count (int): Maximum item count this profile can purchase. [optional]  # noqa: E501
            minimum_item_count (int): Minimum item count this profile must purchase. [optional]  # noqa: E501
            minimum_subtotal (float): Minimum subtotal this profile must purchase. [optional]  # noqa: E501
            no_coupons (bool): True if this profile is prevented from using coupons. [optional]  # noqa: E501
            no_free_shipping (bool): True if this profile is never given free shipping. [optional]  # noqa: E501
            no_realtime_charge (bool): True if this customers orders are not charged in real-time. [optional]  # noqa: E501
            pricing_tiers ([str]): Pricing tier names this profile qualifies for. [optional]  # noqa: E501
            shipping_addresses ([CartCustomerProfileAddress]): Shipping addresses on file for this profile. [optional]  # noqa: E501
            tax_exempt (bool): True if this profile is exempt from sales tax. [optional]  # noqa: E501
            ups_account_number (str): UPS account number on file. [optional]  # noqa: E501
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