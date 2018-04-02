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


class ItemInstantPaymentNotification(object):
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
        'post_operation': 'bool',
        'successful_response_text': 'str',
        'url': 'str'
    }

    attribute_map = {
        'post_operation': 'post_operation',
        'successful_response_text': 'successful_response_text',
        'url': 'url'
    }

    def __init__(self, post_operation=None, successful_response_text=None, url=None):
        """
        ItemInstantPaymentNotification - a model defined in Swagger
        """

        self._post_operation = None
        self._successful_response_text = None
        self._url = None
        self.discriminator = None

        if post_operation is not None:
          self.post_operation = post_operation
        if successful_response_text is not None:
          self.successful_response_text = successful_response_text
        if url is not None:
          self.url = url

    @property
    def post_operation(self):
        """
        Gets the post_operation of this ItemInstantPaymentNotification.
        True for HTTP POST instead of GET

        :return: The post_operation of this ItemInstantPaymentNotification.
        :rtype: bool
        """
        return self._post_operation

    @post_operation.setter
    def post_operation(self, post_operation):
        """
        Sets the post_operation of this ItemInstantPaymentNotification.
        True for HTTP POST instead of GET

        :param post_operation: The post_operation of this ItemInstantPaymentNotification.
        :type: bool
        """

        self._post_operation = post_operation

    @property
    def successful_response_text(self):
        """
        Gets the successful_response_text of this ItemInstantPaymentNotification.
        Successful response text

        :return: The successful_response_text of this ItemInstantPaymentNotification.
        :rtype: str
        """
        return self._successful_response_text

    @successful_response_text.setter
    def successful_response_text(self, successful_response_text):
        """
        Sets the successful_response_text of this ItemInstantPaymentNotification.
        Successful response text

        :param successful_response_text: The successful_response_text of this ItemInstantPaymentNotification.
        :type: str
        """
        if successful_response_text is not None and len(successful_response_text) > 1024:
            raise ValueError("Invalid value for `successful_response_text`, length must be less than or equal to `1024`")

        self._successful_response_text = successful_response_text

    @property
    def url(self):
        """
        Gets the url of this ItemInstantPaymentNotification.
        URL

        :return: The url of this ItemInstantPaymentNotification.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ItemInstantPaymentNotification.
        URL

        :param url: The url of this ItemInstantPaymentNotification.
        :type: str
        """
        if url is not None and len(url) > 1024:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `1024`")

        self._url = url

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
        if not isinstance(other, ItemInstantPaymentNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
