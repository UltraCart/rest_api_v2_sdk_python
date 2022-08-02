# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EmailCommseqSequenceTestRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'cart_id': 'str',
        'cart_item_ids': 'list[str]',
        'esp_commseq_uuid': 'str',
        'name': 'str',
        'order_id': 'str',
        'please_review': 'bool',
        'send_to_email': 'str',
        'send_to_logged_in_user': 'bool'
    }

    attribute_map = {
        'cart_id': 'cart_id',
        'cart_item_ids': 'cart_item_ids',
        'esp_commseq_uuid': 'esp_commseq_uuid',
        'name': 'name',
        'order_id': 'order_id',
        'please_review': 'please_review',
        'send_to_email': 'send_to_email',
        'send_to_logged_in_user': 'send_to_logged_in_user'
    }

    def __init__(self, cart_id=None, cart_item_ids=None, esp_commseq_uuid=None, name=None, order_id=None, please_review=None, send_to_email=None, send_to_logged_in_user=None):  # noqa: E501
        """EmailCommseqSequenceTestRequest - a model defined in Swagger"""  # noqa: E501

        self._cart_id = None
        self._cart_item_ids = None
        self._esp_commseq_uuid = None
        self._name = None
        self._order_id = None
        self._please_review = None
        self._send_to_email = None
        self._send_to_logged_in_user = None
        self.discriminator = None

        if cart_id is not None:
            self.cart_id = cart_id
        if cart_item_ids is not None:
            self.cart_item_ids = cart_item_ids
        if esp_commseq_uuid is not None:
            self.esp_commseq_uuid = esp_commseq_uuid
        if name is not None:
            self.name = name
        if order_id is not None:
            self.order_id = order_id
        if please_review is not None:
            self.please_review = please_review
        if send_to_email is not None:
            self.send_to_email = send_to_email
        if send_to_logged_in_user is not None:
            self.send_to_logged_in_user = send_to_logged_in_user

    @property
    def cart_id(self):
        """Gets the cart_id of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The cart_id of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._cart_id

    @cart_id.setter
    def cart_id(self, cart_id):
        """Sets the cart_id of this EmailCommseqSequenceTestRequest.


        :param cart_id: The cart_id of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._cart_id = cart_id

    @property
    def cart_item_ids(self):
        """Gets the cart_item_ids of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The cart_item_ids of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cart_item_ids

    @cart_item_ids.setter
    def cart_item_ids(self, cart_item_ids):
        """Sets the cart_item_ids of this EmailCommseqSequenceTestRequest.


        :param cart_item_ids: The cart_item_ids of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: list[str]
        """

        self._cart_item_ids = cart_item_ids

    @property
    def esp_commseq_uuid(self):
        """Gets the esp_commseq_uuid of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The esp_commseq_uuid of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._esp_commseq_uuid

    @esp_commseq_uuid.setter
    def esp_commseq_uuid(self, esp_commseq_uuid):
        """Sets the esp_commseq_uuid of this EmailCommseqSequenceTestRequest.


        :param esp_commseq_uuid: The esp_commseq_uuid of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._esp_commseq_uuid = esp_commseq_uuid

    @property
    def name(self):
        """Gets the name of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The name of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmailCommseqSequenceTestRequest.


        :param name: The name of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order_id(self):
        """Gets the order_id of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The order_id of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this EmailCommseqSequenceTestRequest.


        :param order_id: The order_id of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def please_review(self):
        """Gets the please_review of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The please_review of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: bool
        """
        return self._please_review

    @please_review.setter
    def please_review(self, please_review):
        """Sets the please_review of this EmailCommseqSequenceTestRequest.


        :param please_review: The please_review of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: bool
        """

        self._please_review = please_review

    @property
    def send_to_email(self):
        """Gets the send_to_email of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The send_to_email of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: str
        """
        return self._send_to_email

    @send_to_email.setter
    def send_to_email(self, send_to_email):
        """Sets the send_to_email of this EmailCommseqSequenceTestRequest.


        :param send_to_email: The send_to_email of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: str
        """

        self._send_to_email = send_to_email

    @property
    def send_to_logged_in_user(self):
        """Gets the send_to_logged_in_user of this EmailCommseqSequenceTestRequest.  # noqa: E501


        :return: The send_to_logged_in_user of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_to_logged_in_user

    @send_to_logged_in_user.setter
    def send_to_logged_in_user(self, send_to_logged_in_user):
        """Sets the send_to_logged_in_user of this EmailCommseqSequenceTestRequest.


        :param send_to_logged_in_user: The send_to_logged_in_user of this EmailCommseqSequenceTestRequest.  # noqa: E501
        :type: bool
        """

        self._send_to_logged_in_user = send_to_logged_in_user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(EmailCommseqSequenceTestRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EmailCommseqSequenceTestRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
