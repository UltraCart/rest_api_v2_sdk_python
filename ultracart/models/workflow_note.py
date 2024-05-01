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


class WorkflowNote(object):
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
        'attachments': 'list[WorkflowAttachment]',
        'edit_dts': 'str',
        'note': 'str',
        'note_dts': 'str',
        'original_note': 'str',
        'user': 'WorkflowUser'
    }

    attribute_map = {
        'attachments': 'attachments',
        'edit_dts': 'edit_dts',
        'note': 'note',
        'note_dts': 'note_dts',
        'original_note': 'original_note',
        'user': 'user'
    }

    def __init__(self, attachments=None, edit_dts=None, note=None, note_dts=None, original_note=None, user=None):  # noqa: E501
        """WorkflowNote - a model defined in Swagger"""  # noqa: E501

        self._attachments = None
        self._edit_dts = None
        self._note = None
        self._note_dts = None
        self._original_note = None
        self._user = None
        self.discriminator = None

        if attachments is not None:
            self.attachments = attachments
        if edit_dts is not None:
            self.edit_dts = edit_dts
        if note is not None:
            self.note = note
        if note_dts is not None:
            self.note_dts = note_dts
        if original_note is not None:
            self.original_note = original_note
        if user is not None:
            self.user = user

    @property
    def attachments(self):
        """Gets the attachments of this WorkflowNote.  # noqa: E501

        Attachments to the Workflow Task  # noqa: E501

        :return: The attachments of this WorkflowNote.  # noqa: E501
        :rtype: list[WorkflowAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this WorkflowNote.

        Attachments to the Workflow Task  # noqa: E501

        :param attachments: The attachments of this WorkflowNote.  # noqa: E501
        :type: list[WorkflowAttachment]
        """

        self._attachments = attachments

    @property
    def edit_dts(self):
        """Gets the edit_dts of this WorkflowNote.  # noqa: E501

        Date/time that the note was edited  # noqa: E501

        :return: The edit_dts of this WorkflowNote.  # noqa: E501
        :rtype: str
        """
        return self._edit_dts

    @edit_dts.setter
    def edit_dts(self, edit_dts):
        """Sets the edit_dts of this WorkflowNote.

        Date/time that the note was edited  # noqa: E501

        :param edit_dts: The edit_dts of this WorkflowNote.  # noqa: E501
        :type: str
        """

        self._edit_dts = edit_dts

    @property
    def note(self):
        """Gets the note of this WorkflowNote.  # noqa: E501

        Note  # noqa: E501

        :return: The note of this WorkflowNote.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this WorkflowNote.

        Note  # noqa: E501

        :param note: The note of this WorkflowNote.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def note_dts(self):
        """Gets the note_dts of this WorkflowNote.  # noqa: E501

        Date/time that the note was written  # noqa: E501

        :return: The note_dts of this WorkflowNote.  # noqa: E501
        :rtype: str
        """
        return self._note_dts

    @note_dts.setter
    def note_dts(self, note_dts):
        """Sets the note_dts of this WorkflowNote.

        Date/time that the note was written  # noqa: E501

        :param note_dts: The note_dts of this WorkflowNote.  # noqa: E501
        :type: str
        """

        self._note_dts = note_dts

    @property
    def original_note(self):
        """Gets the original_note of this WorkflowNote.  # noqa: E501

        Note originally written before any edits  # noqa: E501

        :return: The original_note of this WorkflowNote.  # noqa: E501
        :rtype: str
        """
        return self._original_note

    @original_note.setter
    def original_note(self, original_note):
        """Sets the original_note of this WorkflowNote.

        Note originally written before any edits  # noqa: E501

        :param original_note: The original_note of this WorkflowNote.  # noqa: E501
        :type: str
        """

        self._original_note = original_note

    @property
    def user(self):
        """Gets the user of this WorkflowNote.  # noqa: E501


        :return: The user of this WorkflowNote.  # noqa: E501
        :rtype: WorkflowUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this WorkflowNote.


        :param user: The user of this WorkflowNote.  # noqa: E501
        :type: WorkflowUser
        """

        self._user = user

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
        if issubclass(WorkflowNote, dict):
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
        if not isinstance(other, WorkflowNote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other