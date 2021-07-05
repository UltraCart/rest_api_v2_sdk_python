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


class IntegrationLog(object):
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
        'direction': 'str',
        'email': 'str',
        'files': 'list[IntegrationLogFile]',
        'integration_log_oid': 'int',
        'item_id': 'str',
        'item_ipn_oid': 'int',
        'log_dts': 'str',
        'log_type': 'str',
        'logger_id': 'str',
        'logger_name': 'str',
        'logs': 'list[IntegrationLogLog]',
        'omit_log_map': 'bool',
        'order_ids': 'list[str]',
        'pk': 'str',
        'sk': 'str',
        'status': 'str',
        'status_code': 'int'
    }

    attribute_map = {
        'action': 'action',
        'direction': 'direction',
        'email': 'email',
        'files': 'files',
        'integration_log_oid': 'integration_log_oid',
        'item_id': 'item_id',
        'item_ipn_oid': 'item_ipn_oid',
        'log_dts': 'log_dts',
        'log_type': 'log_type',
        'logger_id': 'logger_id',
        'logger_name': 'logger_name',
        'logs': 'logs',
        'omit_log_map': 'omit_log_map',
        'order_ids': 'order_ids',
        'pk': 'pk',
        'sk': 'sk',
        'status': 'status',
        'status_code': 'status_code'
    }

    def __init__(self, action=None, direction=None, email=None, files=None, integration_log_oid=None, item_id=None, item_ipn_oid=None, log_dts=None, log_type=None, logger_id=None, logger_name=None, logs=None, omit_log_map=None, order_ids=None, pk=None, sk=None, status=None, status_code=None):  # noqa: E501
        """IntegrationLog - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._direction = None
        self._email = None
        self._files = None
        self._integration_log_oid = None
        self._item_id = None
        self._item_ipn_oid = None
        self._log_dts = None
        self._log_type = None
        self._logger_id = None
        self._logger_name = None
        self._logs = None
        self._omit_log_map = None
        self._order_ids = None
        self._pk = None
        self._sk = None
        self._status = None
        self._status_code = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if direction is not None:
            self.direction = direction
        if email is not None:
            self.email = email
        if files is not None:
            self.files = files
        if integration_log_oid is not None:
            self.integration_log_oid = integration_log_oid
        if item_id is not None:
            self.item_id = item_id
        if item_ipn_oid is not None:
            self.item_ipn_oid = item_ipn_oid
        if log_dts is not None:
            self.log_dts = log_dts
        if log_type is not None:
            self.log_type = log_type
        if logger_id is not None:
            self.logger_id = logger_id
        if logger_name is not None:
            self.logger_name = logger_name
        if logs is not None:
            self.logs = logs
        if omit_log_map is not None:
            self.omit_log_map = omit_log_map
        if order_ids is not None:
            self.order_ids = order_ids
        if pk is not None:
            self.pk = pk
        if sk is not None:
            self.sk = sk
        if status is not None:
            self.status = status
        if status_code is not None:
            self.status_code = status_code

    @property
    def action(self):
        """Gets the action of this IntegrationLog.  # noqa: E501


        :return: The action of this IntegrationLog.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this IntegrationLog.


        :param action: The action of this IntegrationLog.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def direction(self):
        """Gets the direction of this IntegrationLog.  # noqa: E501


        :return: The direction of this IntegrationLog.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this IntegrationLog.


        :param direction: The direction of this IntegrationLog.  # noqa: E501
        :type: str
        """

        self._direction = direction

    @property
    def email(self):
        """Gets the email of this IntegrationLog.  # noqa: E501


        :return: The email of this IntegrationLog.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this IntegrationLog.


        :param email: The email of this IntegrationLog.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def files(self):
        """Gets the files of this IntegrationLog.  # noqa: E501


        :return: The files of this IntegrationLog.  # noqa: E501
        :rtype: list[IntegrationLogFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this IntegrationLog.


        :param files: The files of this IntegrationLog.  # noqa: E501
        :type: list[IntegrationLogFile]
        """

        self._files = files

    @property
    def integration_log_oid(self):
        """Gets the integration_log_oid of this IntegrationLog.  # noqa: E501


        :return: The integration_log_oid of this IntegrationLog.  # noqa: E501
        :rtype: int
        """
        return self._integration_log_oid

    @integration_log_oid.setter
    def integration_log_oid(self, integration_log_oid):
        """Sets the integration_log_oid of this IntegrationLog.


        :param integration_log_oid: The integration_log_oid of this IntegrationLog.  # noqa: E501
        :type: int
        """

        self._integration_log_oid = integration_log_oid

    @property
    def item_id(self):
        """Gets the item_id of this IntegrationLog.  # noqa: E501


        :return: The item_id of this IntegrationLog.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this IntegrationLog.


        :param item_id: The item_id of this IntegrationLog.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def item_ipn_oid(self):
        """Gets the item_ipn_oid of this IntegrationLog.  # noqa: E501


        :return: The item_ipn_oid of this IntegrationLog.  # noqa: E501
        :rtype: int
        """
        return self._item_ipn_oid

    @item_ipn_oid.setter
    def item_ipn_oid(self, item_ipn_oid):
        """Sets the item_ipn_oid of this IntegrationLog.


        :param item_ipn_oid: The item_ipn_oid of this IntegrationLog.  # noqa: E501
        :type: int
        """

        self._item_ipn_oid = item_ipn_oid

    @property
    def log_dts(self):
        """Gets the log_dts of this IntegrationLog.  # noqa: E501


        :return: The log_dts of this IntegrationLog.  # noqa: E501
        :rtype: str
        """
        return self._log_dts

    @log_dts.setter
    def log_dts(self, log_dts):
        """Sets the log_dts of this IntegrationLog.


        :param log_dts: The log_dts of this IntegrationLog.  # noqa: E501
        :type: str
        """

        self._log_dts = log_dts

    @property
    def log_type(self):
        """Gets the log_type of this IntegrationLog.  # noqa: E501


        :return: The log_type of this IntegrationLog.  # noqa: E501
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """Sets the log_type of this IntegrationLog.


        :param log_type: The log_type of this IntegrationLog.  # noqa: E501
        :type: str
        """

        self._log_type = log_type

    @property
    def logger_id(self):
        """Gets the logger_id of this IntegrationLog.  # noqa: E501


        :return: The logger_id of this IntegrationLog.  # noqa: E501
        :rtype: str
        """
        return self._logger_id

    @logger_id.setter
    def logger_id(self, logger_id):
        """Sets the logger_id of this IntegrationLog.


        :param logger_id: The logger_id of this IntegrationLog.  # noqa: E501
        :type: str
        """

        self._logger_id = logger_id

    @property
    def logger_name(self):
        """Gets the logger_name of this IntegrationLog.  # noqa: E501


        :return: The logger_name of this IntegrationLog.  # noqa: E501
        :rtype: str
        """
        return self._logger_name

    @logger_name.setter
    def logger_name(self, logger_name):
        """Sets the logger_name of this IntegrationLog.


        :param logger_name: The logger_name of this IntegrationLog.  # noqa: E501
        :type: str
        """

        self._logger_name = logger_name

    @property
    def logs(self):
        """Gets the logs of this IntegrationLog.  # noqa: E501


        :return: The logs of this IntegrationLog.  # noqa: E501
        :rtype: list[IntegrationLogLog]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this IntegrationLog.


        :param logs: The logs of this IntegrationLog.  # noqa: E501
        :type: list[IntegrationLogLog]
        """

        self._logs = logs

    @property
    def omit_log_map(self):
        """Gets the omit_log_map of this IntegrationLog.  # noqa: E501


        :return: The omit_log_map of this IntegrationLog.  # noqa: E501
        :rtype: bool
        """
        return self._omit_log_map

    @omit_log_map.setter
    def omit_log_map(self, omit_log_map):
        """Sets the omit_log_map of this IntegrationLog.


        :param omit_log_map: The omit_log_map of this IntegrationLog.  # noqa: E501
        :type: bool
        """

        self._omit_log_map = omit_log_map

    @property
    def order_ids(self):
        """Gets the order_ids of this IntegrationLog.  # noqa: E501


        :return: The order_ids of this IntegrationLog.  # noqa: E501
        :rtype: list[str]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        """Sets the order_ids of this IntegrationLog.


        :param order_ids: The order_ids of this IntegrationLog.  # noqa: E501
        :type: list[str]
        """

        self._order_ids = order_ids

    @property
    def pk(self):
        """Gets the pk of this IntegrationLog.  # noqa: E501


        :return: The pk of this IntegrationLog.  # noqa: E501
        :rtype: str
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this IntegrationLog.


        :param pk: The pk of this IntegrationLog.  # noqa: E501
        :type: str
        """

        self._pk = pk

    @property
    def sk(self):
        """Gets the sk of this IntegrationLog.  # noqa: E501


        :return: The sk of this IntegrationLog.  # noqa: E501
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this IntegrationLog.


        :param sk: The sk of this IntegrationLog.  # noqa: E501
        :type: str
        """

        self._sk = sk

    @property
    def status(self):
        """Gets the status of this IntegrationLog.  # noqa: E501


        :return: The status of this IntegrationLog.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IntegrationLog.


        :param status: The status of this IntegrationLog.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_code(self):
        """Gets the status_code of this IntegrationLog.  # noqa: E501


        :return: The status_code of this IntegrationLog.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this IntegrationLog.


        :param status_code: The status_code of this IntegrationLog.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

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
        if issubclass(IntegrationLog, dict):
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
        if not isinstance(other, IntegrationLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
