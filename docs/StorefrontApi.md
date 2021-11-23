# ultracart.StorefrontApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_to_library**](StorefrontApi.md#add_to_library) | **POST** /storefront/code_library | Add to library
[**apply_to_store_front**](StorefrontApi.md#apply_to_store_front) | **POST** /storefront/code_library/apply | Apply library item to storefront.
[**archive_email_list**](StorefrontApi.md#archive_email_list) | **POST** /storefront/{storefront_oid}/email/lists/{email_list_uuid}/archive | Archive email list
[**archive_email_segment**](StorefrontApi.md#archive_email_segment) | **POST** /storefront/{storefront_oid}/email/segments/{email_segment_uuid}/archive | Archive email segment
[**back_populate_email_flow**](StorefrontApi.md#back_populate_email_flow) | **POST** /storefront/{storefront_oid}/email/flows/{email_flow_uuid}/backfill | Back populate email flow
[**check_download_email_segment**](StorefrontApi.md#check_download_email_segment) | **POST** /storefront/{storefront_oid}/email/segments/{email_segment_uuid}/downloadPrepare/{email_segment_rebuild_uuid} | Check download of email segment
[**clone_email_campaign**](StorefrontApi.md#clone_email_campaign) | **POST** /storefront/{storefront_oid}/email/campaigns/{email_campaign_uuid}/clone | Clone email campaign
[**clone_email_flow**](StorefrontApi.md#clone_email_flow) | **POST** /storefront/{storefront_oid}/email/flows/{email_flow_uuid}/clone | Clone email flow
[**create_email_sending_domain**](StorefrontApi.md#create_email_sending_domain) | **POST** /storefront/email/sending_domains/{domain}/create | Create email campaign
[**create_twilio_account**](StorefrontApi.md#create_twilio_account) | **POST** /storefront/twilio/accounts | Create Twilio account
[**delete_email_campaign_folder**](StorefrontApi.md#delete_email_campaign_folder) | **DELETE** /storefront/{storefront_oid}/email/campaign_folders/{email_campaign_folder_uuid} | Delete email campaignFolder
[**delete_email_commseq_stat**](StorefrontApi.md#delete_email_commseq_stat) | **DELETE** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/stat | Delete communication sequence stats
[**delete_email_email**](StorefrontApi.md#delete_email_email) | **DELETE** /storefront/{storefront_oid}/email/emails/{commseq_email_uuid} | Delete email email
[**delete_email_flow_folder**](StorefrontApi.md#delete_email_flow_folder) | **DELETE** /storefront/{storefront_oid}/email/flow_folders/{email_flow_folder_uuid} | Delete email flowFolder
[**delete_email_list_customer**](StorefrontApi.md#delete_email_list_customer) | **DELETE** /storefront/{storefront_oid}/email/lists/{email_list_uuid}/customers/{email_customer_uuid} | Delete email list customer
[**delete_email_list_segment_folder**](StorefrontApi.md#delete_email_list_segment_folder) | **DELETE** /storefront/{storefront_oid}/email/list_segment_folders/{email_list_segment_folder_uuid} | Delete email ListSegmentFolder
[**delete_email_postcard**](StorefrontApi.md#delete_email_postcard) | **DELETE** /storefront/{storefront_oid}/email/postcards/{commseq_postcard_uuid} | Delete email postcard
[**delete_email_sending_domain**](StorefrontApi.md#delete_email_sending_domain) | **DELETE** /storefront/email/sending_domains/{domain} | delete email campaign
[**delete_experiment**](StorefrontApi.md#delete_experiment) | **DELETE** /storefront/{storefront_oid}/experiments/{storefront_experiment_oid} | Delete experiment
[**delete_heatmap**](StorefrontApi.md#delete_heatmap) | **DELETE** /storefront/{storefront_oid}/screen_recordings/heatmap | Delete screen recording heatmap
[**delete_library_item**](StorefrontApi.md#delete_library_item) | **DELETE** /storefront/code_library/{library_item_oid} | Delete library item
[**delete_library_item_published_versions**](StorefrontApi.md#delete_library_item_published_versions) | **DELETE** /storefront/code_library/{library_item_oid}/published_versions | Delete all published versions for a library item, including anything in review.
[**delete_screen_recording_segment**](StorefrontApi.md#delete_screen_recording_segment) | **DELETE** /storefront/{storefront_oid}/screen_recordings/segments/{screen_recording_segment_oid} | Delete screen recording segment
[**delete_twilio_account**](StorefrontApi.md#delete_twilio_account) | **DELETE** /storefront/twilio/accounts/{esp_twilio_uuid} | delete Twilio account
[**duplicate_library_item**](StorefrontApi.md#duplicate_library_item) | **POST** /storefront/code_library/{library_item_oid}/duplicate | Duplicate library item.
[**favorite_screen_recording**](StorefrontApi.md#favorite_screen_recording) | **POST** /storefront/{storefront_oid}/screen_recordings/{screen_recording_uuid}/favorite | Update favorite flag on screen recording
[**geocode_address**](StorefrontApi.md#geocode_address) | **POST** /storefront/{storefront_oid}/email/geocode | Obtain lat/long for an address
[**get_countries**](StorefrontApi.md#get_countries) | **GET** /storefront/{storefront_oid}/email/countries | Get countries
[**get_editor_token**](StorefrontApi.md#get_editor_token) | **GET** /storefront/{storefront_oid}/editor_token | Gets editor token
[**get_email_base_templates**](StorefrontApi.md#get_email_base_templates) | **GET** /storefront/{storefront_oid}/email/baseTemplates | Get email communication base templates
[**get_email_campaign**](StorefrontApi.md#get_email_campaign) | **GET** /storefront/{storefront_oid}/email/campaigns/{email_campaign_uuid} | Get email campaign
[**get_email_campaign_folder**](StorefrontApi.md#get_email_campaign_folder) | **GET** /storefront/{storefront_oid}/email/campaign_folders/{email_campaign_folder_uuid} | Get email campaign folder
[**get_email_campaign_folders**](StorefrontApi.md#get_email_campaign_folders) | **GET** /storefront/{storefront_oid}/email/campaign_folders | Get email campaign folders
[**get_email_campaign_screenshots**](StorefrontApi.md#get_email_campaign_screenshots) | **GET** /storefront/{storefront_oid}/email/campaigns/{email_campaign_uuid}/screenshots | Get email campaign screenshots
[**get_email_campaigns**](StorefrontApi.md#get_email_campaigns) | **GET** /storefront/{storefront_oid}/email/campaigns | Get email campaigns
[**get_email_campaigns_with_stats**](StorefrontApi.md#get_email_campaigns_with_stats) | **GET** /storefront/{storefront_oid}/email/campaignsWithStats/{stat_days} | Get email campaigns with stats
[**get_email_commseq**](StorefrontApi.md#get_email_commseq) | **GET** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid} | Get email commseq
[**get_email_commseq_email_stats**](StorefrontApi.md#get_email_commseq_email_stats) | **POST** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/emailStats | Get email communication sequence emails stats
[**get_email_commseq_postcard_stats**](StorefrontApi.md#get_email_commseq_postcard_stats) | **POST** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/postcardStats | Get email communication sequence postcard stats
[**get_email_commseq_stat_overall**](StorefrontApi.md#get_email_commseq_stat_overall) | **GET** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/stat | Get communication sequence stats overall
[**get_email_commseq_step_stats**](StorefrontApi.md#get_email_commseq_step_stats) | **POST** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/stepStats | Get email communication sequence step stats
[**get_email_commseq_step_waiting**](StorefrontApi.md#get_email_commseq_step_waiting) | **POST** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/waiting | Get email communication sequence customers waiting at each requested step
[**get_email_commseq_webhook_editor_values**](StorefrontApi.md#get_email_commseq_webhook_editor_values) | **GET** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/webhookEditorValues | Get email webhook editor values
[**get_email_commseqs**](StorefrontApi.md#get_email_commseqs) | **GET** /storefront/{storefront_oid}/email/commseqs | Get email commseqs
[**get_email_customer_editor_url**](StorefrontApi.md#get_email_customer_editor_url) | **GET** /storefront/{storefront_oid}/email/customers/{email_customer_uuid}/editor_url | Get customers editor URL
[**get_email_customers**](StorefrontApi.md#get_email_customers) | **GET** /storefront/{storefront_oid}/email/customers | Get email customers
[**get_email_dashboard_activity**](StorefrontApi.md#get_email_dashboard_activity) | **GET** /storefront/{storefront_oid}/email/dashboard_activity | Get email dashboard activity
[**get_email_dashboard_stats**](StorefrontApi.md#get_email_dashboard_stats) | **GET** /storefront/{storefront_oid}/email/dashboard_stats | Get dashboard stats
[**get_email_dispatch_logs**](StorefrontApi.md#get_email_dispatch_logs) | **GET** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/steps/{commseq_step_uuid}/logs | Get email dispatch logs
[**get_email_email**](StorefrontApi.md#get_email_email) | **GET** /storefront/{storefront_oid}/email/emails/{commseq_email_uuid} | Get email email
[**get_email_email_clicks**](StorefrontApi.md#get_email_email_clicks) | **GET** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/steps/{commseq_step_uuid}/emails/{commseq_email_uuid}/clicks | Get email email clicks
[**get_email_email_customer_editor_url**](StorefrontApi.md#get_email_email_customer_editor_url) | **GET** /storefront/{storefront_oid}/email/emails/{commseq_email_uuid}/orders/{order_id}/editor_url | Get email order customer editor url
[**get_email_email_orders**](StorefrontApi.md#get_email_email_orders) | **GET** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/steps/{commseq_step_uuid}/emails/{commseq_email_uuid}/orders | Get email email orders
[**get_email_emails**](StorefrontApi.md#get_email_emails) | **GET** /storefront/{storefront_oid}/email/emails | Get email emails
[**get_email_emails_multiple**](StorefrontApi.md#get_email_emails_multiple) | **POST** /storefront/{storefront_oid}/email/emails/multiple | Get email emails multiple
[**get_email_flow**](StorefrontApi.md#get_email_flow) | **GET** /storefront/{storefront_oid}/email/flows/{email_flow_uuid} | Get email flow
[**get_email_flow_folder**](StorefrontApi.md#get_email_flow_folder) | **GET** /storefront/{storefront_oid}/email/flow_folders/{email_flow_folder_uuid} | Get email flow folder
[**get_email_flow_folders**](StorefrontApi.md#get_email_flow_folders) | **GET** /storefront/{storefront_oid}/email/flow_folders | Get email flow folders
[**get_email_flow_screenshots**](StorefrontApi.md#get_email_flow_screenshots) | **GET** /storefront/{storefront_oid}/email/flows/{email_flow_uuid}/screenshots | Get email flow screenshots
[**get_email_flows**](StorefrontApi.md#get_email_flows) | **GET** /storefront/{storefront_oid}/email/flows | Get email flows
[**get_email_global_settings**](StorefrontApi.md#get_email_global_settings) | **GET** /storefront/email/global_settings | Get email globalsettings
[**get_email_list**](StorefrontApi.md#get_email_list) | **GET** /storefront/{storefront_oid}/email/lists/{email_list_uuid} | Get email list
[**get_email_list_customer_editor_url**](StorefrontApi.md#get_email_list_customer_editor_url) | **GET** /storefront/{storefront_oid}/email/lists/{email_list_uuid}/customers/{email_customer_uuid}/editor_url | Get email list customer editor url
[**get_email_list_customers**](StorefrontApi.md#get_email_list_customers) | **GET** /storefront/{storefront_oid}/email/lists/{email_list_uuid}/customers | Get email list customers
[**get_email_list_segment_folder**](StorefrontApi.md#get_email_list_segment_folder) | **GET** /storefront/{storefront_oid}/email/list_segment_folders/{email_list_segment_folder_uuid} | Get email campaign folder
[**get_email_list_segment_folders**](StorefrontApi.md#get_email_list_segment_folders) | **GET** /storefront/{storefront_oid}/email/list_segment_folders | Get email campaign folders
[**get_email_lists**](StorefrontApi.md#get_email_lists) | **GET** /storefront/{storefront_oid}/email/lists | Get email lists
[**get_email_performance**](StorefrontApi.md#get_email_performance) | **GET** /storefront/{storefront_oid}/email/performance | Get email performance
[**get_email_plan**](StorefrontApi.md#get_email_plan) | **GET** /storefront/{storefront_oid}/email/plan | Get email plan
[**get_email_postcard**](StorefrontApi.md#get_email_postcard) | **GET** /storefront/{storefront_oid}/email/postcards/{commseq_postcard_uuid} | Get email postcard
[**get_email_postcards**](StorefrontApi.md#get_email_postcards) | **GET** /storefront/{storefront_oid}/email/postcards | Get email postcards
[**get_email_postcards_multiple**](StorefrontApi.md#get_email_postcards_multiple) | **POST** /storefront/{storefront_oid}/email/postcards/multiple | Get email postcards multiple
[**get_email_segment**](StorefrontApi.md#get_email_segment) | **GET** /storefront/{storefront_oid}/email/segments/{email_segment_uuid} | Get email segment
[**get_email_segment_customer_editor_url**](StorefrontApi.md#get_email_segment_customer_editor_url) | **GET** /storefront/{storefront_oid}/email/segments/{email_segment_uuid}/customers/{email_customer_uuid}/editor_url | Get email segment customers editor URL
[**get_email_segment_customers**](StorefrontApi.md#get_email_segment_customers) | **GET** /storefront/{storefront_oid}/email/segments/{email_segment_uuid}/customers | Get email segment customers
[**get_email_segments**](StorefrontApi.md#get_email_segments) | **GET** /storefront/{storefront_oid}/email/segments | Get email segments
[**get_email_sending_domain**](StorefrontApi.md#get_email_sending_domain) | **GET** /storefront/email/sending_domain/{domain} | Get email sending domain
[**get_email_sending_domain_status**](StorefrontApi.md#get_email_sending_domain_status) | **POST** /storefront/email/sending_domains/{domain}/status | Get email sending domain status
[**get_email_sending_domains**](StorefrontApi.md#get_email_sending_domains) | **GET** /storefront/email/sending_domains | Get email sending domains
[**get_email_settings**](StorefrontApi.md#get_email_settings) | **GET** /storefront/{storefront_oid}/email/settings | Get email settings
[**get_email_template**](StorefrontApi.md#get_email_template) | **GET** /storefront/{storefront_oid}/email/templates/{email_template_oid} | Get email template
[**get_email_templates**](StorefrontApi.md#get_email_templates) | **GET** /storefront/{storefront_oid}/email/templates | Get email templates
[**get_email_third_party_providers**](StorefrontApi.md#get_email_third_party_providers) | **GET** /storefront/{storefront_oid}/email/third_party_providers | Get a list of third party email providers
[**get_experiments**](StorefrontApi.md#get_experiments) | **GET** /storefront/{storefront_oid}/experiments | Get experiments
[**get_heatmap**](StorefrontApi.md#get_heatmap) | **POST** /storefront/{storefront_oid}/screen_recordings/heatmap | Get screen recording heatmap
[**get_heatmap_index**](StorefrontApi.md#get_heatmap_index) | **POST** /storefront/{storefront_oid}/screen_recordings/heatmap/index | Get screen recording heatmap index
[**get_histogram_property_names**](StorefrontApi.md#get_histogram_property_names) | **GET** /storefront/{storefront_oid}/email/histogram/property_names | Get histogram property names
[**get_histogram_property_values**](StorefrontApi.md#get_histogram_property_values) | **GET** /storefront/{storefront_oid}/email/histogram/property_values | Get histogram property values
[**get_library_filter_values**](StorefrontApi.md#get_library_filter_values) | **GET** /storefront/code_library/filter_values | Get library values used to populate drop down boxes for filtering.
[**get_library_item**](StorefrontApi.md#get_library_item) | **GET** /storefront/code_library/{library_item_oid} | Get library item.
[**get_library_item_published_versions**](StorefrontApi.md#get_library_item_published_versions) | **GET** /storefront/code_library/{library_item_oid}/published_versions | Get all published versions for a library item.
[**get_screen_recording**](StorefrontApi.md#get_screen_recording) | **GET** /storefront/{storefront_oid}/screen_recordings/{screen_recording_uuid} | Get screen recording
[**get_screen_recording_page_view_data**](StorefrontApi.md#get_screen_recording_page_view_data) | **GET** /storefront/{storefront_oid}/screen_recordings/{screen_recording_uuid}/page_view_data/{screen_recording_page_view_uuid} | Get screen recording page view data
[**get_screen_recording_segment**](StorefrontApi.md#get_screen_recording_segment) | **GET** /storefront/{storefront_oid}/screen_recordings/segments/{screen_recording_segment_oid} | Get screen recording segment
[**get_screen_recording_segments**](StorefrontApi.md#get_screen_recording_segments) | **GET** /storefront/{storefront_oid}/screen_recordings/segments | Get screen recording segments
[**get_screen_recording_settings**](StorefrontApi.md#get_screen_recording_settings) | **GET** /storefront/{storefront_oid}/screen_recordings/settings | Get screen recording settings
[**get_screen_recording_tags**](StorefrontApi.md#get_screen_recording_tags) | **POST** /storefront/{storefront_oid}/screen_recordings/tags | Get tags used by screen recording
[**get_screen_recordings_by_query**](StorefrontApi.md#get_screen_recordings_by_query) | **POST** /storefront/{storefront_oid}/screen_recordings/query | Query screen recordings
[**get_screen_recordings_by_segment**](StorefrontApi.md#get_screen_recordings_by_segment) | **POST** /storefront/{storefront_oid}/screen_recordings/segments/{screen_recording_segment_oid}/query | Get screen recordings by segment
[**get_store_front_pricing_tiers**](StorefrontApi.md#get_store_front_pricing_tiers) | **GET** /storefront/pricing_tiers | Retrieve pricing tiers
[**get_thumbnail_parameters**](StorefrontApi.md#get_thumbnail_parameters) | **POST** /storefront/thumbnailParameters | Get thumbnail parameters
[**get_transaction_email**](StorefrontApi.md#get_transaction_email) | **GET** /storefront/{storefront_oid}/transaction_email/list/{email_id} | Gets a transaction email object
[**get_transaction_email_list**](StorefrontApi.md#get_transaction_email_list) | **GET** /storefront/{storefront_oid}/transaction_email/list | Gets a list of transaction email names
[**get_transaction_email_screenshots**](StorefrontApi.md#get_transaction_email_screenshots) | **GET** /storefront/{storefront_oid}/transaction_email/list/{email_id}/screenshots | Get transactional email screenshots
[**get_twilio_account**](StorefrontApi.md#get_twilio_account) | **GET** /storefront/twilio/accounts/{esp_twilio_uuid} | Get Twilio account
[**get_twilio_accounts**](StorefrontApi.md#get_twilio_accounts) | **GET** /storefront/twilio/accounts | Get all Twilio accounts
[**global_unsubscribe**](StorefrontApi.md#global_unsubscribe) | **POST** /storefront/{storefront_oid}/email/globalUnsubscribe | Globally unsubscribe a customer
[**import_email_third_party_provider_list**](StorefrontApi.md#import_email_third_party_provider_list) | **POST** /storefront/{storefront_oid}/email/third_party_providers/import | Import a third party provider list
[**insert_email_campaign**](StorefrontApi.md#insert_email_campaign) | **POST** /storefront/{storefront_oid}/email/campaigns | Insert email campaign
[**insert_email_campaign_folder**](StorefrontApi.md#insert_email_campaign_folder) | **POST** /storefront/{storefront_oid}/email/campaign_folders | Insert email campaign folder
[**insert_email_commseq**](StorefrontApi.md#insert_email_commseq) | **POST** /storefront/{storefront_oid}/email/commseqs | Insert email commseq
[**insert_email_email**](StorefrontApi.md#insert_email_email) | **POST** /storefront/{storefront_oid}/email/emails | Insert email email
[**insert_email_flow**](StorefrontApi.md#insert_email_flow) | **POST** /storefront/{storefront_oid}/email/flows | Insert email flow
[**insert_email_flow_folder**](StorefrontApi.md#insert_email_flow_folder) | **POST** /storefront/{storefront_oid}/email/flow_folders | Insert email flow folder
[**insert_email_list**](StorefrontApi.md#insert_email_list) | **POST** /storefront/{storefront_oid}/email/lists | Insert email list
[**insert_email_list_segment_folder**](StorefrontApi.md#insert_email_list_segment_folder) | **POST** /storefront/{storefront_oid}/email/list_segment_folders | Insert email campaign folder
[**insert_email_postcard**](StorefrontApi.md#insert_email_postcard) | **POST** /storefront/{storefront_oid}/email/postcards | Insert email postcard
[**insert_email_segment**](StorefrontApi.md#insert_email_segment) | **POST** /storefront/{storefront_oid}/email/segments | Insert email segment
[**insert_screen_recording_segment**](StorefrontApi.md#insert_screen_recording_segment) | **POST** /storefront/{storefront_oid}/screen_recordings/segments | Insert screen recording segment
[**prepare_download_email_segment**](StorefrontApi.md#prepare_download_email_segment) | **POST** /storefront/{storefront_oid}/email/segments/{email_segment_uuid}/downloadPrepare | Prepare download of email segment
[**publish_library_item**](StorefrontApi.md#publish_library_item) | **POST** /storefront/code_library/{library_item_oid}/publish | Publish library item.
[**purchase_library_item**](StorefrontApi.md#purchase_library_item) | **POST** /storefront/code_library/{library_item_oid}/purchase | Purchase public library item, which creates a copy of the item in your personal code library
[**release_email_commseq_step_waiting**](StorefrontApi.md#release_email_commseq_step_waiting) | **POST** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/waiting/{commseq_step_uuid} | Release email communication sequence customers waiting at the specified step
[**review**](StorefrontApi.md#review) | **POST** /storefront/{storefront_oid}/email/emails/{commseq_email_uuid}/review | Request a review of an email
[**search**](StorefrontApi.md#search) | **GET** /storefront/search | Searches for all matching values
[**search2**](StorefrontApi.md#search2) | **POST** /storefront/search | Searches for all matching values (using POST)
[**search_email_list_customers**](StorefrontApi.md#search_email_list_customers) | **GET** /storefront/{storefront_oid}/email/lists/{email_list_uuid}/search | Search email list customers
[**search_email_segment_customers**](StorefrontApi.md#search_email_segment_customers) | **GET** /storefront/{storefront_oid}/email/segments/{email_segment_uuid}/search | Search email segment customers
[**search_library_items**](StorefrontApi.md#search_library_items) | **POST** /storefront/code_library/search | Retrieve library items
[**search_published_items**](StorefrontApi.md#search_published_items) | **POST** /storefront/code_library/search_published | Retrieve library items
[**search_review_items**](StorefrontApi.md#search_review_items) | **POST** /storefront/code_library/search_review | Retrieve library items needing review or rejected
[**search_shared_items**](StorefrontApi.md#search_shared_items) | **POST** /storefront/code_library/search_shared | Retrieve library items
[**send_email_test**](StorefrontApi.md#send_email_test) | **POST** /storefront/{storefront_oid}/email/emails/{commseq_email_uuid}/test | Send email test
[**send_postcard_test**](StorefrontApi.md#send_postcard_test) | **POST** /storefront/{storefront_oid}/email/postcards/{commseq_postcard_uuid}/test | Send postcard test
[**send_webhook_test**](StorefrontApi.md#send_webhook_test) | **POST** /storefront/{storefront_oid}/email/webhooks/test | Send webhook test
[**start_email_campaign**](StorefrontApi.md#start_email_campaign) | **PUT** /storefront/{storefront_oid}/email/campaigns/{email_campaign_uuid}/start | Start email campaign
[**subscribe_to_email_list**](StorefrontApi.md#subscribe_to_email_list) | **POST** /storefront/{storefront_oid}/email/lists/{email_list_uuid}/subscribe | Subscribe customers to email list
[**unfavorite_screen_recording**](StorefrontApi.md#unfavorite_screen_recording) | **DELETE** /storefront/{storefront_oid}/screen_recordings/{screen_recording_uuid}/favorite | Remove favorite flag on screen recording
[**update_email_campaign**](StorefrontApi.md#update_email_campaign) | **PUT** /storefront/{storefront_oid}/email/campaigns/{email_campaign_uuid} | Update email campaign
[**update_email_campaign_folder**](StorefrontApi.md#update_email_campaign_folder) | **PUT** /storefront/{storefront_oid}/email/campaign_folders/{email_campaign_folder_uuid} | Update email campaign folder
[**update_email_commseq**](StorefrontApi.md#update_email_commseq) | **PUT** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid} | Update email commseq
[**update_email_customer**](StorefrontApi.md#update_email_customer) | **PUT** /storefront/{storefront_oid}/email/customers/{email_customer_uuid} | Update email customer
[**update_email_email**](StorefrontApi.md#update_email_email) | **PUT** /storefront/{storefront_oid}/email/emails/{commseq_email_uuid} | Update email email
[**update_email_flow**](StorefrontApi.md#update_email_flow) | **PUT** /storefront/{storefront_oid}/email/flows/{email_flow_uuid} | Update email flow
[**update_email_flow_folder**](StorefrontApi.md#update_email_flow_folder) | **PUT** /storefront/{storefront_oid}/email/flow_folders/{email_flow_folder_uuid} | Update email flow folder
[**update_email_global_settings**](StorefrontApi.md#update_email_global_settings) | **POST** /storefront/email/global_settings | Update email global settings
[**update_email_list**](StorefrontApi.md#update_email_list) | **PUT** /storefront/{storefront_oid}/email/lists/{email_list_uuid} | Update email list
[**update_email_list_segment_folder**](StorefrontApi.md#update_email_list_segment_folder) | **PUT** /storefront/{storefront_oid}/email/list_segment_folders/{email_list_segment_folder_uuid} | Update email campaign folder
[**update_email_plan**](StorefrontApi.md#update_email_plan) | **POST** /storefront/{storefront_oid}/email/plan | Update email plan
[**update_email_postcard**](StorefrontApi.md#update_email_postcard) | **PUT** /storefront/{storefront_oid}/email/postcards/{commseq_postcard_uuid} | Update email postcard
[**update_email_segment**](StorefrontApi.md#update_email_segment) | **PUT** /storefront/{storefront_oid}/email/segments/{email_segment_uuid} | Update email segment
[**update_email_settings**](StorefrontApi.md#update_email_settings) | **POST** /storefront/{storefront_oid}/email/settings | Update email settings
[**update_experiment**](StorefrontApi.md#update_experiment) | **PUT** /storefront/{storefront_oid}/experiments/{storefront_experiment_oid} | Update experiment
[**update_library_item**](StorefrontApi.md#update_library_item) | **PUT** /storefront/code_library/{library_item_oid} | Update library item. Note that only certain fields may be updated via this method.
[**update_screen_recording_merchant_notes**](StorefrontApi.md#update_screen_recording_merchant_notes) | **POST** /storefront/{storefront_oid}/screen_recordings/{screen_recording_uuid}/merchant_notes | Update merchant notes on a screen recording
[**update_screen_recording_segment**](StorefrontApi.md#update_screen_recording_segment) | **POST** /storefront/{storefront_oid}/screen_recordings/segments/{screen_recording_segment_oid} | Update screen recording segment
[**update_screen_recording_settings**](StorefrontApi.md#update_screen_recording_settings) | **POST** /storefront/{storefront_oid}/screen_recordings/settings | Update screen recording settings
[**update_screen_recording_tags**](StorefrontApi.md#update_screen_recording_tags) | **POST** /storefront/{storefront_oid}/screen_recordings/{screen_recording_uuid}/tags | Update tags on a screen recording
[**update_transaction_email**](StorefrontApi.md#update_transaction_email) | **PUT** /storefront/{storefront_oid}/transaction_email/list/{email_id} | Updates a transaction email object
[**update_twilio_account**](StorefrontApi.md#update_twilio_account) | **PUT** /storefront/twilio/accounts/{esp_twilio_uuid} | Update Twilio account


# **add_to_library**
> LibraryItemResponse add_to_library(add_library_request)

Add to library

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

add_library_request = ultracart.AddLibraryItemRequest() # AddLibraryItemRequest | New library item request

try:
    # Add to library
    api_response = api_instance.add_to_library(add_library_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->add_to_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_library_request** | [**AddLibraryItemRequest**](AddLibraryItemRequest.md)| New library item request | 

### Return type

[**LibraryItemResponse**](LibraryItemResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_to_store_front**
> ApplyLibraryItemResponse apply_to_store_front(apply_library_request)

Apply library item to storefront.

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

apply_library_request = ultracart.ApplyLibraryItemRequest() # ApplyLibraryItemRequest | New library item

try:
    # Apply library item to storefront.
    api_response = api_instance.apply_to_store_front(apply_library_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->apply_to_store_front: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apply_library_request** | [**ApplyLibraryItemRequest**](ApplyLibraryItemRequest.md)| New library item | 

### Return type

[**ApplyLibraryItemResponse**](ApplyLibraryItemResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_email_list**
> EmailListArchiveResponse archive_email_list(storefront_oid, email_list_uuid)

Archive email list

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list_uuid = 'email_list_uuid_example' # str | 

try:
    # Archive email list
    api_response = api_instance.archive_email_list(storefront_oid, email_list_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->archive_email_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list_uuid** | **str**|  | 

### Return type

[**EmailListArchiveResponse**](EmailListArchiveResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_email_segment**
> EmailSegmentArchiveResponse archive_email_segment(storefront_oid, email_segment_uuid)

Archive email segment

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_segment_uuid = 'email_segment_uuid_example' # str | 

try:
    # Archive email segment
    api_response = api_instance.archive_email_segment(storefront_oid, email_segment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->archive_email_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_segment_uuid** | **str**|  | 

### Return type

[**EmailSegmentArchiveResponse**](EmailSegmentArchiveResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **back_populate_email_flow**
> EmailFlowBackPopulateResponse back_populate_email_flow(storefront_oid, email_flow_uuid, back_populate_request)

Back populate email flow

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_flow_uuid = 'email_flow_uuid_example' # str | 
back_populate_request = ultracart.EmailFlowBackPopulateRequest() # EmailFlowBackPopulateRequest | The request to back populate

try:
    # Back populate email flow
    api_response = api_instance.back_populate_email_flow(storefront_oid, email_flow_uuid, back_populate_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->back_populate_email_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_flow_uuid** | **str**|  | 
 **back_populate_request** | [**EmailFlowBackPopulateRequest**](EmailFlowBackPopulateRequest.md)| The request to back populate | 

### Return type

[**EmailFlowBackPopulateResponse**](EmailFlowBackPopulateResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_download_email_segment**
> EmailSegmentDownloadPrepareResponse check_download_email_segment(storefront_oid, email_segment_uuid, email_segment_rebuild_uuid)

Check download of email segment

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_segment_uuid = 'email_segment_uuid_example' # str | 
email_segment_rebuild_uuid = 'email_segment_rebuild_uuid_example' # str | 

try:
    # Check download of email segment
    api_response = api_instance.check_download_email_segment(storefront_oid, email_segment_uuid, email_segment_rebuild_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->check_download_email_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_segment_uuid** | **str**|  | 
 **email_segment_rebuild_uuid** | **str**|  | 

### Return type

[**EmailSegmentDownloadPrepareResponse**](EmailSegmentDownloadPrepareResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_email_campaign**
> EmailCampaignResponse clone_email_campaign(storefront_oid, email_campaign_uuid, target_storefront_oid=target_storefront_oid)

Clone email campaign

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_campaign_uuid = 'email_campaign_uuid_example' # str | 
target_storefront_oid = 56 # int |  (optional)

try:
    # Clone email campaign
    api_response = api_instance.clone_email_campaign(storefront_oid, email_campaign_uuid, target_storefront_oid=target_storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->clone_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_campaign_uuid** | **str**|  | 
 **target_storefront_oid** | **int**|  | [optional] 

### Return type

[**EmailCampaignResponse**](EmailCampaignResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_email_flow**
> EmailFlowResponse clone_email_flow(storefront_oid, email_flow_uuid, target_storefront_oid=target_storefront_oid)

Clone email flow

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_flow_uuid = 'email_flow_uuid_example' # str | 
target_storefront_oid = 56 # int |  (optional)

try:
    # Clone email flow
    api_response = api_instance.clone_email_flow(storefront_oid, email_flow_uuid, target_storefront_oid=target_storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->clone_email_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_flow_uuid** | **str**|  | 
 **target_storefront_oid** | **int**|  | [optional] 

### Return type

[**EmailFlowResponse**](EmailFlowResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_email_sending_domain**
> EmailSendingDomainResponse create_email_sending_domain(domain)

Create email campaign

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

domain = 'domain_example' # str | 

try:
    # Create email campaign
    api_response = api_instance.create_email_sending_domain(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->create_email_sending_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 

### Return type

[**EmailSendingDomainResponse**](EmailSendingDomainResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_twilio_account**
> TwilioResponse create_twilio_account(twilio)

Create Twilio account

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

twilio = ultracart.Twilio() # Twilio | Twilio

try:
    # Create Twilio account
    api_response = api_instance.create_twilio_account(twilio)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->create_twilio_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **twilio** | [**Twilio**](Twilio.md)| Twilio | 

### Return type

[**TwilioResponse**](TwilioResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_campaign_folder**
> BaseResponse delete_email_campaign_folder(storefront_oid, email_campaign_folder_uuid)

Delete email campaignFolder

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_campaign_folder_uuid = 'email_campaign_folder_uuid_example' # str | 

try:
    # Delete email campaignFolder
    api_response = api_instance.delete_email_campaign_folder(storefront_oid, email_campaign_folder_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_email_campaign_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_campaign_folder_uuid** | **str**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_commseq_stat**
> delete_email_commseq_stat(storefront_oid, commseq_uuid)

Delete communication sequence stats

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 

try:
    # Delete communication sequence stats
    api_instance.delete_email_commseq_stat(storefront_oid, commseq_uuid)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_email_commseq_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_email**
> BaseResponse delete_email_email(storefront_oid, commseq_email_uuid)

Delete email email

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_email_uuid = 'commseq_email_uuid_example' # str | 

try:
    # Delete email email
    api_response = api_instance.delete_email_email(storefront_oid, commseq_email_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_email_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_email_uuid** | **str**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_flow_folder**
> BaseResponse delete_email_flow_folder(storefront_oid, email_flow_folder_uuid)

Delete email flowFolder

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_flow_folder_uuid = 'email_flow_folder_uuid_example' # str | 

try:
    # Delete email flowFolder
    api_response = api_instance.delete_email_flow_folder(storefront_oid, email_flow_folder_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_email_flow_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_flow_folder_uuid** | **str**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_list_customer**
> BaseResponse delete_email_list_customer(storefront_oid, email_list_uuid, email_customer_uuid)

Delete email list customer

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list_uuid = 'email_list_uuid_example' # str | 
email_customer_uuid = 'email_customer_uuid_example' # str | 

try:
    # Delete email list customer
    api_response = api_instance.delete_email_list_customer(storefront_oid, email_list_uuid, email_customer_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_email_list_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list_uuid** | **str**|  | 
 **email_customer_uuid** | **str**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_list_segment_folder**
> BaseResponse delete_email_list_segment_folder(storefront_oid, email_list_segment_folder_uuid)

Delete email ListSegmentFolder

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list_segment_folder_uuid = 'email_list_segment_folder_uuid_example' # str | 

try:
    # Delete email ListSegmentFolder
    api_response = api_instance.delete_email_list_segment_folder(storefront_oid, email_list_segment_folder_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_email_list_segment_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list_segment_folder_uuid** | **str**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_postcard**
> BaseResponse delete_email_postcard(storefront_oid, commseq_postcard_uuid)

Delete email postcard

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_postcard_uuid = 'commseq_postcard_uuid_example' # str | 

try:
    # Delete email postcard
    api_response = api_instance.delete_email_postcard(storefront_oid, commseq_postcard_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_email_postcard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_postcard_uuid** | **str**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_sending_domain**
> BaseResponse delete_email_sending_domain(domain)

delete email campaign

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

domain = 'domain_example' # str | 

try:
    # delete email campaign
    api_response = api_instance.delete_email_sending_domain(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_email_sending_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_experiment**
> delete_experiment(storefront_oid, storefront_experiment_oid)

Delete experiment

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
storefront_experiment_oid = 56 # int | 

try:
    # Delete experiment
    api_instance.delete_experiment(storefront_oid, storefront_experiment_oid)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **storefront_experiment_oid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_heatmap**
> delete_heatmap(storefront_oid, query)

Delete screen recording heatmap

Delete screen recording heatmap 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
query = ultracart.ScreenRecordingHeatmapReset() # ScreenRecordingHeatmapReset | Query

try:
    # Delete screen recording heatmap
    api_instance.delete_heatmap(storefront_oid, query)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_heatmap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **query** | [**ScreenRecordingHeatmapReset**](ScreenRecordingHeatmapReset.md)| Query | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_item**
> delete_library_item(library_item_oid)

Delete library item

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

library_item_oid = 56 # int | 

try:
    # Delete library item
    api_instance.delete_library_item(library_item_oid)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_library_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_oid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_item_published_versions**
> delete_library_item_published_versions(library_item_oid)

Delete all published versions for a library item, including anything in review.

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

library_item_oid = 56 # int | 

try:
    # Delete all published versions for a library item, including anything in review.
    api_instance.delete_library_item_published_versions(library_item_oid)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_library_item_published_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_oid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_screen_recording_segment**
> delete_screen_recording_segment(storefront_oid, screen_recording_segment_oid)

Delete screen recording segment

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
screen_recording_segment_oid = 56 # int | 

try:
    # Delete screen recording segment
    api_instance.delete_screen_recording_segment(storefront_oid, screen_recording_segment_oid)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_screen_recording_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **screen_recording_segment_oid** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_twilio_account**
> BaseResponse delete_twilio_account(esp_twilio_uuid)

delete Twilio account

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

esp_twilio_uuid = 'esp_twilio_uuid_example' # str | 

try:
    # delete Twilio account
    api_response = api_instance.delete_twilio_account(esp_twilio_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_twilio_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **esp_twilio_uuid** | **str**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_library_item**
> LibraryItemResponse duplicate_library_item(library_item_oid)

Duplicate library item.

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

library_item_oid = 56 # int | 

try:
    # Duplicate library item.
    api_response = api_instance.duplicate_library_item(library_item_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->duplicate_library_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_oid** | **int**|  | 

### Return type

[**LibraryItemResponse**](LibraryItemResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorite_screen_recording**
> favorite_screen_recording(storefront_oid, screen_recording_uuid)

Update favorite flag on screen recording

Update favorite flag on screen recording 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
screen_recording_uuid = 'screen_recording_uuid_example' # str | 

try:
    # Update favorite flag on screen recording
    api_instance.favorite_screen_recording(storefront_oid, screen_recording_uuid)
except ApiException as e:
    print("Exception when calling StorefrontApi->favorite_screen_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **screen_recording_uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geocode_address**
> GeocodeResponse geocode_address(storefront_oid, geocode_request)

Obtain lat/long for an address

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
geocode_request = ultracart.GeocodeRequest() # GeocodeRequest | geocode request

try:
    # Obtain lat/long for an address
    api_response = api_instance.geocode_address(storefront_oid, geocode_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->geocode_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **geocode_request** | [**GeocodeRequest**](GeocodeRequest.md)| geocode request | 

### Return type

[**GeocodeResponse**](GeocodeResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries**
> CountriesResponse get_countries(storefront_oid)

Get countries

Obtain a list of all the countries 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get countries
    api_response = api_instance.get_countries(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_countries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editor_token**
> EmailEditorTokenResponse get_editor_token(storefront_oid)

Gets editor token

Fetches a temporary authentication token for the editor 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Gets editor token
    api_response = api_instance.get_editor_token(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_editor_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailEditorTokenResponse**](EmailEditorTokenResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_base_templates**
> EmailBaseTemplateListResponse get_email_base_templates(storefront_oid)

Get email communication base templates

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email communication base templates
    api_response = api_instance.get_email_base_templates(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_base_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailBaseTemplateListResponse**](EmailBaseTemplateListResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaign**
> EmailCampaignResponse get_email_campaign(storefront_oid, email_campaign_uuid)

Get email campaign

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_campaign_uuid = 'email_campaign_uuid_example' # str | 

try:
    # Get email campaign
    api_response = api_instance.get_email_campaign(storefront_oid, email_campaign_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_campaign_uuid** | **str**|  | 

### Return type

[**EmailCampaignResponse**](EmailCampaignResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaign_folder**
> EmailCampaignFolderResponse get_email_campaign_folder(storefront_oid, email_campaign_folder_uuid)

Get email campaign folder

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_campaign_folder_uuid = 'email_campaign_folder_uuid_example' # str | 

try:
    # Get email campaign folder
    api_response = api_instance.get_email_campaign_folder(storefront_oid, email_campaign_folder_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_campaign_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_campaign_folder_uuid** | **str**|  | 

### Return type

[**EmailCampaignFolderResponse**](EmailCampaignFolderResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaign_folders**
> EmailCampaignFoldersResponse get_email_campaign_folders(storefront_oid)

Get email campaign folders

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email campaign folders
    api_response = api_instance.get_email_campaign_folders(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_campaign_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailCampaignFoldersResponse**](EmailCampaignFoldersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaign_screenshots**
> ScreenshotsResponse get_email_campaign_screenshots(storefront_oid, email_campaign_uuid)

Get email campaign screenshots

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_campaign_uuid = 'email_campaign_uuid_example' # str | 

try:
    # Get email campaign screenshots
    api_response = api_instance.get_email_campaign_screenshots(storefront_oid, email_campaign_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_campaign_screenshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_campaign_uuid** | **str**|  | 

### Return type

[**ScreenshotsResponse**](ScreenshotsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaigns**
> EmailCampaignsResponse get_email_campaigns(storefront_oid)

Get email campaigns

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email campaigns
    api_response = api_instance.get_email_campaigns(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailCampaignsResponse**](EmailCampaignsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaigns_with_stats**
> EmailCampaignsResponse get_email_campaigns_with_stats(storefront_oid, stat_days)

Get email campaigns with stats

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
stat_days = 'stat_days_example' # str | 

try:
    # Get email campaigns with stats
    api_response = api_instance.get_email_campaigns_with_stats(storefront_oid, stat_days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_campaigns_with_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **stat_days** | **str**|  | 

### Return type

[**EmailCampaignsResponse**](EmailCampaignsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq**
> EmailCommseqResponse get_email_commseq(storefront_oid, commseq_uuid)

Get email commseq

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 

try:
    # Get email commseq
    api_response = api_instance.get_email_commseq(storefront_oid, commseq_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseq: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 

### Return type

[**EmailCommseqResponse**](EmailCommseqResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_email_stats**
> EmailStatSummaryResponse get_email_commseq_email_stats(storefront_oid, commseq_uuid, stats_request)

Get email communication sequence emails stats

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 
stats_request = ultracart.EmailStatSummaryRequest() # EmailStatSummaryRequest | StatsRequest

try:
    # Get email communication sequence emails stats
    api_response = api_instance.get_email_commseq_email_stats(storefront_oid, commseq_uuid, stats_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseq_email_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 
 **stats_request** | [**EmailStatSummaryRequest**](EmailStatSummaryRequest.md)| StatsRequest | 

### Return type

[**EmailStatSummaryResponse**](EmailStatSummaryResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_postcard_stats**
> EmailStatPostcardSummaryResponse get_email_commseq_postcard_stats(storefront_oid, commseq_uuid, stats_request)

Get email communication sequence postcard stats

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 
stats_request = ultracart.EmailStatPostcardSummaryRequest() # EmailStatPostcardSummaryRequest | StatsRequest

try:
    # Get email communication sequence postcard stats
    api_response = api_instance.get_email_commseq_postcard_stats(storefront_oid, commseq_uuid, stats_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseq_postcard_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 
 **stats_request** | [**EmailStatPostcardSummaryRequest**](EmailStatPostcardSummaryRequest.md)| StatsRequest | 

### Return type

[**EmailStatPostcardSummaryResponse**](EmailStatPostcardSummaryResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_stat_overall**
> EmailCommseqStatResponse get_email_commseq_stat_overall(storefront_oid, commseq_uuid)

Get communication sequence stats overall

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 

try:
    # Get communication sequence stats overall
    api_response = api_instance.get_email_commseq_stat_overall(storefront_oid, commseq_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseq_stat_overall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 

### Return type

[**EmailCommseqStatResponse**](EmailCommseqStatResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_step_stats**
> EmailStepStatResponse get_email_commseq_step_stats(storefront_oid, commseq_uuid, stats_request)

Get email communication sequence step stats

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 
stats_request = ultracart.EmailStepStatRequest() # EmailStepStatRequest | StatsRequest

try:
    # Get email communication sequence step stats
    api_response = api_instance.get_email_commseq_step_stats(storefront_oid, commseq_uuid, stats_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseq_step_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 
 **stats_request** | [**EmailStepStatRequest**](EmailStepStatRequest.md)| StatsRequest | 

### Return type

[**EmailStepStatResponse**](EmailStepStatResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_step_waiting**
> EmailStepWaitingResponse get_email_commseq_step_waiting(storefront_oid, commseq_uuid, waiting_request)

Get email communication sequence customers waiting at each requested step

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 
waiting_request = ultracart.EmailStepWaitingRequest() # EmailStepWaitingRequest | WaitingRequest

try:
    # Get email communication sequence customers waiting at each requested step
    api_response = api_instance.get_email_commseq_step_waiting(storefront_oid, commseq_uuid, waiting_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseq_step_waiting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 
 **waiting_request** | [**EmailStepWaitingRequest**](EmailStepWaitingRequest.md)| WaitingRequest | 

### Return type

[**EmailStepWaitingResponse**](EmailStepWaitingResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_webhook_editor_values**
> EmailWebhookEditorValuesResponse get_email_commseq_webhook_editor_values(storefront_oid, commseq_uuid)

Get email webhook editor values

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 

try:
    # Get email webhook editor values
    api_response = api_instance.get_email_commseq_webhook_editor_values(storefront_oid, commseq_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseq_webhook_editor_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 

### Return type

[**EmailWebhookEditorValuesResponse**](EmailWebhookEditorValuesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseqs**
> EmailCommseqsResponse get_email_commseqs(storefront_oid)

Get email commseqs

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email commseqs
    api_response = api_instance.get_email_commseqs(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseqs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailCommseqsResponse**](EmailCommseqsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_customer_editor_url**
> EmailCustomerEditorUrlResponse get_email_customer_editor_url(storefront_oid, email_customer_uuid)

Get customers editor URL

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_customer_uuid = 'email_customer_uuid_example' # str | 

try:
    # Get customers editor URL
    api_response = api_instance.get_email_customer_editor_url(storefront_oid, email_customer_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_customer_editor_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_customer_uuid** | **str**|  | 

### Return type

[**EmailCustomerEditorUrlResponse**](EmailCustomerEditorUrlResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_customers**
> EmailCustomersResponse get_email_customers(storefront_oid, page_number=page_number, page_size=page_size, search_email_prefix=search_email_prefix)

Get email customers

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
search_email_prefix = 'search_email_prefix_example' # str |  (optional)

try:
    # Get email customers
    api_response = api_instance.get_email_customers(storefront_oid, page_number=page_number, page_size=page_size, search_email_prefix=search_email_prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **search_email_prefix** | **str**|  | [optional] 

### Return type

[**EmailCustomersResponse**](EmailCustomersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_dashboard_activity**
> EmailDashboardActivityResponse get_email_dashboard_activity(storefront_oid, last_records=last_records)

Get email dashboard activity

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
last_records = 56 # int |  (optional)

try:
    # Get email dashboard activity
    api_response = api_instance.get_email_dashboard_activity(storefront_oid, last_records=last_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_dashboard_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **last_records** | **int**|  | [optional] 

### Return type

[**EmailDashboardActivityResponse**](EmailDashboardActivityResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_dashboard_stats**
> EmailDashboardStatsResponse get_email_dashboard_stats(storefront_oid, days=days)

Get dashboard stats

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
days = 56 # int |  (optional)

try:
    # Get dashboard stats
    api_response = api_instance.get_email_dashboard_stats(storefront_oid, days=days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_dashboard_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **days** | **int**|  | [optional] 

### Return type

[**EmailDashboardStatsResponse**](EmailDashboardStatsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_dispatch_logs**
> EmailCommseqStepLogsResponse get_email_dispatch_logs(storefront_oid, commseq_uuid, commseq_step_uuid)

Get email dispatch logs

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 
commseq_step_uuid = 'commseq_step_uuid_example' # str | 

try:
    # Get email dispatch logs
    api_response = api_instance.get_email_dispatch_logs(storefront_oid, commseq_uuid, commseq_step_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_dispatch_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 
 **commseq_step_uuid** | **str**|  | 

### Return type

[**EmailCommseqStepLogsResponse**](EmailCommseqStepLogsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_email**
> EmailCommseqEmailResponse get_email_email(storefront_oid, commseq_email_uuid)

Get email email

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_email_uuid = 'commseq_email_uuid_example' # str | 

try:
    # Get email email
    api_response = api_instance.get_email_email(storefront_oid, commseq_email_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_email_uuid** | **str**|  | 

### Return type

[**EmailCommseqEmailResponse**](EmailCommseqEmailResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_email_clicks**
> EmailClicksResponse get_email_email_clicks(storefront_oid, commseq_uuid, commseq_step_uuid, commseq_email_uuid, days=days)

Get email email clicks

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 
commseq_step_uuid = 'commseq_step_uuid_example' # str | 
commseq_email_uuid = 'commseq_email_uuid_example' # str | 
days = 56 # int |  (optional)

try:
    # Get email email clicks
    api_response = api_instance.get_email_email_clicks(storefront_oid, commseq_uuid, commseq_step_uuid, commseq_email_uuid, days=days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_email_clicks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 
 **commseq_step_uuid** | **str**|  | 
 **commseq_email_uuid** | **str**|  | 
 **days** | **int**|  | [optional] 

### Return type

[**EmailClicksResponse**](EmailClicksResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_email_customer_editor_url**
> EmailCustomerEditorUrlResponse get_email_email_customer_editor_url(storefront_oid, commseq_email_uuid, order_id)

Get email order customer editor url

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_email_uuid = 'commseq_email_uuid_example' # str | 
order_id = 'order_id_example' # str | 

try:
    # Get email order customer editor url
    api_response = api_instance.get_email_email_customer_editor_url(storefront_oid, commseq_email_uuid, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_email_customer_editor_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_email_uuid** | **str**|  | 
 **order_id** | **str**|  | 

### Return type

[**EmailCustomerEditorUrlResponse**](EmailCustomerEditorUrlResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_email_orders**
> EmailOrdersResponse get_email_email_orders(storefront_oid, commseq_uuid, commseq_step_uuid, commseq_email_uuid, days=days)

Get email email orders

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 
commseq_step_uuid = 'commseq_step_uuid_example' # str | 
commseq_email_uuid = 'commseq_email_uuid_example' # str | 
days = 56 # int |  (optional)

try:
    # Get email email orders
    api_response = api_instance.get_email_email_orders(storefront_oid, commseq_uuid, commseq_step_uuid, commseq_email_uuid, days=days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_email_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 
 **commseq_step_uuid** | **str**|  | 
 **commseq_email_uuid** | **str**|  | 
 **days** | **int**|  | [optional] 

### Return type

[**EmailOrdersResponse**](EmailOrdersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_emails**
> EmailCommseqEmailsResponse get_email_emails(storefront_oid)

Get email emails

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email emails
    api_response = api_instance.get_email_emails(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailCommseqEmailsResponse**](EmailCommseqEmailsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_emails_multiple**
> EmailCommseqEmailsResponse get_email_emails_multiple(storefront_oid, email_commseq_emails_request)

Get email emails multiple

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_commseq_emails_request = ultracart.EmailCommseqEmailsRequest() # EmailCommseqEmailsRequest | Request of email uuids

try:
    # Get email emails multiple
    api_response = api_instance.get_email_emails_multiple(storefront_oid, email_commseq_emails_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_emails_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_commseq_emails_request** | [**EmailCommseqEmailsRequest**](EmailCommseqEmailsRequest.md)| Request of email uuids | 

### Return type

[**EmailCommseqEmailsResponse**](EmailCommseqEmailsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_flow**
> EmailFlowResponse get_email_flow(storefront_oid, email_flow_uuid)

Get email flow

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_flow_uuid = 'email_flow_uuid_example' # str | 

try:
    # Get email flow
    api_response = api_instance.get_email_flow(storefront_oid, email_flow_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_flow_uuid** | **str**|  | 

### Return type

[**EmailFlowResponse**](EmailFlowResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_flow_folder**
> EmailFlowFolderResponse get_email_flow_folder(storefront_oid, email_flow_folder_uuid)

Get email flow folder

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_flow_folder_uuid = 'email_flow_folder_uuid_example' # str | 

try:
    # Get email flow folder
    api_response = api_instance.get_email_flow_folder(storefront_oid, email_flow_folder_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_flow_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_flow_folder_uuid** | **str**|  | 

### Return type

[**EmailFlowFolderResponse**](EmailFlowFolderResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_flow_folders**
> EmailFlowFoldersResponse get_email_flow_folders(storefront_oid)

Get email flow folders

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email flow folders
    api_response = api_instance.get_email_flow_folders(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_flow_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailFlowFoldersResponse**](EmailFlowFoldersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_flow_screenshots**
> ScreenshotsResponse get_email_flow_screenshots(storefront_oid, email_flow_uuid)

Get email flow screenshots

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_flow_uuid = 'email_flow_uuid_example' # str | 

try:
    # Get email flow screenshots
    api_response = api_instance.get_email_flow_screenshots(storefront_oid, email_flow_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_flow_screenshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_flow_uuid** | **str**|  | 

### Return type

[**ScreenshotsResponse**](ScreenshotsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_flows**
> EmailFlowsResponse get_email_flows(storefront_oid)

Get email flows

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email flows
    api_response = api_instance.get_email_flows(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_flows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailFlowsResponse**](EmailFlowsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_global_settings**
> EmailGlobalSettingsResponse get_email_global_settings()

Get email globalsettings

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)


try:
    # Get email globalsettings
    api_response = api_instance.get_email_global_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_global_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EmailGlobalSettingsResponse**](EmailGlobalSettingsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list**
> EmailListResponse get_email_list(storefront_oid, email_list_uuid)

Get email list

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list_uuid = 'email_list_uuid_example' # str | 

try:
    # Get email list
    api_response = api_instance.get_email_list(storefront_oid, email_list_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list_uuid** | **str**|  | 

### Return type

[**EmailListResponse**](EmailListResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list_customer_editor_url**
> EmailCustomerEditorUrlResponse get_email_list_customer_editor_url(storefront_oid, email_list_uuid, email_customer_uuid)

Get email list customer editor url

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list_uuid = 'email_list_uuid_example' # str | 
email_customer_uuid = 'email_customer_uuid_example' # str | 

try:
    # Get email list customer editor url
    api_response = api_instance.get_email_list_customer_editor_url(storefront_oid, email_list_uuid, email_customer_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_list_customer_editor_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list_uuid** | **str**|  | 
 **email_customer_uuid** | **str**|  | 

### Return type

[**EmailCustomerEditorUrlResponse**](EmailCustomerEditorUrlResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list_customers**
> EmailListCustomersResponse get_email_list_customers(storefront_oid, email_list_uuid, page_number=page_number, page_size=page_size)

Get email list customers

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list_uuid = 'email_list_uuid_example' # str | 
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Get email list customers
    api_response = api_instance.get_email_list_customers(storefront_oid, email_list_uuid, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_list_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list_uuid** | **str**|  | 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**EmailListCustomersResponse**](EmailListCustomersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list_segment_folder**
> EmailListSegmentFolderResponse get_email_list_segment_folder(storefront_oid, email_list_segment_folder_uuid)

Get email campaign folder

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list_segment_folder_uuid = 'email_list_segment_folder_uuid_example' # str | 

try:
    # Get email campaign folder
    api_response = api_instance.get_email_list_segment_folder(storefront_oid, email_list_segment_folder_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_list_segment_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list_segment_folder_uuid** | **str**|  | 

### Return type

[**EmailListSegmentFolderResponse**](EmailListSegmentFolderResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list_segment_folders**
> EmailListSegmentFoldersResponse get_email_list_segment_folders(storefront_oid)

Get email campaign folders

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email campaign folders
    api_response = api_instance.get_email_list_segment_folders(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_list_segment_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailListSegmentFoldersResponse**](EmailListSegmentFoldersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_lists**
> EmailListsResponse get_email_lists(storefront_oid)

Get email lists

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email lists
    api_response = api_instance.get_email_lists(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailListsResponse**](EmailListsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_performance**
> EmailPerformanceResponse get_email_performance(storefront_oid)

Get email performance

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email performance
    api_response = api_instance.get_email_performance(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailPerformanceResponse**](EmailPerformanceResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_plan**
> EmailPlanResponse get_email_plan(storefront_oid)

Get email plan

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email plan
    api_response = api_instance.get_email_plan(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailPlanResponse**](EmailPlanResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_postcard**
> EmailCommseqPostcardResponse get_email_postcard(storefront_oid, commseq_postcard_uuid)

Get email postcard

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_postcard_uuid = 'commseq_postcard_uuid_example' # str | 

try:
    # Get email postcard
    api_response = api_instance.get_email_postcard(storefront_oid, commseq_postcard_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_postcard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_postcard_uuid** | **str**|  | 

### Return type

[**EmailCommseqPostcardResponse**](EmailCommseqPostcardResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_postcards**
> EmailCommseqPostcardsResponse get_email_postcards(storefront_oid)

Get email postcards

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email postcards
    api_response = api_instance.get_email_postcards(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_postcards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailCommseqPostcardsResponse**](EmailCommseqPostcardsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_postcards_multiple**
> EmailCommseqPostcardsResponse get_email_postcards_multiple(storefront_oid, email_commseq_postcards_request)

Get email postcards multiple

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_commseq_postcards_request = ultracart.EmailCommseqPostcardsRequest() # EmailCommseqPostcardsRequest | Request of postcard uuids

try:
    # Get email postcards multiple
    api_response = api_instance.get_email_postcards_multiple(storefront_oid, email_commseq_postcards_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_postcards_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_commseq_postcards_request** | [**EmailCommseqPostcardsRequest**](EmailCommseqPostcardsRequest.md)| Request of postcard uuids | 

### Return type

[**EmailCommseqPostcardsResponse**](EmailCommseqPostcardsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_segment**
> EmailSegmentResponse get_email_segment(storefront_oid, email_segment_uuid)

Get email segment

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_segment_uuid = 'email_segment_uuid_example' # str | 

try:
    # Get email segment
    api_response = api_instance.get_email_segment(storefront_oid, email_segment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_segment_uuid** | **str**|  | 

### Return type

[**EmailSegmentResponse**](EmailSegmentResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_segment_customer_editor_url**
> EmailCustomerEditorUrlResponse get_email_segment_customer_editor_url(storefront_oid, email_segment_uuid, email_customer_uuid)

Get email segment customers editor URL

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_segment_uuid = 'email_segment_uuid_example' # str | 
email_customer_uuid = 'email_customer_uuid_example' # str | 

try:
    # Get email segment customers editor URL
    api_response = api_instance.get_email_segment_customer_editor_url(storefront_oid, email_segment_uuid, email_customer_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_segment_customer_editor_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_segment_uuid** | **str**|  | 
 **email_customer_uuid** | **str**|  | 

### Return type

[**EmailCustomerEditorUrlResponse**](EmailCustomerEditorUrlResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_segment_customers**
> EmailSegmentCustomersResponse get_email_segment_customers(storefront_oid, email_segment_uuid, page_number=page_number, page_size=page_size)

Get email segment customers

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_segment_uuid = 'email_segment_uuid_example' # str | 
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Get email segment customers
    api_response = api_instance.get_email_segment_customers(storefront_oid, email_segment_uuid, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_segment_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_segment_uuid** | **str**|  | 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**EmailSegmentCustomersResponse**](EmailSegmentCustomersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_segments**
> EmailSegmentsResponse get_email_segments(storefront_oid)

Get email segments

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email segments
    api_response = api_instance.get_email_segments(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailSegmentsResponse**](EmailSegmentsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_sending_domain**
> EmailSendingDomainResponse get_email_sending_domain(domain)

Get email sending domain

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

domain = 'domain_example' # str | 

try:
    # Get email sending domain
    api_response = api_instance.get_email_sending_domain(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_sending_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 

### Return type

[**EmailSendingDomainResponse**](EmailSendingDomainResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_sending_domain_status**
> EmailSendingDomainResponse get_email_sending_domain_status(domain)

Get email sending domain status

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

domain = 'domain_example' # str | 

try:
    # Get email sending domain status
    api_response = api_instance.get_email_sending_domain_status(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_sending_domain_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 

### Return type

[**EmailSendingDomainResponse**](EmailSendingDomainResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_sending_domains**
> EmailSendingDomainsResponse get_email_sending_domains()

Get email sending domains

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)


try:
    # Get email sending domains
    api_response = api_instance.get_email_sending_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_sending_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EmailSendingDomainsResponse**](EmailSendingDomainsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_settings**
> EmailSettingsResponse get_email_settings(storefront_oid)

Get email settings

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get email settings
    api_response = api_instance.get_email_settings(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailSettingsResponse**](EmailSettingsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_template**
> EmailTemplate get_email_template(storefront_oid, email_template_oid)

Get email template

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_template_oid = 56 # int | 

try:
    # Get email template
    api_response = api_instance.get_email_template(storefront_oid, email_template_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_template_oid** | **int**|  | 

### Return type

[**EmailTemplate**](EmailTemplate.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_templates**
> EmailTemplatesResponse get_email_templates(storefront_oid, trigger_type=trigger_type)

Get email templates

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
trigger_type = 'trigger_type_example' # str |  (optional)

try:
    # Get email templates
    api_response = api_instance.get_email_templates(storefront_oid, trigger_type=trigger_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **trigger_type** | **str**|  | [optional] 

### Return type

[**EmailTemplatesResponse**](EmailTemplatesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_third_party_providers**
> EmailThirdPartyProvidersResponse get_email_third_party_providers(storefront_oid)

Get a list of third party email providers

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get a list of third party email providers
    api_response = api_instance.get_email_third_party_providers(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_third_party_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**EmailThirdPartyProvidersResponse**](EmailThirdPartyProvidersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiments**
> ExperimentsResponse get_experiments(storefront_oid)

Get experiments

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get experiments
    api_response = api_instance.get_experiments(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_experiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**ExperimentsResponse**](ExperimentsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heatmap**
> ScreenRecordingHeatmapResponse get_heatmap(storefront_oid, query)

Get screen recording heatmap

Get screen recording heatmap 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
query = ultracart.ScreenRecordingHeatmapRequest() # ScreenRecordingHeatmapRequest | Query

try:
    # Get screen recording heatmap
    api_response = api_instance.get_heatmap(storefront_oid, query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_heatmap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **query** | [**ScreenRecordingHeatmapRequest**](ScreenRecordingHeatmapRequest.md)| Query | 

### Return type

[**ScreenRecordingHeatmapResponse**](ScreenRecordingHeatmapResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heatmap_index**
> ScreenRecordingHeatmapIndexResponse get_heatmap_index(storefront_oid, query, limit=limit, offset=offset, sort=sort)

Get screen recording heatmap index

Get screen recording heatmap index 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
query = ultracart.ScreenRecordingHeatmapIndexRequest() # ScreenRecordingHeatmapIndexRequest | Query
limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 500) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

try:
    # Get screen recording heatmap index
    api_response = api_instance.get_heatmap_index(storefront_oid, query, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_heatmap_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **query** | [**ScreenRecordingHeatmapIndexRequest**](ScreenRecordingHeatmapIndexRequest.md)| Query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 500) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 

### Return type

[**ScreenRecordingHeatmapIndexResponse**](ScreenRecordingHeatmapIndexResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_histogram_property_names**
> EmailHistogramPropertyNamesResponse get_histogram_property_names(storefront_oid, property_type=property_type)

Get histogram property names

Obtain a list of property names for a given property type 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
property_type = 'property_type_example' # str |  (optional)

try:
    # Get histogram property names
    api_response = api_instance.get_histogram_property_names(storefront_oid, property_type=property_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_histogram_property_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **property_type** | **str**|  | [optional] 

### Return type

[**EmailHistogramPropertyNamesResponse**](EmailHistogramPropertyNamesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_histogram_property_values**
> EmailHistogramPropertyValuesResponse get_histogram_property_values(storefront_oid, property_name=property_name, property_type=property_type, limit=limit)

Get histogram property values

Obtain a list of property values for a given property name and type 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
property_name = 'property_name_example' # str |  (optional)
property_type = 'property_type_example' # str |  (optional)
limit = 56 # int |  (optional)

try:
    # Get histogram property values
    api_response = api_instance.get_histogram_property_values(storefront_oid, property_name=property_name, property_type=property_type, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_histogram_property_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **property_name** | **str**|  | [optional] 
 **property_type** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**EmailHistogramPropertyValuesResponse**](EmailHistogramPropertyValuesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_filter_values**
> LibraryFilterValuesResponse get_library_filter_values()

Get library values used to populate drop down boxes for filtering.

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)


try:
    # Get library values used to populate drop down boxes for filtering.
    api_response = api_instance.get_library_filter_values()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_library_filter_values: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LibraryFilterValuesResponse**](LibraryFilterValuesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_item**
> LibraryItemResponse get_library_item(library_item_oid)

Get library item.

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

library_item_oid = 56 # int | 

try:
    # Get library item.
    api_response = api_instance.get_library_item(library_item_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_library_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_oid** | **int**|  | 

### Return type

[**LibraryItemResponse**](LibraryItemResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_item_published_versions**
> LibraryItemsResponse get_library_item_published_versions(library_item_oid)

Get all published versions for a library item.

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

library_item_oid = 56 # int | 

try:
    # Get all published versions for a library item.
    api_response = api_instance.get_library_item_published_versions(library_item_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_library_item_published_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_oid** | **int**|  | 

### Return type

[**LibraryItemsResponse**](LibraryItemsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recording**
> ScreenRecordingResponse get_screen_recording(storefront_oid, screen_recording_uuid)

Get screen recording

Get screen recording 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
screen_recording_uuid = 'screen_recording_uuid_example' # str | 

try:
    # Get screen recording
    api_response = api_instance.get_screen_recording(storefront_oid, screen_recording_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_screen_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **screen_recording_uuid** | **str**|  | 

### Return type

[**ScreenRecordingResponse**](ScreenRecordingResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recording_page_view_data**
> ScreenRecordingPageViewDataResponse get_screen_recording_page_view_data(storefront_oid, screen_recording_uuid, screen_recording_page_view_uuid)

Get screen recording page view data

Get screen recording page view data 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
screen_recording_uuid = 'screen_recording_uuid_example' # str | 
screen_recording_page_view_uuid = 'screen_recording_page_view_uuid_example' # str | 

try:
    # Get screen recording page view data
    api_response = api_instance.get_screen_recording_page_view_data(storefront_oid, screen_recording_uuid, screen_recording_page_view_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_screen_recording_page_view_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **screen_recording_uuid** | **str**|  | 
 **screen_recording_page_view_uuid** | **str**|  | 

### Return type

[**ScreenRecordingPageViewDataResponse**](ScreenRecordingPageViewDataResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recording_segment**
> ScreenRecordingSegmentResponse get_screen_recording_segment(storefront_oid, screen_recording_segment_oid)

Get screen recording segment

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
screen_recording_segment_oid = 56 # int | 

try:
    # Get screen recording segment
    api_response = api_instance.get_screen_recording_segment(storefront_oid, screen_recording_segment_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_screen_recording_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **screen_recording_segment_oid** | **int**|  | 

### Return type

[**ScreenRecordingSegmentResponse**](ScreenRecordingSegmentResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recording_segments**
> ScreenRecordingSegmentsResponse get_screen_recording_segments(storefront_oid)

Get screen recording segments

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get screen recording segments
    api_response = api_instance.get_screen_recording_segments(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_screen_recording_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**ScreenRecordingSegmentsResponse**](ScreenRecordingSegmentsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recording_settings**
> ScreenRecordingSettingsResponse get_screen_recording_settings(storefront_oid)

Get screen recording settings

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get screen recording settings
    api_response = api_instance.get_screen_recording_settings(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_screen_recording_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**ScreenRecordingSettingsResponse**](ScreenRecordingSettingsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recording_tags**
> ScreenRecordingTagsResponse get_screen_recording_tags(storefront_oid)

Get tags used by screen recording

Get tags used by screen recording 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Get tags used by screen recording
    api_response = api_instance.get_screen_recording_tags(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_screen_recording_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**ScreenRecordingTagsResponse**](ScreenRecordingTagsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recordings_by_query**
> ScreenRecordingQueryResponse get_screen_recordings_by_query(storefront_oid, query, limit=limit, offset=offset, sort=sort)

Query screen recordings

Query screen recordings 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
query = ultracart.ScreenRecordingQueryRequest() # ScreenRecordingQueryRequest | Query
limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 500) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

try:
    # Query screen recordings
    api_response = api_instance.get_screen_recordings_by_query(storefront_oid, query, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_screen_recordings_by_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **query** | [**ScreenRecordingQueryRequest**](ScreenRecordingQueryRequest.md)| Query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 500) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 

### Return type

[**ScreenRecordingQueryResponse**](ScreenRecordingQueryResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recordings_by_segment**
> ScreenRecordingQueryResponse get_screen_recordings_by_segment(storefront_oid, screen_recording_segment_oid, limit=limit, offset=offset, sort=sort)

Get screen recordings by segment

Get screen recordings by segment 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
screen_recording_segment_oid = 56 # int | 
limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 500) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

try:
    # Get screen recordings by segment
    api_response = api_instance.get_screen_recordings_by_segment(storefront_oid, screen_recording_segment_oid, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_screen_recordings_by_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **screen_recording_segment_oid** | **int**|  | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 500) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 

### Return type

[**ScreenRecordingQueryResponse**](ScreenRecordingQueryResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store_front_pricing_tiers**
> PricingTiersResponse get_store_front_pricing_tiers(expand=expand)

Retrieve pricing tiers

Retrieves the pricing tiers 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try:
    # Retrieve pricing tiers
    api_response = api_instance.get_store_front_pricing_tiers(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_store_front_pricing_tiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**PricingTiersResponse**](PricingTiersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnail_parameters**
> ThumbnailParametersResponse get_thumbnail_parameters(thumbnail_parameters)

Get thumbnail parameters

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

thumbnail_parameters = ultracart.ThumbnailParametersRequest() # ThumbnailParametersRequest | Thumbnail Parameters

try:
    # Get thumbnail parameters
    api_response = api_instance.get_thumbnail_parameters(thumbnail_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_thumbnail_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thumbnail_parameters** | [**ThumbnailParametersRequest**](ThumbnailParametersRequest.md)| Thumbnail Parameters | 

### Return type

[**ThumbnailParametersResponse**](ThumbnailParametersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_email**
> TransactionEmailResponse get_transaction_email(storefront_oid, email_id)

Gets a transaction email object

Fetch a transactional email 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_id = 'email_id_example' # str | 

try:
    # Gets a transaction email object
    api_response = api_instance.get_transaction_email(storefront_oid, email_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_transaction_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_id** | **str**|  | 

### Return type

[**TransactionEmailResponse**](TransactionEmailResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_email_list**
> TransactionEmailListResponse get_transaction_email_list(storefront_oid)

Gets a list of transaction email names

Obtain a list of all transactional emails and return back just their names 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 

try:
    # Gets a list of transaction email names
    api_response = api_instance.get_transaction_email_list(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_transaction_email_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 

### Return type

[**TransactionEmailListResponse**](TransactionEmailListResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_email_screenshots**
> ScreenshotsResponse get_transaction_email_screenshots(storefront_oid, email_id)

Get transactional email screenshots

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_id = 'email_id_example' # str | 

try:
    # Get transactional email screenshots
    api_response = api_instance.get_transaction_email_screenshots(storefront_oid, email_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_transaction_email_screenshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_id** | **str**|  | 

### Return type

[**ScreenshotsResponse**](ScreenshotsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_twilio_account**
> TwilioResponse get_twilio_account(esp_twilio_uuid)

Get Twilio account

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

esp_twilio_uuid = 'esp_twilio_uuid_example' # str | 

try:
    # Get Twilio account
    api_response = api_instance.get_twilio_account(esp_twilio_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_twilio_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **esp_twilio_uuid** | **str**|  | 

### Return type

[**TwilioResponse**](TwilioResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_twilio_accounts**
> TwiliosResponse get_twilio_accounts()

Get all Twilio accounts

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)


try:
    # Get all Twilio accounts
    api_response = api_instance.get_twilio_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_twilio_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TwiliosResponse**](TwiliosResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_unsubscribe**
> EmailGlobalUnsubscribeResponse global_unsubscribe(storefront_oid, unsubscribe)

Globally unsubscribe a customer

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
unsubscribe = ultracart.EmailGlobalUnsubscribeRequest() # EmailGlobalUnsubscribeRequest | Unsubscribe

try:
    # Globally unsubscribe a customer
    api_response = api_instance.global_unsubscribe(storefront_oid, unsubscribe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->global_unsubscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **unsubscribe** | [**EmailGlobalUnsubscribeRequest**](EmailGlobalUnsubscribeRequest.md)| Unsubscribe | 

### Return type

[**EmailGlobalUnsubscribeResponse**](EmailGlobalUnsubscribeResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_email_third_party_provider_list**
> import_email_third_party_provider_list(storefront_oid, import_request)

Import a third party provider list

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
import_request = ultracart.EmailThirdPartyListImportRequest() # EmailThirdPartyListImportRequest | lists to import

try:
    # Import a third party provider list
    api_instance.import_email_third_party_provider_list(storefront_oid, import_request)
except ApiException as e:
    print("Exception when calling StorefrontApi->import_email_third_party_provider_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **import_request** | [**EmailThirdPartyListImportRequest**](EmailThirdPartyListImportRequest.md)| lists to import | 

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_campaign**
> EmailCampaignResponse insert_email_campaign(storefront_oid, email_campaign)

Insert email campaign

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_campaign = ultracart.EmailCampaign() # EmailCampaign | Email campaign

try:
    # Insert email campaign
    api_response = api_instance.insert_email_campaign(storefront_oid, email_campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_campaign** | [**EmailCampaign**](EmailCampaign.md)| Email campaign | 

### Return type

[**EmailCampaignResponse**](EmailCampaignResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_campaign_folder**
> EmailCampaignFolderResponse insert_email_campaign_folder(storefront_oid, email_campaign_folder)

Insert email campaign folder

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_campaign_folder = ultracart.EmailCampaignFolder() # EmailCampaignFolder | Email campaign folder

try:
    # Insert email campaign folder
    api_response = api_instance.insert_email_campaign_folder(storefront_oid, email_campaign_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_campaign_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_campaign_folder** | [**EmailCampaignFolder**](EmailCampaignFolder.md)| Email campaign folder | 

### Return type

[**EmailCampaignFolderResponse**](EmailCampaignFolderResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_commseq**
> EmailCommseqResponse insert_email_commseq(storefront_oid, email_commseq)

Insert email commseq

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_commseq = ultracart.EmailCommseq() # EmailCommseq | Email commseq

try:
    # Insert email commseq
    api_response = api_instance.insert_email_commseq(storefront_oid, email_commseq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_commseq: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_commseq** | [**EmailCommseq**](EmailCommseq.md)| Email commseq | 

### Return type

[**EmailCommseqResponse**](EmailCommseqResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_email**
> EmailCommseqEmailResponse insert_email_email(storefront_oid, email_commseq_email)

Insert email email

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_commseq_email = ultracart.EmailCommseqEmail() # EmailCommseqEmail | Email email

try:
    # Insert email email
    api_response = api_instance.insert_email_email(storefront_oid, email_commseq_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_commseq_email** | [**EmailCommseqEmail**](EmailCommseqEmail.md)| Email email | 

### Return type

[**EmailCommseqEmailResponse**](EmailCommseqEmailResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_flow**
> EmailFlowResponse insert_email_flow(storefront_oid, email_flow)

Insert email flow

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_flow = ultracart.EmailFlow() # EmailFlow | Email flow

try:
    # Insert email flow
    api_response = api_instance.insert_email_flow(storefront_oid, email_flow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_flow** | [**EmailFlow**](EmailFlow.md)| Email flow | 

### Return type

[**EmailFlowResponse**](EmailFlowResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_flow_folder**
> EmailFlowFolderResponse insert_email_flow_folder(storefront_oid, email_flow_folder)

Insert email flow folder

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_flow_folder = ultracart.EmailFlowFolder() # EmailFlowFolder | Email flow folder

try:
    # Insert email flow folder
    api_response = api_instance.insert_email_flow_folder(storefront_oid, email_flow_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_flow_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_flow_folder** | [**EmailFlowFolder**](EmailFlowFolder.md)| Email flow folder | 

### Return type

[**EmailFlowFolderResponse**](EmailFlowFolderResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_list**
> EmailListResponse insert_email_list(storefront_oid, email_list)

Insert email list

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list = ultracart.EmailList() # EmailList | Email list

try:
    # Insert email list
    api_response = api_instance.insert_email_list(storefront_oid, email_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list** | [**EmailList**](EmailList.md)| Email list | 

### Return type

[**EmailListResponse**](EmailListResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_list_segment_folder**
> EmailListSegmentFolderResponse insert_email_list_segment_folder(storefront_oid, email_list_segment_folder)

Insert email campaign folder

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list_segment_folder = ultracart.EmailListSegmentFolder() # EmailListSegmentFolder | Email campaign folder

try:
    # Insert email campaign folder
    api_response = api_instance.insert_email_list_segment_folder(storefront_oid, email_list_segment_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_list_segment_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list_segment_folder** | [**EmailListSegmentFolder**](EmailListSegmentFolder.md)| Email campaign folder | 

### Return type

[**EmailListSegmentFolderResponse**](EmailListSegmentFolderResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_postcard**
> EmailCommseqPostcardResponse insert_email_postcard(storefront_oid, email_commseq_postcard)

Insert email postcard

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_commseq_postcard = ultracart.EmailCommseqPostcard() # EmailCommseqPostcard | Email postcard

try:
    # Insert email postcard
    api_response = api_instance.insert_email_postcard(storefront_oid, email_commseq_postcard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_postcard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_commseq_postcard** | [**EmailCommseqPostcard**](EmailCommseqPostcard.md)| Email postcard | 

### Return type

[**EmailCommseqPostcardResponse**](EmailCommseqPostcardResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_segment**
> EmailSegmentResponse insert_email_segment(storefront_oid, email_segment)

Insert email segment

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_segment = ultracart.EmailSegment() # EmailSegment | Email segment

try:
    # Insert email segment
    api_response = api_instance.insert_email_segment(storefront_oid, email_segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_segment** | [**EmailSegment**](EmailSegment.md)| Email segment | 

### Return type

[**EmailSegmentResponse**](EmailSegmentResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_screen_recording_segment**
> ScreenRecordingSegmentResponse insert_screen_recording_segment(storefront_oid, segment)

Insert screen recording segment

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
segment = ultracart.ScreenRecordingSegment() # ScreenRecordingSegment | Segment

try:
    # Insert screen recording segment
    api_response = api_instance.insert_screen_recording_segment(storefront_oid, segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_screen_recording_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **segment** | [**ScreenRecordingSegment**](ScreenRecordingSegment.md)| Segment | 

### Return type

[**ScreenRecordingSegmentResponse**](ScreenRecordingSegmentResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepare_download_email_segment**
> EmailSegmentDownloadPrepareResponse prepare_download_email_segment(storefront_oid, email_segment_uuid)

Prepare download of email segment

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_segment_uuid = 'email_segment_uuid_example' # str | 

try:
    # Prepare download of email segment
    api_response = api_instance.prepare_download_email_segment(storefront_oid, email_segment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->prepare_download_email_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_segment_uuid** | **str**|  | 

### Return type

[**EmailSegmentDownloadPrepareResponse**](EmailSegmentDownloadPrepareResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_library_item**
> LibraryItemResponse publish_library_item(library_item_oid, publish_library_request)

Publish library item.

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

library_item_oid = 56 # int | 
publish_library_request = ultracart.PublishLibraryItemRequest() # PublishLibraryItemRequest | Publish library item request

try:
    # Publish library item.
    api_response = api_instance.publish_library_item(library_item_oid, publish_library_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->publish_library_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_oid** | **int**|  | 
 **publish_library_request** | [**PublishLibraryItemRequest**](PublishLibraryItemRequest.md)| Publish library item request | 

### Return type

[**LibraryItemResponse**](LibraryItemResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_library_item**
> LibraryItemResponse purchase_library_item(library_item_oid, storefront_oid=storefront_oid)

Purchase public library item, which creates a copy of the item in your personal code library

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

library_item_oid = 56 # int | 
storefront_oid = 56 # int |  (optional)

try:
    # Purchase public library item, which creates a copy of the item in your personal code library
    api_response = api_instance.purchase_library_item(library_item_oid, storefront_oid=storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->purchase_library_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_oid** | **int**|  | 
 **storefront_oid** | **int**|  | [optional] 

### Return type

[**LibraryItemResponse**](LibraryItemResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_email_commseq_step_waiting**
> release_email_commseq_step_waiting(storefront_oid, commseq_uuid, commseq_step_uuid)

Release email communication sequence customers waiting at the specified step

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 
commseq_step_uuid = 'commseq_step_uuid_example' # str | 

try:
    # Release email communication sequence customers waiting at the specified step
    api_instance.release_email_commseq_step_waiting(storefront_oid, commseq_uuid, commseq_step_uuid)
except ApiException as e:
    print("Exception when calling StorefrontApi->release_email_commseq_step_waiting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 
 **commseq_step_uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review**
> EmailCommseqEmailSendTestResponse review(storefront_oid, commseq_email_uuid, email_commseq_email_review_request)

Request a review of an email

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_email_uuid = 'commseq_email_uuid_example' # str | 
email_commseq_email_review_request = ultracart.EmailCommseqEmailSendTestRequest() # EmailCommseqEmailSendTestRequest | Email commseq email review request

try:
    # Request a review of an email
    api_response = api_instance.review(storefront_oid, commseq_email_uuid, email_commseq_email_review_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_email_uuid** | **str**|  | 
 **email_commseq_email_review_request** | [**EmailCommseqEmailSendTestRequest**](EmailCommseqEmailSendTestRequest.md)| Email commseq email review request | 

### Return type

[**EmailCommseqEmailSendTestResponse**](EmailCommseqEmailSendTestResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> LookupResponse search(category=category, matches=matches, storefront_oid=storefront_oid, max_hits=max_hits, subcategory=subcategory)

Searches for all matching values

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

category = 'category_example' # str |  (optional)
matches = 'matches_example' # str |  (optional)
storefront_oid = 'storefront_oid_example' # str |  (optional)
max_hits = 56 # int |  (optional)
subcategory = 'subcategory_example' # str |  (optional)

try:
    # Searches for all matching values
    api_response = api_instance.search(category=category, matches=matches, storefront_oid=storefront_oid, max_hits=max_hits, subcategory=subcategory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | [optional] 
 **matches** | **str**|  | [optional] 
 **storefront_oid** | **str**|  | [optional] 
 **max_hits** | **int**|  | [optional] 
 **subcategory** | **str**|  | [optional] 

### Return type

[**LookupResponse**](LookupResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search2**
> LookupResponse search2(lookup_request)

Searches for all matching values (using POST)

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

lookup_request = ultracart.LookupRequest() # LookupRequest | LookupRequest

try:
    # Searches for all matching values (using POST)
    api_response = api_instance.search2(lookup_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->search2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookup_request** | [**LookupRequest**](LookupRequest.md)| LookupRequest | 

### Return type

[**LookupResponse**](LookupResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_email_list_customers**
> EmailListCustomersResponse search_email_list_customers(storefront_oid, email_list_uuid, starts_with=starts_with)

Search email list customers

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list_uuid = 'email_list_uuid_example' # str | 
starts_with = 'starts_with_example' # str |  (optional)

try:
    # Search email list customers
    api_response = api_instance.search_email_list_customers(storefront_oid, email_list_uuid, starts_with=starts_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->search_email_list_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list_uuid** | **str**|  | 
 **starts_with** | **str**|  | [optional] 

### Return type

[**EmailListCustomersResponse**](EmailListCustomersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_email_segment_customers**
> EmailSegmentCustomersResponse search_email_segment_customers(storefront_oid, email_segment_uuid, starts_with=starts_with)

Search email segment customers

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_segment_uuid = 'email_segment_uuid_example' # str | 
starts_with = 'starts_with_example' # str |  (optional)

try:
    # Search email segment customers
    api_response = api_instance.search_email_segment_customers(storefront_oid, email_segment_uuid, starts_with=starts_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->search_email_segment_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_segment_uuid** | **str**|  | 
 **starts_with** | **str**|  | [optional] 

### Return type

[**EmailSegmentCustomersResponse**](EmailSegmentCustomersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_library_items**
> LibraryItemsResponse search_library_items(item_query, limit=limit, offset=offset, sort=sort)

Retrieve library items

Retrieves a library items based on a query object.  If no parameters are specified, the API call will default to the merchant id only.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

item_query = ultracart.LibraryItemQuery() # LibraryItemQuery | Item query
limit = 10000 # int | The maximum number of records to return on this one API call. (Maximum 10000) (optional) (default to 10000)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

try:
    # Retrieve library items
    api_response = api_instance.search_library_items(item_query, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->search_library_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_query** | [**LibraryItemQuery**](LibraryItemQuery.md)| Item query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 10000) | [optional] [default to 10000]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 

### Return type

[**LibraryItemsResponse**](LibraryItemsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_published_items**
> LibraryItemsResponse search_published_items(item_query, limit=limit, offset=offset, sort=sort)

Retrieve library items

Retrieves a library items based on a query object.  If no parameters are specified, the API call will default to the merchant id only.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

item_query = ultracart.LibraryItemQuery() # LibraryItemQuery | Item query
limit = 10000 # int | The maximum number of records to return on this one API call. (Maximum 10000) (optional) (default to 10000)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

try:
    # Retrieve library items
    api_response = api_instance.search_published_items(item_query, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->search_published_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_query** | [**LibraryItemQuery**](LibraryItemQuery.md)| Item query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 10000) | [optional] [default to 10000]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 

### Return type

[**LibraryItemsResponse**](LibraryItemsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_review_items**
> LibraryItemsResponse search_review_items(item_query, limit=limit, offset=offset, sort=sort)

Retrieve library items needing review or rejected

Retrieves a library items based on a query object.  If no parameters are specified, the API call will default to the merchant id only.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

item_query = ultracart.LibraryItemQuery() # LibraryItemQuery | Item query
limit = 10000 # int | The maximum number of records to return on this one API call. (Maximum 10000) (optional) (default to 10000)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

try:
    # Retrieve library items needing review or rejected
    api_response = api_instance.search_review_items(item_query, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->search_review_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_query** | [**LibraryItemQuery**](LibraryItemQuery.md)| Item query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 10000) | [optional] [default to 10000]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 

### Return type

[**LibraryItemsResponse**](LibraryItemsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_shared_items**
> LibraryItemsResponse search_shared_items(item_query, limit=limit, offset=offset, sort=sort)

Retrieve library items

Retrieves a library items based on a query object.  If no parameters are specified, the API call will default to the merchant id only.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

item_query = ultracart.LibraryItemQuery() # LibraryItemQuery | Item query
limit = 10000 # int | The maximum number of records to return on this one API call. (Maximum 10000) (optional) (default to 10000)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
sort = 'sort_example' # str | The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

try:
    # Retrieve library items
    api_response = api_instance.search_shared_items(item_query, limit=limit, offset=offset, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->search_shared_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_query** | [**LibraryItemQuery**](LibraryItemQuery.md)| Item query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 10000) | [optional] [default to 10000]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **sort** | **str**| The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 

### Return type

[**LibraryItemsResponse**](LibraryItemsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_test**
> EmailCommseqEmailSendTestResponse send_email_test(storefront_oid, commseq_email_uuid, email_commseq_email_test_request)

Send email test

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_email_uuid = 'commseq_email_uuid_example' # str | 
email_commseq_email_test_request = ultracart.EmailCommseqEmailSendTestRequest() # EmailCommseqEmailSendTestRequest | Email commseq email test request

try:
    # Send email test
    api_response = api_instance.send_email_test(storefront_oid, commseq_email_uuid, email_commseq_email_test_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->send_email_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_email_uuid** | **str**|  | 
 **email_commseq_email_test_request** | [**EmailCommseqEmailSendTestRequest**](EmailCommseqEmailSendTestRequest.md)| Email commseq email test request | 

### Return type

[**EmailCommseqEmailSendTestResponse**](EmailCommseqEmailSendTestResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_postcard_test**
> EmailCommseqPostcardSendTestResponse send_postcard_test(storefront_oid, commseq_postcard_uuid, email_commseq_postcard_test_request)

Send postcard test

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_postcard_uuid = 'commseq_postcard_uuid_example' # str | 
email_commseq_postcard_test_request = ultracart.EmailCommseqPostcardSendTestRequest() # EmailCommseqPostcardSendTestRequest | Email commseq email test request

try:
    # Send postcard test
    api_response = api_instance.send_postcard_test(storefront_oid, commseq_postcard_uuid, email_commseq_postcard_test_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->send_postcard_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_postcard_uuid** | **str**|  | 
 **email_commseq_postcard_test_request** | [**EmailCommseqPostcardSendTestRequest**](EmailCommseqPostcardSendTestRequest.md)| Email commseq email test request | 

### Return type

[**EmailCommseqPostcardSendTestResponse**](EmailCommseqPostcardSendTestResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_webhook_test**
> EmailCommseqEmailSendTestResponse send_webhook_test(storefront_oid, email_commseq_webhook_test_request)

Send webhook test

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_commseq_webhook_test_request = ultracart.EmailCommseqWebhookSendTestRequest() # EmailCommseqWebhookSendTestRequest | Email commseq webhook test request

try:
    # Send webhook test
    api_response = api_instance.send_webhook_test(storefront_oid, email_commseq_webhook_test_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->send_webhook_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_commseq_webhook_test_request** | [**EmailCommseqWebhookSendTestRequest**](EmailCommseqWebhookSendTestRequest.md)| Email commseq webhook test request | 

### Return type

[**EmailCommseqEmailSendTestResponse**](EmailCommseqEmailSendTestResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_email_campaign**
> BaseResponse start_email_campaign(storefront_oid, email_campaign_uuid)

Start email campaign

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_campaign_uuid = 'email_campaign_uuid_example' # str | 

try:
    # Start email campaign
    api_response = api_instance.start_email_campaign(storefront_oid, email_campaign_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->start_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_campaign_uuid** | **str**|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_to_email_list**
> EmailListSubscribeResponse subscribe_to_email_list(storefront_oid, email_list_uuid, customers)

Subscribe customers to email list

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list_uuid = 'email_list_uuid_example' # str | 
customers = [ultracart.EmailCustomer()] # list[EmailCustomer] | Customers

try:
    # Subscribe customers to email list
    api_response = api_instance.subscribe_to_email_list(storefront_oid, email_list_uuid, customers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->subscribe_to_email_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list_uuid** | **str**|  | 
 **customers** | [**list[EmailCustomer]**](EmailCustomer.md)| Customers | 

### Return type

[**EmailListSubscribeResponse**](EmailListSubscribeResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfavorite_screen_recording**
> unfavorite_screen_recording(storefront_oid, screen_recording_uuid)

Remove favorite flag on screen recording

Remove favorite flag on screen recording 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
screen_recording_uuid = 'screen_recording_uuid_example' # str | 

try:
    # Remove favorite flag on screen recording
    api_instance.unfavorite_screen_recording(storefront_oid, screen_recording_uuid)
except ApiException as e:
    print("Exception when calling StorefrontApi->unfavorite_screen_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **screen_recording_uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_campaign**
> EmailCampaignResponse update_email_campaign(storefront_oid, email_campaign_uuid, email_campaign)

Update email campaign

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_campaign_uuid = 'email_campaign_uuid_example' # str | 
email_campaign = ultracart.EmailCampaign() # EmailCampaign | Email campaign

try:
    # Update email campaign
    api_response = api_instance.update_email_campaign(storefront_oid, email_campaign_uuid, email_campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_campaign_uuid** | **str**|  | 
 **email_campaign** | [**EmailCampaign**](EmailCampaign.md)| Email campaign | 

### Return type

[**EmailCampaignResponse**](EmailCampaignResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_campaign_folder**
> EmailCampaignFolderResponse update_email_campaign_folder(storefront_oid, email_campaign_folder_uuid, email_campaign_folder)

Update email campaign folder

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_campaign_folder_uuid = 'email_campaign_folder_uuid_example' # str | 
email_campaign_folder = ultracart.EmailCampaignFolder() # EmailCampaignFolder | Email campaign folder

try:
    # Update email campaign folder
    api_response = api_instance.update_email_campaign_folder(storefront_oid, email_campaign_folder_uuid, email_campaign_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_campaign_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_campaign_folder_uuid** | **str**|  | 
 **email_campaign_folder** | [**EmailCampaignFolder**](EmailCampaignFolder.md)| Email campaign folder | 

### Return type

[**EmailCampaignFolderResponse**](EmailCampaignFolderResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_commseq**
> EmailCommseqResponse update_email_commseq(storefront_oid, commseq_uuid, email_commseq)

Update email commseq

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_uuid = 'commseq_uuid_example' # str | 
email_commseq = ultracart.EmailCommseq() # EmailCommseq | Email commseq

try:
    # Update email commseq
    api_response = api_instance.update_email_commseq(storefront_oid, commseq_uuid, email_commseq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_commseq: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_uuid** | **str**|  | 
 **email_commseq** | [**EmailCommseq**](EmailCommseq.md)| Email commseq | 

### Return type

[**EmailCommseqResponse**](EmailCommseqResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_customer**
> update_email_customer(storefront_oid, email_customer_uuid, email_customer)

Update email customer

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_customer_uuid = 'email_customer_uuid_example' # str | 
email_customer = ultracart.EmailCustomer() # EmailCustomer | Email customer

try:
    # Update email customer
    api_instance.update_email_customer(storefront_oid, email_customer_uuid, email_customer)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_customer_uuid** | **str**|  | 
 **email_customer** | [**EmailCustomer**](EmailCustomer.md)| Email customer | 

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_email**
> EmailCommseqEmailResponse update_email_email(storefront_oid, commseq_email_uuid, email_commseq_email)

Update email email

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_email_uuid = 'commseq_email_uuid_example' # str | 
email_commseq_email = ultracart.EmailCommseqEmail() # EmailCommseqEmail | Email commseq email

try:
    # Update email email
    api_response = api_instance.update_email_email(storefront_oid, commseq_email_uuid, email_commseq_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_email_uuid** | **str**|  | 
 **email_commseq_email** | [**EmailCommseqEmail**](EmailCommseqEmail.md)| Email commseq email | 

### Return type

[**EmailCommseqEmailResponse**](EmailCommseqEmailResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_flow**
> EmailFlowResponse update_email_flow(storefront_oid, email_flow_uuid, email_flow)

Update email flow

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_flow_uuid = 'email_flow_uuid_example' # str | 
email_flow = ultracart.EmailFlow() # EmailFlow | Email flow

try:
    # Update email flow
    api_response = api_instance.update_email_flow(storefront_oid, email_flow_uuid, email_flow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_flow_uuid** | **str**|  | 
 **email_flow** | [**EmailFlow**](EmailFlow.md)| Email flow | 

### Return type

[**EmailFlowResponse**](EmailFlowResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_flow_folder**
> EmailFlowFolderResponse update_email_flow_folder(storefront_oid, email_flow_folder_uuid, email_flow_folder)

Update email flow folder

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_flow_folder_uuid = 'email_flow_folder_uuid_example' # str | 
email_flow_folder = ultracart.EmailFlowFolder() # EmailFlowFolder | Email flow folder

try:
    # Update email flow folder
    api_response = api_instance.update_email_flow_folder(storefront_oid, email_flow_folder_uuid, email_flow_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_flow_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_flow_folder_uuid** | **str**|  | 
 **email_flow_folder** | [**EmailFlowFolder**](EmailFlowFolder.md)| Email flow folder | 

### Return type

[**EmailFlowFolderResponse**](EmailFlowFolderResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_global_settings**
> EmailGlobalSettingsResponse update_email_global_settings(global_settings)

Update email global settings

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

global_settings = ultracart.EmailGlobalSettings() # EmailGlobalSettings | global settings request

try:
    # Update email global settings
    api_response = api_instance.update_email_global_settings(global_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_global_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_settings** | [**EmailGlobalSettings**](EmailGlobalSettings.md)| global settings request | 

### Return type

[**EmailGlobalSettingsResponse**](EmailGlobalSettingsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_list**
> EmailListResponse update_email_list(storefront_oid, email_list_uuid, email_list)

Update email list

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list_uuid = 'email_list_uuid_example' # str | 
email_list = ultracart.EmailList() # EmailList | Email list

try:
    # Update email list
    api_response = api_instance.update_email_list(storefront_oid, email_list_uuid, email_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list_uuid** | **str**|  | 
 **email_list** | [**EmailList**](EmailList.md)| Email list | 

### Return type

[**EmailListResponse**](EmailListResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_list_segment_folder**
> EmailListSegmentFolderResponse update_email_list_segment_folder(storefront_oid, email_list_segment_folder_uuid, email_list_segment_folder)

Update email campaign folder

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_list_segment_folder_uuid = 'email_list_segment_folder_uuid_example' # str | 
email_list_segment_folder = ultracart.EmailListSegmentFolder() # EmailListSegmentFolder | Email campaign folder

try:
    # Update email campaign folder
    api_response = api_instance.update_email_list_segment_folder(storefront_oid, email_list_segment_folder_uuid, email_list_segment_folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_list_segment_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_list_segment_folder_uuid** | **str**|  | 
 **email_list_segment_folder** | [**EmailListSegmentFolder**](EmailListSegmentFolder.md)| Email campaign folder | 

### Return type

[**EmailListSegmentFolderResponse**](EmailListSegmentFolderResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_plan**
> EmailPlanResponse update_email_plan(storefront_oid, settings)

Update email plan

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
settings = ultracart.EmailPlan() # EmailPlan | plan request

try:
    # Update email plan
    api_response = api_instance.update_email_plan(storefront_oid, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **settings** | [**EmailPlan**](EmailPlan.md)| plan request | 

### Return type

[**EmailPlanResponse**](EmailPlanResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_postcard**
> EmailCommseqPostcardResponse update_email_postcard(storefront_oid, commseq_postcard_uuid, email_commseq_postcard)

Update email postcard

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
commseq_postcard_uuid = 'commseq_postcard_uuid_example' # str | 
email_commseq_postcard = ultracart.EmailCommseqPostcard() # EmailCommseqPostcard | Email commseq postcard

try:
    # Update email postcard
    api_response = api_instance.update_email_postcard(storefront_oid, commseq_postcard_uuid, email_commseq_postcard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_postcard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **commseq_postcard_uuid** | **str**|  | 
 **email_commseq_postcard** | [**EmailCommseqPostcard**](EmailCommseqPostcard.md)| Email commseq postcard | 

### Return type

[**EmailCommseqPostcardResponse**](EmailCommseqPostcardResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_segment**
> EmailSegmentResponse update_email_segment(storefront_oid, email_segment_uuid, email_segment)

Update email segment

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_segment_uuid = 'email_segment_uuid_example' # str | 
email_segment = ultracart.EmailSegment() # EmailSegment | Email segment

try:
    # Update email segment
    api_response = api_instance.update_email_segment(storefront_oid, email_segment_uuid, email_segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_segment_uuid** | **str**|  | 
 **email_segment** | [**EmailSegment**](EmailSegment.md)| Email segment | 

### Return type

[**EmailSegmentResponse**](EmailSegmentResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_settings**
> EmailSettingsResponse update_email_settings(storefront_oid, settings)

Update email settings

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
settings = ultracart.EmailSettings() # EmailSettings | settings request

try:
    # Update email settings
    api_response = api_instance.update_email_settings(storefront_oid, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **settings** | [**EmailSettings**](EmailSettings.md)| settings request | 

### Return type

[**EmailSettingsResponse**](EmailSettingsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_experiment**
> ExperimentResponse update_experiment(storefront_oid, storefront_experiment_oid, experiment)

Update experiment

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
storefront_experiment_oid = 56 # int | 
experiment = ultracart.Experiment() # Experiment | Experiment

try:
    # Update experiment
    api_response = api_instance.update_experiment(storefront_oid, storefront_experiment_oid, experiment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **storefront_experiment_oid** | **int**|  | 
 **experiment** | [**Experiment**](Experiment.md)| Experiment | 

### Return type

[**ExperimentResponse**](ExperimentResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_item**
> LibraryItemResponse update_library_item(library_item_oid, library_item)

Update library item. Note that only certain fields may be updated via this method.

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

library_item_oid = 56 # int | 
library_item = ultracart.LibraryItem() # LibraryItem | Library item

try:
    # Update library item. Note that only certain fields may be updated via this method.
    api_response = api_instance.update_library_item(library_item_oid, library_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_library_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **library_item_oid** | **int**|  | 
 **library_item** | [**LibraryItem**](LibraryItem.md)| Library item | 

### Return type

[**LibraryItemResponse**](LibraryItemResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_screen_recording_merchant_notes**
> update_screen_recording_merchant_notes(storefront_oid, screen_recording_uuid, merchant_notes_request)

Update merchant notes on a screen recording

Update merchant notes on a screen recording 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
screen_recording_uuid = 'screen_recording_uuid_example' # str | 
merchant_notes_request = ultracart.ScreenRecordingMerchantNotesRequest() # ScreenRecordingMerchantNotesRequest | Merchant Notes

try:
    # Update merchant notes on a screen recording
    api_instance.update_screen_recording_merchant_notes(storefront_oid, screen_recording_uuid, merchant_notes_request)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_screen_recording_merchant_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **screen_recording_uuid** | **str**|  | 
 **merchant_notes_request** | [**ScreenRecordingMerchantNotesRequest**](ScreenRecordingMerchantNotesRequest.md)| Merchant Notes | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_screen_recording_segment**
> ScreenRecordingSegmentResponse update_screen_recording_segment(storefront_oid, screen_recording_segment_oid, segment)

Update screen recording segment

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
screen_recording_segment_oid = 56 # int | 
segment = ultracart.ScreenRecordingSegment() # ScreenRecordingSegment | Segment

try:
    # Update screen recording segment
    api_response = api_instance.update_screen_recording_segment(storefront_oid, screen_recording_segment_oid, segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_screen_recording_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **screen_recording_segment_oid** | **int**|  | 
 **segment** | [**ScreenRecordingSegment**](ScreenRecordingSegment.md)| Segment | 

### Return type

[**ScreenRecordingSegmentResponse**](ScreenRecordingSegmentResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_screen_recording_settings**
> ScreenRecordingSettingsResponse update_screen_recording_settings(storefront_oid, settings)

Update screen recording settings

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
settings = ultracart.ScreenRecordingSettings() # ScreenRecordingSettings | Settings

try:
    # Update screen recording settings
    api_response = api_instance.update_screen_recording_settings(storefront_oid, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_screen_recording_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **settings** | [**ScreenRecordingSettings**](ScreenRecordingSettings.md)| Settings | 

### Return type

[**ScreenRecordingSettingsResponse**](ScreenRecordingSettingsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_screen_recording_tags**
> update_screen_recording_tags(storefront_oid, screen_recording_uuid, tags)

Update tags on a screen recording

Update tags on a screen recording 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
screen_recording_uuid = 'screen_recording_uuid_example' # str | 
tags = ultracart.ScreenRecordingTagsRequest() # ScreenRecordingTagsRequest | Tags

try:
    # Update tags on a screen recording
    api_instance.update_screen_recording_tags(storefront_oid, screen_recording_uuid, tags)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_screen_recording_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **screen_recording_uuid** | **str**|  | 
 **tags** | [**ScreenRecordingTagsRequest**](ScreenRecordingTagsRequest.md)| Tags | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction_email**
> TransactionEmailResponse update_transaction_email(storefront_oid, email_id, transaction_email)

Updates a transaction email object

Updates a transactional email 

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

storefront_oid = 56 # int | 
email_id = 'email_id_example' # str | 
transaction_email = ultracart.TransactionEmail() # TransactionEmail | TransactionEmail

try:
    # Updates a transaction email object
    api_response = api_instance.update_transaction_email(storefront_oid, email_id, transaction_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_transaction_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  | 
 **email_id** | **str**|  | 
 **transaction_email** | [**TransactionEmail**](TransactionEmail.md)| TransactionEmail | 

### Return type

[**TransactionEmailResponse**](TransactionEmailResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_twilio_account**
> TwilioResponse update_twilio_account(esp_twilio_uuid, twilio)

Update Twilio account

### Example
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint

# Create a Simple Key: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
simple_key = '109ee846ee69f50177018ab12f008a00748a25aa28dbdc0177018ab12f008a00'
api_instance = ultracart.StorefrontApi.fromApiKey(simple_key, False, True)

esp_twilio_uuid = 'esp_twilio_uuid_example' # str | 
twilio = ultracart.Twilio() # Twilio | Twilio

try:
    # Update Twilio account
    api_response = api_instance.update_twilio_account(esp_twilio_uuid, twilio)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_twilio_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **esp_twilio_uuid** | **str**|  | 
 **twilio** | [**Twilio**](Twilio.md)| Twilio | 

### Return type

[**TwilioResponse**](TwilioResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

