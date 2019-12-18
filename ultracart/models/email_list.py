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


class EmailList(object):
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
        'created_dts': 'str',
        'deleted': 'bool',
        'email_list_uuid': 'str',
        'member_count': 'int',
        'merchant_id': 'str',
        'name': 'str',
        'storefront_oid': 'int'
    }

    attribute_map = {
        'created_dts': 'created_dts',
        'deleted': 'deleted',
        'email_list_uuid': 'email_list_uuid',
        'member_count': 'member_count',
        'merchant_id': 'merchant_id',
        'name': 'name',
        'storefront_oid': 'storefront_oid'
    }

    def __init__(self, created_dts=None, deleted=None, email_list_uuid=None, member_count=None, merchant_id=None, name=None, storefront_oid=None):
        """
        EmailList - a model defined in Swagger
        """

        self._created_dts = None
        self._deleted = None
        self._email_list_uuid = None
        self._member_count = None
        self._merchant_id = None
        self._name = None
        self._storefront_oid = None
        self.discriminator = None

        if created_dts is not None:
          self.created_dts = created_dts
        if deleted is not None:
          self.deleted = deleted
        if email_list_uuid is not None:
          self.email_list_uuid = email_list_uuid
        if member_count is not None:
          self.member_count = member_count
        if merchant_id is not None:
          self.merchant_id = merchant_id
        if name is not None:
          self.name = name
        if storefront_oid is not None:
          self.storefront_oid = storefront_oid

    @property
    def created_dts(self):
        """
        Gets the created_dts of this EmailList.
        Created date

        :return: The created_dts of this EmailList.
        :rtype: str
        """
        return self._created_dts

    @created_dts.setter
    def created_dts(self, created_dts):
        """
        Sets the created_dts of this EmailList.
        Created date

        :param created_dts: The created_dts of this EmailList.
        :type: str
        """

        self._created_dts = created_dts

    @property
    def deleted(self):
        """
        Gets the deleted of this EmailList.
        True if this campaign was deleted

        :return: The deleted of this EmailList.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this EmailList.
        True if this campaign was deleted

        :param deleted: The deleted of this EmailList.
        :type: bool
        """

        self._deleted = deleted

    @property
    def email_list_uuid(self):
        """
        Gets the email_list_uuid of this EmailList.
        Email list UUID

        :return: The email_list_uuid of this EmailList.
        :rtype: str
        """
        return self._email_list_uuid

    @email_list_uuid.setter
    def email_list_uuid(self, email_list_uuid):
        """
        Sets the email_list_uuid of this EmailList.
        Email list UUID

        :param email_list_uuid: The email_list_uuid of this EmailList.
        :type: str
        """

        self._email_list_uuid = email_list_uuid

    @property
    def member_count(self):
        """
        Gets the member_count of this EmailList.
        Count of members in this list

        :return: The member_count of this EmailList.
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """
        Sets the member_count of this EmailList.
        Count of members in this list

        :param member_count: The member_count of this EmailList.
        :type: int
        """

        self._member_count = member_count

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this EmailList.
        Merchant ID

        :return: The merchant_id of this EmailList.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this EmailList.
        Merchant ID

        :param merchant_id: The merchant_id of this EmailList.
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def name(self):
        """
        Gets the name of this EmailList.
        Name of email list

        :return: The name of this EmailList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EmailList.
        Name of email list

        :param name: The name of this EmailList.
        :type: str
        """
        if name is not None and len(name) > 250:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `250`")

        self._name = name

    @property
    def storefront_oid(self):
        """
        Gets the storefront_oid of this EmailList.
        Storefront oid

        :return: The storefront_oid of this EmailList.
        :rtype: int
        """
        return self._storefront_oid

    @storefront_oid.setter
    def storefront_oid(self, storefront_oid):
        """
        Sets the storefront_oid of this EmailList.
        Storefront oid

        :param storefront_oid: The storefront_oid of this EmailList.
        :type: int
        """

        self._storefront_oid = storefront_oid

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
        if not isinstance(other, EmailList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
