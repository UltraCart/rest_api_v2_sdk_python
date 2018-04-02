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
from ultracart.apis.customer_api import CustomerApi


class TestCustomerApi(unittest.TestCase):
    """ CustomerApi unit test stubs """

    def setUp(self):
        self.api = ultracart.apis.customer_api.CustomerApi()

    def tearDown(self):
        pass

    def test_delete_customer(self):
        """
        Test case for delete_customer

        Delete a customer
        """
        pass

    def test_get_customer(self):
        """
        Test case for get_customer

        Retrieve a customer
        """
        pass

    def test_get_customers(self):
        """
        Test case for get_customers

        Retrieve customers
        """
        pass

    def test_get_customers_by_query(self):
        """
        Test case for get_customers_by_query

        Retrieve customers by query
        """
        pass

    def test_get_customers_for_data_tables(self):
        """
        Test case for get_customers_for_data_tables

        Retrieve customers for DataTables plugin
        """
        pass

    def test_get_editor_values(self):
        """
        Test case for get_editor_values

        Retrieve values needed for a customer profile editor
        """
        pass

    def test_insert_customer(self):
        """
        Test case for insert_customer

        Insert a customer
        """
        pass

    def test_update_customer(self):
        """
        Test case for update_customer

        Update a customer
        """
        pass


if __name__ == '__main__':
    unittest.main()
