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


class WorkflowTasksRequest(object):
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
        'assigned_to_group': 'str',
        'assigned_to_group_id': 'int',
        'assigned_to_me': 'bool',
        'assigned_to_user': 'str',
        'assigned_to_user_id': 'int',
        'created_by': 'WorkflowUser',
        'created_dts_begin': 'str',
        'created_dts_end': 'str',
        'delay_until_dts_begin': 'str',
        'delay_until_dts_end': 'str',
        'due_dts_begin': 'str',
        'due_dts_end': 'str',
        'last_update_dts_begin': 'str',
        'last_update_dts_end': 'str',
        'object_email': 'str',
        'object_type': 'str',
        'priority': 'str',
        'status': 'str',
        'tags': 'list[str]',
        'unassigned': 'bool'
    }

    attribute_map = {
        'assigned_to_group': 'assigned_to_group',
        'assigned_to_group_id': 'assigned_to_group_id',
        'assigned_to_me': 'assigned_to_me',
        'assigned_to_user': 'assigned_to_user',
        'assigned_to_user_id': 'assigned_to_user_id',
        'created_by': 'created_by',
        'created_dts_begin': 'created_dts_begin',
        'created_dts_end': 'created_dts_end',
        'delay_until_dts_begin': 'delay_until_dts_begin',
        'delay_until_dts_end': 'delay_until_dts_end',
        'due_dts_begin': 'due_dts_begin',
        'due_dts_end': 'due_dts_end',
        'last_update_dts_begin': 'last_update_dts_begin',
        'last_update_dts_end': 'last_update_dts_end',
        'object_email': 'object_email',
        'object_type': 'object_type',
        'priority': 'priority',
        'status': 'status',
        'tags': 'tags',
        'unassigned': 'unassigned'
    }

    def __init__(self, assigned_to_group=None, assigned_to_group_id=None, assigned_to_me=None, assigned_to_user=None, assigned_to_user_id=None, created_by=None, created_dts_begin=None, created_dts_end=None, delay_until_dts_begin=None, delay_until_dts_end=None, due_dts_begin=None, due_dts_end=None, last_update_dts_begin=None, last_update_dts_end=None, object_email=None, object_type=None, priority=None, status=None, tags=None, unassigned=None):  # noqa: E501
        """WorkflowTasksRequest - a model defined in Swagger"""  # noqa: E501

        self._assigned_to_group = None
        self._assigned_to_group_id = None
        self._assigned_to_me = None
        self._assigned_to_user = None
        self._assigned_to_user_id = None
        self._created_by = None
        self._created_dts_begin = None
        self._created_dts_end = None
        self._delay_until_dts_begin = None
        self._delay_until_dts_end = None
        self._due_dts_begin = None
        self._due_dts_end = None
        self._last_update_dts_begin = None
        self._last_update_dts_end = None
        self._object_email = None
        self._object_type = None
        self._priority = None
        self._status = None
        self._tags = None
        self._unassigned = None
        self.discriminator = None

        if assigned_to_group is not None:
            self.assigned_to_group = assigned_to_group
        if assigned_to_group_id is not None:
            self.assigned_to_group_id = assigned_to_group_id
        if assigned_to_me is not None:
            self.assigned_to_me = assigned_to_me
        if assigned_to_user is not None:
            self.assigned_to_user = assigned_to_user
        if assigned_to_user_id is not None:
            self.assigned_to_user_id = assigned_to_user_id
        if created_by is not None:
            self.created_by = created_by
        if created_dts_begin is not None:
            self.created_dts_begin = created_dts_begin
        if created_dts_end is not None:
            self.created_dts_end = created_dts_end
        if delay_until_dts_begin is not None:
            self.delay_until_dts_begin = delay_until_dts_begin
        if delay_until_dts_end is not None:
            self.delay_until_dts_end = delay_until_dts_end
        if due_dts_begin is not None:
            self.due_dts_begin = due_dts_begin
        if due_dts_end is not None:
            self.due_dts_end = due_dts_end
        if last_update_dts_begin is not None:
            self.last_update_dts_begin = last_update_dts_begin
        if last_update_dts_end is not None:
            self.last_update_dts_end = last_update_dts_end
        if object_email is not None:
            self.object_email = object_email
        if object_type is not None:
            self.object_type = object_type
        if priority is not None:
            self.priority = priority
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if unassigned is not None:
            self.unassigned = unassigned

    @property
    def assigned_to_group(self):
        """Gets the assigned_to_group of this WorkflowTasksRequest.  # noqa: E501

        Assigned to group  # noqa: E501

        :return: The assigned_to_group of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._assigned_to_group

    @assigned_to_group.setter
    def assigned_to_group(self, assigned_to_group):
        """Sets the assigned_to_group of this WorkflowTasksRequest.

        Assigned to group  # noqa: E501

        :param assigned_to_group: The assigned_to_group of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """

        self._assigned_to_group = assigned_to_group

    @property
    def assigned_to_group_id(self):
        """Gets the assigned_to_group_id of this WorkflowTasksRequest.  # noqa: E501

        Assigned to group ID  # noqa: E501

        :return: The assigned_to_group_id of this WorkflowTasksRequest.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to_group_id

    @assigned_to_group_id.setter
    def assigned_to_group_id(self, assigned_to_group_id):
        """Sets the assigned_to_group_id of this WorkflowTasksRequest.

        Assigned to group ID  # noqa: E501

        :param assigned_to_group_id: The assigned_to_group_id of this WorkflowTasksRequest.  # noqa: E501
        :type: int
        """

        self._assigned_to_group_id = assigned_to_group_id

    @property
    def assigned_to_me(self):
        """Gets the assigned_to_me of this WorkflowTasksRequest.  # noqa: E501

        Tasks are assigned to me either by direct user id or a group that the user is a member of  # noqa: E501

        :return: The assigned_to_me of this WorkflowTasksRequest.  # noqa: E501
        :rtype: bool
        """
        return self._assigned_to_me

    @assigned_to_me.setter
    def assigned_to_me(self, assigned_to_me):
        """Sets the assigned_to_me of this WorkflowTasksRequest.

        Tasks are assigned to me either by direct user id or a group that the user is a member of  # noqa: E501

        :param assigned_to_me: The assigned_to_me of this WorkflowTasksRequest.  # noqa: E501
        :type: bool
        """

        self._assigned_to_me = assigned_to_me

    @property
    def assigned_to_user(self):
        """Gets the assigned_to_user of this WorkflowTasksRequest.  # noqa: E501

        Assigned to user  # noqa: E501

        :return: The assigned_to_user of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._assigned_to_user

    @assigned_to_user.setter
    def assigned_to_user(self, assigned_to_user):
        """Sets the assigned_to_user of this WorkflowTasksRequest.

        Assigned to user  # noqa: E501

        :param assigned_to_user: The assigned_to_user of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """

        self._assigned_to_user = assigned_to_user

    @property
    def assigned_to_user_id(self):
        """Gets the assigned_to_user_id of this WorkflowTasksRequest.  # noqa: E501

        Assigned to user ID  # noqa: E501

        :return: The assigned_to_user_id of this WorkflowTasksRequest.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to_user_id

    @assigned_to_user_id.setter
    def assigned_to_user_id(self, assigned_to_user_id):
        """Sets the assigned_to_user_id of this WorkflowTasksRequest.

        Assigned to user ID  # noqa: E501

        :param assigned_to_user_id: The assigned_to_user_id of this WorkflowTasksRequest.  # noqa: E501
        :type: int
        """

        self._assigned_to_user_id = assigned_to_user_id

    @property
    def created_by(self):
        """Gets the created_by of this WorkflowTasksRequest.  # noqa: E501


        :return: The created_by of this WorkflowTasksRequest.  # noqa: E501
        :rtype: WorkflowUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this WorkflowTasksRequest.


        :param created_by: The created_by of this WorkflowTasksRequest.  # noqa: E501
        :type: WorkflowUser
        """

        self._created_by = created_by

    @property
    def created_dts_begin(self):
        """Gets the created_dts_begin of this WorkflowTasksRequest.  # noqa: E501

        Date/time that the workflow task was created  # noqa: E501

        :return: The created_dts_begin of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._created_dts_begin

    @created_dts_begin.setter
    def created_dts_begin(self, created_dts_begin):
        """Sets the created_dts_begin of this WorkflowTasksRequest.

        Date/time that the workflow task was created  # noqa: E501

        :param created_dts_begin: The created_dts_begin of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """

        self._created_dts_begin = created_dts_begin

    @property
    def created_dts_end(self):
        """Gets the created_dts_end of this WorkflowTasksRequest.  # noqa: E501

        Date/time that the workflow task was created  # noqa: E501

        :return: The created_dts_end of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._created_dts_end

    @created_dts_end.setter
    def created_dts_end(self, created_dts_end):
        """Sets the created_dts_end of this WorkflowTasksRequest.

        Date/time that the workflow task was created  # noqa: E501

        :param created_dts_end: The created_dts_end of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """

        self._created_dts_end = created_dts_end

    @property
    def delay_until_dts_begin(self):
        """Gets the delay_until_dts_begin of this WorkflowTasksRequest.  # noqa: E501

        Date/time that the workflow task should delay until  # noqa: E501

        :return: The delay_until_dts_begin of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._delay_until_dts_begin

    @delay_until_dts_begin.setter
    def delay_until_dts_begin(self, delay_until_dts_begin):
        """Sets the delay_until_dts_begin of this WorkflowTasksRequest.

        Date/time that the workflow task should delay until  # noqa: E501

        :param delay_until_dts_begin: The delay_until_dts_begin of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """

        self._delay_until_dts_begin = delay_until_dts_begin

    @property
    def delay_until_dts_end(self):
        """Gets the delay_until_dts_end of this WorkflowTasksRequest.  # noqa: E501

        Date/time that the workflow task should delay until  # noqa: E501

        :return: The delay_until_dts_end of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._delay_until_dts_end

    @delay_until_dts_end.setter
    def delay_until_dts_end(self, delay_until_dts_end):
        """Sets the delay_until_dts_end of this WorkflowTasksRequest.

        Date/time that the workflow task should delay until  # noqa: E501

        :param delay_until_dts_end: The delay_until_dts_end of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """

        self._delay_until_dts_end = delay_until_dts_end

    @property
    def due_dts_begin(self):
        """Gets the due_dts_begin of this WorkflowTasksRequest.  # noqa: E501

        Date/time that the workflow task is due  # noqa: E501

        :return: The due_dts_begin of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._due_dts_begin

    @due_dts_begin.setter
    def due_dts_begin(self, due_dts_begin):
        """Sets the due_dts_begin of this WorkflowTasksRequest.

        Date/time that the workflow task is due  # noqa: E501

        :param due_dts_begin: The due_dts_begin of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """

        self._due_dts_begin = due_dts_begin

    @property
    def due_dts_end(self):
        """Gets the due_dts_end of this WorkflowTasksRequest.  # noqa: E501

        Date/time that the workflow task is due  # noqa: E501

        :return: The due_dts_end of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._due_dts_end

    @due_dts_end.setter
    def due_dts_end(self, due_dts_end):
        """Sets the due_dts_end of this WorkflowTasksRequest.

        Date/time that the workflow task is due  # noqa: E501

        :param due_dts_end: The due_dts_end of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """

        self._due_dts_end = due_dts_end

    @property
    def last_update_dts_begin(self):
        """Gets the last_update_dts_begin of this WorkflowTasksRequest.  # noqa: E501

        Date/time that the workflow task was last updated  # noqa: E501

        :return: The last_update_dts_begin of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_update_dts_begin

    @last_update_dts_begin.setter
    def last_update_dts_begin(self, last_update_dts_begin):
        """Sets the last_update_dts_begin of this WorkflowTasksRequest.

        Date/time that the workflow task was last updated  # noqa: E501

        :param last_update_dts_begin: The last_update_dts_begin of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """

        self._last_update_dts_begin = last_update_dts_begin

    @property
    def last_update_dts_end(self):
        """Gets the last_update_dts_end of this WorkflowTasksRequest.  # noqa: E501

        Date/time that the workflow task was last updated  # noqa: E501

        :return: The last_update_dts_end of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_update_dts_end

    @last_update_dts_end.setter
    def last_update_dts_end(self, last_update_dts_end):
        """Sets the last_update_dts_end of this WorkflowTasksRequest.

        Date/time that the workflow task was last updated  # noqa: E501

        :param last_update_dts_end: The last_update_dts_end of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """

        self._last_update_dts_end = last_update_dts_end

    @property
    def object_email(self):
        """Gets the object_email of this WorkflowTasksRequest.  # noqa: E501

        Object is associated with customer email  # noqa: E501

        :return: The object_email of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._object_email

    @object_email.setter
    def object_email(self, object_email):
        """Sets the object_email of this WorkflowTasksRequest.

        Object is associated with customer email  # noqa: E501

        :param object_email: The object_email of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """

        self._object_email = object_email

    @property
    def object_type(self):
        """Gets the object_type of this WorkflowTasksRequest.  # noqa: E501

        Object Type  # noqa: E501

        :return: The object_type of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this WorkflowTasksRequest.

        Object Type  # noqa: E501

        :param object_type: The object_type of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["order", "auto order", "item", "customer profile"]  # noqa: E501
        if object_type not in allowed_values:
            raise ValueError(
                "Invalid value for `object_type` ({0}), must be one of {1}"  # noqa: E501
                .format(object_type, allowed_values)
            )

        self._object_type = object_type

    @property
    def priority(self):
        """Gets the priority of this WorkflowTasksRequest.  # noqa: E501

        Priority  # noqa: E501

        :return: The priority of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this WorkflowTasksRequest.

        Priority  # noqa: E501

        :param priority: The priority of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["1 - low", "2 - medium", "3 - high", "4 - critical"]  # noqa: E501
        if priority not in allowed_values:
            raise ValueError(
                "Invalid value for `priority` ({0}), must be one of {1}"  # noqa: E501
                .format(priority, allowed_values)
            )

        self._priority = priority

    @property
    def status(self):
        """Gets the status of this WorkflowTasksRequest.  # noqa: E501

        Status of the workflow task  # noqa: E501

        :return: The status of this WorkflowTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkflowTasksRequest.

        Status of the workflow task  # noqa: E501

        :param status: The status of this WorkflowTasksRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["open", "closed", "delayed", "awaiting customer feedback"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this WorkflowTasksRequest.  # noqa: E501

        Tasks that are tagged with the specified tags  # noqa: E501

        :return: The tags of this WorkflowTasksRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WorkflowTasksRequest.

        Tasks that are tagged with the specified tags  # noqa: E501

        :param tags: The tags of this WorkflowTasksRequest.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def unassigned(self):
        """Gets the unassigned of this WorkflowTasksRequest.  # noqa: E501

        Tasks that are unassigned to a user or group  # noqa: E501

        :return: The unassigned of this WorkflowTasksRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unassigned

    @unassigned.setter
    def unassigned(self, unassigned):
        """Sets the unassigned of this WorkflowTasksRequest.

        Tasks that are unassigned to a user or group  # noqa: E501

        :param unassigned: The unassigned of this WorkflowTasksRequest.  # noqa: E501
        :type: bool
        """

        self._unassigned = unassigned

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
        if issubclass(WorkflowTasksRequest, dict):
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
        if not isinstance(other, WorkflowTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
