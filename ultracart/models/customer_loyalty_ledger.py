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


class CustomerLoyaltyLedger(object):
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
        'created_by': 'str',
        'created_dts': 'str',
        'description': 'str',
        'email': 'str',
        'item_id': 'str',
        'item_index': 'int',
        'ledger_dts': 'str',
        'loyalty_campaign_oid': 'int',
        'loyalty_ledger_oid': 'int',
        'loyalty_points': 'int',
        'modified_by': 'str',
        'modified_dts': 'str',
        'order_id': 'str',
        'quantity': 'int',
        'vesting_dts': 'str'
    }

    attribute_map = {
        'created_by': 'created_by',
        'created_dts': 'created_dts',
        'description': 'description',
        'email': 'email',
        'item_id': 'item_id',
        'item_index': 'item_index',
        'ledger_dts': 'ledger_dts',
        'loyalty_campaign_oid': 'loyalty_campaign_oid',
        'loyalty_ledger_oid': 'loyalty_ledger_oid',
        'loyalty_points': 'loyalty_points',
        'modified_by': 'modified_by',
        'modified_dts': 'modified_dts',
        'order_id': 'order_id',
        'quantity': 'quantity',
        'vesting_dts': 'vesting_dts'
    }

    def __init__(self, created_by=None, created_dts=None, description=None, email=None, item_id=None, item_index=None, ledger_dts=None, loyalty_campaign_oid=None, loyalty_ledger_oid=None, loyalty_points=None, modified_by=None, modified_dts=None, order_id=None, quantity=None, vesting_dts=None):  # noqa: E501
        """CustomerLoyaltyLedger - a model defined in Swagger"""  # noqa: E501

        self._created_by = None
        self._created_dts = None
        self._description = None
        self._email = None
        self._item_id = None
        self._item_index = None
        self._ledger_dts = None
        self._loyalty_campaign_oid = None
        self._loyalty_ledger_oid = None
        self._loyalty_points = None
        self._modified_by = None
        self._modified_dts = None
        self._order_id = None
        self._quantity = None
        self._vesting_dts = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if created_dts is not None:
            self.created_dts = created_dts
        if description is not None:
            self.description = description
        if email is not None:
            self.email = email
        if item_id is not None:
            self.item_id = item_id
        if item_index is not None:
            self.item_index = item_index
        if ledger_dts is not None:
            self.ledger_dts = ledger_dts
        if loyalty_campaign_oid is not None:
            self.loyalty_campaign_oid = loyalty_campaign_oid
        if loyalty_ledger_oid is not None:
            self.loyalty_ledger_oid = loyalty_ledger_oid
        if loyalty_points is not None:
            self.loyalty_points = loyalty_points
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_dts is not None:
            self.modified_dts = modified_dts
        if order_id is not None:
            self.order_id = order_id
        if quantity is not None:
            self.quantity = quantity
        if vesting_dts is not None:
            self.vesting_dts = vesting_dts

    @property
    def created_by(self):
        """Gets the created_by of this CustomerLoyaltyLedger.  # noqa: E501

        Created By  # noqa: E501

        :return: The created_by of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CustomerLoyaltyLedger.

        Created By  # noqa: E501

        :param created_by: The created_by of this CustomerLoyaltyLedger.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_dts(self):
        """Gets the created_dts of this CustomerLoyaltyLedger.  # noqa: E501

        Created date  # noqa: E501

        :return: The created_dts of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: str
        """
        return self._created_dts

    @created_dts.setter
    def created_dts(self, created_dts):
        """Sets the created_dts of this CustomerLoyaltyLedger.

        Created date  # noqa: E501

        :param created_dts: The created_dts of this CustomerLoyaltyLedger.  # noqa: E501
        :type: str
        """

        self._created_dts = created_dts

    @property
    def description(self):
        """Gets the description of this CustomerLoyaltyLedger.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomerLoyaltyLedger.

        Description  # noqa: E501

        :param description: The description of this CustomerLoyaltyLedger.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email(self):
        """Gets the email of this CustomerLoyaltyLedger.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CustomerLoyaltyLedger.

        Email  # noqa: E501

        :param email: The email of this CustomerLoyaltyLedger.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def item_id(self):
        """Gets the item_id of this CustomerLoyaltyLedger.  # noqa: E501

        Item Id  # noqa: E501

        :return: The item_id of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this CustomerLoyaltyLedger.

        Item Id  # noqa: E501

        :param item_id: The item_id of this CustomerLoyaltyLedger.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def item_index(self):
        """Gets the item_index of this CustomerLoyaltyLedger.  # noqa: E501

        Item Index  # noqa: E501

        :return: The item_index of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: int
        """
        return self._item_index

    @item_index.setter
    def item_index(self, item_index):
        """Sets the item_index of this CustomerLoyaltyLedger.

        Item Index  # noqa: E501

        :param item_index: The item_index of this CustomerLoyaltyLedger.  # noqa: E501
        :type: int
        """

        self._item_index = item_index

    @property
    def ledger_dts(self):
        """Gets the ledger_dts of this CustomerLoyaltyLedger.  # noqa: E501

        Ledger date  # noqa: E501

        :return: The ledger_dts of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: str
        """
        return self._ledger_dts

    @ledger_dts.setter
    def ledger_dts(self, ledger_dts):
        """Sets the ledger_dts of this CustomerLoyaltyLedger.

        Ledger date  # noqa: E501

        :param ledger_dts: The ledger_dts of this CustomerLoyaltyLedger.  # noqa: E501
        :type: str
        """

        self._ledger_dts = ledger_dts

    @property
    def loyalty_campaign_oid(self):
        """Gets the loyalty_campaign_oid of this CustomerLoyaltyLedger.  # noqa: E501

        Loyalty campaign oid  # noqa: E501

        :return: The loyalty_campaign_oid of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: int
        """
        return self._loyalty_campaign_oid

    @loyalty_campaign_oid.setter
    def loyalty_campaign_oid(self, loyalty_campaign_oid):
        """Sets the loyalty_campaign_oid of this CustomerLoyaltyLedger.

        Loyalty campaign oid  # noqa: E501

        :param loyalty_campaign_oid: The loyalty_campaign_oid of this CustomerLoyaltyLedger.  # noqa: E501
        :type: int
        """

        self._loyalty_campaign_oid = loyalty_campaign_oid

    @property
    def loyalty_ledger_oid(self):
        """Gets the loyalty_ledger_oid of this CustomerLoyaltyLedger.  # noqa: E501

        Loyalty ledger oid  # noqa: E501

        :return: The loyalty_ledger_oid of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: int
        """
        return self._loyalty_ledger_oid

    @loyalty_ledger_oid.setter
    def loyalty_ledger_oid(self, loyalty_ledger_oid):
        """Sets the loyalty_ledger_oid of this CustomerLoyaltyLedger.

        Loyalty ledger oid  # noqa: E501

        :param loyalty_ledger_oid: The loyalty_ledger_oid of this CustomerLoyaltyLedger.  # noqa: E501
        :type: int
        """

        self._loyalty_ledger_oid = loyalty_ledger_oid

    @property
    def loyalty_points(self):
        """Gets the loyalty_points of this CustomerLoyaltyLedger.  # noqa: E501

        Loyalty points  # noqa: E501

        :return: The loyalty_points of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: int
        """
        return self._loyalty_points

    @loyalty_points.setter
    def loyalty_points(self, loyalty_points):
        """Sets the loyalty_points of this CustomerLoyaltyLedger.

        Loyalty points  # noqa: E501

        :param loyalty_points: The loyalty_points of this CustomerLoyaltyLedger.  # noqa: E501
        :type: int
        """

        self._loyalty_points = loyalty_points

    @property
    def modified_by(self):
        """Gets the modified_by of this CustomerLoyaltyLedger.  # noqa: E501

        Modified By  # noqa: E501

        :return: The modified_by of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this CustomerLoyaltyLedger.

        Modified By  # noqa: E501

        :param modified_by: The modified_by of this CustomerLoyaltyLedger.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def modified_dts(self):
        """Gets the modified_dts of this CustomerLoyaltyLedger.  # noqa: E501

        Modified date  # noqa: E501

        :return: The modified_dts of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: str
        """
        return self._modified_dts

    @modified_dts.setter
    def modified_dts(self, modified_dts):
        """Sets the modified_dts of this CustomerLoyaltyLedger.

        Modified date  # noqa: E501

        :param modified_dts: The modified_dts of this CustomerLoyaltyLedger.  # noqa: E501
        :type: str
        """

        self._modified_dts = modified_dts

    @property
    def order_id(self):
        """Gets the order_id of this CustomerLoyaltyLedger.  # noqa: E501

        Order Id  # noqa: E501

        :return: The order_id of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CustomerLoyaltyLedger.

        Order Id  # noqa: E501

        :param order_id: The order_id of this CustomerLoyaltyLedger.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def quantity(self):
        """Gets the quantity of this CustomerLoyaltyLedger.  # noqa: E501

        Quantity  # noqa: E501

        :return: The quantity of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CustomerLoyaltyLedger.

        Quantity  # noqa: E501

        :param quantity: The quantity of this CustomerLoyaltyLedger.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def vesting_dts(self):
        """Gets the vesting_dts of this CustomerLoyaltyLedger.  # noqa: E501

        Vesting date  # noqa: E501

        :return: The vesting_dts of this CustomerLoyaltyLedger.  # noqa: E501
        :rtype: str
        """
        return self._vesting_dts

    @vesting_dts.setter
    def vesting_dts(self, vesting_dts):
        """Sets the vesting_dts of this CustomerLoyaltyLedger.

        Vesting date  # noqa: E501

        :param vesting_dts: The vesting_dts of this CustomerLoyaltyLedger.  # noqa: E501
        :type: str
        """

        self._vesting_dts = vesting_dts

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
        if issubclass(CustomerLoyaltyLedger, dict):
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
        if not isinstance(other, CustomerLoyaltyLedger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
