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
    from ultracart.model.accounts_receivable_retry_day_activity import AccountsReceivableRetryDayActivity
    from ultracart.model.accounts_receivable_retry_transaction_reject import AccountsReceivableRetryTransactionReject
    globals()['AccountsReceivableRetryDayActivity'] = AccountsReceivableRetryDayActivity
    globals()['AccountsReceivableRetryTransactionReject'] = AccountsReceivableRetryTransactionReject


class AccountsReceivableRetryConfig(ModelNormal):
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
            'active': (bool,),  # noqa: E501
            'allow_process_linked_accounts': (bool,),  # noqa: E501
            'cancel_auto_order': (bool,),  # noqa: E501
            'current_service_plan': (str,),  # noqa: E501
            'daily_activity_list': ([AccountsReceivableRetryDayActivity],),  # noqa: E501
            'managed_by_linked_account_merchant_id': (bool,),  # noqa: E501
            'merchant_id': (str,),  # noqa: E501
            'notify_emails': ([str],),  # noqa: E501
            'notify_rejections': (bool,),  # noqa: E501
            'notify_successes': (bool,),  # noqa: E501
            'process_linked_accounts': (bool,),  # noqa: E501
            'processing_percentage': (str,),  # noqa: E501
            'reject_at_end': (bool,),  # noqa: E501
            'transaction_rejects': ([AccountsReceivableRetryTransactionReject],),  # noqa: E501
            'trial_mode': (bool,),  # noqa: E501
            'trial_mode_expiration_dts': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'active': 'active',  # noqa: E501
        'allow_process_linked_accounts': 'allow_process_linked_accounts',  # noqa: E501
        'cancel_auto_order': 'cancel_auto_order',  # noqa: E501
        'current_service_plan': 'current_service_plan',  # noqa: E501
        'daily_activity_list': 'daily_activity_list',  # noqa: E501
        'managed_by_linked_account_merchant_id': 'managed_by_linked_account_merchant_id',  # noqa: E501
        'merchant_id': 'merchant_id',  # noqa: E501
        'notify_emails': 'notify_emails',  # noqa: E501
        'notify_rejections': 'notify_rejections',  # noqa: E501
        'notify_successes': 'notify_successes',  # noqa: E501
        'process_linked_accounts': 'process_linked_accounts',  # noqa: E501
        'processing_percentage': 'processing_percentage',  # noqa: E501
        'reject_at_end': 'reject_at_end',  # noqa: E501
        'transaction_rejects': 'transaction_rejects',  # noqa: E501
        'trial_mode': 'trial_mode',  # noqa: E501
        'trial_mode_expiration_dts': 'trial_mode_expiration_dts',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AccountsReceivableRetryConfig - a model defined in OpenAPI

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
            active (bool): True if the retry should run daily.  False puts the retry service into an inactive state for this merchant.. [optional]  # noqa: E501
            allow_process_linked_accounts (bool): True if this account has linked accounts that it can process.. [optional]  # noqa: E501
            cancel_auto_order (bool): If true also cancel the auto order if the order is rejected at the end. [optional]  # noqa: E501
            current_service_plan (str): The current service plan that the account is on.. [optional]  # noqa: E501
            daily_activity_list ([AccountsReceivableRetryDayActivity]): A list of days and what actions should take place on those days after an order reaches accounts receivable. [optional]  # noqa: E501
            managed_by_linked_account_merchant_id (bool): If not null, this account is managed by the specified parent merchant id.. [optional]  # noqa: E501
            merchant_id (str): UltraCart merchant ID. [optional]  # noqa: E501
            notify_emails ([str]): A list of email addresses to receive summary notifications from the retry service.. [optional]  # noqa: E501
            notify_rejections (bool): If true, email addresses are notified of rejections.. [optional]  # noqa: E501
            notify_successes (bool): If true, email addresses are notified of successful charges.. [optional]  # noqa: E501
            process_linked_accounts (bool): If true, all linked accounts are also processed using the same rules.. [optional]  # noqa: E501
            processing_percentage (str): The percentage rate charged for the service.. [optional]  # noqa: E501
            reject_at_end (bool): If true, the order is rejected the day after the last configured activity day. [optional]  # noqa: E501
            transaction_rejects ([AccountsReceivableRetryTransactionReject]): Array of key/value pairs that when found in the response cause the rejection of the transaction.. [optional]  # noqa: E501
            trial_mode (bool): True if the account is currently in trial mode.  Set to false to exit trial mode.. [optional]  # noqa: E501
            trial_mode_expiration_dts (str): The date when trial mode expires.  If this date is reached without exiting trial mode, the service will de-activate.. [optional]  # noqa: E501
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
        """AccountsReceivableRetryConfig - a model defined in OpenAPI

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
            active (bool): True if the retry should run daily.  False puts the retry service into an inactive state for this merchant.. [optional]  # noqa: E501
            allow_process_linked_accounts (bool): True if this account has linked accounts that it can process.. [optional]  # noqa: E501
            cancel_auto_order (bool): If true also cancel the auto order if the order is rejected at the end. [optional]  # noqa: E501
            current_service_plan (str): The current service plan that the account is on.. [optional]  # noqa: E501
            daily_activity_list ([AccountsReceivableRetryDayActivity]): A list of days and what actions should take place on those days after an order reaches accounts receivable. [optional]  # noqa: E501
            managed_by_linked_account_merchant_id (bool): If not null, this account is managed by the specified parent merchant id.. [optional]  # noqa: E501
            merchant_id (str): UltraCart merchant ID. [optional]  # noqa: E501
            notify_emails ([str]): A list of email addresses to receive summary notifications from the retry service.. [optional]  # noqa: E501
            notify_rejections (bool): If true, email addresses are notified of rejections.. [optional]  # noqa: E501
            notify_successes (bool): If true, email addresses are notified of successful charges.. [optional]  # noqa: E501
            process_linked_accounts (bool): If true, all linked accounts are also processed using the same rules.. [optional]  # noqa: E501
            processing_percentage (str): The percentage rate charged for the service.. [optional]  # noqa: E501
            reject_at_end (bool): If true, the order is rejected the day after the last configured activity day. [optional]  # noqa: E501
            transaction_rejects ([AccountsReceivableRetryTransactionReject]): Array of key/value pairs that when found in the response cause the rejection of the transaction.. [optional]  # noqa: E501
            trial_mode (bool): True if the account is currently in trial mode.  Set to false to exit trial mode.. [optional]  # noqa: E501
            trial_mode_expiration_dts (str): The date when trial mode expires.  If this date is reached without exiting trial mode, the service will de-activate.. [optional]  # noqa: E501
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
