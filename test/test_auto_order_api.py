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
from ultracart.apis.auto_order_api import AutoOrderApi


class TestAutoOrderApi(unittest.TestCase):
    """ AutoOrderApi unit test stubs """

    def setUp(self):
        self.api = ultracart.apis.auto_order_api.AutoOrderApi()

    def tearDown(self):
        pass

    def test_get_auto_order(self):
        """
        Test case for get_auto_order

        Retrieve an auto order
        """
        pass

    def test_get_auto_order_by_code(self):
        """
        Test case for get_auto_order_by_code

        Retrieve an auto order
        """
        pass

    def test_get_auto_order_by_reference_order_id(self):
        """
        Test case for get_auto_order_by_reference_order_id

        Retrieve an auto order
        """
        pass

    def test_get_auto_orders(self):
        """
        Test case for get_auto_orders

        Retrieve auto orders
        """
        pass

    def test_get_auto_orders_batch(self):
        """
        Test case for get_auto_orders_batch

        Retrieve auto order batch
        """
        pass

    def test_get_auto_orders_by_query(self):
        """
        Test case for get_auto_orders_by_query

        Retrieve auto orders
        """
        pass

    def test_update_auto_order(self):
        """
        Test case for update_auto_order

        Update an auto order
        """
        pass

    def test_update_auto_orders_batch(self):
        """
        Test case for update_auto_orders_batch

        Update multiple auto orders
        """
        pass


if __name__ == '__main__':
    unittest.main()
