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
    from ultracart.model.affiliate_click import AffiliateClick
    from ultracart.model.affiliate_link import AffiliateLink
    from ultracart.model.order import Order
    globals()['AffiliateClick'] = AffiliateClick
    globals()['AffiliateLink'] = AffiliateLink
    globals()['Order'] = Order


class AffiliateLedger(ModelNormal):
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
        ('transaction_state',): {
            'PENDING': "Pending",
            'POSTED': "Posted",
            'APPROVED': "Approved",
            'PAID': "Paid",
            'REJECTED': "Rejected",
            'PARTIALLY_PAID': "Partially Paid",
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
            'affiliate_click_oid': (int,),  # noqa: E501
            'affiliate_ledger_oid': (int,),  # noqa: E501
            'affiliate_link_oid': (int,),  # noqa: E501
            'affiliate_oid': (int,),  # noqa: E501
            'assigned_by_user': (str,),  # noqa: E501
            'click': (AffiliateClick,),  # noqa: E501
            'item_id': (str,),  # noqa: E501
            'link': (AffiliateLink,),  # noqa: E501
            'order': (Order,),  # noqa: E501
            'order_id': (str,),  # noqa: E501
            'original_transaction_dts': (str,),  # noqa: E501
            'sub_id': (str,),  # noqa: E501
            'tier_number': (int,),  # noqa: E501
            'transaction_amount': (float,),  # noqa: E501
            'transaction_amount_paid': (float,),  # noqa: E501
            'transaction_dts': (str,),  # noqa: E501
            'transaction_memo': (str,),  # noqa: E501
            'transaction_percentage': (float,),  # noqa: E501
            'transaction_state': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'affiliate_click_oid': 'affiliate_click_oid',  # noqa: E501
        'affiliate_ledger_oid': 'affiliate_ledger_oid',  # noqa: E501
        'affiliate_link_oid': 'affiliate_link_oid',  # noqa: E501
        'affiliate_oid': 'affiliate_oid',  # noqa: E501
        'assigned_by_user': 'assigned_by_user',  # noqa: E501
        'click': 'click',  # noqa: E501
        'item_id': 'item_id',  # noqa: E501
        'link': 'link',  # noqa: E501
        'order': 'order',  # noqa: E501
        'order_id': 'order_id',  # noqa: E501
        'original_transaction_dts': 'original_transaction_dts',  # noqa: E501
        'sub_id': 'sub_id',  # noqa: E501
        'tier_number': 'tier_number',  # noqa: E501
        'transaction_amount': 'transaction_amount',  # noqa: E501
        'transaction_amount_paid': 'transaction_amount_paid',  # noqa: E501
        'transaction_dts': 'transaction_dts',  # noqa: E501
        'transaction_memo': 'transaction_memo',  # noqa: E501
        'transaction_percentage': 'transaction_percentage',  # noqa: E501
        'transaction_state': 'transaction_state',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AffiliateLedger - a model defined in OpenAPI

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
            affiliate_click_oid (int): Unique object identifier for the click associated with this ledger entry. [optional]  # noqa: E501
            affiliate_ledger_oid (int): Affiliate ledger object ID associated with this ledger. [optional]  # noqa: E501
            affiliate_link_oid (int): Unique object identifier for the link that this click is associated with. [optional]  # noqa: E501
            affiliate_oid (int): Affiliate object ID associated with this transaction. [optional]  # noqa: E501
            assigned_by_user (str): User that assigned the transaction if it was done manually. [optional]  # noqa: E501
            click (AffiliateClick): [optional]  # noqa: E501
            item_id (str): Item ID associated with this transaction. [optional]  # noqa: E501
            link (AffiliateLink): [optional]  # noqa: E501
            order (Order): [optional]  # noqa: E501
            order_id (str): Order ID associated with this transaction. [optional]  # noqa: E501
            original_transaction_dts (str): Date/time of the original transaction for reversals. [optional]  # noqa: E501
            sub_id (str): Sub ID associated with transaction (from the click). [optional]  # noqa: E501
            tier_number (int): Tier number that this transaction earned. [optional]  # noqa: E501
            transaction_amount (float): Transaction amount. [optional]  # noqa: E501
            transaction_amount_paid (float): Amount of the transaction that has been paid out.. [optional]  # noqa: E501
            transaction_dts (str): Date/time that the transaction was made. [optional]  # noqa: E501
            transaction_memo (str): Memo explaining the transaction. [optional]  # noqa: E501
            transaction_percentage (float): Percentage associated with this transaction. [optional]  # noqa: E501
            transaction_state (str): Transaction state. [optional]  # noqa: E501
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
        """AffiliateLedger - a model defined in OpenAPI

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
            affiliate_click_oid (int): Unique object identifier for the click associated with this ledger entry. [optional]  # noqa: E501
            affiliate_ledger_oid (int): Affiliate ledger object ID associated with this ledger. [optional]  # noqa: E501
            affiliate_link_oid (int): Unique object identifier for the link that this click is associated with. [optional]  # noqa: E501
            affiliate_oid (int): Affiliate object ID associated with this transaction. [optional]  # noqa: E501
            assigned_by_user (str): User that assigned the transaction if it was done manually. [optional]  # noqa: E501
            click (AffiliateClick): [optional]  # noqa: E501
            item_id (str): Item ID associated with this transaction. [optional]  # noqa: E501
            link (AffiliateLink): [optional]  # noqa: E501
            order (Order): [optional]  # noqa: E501
            order_id (str): Order ID associated with this transaction. [optional]  # noqa: E501
            original_transaction_dts (str): Date/time of the original transaction for reversals. [optional]  # noqa: E501
            sub_id (str): Sub ID associated with transaction (from the click). [optional]  # noqa: E501
            tier_number (int): Tier number that this transaction earned. [optional]  # noqa: E501
            transaction_amount (float): Transaction amount. [optional]  # noqa: E501
            transaction_amount_paid (float): Amount of the transaction that has been paid out.. [optional]  # noqa: E501
            transaction_dts (str): Date/time that the transaction was made. [optional]  # noqa: E501
            transaction_memo (str): Memo explaining the transaction. [optional]  # noqa: E501
            transaction_percentage (float): Percentage associated with this transaction. [optional]  # noqa: E501
            transaction_state (str): Transaction state. [optional]  # noqa: E501
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