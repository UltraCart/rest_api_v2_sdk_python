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
    from ultracart.model.conversation_message_translation import ConversationMessageTranslation
    from ultracart.model.conversation_message_transport_status import ConversationMessageTransportStatus
    globals()['ConversationMessageTranslation'] = ConversationMessageTranslation
    globals()['ConversationMessageTransportStatus'] = ConversationMessageTransportStatus


class ConversationMessage(ModelNormal):
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
        ('type',): {
            'MESSAGE': "message",
            'NOTICE': "notice",
            'ENGAGEMENT_PROMPT': "engagement prompt",
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
            'author_conversation_participant_arn': (str,),  # noqa: E501
            'author_conversation_participant_name': (str,),  # noqa: E501
            'body': (str,),  # noqa: E501
            'client_message_id': (str,),  # noqa: E501
            'conversation_message_uuid': (str,),  # noqa: E501
            'delay_until_dts': (str,),  # noqa: E501
            'language_iso_code': (str,),  # noqa: E501
            'media_urls': ([str],),  # noqa: E501
            'merchant_id': (str,),  # noqa: E501
            'message_dts': (str,),  # noqa: E501
            'message_epoch': (int,),  # noqa: E501
            'translations': ([ConversationMessageTranslation],),  # noqa: E501
            'transport_statuses': ([ConversationMessageTransportStatus],),  # noqa: E501
            'type': (str,),  # noqa: E501
            'upload_keys': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'author_conversation_participant_arn': 'author_conversation_participant_arn',  # noqa: E501
        'author_conversation_participant_name': 'author_conversation_participant_name',  # noqa: E501
        'body': 'body',  # noqa: E501
        'client_message_id': 'client_message_id',  # noqa: E501
        'conversation_message_uuid': 'conversation_message_uuid',  # noqa: E501
        'delay_until_dts': 'delay_until_dts',  # noqa: E501
        'language_iso_code': 'language_iso_code',  # noqa: E501
        'media_urls': 'media_urls',  # noqa: E501
        'merchant_id': 'merchant_id',  # noqa: E501
        'message_dts': 'message_dts',  # noqa: E501
        'message_epoch': 'message_epoch',  # noqa: E501
        'translations': 'translations',  # noqa: E501
        'transport_statuses': 'transport_statuses',  # noqa: E501
        'type': 'type',  # noqa: E501
        'upload_keys': 'upload_keys',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ConversationMessage - a model defined in OpenAPI

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
            author_conversation_participant_arn (str): [optional]  # noqa: E501
            author_conversation_participant_name (str): [optional]  # noqa: E501
            body (str): [optional]  # noqa: E501
            client_message_id (str): [optional]  # noqa: E501
            conversation_message_uuid (str): [optional]  # noqa: E501
            delay_until_dts (str): Delay message transmission until date/time. [optional]  # noqa: E501
            language_iso_code (str): [optional]  # noqa: E501
            media_urls ([str]): [optional]  # noqa: E501
            merchant_id (str): [optional]  # noqa: E501
            message_dts (str): Message date/time. [optional]  # noqa: E501
            message_epoch (int): Message epoch milliseconds. [optional]  # noqa: E501
            translations ([ConversationMessageTranslation]): [optional]  # noqa: E501
            transport_statuses ([ConversationMessageTransportStatus]): [optional]  # noqa: E501
            type (str): Message type. [optional]  # noqa: E501
            upload_keys ([str]): [optional]  # noqa: E501
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
        """ConversationMessage - a model defined in OpenAPI

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
            author_conversation_participant_arn (str): [optional]  # noqa: E501
            author_conversation_participant_name (str): [optional]  # noqa: E501
            body (str): [optional]  # noqa: E501
            client_message_id (str): [optional]  # noqa: E501
            conversation_message_uuid (str): [optional]  # noqa: E501
            delay_until_dts (str): Delay message transmission until date/time. [optional]  # noqa: E501
            language_iso_code (str): [optional]  # noqa: E501
            media_urls ([str]): [optional]  # noqa: E501
            merchant_id (str): [optional]  # noqa: E501
            message_dts (str): Message date/time. [optional]  # noqa: E501
            message_epoch (int): Message epoch milliseconds. [optional]  # noqa: E501
            translations ([ConversationMessageTranslation]): [optional]  # noqa: E501
            transport_statuses ([ConversationMessageTransportStatus]): [optional]  # noqa: E501
            type (str): Message type. [optional]  # noqa: E501
            upload_keys ([str]): [optional]  # noqa: E501
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
