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


class CartPayment(object):
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
        'affirm': 'CartPaymentAffirm',
        'amazon': 'CartPaymentAmazon',
        'check': 'CartPaymentCheck',
        'credit_card': 'CartPaymentCreditCard',
        'payment_method': 'str',
        'purchase_order': 'CartPaymentPurchaseOrder',
        'rtg_code': 'str'
    }

    attribute_map = {
        'affirm': 'affirm',
        'amazon': 'amazon',
        'check': 'check',
        'credit_card': 'credit_card',
        'payment_method': 'payment_method',
        'purchase_order': 'purchase_order',
        'rtg_code': 'rtg_code'
    }

    def __init__(self, affirm=None, amazon=None, check=None, credit_card=None, payment_method=None, purchase_order=None, rtg_code=None):
        """
        CartPayment - a model defined in Swagger
        """

        self._affirm = None
        self._amazon = None
        self._check = None
        self._credit_card = None
        self._payment_method = None
        self._purchase_order = None
        self._rtg_code = None
        self.discriminator = None

        if affirm is not None:
          self.affirm = affirm
        if amazon is not None:
          self.amazon = amazon
        if check is not None:
          self.check = check
        if credit_card is not None:
          self.credit_card = credit_card
        if payment_method is not None:
          self.payment_method = payment_method
        if purchase_order is not None:
          self.purchase_order = purchase_order
        if rtg_code is not None:
          self.rtg_code = rtg_code

    @property
    def affirm(self):
        """
        Gets the affirm of this CartPayment.

        :return: The affirm of this CartPayment.
        :rtype: CartPaymentAffirm
        """
        return self._affirm

    @affirm.setter
    def affirm(self, affirm):
        """
        Sets the affirm of this CartPayment.

        :param affirm: The affirm of this CartPayment.
        :type: CartPaymentAffirm
        """

        self._affirm = affirm

    @property
    def amazon(self):
        """
        Gets the amazon of this CartPayment.

        :return: The amazon of this CartPayment.
        :rtype: CartPaymentAmazon
        """
        return self._amazon

    @amazon.setter
    def amazon(self, amazon):
        """
        Sets the amazon of this CartPayment.

        :param amazon: The amazon of this CartPayment.
        :type: CartPaymentAmazon
        """

        self._amazon = amazon

    @property
    def check(self):
        """
        Gets the check of this CartPayment.

        :return: The check of this CartPayment.
        :rtype: CartPaymentCheck
        """
        return self._check

    @check.setter
    def check(self, check):
        """
        Sets the check of this CartPayment.

        :param check: The check of this CartPayment.
        :type: CartPaymentCheck
        """

        self._check = check

    @property
    def credit_card(self):
        """
        Gets the credit_card of this CartPayment.

        :return: The credit_card of this CartPayment.
        :rtype: CartPaymentCreditCard
        """
        return self._credit_card

    @credit_card.setter
    def credit_card(self, credit_card):
        """
        Sets the credit_card of this CartPayment.

        :param credit_card: The credit_card of this CartPayment.
        :type: CartPaymentCreditCard
        """

        self._credit_card = credit_card

    @property
    def payment_method(self):
        """
        Gets the payment_method of this CartPayment.
        Payment method

        :return: The payment_method of this CartPayment.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this CartPayment.
        Payment method

        :param payment_method: The payment_method of this CartPayment.
        :type: str
        """

        self._payment_method = payment_method

    @property
    def purchase_order(self):
        """
        Gets the purchase_order of this CartPayment.

        :return: The purchase_order of this CartPayment.
        :rtype: CartPaymentPurchaseOrder
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """
        Sets the purchase_order of this CartPayment.

        :param purchase_order: The purchase_order of this CartPayment.
        :type: CartPaymentPurchaseOrder
        """

        self._purchase_order = purchase_order

    @property
    def rtg_code(self):
        """
        Gets the rtg_code of this CartPayment.
        Rotating transaction gateway code

        :return: The rtg_code of this CartPayment.
        :rtype: str
        """
        return self._rtg_code

    @rtg_code.setter
    def rtg_code(self, rtg_code):
        """
        Sets the rtg_code of this CartPayment.
        Rotating transaction gateway code

        :param rtg_code: The rtg_code of this CartPayment.
        :type: str
        """

        self._rtg_code = rtg_code

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
        if not isinstance(other, CartPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
