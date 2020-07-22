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


class TransactionEmail(object):
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
        'content': 'str',
        'esp_domain_uuid': 'str',
        'esp_friendly_name': 'str',
        'esp_user': 'str',
        'file_exists': 'bool',
        'file_name': 'str',
        'group': 'str',
        'invalid': 'bool',
        'last_modified': 'str',
        'options': 'list[TransactionEmailOption]',
        'path': 'str',
        'size': 'str',
        'store_front_fs_directory_oid': 'int',
        'store_front_fs_file_oid': 'int',
        'subject': 'str',
        'syntax_errors': 'str',
        'template_path_relative_path': 'str',
        'theme_relative_path': 'str'
    }

    attribute_map = {
        'content': 'content',
        'esp_domain_uuid': 'esp_domain_uuid',
        'esp_friendly_name': 'esp_friendly_name',
        'esp_user': 'esp_user',
        'file_exists': 'file_exists',
        'file_name': 'file_name',
        'group': 'group',
        'invalid': 'invalid',
        'last_modified': 'last_modified',
        'options': 'options',
        'path': 'path',
        'size': 'size',
        'store_front_fs_directory_oid': 'store_front_fs_directory_oid',
        'store_front_fs_file_oid': 'store_front_fs_file_oid',
        'subject': 'subject',
        'syntax_errors': 'syntax_errors',
        'template_path_relative_path': 'template_path_relative_path',
        'theme_relative_path': 'theme_relative_path'
    }

    def __init__(self, content=None, esp_domain_uuid=None, esp_friendly_name=None, esp_user=None, file_exists=None, file_name=None, group=None, invalid=None, last_modified=None, options=None, path=None, size=None, store_front_fs_directory_oid=None, store_front_fs_file_oid=None, subject=None, syntax_errors=None, template_path_relative_path=None, theme_relative_path=None):  # noqa: E501
        """TransactionEmail - a model defined in Swagger"""  # noqa: E501

        self._content = None
        self._esp_domain_uuid = None
        self._esp_friendly_name = None
        self._esp_user = None
        self._file_exists = None
        self._file_name = None
        self._group = None
        self._invalid = None
        self._last_modified = None
        self._options = None
        self._path = None
        self._size = None
        self._store_front_fs_directory_oid = None
        self._store_front_fs_file_oid = None
        self._subject = None
        self._syntax_errors = None
        self._template_path_relative_path = None
        self._theme_relative_path = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if esp_domain_uuid is not None:
            self.esp_domain_uuid = esp_domain_uuid
        if esp_friendly_name is not None:
            self.esp_friendly_name = esp_friendly_name
        if esp_user is not None:
            self.esp_user = esp_user
        if file_exists is not None:
            self.file_exists = file_exists
        if file_name is not None:
            self.file_name = file_name
        if group is not None:
            self.group = group
        if invalid is not None:
            self.invalid = invalid
        if last_modified is not None:
            self.last_modified = last_modified
        if options is not None:
            self.options = options
        if path is not None:
            self.path = path
        if size is not None:
            self.size = size
        if store_front_fs_directory_oid is not None:
            self.store_front_fs_directory_oid = store_front_fs_directory_oid
        if store_front_fs_file_oid is not None:
            self.store_front_fs_file_oid = store_front_fs_file_oid
        if subject is not None:
            self.subject = subject
        if syntax_errors is not None:
            self.syntax_errors = syntax_errors
        if template_path_relative_path is not None:
            self.template_path_relative_path = template_path_relative_path
        if theme_relative_path is not None:
            self.theme_relative_path = theme_relative_path

    @property
    def content(self):
        """Gets the content of this TransactionEmail.  # noqa: E501

        Actual template contents  # noqa: E501

        :return: The content of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this TransactionEmail.

        Actual template contents  # noqa: E501

        :param content: The content of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def esp_domain_uuid(self):
        """Gets the esp_domain_uuid of this TransactionEmail.  # noqa: E501

        The uuid of the sending domain  # noqa: E501

        :return: The esp_domain_uuid of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._esp_domain_uuid

    @esp_domain_uuid.setter
    def esp_domain_uuid(self, esp_domain_uuid):
        """Sets the esp_domain_uuid of this TransactionEmail.

        The uuid of the sending domain  # noqa: E501

        :param esp_domain_uuid: The esp_domain_uuid of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._esp_domain_uuid = esp_domain_uuid

    @property
    def esp_friendly_name(self):
        """Gets the esp_friendly_name of this TransactionEmail.  # noqa: E501

        Friendly from that will appear in customer email clients.  # noqa: E501

        :return: The esp_friendly_name of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._esp_friendly_name

    @esp_friendly_name.setter
    def esp_friendly_name(self, esp_friendly_name):
        """Sets the esp_friendly_name of this TransactionEmail.

        Friendly from that will appear in customer email clients.  # noqa: E501

        :param esp_friendly_name: The esp_friendly_name of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._esp_friendly_name = esp_friendly_name

    @property
    def esp_user(self):
        """Gets the esp_user of this TransactionEmail.  # noqa: E501

        The username of the sending email.  This is not the full email.  Only the username which is everything before the @ sign.  # noqa: E501

        :return: The esp_user of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._esp_user

    @esp_user.setter
    def esp_user(self, esp_user):
        """Sets the esp_user of this TransactionEmail.

        The username of the sending email.  This is not the full email.  Only the username which is everything before the @ sign.  # noqa: E501

        :param esp_user: The esp_user of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._esp_user = esp_user

    @property
    def file_exists(self):
        """Gets the file_exists of this TransactionEmail.  # noqa: E501

        An internal identifier used to aid in retrieving templates from the filesystem.  # noqa: E501

        :return: The file_exists of this TransactionEmail.  # noqa: E501
        :rtype: bool
        """
        return self._file_exists

    @file_exists.setter
    def file_exists(self, file_exists):
        """Sets the file_exists of this TransactionEmail.

        An internal identifier used to aid in retrieving templates from the filesystem.  # noqa: E501

        :param file_exists: The file_exists of this TransactionEmail.  # noqa: E501
        :type: bool
        """

        self._file_exists = file_exists

    @property
    def file_name(self):
        """Gets the file_name of this TransactionEmail.  # noqa: E501

        File name  # noqa: E501

        :return: The file_name of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this TransactionEmail.

        File name  # noqa: E501

        :param file_name: The file_name of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def group(self):
        """Gets the group of this TransactionEmail.  # noqa: E501

        Group  # noqa: E501

        :return: The group of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this TransactionEmail.

        Group  # noqa: E501

        :param group: The group of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def invalid(self):
        """Gets the invalid of this TransactionEmail.  # noqa: E501

        Invalid will be true if the template cannot compile  # noqa: E501

        :return: The invalid of this TransactionEmail.  # noqa: E501
        :rtype: bool
        """
        return self._invalid

    @invalid.setter
    def invalid(self, invalid):
        """Sets the invalid of this TransactionEmail.

        Invalid will be true if the template cannot compile  # noqa: E501

        :param invalid: The invalid of this TransactionEmail.  # noqa: E501
        :type: bool
        """

        self._invalid = invalid

    @property
    def last_modified(self):
        """Gets the last_modified of this TransactionEmail.  # noqa: E501

        Last modified timestamp  # noqa: E501

        :return: The last_modified of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this TransactionEmail.

        Last modified timestamp  # noqa: E501

        :param last_modified: The last_modified of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._last_modified = last_modified

    @property
    def options(self):
        """Gets the options of this TransactionEmail.  # noqa: E501

        Options that help govern how and when this template is used  # noqa: E501

        :return: The options of this TransactionEmail.  # noqa: E501
        :rtype: list[TransactionEmailOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this TransactionEmail.

        Options that help govern how and when this template is used  # noqa: E501

        :param options: The options of this TransactionEmail.  # noqa: E501
        :type: list[TransactionEmailOption]
        """

        self._options = options

    @property
    def path(self):
        """Gets the path of this TransactionEmail.  # noqa: E501

        directory path where template is stored in file system  # noqa: E501

        :return: The path of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TransactionEmail.

        directory path where template is stored in file system  # noqa: E501

        :param path: The path of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def size(self):
        """Gets the size of this TransactionEmail.  # noqa: E501

        Size of file in friendly description  # noqa: E501

        :return: The size of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TransactionEmail.

        Size of file in friendly description  # noqa: E501

        :param size: The size of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def store_front_fs_directory_oid(self):
        """Gets the store_front_fs_directory_oid of this TransactionEmail.  # noqa: E501

        Internal identifier used to store and retrieve template from filesystem  # noqa: E501

        :return: The store_front_fs_directory_oid of this TransactionEmail.  # noqa: E501
        :rtype: int
        """
        return self._store_front_fs_directory_oid

    @store_front_fs_directory_oid.setter
    def store_front_fs_directory_oid(self, store_front_fs_directory_oid):
        """Sets the store_front_fs_directory_oid of this TransactionEmail.

        Internal identifier used to store and retrieve template from filesystem  # noqa: E501

        :param store_front_fs_directory_oid: The store_front_fs_directory_oid of this TransactionEmail.  # noqa: E501
        :type: int
        """

        self._store_front_fs_directory_oid = store_front_fs_directory_oid

    @property
    def store_front_fs_file_oid(self):
        """Gets the store_front_fs_file_oid of this TransactionEmail.  # noqa: E501

        Internal identifier used to store and retrieve template from filesystem  # noqa: E501

        :return: The store_front_fs_file_oid of this TransactionEmail.  # noqa: E501
        :rtype: int
        """
        return self._store_front_fs_file_oid

    @store_front_fs_file_oid.setter
    def store_front_fs_file_oid(self, store_front_fs_file_oid):
        """Sets the store_front_fs_file_oid of this TransactionEmail.

        Internal identifier used to store and retrieve template from filesystem  # noqa: E501

        :param store_front_fs_file_oid: The store_front_fs_file_oid of this TransactionEmail.  # noqa: E501
        :type: int
        """

        self._store_front_fs_file_oid = store_front_fs_file_oid

    @property
    def subject(self):
        """Gets the subject of this TransactionEmail.  # noqa: E501

        Subject  # noqa: E501

        :return: The subject of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this TransactionEmail.

        Subject  # noqa: E501

        :param subject: The subject of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def syntax_errors(self):
        """Gets the syntax_errors of this TransactionEmail.  # noqa: E501

        Any syntax errors contained within the tempalate  # noqa: E501

        :return: The syntax_errors of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._syntax_errors

    @syntax_errors.setter
    def syntax_errors(self, syntax_errors):
        """Sets the syntax_errors of this TransactionEmail.

        Any syntax errors contained within the tempalate  # noqa: E501

        :param syntax_errors: The syntax_errors of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._syntax_errors = syntax_errors

    @property
    def template_path_relative_path(self):
        """Gets the template_path_relative_path of this TransactionEmail.  # noqa: E501

        Internal value used to locate the template in the filesystem  # noqa: E501

        :return: The template_path_relative_path of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._template_path_relative_path

    @template_path_relative_path.setter
    def template_path_relative_path(self, template_path_relative_path):
        """Sets the template_path_relative_path of this TransactionEmail.

        Internal value used to locate the template in the filesystem  # noqa: E501

        :param template_path_relative_path: The template_path_relative_path of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._template_path_relative_path = template_path_relative_path

    @property
    def theme_relative_path(self):
        """Gets the theme_relative_path of this TransactionEmail.  # noqa: E501

        Theme relative path in the filesystem.  # noqa: E501

        :return: The theme_relative_path of this TransactionEmail.  # noqa: E501
        :rtype: str
        """
        return self._theme_relative_path

    @theme_relative_path.setter
    def theme_relative_path(self, theme_relative_path):
        """Sets the theme_relative_path of this TransactionEmail.

        Theme relative path in the filesystem.  # noqa: E501

        :param theme_relative_path: The theme_relative_path of this TransactionEmail.  # noqa: E501
        :type: str
        """

        self._theme_relative_path = theme_relative_path

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
        if issubclass(TransactionEmail, dict):
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
        if not isinstance(other, TransactionEmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
