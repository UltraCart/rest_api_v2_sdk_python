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
    from ultracart.model.auto_order_item_future_schedule import AutoOrderItemFutureSchedule
    from ultracart.model.auto_order_item_option import AutoOrderItemOption
    from ultracart.model.auto_order_item_simple_schedule import AutoOrderItemSimpleSchedule
    globals()['AutoOrderItemFutureSchedule'] = AutoOrderItemFutureSchedule
    globals()['AutoOrderItemOption'] = AutoOrderItemOption
    globals()['AutoOrderItemSimpleSchedule'] = AutoOrderItemSimpleSchedule


class AutoOrderItem(ModelNormal):
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
        ('frequency',): {
            'WEEKLY': "Weekly",
            'BIWEEKLY': "Biweekly",
            'EVERY...': "Every...",
            'EVERY_10_DAYS': "Every 10 Days",
            'EVERY_24_DAYS': "Every 24 Days",
            'EVERY_28_DAYS': "Every 28 Days",
            'MONTHLY': "Monthly",
            'EVERY_45_DAYS': "Every 45 Days",
            'EVERY_2_MONTHS': "Every 2 Months",
            'EVERY_3_MONTHS': "Every 3 Months",
            'EVERY_4_MONTHS': "Every 4 Months",
            'EVERY_6_MONTHS': "Every 6 Months",
            'YEARLY': "Yearly",
        },
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
            'arbitrary_item_id': (str,),  # noqa: E501
            'arbitrary_percentage_discount': (float,),  # noqa: E501
            'arbitrary_quantity': (float,),  # noqa: E501
            'arbitrary_schedule_days': (int,),  # noqa: E501
            'arbitrary_unit_cost': (float,),  # noqa: E501
            'arbitrary_unit_cost_remaining_orders': (int,),  # noqa: E501
            'auto_order_item_oid': (int,),  # noqa: E501
            'frequency': (str,),  # noqa: E501
            'future_schedules': ([AutoOrderItemFutureSchedule],),  # noqa: E501
            'last_order_dts': (str,),  # noqa: E501
            'life_time_value': (float,),  # noqa: E501
            'next_preshipment_notice_dts': (str,),  # noqa: E501
            'next_shipment_dts': (str,),  # noqa: E501
            'no_order_after_dts': (str,),  # noqa: E501
            'number_of_rebills': (int,),  # noqa: E501
            'options': ([AutoOrderItemOption],),  # noqa: E501
            'original_item_id': (str,),  # noqa: E501
            'original_quantity': (float,),  # noqa: E501
            'paypal_payer_id': (str,),  # noqa: E501
            'paypal_recurring_payment_profile_id': (str,),  # noqa: E501
            'preshipment_notice_sent': (bool,),  # noqa: E501
            'rebill_value': (float,),  # noqa: E501
            'remaining_repeat_count': (int,),  # noqa: E501
            'simple_schedule': (AutoOrderItemSimpleSchedule,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'arbitrary_item_id': 'arbitrary_item_id',  # noqa: E501
        'arbitrary_percentage_discount': 'arbitrary_percentage_discount',  # noqa: E501
        'arbitrary_quantity': 'arbitrary_quantity',  # noqa: E501
        'arbitrary_schedule_days': 'arbitrary_schedule_days',  # noqa: E501
        'arbitrary_unit_cost': 'arbitrary_unit_cost',  # noqa: E501
        'arbitrary_unit_cost_remaining_orders': 'arbitrary_unit_cost_remaining_orders',  # noqa: E501
        'auto_order_item_oid': 'auto_order_item_oid',  # noqa: E501
        'frequency': 'frequency',  # noqa: E501
        'future_schedules': 'future_schedules',  # noqa: E501
        'last_order_dts': 'last_order_dts',  # noqa: E501
        'life_time_value': 'life_time_value',  # noqa: E501
        'next_preshipment_notice_dts': 'next_preshipment_notice_dts',  # noqa: E501
        'next_shipment_dts': 'next_shipment_dts',  # noqa: E501
        'no_order_after_dts': 'no_order_after_dts',  # noqa: E501
        'number_of_rebills': 'number_of_rebills',  # noqa: E501
        'options': 'options',  # noqa: E501
        'original_item_id': 'original_item_id',  # noqa: E501
        'original_quantity': 'original_quantity',  # noqa: E501
        'paypal_payer_id': 'paypal_payer_id',  # noqa: E501
        'paypal_recurring_payment_profile_id': 'paypal_recurring_payment_profile_id',  # noqa: E501
        'preshipment_notice_sent': 'preshipment_notice_sent',  # noqa: E501
        'rebill_value': 'rebill_value',  # noqa: E501
        'remaining_repeat_count': 'remaining_repeat_count',  # noqa: E501
        'simple_schedule': 'simple_schedule',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AutoOrderItem - a model defined in OpenAPI

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
            arbitrary_item_id (str): Arbitrary item id that should be rebilled instead of the normal schedule. [optional]  # noqa: E501
            arbitrary_percentage_discount (float): An arbitrary percentage discount to provide on future rebills. [optional]  # noqa: E501
            arbitrary_quantity (float): Arbitrary quantity to rebill. [optional]  # noqa: E501
            arbitrary_schedule_days (int): The number of days to rebill if the frequency is set to an arbitrary number of days. [optional]  # noqa: E501
            arbitrary_unit_cost (float): Arbitrary unit cost that rebills of this item should occur at. [optional]  # noqa: E501
            arbitrary_unit_cost_remaining_orders (int): The number of rebills to give the arbitrary unit cost on before reverting to normal pricing.. [optional]  # noqa: E501
            auto_order_item_oid (int): Primary key of AutoOrderItem. [optional]  # noqa: E501
            frequency (str): Frequency of the rebill if not a fixed schedule. [optional]  # noqa: E501
            future_schedules ([AutoOrderItemFutureSchedule]): The future rebill schedule for this item up to the next ten rebills. [optional]  # noqa: E501
            last_order_dts (str): Date/time of the last order of this item. [optional]  # noqa: E501
            life_time_value (float): The life time value of this item including the original purchase. [optional]  # noqa: E501
            next_preshipment_notice_dts (str): The date/time of when the next pre-shipment notice should be sent. [optional]  # noqa: E501
            next_shipment_dts (str): Date/time that this item is scheduled to rebill. [optional]  # noqa: E501
            no_order_after_dts (str): Date/time after which no additional rebills of this item should occur. [optional]  # noqa: E501
            number_of_rebills (int): The number of times this item has rebilled. [optional]  # noqa: E501
            options ([AutoOrderItemOption]): Options associated with this item. [optional]  # noqa: E501
            original_item_id (str): The original item id purchased.  This item controls scheduling.  If you wish to modify a schedule, for example, from monthly to yearly, change this item from your monthly item to your yearly item, and then change the next_shipment_dts to your desired date.. [optional]  # noqa: E501
            original_quantity (float): The original quantity purchased. [optional]  # noqa: E501
            paypal_payer_id (str): The PayPal Payer ID tied to this item. [optional]  # noqa: E501
            paypal_recurring_payment_profile_id (str): The PayPal Profile ID tied to this item. [optional]  # noqa: E501
            preshipment_notice_sent (bool): True if the preshipment notice associated with the next rebill has been sent. [optional]  # noqa: E501
            rebill_value (float): The value of the rebills of this item. [optional]  # noqa: E501
            remaining_repeat_count (int): The number of rebills remaining before this item is complete. [optional]  # noqa: E501
            simple_schedule (AutoOrderItemSimpleSchedule): [optional]  # noqa: E501
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
        """AutoOrderItem - a model defined in OpenAPI

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
            arbitrary_item_id (str): Arbitrary item id that should be rebilled instead of the normal schedule. [optional]  # noqa: E501
            arbitrary_percentage_discount (float): An arbitrary percentage discount to provide on future rebills. [optional]  # noqa: E501
            arbitrary_quantity (float): Arbitrary quantity to rebill. [optional]  # noqa: E501
            arbitrary_schedule_days (int): The number of days to rebill if the frequency is set to an arbitrary number of days. [optional]  # noqa: E501
            arbitrary_unit_cost (float): Arbitrary unit cost that rebills of this item should occur at. [optional]  # noqa: E501
            arbitrary_unit_cost_remaining_orders (int): The number of rebills to give the arbitrary unit cost on before reverting to normal pricing.. [optional]  # noqa: E501
            auto_order_item_oid (int): Primary key of AutoOrderItem. [optional]  # noqa: E501
            frequency (str): Frequency of the rebill if not a fixed schedule. [optional]  # noqa: E501
            future_schedules ([AutoOrderItemFutureSchedule]): The future rebill schedule for this item up to the next ten rebills. [optional]  # noqa: E501
            last_order_dts (str): Date/time of the last order of this item. [optional]  # noqa: E501
            life_time_value (float): The life time value of this item including the original purchase. [optional]  # noqa: E501
            next_preshipment_notice_dts (str): The date/time of when the next pre-shipment notice should be sent. [optional]  # noqa: E501
            next_shipment_dts (str): Date/time that this item is scheduled to rebill. [optional]  # noqa: E501
            no_order_after_dts (str): Date/time after which no additional rebills of this item should occur. [optional]  # noqa: E501
            number_of_rebills (int): The number of times this item has rebilled. [optional]  # noqa: E501
            options ([AutoOrderItemOption]): Options associated with this item. [optional]  # noqa: E501
            original_item_id (str): The original item id purchased.  This item controls scheduling.  If you wish to modify a schedule, for example, from monthly to yearly, change this item from your monthly item to your yearly item, and then change the next_shipment_dts to your desired date.. [optional]  # noqa: E501
            original_quantity (float): The original quantity purchased. [optional]  # noqa: E501
            paypal_payer_id (str): The PayPal Payer ID tied to this item. [optional]  # noqa: E501
            paypal_recurring_payment_profile_id (str): The PayPal Profile ID tied to this item. [optional]  # noqa: E501
            preshipment_notice_sent (bool): True if the preshipment notice associated with the next rebill has been sent. [optional]  # noqa: E501
            rebill_value (float): The value of the rebills of this item. [optional]  # noqa: E501
            remaining_repeat_count (int): The number of rebills remaining before this item is complete. [optional]  # noqa: E501
            simple_schedule (AutoOrderItemSimpleSchedule): [optional]  # noqa: E501
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
