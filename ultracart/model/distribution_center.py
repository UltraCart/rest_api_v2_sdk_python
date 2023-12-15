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



class DistributionCenter(ModelNormal):
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
        return {
            'address1': (str,),  # noqa: E501
            'address2': (str,),  # noqa: E501
            'city': (str,),  # noqa: E501
            'code': (str,),  # noqa: E501
            'country_code': (str,),  # noqa: E501
            'default_center': (bool,),  # noqa: E501
            'default_handles_all_items': (bool,),  # noqa: E501
            'distribution_center_oid': (int,),  # noqa: E501
            'duns': (str,),  # noqa: E501
            'estimate_from_distribution_center_oid': (int,),  # noqa: E501
            'ftp_password': (str,),  # noqa: E501
            'hold_before_shipment_minutes': (int,),  # noqa: E501
            'hold_before_transmission': (bool,),  # noqa: E501
            'hold_auto_order_before_shipment_minutes': (int,),  # noqa: E501
            'latitude': (float,),  # noqa: E501
            'longitude': (float,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'no_customer_direct_shipments': (bool,),  # noqa: E501
            'no_split_shipment': (bool,),  # noqa: E501
            'pickup_cutoff_time_friday': (str,),  # noqa: E501
            'pickup_cutoff_time_monday': (str,),  # noqa: E501
            'pickup_cutoff_time_saturday': (str,),  # noqa: E501
            'pickup_cutoff_time_sunday': (str,),  # noqa: E501
            'pickup_cutoff_time_thursday': (str,),  # noqa: E501
            'pickup_cutoff_time_tuesday': (str,),  # noqa: E501
            'pickup_cutoff_time_wednesday': (str,),  # noqa: E501
            'pickup_start_time_friday': (str,),  # noqa: E501
            'pickup_start_time_monday': (str,),  # noqa: E501
            'pickup_start_time_saturday': (str,),  # noqa: E501
            'pickup_start_time_sunday': (str,),  # noqa: E501
            'pickup_start_time_thursday': (str,),  # noqa: E501
            'pickup_start_time_tuesday': (str,),  # noqa: E501
            'pickup_start_time_wednesday': (str,),  # noqa: E501
            'pickup_tz': (str,),  # noqa: E501
            'postal_code': (str,),  # noqa: E501
            'process_days': (int,),  # noqa: E501
            'process_inventory_start_time': (str,),  # noqa: E501
            'process_inventory_stop_time': (str,),  # noqa: E501
            'require_asn': (bool,),  # noqa: E501
            'send_kit_instead_of_components': (bool,),  # noqa: E501
            'shipment_cutoff_time_friday': (str,),  # noqa: E501
            'shipment_cutoff_time_monday': (str,),  # noqa: E501
            'shipment_cutoff_time_saturday': (str,),  # noqa: E501
            'shipment_cutoff_time_sunday': (str,),  # noqa: E501
            'shipment_cutoff_time_thursday': (str,),  # noqa: E501
            'shipment_cutoff_time_tuesday': (str,),  # noqa: E501
            'shipment_cutoff_time_wednesday': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'transmit_blank_costs': (bool,),  # noqa: E501
            'transport': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'address1': 'address1',  # noqa: E501
        'address2': 'address2',  # noqa: E501
        'city': 'city',  # noqa: E501
        'code': 'code',  # noqa: E501
        'country_code': 'country_code',  # noqa: E501
        'default_center': 'default_center',  # noqa: E501
        'default_handles_all_items': 'default_handles_all_items',  # noqa: E501
        'distribution_center_oid': 'distribution_center_oid',  # noqa: E501
        'duns': 'duns',  # noqa: E501
        'estimate_from_distribution_center_oid': 'estimate_from_distribution_center_oid',  # noqa: E501
        'ftp_password': 'ftp_password',  # noqa: E501
        'hold_before_shipment_minutes': 'hold_before_shipment_minutes',  # noqa: E501
        'hold_before_transmission': 'hold_before_transmission',  # noqa: E501
        'hold_auto_order_before_shipment_minutes': 'holdAutoOrderBeforeShipmentMinutes',  # noqa: E501
        'latitude': 'latitude',  # noqa: E501
        'longitude': 'longitude',  # noqa: E501
        'name': 'name',  # noqa: E501
        'no_customer_direct_shipments': 'no_customer_direct_shipments',  # noqa: E501
        'no_split_shipment': 'no_split_shipment',  # noqa: E501
        'pickup_cutoff_time_friday': 'pickup_cutoff_time_friday',  # noqa: E501
        'pickup_cutoff_time_monday': 'pickup_cutoff_time_monday',  # noqa: E501
        'pickup_cutoff_time_saturday': 'pickup_cutoff_time_saturday',  # noqa: E501
        'pickup_cutoff_time_sunday': 'pickup_cutoff_time_sunday',  # noqa: E501
        'pickup_cutoff_time_thursday': 'pickup_cutoff_time_thursday',  # noqa: E501
        'pickup_cutoff_time_tuesday': 'pickup_cutoff_time_tuesday',  # noqa: E501
        'pickup_cutoff_time_wednesday': 'pickup_cutoff_time_wednesday',  # noqa: E501
        'pickup_start_time_friday': 'pickup_start_time_friday',  # noqa: E501
        'pickup_start_time_monday': 'pickup_start_time_monday',  # noqa: E501
        'pickup_start_time_saturday': 'pickup_start_time_saturday',  # noqa: E501
        'pickup_start_time_sunday': 'pickup_start_time_sunday',  # noqa: E501
        'pickup_start_time_thursday': 'pickup_start_time_thursday',  # noqa: E501
        'pickup_start_time_tuesday': 'pickup_start_time_tuesday',  # noqa: E501
        'pickup_start_time_wednesday': 'pickup_start_time_wednesday',  # noqa: E501
        'pickup_tz': 'pickup_tz',  # noqa: E501
        'postal_code': 'postal_code',  # noqa: E501
        'process_days': 'process_days',  # noqa: E501
        'process_inventory_start_time': 'process_inventory_start_time',  # noqa: E501
        'process_inventory_stop_time': 'process_inventory_stop_time',  # noqa: E501
        'require_asn': 'require_asn',  # noqa: E501
        'send_kit_instead_of_components': 'send_kit_instead_of_components',  # noqa: E501
        'shipment_cutoff_time_friday': 'shipment_cutoff_time_friday',  # noqa: E501
        'shipment_cutoff_time_monday': 'shipment_cutoff_time_monday',  # noqa: E501
        'shipment_cutoff_time_saturday': 'shipment_cutoff_time_saturday',  # noqa: E501
        'shipment_cutoff_time_sunday': 'shipment_cutoff_time_sunday',  # noqa: E501
        'shipment_cutoff_time_thursday': 'shipment_cutoff_time_thursday',  # noqa: E501
        'shipment_cutoff_time_tuesday': 'shipment_cutoff_time_tuesday',  # noqa: E501
        'shipment_cutoff_time_wednesday': 'shipment_cutoff_time_wednesday',  # noqa: E501
        'state': 'state',  # noqa: E501
        'transmit_blank_costs': 'transmit_blank_costs',  # noqa: E501
        'transport': 'transport',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """DistributionCenter - a model defined in OpenAPI

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
            address1 (str): Address line 1 of the distribution center. [optional]  # noqa: E501
            address2 (str): Address line 2 of the distribution center. [optional]  # noqa: E501
            city (str): City of the distribution center. [optional]  # noqa: E501
            code (str): Unique code for this distribution center. [optional]  # noqa: E501
            country_code (str): Country code of the distribution center. [optional]  # noqa: E501
            default_center (bool): True if this is the default distribution center on the account. [optional]  # noqa: E501
            default_handles_all_items (bool): True if this distribution center handles all new items by default. [optional]  # noqa: E501
            distribution_center_oid (int): Distribution center object identifier. [optional]  # noqa: E501
            duns (str): DUNS number assigned to this distribution center (EDI). [optional]  # noqa: E501
            estimate_from_distribution_center_oid (int): Estimate shipments for this distribution center as if they came from the other distribution center. [optional]  # noqa: E501
            ftp_password (str): Password associated with the virtual FTP. [optional]  # noqa: E501
            hold_before_shipment_minutes (int): The number of minutes to hold a shipment. [optional]  # noqa: E501
            hold_before_transmission (bool): True if the shipment should be held before transmission and require a manual release. [optional]  # noqa: E501
            hold_auto_order_before_shipment_minutes (int): [optional]  # noqa: E501
            latitude (float): Latitude where the distribution center is located. [optional]  # noqa: E501
            longitude (float): Longitude where the distribution center is located. [optional]  # noqa: E501
            name (str): Name of this distribution center. [optional]  # noqa: E501
            no_customer_direct_shipments (bool): True if this distribution center does not handle customer direct shipments. [optional]  # noqa: E501
            no_split_shipment (bool): True if this distribution center is not allowed to participate in a split shipment.. [optional]  # noqa: E501
            pickup_cutoff_time_friday (str): The time (EST) after which pickups will not be available on Friday. [optional]  # noqa: E501
            pickup_cutoff_time_monday (str): The time (EST) after which pickups will not be available on Monday. [optional]  # noqa: E501
            pickup_cutoff_time_saturday (str): The time (EST) after which pickups will not be available on Saturday. [optional]  # noqa: E501
            pickup_cutoff_time_sunday (str): The time (EST) after which pickups will not be available on Sunday. [optional]  # noqa: E501
            pickup_cutoff_time_thursday (str): The time (EST) after which pickups will not be available on Thursday. [optional]  # noqa: E501
            pickup_cutoff_time_tuesday (str): The time (EST) after which pickups will not be available on Tuesday. [optional]  # noqa: E501
            pickup_cutoff_time_wednesday (str): The time (EST) after which pickups will not be available on Wednesday. [optional]  # noqa: E501
            pickup_start_time_friday (str): The time (EST) after which pickups are available on Friday. [optional]  # noqa: E501
            pickup_start_time_monday (str): The time (EST) after which pickups are available on Monday. [optional]  # noqa: E501
            pickup_start_time_saturday (str): The time (EST) after which pickups are available on Saturday. [optional]  # noqa: E501
            pickup_start_time_sunday (str): The time (EST) after which pickups are available on Sunday. [optional]  # noqa: E501
            pickup_start_time_thursday (str): The time (EST) after which pickups are available on Thursday. [optional]  # noqa: E501
            pickup_start_time_tuesday (str): The time (EST) after which pickups are available on Tuesday. [optional]  # noqa: E501
            pickup_start_time_wednesday (str): The time (EST) after which pickups are available on Wednesday. [optional]  # noqa: E501
            pickup_tz (str): The IANA timezone for all pickup times. [optional]  # noqa: E501
            postal_code (str): Postal code of the distribution center. [optional]  # noqa: E501
            process_days (int): The number of processing days required before an order ships. [optional]  # noqa: E501
            process_inventory_start_time (str): The time (EST) after which inventory updates will be processed. [optional]  # noqa: E501
            process_inventory_stop_time (str): The time (EST) before which inventory updates will be processed. [optional]  # noqa: E501
            require_asn (bool): True if ASNs are required for this distribution center (EDI). [optional]  # noqa: E501
            send_kit_instead_of_components (bool): True if we should send the kit instead of the components. [optional]  # noqa: E501
            shipment_cutoff_time_friday (str): The time (EST) after which shipments will not be processed on Friday. [optional]  # noqa: E501
            shipment_cutoff_time_monday (str): The time (EST) after which shipments will not be processed on Monday. [optional]  # noqa: E501
            shipment_cutoff_time_saturday (str): The time (EST) after which shipments will not be processed on Saturday. [optional]  # noqa: E501
            shipment_cutoff_time_sunday (str): The time (EST) after which shipments will not be processed on Sunday. [optional]  # noqa: E501
            shipment_cutoff_time_thursday (str): The time (EST) after which shipments will not be processed on Thursday. [optional]  # noqa: E501
            shipment_cutoff_time_tuesday (str): The time (EST) after which shipments will not be processed on Tuesday. [optional]  # noqa: E501
            shipment_cutoff_time_wednesday (str): The time (EST) after which shipments will not be processed on Wednesday. [optional]  # noqa: E501
            state (str): State of the distribution center. [optional]  # noqa: E501
            transmit_blank_costs (bool): True if monetary amounts should be zeroed before transmission. [optional]  # noqa: E501
            transport (str): Transport mechanism for this distribution center. [optional]  # noqa: E501
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
        """DistributionCenter - a model defined in OpenAPI

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
            address1 (str): Address line 1 of the distribution center. [optional]  # noqa: E501
            address2 (str): Address line 2 of the distribution center. [optional]  # noqa: E501
            city (str): City of the distribution center. [optional]  # noqa: E501
            code (str): Unique code for this distribution center. [optional]  # noqa: E501
            country_code (str): Country code of the distribution center. [optional]  # noqa: E501
            default_center (bool): True if this is the default distribution center on the account. [optional]  # noqa: E501
            default_handles_all_items (bool): True if this distribution center handles all new items by default. [optional]  # noqa: E501
            distribution_center_oid (int): Distribution center object identifier. [optional]  # noqa: E501
            duns (str): DUNS number assigned to this distribution center (EDI). [optional]  # noqa: E501
            estimate_from_distribution_center_oid (int): Estimate shipments for this distribution center as if they came from the other distribution center. [optional]  # noqa: E501
            ftp_password (str): Password associated with the virtual FTP. [optional]  # noqa: E501
            hold_before_shipment_minutes (int): The number of minutes to hold a shipment. [optional]  # noqa: E501
            hold_before_transmission (bool): True if the shipment should be held before transmission and require a manual release. [optional]  # noqa: E501
            hold_auto_order_before_shipment_minutes (int): [optional]  # noqa: E501
            latitude (float): Latitude where the distribution center is located. [optional]  # noqa: E501
            longitude (float): Longitude where the distribution center is located. [optional]  # noqa: E501
            name (str): Name of this distribution center. [optional]  # noqa: E501
            no_customer_direct_shipments (bool): True if this distribution center does not handle customer direct shipments. [optional]  # noqa: E501
            no_split_shipment (bool): True if this distribution center is not allowed to participate in a split shipment.. [optional]  # noqa: E501
            pickup_cutoff_time_friday (str): The time (EST) after which pickups will not be available on Friday. [optional]  # noqa: E501
            pickup_cutoff_time_monday (str): The time (EST) after which pickups will not be available on Monday. [optional]  # noqa: E501
            pickup_cutoff_time_saturday (str): The time (EST) after which pickups will not be available on Saturday. [optional]  # noqa: E501
            pickup_cutoff_time_sunday (str): The time (EST) after which pickups will not be available on Sunday. [optional]  # noqa: E501
            pickup_cutoff_time_thursday (str): The time (EST) after which pickups will not be available on Thursday. [optional]  # noqa: E501
            pickup_cutoff_time_tuesday (str): The time (EST) after which pickups will not be available on Tuesday. [optional]  # noqa: E501
            pickup_cutoff_time_wednesday (str): The time (EST) after which pickups will not be available on Wednesday. [optional]  # noqa: E501
            pickup_start_time_friday (str): The time (EST) after which pickups are available on Friday. [optional]  # noqa: E501
            pickup_start_time_monday (str): The time (EST) after which pickups are available on Monday. [optional]  # noqa: E501
            pickup_start_time_saturday (str): The time (EST) after which pickups are available on Saturday. [optional]  # noqa: E501
            pickup_start_time_sunday (str): The time (EST) after which pickups are available on Sunday. [optional]  # noqa: E501
            pickup_start_time_thursday (str): The time (EST) after which pickups are available on Thursday. [optional]  # noqa: E501
            pickup_start_time_tuesday (str): The time (EST) after which pickups are available on Tuesday. [optional]  # noqa: E501
            pickup_start_time_wednesday (str): The time (EST) after which pickups are available on Wednesday. [optional]  # noqa: E501
            pickup_tz (str): The IANA timezone for all pickup times. [optional]  # noqa: E501
            postal_code (str): Postal code of the distribution center. [optional]  # noqa: E501
            process_days (int): The number of processing days required before an order ships. [optional]  # noqa: E501
            process_inventory_start_time (str): The time (EST) after which inventory updates will be processed. [optional]  # noqa: E501
            process_inventory_stop_time (str): The time (EST) before which inventory updates will be processed. [optional]  # noqa: E501
            require_asn (bool): True if ASNs are required for this distribution center (EDI). [optional]  # noqa: E501
            send_kit_instead_of_components (bool): True if we should send the kit instead of the components. [optional]  # noqa: E501
            shipment_cutoff_time_friday (str): The time (EST) after which shipments will not be processed on Friday. [optional]  # noqa: E501
            shipment_cutoff_time_monday (str): The time (EST) after which shipments will not be processed on Monday. [optional]  # noqa: E501
            shipment_cutoff_time_saturday (str): The time (EST) after which shipments will not be processed on Saturday. [optional]  # noqa: E501
            shipment_cutoff_time_sunday (str): The time (EST) after which shipments will not be processed on Sunday. [optional]  # noqa: E501
            shipment_cutoff_time_thursday (str): The time (EST) after which shipments will not be processed on Thursday. [optional]  # noqa: E501
            shipment_cutoff_time_tuesday (str): The time (EST) after which shipments will not be processed on Tuesday. [optional]  # noqa: E501
            shipment_cutoff_time_wednesday (str): The time (EST) after which shipments will not be processed on Wednesday. [optional]  # noqa: E501
            state (str): State of the distribution center. [optional]  # noqa: E501
            transmit_blank_costs (bool): True if monetary amounts should be zeroed before transmission. [optional]  # noqa: E501
            transport (str): Transport mechanism for this distribution center. [optional]  # noqa: E501
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
