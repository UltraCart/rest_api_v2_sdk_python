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
from ultracart.apis.storefront_api import StorefrontApi


class TestStorefrontApi(unittest.TestCase):
    """ StorefrontApi unit test stubs """

    def setUp(self):
        self.api = ultracart.apis.storefront_api.StorefrontApi()

    def tearDown(self):
        pass

    def test_add_to_library(self):
        """
        Test case for add_to_library

        Add to library
        """
        pass

    def test_apply_to_store_front(self):
        """
        Test case for apply_to_store_front

        Apply library item to storefront.
        """
        pass

    def test_archive_email_list(self):
        """
        Test case for archive_email_list

        Archive email list
        """
        pass

    def test_archive_email_segment(self):
        """
        Test case for archive_email_segment

        Archive email segment
        """
        pass

    def test_back_populate_email_flow(self):
        """
        Test case for back_populate_email_flow

        Back populate email flow
        """
        pass

    def test_check_download_email_segment(self):
        """
        Test case for check_download_email_segment

        Check download of email segment
        """
        pass

    def test_clone_email_campaign(self):
        """
        Test case for clone_email_campaign

        Clone email campaign
        """
        pass

    def test_clone_email_flow(self):
        """
        Test case for clone_email_flow

        Clone email flow
        """
        pass

    def test_clone_library_item(self):
        """
        Test case for clone_library_item

        Clone public library item.
        """
        pass

    def test_create_email_sending_domain(self):
        """
        Test case for create_email_sending_domain

        Create email campaign
        """
        pass

    def test_delete_email_commseq_stat(self):
        """
        Test case for delete_email_commseq_stat

        Delete communication sequence stats
        """
        pass

    def test_delete_email_email(self):
        """
        Test case for delete_email_email

        Delete email email
        """
        pass

    def test_delete_email_list_customer(self):
        """
        Test case for delete_email_list_customer

        Delete email list customer
        """
        pass

    def test_delete_email_postcard(self):
        """
        Test case for delete_email_postcard

        Delete email postcard
        """
        pass

    def test_delete_email_sending_domain(self):
        """
        Test case for delete_email_sending_domain

        delete email campaign
        """
        pass

    def test_delete_experiment(self):
        """
        Test case for delete_experiment

        Delete experiment
        """
        pass

    def test_delete_library_item(self):
        """
        Test case for delete_library_item

        Delete library item
        """
        pass

    def test_duplicate_library_item(self):
        """
        Test case for duplicate_library_item

        Duplicate library item.
        """
        pass

    def test_geocode_address(self):
        """
        Test case for geocode_address

        Obtain lat/long for an address
        """
        pass

    def test_get_countries(self):
        """
        Test case for get_countries

        Get countries
        """
        pass

    def test_get_editor_token(self):
        """
        Test case for get_editor_token

        Gets editor token
        """
        pass

    def test_get_email_base_templates(self):
        """
        Test case for get_email_base_templates

        Get email communication base templates
        """
        pass

    def test_get_email_campaign(self):
        """
        Test case for get_email_campaign

        Get email campaign
        """
        pass

    def test_get_email_campaigns(self):
        """
        Test case for get_email_campaigns

        Get email campaigns
        """
        pass

    def test_get_email_campaigns_with_stats(self):
        """
        Test case for get_email_campaigns_with_stats

        Get email campaigns with stats
        """
        pass

    def test_get_email_commseq(self):
        """
        Test case for get_email_commseq

        Get email commseq
        """
        pass

    def test_get_email_commseq_email_stats(self):
        """
        Test case for get_email_commseq_email_stats

        Get email communication sequence emails stats
        """
        pass

    def test_get_email_commseq_postcard_stats(self):
        """
        Test case for get_email_commseq_postcard_stats

        Get email communication sequence postcard stats
        """
        pass

    def test_get_email_commseq_stat_overall(self):
        """
        Test case for get_email_commseq_stat_overall

        Get communication sequence stats overall
        """
        pass

    def test_get_email_commseq_step_stats(self):
        """
        Test case for get_email_commseq_step_stats

        Get email communication sequence step stats
        """
        pass

    def test_get_email_commseq_step_waiting(self):
        """
        Test case for get_email_commseq_step_waiting

        Get email communication sequence customers waiting at each requested step
        """
        pass

    def test_get_email_commseqs(self):
        """
        Test case for get_email_commseqs

        Get email commseqs
        """
        pass

    def test_get_email_customer_editor_url(self):
        """
        Test case for get_email_customer_editor_url

        Get customers editor URL
        """
        pass

    def test_get_email_customers(self):
        """
        Test case for get_email_customers

        Get email customers
        """
        pass

    def test_get_email_dashboard_activity(self):
        """
        Test case for get_email_dashboard_activity

        Get email dashboard activity
        """
        pass

    def test_get_email_dashboard_stats(self):
        """
        Test case for get_email_dashboard_stats

        Get dashboard stats
        """
        pass

    def test_get_email_email(self):
        """
        Test case for get_email_email

        Get email email
        """
        pass

    def test_get_email_email_clicks(self):
        """
        Test case for get_email_email_clicks

        Get email email clicks
        """
        pass

    def test_get_email_email_customer_editor_url(self):
        """
        Test case for get_email_email_customer_editor_url

        Get email order customer editor url
        """
        pass

    def test_get_email_email_orders(self):
        """
        Test case for get_email_email_orders

        Get email email orders
        """
        pass

    def test_get_email_emails(self):
        """
        Test case for get_email_emails

        Get email emails
        """
        pass

    def test_get_email_emails_multiple(self):
        """
        Test case for get_email_emails_multiple

        Get email emails multiple
        """
        pass

    def test_get_email_flow(self):
        """
        Test case for get_email_flow

        Get email flow
        """
        pass

    def test_get_email_flows(self):
        """
        Test case for get_email_flows

        Get email flows
        """
        pass

    def test_get_email_global_settings(self):
        """
        Test case for get_email_global_settings

        Get email globalsettings
        """
        pass

    def test_get_email_list(self):
        """
        Test case for get_email_list

        Get email list
        """
        pass

    def test_get_email_list_customer_editor_url(self):
        """
        Test case for get_email_list_customer_editor_url

        Get email list customer editor url
        """
        pass

    def test_get_email_list_customers(self):
        """
        Test case for get_email_list_customers

        Get email list customers
        """
        pass

    def test_get_email_lists(self):
        """
        Test case for get_email_lists

        Get email lists
        """
        pass

    def test_get_email_performance(self):
        """
        Test case for get_email_performance

        Get email performance
        """
        pass

    def test_get_email_plan(self):
        """
        Test case for get_email_plan

        Get email plan
        """
        pass

    def test_get_email_postcard(self):
        """
        Test case for get_email_postcard

        Get email postcard
        """
        pass

    def test_get_email_postcards(self):
        """
        Test case for get_email_postcards

        Get email postcards
        """
        pass

    def test_get_email_postcards_multiple(self):
        """
        Test case for get_email_postcards_multiple

        Get email postcards multiple
        """
        pass

    def test_get_email_segment(self):
        """
        Test case for get_email_segment

        Get email segment
        """
        pass

    def test_get_email_segment_customer_editor_url(self):
        """
        Test case for get_email_segment_customer_editor_url

        Get email segment customers editor URL
        """
        pass

    def test_get_email_segment_customers(self):
        """
        Test case for get_email_segment_customers

        Get email segment customers
        """
        pass

    def test_get_email_segments(self):
        """
        Test case for get_email_segments

        Get email segments
        """
        pass

    def test_get_email_sending_domain(self):
        """
        Test case for get_email_sending_domain

        Get email sending domain
        """
        pass

    def test_get_email_sending_domain_status(self):
        """
        Test case for get_email_sending_domain_status

        Get email sending domain status
        """
        pass

    def test_get_email_sending_domains(self):
        """
        Test case for get_email_sending_domains

        Get email sending domains
        """
        pass

    def test_get_email_settings(self):
        """
        Test case for get_email_settings

        Get email settings
        """
        pass

    def test_get_email_template(self):
        """
        Test case for get_email_template

        Get email template
        """
        pass

    def test_get_email_templates(self):
        """
        Test case for get_email_templates

        Get email templates
        """
        pass

    def test_get_email_third_party_providers(self):
        """
        Test case for get_email_third_party_providers

        Get a list of third party email providers
        """
        pass

    def test_get_experiments(self):
        """
        Test case for get_experiments

        Get experiments
        """
        pass

    def test_get_histogram_property_names(self):
        """
        Test case for get_histogram_property_names

        Get histogram property names
        """
        pass

    def test_get_histogram_property_values(self):
        """
        Test case for get_histogram_property_values

        Get histogram property values
        """
        pass

    def test_get_library_items_by_query(self):
        """
        Test case for get_library_items_by_query

        Retrieve library items
        """
        pass

    def test_get_transaction_email(self):
        """
        Test case for get_transaction_email

        Gets a transaction email object
        """
        pass

    def test_get_transaction_email_list(self):
        """
        Test case for get_transaction_email_list

        Gets a list of transaction email names
        """
        pass

    def test_global_unsubscribe(self):
        """
        Test case for global_unsubscribe

        Globally unsubscribe a customer
        """
        pass

    def test_import_email_third_party_provider_list(self):
        """
        Test case for import_email_third_party_provider_list

        Import a third party provider list
        """
        pass

    def test_insert_email_campaign(self):
        """
        Test case for insert_email_campaign

        Insert email campaign
        """
        pass

    def test_insert_email_commseq(self):
        """
        Test case for insert_email_commseq

        Insert email commseq
        """
        pass

    def test_insert_email_email(self):
        """
        Test case for insert_email_email

        Insert email email
        """
        pass

    def test_insert_email_flow(self):
        """
        Test case for insert_email_flow

        Insert email flow
        """
        pass

    def test_insert_email_list(self):
        """
        Test case for insert_email_list

        Insert email list
        """
        pass

    def test_insert_email_postcard(self):
        """
        Test case for insert_email_postcard

        Insert email postcard
        """
        pass

    def test_insert_email_segment(self):
        """
        Test case for insert_email_segment

        Insert email segment
        """
        pass

    def test_prepare_download_email_segment(self):
        """
        Test case for prepare_download_email_segment

        Prepare download of email segment
        """
        pass

    def test_release_email_commseq_step_waiting(self):
        """
        Test case for release_email_commseq_step_waiting

        Release email communication sequence customers waiting at the specified step
        """
        pass

    def test_review(self):
        """
        Test case for review

        Request a review of an email
        """
        pass

    def test_search(self):
        """
        Test case for search

        Searches for all matching values
        """
        pass

    def test_search_email_list_customers(self):
        """
        Test case for search_email_list_customers

        Search email list customers
        """
        pass

    def test_search_email_segment_customers(self):
        """
        Test case for search_email_segment_customers

        Search email segment customers
        """
        pass

    def test_send_email_test(self):
        """
        Test case for send_email_test

        Send email test
        """
        pass

    def test_send_postcard_test(self):
        """
        Test case for send_postcard_test

        Send postcard test
        """
        pass

    def test_start_email_campaign(self):
        """
        Test case for start_email_campaign

        Start email campaign
        """
        pass

    def test_subscribe_to_email_list(self):
        """
        Test case for subscribe_to_email_list

        Subscribe customers to email list
        """
        pass

    def test_update_email_campaign(self):
        """
        Test case for update_email_campaign

        Update email campaign
        """
        pass

    def test_update_email_commseq(self):
        """
        Test case for update_email_commseq

        Update email commseq
        """
        pass

    def test_update_email_customer(self):
        """
        Test case for update_email_customer

        Update email customer
        """
        pass

    def test_update_email_email(self):
        """
        Test case for update_email_email

        Update email email
        """
        pass

    def test_update_email_flow(self):
        """
        Test case for update_email_flow

        Update email flow
        """
        pass

    def test_update_email_global_settings(self):
        """
        Test case for update_email_global_settings

        Update email global settings
        """
        pass

    def test_update_email_list(self):
        """
        Test case for update_email_list

        Update email list
        """
        pass

    def test_update_email_plan(self):
        """
        Test case for update_email_plan

        Update email plan
        """
        pass

    def test_update_email_postcard(self):
        """
        Test case for update_email_postcard

        Update email postcard
        """
        pass

    def test_update_email_segment(self):
        """
        Test case for update_email_segment

        Update email segment
        """
        pass

    def test_update_email_settings(self):
        """
        Test case for update_email_settings

        Update email settings
        """
        pass

    def test_update_experiment(self):
        """
        Test case for update_experiment

        Update experiment
        """
        pass

    def test_update_library_item(self):
        """
        Test case for update_library_item

        Update library item. Note that only certain fields may be updated via this method.
        """
        pass

    def test_update_transaction_email(self):
        """
        Test case for update_transaction_email

        Updates a transaction email object
        """
        pass


if __name__ == '__main__':
    unittest.main()
