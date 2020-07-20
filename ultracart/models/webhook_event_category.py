# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WebhookEventCategory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'any_subscribed': 'bool',
        'available_expansions': 'list[str]',
        'event_category': 'str',
        'events': 'list[WebhookEventSubscription]',
        'subscribed': 'bool'
    }

    attribute_map = {
        'any_subscribed': 'any_subscribed',
        'available_expansions': 'available_expansions',
        'event_category': 'event_category',
        'events': 'events',
        'subscribed': 'subscribed'
    }

    def __init__(self, any_subscribed=None, available_expansions=None, event_category=None, events=None, subscribed=None):
        """
        WebhookEventCategory - a model defined in Swagger
        """

        self._any_subscribed = None
        self._available_expansions = None
        self._event_category = None
        self._events = None
        self._subscribed = None
        self.discriminator = None

        if any_subscribed is not None:
          self.any_subscribed = any_subscribed
        if available_expansions is not None:
          self.available_expansions = available_expansions
        if event_category is not None:
          self.event_category = event_category
        if events is not None:
          self.events = events
        if subscribed is not None:
          self.subscribed = subscribed

    @property
    def any_subscribed(self):
        """
        Gets the any_subscribed of this WebhookEventCategory.
        True if any events are subscribed to.

        :return: The any_subscribed of this WebhookEventCategory.
        :rtype: bool
        """
        return self._any_subscribed

    @any_subscribed.setter
    def any_subscribed(self, any_subscribed):
        """
        Sets the any_subscribed of this WebhookEventCategory.
        True if any events are subscribed to.

        :param any_subscribed: The any_subscribed of this WebhookEventCategory.
        :type: bool
        """

        self._any_subscribed = any_subscribed

    @property
    def available_expansions(self):
        """
        Gets the available_expansions of this WebhookEventCategory.
        Array of available expansion constants

        :return: The available_expansions of this WebhookEventCategory.
        :rtype: list[str]
        """
        return self._available_expansions

    @available_expansions.setter
    def available_expansions(self, available_expansions):
        """
        Sets the available_expansions of this WebhookEventCategory.
        Array of available expansion constants

        :param available_expansions: The available_expansions of this WebhookEventCategory.
        :type: list[str]
        """

        self._available_expansions = available_expansions

    @property
    def event_category(self):
        """
        Gets the event_category of this WebhookEventCategory.
        Name of the event category

        :return: The event_category of this WebhookEventCategory.
        :rtype: str
        """
        return self._event_category

    @event_category.setter
    def event_category(self, event_category):
        """
        Sets the event_category of this WebhookEventCategory.
        Name of the event category

        :param event_category: The event_category of this WebhookEventCategory.
        :type: str
        """

        self._event_category = event_category

    @property
    def events(self):
        """
        Gets the events of this WebhookEventCategory.
        The events within the category.  Individual subscription flags contained within the child object.

        :return: The events of this WebhookEventCategory.
        :rtype: list[WebhookEventSubscription]
        """
        return self._events

    @events.setter
    def events(self, events):
        """
        Sets the events of this WebhookEventCategory.
        The events within the category.  Individual subscription flags contained within the child object.

        :param events: The events of this WebhookEventCategory.
        :type: list[WebhookEventSubscription]
        """

        self._events = events

    @property
    def subscribed(self):
        """
        Gets the subscribed of this WebhookEventCategory.
        True if all the events within this category are subscribed.  This is a convenience flag to make user interfaces easier.

        :return: The subscribed of this WebhookEventCategory.
        :rtype: bool
        """
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        """
        Sets the subscribed of this WebhookEventCategory.
        True if all the events within this category are subscribed.  This is a convenience flag to make user interfaces easier.

        :param subscribed: The subscribed of this WebhookEventCategory.
        :type: bool
        """

        self._subscribed = subscribed

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, WebhookEventCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
