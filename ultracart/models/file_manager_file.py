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


class FileManagerFile(object):
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
        'favorite': 'bool',
        'hostname': 'str',
        'i18n_violation': 'bool',
        'icon': 'str',
        'internal_version': 'int',
        'last_modified': 'str',
        'merge_conflict': 'bool',
        'name': 'str',
        'parent_storefront_fs_directory_oid': 'int',
        'part_of_active_theme': 'bool',
        'path': 'str',
        'raw_size': 'int',
        'selected': 'bool',
        'size': 'str',
        'storefront_fs_directory_oid': 'int',
        'storefront_fs_file_oid': 'int',
        'storefront_oid': 'int',
        'type': 'str',
        'valid_velocity': 'str'
    }

    attribute_map = {
        'favorite': 'favorite',
        'hostname': 'hostname',
        'i18n_violation': 'i18n_violation',
        'icon': 'icon',
        'internal_version': 'internal_version',
        'last_modified': 'last_modified',
        'merge_conflict': 'merge_conflict',
        'name': 'name',
        'parent_storefront_fs_directory_oid': 'parent_storefront_fs_directory_oid',
        'part_of_active_theme': 'part_of_active_theme',
        'path': 'path',
        'raw_size': 'raw_size',
        'selected': 'selected',
        'size': 'size',
        'storefront_fs_directory_oid': 'storefront_fs_directory_oid',
        'storefront_fs_file_oid': 'storefront_fs_file_oid',
        'storefront_oid': 'storefront_oid',
        'type': 'type',
        'valid_velocity': 'valid_velocity'
    }

    def __init__(self, favorite=None, hostname=None, i18n_violation=None, icon=None, internal_version=None, last_modified=None, merge_conflict=None, name=None, parent_storefront_fs_directory_oid=None, part_of_active_theme=None, path=None, raw_size=None, selected=None, size=None, storefront_fs_directory_oid=None, storefront_fs_file_oid=None, storefront_oid=None, type=None, valid_velocity=None):  # noqa: E501
        """FileManagerFile - a model defined in Swagger"""  # noqa: E501

        self._favorite = None
        self._hostname = None
        self._i18n_violation = None
        self._icon = None
        self._internal_version = None
        self._last_modified = None
        self._merge_conflict = None
        self._name = None
        self._parent_storefront_fs_directory_oid = None
        self._part_of_active_theme = None
        self._path = None
        self._raw_size = None
        self._selected = None
        self._size = None
        self._storefront_fs_directory_oid = None
        self._storefront_fs_file_oid = None
        self._storefront_oid = None
        self._type = None
        self._valid_velocity = None
        self.discriminator = None

        if favorite is not None:
            self.favorite = favorite
        if hostname is not None:
            self.hostname = hostname
        if i18n_violation is not None:
            self.i18n_violation = i18n_violation
        if icon is not None:
            self.icon = icon
        if internal_version is not None:
            self.internal_version = internal_version
        if last_modified is not None:
            self.last_modified = last_modified
        if merge_conflict is not None:
            self.merge_conflict = merge_conflict
        if name is not None:
            self.name = name
        if parent_storefront_fs_directory_oid is not None:
            self.parent_storefront_fs_directory_oid = parent_storefront_fs_directory_oid
        if part_of_active_theme is not None:
            self.part_of_active_theme = part_of_active_theme
        if path is not None:
            self.path = path
        if raw_size is not None:
            self.raw_size = raw_size
        if selected is not None:
            self.selected = selected
        if size is not None:
            self.size = size
        if storefront_fs_directory_oid is not None:
            self.storefront_fs_directory_oid = storefront_fs_directory_oid
        if storefront_fs_file_oid is not None:
            self.storefront_fs_file_oid = storefront_fs_file_oid
        if storefront_oid is not None:
            self.storefront_oid = storefront_oid
        if type is not None:
            self.type = type
        if valid_velocity is not None:
            self.valid_velocity = valid_velocity

    @property
    def favorite(self):
        """Gets the favorite of this FileManagerFile.  # noqa: E501


        :return: The favorite of this FileManagerFile.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this FileManagerFile.


        :param favorite: The favorite of this FileManagerFile.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

    @property
    def hostname(self):
        """Gets the hostname of this FileManagerFile.  # noqa: E501


        :return: The hostname of this FileManagerFile.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this FileManagerFile.


        :param hostname: The hostname of this FileManagerFile.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def i18n_violation(self):
        """Gets the i18n_violation of this FileManagerFile.  # noqa: E501


        :return: The i18n_violation of this FileManagerFile.  # noqa: E501
        :rtype: bool
        """
        return self._i18n_violation

    @i18n_violation.setter
    def i18n_violation(self, i18n_violation):
        """Sets the i18n_violation of this FileManagerFile.


        :param i18n_violation: The i18n_violation of this FileManagerFile.  # noqa: E501
        :type: bool
        """

        self._i18n_violation = i18n_violation

    @property
    def icon(self):
        """Gets the icon of this FileManagerFile.  # noqa: E501


        :return: The icon of this FileManagerFile.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this FileManagerFile.


        :param icon: The icon of this FileManagerFile.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def internal_version(self):
        """Gets the internal_version of this FileManagerFile.  # noqa: E501


        :return: The internal_version of this FileManagerFile.  # noqa: E501
        :rtype: int
        """
        return self._internal_version

    @internal_version.setter
    def internal_version(self, internal_version):
        """Sets the internal_version of this FileManagerFile.


        :param internal_version: The internal_version of this FileManagerFile.  # noqa: E501
        :type: int
        """

        self._internal_version = internal_version

    @property
    def last_modified(self):
        """Gets the last_modified of this FileManagerFile.  # noqa: E501


        :return: The last_modified of this FileManagerFile.  # noqa: E501
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this FileManagerFile.


        :param last_modified: The last_modified of this FileManagerFile.  # noqa: E501
        :type: str
        """

        self._last_modified = last_modified

    @property
    def merge_conflict(self):
        """Gets the merge_conflict of this FileManagerFile.  # noqa: E501


        :return: The merge_conflict of this FileManagerFile.  # noqa: E501
        :rtype: bool
        """
        return self._merge_conflict

    @merge_conflict.setter
    def merge_conflict(self, merge_conflict):
        """Sets the merge_conflict of this FileManagerFile.


        :param merge_conflict: The merge_conflict of this FileManagerFile.  # noqa: E501
        :type: bool
        """

        self._merge_conflict = merge_conflict

    @property
    def name(self):
        """Gets the name of this FileManagerFile.  # noqa: E501


        :return: The name of this FileManagerFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileManagerFile.


        :param name: The name of this FileManagerFile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent_storefront_fs_directory_oid(self):
        """Gets the parent_storefront_fs_directory_oid of this FileManagerFile.  # noqa: E501


        :return: The parent_storefront_fs_directory_oid of this FileManagerFile.  # noqa: E501
        :rtype: int
        """
        return self._parent_storefront_fs_directory_oid

    @parent_storefront_fs_directory_oid.setter
    def parent_storefront_fs_directory_oid(self, parent_storefront_fs_directory_oid):
        """Sets the parent_storefront_fs_directory_oid of this FileManagerFile.


        :param parent_storefront_fs_directory_oid: The parent_storefront_fs_directory_oid of this FileManagerFile.  # noqa: E501
        :type: int
        """

        self._parent_storefront_fs_directory_oid = parent_storefront_fs_directory_oid

    @property
    def part_of_active_theme(self):
        """Gets the part_of_active_theme of this FileManagerFile.  # noqa: E501


        :return: The part_of_active_theme of this FileManagerFile.  # noqa: E501
        :rtype: bool
        """
        return self._part_of_active_theme

    @part_of_active_theme.setter
    def part_of_active_theme(self, part_of_active_theme):
        """Sets the part_of_active_theme of this FileManagerFile.


        :param part_of_active_theme: The part_of_active_theme of this FileManagerFile.  # noqa: E501
        :type: bool
        """

        self._part_of_active_theme = part_of_active_theme

    @property
    def path(self):
        """Gets the path of this FileManagerFile.  # noqa: E501


        :return: The path of this FileManagerFile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FileManagerFile.


        :param path: The path of this FileManagerFile.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def raw_size(self):
        """Gets the raw_size of this FileManagerFile.  # noqa: E501


        :return: The raw_size of this FileManagerFile.  # noqa: E501
        :rtype: int
        """
        return self._raw_size

    @raw_size.setter
    def raw_size(self, raw_size):
        """Sets the raw_size of this FileManagerFile.


        :param raw_size: The raw_size of this FileManagerFile.  # noqa: E501
        :type: int
        """

        self._raw_size = raw_size

    @property
    def selected(self):
        """Gets the selected of this FileManagerFile.  # noqa: E501


        :return: The selected of this FileManagerFile.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this FileManagerFile.


        :param selected: The selected of this FileManagerFile.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def size(self):
        """Gets the size of this FileManagerFile.  # noqa: E501


        :return: The size of this FileManagerFile.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileManagerFile.


        :param size: The size of this FileManagerFile.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def storefront_fs_directory_oid(self):
        """Gets the storefront_fs_directory_oid of this FileManagerFile.  # noqa: E501


        :return: The storefront_fs_directory_oid of this FileManagerFile.  # noqa: E501
        :rtype: int
        """
        return self._storefront_fs_directory_oid

    @storefront_fs_directory_oid.setter
    def storefront_fs_directory_oid(self, storefront_fs_directory_oid):
        """Sets the storefront_fs_directory_oid of this FileManagerFile.


        :param storefront_fs_directory_oid: The storefront_fs_directory_oid of this FileManagerFile.  # noqa: E501
        :type: int
        """

        self._storefront_fs_directory_oid = storefront_fs_directory_oid

    @property
    def storefront_fs_file_oid(self):
        """Gets the storefront_fs_file_oid of this FileManagerFile.  # noqa: E501


        :return: The storefront_fs_file_oid of this FileManagerFile.  # noqa: E501
        :rtype: int
        """
        return self._storefront_fs_file_oid

    @storefront_fs_file_oid.setter
    def storefront_fs_file_oid(self, storefront_fs_file_oid):
        """Sets the storefront_fs_file_oid of this FileManagerFile.


        :param storefront_fs_file_oid: The storefront_fs_file_oid of this FileManagerFile.  # noqa: E501
        :type: int
        """

        self._storefront_fs_file_oid = storefront_fs_file_oid

    @property
    def storefront_oid(self):
        """Gets the storefront_oid of this FileManagerFile.  # noqa: E501


        :return: The storefront_oid of this FileManagerFile.  # noqa: E501
        :rtype: int
        """
        return self._storefront_oid

    @storefront_oid.setter
    def storefront_oid(self, storefront_oid):
        """Sets the storefront_oid of this FileManagerFile.


        :param storefront_oid: The storefront_oid of this FileManagerFile.  # noqa: E501
        :type: int
        """

        self._storefront_oid = storefront_oid

    @property
    def type(self):
        """Gets the type of this FileManagerFile.  # noqa: E501


        :return: The type of this FileManagerFile.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileManagerFile.


        :param type: The type of this FileManagerFile.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def valid_velocity(self):
        """Gets the valid_velocity of this FileManagerFile.  # noqa: E501


        :return: The valid_velocity of this FileManagerFile.  # noqa: E501
        :rtype: str
        """
        return self._valid_velocity

    @valid_velocity.setter
    def valid_velocity(self, valid_velocity):
        """Sets the valid_velocity of this FileManagerFile.


        :param valid_velocity: The valid_velocity of this FileManagerFile.  # noqa: E501
        :type: str
        """

        self._valid_velocity = valid_velocity

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
        if issubclass(FileManagerFile, dict):
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
        if not isinstance(other, FileManagerFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
