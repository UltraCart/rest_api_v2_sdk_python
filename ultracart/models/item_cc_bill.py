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


class ItemCCBill(object):
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
        'ccbill_allowed_currencies': 'str',
        'ccbill_allowed_types': 'str',
        'ccbill_currency_code': 'str',
        'ccbill_form_name': 'str',
        'ccbill_subaccount_id': 'str',
        'ccbill_subscription_type_id': 'str'
    }

    attribute_map = {
        'ccbill_allowed_currencies': 'ccbill_allowed_currencies',
        'ccbill_allowed_types': 'ccbill_allowed_types',
        'ccbill_currency_code': 'ccbill_currency_code',
        'ccbill_form_name': 'ccbill_form_name',
        'ccbill_subaccount_id': 'ccbill_subaccount_id',
        'ccbill_subscription_type_id': 'ccbill_subscription_type_id'
    }

    def __init__(self, ccbill_allowed_currencies=None, ccbill_allowed_types=None, ccbill_currency_code=None, ccbill_form_name=None, ccbill_subaccount_id=None, ccbill_subscription_type_id=None):
        """
        ItemCCBill - a model defined in Swagger
        """

        self._ccbill_allowed_currencies = None
        self._ccbill_allowed_types = None
        self._ccbill_currency_code = None
        self._ccbill_form_name = None
        self._ccbill_subaccount_id = None
        self._ccbill_subscription_type_id = None
        self.discriminator = None

        if ccbill_allowed_currencies is not None:
          self.ccbill_allowed_currencies = ccbill_allowed_currencies
        if ccbill_allowed_types is not None:
          self.ccbill_allowed_types = ccbill_allowed_types
        if ccbill_currency_code is not None:
          self.ccbill_currency_code = ccbill_currency_code
        if ccbill_form_name is not None:
          self.ccbill_form_name = ccbill_form_name
        if ccbill_subaccount_id is not None:
          self.ccbill_subaccount_id = ccbill_subaccount_id
        if ccbill_subscription_type_id is not None:
          self.ccbill_subscription_type_id = ccbill_subscription_type_id

    @property
    def ccbill_allowed_currencies(self):
        """
        Gets the ccbill_allowed_currencies of this ItemCCBill.
        Allowed currencies

        :return: The ccbill_allowed_currencies of this ItemCCBill.
        :rtype: str
        """
        return self._ccbill_allowed_currencies

    @ccbill_allowed_currencies.setter
    def ccbill_allowed_currencies(self, ccbill_allowed_currencies):
        """
        Sets the ccbill_allowed_currencies of this ItemCCBill.
        Allowed currencies

        :param ccbill_allowed_currencies: The ccbill_allowed_currencies of this ItemCCBill.
        :type: str
        """

        self._ccbill_allowed_currencies = ccbill_allowed_currencies

    @property
    def ccbill_allowed_types(self):
        """
        Gets the ccbill_allowed_types of this ItemCCBill.
        Allowed types

        :return: The ccbill_allowed_types of this ItemCCBill.
        :rtype: str
        """
        return self._ccbill_allowed_types

    @ccbill_allowed_types.setter
    def ccbill_allowed_types(self, ccbill_allowed_types):
        """
        Sets the ccbill_allowed_types of this ItemCCBill.
        Allowed types

        :param ccbill_allowed_types: The ccbill_allowed_types of this ItemCCBill.
        :type: str
        """

        self._ccbill_allowed_types = ccbill_allowed_types

    @property
    def ccbill_currency_code(self):
        """
        Gets the ccbill_currency_code of this ItemCCBill.
        Currency code

        :return: The ccbill_currency_code of this ItemCCBill.
        :rtype: str
        """
        return self._ccbill_currency_code

    @ccbill_currency_code.setter
    def ccbill_currency_code(self, ccbill_currency_code):
        """
        Sets the ccbill_currency_code of this ItemCCBill.
        Currency code

        :param ccbill_currency_code: The ccbill_currency_code of this ItemCCBill.
        :type: str
        """

        self._ccbill_currency_code = ccbill_currency_code

    @property
    def ccbill_form_name(self):
        """
        Gets the ccbill_form_name of this ItemCCBill.
        Form name

        :return: The ccbill_form_name of this ItemCCBill.
        :rtype: str
        """
        return self._ccbill_form_name

    @ccbill_form_name.setter
    def ccbill_form_name(self, ccbill_form_name):
        """
        Sets the ccbill_form_name of this ItemCCBill.
        Form name

        :param ccbill_form_name: The ccbill_form_name of this ItemCCBill.
        :type: str
        """

        self._ccbill_form_name = ccbill_form_name

    @property
    def ccbill_subaccount_id(self):
        """
        Gets the ccbill_subaccount_id of this ItemCCBill.
        Sub-account id

        :return: The ccbill_subaccount_id of this ItemCCBill.
        :rtype: str
        """
        return self._ccbill_subaccount_id

    @ccbill_subaccount_id.setter
    def ccbill_subaccount_id(self, ccbill_subaccount_id):
        """
        Sets the ccbill_subaccount_id of this ItemCCBill.
        Sub-account id

        :param ccbill_subaccount_id: The ccbill_subaccount_id of this ItemCCBill.
        :type: str
        """

        self._ccbill_subaccount_id = ccbill_subaccount_id

    @property
    def ccbill_subscription_type_id(self):
        """
        Gets the ccbill_subscription_type_id of this ItemCCBill.
        Subscription type id

        :return: The ccbill_subscription_type_id of this ItemCCBill.
        :rtype: str
        """
        return self._ccbill_subscription_type_id

    @ccbill_subscription_type_id.setter
    def ccbill_subscription_type_id(self, ccbill_subscription_type_id):
        """
        Sets the ccbill_subscription_type_id of this ItemCCBill.
        Subscription type id

        :param ccbill_subscription_type_id: The ccbill_subscription_type_id of this ItemCCBill.
        :type: str
        """

        self._ccbill_subscription_type_id = ccbill_subscription_type_id

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
        if not isinstance(other, ItemCCBill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
