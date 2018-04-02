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


class PricingTierNotification(object):
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
        'format': 'str',
        'subject': 'str',
        'text': 'str'
    }

    attribute_map = {
        'format': 'format',
        'subject': 'subject',
        'text': 'text'
    }

    def __init__(self, format=None, subject=None, text=None):
        """
        PricingTierNotification - a model defined in Swagger
        """

        self._format = None
        self._subject = None
        self._text = None
        self.discriminator = None

        if format is not None:
          self.format = format
        if subject is not None:
          self.subject = subject
        if text is not None:
          self.text = text

    @property
    def format(self):
        """
        Gets the format of this PricingTierNotification.
        Notification format

        :return: The format of this PricingTierNotification.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this PricingTierNotification.
        Notification format

        :param format: The format of this PricingTierNotification.
        :type: str
        """
        if format is not None and len(format) > 16:
            raise ValueError("Invalid value for `format`, length must be less than or equal to `16`")

        self._format = format

    @property
    def subject(self):
        """
        Gets the subject of this PricingTierNotification.
        Notification subject

        :return: The subject of this PricingTierNotification.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this PricingTierNotification.
        Notification subject

        :param subject: The subject of this PricingTierNotification.
        :type: str
        """
        if subject is not None and len(subject) > 100:
            raise ValueError("Invalid value for `subject`, length must be less than or equal to `100`")

        self._subject = subject

    @property
    def text(self):
        """
        Gets the text of this PricingTierNotification.
        Notification text

        :return: The text of this PricingTierNotification.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this PricingTierNotification.
        Notification text

        :param text: The text of this PricingTierNotification.
        :type: str
        """

        self._text = text

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
        if not isinstance(other, PricingTierNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
