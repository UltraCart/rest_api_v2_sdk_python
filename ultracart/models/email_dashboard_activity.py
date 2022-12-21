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


class EmailDashboardActivity(object):
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
        'action': 'str',
        'activity_dts': 'str',
        'destination_name': 'str',
        'destination_uuid': 'str',
        'email': 'str',
        'is_list': 'bool',
        'is_segment': 'bool'
    }

    attribute_map = {
        'action': 'action',
        'activity_dts': 'activity_dts',
        'destination_name': 'destination_name',
        'destination_uuid': 'destination_uuid',
        'email': 'email',
        'is_list': 'is_list',
        'is_segment': 'is_segment'
    }

    def __init__(self, action=None, activity_dts=None, destination_name=None, destination_uuid=None, email=None, is_list=None, is_segment=None):  # noqa: E501
        """EmailDashboardActivity - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._activity_dts = None
        self._destination_name = None
        self._destination_uuid = None
        self._email = None
        self._is_list = None
        self._is_segment = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if activity_dts is not None:
            self.activity_dts = activity_dts
        if destination_name is not None:
            self.destination_name = destination_name
        if destination_uuid is not None:
            self.destination_uuid = destination_uuid
        if email is not None:
            self.email = email
        if is_list is not None:
            self.is_list = is_list
        if is_segment is not None:
            self.is_segment = is_segment

    @property
    def action(self):
        """Gets the action of this EmailDashboardActivity.  # noqa: E501

        Type of action such as add, remove, subscribe, unsubscribe  # noqa: E501

        :return: The action of this EmailDashboardActivity.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this EmailDashboardActivity.

        Type of action such as add, remove, subscribe, unsubscribe  # noqa: E501

        :param action: The action of this EmailDashboardActivity.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def activity_dts(self):
        """Gets the activity_dts of this EmailDashboardActivity.  # noqa: E501

        Date/time of the activity  # noqa: E501

        :return: The activity_dts of this EmailDashboardActivity.  # noqa: E501
        :rtype: str
        """
        return self._activity_dts

    @activity_dts.setter
    def activity_dts(self, activity_dts):
        """Sets the activity_dts of this EmailDashboardActivity.

        Date/time of the activity  # noqa: E501

        :param activity_dts: The activity_dts of this EmailDashboardActivity.  # noqa: E501
        :type: str
        """

        self._activity_dts = activity_dts

    @property
    def destination_name(self):
        """Gets the destination_name of this EmailDashboardActivity.  # noqa: E501

        List or segment name  # noqa: E501

        :return: The destination_name of this EmailDashboardActivity.  # noqa: E501
        :rtype: str
        """
        return self._destination_name

    @destination_name.setter
    def destination_name(self, destination_name):
        """Sets the destination_name of this EmailDashboardActivity.

        List or segment name  # noqa: E501

        :param destination_name: The destination_name of this EmailDashboardActivity.  # noqa: E501
        :type: str
        """

        self._destination_name = destination_name

    @property
    def destination_uuid(self):
        """Gets the destination_uuid of this EmailDashboardActivity.  # noqa: E501

        List or segment uuid  # noqa: E501

        :return: The destination_uuid of this EmailDashboardActivity.  # noqa: E501
        :rtype: str
        """
        return self._destination_uuid

    @destination_uuid.setter
    def destination_uuid(self, destination_uuid):
        """Sets the destination_uuid of this EmailDashboardActivity.

        List or segment uuid  # noqa: E501

        :param destination_uuid: The destination_uuid of this EmailDashboardActivity.  # noqa: E501
        :type: str
        """

        self._destination_uuid = destination_uuid

    @property
    def email(self):
        """Gets the email of this EmailDashboardActivity.  # noqa: E501

        Email address  # noqa: E501

        :return: The email of this EmailDashboardActivity.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EmailDashboardActivity.

        Email address  # noqa: E501

        :param email: The email of this EmailDashboardActivity.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def is_list(self):
        """Gets the is_list of this EmailDashboardActivity.  # noqa: E501

        true if activity is related to list  # noqa: E501

        :return: The is_list of this EmailDashboardActivity.  # noqa: E501
        :rtype: bool
        """
        return self._is_list

    @is_list.setter
    def is_list(self, is_list):
        """Sets the is_list of this EmailDashboardActivity.

        true if activity is related to list  # noqa: E501

        :param is_list: The is_list of this EmailDashboardActivity.  # noqa: E501
        :type: bool
        """

        self._is_list = is_list

    @property
    def is_segment(self):
        """Gets the is_segment of this EmailDashboardActivity.  # noqa: E501

        true if activity is related to segment  # noqa: E501

        :return: The is_segment of this EmailDashboardActivity.  # noqa: E501
        :rtype: bool
        """
        return self._is_segment

    @is_segment.setter
    def is_segment(self, is_segment):
        """Sets the is_segment of this EmailDashboardActivity.

        true if activity is related to segment  # noqa: E501

        :param is_segment: The is_segment of this EmailDashboardActivity.  # noqa: E501
        :type: bool
        """

        self._is_segment = is_segment

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
        if issubclass(EmailDashboardActivity, dict):
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
        if not isinstance(other, EmailDashboardActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other