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
    from ultracart.model.conversation_pbx_queue_members import ConversationPbxQueueMembers
    globals()['ConversationPbxQueueMembers'] = ConversationPbxQueueMembers


class ConversationPbxQueue(ModelNormal):
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
        ('conversation_voicemail_mailbox_uuid',): {
            'max_length': 50,
        },
        ('hold_conversation_pbx_audio_uuid',): {
            'max_length': 50,
        },
        ('merchant_id',): {
            'max_length': 5,
        },
        ('name',): {
            'max_length': 50,
        },
        ('no_agent_available_play_audio_uuid',): {
            'max_length': 50,
        },
        ('no_agent_available_say_voice',): {
            'max_length': 50,
        },
        ('play_audio_uuid',): {
            'max_length': 50,
        },
        ('say_voice',): {
            'max_length': 50,
        },
        ('twilio_taskrouter_workflow_sid',): {
            'max_length': 100,
        },
        ('twilio_workspace_queue_sid',): {
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
            'announce_queue_position': (bool,),  # noqa: E501
            'conversation_pbx_queue_uuid': (str,),  # noqa: E501
            'conversation_voicemail_mailbox_uuid': (str,),  # noqa: E501
            'hold_conversation_pbx_audio_uuid': (str,),  # noqa: E501
            'max_hold_seconds': (int,),  # noqa: E501
            'members': (ConversationPbxQueueMembers,),  # noqa: E501
            'merchant_id': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'no_agent_available_play_audio_uuid': (str,),  # noqa: E501
            'no_agent_available_say': (str,),  # noqa: E501
            'no_agent_available_say_voice': (str,),  # noqa: E501
            'play_audio_uuid': (str,),  # noqa: E501
            'record_call': (bool,),  # noqa: E501
            'say': (str,),  # noqa: E501
            'say_voice': (str,),  # noqa: E501
            'twilio_taskrouter_workflow_sid': (str,),  # noqa: E501
            'twilio_workspace_queue_sid': (str,),  # noqa: E501
            'voicemail': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'announce_queue_position': 'announce_queue_position',  # noqa: E501
        'conversation_pbx_queue_uuid': 'conversation_pbx_queue_uuid',  # noqa: E501
        'conversation_voicemail_mailbox_uuid': 'conversation_voicemail_mailbox_uuid',  # noqa: E501
        'hold_conversation_pbx_audio_uuid': 'hold_conversation_pbx_audio_uuid',  # noqa: E501
        'max_hold_seconds': 'max_hold_seconds',  # noqa: E501
        'members': 'members',  # noqa: E501
        'merchant_id': 'merchant_id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'no_agent_available_play_audio_uuid': 'no_agent_available_play_audio_uuid',  # noqa: E501
        'no_agent_available_say': 'no_agent_available_say',  # noqa: E501
        'no_agent_available_say_voice': 'no_agent_available_say_voice',  # noqa: E501
        'play_audio_uuid': 'play_audio_uuid',  # noqa: E501
        'record_call': 'record_call',  # noqa: E501
        'say': 'say',  # noqa: E501
        'say_voice': 'say_voice',  # noqa: E501
        'twilio_taskrouter_workflow_sid': 'twilio_taskrouter_workflow_sid',  # noqa: E501
        'twilio_workspace_queue_sid': 'twilio_workspace_queue_sid',  # noqa: E501
        'voicemail': 'voicemail',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ConversationPbxQueue - a model defined in OpenAPI

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
            announce_queue_position (bool): If true, the customer is told their queue position upon entering the queue. [optional]  # noqa: E501
            conversation_pbx_queue_uuid (str): Conversation Pbx Queue unique identifier. [optional]  # noqa: E501
            conversation_voicemail_mailbox_uuid (str): The voicemail mailbox associated with this queue. [optional]  # noqa: E501
            hold_conversation_pbx_audio_uuid (str): The audio to play while holding in a queue. [optional]  # noqa: E501
            max_hold_seconds (int): The maximum number of seconds for a customer to hold in a queue. [optional]  # noqa: E501
            members (ConversationPbxQueueMembers): [optional]  # noqa: E501
            merchant_id (str): Merchant Id. [optional]  # noqa: E501
            name (str): Name of queue. [optional]  # noqa: E501
            no_agent_available_play_audio_uuid (str): When no agent is available after the max_hold_seconds, say this. [optional]  # noqa: E501
            no_agent_available_say (str): When no agent is available after the max_hold_seconds, say this. [optional]  # noqa: E501
            no_agent_available_say_voice (str): The type of voice used to say text when no agent is available. [optional]  # noqa: E501
            play_audio_uuid (str): Audio played when customer enters a queue. [optional]  # noqa: E501
            record_call (bool): If true, any calls in this queue are recorded. [optional]  # noqa: E501
            say (str): Say text when a customer enters queue. [optional]  # noqa: E501
            say_voice (str): The type of voice to use when say text is spoken. [optional]  # noqa: E501
            twilio_taskrouter_workflow_sid (str): Twilio taskrouter workflow sid. [optional]  # noqa: E501
            twilio_workspace_queue_sid (str): Twilio workspace queue sid. [optional]  # noqa: E501
            voicemail (bool): If true, this queue has a voicemail associated with it. [optional]  # noqa: E501
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
        """ConversationPbxQueue - a model defined in OpenAPI

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
            announce_queue_position (bool): If true, the customer is told their queue position upon entering the queue. [optional]  # noqa: E501
            conversation_pbx_queue_uuid (str): Conversation Pbx Queue unique identifier. [optional]  # noqa: E501
            conversation_voicemail_mailbox_uuid (str): The voicemail mailbox associated with this queue. [optional]  # noqa: E501
            hold_conversation_pbx_audio_uuid (str): The audio to play while holding in a queue. [optional]  # noqa: E501
            max_hold_seconds (int): The maximum number of seconds for a customer to hold in a queue. [optional]  # noqa: E501
            members (ConversationPbxQueueMembers): [optional]  # noqa: E501
            merchant_id (str): Merchant Id. [optional]  # noqa: E501
            name (str): Name of queue. [optional]  # noqa: E501
            no_agent_available_play_audio_uuid (str): When no agent is available after the max_hold_seconds, say this. [optional]  # noqa: E501
            no_agent_available_say (str): When no agent is available after the max_hold_seconds, say this. [optional]  # noqa: E501
            no_agent_available_say_voice (str): The type of voice used to say text when no agent is available. [optional]  # noqa: E501
            play_audio_uuid (str): Audio played when customer enters a queue. [optional]  # noqa: E501
            record_call (bool): If true, any calls in this queue are recorded. [optional]  # noqa: E501
            say (str): Say text when a customer enters queue. [optional]  # noqa: E501
            say_voice (str): The type of voice to use when say text is spoken. [optional]  # noqa: E501
            twilio_taskrouter_workflow_sid (str): Twilio taskrouter workflow sid. [optional]  # noqa: E501
            twilio_workspace_queue_sid (str): Twilio workspace queue sid. [optional]  # noqa: E501
            voicemail (bool): If true, this queue has a voicemail associated with it. [optional]  # noqa: E501
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