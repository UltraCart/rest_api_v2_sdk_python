# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import ultracart
from ultracart.rest import ApiException
from ultracart.apis.order_api import OrderApi


class TestOrderApi(unittest.TestCase):
    """ OrderApi unit test stubs """

    def setUp(self):
        self.api = ultracart.apis.order_api.OrderApi()

    def tearDown(self):
        pass

    def test_cancel_order(self):
        """
        Test case for cancel_order

        Cancel an order
        """
        pass

    def test_delete_order(self):
        """
        Test case for delete_order

        Delete an order
        """
        pass

    def test_format(self):
        """
        Test case for format

        Format order
        """
        pass

    def test_generate_order_token(self):
        """
        Test case for generate_order_token

        Generate an order token for a given order id
        """
        pass

    def test_get_accounts_receivable_retry_config(self):
        """
        Test case for get_accounts_receivable_retry_config

        Retrieve A/R Retry Configuration
        """
        pass

    def test_get_accounts_receivable_retry_stats(self):
        """
        Test case for get_accounts_receivable_retry_stats

        Retrieve A/R Retry Statistics
        """
        pass

    def test_get_order(self):
        """
        Test case for get_order

        Retrieve an order
        """
        pass

    def test_get_order_by_token(self):
        """
        Test case for get_order_by_token

        Retrieve an order using a token
        """
        pass

    def test_get_orders(self):
        """
        Test case for get_orders

        Retrieve orders
        """
        pass

    def test_get_orders_batch(self):
        """
        Test case for get_orders_batch

        Retrieve order batch
        """
        pass

    def test_get_orders_by_query(self):
        """
        Test case for get_orders_by_query

        Retrieve orders
        """
        pass

    def test_insert_order(self):
        """
        Test case for insert_order

        Insert an order
        """
        pass

    def test_refund_order(self):
        """
        Test case for refund_order

        Refund an order
        """
        pass

    def test_replacement(self):
        """
        Test case for replacement

        Replacement order
        """
        pass

    def test_resend_receipt(self):
        """
        Test case for resend_receipt

        Resend receipt
        """
        pass

    def test_resend_shipment_confirmation(self):
        """
        Test case for resend_shipment_confirmation

        Resend shipment confirmation
        """
        pass

    def test_update_accounts_receivable_retry_config(self):
        """
        Test case for update_accounts_receivable_retry_config

        Update A/R Retry Configuration
        """
        pass

    def test_update_order(self):
        """
        Test case for update_order

        Update an order
        """
        pass


if __name__ == '__main__':
    unittest.main()
