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


class OrderPayment(object):
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
        'check': 'OrderPaymentCheck',
        'credit_card': 'OrderPaymentCreditCard',
        'echeck': 'OrderPaymentECheck',
        'hold_for_fraud_review': 'bool',
        'insurance': 'OrderPaymentInsurance',
        'payment_dts': 'str',
        'payment_method': 'str',
        'payment_method_accounting_code': 'str',
        'payment_method_deposit_to_account': 'str',
        'payment_status': 'str',
        'purchase_order': 'OrderPaymentPurchaseOrder',
        'rotating_transaction_gateway_code': 'str',
        'surcharge': 'Currency',
        'surcharge_accounting_code': 'str',
        'surcharge_transaction_fee': 'float',
        'surcharge_transaction_percentage': 'float',
        'test_order': 'bool',
        'transactions': 'list[OrderPaymentTransaction]'
    }

    attribute_map = {
        'check': 'check',
        'credit_card': 'credit_card',
        'echeck': 'echeck',
        'hold_for_fraud_review': 'hold_for_fraud_review',
        'insurance': 'insurance',
        'payment_dts': 'payment_dts',
        'payment_method': 'payment_method',
        'payment_method_accounting_code': 'payment_method_accounting_code',
        'payment_method_deposit_to_account': 'payment_method_deposit_to_account',
        'payment_status': 'payment_status',
        'purchase_order': 'purchase_order',
        'rotating_transaction_gateway_code': 'rotating_transaction_gateway_code',
        'surcharge': 'surcharge',
        'surcharge_accounting_code': 'surcharge_accounting_code',
        'surcharge_transaction_fee': 'surcharge_transaction_fee',
        'surcharge_transaction_percentage': 'surcharge_transaction_percentage',
        'test_order': 'test_order',
        'transactions': 'transactions'
    }

    def __init__(self, check=None, credit_card=None, echeck=None, hold_for_fraud_review=None, insurance=None, payment_dts=None, payment_method=None, payment_method_accounting_code=None, payment_method_deposit_to_account=None, payment_status=None, purchase_order=None, rotating_transaction_gateway_code=None, surcharge=None, surcharge_accounting_code=None, surcharge_transaction_fee=None, surcharge_transaction_percentage=None, test_order=None, transactions=None):  # noqa: E501
        """OrderPayment - a model defined in Swagger"""  # noqa: E501

        self._check = None
        self._credit_card = None
        self._echeck = None
        self._hold_for_fraud_review = None
        self._insurance = None
        self._payment_dts = None
        self._payment_method = None
        self._payment_method_accounting_code = None
        self._payment_method_deposit_to_account = None
        self._payment_status = None
        self._purchase_order = None
        self._rotating_transaction_gateway_code = None
        self._surcharge = None
        self._surcharge_accounting_code = None
        self._surcharge_transaction_fee = None
        self._surcharge_transaction_percentage = None
        self._test_order = None
        self._transactions = None
        self.discriminator = None

        if check is not None:
            self.check = check
        if credit_card is not None:
            self.credit_card = credit_card
        if echeck is not None:
            self.echeck = echeck
        if hold_for_fraud_review is not None:
            self.hold_for_fraud_review = hold_for_fraud_review
        if insurance is not None:
            self.insurance = insurance
        if payment_dts is not None:
            self.payment_dts = payment_dts
        if payment_method is not None:
            self.payment_method = payment_method
        if payment_method_accounting_code is not None:
            self.payment_method_accounting_code = payment_method_accounting_code
        if payment_method_deposit_to_account is not None:
            self.payment_method_deposit_to_account = payment_method_deposit_to_account
        if payment_status is not None:
            self.payment_status = payment_status
        if purchase_order is not None:
            self.purchase_order = purchase_order
        if rotating_transaction_gateway_code is not None:
            self.rotating_transaction_gateway_code = rotating_transaction_gateway_code
        if surcharge is not None:
            self.surcharge = surcharge
        if surcharge_accounting_code is not None:
            self.surcharge_accounting_code = surcharge_accounting_code
        if surcharge_transaction_fee is not None:
            self.surcharge_transaction_fee = surcharge_transaction_fee
        if surcharge_transaction_percentage is not None:
            self.surcharge_transaction_percentage = surcharge_transaction_percentage
        if test_order is not None:
            self.test_order = test_order
        if transactions is not None:
            self.transactions = transactions

    @property
    def check(self):
        """Gets the check of this OrderPayment.  # noqa: E501


        :return: The check of this OrderPayment.  # noqa: E501
        :rtype: OrderPaymentCheck
        """
        return self._check

    @check.setter
    def check(self, check):
        """Sets the check of this OrderPayment.


        :param check: The check of this OrderPayment.  # noqa: E501
        :type: OrderPaymentCheck
        """

        self._check = check

    @property
    def credit_card(self):
        """Gets the credit_card of this OrderPayment.  # noqa: E501


        :return: The credit_card of this OrderPayment.  # noqa: E501
        :rtype: OrderPaymentCreditCard
        """
        return self._credit_card

    @credit_card.setter
    def credit_card(self, credit_card):
        """Sets the credit_card of this OrderPayment.


        :param credit_card: The credit_card of this OrderPayment.  # noqa: E501
        :type: OrderPaymentCreditCard
        """

        self._credit_card = credit_card

    @property
    def echeck(self):
        """Gets the echeck of this OrderPayment.  # noqa: E501


        :return: The echeck of this OrderPayment.  # noqa: E501
        :rtype: OrderPaymentECheck
        """
        return self._echeck

    @echeck.setter
    def echeck(self, echeck):
        """Sets the echeck of this OrderPayment.


        :param echeck: The echeck of this OrderPayment.  # noqa: E501
        :type: OrderPaymentECheck
        """

        self._echeck = echeck

    @property
    def hold_for_fraud_review(self):
        """Gets the hold_for_fraud_review of this OrderPayment.  # noqa: E501

        True if order has been held for fraud review  # noqa: E501

        :return: The hold_for_fraud_review of this OrderPayment.  # noqa: E501
        :rtype: bool
        """
        return self._hold_for_fraud_review

    @hold_for_fraud_review.setter
    def hold_for_fraud_review(self, hold_for_fraud_review):
        """Sets the hold_for_fraud_review of this OrderPayment.

        True if order has been held for fraud review  # noqa: E501

        :param hold_for_fraud_review: The hold_for_fraud_review of this OrderPayment.  # noqa: E501
        :type: bool
        """

        self._hold_for_fraud_review = hold_for_fraud_review

    @property
    def insurance(self):
        """Gets the insurance of this OrderPayment.  # noqa: E501


        :return: The insurance of this OrderPayment.  # noqa: E501
        :rtype: OrderPaymentInsurance
        """
        return self._insurance

    @insurance.setter
    def insurance(self, insurance):
        """Sets the insurance of this OrderPayment.


        :param insurance: The insurance of this OrderPayment.  # noqa: E501
        :type: OrderPaymentInsurance
        """

        self._insurance = insurance

    @property
    def payment_dts(self):
        """Gets the payment_dts of this OrderPayment.  # noqa: E501

        Date/time that the payment was successfully processed, for new orders, this field is only considered if channel_partner.skip_payment_processing is true  # noqa: E501

        :return: The payment_dts of this OrderPayment.  # noqa: E501
        :rtype: str
        """
        return self._payment_dts

    @payment_dts.setter
    def payment_dts(self, payment_dts):
        """Sets the payment_dts of this OrderPayment.

        Date/time that the payment was successfully processed, for new orders, this field is only considered if channel_partner.skip_payment_processing is true  # noqa: E501

        :param payment_dts: The payment_dts of this OrderPayment.  # noqa: E501
        :type: str
        """

        self._payment_dts = payment_dts

    @property
    def payment_method(self):
        """Gets the payment_method of this OrderPayment.  # noqa: E501

        Payment method  # noqa: E501

        :return: The payment_method of this OrderPayment.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this OrderPayment.

        Payment method  # noqa: E501

        :param payment_method: The payment_method of this OrderPayment.  # noqa: E501
        :type: str
        """
        allowed_values = ["Affirm", "Amazon", "Amazon SC", "Cash", "Check", "COD", "Credit Card", "eBay", "eCheck", "Insurance", "LoanHero", "Money Order", "PayPal", "Purchase Order", "Quote Request", "Unknown", "Wire Transfer", "Walmart"]  # noqa: E501
        if payment_method not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_method` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_method, allowed_values)
            )

        self._payment_method = payment_method

    @property
    def payment_method_accounting_code(self):
        """Gets the payment_method_accounting_code of this OrderPayment.  # noqa: E501

        Payment method QuickBooks code  # noqa: E501

        :return: The payment_method_accounting_code of this OrderPayment.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_accounting_code

    @payment_method_accounting_code.setter
    def payment_method_accounting_code(self, payment_method_accounting_code):
        """Sets the payment_method_accounting_code of this OrderPayment.

        Payment method QuickBooks code  # noqa: E501

        :param payment_method_accounting_code: The payment_method_accounting_code of this OrderPayment.  # noqa: E501
        :type: str
        """

        self._payment_method_accounting_code = payment_method_accounting_code

    @property
    def payment_method_deposit_to_account(self):
        """Gets the payment_method_deposit_to_account of this OrderPayment.  # noqa: E501

        Payment method QuickBooks deposit account  # noqa: E501

        :return: The payment_method_deposit_to_account of this OrderPayment.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_deposit_to_account

    @payment_method_deposit_to_account.setter
    def payment_method_deposit_to_account(self, payment_method_deposit_to_account):
        """Sets the payment_method_deposit_to_account of this OrderPayment.

        Payment method QuickBooks deposit account  # noqa: E501

        :param payment_method_deposit_to_account: The payment_method_deposit_to_account of this OrderPayment.  # noqa: E501
        :type: str
        """

        self._payment_method_deposit_to_account = payment_method_deposit_to_account

    @property
    def payment_status(self):
        """Gets the payment_status of this OrderPayment.  # noqa: E501

        Payment status  # noqa: E501

        :return: The payment_status of this OrderPayment.  # noqa: E501
        :rtype: str
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        """Sets the payment_status of this OrderPayment.

        Payment status  # noqa: E501

        :param payment_status: The payment_status of this OrderPayment.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unprocessed", "Authorized", "Capture Failed", "Processed", "Declined", "Voided", "Refunded", "Skipped"]  # noqa: E501
        if payment_status not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_status` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_status, allowed_values)
            )

        self._payment_status = payment_status

    @property
    def purchase_order(self):
        """Gets the purchase_order of this OrderPayment.  # noqa: E501


        :return: The purchase_order of this OrderPayment.  # noqa: E501
        :rtype: OrderPaymentPurchaseOrder
        """
        return self._purchase_order

    @purchase_order.setter
    def purchase_order(self, purchase_order):
        """Sets the purchase_order of this OrderPayment.


        :param purchase_order: The purchase_order of this OrderPayment.  # noqa: E501
        :type: OrderPaymentPurchaseOrder
        """

        self._purchase_order = purchase_order

    @property
    def rotating_transaction_gateway_code(self):
        """Gets the rotating_transaction_gateway_code of this OrderPayment.  # noqa: E501

        Rotating transaction gateway code used to process this order  # noqa: E501

        :return: The rotating_transaction_gateway_code of this OrderPayment.  # noqa: E501
        :rtype: str
        """
        return self._rotating_transaction_gateway_code

    @rotating_transaction_gateway_code.setter
    def rotating_transaction_gateway_code(self, rotating_transaction_gateway_code):
        """Sets the rotating_transaction_gateway_code of this OrderPayment.

        Rotating transaction gateway code used to process this order  # noqa: E501

        :param rotating_transaction_gateway_code: The rotating_transaction_gateway_code of this OrderPayment.  # noqa: E501
        :type: str
        """

        self._rotating_transaction_gateway_code = rotating_transaction_gateway_code

    @property
    def surcharge(self):
        """Gets the surcharge of this OrderPayment.  # noqa: E501


        :return: The surcharge of this OrderPayment.  # noqa: E501
        :rtype: Currency
        """
        return self._surcharge

    @surcharge.setter
    def surcharge(self, surcharge):
        """Sets the surcharge of this OrderPayment.


        :param surcharge: The surcharge of this OrderPayment.  # noqa: E501
        :type: Currency
        """

        self._surcharge = surcharge

    @property
    def surcharge_accounting_code(self):
        """Gets the surcharge_accounting_code of this OrderPayment.  # noqa: E501

        Surcharge accounting code  # noqa: E501

        :return: The surcharge_accounting_code of this OrderPayment.  # noqa: E501
        :rtype: str
        """
        return self._surcharge_accounting_code

    @surcharge_accounting_code.setter
    def surcharge_accounting_code(self, surcharge_accounting_code):
        """Sets the surcharge_accounting_code of this OrderPayment.

        Surcharge accounting code  # noqa: E501

        :param surcharge_accounting_code: The surcharge_accounting_code of this OrderPayment.  # noqa: E501
        :type: str
        """

        self._surcharge_accounting_code = surcharge_accounting_code

    @property
    def surcharge_transaction_fee(self):
        """Gets the surcharge_transaction_fee of this OrderPayment.  # noqa: E501

        Surcharge transaction fee  # noqa: E501

        :return: The surcharge_transaction_fee of this OrderPayment.  # noqa: E501
        :rtype: float
        """
        return self._surcharge_transaction_fee

    @surcharge_transaction_fee.setter
    def surcharge_transaction_fee(self, surcharge_transaction_fee):
        """Sets the surcharge_transaction_fee of this OrderPayment.

        Surcharge transaction fee  # noqa: E501

        :param surcharge_transaction_fee: The surcharge_transaction_fee of this OrderPayment.  # noqa: E501
        :type: float
        """

        self._surcharge_transaction_fee = surcharge_transaction_fee

    @property
    def surcharge_transaction_percentage(self):
        """Gets the surcharge_transaction_percentage of this OrderPayment.  # noqa: E501

        Surcharge transaction percentage  # noqa: E501

        :return: The surcharge_transaction_percentage of this OrderPayment.  # noqa: E501
        :rtype: float
        """
        return self._surcharge_transaction_percentage

    @surcharge_transaction_percentage.setter
    def surcharge_transaction_percentage(self, surcharge_transaction_percentage):
        """Sets the surcharge_transaction_percentage of this OrderPayment.

        Surcharge transaction percentage  # noqa: E501

        :param surcharge_transaction_percentage: The surcharge_transaction_percentage of this OrderPayment.  # noqa: E501
        :type: float
        """

        self._surcharge_transaction_percentage = surcharge_transaction_percentage

    @property
    def test_order(self):
        """Gets the test_order of this OrderPayment.  # noqa: E501

        True if this is a test order  # noqa: E501

        :return: The test_order of this OrderPayment.  # noqa: E501
        :rtype: bool
        """
        return self._test_order

    @test_order.setter
    def test_order(self, test_order):
        """Sets the test_order of this OrderPayment.

        True if this is a test order  # noqa: E501

        :param test_order: The test_order of this OrderPayment.  # noqa: E501
        :type: bool
        """

        self._test_order = test_order

    @property
    def transactions(self):
        """Gets the transactions of this OrderPayment.  # noqa: E501

        Transactions associated with processing this payment  # noqa: E501

        :return: The transactions of this OrderPayment.  # noqa: E501
        :rtype: list[OrderPaymentTransaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this OrderPayment.

        Transactions associated with processing this payment  # noqa: E501

        :param transactions: The transactions of this OrderPayment.  # noqa: E501
        :type: list[OrderPaymentTransaction]
        """

        self._transactions = transactions

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
        if issubclass(OrderPayment, dict):
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
        if not isinstance(other, OrderPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
