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
    from ultracart.model.conversation_event_add_coupon import ConversationEventAddCoupon
    from ultracart.model.conversation_event_add_item import ConversationEventAddItem
    from ultracart.model.conversation_event_queue_position import ConversationEventQueuePosition
    from ultracart.model.conversation_event_read_message import ConversationEventReadMessage
    from ultracart.model.conversation_event_rr_web import ConversationEventRRWeb
    from ultracart.model.conversation_event_typing import ConversationEventTyping
    from ultracart.model.conversation_event_webchat_context import ConversationEventWebchatContext
    from ultracart.model.conversation_message import ConversationMessage
    from ultracart.model.conversation_participant import ConversationParticipant
    from ultracart.model.conversation_summary import ConversationSummary
    from ultracart.model.conversation_webchat_queue_status import ConversationWebchatQueueStatus
    from ultracart.model.conversation_webchat_queue_status_queue_entry import ConversationWebchatQueueStatusQueueEntry
    globals()['ConversationEventAddCoupon'] = ConversationEventAddCoupon
    globals()['ConversationEventAddItem'] = ConversationEventAddItem
    globals()['ConversationEventQueuePosition'] = ConversationEventQueuePosition
    globals()['ConversationEventRRWeb'] = ConversationEventRRWeb
    globals()['ConversationEventReadMessage'] = ConversationEventReadMessage
    globals()['ConversationEventTyping'] = ConversationEventTyping
    globals()['ConversationEventWebchatContext'] = ConversationEventWebchatContext
    globals()['ConversationMessage'] = ConversationMessage
    globals()['ConversationParticipant'] = ConversationParticipant
    globals()['ConversationSummary'] = ConversationSummary
    globals()['ConversationWebchatQueueStatus'] = ConversationWebchatQueueStatus
    globals()['ConversationWebchatQueueStatusQueueEntry'] = ConversationWebchatQueueStatusQueueEntry


class ConversationWebsocketMessage(ModelNormal):
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
        ('event_type',): {
            'QUEUE_POSITION': "queue position",
            'WEBCHAT_START_CONVERSATION': "webchat start conversation",
            'CONVERSATION_CLOSED': "conversation closed",
            'NEW_CONVERSATION': "new conversation",
            'NEW_MESSAGE': "new message",
            'UPDATED_MESSAGE': "updated message",
            'QUEUE_STATUS_UPDATE': "queue status update",
            'RRWEB': "rrweb",
            'PARTICIPANT_UPDATE': "participant update",
            'PARTICIPANT_JOIN': "participant join",
            'PARTICIPANT_LEFT': "participant left",
            'READ_MESSAGE': "read message",
            'TYPING': "typing",
            'ADD_COUPON': "add coupon",
            'ADD_ITEM': "add item",
            'WEBCHAT_CONTEXT': "webchat context",
            'ENGAGE_CUSTOMER': "engage customer",
            'QUEUE_NEW_MEMBER': "queue new member",
        },
        ('type',): {
            'MESSAGE': "message",
            'EVENT': "event",
            'PING': "ping",
            'CHECK_QUEUE_POSITION': "check queue position",
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
            'conversation_arn': (str,),  # noqa: E501
            'conversation_uuid': (str,),  # noqa: E501
            'event_add_coupon': (ConversationEventAddCoupon,),  # noqa: E501
            'event_add_item': (ConversationEventAddItem,),  # noqa: E501
            'event_conversation_closed': (ConversationSummary,),  # noqa: E501
            'event_engage_customer': (ConversationWebchatQueueStatusQueueEntry,),  # noqa: E501
            'event_new_conversation': (ConversationSummary,),  # noqa: E501
            'event_new_message': (ConversationSummary,),  # noqa: E501
            'event_participant_join': (ConversationSummary,),  # noqa: E501
            'event_participant_join_participant': (ConversationParticipant,),  # noqa: E501
            'event_participant_left': (ConversationSummary,),  # noqa: E501
            'event_participant_left_participant': (ConversationParticipant,),  # noqa: E501
            'event_participant_update': (ConversationSummary,),  # noqa: E501
            'event_queue_new_member': (ConversationWebchatQueueStatusQueueEntry,),  # noqa: E501
            'event_queue_position': (ConversationEventQueuePosition,),  # noqa: E501
            'event_queue_status_update': (ConversationWebchatQueueStatus,),  # noqa: E501
            'event_read_message': (ConversationEventReadMessage,),  # noqa: E501
            'event_rrweb': (ConversationEventRRWeb,),  # noqa: E501
            'event_type': (str,),  # noqa: E501
            'event_typing': (ConversationEventTyping,),  # noqa: E501
            'event_updated_message': (ConversationMessage,),  # noqa: E501
            'event_webchat_context': (ConversationEventWebchatContext,),  # noqa: E501
            'message': (ConversationMessage,),  # noqa: E501
            'type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'conversation_arn': 'conversation_arn',  # noqa: E501
        'conversation_uuid': 'conversation_uuid',  # noqa: E501
        'event_add_coupon': 'event_add_coupon',  # noqa: E501
        'event_add_item': 'event_add_item',  # noqa: E501
        'event_conversation_closed': 'event_conversation_closed',  # noqa: E501
        'event_engage_customer': 'event_engage_customer',  # noqa: E501
        'event_new_conversation': 'event_new_conversation',  # noqa: E501
        'event_new_message': 'event_new_message',  # noqa: E501
        'event_participant_join': 'event_participant_join',  # noqa: E501
        'event_participant_join_participant': 'event_participant_join_participant',  # noqa: E501
        'event_participant_left': 'event_participant_left',  # noqa: E501
        'event_participant_left_participant': 'event_participant_left_participant',  # noqa: E501
        'event_participant_update': 'event_participant_update',  # noqa: E501
        'event_queue_new_member': 'event_queue_new_member',  # noqa: E501
        'event_queue_position': 'event_queue_position',  # noqa: E501
        'event_queue_status_update': 'event_queue_status_update',  # noqa: E501
        'event_read_message': 'event_read_message',  # noqa: E501
        'event_rrweb': 'event_rrweb',  # noqa: E501
        'event_type': 'event_type',  # noqa: E501
        'event_typing': 'event_typing',  # noqa: E501
        'event_updated_message': 'event_updated_message',  # noqa: E501
        'event_webchat_context': 'event_webchat_context',  # noqa: E501
        'message': 'message',  # noqa: E501
        'type': 'type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ConversationWebsocketMessage - a model defined in OpenAPI

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
            conversation_arn (str): Conversation ARN. [optional]  # noqa: E501
            conversation_uuid (str): Conversation UUID if the websocket message is tied to a specific conversation. [optional]  # noqa: E501
            event_add_coupon (ConversationEventAddCoupon): [optional]  # noqa: E501
            event_add_item (ConversationEventAddItem): [optional]  # noqa: E501
            event_conversation_closed (ConversationSummary): [optional]  # noqa: E501
            event_engage_customer (ConversationWebchatQueueStatusQueueEntry): [optional]  # noqa: E501
            event_new_conversation (ConversationSummary): [optional]  # noqa: E501
            event_new_message (ConversationSummary): [optional]  # noqa: E501
            event_participant_join (ConversationSummary): [optional]  # noqa: E501
            event_participant_join_participant (ConversationParticipant): [optional]  # noqa: E501
            event_participant_left (ConversationSummary): [optional]  # noqa: E501
            event_participant_left_participant (ConversationParticipant): [optional]  # noqa: E501
            event_participant_update (ConversationSummary): [optional]  # noqa: E501
            event_queue_new_member (ConversationWebchatQueueStatusQueueEntry): [optional]  # noqa: E501
            event_queue_position (ConversationEventQueuePosition): [optional]  # noqa: E501
            event_queue_status_update (ConversationWebchatQueueStatus): [optional]  # noqa: E501
            event_read_message (ConversationEventReadMessage): [optional]  # noqa: E501
            event_rrweb (ConversationEventRRWeb): [optional]  # noqa: E501
            event_type (str): Type of event. [optional]  # noqa: E501
            event_typing (ConversationEventTyping): [optional]  # noqa: E501
            event_updated_message (ConversationMessage): [optional]  # noqa: E501
            event_webchat_context (ConversationEventWebchatContext): [optional]  # noqa: E501
            message (ConversationMessage): [optional]  # noqa: E501
            type (str): Type of message. [optional]  # noqa: E501
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
        """ConversationWebsocketMessage - a model defined in OpenAPI

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
            conversation_arn (str): Conversation ARN. [optional]  # noqa: E501
            conversation_uuid (str): Conversation UUID if the websocket message is tied to a specific conversation. [optional]  # noqa: E501
            event_add_coupon (ConversationEventAddCoupon): [optional]  # noqa: E501
            event_add_item (ConversationEventAddItem): [optional]  # noqa: E501
            event_conversation_closed (ConversationSummary): [optional]  # noqa: E501
            event_engage_customer (ConversationWebchatQueueStatusQueueEntry): [optional]  # noqa: E501
            event_new_conversation (ConversationSummary): [optional]  # noqa: E501
            event_new_message (ConversationSummary): [optional]  # noqa: E501
            event_participant_join (ConversationSummary): [optional]  # noqa: E501
            event_participant_join_participant (ConversationParticipant): [optional]  # noqa: E501
            event_participant_left (ConversationSummary): [optional]  # noqa: E501
            event_participant_left_participant (ConversationParticipant): [optional]  # noqa: E501
            event_participant_update (ConversationSummary): [optional]  # noqa: E501
            event_queue_new_member (ConversationWebchatQueueStatusQueueEntry): [optional]  # noqa: E501
            event_queue_position (ConversationEventQueuePosition): [optional]  # noqa: E501
            event_queue_status_update (ConversationWebchatQueueStatus): [optional]  # noqa: E501
            event_read_message (ConversationEventReadMessage): [optional]  # noqa: E501
            event_rrweb (ConversationEventRRWeb): [optional]  # noqa: E501
            event_type (str): Type of event. [optional]  # noqa: E501
            event_typing (ConversationEventTyping): [optional]  # noqa: E501
            event_updated_message (ConversationMessage): [optional]  # noqa: E501
            event_webchat_context (ConversationEventWebchatContext): [optional]  # noqa: E501
            message (ConversationMessage): [optional]  # noqa: E501
            type (str): Type of message. [optional]  # noqa: E501
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
