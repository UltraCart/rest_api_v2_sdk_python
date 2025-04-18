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



class EmailCommseqStat(ModelNormal):
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
            'click_count': (int,),  # noqa: E501
            'click_count_formatted': (str,),  # noqa: E501
            'conversion_count': (int,),  # noqa: E501
            'conversion_count_formatted': (str,),  # noqa: E501
            'delivered_count': (int,),  # noqa: E501
            'delivered_count_formatted': (str,),  # noqa: E501
            'email_communication_sequence_uuid': (str,),  # noqa: E501
            'finished_count': (int,),  # noqa: E501
            'finished_count_formatted': (str,),  # noqa: E501
            'in_progress_count': (int,),  # noqa: E501
            'in_progress_count_formatted': (str,),  # noqa: E501
            'kickbox_count': (int,),  # noqa: E501
            'kickbox_count_formatted': (str,),  # noqa: E501
            'merchant_id': (str,),  # noqa: E501
            'open_count': (int,),  # noqa: E501
            'open_count_formatted': (str,),  # noqa: E501
            'order_count': (int,),  # noqa: E501
            'order_count_formatted': (str,),  # noqa: E501
            'permanent_bounce_count': (int,),  # noqa: E501
            'permanent_bounce_count_formatted': (str,),  # noqa: E501
            'profit': (float,),  # noqa: E501
            'profit_formatted': (str,),  # noqa: E501
            'revenue': (float,),  # noqa: E501
            'revenue_formatted': (str,),  # noqa: E501
            'send_count': (int,),  # noqa: E501
            'send_count_formatted': (str,),  # noqa: E501
            'skipped_count': (int,),  # noqa: E501
            'skipped_count_formatted': (str,),  # noqa: E501
            'spam_count': (int,),  # noqa: E501
            'spam_count_formatted': (str,),  # noqa: E501
            'started_count': (int,),  # noqa: E501
            'started_count_formatted': (str,),  # noqa: E501
            'storefront_oid': (int,),  # noqa: E501
            'unsubscribe_count': (int,),  # noqa: E501
            'unsubscribe_count_formatted': (str,),  # noqa: E501
            'view_count': (int,),  # noqa: E501
            'view_count_formatted': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'click_count': 'click_count',  # noqa: E501
        'click_count_formatted': 'click_count_formatted',  # noqa: E501
        'conversion_count': 'conversion_count',  # noqa: E501
        'conversion_count_formatted': 'conversion_count_formatted',  # noqa: E501
        'delivered_count': 'delivered_count',  # noqa: E501
        'delivered_count_formatted': 'delivered_count_formatted',  # noqa: E501
        'email_communication_sequence_uuid': 'email_communication_sequence_uuid',  # noqa: E501
        'finished_count': 'finished_count',  # noqa: E501
        'finished_count_formatted': 'finished_count_formatted',  # noqa: E501
        'in_progress_count': 'in_progress_count',  # noqa: E501
        'in_progress_count_formatted': 'in_progress_count_formatted',  # noqa: E501
        'kickbox_count': 'kickbox_count',  # noqa: E501
        'kickbox_count_formatted': 'kickbox_count_formatted',  # noqa: E501
        'merchant_id': 'merchant_id',  # noqa: E501
        'open_count': 'open_count',  # noqa: E501
        'open_count_formatted': 'open_count_formatted',  # noqa: E501
        'order_count': 'order_count',  # noqa: E501
        'order_count_formatted': 'order_count_formatted',  # noqa: E501
        'permanent_bounce_count': 'permanent_bounce_count',  # noqa: E501
        'permanent_bounce_count_formatted': 'permanent_bounce_count_formatted',  # noqa: E501
        'profit': 'profit',  # noqa: E501
        'profit_formatted': 'profit_formatted',  # noqa: E501
        'revenue': 'revenue',  # noqa: E501
        'revenue_formatted': 'revenue_formatted',  # noqa: E501
        'send_count': 'send_count',  # noqa: E501
        'send_count_formatted': 'send_count_formatted',  # noqa: E501
        'skipped_count': 'skipped_count',  # noqa: E501
        'skipped_count_formatted': 'skipped_count_formatted',  # noqa: E501
        'spam_count': 'spam_count',  # noqa: E501
        'spam_count_formatted': 'spam_count_formatted',  # noqa: E501
        'started_count': 'started_count',  # noqa: E501
        'started_count_formatted': 'started_count_formatted',  # noqa: E501
        'storefront_oid': 'storefront_oid',  # noqa: E501
        'unsubscribe_count': 'unsubscribe_count',  # noqa: E501
        'unsubscribe_count_formatted': 'unsubscribe_count_formatted',  # noqa: E501
        'view_count': 'view_count',  # noqa: E501
        'view_count_formatted': 'view_count_formatted',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EmailCommseqStat - a model defined in OpenAPI

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
            click_count (int): Count of clicked emails. [optional]  # noqa: E501
            click_count_formatted (str): Count of clicked emails, formatted. [optional]  # noqa: E501
            conversion_count (int): Count of conversion. [optional]  # noqa: E501
            conversion_count_formatted (str): Count of conversions, formatted. [optional]  # noqa: E501
            delivered_count (int): Count of delivered emails. [optional]  # noqa: E501
            delivered_count_formatted (str): Count of delivered emails, formatted. [optional]  # noqa: E501
            email_communication_sequence_uuid (str): UUID associated with the communication sequence. [optional]  # noqa: E501
            finished_count (int): Count of customers that finished the sequence. [optional]  # noqa: E501
            finished_count_formatted (str): Count of customers that finished the sequence, formatted. [optional]  # noqa: E501
            in_progress_count (int): Count of customers in progress. [optional]  # noqa: E501
            in_progress_count_formatted (str): Count of customers in progress, formatted. [optional]  # noqa: E501
            kickbox_count (int): Count of emails kicked. [optional]  # noqa: E501
            kickbox_count_formatted (str): Count of emails kicked, formatted. [optional]  # noqa: E501
            merchant_id (str): Merchant ID. [optional]  # noqa: E501
            open_count (int): Count of opened emails. [optional]  # noqa: E501
            open_count_formatted (str): Count of opened emails, formatted. [optional]  # noqa: E501
            order_count (int): Count of orders. [optional]  # noqa: E501
            order_count_formatted (str): Count of orders, formatted. [optional]  # noqa: E501
            permanent_bounce_count (int): Count of emails permanently bounced. [optional]  # noqa: E501
            permanent_bounce_count_formatted (str): Count of emails permanently bounced, formatted. [optional]  # noqa: E501
            profit (float): Profit. [optional]  # noqa: E501
            profit_formatted (str): Profit, formatted. [optional]  # noqa: E501
            revenue (float): Revenue. [optional]  # noqa: E501
            revenue_formatted (str): Revenue, formatted. [optional]  # noqa: E501
            send_count (int): Count of emails sent. [optional]  # noqa: E501
            send_count_formatted (str): Count of emails sent, formatted. [optional]  # noqa: E501
            skipped_count (int): Count of skipped emails. [optional]  # noqa: E501
            skipped_count_formatted (str): Count of skipped emails, formatted. [optional]  # noqa: E501
            spam_count (int): Count of emails classified as spam. [optional]  # noqa: E501
            spam_count_formatted (str): Count of emails classified as spam, formatted. [optional]  # noqa: E501
            started_count (int): Count of customers that started the sequence. [optional]  # noqa: E501
            started_count_formatted (str): Count of customers that started the sequence, formatted. [optional]  # noqa: E501
            storefront_oid (int): Storefront oid. [optional]  # noqa: E501
            unsubscribe_count (int): Count of unsubscribes caused. [optional]  # noqa: E501
            unsubscribe_count_formatted (str): Count of unsubscribes caused, formatted. [optional]  # noqa: E501
            view_count (int): Count of views. [optional]  # noqa: E501
            view_count_formatted (str): Count of views, formatted. [optional]  # noqa: E501
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
        """EmailCommseqStat - a model defined in OpenAPI

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
            click_count (int): Count of clicked emails. [optional]  # noqa: E501
            click_count_formatted (str): Count of clicked emails, formatted. [optional]  # noqa: E501
            conversion_count (int): Count of conversion. [optional]  # noqa: E501
            conversion_count_formatted (str): Count of conversions, formatted. [optional]  # noqa: E501
            delivered_count (int): Count of delivered emails. [optional]  # noqa: E501
            delivered_count_formatted (str): Count of delivered emails, formatted. [optional]  # noqa: E501
            email_communication_sequence_uuid (str): UUID associated with the communication sequence. [optional]  # noqa: E501
            finished_count (int): Count of customers that finished the sequence. [optional]  # noqa: E501
            finished_count_formatted (str): Count of customers that finished the sequence, formatted. [optional]  # noqa: E501
            in_progress_count (int): Count of customers in progress. [optional]  # noqa: E501
            in_progress_count_formatted (str): Count of customers in progress, formatted. [optional]  # noqa: E501
            kickbox_count (int): Count of emails kicked. [optional]  # noqa: E501
            kickbox_count_formatted (str): Count of emails kicked, formatted. [optional]  # noqa: E501
            merchant_id (str): Merchant ID. [optional]  # noqa: E501
            open_count (int): Count of opened emails. [optional]  # noqa: E501
            open_count_formatted (str): Count of opened emails, formatted. [optional]  # noqa: E501
            order_count (int): Count of orders. [optional]  # noqa: E501
            order_count_formatted (str): Count of orders, formatted. [optional]  # noqa: E501
            permanent_bounce_count (int): Count of emails permanently bounced. [optional]  # noqa: E501
            permanent_bounce_count_formatted (str): Count of emails permanently bounced, formatted. [optional]  # noqa: E501
            profit (float): Profit. [optional]  # noqa: E501
            profit_formatted (str): Profit, formatted. [optional]  # noqa: E501
            revenue (float): Revenue. [optional]  # noqa: E501
            revenue_formatted (str): Revenue, formatted. [optional]  # noqa: E501
            send_count (int): Count of emails sent. [optional]  # noqa: E501
            send_count_formatted (str): Count of emails sent, formatted. [optional]  # noqa: E501
            skipped_count (int): Count of skipped emails. [optional]  # noqa: E501
            skipped_count_formatted (str): Count of skipped emails, formatted. [optional]  # noqa: E501
            spam_count (int): Count of emails classified as spam. [optional]  # noqa: E501
            spam_count_formatted (str): Count of emails classified as spam, formatted. [optional]  # noqa: E501
            started_count (int): Count of customers that started the sequence. [optional]  # noqa: E501
            started_count_formatted (str): Count of customers that started the sequence, formatted. [optional]  # noqa: E501
            storefront_oid (int): Storefront oid. [optional]  # noqa: E501
            unsubscribe_count (int): Count of unsubscribes caused. [optional]  # noqa: E501
            unsubscribe_count_formatted (str): Count of unsubscribes caused, formatted. [optional]  # noqa: E501
            view_count (int): Count of views. [optional]  # noqa: E501
            view_count_formatted (str): Count of views, formatted. [optional]  # noqa: E501
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
