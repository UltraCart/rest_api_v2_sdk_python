"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ultracart.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from ultracart.exceptions import ApiAttributeError


def lazy_import():
    from ultracart.model.linked_account import LinkedAccount
    from ultracart.model.notification import Notification
    from ultracart.model.permission import Permission
    from ultracart.model.user_group_membership import UserGroupMembership
    from ultracart.model.user_login import UserLogin
    globals()['LinkedAccount'] = LinkedAccount
    globals()['Notification'] = Notification
    globals()['Permission'] = Permission
    globals()['UserGroupMembership'] = UserGroupMembership
    globals()['UserLogin'] = UserLogin


class User(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('email',): {
            'max_length': 150,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'api_ip_address_masks': ([str],),  # noqa: E501
            'change_ftp_password_to': (str,),  # noqa: E501
            'change_password_to': (str,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'full_name': (str,),  # noqa: E501
            'groups': ([UserGroupMembership],),  # noqa: E501
            'linked_accounts': ([LinkedAccount],),  # noqa: E501
            'login': (str,),  # noqa: E501
            'login_histories': ([UserLogin],),  # noqa: E501
            'notifications': ([Notification],),  # noqa: E501
            'otp_serial_number': (str,),  # noqa: E501
            'permissions': ([Permission],),  # noqa: E501
            'phone': (str,),  # noqa: E501
            'user_id': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'api_ip_address_masks': 'api_ip_address_masks',  # noqa: E501
        'change_ftp_password_to': 'change_ftp_password_to',  # noqa: E501
        'change_password_to': 'change_password_to',  # noqa: E501
        'email': 'email',  # noqa: E501
        'full_name': 'full_name',  # noqa: E501
        'groups': 'groups',  # noqa: E501
        'linked_accounts': 'linked_accounts',  # noqa: E501
        'login': 'login',  # noqa: E501
        'login_histories': 'login_histories',  # noqa: E501
        'notifications': 'notifications',  # noqa: E501
        'otp_serial_number': 'otp_serial_number',  # noqa: E501
        'permissions': 'permissions',  # noqa: E501
        'phone': 'phone',  # noqa: E501
        'user_id': 'user_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """User - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            api_ip_address_masks ([str]): A list of IP addresses whitelisted for any user with API Access permission.  Without this list, each ip address must be authenticated by a user, which can be a pain for some servers.. [optional]  # noqa: E501
            change_ftp_password_to (str): Supply a new FTP password using this field.  Password are stored using one-way encryption, so they are never available anywhere in the system.  The FTP password cannot be the same as the normal password.. [optional]  # noqa: E501
            change_password_to (str): Supply a new password using this field.  Password are stored using one-way encryption, so they are never available anywhere in the system.. [optional]  # noqa: E501
            email (str): Email address of user. [optional]  # noqa: E501
            full_name (str): Full name of user.  This is used solely for human assistance and so the UltraCart staff knows who they are calling when there is a problem.. [optional]  # noqa: E501
            groups ([UserGroupMembership]): A list of groups for this merchant and whether or not this user is a member of those groups.. [optional]  # noqa: E501
            linked_accounts ([LinkedAccount]): A list of linked accounts and whether or not this user is mirrored to any of those accounts.. [optional]  # noqa: E501
            login (str): User name of user.  Must be unique across a merchant account.. [optional]  # noqa: E501
            login_histories ([UserLogin]): A list of user logins over the past 90 days. [optional]  # noqa: E501
            notifications ([Notification]): A list of notifications the user receives.. [optional]  # noqa: E501
            otp_serial_number (str): OTP Serial Number such as Google Authenticator or Crypto Card.. [optional]  # noqa: E501
            permissions ([Permission]): A list of permissions the user enjoys for accessing the backend of UltraCart.. [optional]  # noqa: E501
            phone (str): Phone number of user.  Please supply a valid phone number.  When something breaks on your account, we need to be able to reach you.. [optional]  # noqa: E501
            user_id (int): User id is a unique identifier for this user. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """User - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            api_ip_address_masks ([str]): A list of IP addresses whitelisted for any user with API Access permission.  Without this list, each ip address must be authenticated by a user, which can be a pain for some servers.. [optional]  # noqa: E501
            change_ftp_password_to (str): Supply a new FTP password using this field.  Password are stored using one-way encryption, so they are never available anywhere in the system.  The FTP password cannot be the same as the normal password.. [optional]  # noqa: E501
            change_password_to (str): Supply a new password using this field.  Password are stored using one-way encryption, so they are never available anywhere in the system.. [optional]  # noqa: E501
            email (str): Email address of user. [optional]  # noqa: E501
            full_name (str): Full name of user.  This is used solely for human assistance and so the UltraCart staff knows who they are calling when there is a problem.. [optional]  # noqa: E501
            groups ([UserGroupMembership]): A list of groups for this merchant and whether or not this user is a member of those groups.. [optional]  # noqa: E501
            linked_accounts ([LinkedAccount]): A list of linked accounts and whether or not this user is mirrored to any of those accounts.. [optional]  # noqa: E501
            login (str): User name of user.  Must be unique across a merchant account.. [optional]  # noqa: E501
            login_histories ([UserLogin]): A list of user logins over the past 90 days. [optional]  # noqa: E501
            notifications ([Notification]): A list of notifications the user receives.. [optional]  # noqa: E501
            otp_serial_number (str): OTP Serial Number such as Google Authenticator or Crypto Card.. [optional]  # noqa: E501
            permissions ([Permission]): A list of permissions the user enjoys for accessing the backend of UltraCart.. [optional]  # noqa: E501
            phone (str): Phone number of user.  Please supply a valid phone number.  When something breaks on your account, we need to be able to reach you.. [optional]  # noqa: E501
            user_id (int): User id is a unique identifier for this user. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
