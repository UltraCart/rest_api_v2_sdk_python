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
    from ultracart.model.order_tracking_number_details import OrderTrackingNumberDetails
    from ultracart.model.weight import Weight
    globals()['OrderTrackingNumberDetails'] = OrderTrackingNumberDetails
    globals()['Weight'] = Weight


class OrderShipping(ModelNormal):
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
        ('address1',): {
            'max_length': 50,
        },
        ('address2',): {
            'max_length': 50,
        },
        ('city',): {
            'max_length': 32,
        },
        ('company',): {
            'max_length': 50,
        },
        ('country_code',): {
            'max_length': 2,
        },
        ('day_phone',): {
            'max_length': 25,
        },
        ('day_phone_e164',): {
            'max_length': 25,
        },
        ('evening_phone',): {
            'max_length': 25,
        },
        ('evening_phone_e164',): {
            'max_length': 25,
        },
        ('first_name',): {
            'max_length': 30,
        },
        ('last_name',): {
            'max_length': 30,
        },
        ('postal_code',): {
            'max_length': 20,
        },
        ('rma',): {
            'max_length': 30,
        },
        ('shipping_3rd_party_account_number',): {
            'max_length': 20,
        },
        ('shipping_department_status',): {
            'max_length': 30,
        },
        ('state_region',): {
            'max_length': 32,
        },
        ('title',): {
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
            'address1': (str,),  # noqa: E501
            'address2': (str,),  # noqa: E501
            'city': (str,),  # noqa: E501
            'company': (str,),  # noqa: E501
            'country_code': (str,),  # noqa: E501
            'day_phone': (str,),  # noqa: E501
            'day_phone_e164': (str,),  # noqa: E501
            'delivery_date': (str,),  # noqa: E501
            'evening_phone': (str,),  # noqa: E501
            'evening_phone_e164': (str,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'least_cost_route': (bool,),  # noqa: E501
            'least_cost_route_shipping_methods': ([str],),  # noqa: E501
            'lift_gate': (bool,),  # noqa: E501
            'postal_code': (str,),  # noqa: E501
            'rma': (str,),  # noqa: E501
            'ship_on_date': (str,),  # noqa: E501
            'ship_to_residential': (bool,),  # noqa: E501
            'shipping_3rd_party_account_number': (str,),  # noqa: E501
            'shipping_date': (str,),  # noqa: E501
            'shipping_department_status': (str,),  # noqa: E501
            'shipping_method': (str,),  # noqa: E501
            'shipping_method_accounting_code': (str,),  # noqa: E501
            'special_instructions': (str,),  # noqa: E501
            'state_region': (str,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'tracking_number_details': ([OrderTrackingNumberDetails],),  # noqa: E501
            'tracking_numbers': ([str],),  # noqa: E501
            'weight': (Weight,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'address1': 'address1',  # noqa: E501
        'address2': 'address2',  # noqa: E501
        'city': 'city',  # noqa: E501
        'company': 'company',  # noqa: E501
        'country_code': 'country_code',  # noqa: E501
        'day_phone': 'day_phone',  # noqa: E501
        'day_phone_e164': 'day_phone_e164',  # noqa: E501
        'delivery_date': 'delivery_date',  # noqa: E501
        'evening_phone': 'evening_phone',  # noqa: E501
        'evening_phone_e164': 'evening_phone_e164',  # noqa: E501
        'first_name': 'first_name',  # noqa: E501
        'last_name': 'last_name',  # noqa: E501
        'least_cost_route': 'least_cost_route',  # noqa: E501
        'least_cost_route_shipping_methods': 'least_cost_route_shipping_methods',  # noqa: E501
        'lift_gate': 'lift_gate',  # noqa: E501
        'postal_code': 'postal_code',  # noqa: E501
        'rma': 'rma',  # noqa: E501
        'ship_on_date': 'ship_on_date',  # noqa: E501
        'ship_to_residential': 'ship_to_residential',  # noqa: E501
        'shipping_3rd_party_account_number': 'shipping_3rd_party_account_number',  # noqa: E501
        'shipping_date': 'shipping_date',  # noqa: E501
        'shipping_department_status': 'shipping_department_status',  # noqa: E501
        'shipping_method': 'shipping_method',  # noqa: E501
        'shipping_method_accounting_code': 'shipping_method_accounting_code',  # noqa: E501
        'special_instructions': 'special_instructions',  # noqa: E501
        'state_region': 'state_region',  # noqa: E501
        'title': 'title',  # noqa: E501
        'tracking_number_details': 'tracking_number_details',  # noqa: E501
        'tracking_numbers': 'tracking_numbers',  # noqa: E501
        'weight': 'weight',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """OrderShipping - a model defined in OpenAPI

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
            address1 (str): Address line 1. [optional]  # noqa: E501
            address2 (str): Address line 2. [optional]  # noqa: E501
            city (str): City. [optional]  # noqa: E501
            company (str): Company. [optional]  # noqa: E501
            country_code (str): ISO-3166 two letter country code. [optional]  # noqa: E501
            day_phone (str): Day time phone. [optional]  # noqa: E501
            day_phone_e164 (str): Day time phone (E164 format). [optional]  # noqa: E501
            delivery_date (str): Date the customer is requesting delivery on.  Typically used for perishable product delivery.. [optional]  # noqa: E501
            evening_phone (str): Evening phone. [optional]  # noqa: E501
            evening_phone_e164 (str): Evening phone (E164 format). [optional]  # noqa: E501
            first_name (str): First name. [optional]  # noqa: E501
            last_name (str): Last name. [optional]  # noqa: E501
            least_cost_route (bool): If true, instructs UltraCart to apply the cheapest shipping method to this order.  Used only for channel partner order inserts.. [optional]  # noqa: E501
            least_cost_route_shipping_methods ([str]): List of shipping methods to consider if least_code_route is true. Used only for channel parter order inserts.. [optional]  # noqa: E501
            lift_gate (bool): Lift gate requested (LTL shipping methods only). [optional]  # noqa: E501
            postal_code (str): Postal code. [optional]  # noqa: E501
            rma (str): RMA number. [optional]  # noqa: E501
            ship_on_date (str): Date the customer is requesting that the order ship on.  Typically used for perishable product delivery.. [optional]  # noqa: E501
            ship_to_residential (bool): True if the shipping address is residential.  Effects the methods that are available to the customer as well as the price of the shipping method.. [optional]  # noqa: E501
            shipping_3rd_party_account_number (str): Shipping 3rd party account number. [optional]  # noqa: E501
            shipping_date (str): Date/time the order shipped on.  This date is set once the first shipment is sent to the customer.. [optional]  # noqa: E501
            shipping_department_status (str): Shipping department status. [optional]  # noqa: E501
            shipping_method (str): Shipping method. [optional]  # noqa: E501
            shipping_method_accounting_code (str): Shipping method accounting code. [optional]  # noqa: E501
            special_instructions (str): Special instructions from the customer regarding shipping. [optional]  # noqa: E501
            state_region (str): State. [optional]  # noqa: E501
            title (str): Title. [optional]  # noqa: E501
            tracking_number_details ([OrderTrackingNumberDetails]): Tracking number details. [optional]  # noqa: E501
            tracking_numbers ([str]): Tracking numbers. [optional]  # noqa: E501
            weight (Weight): [optional]  # noqa: E501
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
        """OrderShipping - a model defined in OpenAPI

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
            address1 (str): Address line 1. [optional]  # noqa: E501
            address2 (str): Address line 2. [optional]  # noqa: E501
            city (str): City. [optional]  # noqa: E501
            company (str): Company. [optional]  # noqa: E501
            country_code (str): ISO-3166 two letter country code. [optional]  # noqa: E501
            day_phone (str): Day time phone. [optional]  # noqa: E501
            day_phone_e164 (str): Day time phone (E164 format). [optional]  # noqa: E501
            delivery_date (str): Date the customer is requesting delivery on.  Typically used for perishable product delivery.. [optional]  # noqa: E501
            evening_phone (str): Evening phone. [optional]  # noqa: E501
            evening_phone_e164 (str): Evening phone (E164 format). [optional]  # noqa: E501
            first_name (str): First name. [optional]  # noqa: E501
            last_name (str): Last name. [optional]  # noqa: E501
            least_cost_route (bool): If true, instructs UltraCart to apply the cheapest shipping method to this order.  Used only for channel partner order inserts.. [optional]  # noqa: E501
            least_cost_route_shipping_methods ([str]): List of shipping methods to consider if least_code_route is true. Used only for channel parter order inserts.. [optional]  # noqa: E501
            lift_gate (bool): Lift gate requested (LTL shipping methods only). [optional]  # noqa: E501
            postal_code (str): Postal code. [optional]  # noqa: E501
            rma (str): RMA number. [optional]  # noqa: E501
            ship_on_date (str): Date the customer is requesting that the order ship on.  Typically used for perishable product delivery.. [optional]  # noqa: E501
            ship_to_residential (bool): True if the shipping address is residential.  Effects the methods that are available to the customer as well as the price of the shipping method.. [optional]  # noqa: E501
            shipping_3rd_party_account_number (str): Shipping 3rd party account number. [optional]  # noqa: E501
            shipping_date (str): Date/time the order shipped on.  This date is set once the first shipment is sent to the customer.. [optional]  # noqa: E501
            shipping_department_status (str): Shipping department status. [optional]  # noqa: E501
            shipping_method (str): Shipping method. [optional]  # noqa: E501
            shipping_method_accounting_code (str): Shipping method accounting code. [optional]  # noqa: E501
            special_instructions (str): Special instructions from the customer regarding shipping. [optional]  # noqa: E501
            state_region (str): State. [optional]  # noqa: E501
            title (str): Title. [optional]  # noqa: E501
            tracking_number_details ([OrderTrackingNumberDetails]): Tracking number details. [optional]  # noqa: E501
            tracking_numbers ([str]): Tracking numbers. [optional]  # noqa: E501
            weight (Weight): [optional]  # noqa: E501
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
