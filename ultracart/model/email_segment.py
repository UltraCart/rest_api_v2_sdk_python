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
    from ultracart.model.email_list_segment_used_by import EmailListSegmentUsedBy
    globals()['EmailListSegmentUsedBy'] = EmailListSegmentUsedBy


class EmailSegment(ModelNormal):
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
            'max_length': 250,
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
            'allow_csv_download': (bool,),  # noqa: E501
            'allow_facebook_audiences': (bool,),  # noqa: E501
            'created_dts': (str,),  # noqa: E501
            'deleted': (bool,),  # noqa: E501
            'email_segment_uuid': (str,),  # noqa: E501
            'esp_list_segment_folder_uuid': (str,),  # noqa: E501
            'facebook_custom_audience': (bool,),  # noqa: E501
            'filter_profile_equation_json': (str,),  # noqa: E501
            'member_count': (int,),  # noqa: E501
            'merchant_id': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'rank_json': (str,),  # noqa: E501
            'rebuild_required': (bool,),  # noqa: E501
            'storefront_oid': (int,),  # noqa: E501
            'thirdparty_join_add_tags': ([str],),  # noqa: E501
            'thirdparty_join_remove_tags': ([str],),  # noqa: E501
            'thirdparty_leave_add_tags': ([str],),  # noqa: E501
            'thirdparty_leave_remove_tags': ([str],),  # noqa: E501
            'thirdparty_list_id': (str,),  # noqa: E501
            'thirdparty_provider_name': (str,),  # noqa: E501
            'used_by': ([EmailListSegmentUsedBy],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'allow_csv_download': 'allow_csv_download',  # noqa: E501
        'allow_facebook_audiences': 'allow_facebook_audiences',  # noqa: E501
        'created_dts': 'created_dts',  # noqa: E501
        'deleted': 'deleted',  # noqa: E501
        'email_segment_uuid': 'email_segment_uuid',  # noqa: E501
        'esp_list_segment_folder_uuid': 'esp_list_segment_folder_uuid',  # noqa: E501
        'facebook_custom_audience': 'facebook_custom_audience',  # noqa: E501
        'filter_profile_equation_json': 'filter_profile_equation_json',  # noqa: E501
        'member_count': 'member_count',  # noqa: E501
        'merchant_id': 'merchant_id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'rank_json': 'rank_json',  # noqa: E501
        'rebuild_required': 'rebuild_required',  # noqa: E501
        'storefront_oid': 'storefront_oid',  # noqa: E501
        'thirdparty_join_add_tags': 'thirdparty_join_add_tags',  # noqa: E501
        'thirdparty_join_remove_tags': 'thirdparty_join_remove_tags',  # noqa: E501
        'thirdparty_leave_add_tags': 'thirdparty_leave_add_tags',  # noqa: E501
        'thirdparty_leave_remove_tags': 'thirdparty_leave_remove_tags',  # noqa: E501
        'thirdparty_list_id': 'thirdparty_list_id',  # noqa: E501
        'thirdparty_provider_name': 'thirdparty_provider_name',  # noqa: E501
        'used_by': 'used_by',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EmailSegment - a model defined in OpenAPI

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
            allow_csv_download (bool): True if the current user has the rights to download this segment.. [optional]  # noqa: E501
            allow_facebook_audiences (bool): True if this StoreFront has the Facebook Analytics app connected and supports them. [optional]  # noqa: E501
            created_dts (str): Created date. [optional]  # noqa: E501
            deleted (bool): True if this campaign was deleted. [optional]  # noqa: E501
            email_segment_uuid (str): Email segment UUID. [optional]  # noqa: E501
            esp_list_segment_folder_uuid (str): List/Segment folder UUID. [optional]  # noqa: E501
            facebook_custom_audience (bool): True if you want to sync to a facebook custom audience. [optional]  # noqa: E501
            filter_profile_equation_json (str): File profile equation json. [optional]  # noqa: E501
            member_count (int): Count of members in this segment. [optional]  # noqa: E501
            merchant_id (str): Merchant ID. [optional]  # noqa: E501
            name (str): Name of email segment. [optional]  # noqa: E501
            rank_json (str): Rank settings json. [optional]  # noqa: E501
            rebuild_required (bool): True if a rebuild is required because some part of the segment has changed. [optional]  # noqa: E501
            storefront_oid (int): Storefront oid. [optional]  # noqa: E501
            thirdparty_join_add_tags ([str]): Third party provider tags to add when a customer joins the segment.. [optional]  # noqa: E501
            thirdparty_join_remove_tags ([str]): Third party provider tags to remove when a customer joins the segment.. [optional]  # noqa: E501
            thirdparty_leave_add_tags ([str]): Third party provider tags to add when a customer leaves the segment.. [optional]  # noqa: E501
            thirdparty_leave_remove_tags ([str]): Third party provider tags to remove when a customer leaves the segment.. [optional]  # noqa: E501
            thirdparty_list_id (str): List id of third party provider to sync with.. [optional]  # noqa: E501
            thirdparty_provider_name (str): Name of third party provider to sync segment to a list with.. [optional]  # noqa: E501
            used_by ([EmailListSegmentUsedBy]): Details on the flows or campaigns that use this list.. [optional]  # noqa: E501
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
        """EmailSegment - a model defined in OpenAPI

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
            allow_csv_download (bool): True if the current user has the rights to download this segment.. [optional]  # noqa: E501
            allow_facebook_audiences (bool): True if this StoreFront has the Facebook Analytics app connected and supports them. [optional]  # noqa: E501
            created_dts (str): Created date. [optional]  # noqa: E501
            deleted (bool): True if this campaign was deleted. [optional]  # noqa: E501
            email_segment_uuid (str): Email segment UUID. [optional]  # noqa: E501
            esp_list_segment_folder_uuid (str): List/Segment folder UUID. [optional]  # noqa: E501
            facebook_custom_audience (bool): True if you want to sync to a facebook custom audience. [optional]  # noqa: E501
            filter_profile_equation_json (str): File profile equation json. [optional]  # noqa: E501
            member_count (int): Count of members in this segment. [optional]  # noqa: E501
            merchant_id (str): Merchant ID. [optional]  # noqa: E501
            name (str): Name of email segment. [optional]  # noqa: E501
            rank_json (str): Rank settings json. [optional]  # noqa: E501
            rebuild_required (bool): True if a rebuild is required because some part of the segment has changed. [optional]  # noqa: E501
            storefront_oid (int): Storefront oid. [optional]  # noqa: E501
            thirdparty_join_add_tags ([str]): Third party provider tags to add when a customer joins the segment.. [optional]  # noqa: E501
            thirdparty_join_remove_tags ([str]): Third party provider tags to remove when a customer joins the segment.. [optional]  # noqa: E501
            thirdparty_leave_add_tags ([str]): Third party provider tags to add when a customer leaves the segment.. [optional]  # noqa: E501
            thirdparty_leave_remove_tags ([str]): Third party provider tags to remove when a customer leaves the segment.. [optional]  # noqa: E501
            thirdparty_list_id (str): List id of third party provider to sync with.. [optional]  # noqa: E501
            thirdparty_provider_name (str): Name of third party provider to sync segment to a list with.. [optional]  # noqa: E501
            used_by ([EmailListSegmentUsedBy]): Details on the flows or campaigns that use this list.. [optional]  # noqa: E501
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