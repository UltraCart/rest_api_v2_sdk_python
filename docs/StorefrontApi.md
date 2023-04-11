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
[**create_email_sending_domain2**](StorefrontApi.md#create_email_sending_domain2) | **POST** /storefront/email/sending_domains | Create email sending domain for various providers
[**create_fs_directory**](StorefrontApi.md#create_fs_directory) | **POST** /storefront/{id}/fs/dir | Create file manager directory
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
[**delete_fs_file**](StorefrontApi.md#delete_fs_file) | **DELETE** /storefront/{id}/fs/file | Delete file manager directory
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
[**get_email_commseq_postcard_tracking**](StorefrontApi.md#get_email_commseq_postcard_tracking) | **GET** /storefront/{storefront_oid}/email/postcards/{commseq_postcard_uuid}/tracking | Get email communication postcard tracking
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
[**get_fs_directory**](StorefrontApi.md#get_fs_directory) | **GET** /storefront/{id}/fs/dir | Get file manager directory
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
[**get_store_fronts**](StorefrontApi.md#get_store_fronts) | **GET** /storefront | Get storefronts (internal use only for security reasons)
[**get_thumbnail_parameters**](StorefrontApi.md#get_thumbnail_parameters) | **POST** /storefront/thumbnailParameters | Get thumbnail parameters
[**get_transaction_email**](StorefrontApi.md#get_transaction_email) | **GET** /storefront/{storefront_oid}/transaction_email/list/{email_id} | Gets a transaction email object
[**get_transaction_email_list**](StorefrontApi.md#get_transaction_email_list) | **GET** /storefront/{storefront_oid}/transaction_email/list | Gets a list of transaction email names
[**get_transaction_email_screenshots**](StorefrontApi.md#get_transaction_email_screenshots) | **GET** /storefront/{storefront_oid}/transaction_email/list/{email_id}/screenshots | Get transactional email screenshots
[**get_twilio_account**](StorefrontApi.md#get_twilio_account) | **GET** /storefront/twilio/accounts/{esp_twilio_uuid} | Get Twilio account
[**get_twilio_accounts**](StorefrontApi.md#get_twilio_accounts) | **GET** /storefront/twilio/accounts | Get all Twilio accounts
[**get_upload_fs_file_url**](StorefrontApi.md#get_upload_fs_file_url) | **GET** /storefront/{id}/fs/upload_url/{extension} | Retrieves a S3 url where a file may be uploaded. Once uploaded, use uploadFsFile to trigger the server into reading the S3 bucket and retrieving the file.
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
[**send_sms_test**](StorefrontApi.md#send_sms_test) | **POST** /storefront/{storefront_oid}/email/sms/{commseq_uuid}/{commseq_step_uuid}/test | Send SMS test
[**send_webhook_test**](StorefrontApi.md#send_webhook_test) | **POST** /storefront/{storefront_oid}/email/webhooks/test | Send webhook test
[**sequence_test**](StorefrontApi.md#sequence_test) | **POST** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/test | Sequence test
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
[**update_email_sending_domain**](StorefrontApi.md#update_email_sending_domain) | **PUT** /storefront/email/sending_domains/{domain} | Update email sending domain
[**update_email_settings**](StorefrontApi.md#update_email_settings) | **POST** /storefront/{storefront_oid}/email/settings | Update email settings
[**update_experiment**](StorefrontApi.md#update_experiment) | **PUT** /storefront/{storefront_oid}/experiments/{storefront_experiment_oid} | Update experiment
[**update_library_item**](StorefrontApi.md#update_library_item) | **PUT** /storefront/code_library/{library_item_oid} | Update library item. Note that only certain fields may be updated via this method.
[**update_screen_recording_merchant_notes**](StorefrontApi.md#update_screen_recording_merchant_notes) | **POST** /storefront/{storefront_oid}/screen_recordings/{screen_recording_uuid}/merchant_notes | Update merchant notes on a screen recording
[**update_screen_recording_segment**](StorefrontApi.md#update_screen_recording_segment) | **POST** /storefront/{storefront_oid}/screen_recordings/segments/{screen_recording_segment_oid} | Update screen recording segment
[**update_screen_recording_settings**](StorefrontApi.md#update_screen_recording_settings) | **POST** /storefront/{storefront_oid}/screen_recordings/settings | Update screen recording settings
[**update_screen_recording_tags**](StorefrontApi.md#update_screen_recording_tags) | **POST** /storefront/{storefront_oid}/screen_recordings/{screen_recording_uuid}/tags | Update tags on a screen recording
[**update_transaction_email**](StorefrontApi.md#update_transaction_email) | **PUT** /storefront/{storefront_oid}/transaction_email/list/{email_id} | Updates a transaction email object
[**update_twilio_account**](StorefrontApi.md#update_twilio_account) | **PUT** /storefront/twilio/accounts/{esp_twilio_uuid} | Update Twilio account
[**upload_fs_file**](StorefrontApi.md#upload_fs_file) | **POST** /storefront/{id}/fs/upload | This is the last step in uploading a file after 1) calling getUploadFsFileUrl and 2) uploading a file to the provided url, then finally 3) calling this method and providing the key to trigger the server into reading the S3 bucket and retrieving the file.
[**validate_ruler**](StorefrontApi.md#validate_ruler) | **POST** /storefront/ruler/validate | Validate AWS Event Ruler


# **add_to_library**
> LibraryItemResponse add_to_library(add_library_request)

Add to library

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.library_item_response import LibraryItemResponse
from ultracart.model.add_library_item_request import AddLibraryItemRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    add_library_request = AddLibraryItemRequest(
        attributes=[
            LibraryItemAttribute(
                name="name_example",
                value="value_example",
            ),
        ],
        cjson="cjson_example",
        content_type="content_type_example",
        description="description_example",
        email_name="email_name_example",
        email_path="email_path_example",
        screenshots=[
            LibraryItemScreenshot(
                default_url=True,
                screenshot_url="screenshot_url_example",
            ),
        ],
        storefront_oid=1,
        title="title_example",
        upsell_offer_oid=1,
        uuid="uuid_example",
    ) # AddLibraryItemRequest | New library item request

    # example passing only required values which don't have defaults set
    try:
        # Add to library
        api_response = api_instance.add_to_library(add_library_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_to_store_front**
> ApplyLibraryItemResponse apply_to_store_front(apply_library_request)

Apply library item to storefront.

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.apply_library_item_request import ApplyLibraryItemRequest
from ultracart.model.apply_library_item_response import ApplyLibraryItemResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    apply_library_request = ApplyLibraryItemRequest(
        email_uuid="email_uuid_example",
        library_item_oid=1,
        postcard_uuid="postcard_uuid_example",
        storefront_oid=1,
    ) # ApplyLibraryItemRequest | New library item

    # example passing only required values which don't have defaults set
    try:
        # Apply library item to storefront.
        api_response = api_instance.apply_to_store_front(apply_library_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_email_list**
> EmailListArchiveResponse archive_email_list(storefront_oid, email_list_uuid)

Archive email list

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_list_archive_response import EmailListArchiveResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list_uuid = "email_list_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Archive email list
        api_response = api_instance.archive_email_list(storefront_oid, email_list_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_email_segment**
> EmailSegmentArchiveResponse archive_email_segment(storefront_oid, email_segment_uuid)

Archive email segment

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_segment_archive_response import EmailSegmentArchiveResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_segment_uuid = "email_segment_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Archive email segment
        api_response = api_instance.archive_email_segment(storefront_oid, email_segment_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **back_populate_email_flow**
> EmailFlowBackPopulateResponse back_populate_email_flow(storefront_oid, email_flow_uuid, back_populate_request)

Back populate email flow

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_flow_back_populate_response import EmailFlowBackPopulateResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_flow_back_populate_request import EmailFlowBackPopulateRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_flow_uuid = "email_flow_uuid_example" # str | 
    back_populate_request = EmailFlowBackPopulateRequest(
        order_days_old=1,
        relative_to_event=True,
    ) # EmailFlowBackPopulateRequest | The request to back populate

    # example passing only required values which don't have defaults set
    try:
        # Back populate email flow
        api_response = api_instance.back_populate_email_flow(storefront_oid, email_flow_uuid, back_populate_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_download_email_segment**
> EmailSegmentDownloadPrepareResponse check_download_email_segment(storefront_oid, email_segment_uuid, email_segment_rebuild_uuid)

Check download of email segment

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_segment_download_prepare_response import EmailSegmentDownloadPrepareResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_segment_uuid = "email_segment_uuid_example" # str | 
    email_segment_rebuild_uuid = "email_segment_rebuild_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Check download of email segment
        api_response = api_instance.check_download_email_segment(storefront_oid, email_segment_uuid, email_segment_rebuild_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_email_campaign**
> EmailCampaignResponse clone_email_campaign(storefront_oid, email_campaign_uuid)

Clone email campaign

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_campaign_response import EmailCampaignResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_campaign_uuid = "email_campaign_uuid_example" # str | 
    target_storefront_oid = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Clone email campaign
        api_response = api_instance.clone_email_campaign(storefront_oid, email_campaign_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->clone_email_campaign: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Clone email campaign
        api_response = api_instance.clone_email_campaign(storefront_oid, email_campaign_uuid, target_storefront_oid=target_storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_email_flow**
> EmailFlowResponse clone_email_flow(storefront_oid, email_flow_uuid)

Clone email flow

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_flow_response import EmailFlowResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_flow_uuid = "email_flow_uuid_example" # str | 
    target_storefront_oid = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Clone email flow
        api_response = api_instance.clone_email_flow(storefront_oid, email_flow_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->clone_email_flow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Clone email flow
        api_response = api_instance.clone_email_flow(storefront_oid, email_flow_uuid, target_storefront_oid=target_storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_email_sending_domain**
> EmailSendingDomainResponse create_email_sending_domain(domain)

Create email campaign

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_sending_domain_response import EmailSendingDomainResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    domain = "domain_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Create email campaign
        api_response = api_instance.create_email_sending_domain(domain)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_email_sending_domain2**
> EmailSendingDomainResponse create_email_sending_domain2(email_domain)

Create email sending domain for various providers

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_domain import EmailDomain
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_sending_domain_response import EmailSendingDomainResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    email_domain = EmailDomain(
        comment="comment_example",
        dkim=[
            VerificationRecord(
                name="name_example",
                type="type_example",
                value="value_example",
            ),
        ],
        dkim_status="dkim_status_example",
        domain="domain_example",
        esp_domain_uuid="esp_domain_uuid_example",
        identity_status="identity_status_example",
        mailgun=Mailgun(
            api_key="api_key_example",
        ),
        merchant_id="merchant_id_example",
        provider="provider_example",
        spf=VerificationRecord(
            name="name_example",
            type="type_example",
            value="value_example",
        ),
        start_dkim_dts="start_dkim_dts_example",
        start_identity_dts="start_identity_dts_example",
        verification=VerificationRecord(
            name="name_example",
            type="type_example",
            value="value_example",
        ),
    ) # EmailDomain | EmailDomain

    # example passing only required values which don't have defaults set
    try:
        # Create email sending domain for various providers
        api_response = api_instance.create_email_sending_domain2(email_domain)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->create_email_sending_domain2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_domain** | [**EmailDomain**](EmailDomain.md)| EmailDomain |

### Return type

[**EmailSendingDomainResponse**](EmailSendingDomainResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fs_directory**
> FileManagerPageResponse create_fs_directory(id)

Create file manager directory

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.file_manager_page_response import FileManagerPageResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    id = 1 # int | 
    name = "name_example" # str |  (optional)
    parent_storefront_fs_directory_oid = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create file manager directory
        api_response = api_instance.create_fs_directory(id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->create_fs_directory: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create file manager directory
        api_response = api_instance.create_fs_directory(id, name=name, parent_storefront_fs_directory_oid=parent_storefront_fs_directory_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->create_fs_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **name** | **str**|  | [optional]
 **parent_storefront_fs_directory_oid** | **int**|  | [optional]

### Return type

[**FileManagerPageResponse**](FileManagerPageResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_twilio_account**
> TwilioResponse create_twilio_account(twilio)

Create Twilio account

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.twilio_response import TwilioResponse
from ultracart.model.twilio import Twilio
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    twilio = Twilio(
        account_sid="account_sid_example",
        auth_token="auth_token_example",
        esp_twilio_uuid="esp_twilio_uuid_example",
        phone_numbers=[
            "phone_numbers_example",
        ],
    ) # Twilio | Twilio

    # example passing only required values which don't have defaults set
    try:
        # Create Twilio account
        api_response = api_instance.create_twilio_account(twilio)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_campaign_folder**
> BaseResponse delete_email_campaign_folder(storefront_oid, email_campaign_folder_uuid)

Delete email campaignFolder

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_campaign_folder_uuid = "email_campaign_folder_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete email campaignFolder
        api_response = api_instance.delete_email_campaign_folder(storefront_oid, email_campaign_folder_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_commseq_stat**
> delete_email_commseq_stat(storefront_oid, commseq_uuid)

Delete communication sequence stats

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete communication sequence stats
        api_instance.delete_email_commseq_stat(storefront_oid, commseq_uuid)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_email**
> BaseResponse delete_email_email(storefront_oid, commseq_email_uuid)

Delete email email

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_email_uuid = "commseq_email_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete email email
        api_response = api_instance.delete_email_email(storefront_oid, commseq_email_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_flow_folder**
> BaseResponse delete_email_flow_folder(storefront_oid, email_flow_folder_uuid)

Delete email flowFolder

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_flow_folder_uuid = "email_flow_folder_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete email flowFolder
        api_response = api_instance.delete_email_flow_folder(storefront_oid, email_flow_folder_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_list_customer**
> BaseResponse delete_email_list_customer(storefront_oid, email_list_uuid, email_customer_uuid)

Delete email list customer

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list_uuid = "email_list_uuid_example" # str | 
    email_customer_uuid = "email_customer_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete email list customer
        api_response = api_instance.delete_email_list_customer(storefront_oid, email_list_uuid, email_customer_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_list_segment_folder**
> BaseResponse delete_email_list_segment_folder(storefront_oid, email_list_segment_folder_uuid)

Delete email ListSegmentFolder

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list_segment_folder_uuid = "email_list_segment_folder_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete email ListSegmentFolder
        api_response = api_instance.delete_email_list_segment_folder(storefront_oid, email_list_segment_folder_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_postcard**
> BaseResponse delete_email_postcard(storefront_oid, commseq_postcard_uuid)

Delete email postcard

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_postcard_uuid = "commseq_postcard_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete email postcard
        api_response = api_instance.delete_email_postcard(storefront_oid, commseq_postcard_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_sending_domain**
> BaseResponse delete_email_sending_domain(domain)

delete email campaign

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    domain = "domain_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # delete email campaign
        api_response = api_instance.delete_email_sending_domain(domain)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_experiment**
> delete_experiment(storefront_oid, storefront_experiment_oid)

Delete experiment

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    storefront_experiment_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete experiment
        api_instance.delete_experiment(storefront_oid, storefront_experiment_oid)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fs_file**
> FileManagerPageResponse delete_fs_file(id)

Delete file manager directory

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.file_manager_page_response import FileManagerPageResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    id = 1 # int | 
    parent_storefront_fs_directory_oid = 1 # int |  (optional)
    storefront_fs_file_oid = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete file manager directory
        api_response = api_instance.delete_fs_file(id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->delete_fs_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete file manager directory
        api_response = api_instance.delete_fs_file(id, parent_storefront_fs_directory_oid=parent_storefront_fs_directory_oid, storefront_fs_file_oid=storefront_fs_file_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->delete_fs_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **parent_storefront_fs_directory_oid** | **int**|  | [optional]
 **storefront_fs_file_oid** | **int**|  | [optional]

### Return type

[**FileManagerPageResponse**](FileManagerPageResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_heatmap**
> delete_heatmap(storefront_oid, query)

Delete screen recording heatmap

Delete screen recording heatmap 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_heatmap_reset import ScreenRecordingHeatmapReset
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    query = ScreenRecordingHeatmapReset(
        url="url_example",
    ) # ScreenRecordingHeatmapReset | Query

    # example passing only required values which don't have defaults set
    try:
        # Delete screen recording heatmap
        api_instance.delete_heatmap(storefront_oid, query)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_item**
> delete_library_item(library_item_oid)

Delete library item

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    library_item_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete library item
        api_instance.delete_library_item(library_item_oid)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_library_item_published_versions**
> delete_library_item_published_versions(library_item_oid)

Delete all published versions for a library item, including anything in review.

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    library_item_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete all published versions for a library item, including anything in review.
        api_instance.delete_library_item_published_versions(library_item_oid)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_screen_recording_segment**
> delete_screen_recording_segment(storefront_oid, screen_recording_segment_oid)

Delete screen recording segment

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    screen_recording_segment_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Delete screen recording segment
        api_instance.delete_screen_recording_segment(storefront_oid, screen_recording_segment_oid)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_twilio_account**
> BaseResponse delete_twilio_account(esp_twilio_uuid)

delete Twilio account

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    esp_twilio_uuid = "esp_twilio_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # delete Twilio account
        api_response = api_instance.delete_twilio_account(esp_twilio_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_library_item**
> LibraryItemResponse duplicate_library_item(library_item_oid)

Duplicate library item.

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.library_item_response import LibraryItemResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    library_item_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Duplicate library item.
        api_response = api_instance.duplicate_library_item(library_item_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorite_screen_recording**
> favorite_screen_recording(storefront_oid, screen_recording_uuid)

Update favorite flag on screen recording

Update favorite flag on screen recording 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    screen_recording_uuid = "screen_recording_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update favorite flag on screen recording
        api_instance.favorite_screen_recording(storefront_oid, screen_recording_uuid)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geocode_address**
> GeocodeResponse geocode_address(storefront_oid, geocode_request)

Obtain lat/long for an address

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.geocode_response import GeocodeResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.geocode_request import GeocodeRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    geocode_request = GeocodeRequest(
        address="address_example",
        city="city_example",
        country_code="country_code_example",
        postal_code="postal_code_example",
        state="state_example",
    ) # GeocodeRequest | geocode request

    # example passing only required values which don't have defaults set
    try:
        # Obtain lat/long for an address
        api_response = api_instance.geocode_address(storefront_oid, geocode_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries**
> CountriesResponse get_countries(storefront_oid)

Get countries

Obtain a list of all the countries 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.countries_response import CountriesResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get countries
        api_response = api_instance.get_countries(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editor_token**
> EmailEditorTokenResponse get_editor_token(storefront_oid)

Gets editor token

Fetches a temporary authentication token for the editor 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_editor_token_response import EmailEditorTokenResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Gets editor token
        api_response = api_instance.get_editor_token(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_base_templates**
> EmailBaseTemplateListResponse get_email_base_templates(storefront_oid)

Get email communication base templates

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_base_template_list_response import EmailBaseTemplateListResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email communication base templates
        api_response = api_instance.get_email_base_templates(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaign**
> EmailCampaignResponse get_email_campaign(storefront_oid, email_campaign_uuid)

Get email campaign

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_campaign_response import EmailCampaignResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_campaign_uuid = "email_campaign_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email campaign
        api_response = api_instance.get_email_campaign(storefront_oid, email_campaign_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaign_folder**
> EmailCampaignFolderResponse get_email_campaign_folder(storefront_oid, email_campaign_folder_uuid)

Get email campaign folder

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_campaign_folder_response import EmailCampaignFolderResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_campaign_folder_uuid = "email_campaign_folder_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email campaign folder
        api_response = api_instance.get_email_campaign_folder(storefront_oid, email_campaign_folder_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaign_folders**
> EmailCampaignFoldersResponse get_email_campaign_folders(storefront_oid)

Get email campaign folders

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_campaign_folders_response import EmailCampaignFoldersResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email campaign folders
        api_response = api_instance.get_email_campaign_folders(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaign_screenshots**
> ScreenshotsResponse get_email_campaign_screenshots(storefront_oid, email_campaign_uuid)

Get email campaign screenshots

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screenshots_response import ScreenshotsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_campaign_uuid = "email_campaign_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email campaign screenshots
        api_response = api_instance.get_email_campaign_screenshots(storefront_oid, email_campaign_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaigns**
> EmailCampaignsResponse get_email_campaigns(storefront_oid)

Get email campaigns

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_campaigns_response import EmailCampaignsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email campaigns
        api_response = api_instance.get_email_campaigns(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaigns_with_stats**
> EmailCampaignsResponse get_email_campaigns_with_stats(storefront_oid, stat_days)

Get email campaigns with stats

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_campaigns_response import EmailCampaignsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    stat_days = "stat_days_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email campaigns with stats
        api_response = api_instance.get_email_campaigns_with_stats(storefront_oid, stat_days)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq**
> EmailCommseqResponse get_email_commseq(storefront_oid, commseq_uuid)

Get email commseq

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq_response import EmailCommseqResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email commseq
        api_response = api_instance.get_email_commseq(storefront_oid, commseq_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_email_stats**
> EmailStatSummaryResponse get_email_commseq_email_stats(storefront_oid, commseq_uuid, stats_request)

Get email communication sequence emails stats

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_stat_summary_response import EmailStatSummaryResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_stat_summary_request import EmailStatSummaryRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 
    stats_request = EmailStatSummaryRequest(
        commseq_email_uuids=[
            "commseq_email_uuids_example",
        ],
        commseq_step_uuids=[
            "commseq_step_uuids_example",
        ],
        days=1,
    ) # EmailStatSummaryRequest | StatsRequest

    # example passing only required values which don't have defaults set
    try:
        # Get email communication sequence emails stats
        api_response = api_instance.get_email_commseq_email_stats(storefront_oid, commseq_uuid, stats_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_postcard_stats**
> EmailStatPostcardSummaryResponse get_email_commseq_postcard_stats(storefront_oid, commseq_uuid, stats_request)

Get email communication sequence postcard stats

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_stat_postcard_summary_request import EmailStatPostcardSummaryRequest
from ultracart.model.email_stat_postcard_summary_response import EmailStatPostcardSummaryResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 
    stats_request = EmailStatPostcardSummaryRequest(
        commseq_postcard_uuids=[
            "commseq_postcard_uuids_example",
        ],
        days=1,
    ) # EmailStatPostcardSummaryRequest | StatsRequest

    # example passing only required values which don't have defaults set
    try:
        # Get email communication sequence postcard stats
        api_response = api_instance.get_email_commseq_postcard_stats(storefront_oid, commseq_uuid, stats_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_postcard_tracking**
> EmailPostcardTrackingResponse get_email_commseq_postcard_tracking(storefront_oid, commseq_postcard_uuid)

Get email communication postcard tracking

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_postcard_tracking_response import EmailPostcardTrackingResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_postcard_uuid = "commseq_postcard_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email communication postcard tracking
        api_response = api_instance.get_email_commseq_postcard_tracking(storefront_oid, commseq_postcard_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_email_commseq_postcard_tracking: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **commseq_postcard_uuid** | **str**|  |

### Return type

[**EmailPostcardTrackingResponse**](EmailPostcardTrackingResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_stat_overall**
> EmailCommseqStatResponse get_email_commseq_stat_overall(storefront_oid, commseq_uuid)

Get communication sequence stats overall

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseq_stat_response import EmailCommseqStatResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get communication sequence stats overall
        api_response = api_instance.get_email_commseq_stat_overall(storefront_oid, commseq_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_step_stats**
> EmailStepStatResponse get_email_commseq_step_stats(storefront_oid, commseq_uuid, stats_request)

Get email communication sequence step stats

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_step_stat_response import EmailStepStatResponse
from ultracart.model.email_step_stat_request import EmailStepStatRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 
    stats_request = EmailStepStatRequest(
        commseq_step_uuids=[
            "commseq_step_uuids_example",
        ],
        days=1,
    ) # EmailStepStatRequest | StatsRequest

    # example passing only required values which don't have defaults set
    try:
        # Get email communication sequence step stats
        api_response = api_instance.get_email_commseq_step_stats(storefront_oid, commseq_uuid, stats_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_step_waiting**
> EmailStepWaitingResponse get_email_commseq_step_waiting(storefront_oid, commseq_uuid, waiting_request)

Get email communication sequence customers waiting at each requested step

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_step_waiting_request import EmailStepWaitingRequest
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_step_waiting_response import EmailStepWaitingResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 
    waiting_request = EmailStepWaitingRequest(
        commseq_step_uuids=[
            "commseq_step_uuids_example",
        ],
    ) # EmailStepWaitingRequest | WaitingRequest

    # example passing only required values which don't have defaults set
    try:
        # Get email communication sequence customers waiting at each requested step
        api_response = api_instance.get_email_commseq_step_waiting(storefront_oid, commseq_uuid, waiting_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_webhook_editor_values**
> EmailWebhookEditorValuesResponse get_email_commseq_webhook_editor_values(storefront_oid, commseq_uuid)

Get email webhook editor values

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_webhook_editor_values_response import EmailWebhookEditorValuesResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email webhook editor values
        api_response = api_instance.get_email_commseq_webhook_editor_values(storefront_oid, commseq_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseqs**
> EmailCommseqsResponse get_email_commseqs(storefront_oid)

Get email commseqs

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseqs_response import EmailCommseqsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email commseqs
        api_response = api_instance.get_email_commseqs(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_customer_editor_url**
> EmailCustomerEditorUrlResponse get_email_customer_editor_url(storefront_oid, email_customer_uuid)

Get customers editor URL

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_customer_editor_url_response import EmailCustomerEditorUrlResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_customer_uuid = "email_customer_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get customers editor URL
        api_response = api_instance.get_email_customer_editor_url(storefront_oid, email_customer_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_customers**
> EmailCustomersResponse get_email_customers(storefront_oid)

Get email customers

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_customers_response import EmailCustomersResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    page_number = 1 # int |  (optional)
    page_size = 1 # int |  (optional)
    search_email_prefix = "searchEmailPrefix_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get email customers
        api_response = api_instance.get_email_customers(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_email_customers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get email customers
        api_response = api_instance.get_email_customers(storefront_oid, page_number=page_number, page_size=page_size, search_email_prefix=search_email_prefix)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_dashboard_activity**
> EmailDashboardActivityResponse get_email_dashboard_activity(storefront_oid)

Get email dashboard activity

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_dashboard_activity_response import EmailDashboardActivityResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    last_records = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get email dashboard activity
        api_response = api_instance.get_email_dashboard_activity(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_email_dashboard_activity: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get email dashboard activity
        api_response = api_instance.get_email_dashboard_activity(storefront_oid, last_records=last_records)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_dashboard_stats**
> EmailDashboardStatsResponse get_email_dashboard_stats(storefront_oid)

Get dashboard stats

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_dashboard_stats_response import EmailDashboardStatsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    days = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get dashboard stats
        api_response = api_instance.get_email_dashboard_stats(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_email_dashboard_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get dashboard stats
        api_response = api_instance.get_email_dashboard_stats(storefront_oid, days=days)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_dispatch_logs**
> EmailCommseqStepLogsResponse get_email_dispatch_logs(storefront_oid, commseq_uuid, commseq_step_uuid)

Get email dispatch logs

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq_step_logs_response import EmailCommseqStepLogsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 
    commseq_step_uuid = "commseq_step_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email dispatch logs
        api_response = api_instance.get_email_dispatch_logs(storefront_oid, commseq_uuid, commseq_step_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_email**
> EmailCommseqEmailResponse get_email_email(storefront_oid, commseq_email_uuid)

Get email email

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseq_email_response import EmailCommseqEmailResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_email_uuid = "commseq_email_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email email
        api_response = api_instance.get_email_email(storefront_oid, commseq_email_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_email_clicks**
> EmailClicksResponse get_email_email_clicks(storefront_oid, commseq_uuid, commseq_step_uuid, commseq_email_uuid)

Get email email clicks

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_clicks_response import EmailClicksResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 
    commseq_step_uuid = "commseq_step_uuid_example" # str | 
    commseq_email_uuid = "commseq_email_uuid_example" # str | 
    days = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get email email clicks
        api_response = api_instance.get_email_email_clicks(storefront_oid, commseq_uuid, commseq_step_uuid, commseq_email_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_email_email_clicks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get email email clicks
        api_response = api_instance.get_email_email_clicks(storefront_oid, commseq_uuid, commseq_step_uuid, commseq_email_uuid, days=days)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_email_customer_editor_url**
> EmailCustomerEditorUrlResponse get_email_email_customer_editor_url(storefront_oid, commseq_email_uuid, order_id)

Get email order customer editor url

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_customer_editor_url_response import EmailCustomerEditorUrlResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_email_uuid = "commseq_email_uuid_example" # str | 
    order_id = "order_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email order customer editor url
        api_response = api_instance.get_email_email_customer_editor_url(storefront_oid, commseq_email_uuid, order_id)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_email_orders**
> EmailOrdersResponse get_email_email_orders(storefront_oid, commseq_uuid, commseq_step_uuid, commseq_email_uuid)

Get email email orders

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_orders_response import EmailOrdersResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 
    commseq_step_uuid = "commseq_step_uuid_example" # str | 
    commseq_email_uuid = "commseq_email_uuid_example" # str | 
    days = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get email email orders
        api_response = api_instance.get_email_email_orders(storefront_oid, commseq_uuid, commseq_step_uuid, commseq_email_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_email_email_orders: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get email email orders
        api_response = api_instance.get_email_email_orders(storefront_oid, commseq_uuid, commseq_step_uuid, commseq_email_uuid, days=days)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_emails**
> EmailCommseqEmailsResponse get_email_emails(storefront_oid)

Get email emails

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq_emails_response import EmailCommseqEmailsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email emails
        api_response = api_instance.get_email_emails(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_emails_multiple**
> EmailCommseqEmailsResponse get_email_emails_multiple(storefront_oid, email_commseq_emails_request)

Get email emails multiple

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq_emails_request import EmailCommseqEmailsRequest
from ultracart.model.email_commseq_emails_response import EmailCommseqEmailsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_commseq_emails_request = EmailCommseqEmailsRequest(
        error=Error(
            developer_message="developer_message_example",
            error_code="error_code_example",
            more_info="more_info_example",
            object_id="object_id_example",
            user_message="user_message_example",
        ),
        esp_commseq_email_uuids=[
            "esp_commseq_email_uuids_example",
        ],
        metadata=ResponseMetadata(
            payload_name="payload_name_example",
            result_set=ResultSet(
                count=1,
                limit=1,
                more=True,
                next_offset=1,
                offset=1,
                total_records=1,
            ),
        ),
        success=True,
        warning=Warning(
            more_info="more_info_example",
            warning_message="warning_message_example",
        ),
    ) # EmailCommseqEmailsRequest | Request of email uuids

    # example passing only required values which don't have defaults set
    try:
        # Get email emails multiple
        api_response = api_instance.get_email_emails_multiple(storefront_oid, email_commseq_emails_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_flow**
> EmailFlowResponse get_email_flow(storefront_oid, email_flow_uuid)

Get email flow

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_flow_response import EmailFlowResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_flow_uuid = "email_flow_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email flow
        api_response = api_instance.get_email_flow(storefront_oid, email_flow_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_flow_folder**
> EmailFlowFolderResponse get_email_flow_folder(storefront_oid, email_flow_folder_uuid)

Get email flow folder

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_flow_folder_response import EmailFlowFolderResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_flow_folder_uuid = "email_flow_folder_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email flow folder
        api_response = api_instance.get_email_flow_folder(storefront_oid, email_flow_folder_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_flow_folders**
> EmailFlowFoldersResponse get_email_flow_folders(storefront_oid)

Get email flow folders

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_flow_folders_response import EmailFlowFoldersResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email flow folders
        api_response = api_instance.get_email_flow_folders(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_flow_screenshots**
> ScreenshotsResponse get_email_flow_screenshots(storefront_oid, email_flow_uuid)

Get email flow screenshots

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screenshots_response import ScreenshotsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_flow_uuid = "email_flow_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email flow screenshots
        api_response = api_instance.get_email_flow_screenshots(storefront_oid, email_flow_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_flows**
> EmailFlowsResponse get_email_flows(storefront_oid)

Get email flows

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_flows_response import EmailFlowsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email flows
        api_response = api_instance.get_email_flows(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_global_settings**
> EmailGlobalSettingsResponse get_email_global_settings()

Get email globalsettings

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_global_settings_response import EmailGlobalSettingsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get email globalsettings
        api_response = api_instance.get_email_global_settings()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_email_global_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**EmailGlobalSettingsResponse**](EmailGlobalSettingsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list**
> EmailListResponse get_email_list(storefront_oid, email_list_uuid)

Get email list

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_list_response import EmailListResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list_uuid = "email_list_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email list
        api_response = api_instance.get_email_list(storefront_oid, email_list_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list_customer_editor_url**
> EmailCustomerEditorUrlResponse get_email_list_customer_editor_url(storefront_oid, email_list_uuid, email_customer_uuid)

Get email list customer editor url

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_customer_editor_url_response import EmailCustomerEditorUrlResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list_uuid = "email_list_uuid_example" # str | 
    email_customer_uuid = "email_customer_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email list customer editor url
        api_response = api_instance.get_email_list_customer_editor_url(storefront_oid, email_list_uuid, email_customer_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list_customers**
> EmailListCustomersResponse get_email_list_customers(storefront_oid, email_list_uuid)

Get email list customers

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_list_customers_response import EmailListCustomersResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list_uuid = "email_list_uuid_example" # str | 
    page_number = 1 # int |  (optional)
    page_size = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get email list customers
        api_response = api_instance.get_email_list_customers(storefront_oid, email_list_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_email_list_customers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get email list customers
        api_response = api_instance.get_email_list_customers(storefront_oid, email_list_uuid, page_number=page_number, page_size=page_size)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list_segment_folder**
> EmailListSegmentFolderResponse get_email_list_segment_folder(storefront_oid, email_list_segment_folder_uuid)

Get email campaign folder

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_list_segment_folder_response import EmailListSegmentFolderResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list_segment_folder_uuid = "email_list_segment_folder_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email campaign folder
        api_response = api_instance.get_email_list_segment_folder(storefront_oid, email_list_segment_folder_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list_segment_folders**
> EmailListSegmentFoldersResponse get_email_list_segment_folders(storefront_oid)

Get email campaign folders

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_list_segment_folders_response import EmailListSegmentFoldersResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email campaign folders
        api_response = api_instance.get_email_list_segment_folders(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_lists**
> EmailListsResponse get_email_lists(storefront_oid)

Get email lists

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_lists_response import EmailListsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email lists
        api_response = api_instance.get_email_lists(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_performance**
> EmailPerformanceResponse get_email_performance(storefront_oid)

Get email performance

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_performance_response import EmailPerformanceResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email performance
        api_response = api_instance.get_email_performance(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_plan**
> EmailPlanResponse get_email_plan(storefront_oid)

Get email plan

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_plan_response import EmailPlanResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email plan
        api_response = api_instance.get_email_plan(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_postcard**
> EmailCommseqPostcardResponse get_email_postcard(storefront_oid, commseq_postcard_uuid)

Get email postcard

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq_postcard_response import EmailCommseqPostcardResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_postcard_uuid = "commseq_postcard_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email postcard
        api_response = api_instance.get_email_postcard(storefront_oid, commseq_postcard_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_postcards**
> EmailCommseqPostcardsResponse get_email_postcards(storefront_oid)

Get email postcards

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseq_postcards_response import EmailCommseqPostcardsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email postcards
        api_response = api_instance.get_email_postcards(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_postcards_multiple**
> EmailCommseqPostcardsResponse get_email_postcards_multiple(storefront_oid, email_commseq_postcards_request)

Get email postcards multiple

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseq_postcards_response import EmailCommseqPostcardsResponse
from ultracart.model.email_commseq_postcards_request import EmailCommseqPostcardsRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_commseq_postcards_request = EmailCommseqPostcardsRequest(
        esp_commseq_postcard_uuids=[
            "esp_commseq_postcard_uuids_example",
        ],
    ) # EmailCommseqPostcardsRequest | Request of postcard uuids

    # example passing only required values which don't have defaults set
    try:
        # Get email postcards multiple
        api_response = api_instance.get_email_postcards_multiple(storefront_oid, email_commseq_postcards_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_segment**
> EmailSegmentResponse get_email_segment(storefront_oid, email_segment_uuid)

Get email segment

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_segment_response import EmailSegmentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_segment_uuid = "email_segment_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email segment
        api_response = api_instance.get_email_segment(storefront_oid, email_segment_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_segment_customer_editor_url**
> EmailCustomerEditorUrlResponse get_email_segment_customer_editor_url(storefront_oid, email_segment_uuid, email_customer_uuid)

Get email segment customers editor URL

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_customer_editor_url_response import EmailCustomerEditorUrlResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_segment_uuid = "email_segment_uuid_example" # str | 
    email_customer_uuid = "email_customer_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email segment customers editor URL
        api_response = api_instance.get_email_segment_customer_editor_url(storefront_oid, email_segment_uuid, email_customer_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_segment_customers**
> EmailSegmentCustomersResponse get_email_segment_customers(storefront_oid, email_segment_uuid)

Get email segment customers

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_segment_customers_response import EmailSegmentCustomersResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_segment_uuid = "email_segment_uuid_example" # str | 
    page_number = 1 # int |  (optional)
    page_size = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get email segment customers
        api_response = api_instance.get_email_segment_customers(storefront_oid, email_segment_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_email_segment_customers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get email segment customers
        api_response = api_instance.get_email_segment_customers(storefront_oid, email_segment_uuid, page_number=page_number, page_size=page_size)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_segments**
> EmailSegmentsResponse get_email_segments(storefront_oid)

Get email segments

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_segments_response import EmailSegmentsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email segments
        api_response = api_instance.get_email_segments(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_sending_domain**
> EmailSendingDomainResponse get_email_sending_domain(domain)

Get email sending domain

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_sending_domain_response import EmailSendingDomainResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    domain = "domain_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email sending domain
        api_response = api_instance.get_email_sending_domain(domain)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_sending_domain_status**
> EmailSendingDomainResponse get_email_sending_domain_status(domain)

Get email sending domain status

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_sending_domain_response import EmailSendingDomainResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    domain = "domain_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get email sending domain status
        api_response = api_instance.get_email_sending_domain_status(domain)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_sending_domains**
> EmailSendingDomainsResponse get_email_sending_domains()

Get email sending domains

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_sending_domains_response import EmailSendingDomainsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get email sending domains
        api_response = api_instance.get_email_sending_domains()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_email_sending_domains: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**EmailSendingDomainsResponse**](EmailSendingDomainsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_settings**
> EmailSettingsResponse get_email_settings(storefront_oid)

Get email settings

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_settings_response import EmailSettingsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email settings
        api_response = api_instance.get_email_settings(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_template**
> EmailTemplate get_email_template(storefront_oid, email_template_oid)

Get email template

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_template import EmailTemplate
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_template_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get email template
        api_response = api_instance.get_email_template(storefront_oid, email_template_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_templates**
> EmailTemplatesResponse get_email_templates(storefront_oid)

Get email templates

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_templates_response import EmailTemplatesResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    trigger_type = "trigger_type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get email templates
        api_response = api_instance.get_email_templates(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_email_templates: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get email templates
        api_response = api_instance.get_email_templates(storefront_oid, trigger_type=trigger_type)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_third_party_providers**
> EmailThirdPartyProvidersResponse get_email_third_party_providers(storefront_oid)

Get a list of third party email providers

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_third_party_providers_response import EmailThirdPartyProvidersResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get a list of third party email providers
        api_response = api_instance.get_email_third_party_providers(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiments**
> ExperimentsResponse get_experiments(storefront_oid)

Get experiments

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.experiments_response import ExperimentsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get experiments
        api_response = api_instance.get_experiments(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fs_directory**
> FileManagerPageResponse get_fs_directory(id)

Get file manager directory

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.file_manager_page_response import FileManagerPageResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    id = 1 # int | 
    path = "path_example" # str |  (optional)
    storefront_fs_directory_oid = 1 # int |  (optional)
    storefront_theme_oid = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get file manager directory
        api_response = api_instance.get_fs_directory(id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_fs_directory: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get file manager directory
        api_response = api_instance.get_fs_directory(id, path=path, storefront_fs_directory_oid=storefront_fs_directory_oid, storefront_theme_oid=storefront_theme_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_fs_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **path** | **str**|  | [optional]
 **storefront_fs_directory_oid** | **int**|  | [optional]
 **storefront_theme_oid** | **int**|  | [optional]

### Return type

[**FileManagerPageResponse**](FileManagerPageResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heatmap**
> ScreenRecordingHeatmapResponse get_heatmap(storefront_oid, query)

Get screen recording heatmap

Get screen recording heatmap 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_heatmap_response import ScreenRecordingHeatmapResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.screen_recording_heatmap_request import ScreenRecordingHeatmapRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    query = ScreenRecordingHeatmapRequest(
        range=ScreenRecordingFilterRangeDate(
            end="end_example",
            start="start_example",
        ),
        screen_sizes=[
            "screen_sizes_example",
        ],
        url="url_example",
    ) # ScreenRecordingHeatmapRequest | Query

    # example passing only required values which don't have defaults set
    try:
        # Get screen recording heatmap
        api_response = api_instance.get_heatmap(storefront_oid, query)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heatmap_index**
> ScreenRecordingHeatmapIndexResponse get_heatmap_index(storefront_oid, query)

Get screen recording heatmap index

Get screen recording heatmap index 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.screen_recording_heatmap_index_response import ScreenRecordingHeatmapIndexResponse
from ultracart.model.screen_recording_heatmap_index_request import ScreenRecordingHeatmapIndexRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    query = ScreenRecordingHeatmapIndexRequest(
        url_contains="url_contains_example",
    ) # ScreenRecordingHeatmapIndexRequest | Query
    limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 500) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get screen recording heatmap index
        api_response = api_instance.get_heatmap_index(storefront_oid, query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_heatmap_index: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get screen recording heatmap index
        api_response = api_instance.get_heatmap_index(storefront_oid, query, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_heatmap_index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **query** | [**ScreenRecordingHeatmapIndexRequest**](ScreenRecordingHeatmapIndexRequest.md)| Query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 500) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]

### Return type

[**ScreenRecordingHeatmapIndexResponse**](ScreenRecordingHeatmapIndexResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_histogram_property_names**
> EmailHistogramPropertyNamesResponse get_histogram_property_names(storefront_oid)

Get histogram property names

Obtain a list of property names for a given property type 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_histogram_property_names_response import EmailHistogramPropertyNamesResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    property_type = "property_type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get histogram property names
        api_response = api_instance.get_histogram_property_names(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_histogram_property_names: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get histogram property names
        api_response = api_instance.get_histogram_property_names(storefront_oid, property_type=property_type)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_histogram_property_values**
> EmailHistogramPropertyValuesResponse get_histogram_property_values(storefront_oid)

Get histogram property values

Obtain a list of property values for a given property name and type 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_histogram_property_values_response import EmailHistogramPropertyValuesResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    property_name = "property_name_example" # str |  (optional)
    property_type = "property_type_example" # str |  (optional)
    limit = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get histogram property values
        api_response = api_instance.get_histogram_property_values(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_histogram_property_values: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get histogram property values
        api_response = api_instance.get_histogram_property_values(storefront_oid, property_name=property_name, property_type=property_type, limit=limit)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_filter_values**
> LibraryFilterValuesResponse get_library_filter_values()

Get library values used to populate drop down boxes for filtering.

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.library_filter_values_response import LibraryFilterValuesResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get library values used to populate drop down boxes for filtering.
        api_response = api_instance.get_library_filter_values()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_library_filter_values: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LibraryFilterValuesResponse**](LibraryFilterValuesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_item**
> LibraryItemResponse get_library_item(library_item_oid)

Get library item.

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.library_item_response import LibraryItemResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    library_item_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get library item.
        api_response = api_instance.get_library_item(library_item_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_library_item_published_versions**
> LibraryItemsResponse get_library_item_published_versions(library_item_oid)

Get all published versions for a library item.

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.library_items_response import LibraryItemsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    library_item_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get all published versions for a library item.
        api_response = api_instance.get_library_item_published_versions(library_item_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recording**
> ScreenRecordingResponse get_screen_recording(storefront_oid, screen_recording_uuid)

Get screen recording

Get screen recording 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_response import ScreenRecordingResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    screen_recording_uuid = "screen_recording_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get screen recording
        api_response = api_instance.get_screen_recording(storefront_oid, screen_recording_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recording_page_view_data**
> ScreenRecordingPageViewDataResponse get_screen_recording_page_view_data(storefront_oid, screen_recording_uuid, screen_recording_page_view_uuid)

Get screen recording page view data

Get screen recording page view data 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_page_view_data_response import ScreenRecordingPageViewDataResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    screen_recording_uuid = "screen_recording_uuid_example" # str | 
    screen_recording_page_view_uuid = "screen_recording_page_view_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get screen recording page view data
        api_response = api_instance.get_screen_recording_page_view_data(storefront_oid, screen_recording_uuid, screen_recording_page_view_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recording_segment**
> ScreenRecordingSegmentResponse get_screen_recording_segment(storefront_oid, screen_recording_segment_oid)

Get screen recording segment

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.screen_recording_segment_response import ScreenRecordingSegmentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    screen_recording_segment_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get screen recording segment
        api_response = api_instance.get_screen_recording_segment(storefront_oid, screen_recording_segment_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recording_segments**
> ScreenRecordingSegmentsResponse get_screen_recording_segments(storefront_oid)

Get screen recording segments

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_segments_response import ScreenRecordingSegmentsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get screen recording segments
        api_response = api_instance.get_screen_recording_segments(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recording_settings**
> ScreenRecordingSettingsResponse get_screen_recording_settings(storefront_oid)

Get screen recording settings

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_settings_response import ScreenRecordingSettingsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get screen recording settings
        api_response = api_instance.get_screen_recording_settings(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recording_tags**
> ScreenRecordingTagsResponse get_screen_recording_tags(storefront_oid)

Get tags used by screen recording

Get tags used by screen recording 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_tags_response import ScreenRecordingTagsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get tags used by screen recording
        api_response = api_instance.get_screen_recording_tags(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recordings_by_query**
> ScreenRecordingQueryResponse get_screen_recordings_by_query(storefront_oid, query)

Query screen recordings

Query screen recordings 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_query_response import ScreenRecordingQueryResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.screen_recording_query_request import ScreenRecordingQueryRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    query = ScreenRecordingQueryRequest(
        filter=ScreenRecordingFilter(
            affiliate_email="affiliate_email_example",
            affiliate_id=1,
            communications_campaign_name="communications_campaign_name_example",
            communications_campaign_name_filter=True,
            communications_email_subject="communications_email_subject_example",
            communications_email_subject_filter=True,
            communications_flow_name="communications_flow_name_example",
            communications_flow_name_filter=True,
            email=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            email_domain="email_domain_example",
            email_domain_filter=True,
            email_identified=True,
            end_timestamp=ScreenRecordingFilterRangeDate(
                end="end_example",
                start="start_example",
            ),
            esp_customer_uuid="esp_customer_uuid_example",
            favorite=True,
            geolocation=ScreenRecordingFilterGeoDistance(
                distance=1,
                distance_uom="distance_uom_example",
                from_address="from_address_example",
                lat=3.14,
                lon=3.14,
            ),
            geolocation_country=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            geolocation_country_filter=True,
            geolocation_state=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            geolocation_state_filter=True,
            language_iso_code=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            language_iso_code_filter=True,
            last_x_days=1,
            max_filter_values=1,
            order_id=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            page_view_count=ScreenRecordingFilterRangeInteger(
                eq=1,
                gt=1,
                gte=1,
                lt=1,
                lte=1,
            ),
            page_views=[
                ScreenRecordingFilterPageView(
                    domain=ScreenRecordingFilterStringSearch(
                        does_not_exist=True,
                        exists=True,
                        _is="_is_example",
                        is_not="is_not_example",
                        starts_with="starts_with_example",
                    ),
                    domain_filter=True,
                    event_name_filter=True,
                    event_param_name_filter=True,
                    event_param_value_filter=True,
                    events=[
                        ScreenRecordingFilterPageViewEvent(
                            event_name="event_name_example",
                            event_params=[
                                ScreenRecordingFilterPageViewEventParam(
                                    name="name_example",
                                    value_bd=ScreenRecordingFilterRangeBigDecimal(
                                        eq=3.14,
                                        gt=3.14,
                                        gte=3.14,
                                        lt=3.14,
                                        lte=3.14,
                                    ),
                                    value_bool=True,
                                    value_num=ScreenRecordingFilterRangeInteger(
                                        eq=1,
                                        gt=1,
                                        gte=1,
                                        lt=1,
                                        lte=1,
                                    ),
                                    value_text=ScreenRecordingFilterStringSearch(
                                        does_not_exist=True,
                                        exists=True,
                                        _is="_is_example",
                                        is_not="is_not_example",
                                        starts_with="starts_with_example",
                                    ),
                                ),
                            ],
                        ),
                    ],
                    param_name_filter=True,
                    param_value_filter=True,
                    params=[
                        ScreenRecordingFilterPageViewParam(
                            name="name_example",
                            value=ScreenRecordingFilterStringSearch(
                                does_not_exist=True,
                                exists=True,
                                _is="_is_example",
                                is_not="is_not_example",
                                starts_with="starts_with_example",
                            ),
                        ),
                    ],
                    referrer=ScreenRecordingFilterStringSearch(
                        does_not_exist=True,
                        exists=True,
                        _is="_is_example",
                        is_not="is_not_example",
                        starts_with="starts_with_example",
                    ),
                    referrer_params=[
                        ScreenRecordingFilterPageViewReferrerParam(
                            name="name_example",
                            value=ScreenRecordingFilterStringSearch(
                                does_not_exist=True,
                                exists=True,
                                _is="_is_example",
                                is_not="is_not_example",
                                starts_with="starts_with_example",
                            ),
                        ),
                    ],
                    referrer_raw=ScreenRecordingFilterStringSearch(
                        does_not_exist=True,
                        exists=True,
                        _is="_is_example",
                        is_not="is_not_example",
                        starts_with="starts_with_example",
                    ),
                    time_on_page=ScreenRecordingFilterRangeInteger(
                        eq=1,
                        gt=1,
                        gte=1,
                        lt=1,
                        lte=1,
                    ),
                    time_on_page_max_filter=True,
                    time_on_page_min_filter=True,
                    url=ScreenRecordingFilterStringSearch(
                        does_not_exist=True,
                        exists=True,
                        _is="_is_example",
                        is_not="is_not_example",
                        starts_with="starts_with_example",
                    ),
                    url_filter=True,
                ),
            ],
            placed_order=True,
            preferred_language=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            preferred_language_filter=True,
            referrer_domain="referrer_domain_example",
            referrer_domain_filter=True,
            screen_recording_uuids=[
                "screen_recording_uuids_example",
            ],
            screen_sizes=[
                "screen_sizes_example",
            ],
            skip_filter_values=True,
            skip_histogram=True,
            skip_hits=True,
            start_timestamp=ScreenRecordingFilterRangeDate(
                end="end_example",
                start="start_example",
            ),
            tags=[
                "tags_example",
            ],
            time_on_site=ScreenRecordingFilterRangeInteger(
                eq=1,
                gt=1,
                gte=1,
                lt=1,
                lte=1,
            ),
            time_on_site_max_filter=True,
            time_on_site_min_filter=True,
            url_filter=True,
            user_agent_device_name="user_agent_device_name_example",
            user_agent_device_name_filter=True,
            user_agent_device_os_name_filter=True,
            user_agent_device_os_version_filter=True,
            user_agent_name="user_agent_name_example",
            user_agent_name_filter=True,
            user_agent_original=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            user_agent_original_filter=True,
            user_agent_os_name="user_agent_os_name_example",
            user_agent_os_version="user_agent_os_version_example",
            user_ip=ScreenRecordingFilterIpSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
            ),
            utm_campaign="utm_campaign_example",
            utm_campaign_filter=True,
            utm_source="utm_source_example",
            utm_source_filter=True,
            visitor_number=1,
            watched=True,
        ),
    ) # ScreenRecordingQueryRequest | Query
    limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 500) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Query screen recordings
        api_response = api_instance.get_screen_recordings_by_query(storefront_oid, query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_screen_recordings_by_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query screen recordings
        api_response = api_instance.get_screen_recordings_by_query(storefront_oid, query, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_screen_recordings_by_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **query** | [**ScreenRecordingQueryRequest**](ScreenRecordingQueryRequest.md)| Query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 500) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]

### Return type

[**ScreenRecordingQueryResponse**](ScreenRecordingQueryResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screen_recordings_by_segment**
> ScreenRecordingQueryResponse get_screen_recordings_by_segment(storefront_oid, screen_recording_segment_oid)

Get screen recordings by segment

Get screen recordings by segment 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_query_response import ScreenRecordingQueryResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    screen_recording_segment_oid = 1 # int | 
    limit = 100 # int | The maximum number of records to return on this one API call. (Default 100, Max 500) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get screen recordings by segment
        api_response = api_instance.get_screen_recordings_by_segment(storefront_oid, screen_recording_segment_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_screen_recordings_by_segment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get screen recordings by segment
        api_response = api_instance.get_screen_recordings_by_segment(storefront_oid, screen_recording_segment_oid, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_screen_recordings_by_segment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **screen_recording_segment_oid** | **int**|  |
 **limit** | **int**| The maximum number of records to return on this one API call. (Default 100, Max 500) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]

### Return type

[**ScreenRecordingQueryResponse**](ScreenRecordingQueryResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store_front_pricing_tiers**
> PricingTiersResponse get_store_front_pricing_tiers()

Retrieve pricing tiers

Retrieves the pricing tiers 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.pricing_tiers_response import PricingTiersResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve pricing tiers
        api_response = api_instance.get_store_front_pricing_tiers(expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store_fronts**
> StoreFrontsResponse get_store_fronts()

Get storefronts (internal use only for security reasons)

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.store_fronts_response import StoreFrontsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get storefronts (internal use only for security reasons)
        api_response = api_instance.get_store_fronts()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_store_fronts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**StoreFrontsResponse**](StoreFrontsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnail_parameters**
> ThumbnailParametersResponse get_thumbnail_parameters(thumbnail_parameters)

Get thumbnail parameters

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.thumbnail_parameters_response import ThumbnailParametersResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.thumbnail_parameters_request import ThumbnailParametersRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    thumbnail_parameters = ThumbnailParametersRequest(
        height=1,
        png_format=True,
        square_thumbnail=True,
        webp=True,
        width=1,
    ) # ThumbnailParametersRequest | Thumbnail Parameters

    # example passing only required values which don't have defaults set
    try:
        # Get thumbnail parameters
        api_response = api_instance.get_thumbnail_parameters(thumbnail_parameters)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_email**
> TransactionEmailResponse get_transaction_email(storefront_oid, email_id)

Gets a transaction email object

Fetch a transactional email 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.transaction_email_response import TransactionEmailResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_id = "email_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets a transaction email object
        api_response = api_instance.get_transaction_email(storefront_oid, email_id)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_email_list**
> TransactionEmailListResponse get_transaction_email_list(storefront_oid)

Gets a list of transaction email names

Obtain a list of all transactional emails and return back just their names 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.transaction_email_list_response import TransactionEmailListResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of transaction email names
        api_response = api_instance.get_transaction_email_list(storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_email_screenshots**
> ScreenshotsResponse get_transaction_email_screenshots(storefront_oid, email_id)

Get transactional email screenshots

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screenshots_response import ScreenshotsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_id = "email_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get transactional email screenshots
        api_response = api_instance.get_transaction_email_screenshots(storefront_oid, email_id)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_twilio_account**
> TwilioResponse get_twilio_account(esp_twilio_uuid)

Get Twilio account

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.twilio_response import TwilioResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    esp_twilio_uuid = "esp_twilio_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Twilio account
        api_response = api_instance.get_twilio_account(esp_twilio_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_twilio_accounts**
> TwiliosResponse get_twilio_accounts()

Get all Twilio accounts

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.twilios_response import TwiliosResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get all Twilio accounts
        api_response = api_instance.get_twilio_accounts()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_twilio_accounts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TwiliosResponse**](TwiliosResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_fs_file_url**
> FileManagerUploadUrlResponse get_upload_fs_file_url(id, extension)

Retrieves a S3 url where a file may be uploaded. Once uploaded, use uploadFsFile to trigger the server into reading the S3 bucket and retrieving the file.

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.file_manager_upload_url_response import FileManagerUploadUrlResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    id = 1 # int | 
    extension = "extension_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieves a S3 url where a file may be uploaded. Once uploaded, use uploadFsFile to trigger the server into reading the S3 bucket and retrieving the file.
        api_response = api_instance.get_upload_fs_file_url(id, extension)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->get_upload_fs_file_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **extension** | **str**|  |

### Return type

[**FileManagerUploadUrlResponse**](FileManagerUploadUrlResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_unsubscribe**
> EmailGlobalUnsubscribeResponse global_unsubscribe(storefront_oid, unsubscribe)

Globally unsubscribe a customer

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_global_unsubscribe_request import EmailGlobalUnsubscribeRequest
from ultracart.model.email_global_unsubscribe_response import EmailGlobalUnsubscribeResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    unsubscribe = EmailGlobalUnsubscribeRequest(
        email="email_example",
    ) # EmailGlobalUnsubscribeRequest | Unsubscribe

    # example passing only required values which don't have defaults set
    try:
        # Globally unsubscribe a customer
        api_response = api_instance.global_unsubscribe(storefront_oid, unsubscribe)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_email_third_party_provider_list**
> import_email_third_party_provider_list(storefront_oid, import_request)

Import a third party provider list

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_third_party_list_import_request import EmailThirdPartyListImportRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    import_request = EmailThirdPartyListImportRequest(
        providers=[
            EmailThirdPartyProvider(
                connect_url="connect_url_example",
                list_count=1,
                lists=[
                    EmailThirdPartyList(
                        id="id_example",
                        name="name_example",
                    ),
                ],
                logo_url="logo_url_example",
                name="name_example",
                supports_add_tags=True,
                supports_list_subscribe=True,
                supports_list_unsubscribe=True,
                supports_remove_tags=True,
                tag_count=1,
                tags=[
                    EmailThirdPartyTag(
                        id="id_example",
                        name="name_example",
                    ),
                ],
            ),
        ],
    ) # EmailThirdPartyListImportRequest | lists to import

    # example passing only required values which don't have defaults set
    try:
        # Import a third party provider list
        api_instance.import_email_third_party_provider_list(storefront_oid, import_request)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_campaign**
> EmailCampaignResponse insert_email_campaign(storefront_oid, email_campaign)

Insert email campaign

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_campaign_response import EmailCampaignResponse
from ultracart.model.email_campaign import EmailCampaign
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_campaign = EmailCampaign(
        click_rate_formatted="click_rate_formatted_example",
        created_dts="created_dts_example",
        deleted=True,
        email_campaign_uuid="email_campaign_uuid_example",
        email_communication_sequence_uuid="email_communication_sequence_uuid_example",
        end_once_customer_purchases=True,
        end_once_customer_purchases_anywhere=True,
        esp_campaign_folder_uuid="esp_campaign_folder_uuid_example",
        esp_domain_user="esp_domain_user_example",
        esp_domain_uuid="esp_domain_uuid_example",
        esp_friendly_name="esp_friendly_name_example",
        library_item_oid=1,
        memberships=[
            EmailListSegmentMembership(
                email_list_uuid="email_list_uuid_example",
                email_segment_uuid="email_segment_uuid_example",
                exclude=True,
                name="name_example",
            ),
        ],
        merchant_id="merchant_id_example",
        name="name_example",
        open_rate_formatted="open_rate_formatted_example",
        prevent_sending_due_to_spam=True,
        revenue_formatted="revenue_formatted_example",
        revenue_per_customer_formatted="revenue_per_customer_formatted_example",
        scheduled_dts="scheduled_dts_example",
        screenshot_large_full_url="screenshot_large_full_url_example",
        sms_esp_twilio_uuid="sms_esp_twilio_uuid_example",
        sms_phone_number="sms_phone_number_example",
        status="status_example",
        status_dts="status_dts_example",
        storefront_oid=1,
    ) # EmailCampaign | Email campaign

    # example passing only required values which don't have defaults set
    try:
        # Insert email campaign
        api_response = api_instance.insert_email_campaign(storefront_oid, email_campaign)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_campaign_folder**
> EmailCampaignFolderResponse insert_email_campaign_folder(storefront_oid, email_campaign_folder)

Insert email campaign folder

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_campaign_folder import EmailCampaignFolder
from ultracart.model.email_campaign_folder_response import EmailCampaignFolderResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_campaign_folder = EmailCampaignFolder(
        esp_campaign_folder_uuid="esp_campaign_folder_uuid_example",
        merchant_id="merchant_id_example",
        name="name_example",
        storefront_oid=1,
        system_generated=True,
    ) # EmailCampaignFolder | Email campaign folder

    # example passing only required values which don't have defaults set
    try:
        # Insert email campaign folder
        api_response = api_instance.insert_email_campaign_folder(storefront_oid, email_campaign_folder)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_commseq**
> EmailCommseqResponse insert_email_commseq(storefront_oid, email_commseq)

Insert email commseq

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq import EmailCommseq
from ultracart.model.email_commseq_response import EmailCommseqResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_commseq = EmailCommseq(
        email_communication_sequence_steps=[
            EmailCommseqStep(
                alt_child_email_communication_sequence_steps=[
                    EmailCommseqStep(),
                ],
                child_email_communication_sequence_steps=[
                    EmailCommseqStep(),
                ],
                email_communication_sequence_step_uuid="email_communication_sequence_step_uuid_example",
                email_pending_review=True,
                email_rejected=True,
                email_requires_review=True,
                filter_profile_equation_json="filter_profile_equation_json_example",
                merchant_notes="merchant_notes_example",
                step_config_json="step_config_json_example",
                type="begin",
            ),
        ],
        email_communication_sequence_uuid="email_communication_sequence_uuid_example",
        merchant_id="merchant_id_example",
        storefront_oid=1,
    ) # EmailCommseq | Email commseq

    # example passing only required values which don't have defaults set
    try:
        # Insert email commseq
        api_response = api_instance.insert_email_commseq(storefront_oid, email_commseq)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_email**
> EmailCommseqEmailResponse insert_email_email(storefront_oid, email_commseq_email)

Insert email email

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseq_email_response import EmailCommseqEmailResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq_email import EmailCommseqEmail
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_commseq_email = EmailCommseqEmail(
        deleted=True,
        edited_by_user="edited_by_user_example",
        email_communication_sequence_email_uuid="email_communication_sequence_email_uuid_example",
        email_communication_sequence_uuid="email_communication_sequence_uuid_example",
        email_container_cjson="email_container_cjson_example",
        email_container_cjson_last_modified_dts="email_container_cjson_last_modified_dts_example",
        email_template_vm_path="email_template_vm_path_example",
        filter_profile_equation_json="filter_profile_equation_json_example",
        individually_render=True,
        library_item_oid=1,
        magic_link=True,
        merchant_id="merchant_id_example",
        pending_review=True,
        preview_text="preview_text_example",
        rejected=True,
        requires_review=True,
        screenshot_large_full_url="screenshot_large_full_url_example",
        screenshot_large_viewport_url="screenshot_large_viewport_url_example",
        screenshot_small_full_url="screenshot_small_full_url_example",
        screenshot_small_viewport_url="screenshot_small_viewport_url_example",
        smart_sending=True,
        storefront_oid=1,
        subject="subject_example",
        suspended_for_spam=True,
        transactional_email=True,
        version=1,
    ) # EmailCommseqEmail | Email email

    # example passing only required values which don't have defaults set
    try:
        # Insert email email
        api_response = api_instance.insert_email_email(storefront_oid, email_commseq_email)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_flow**
> EmailFlowResponse insert_email_flow(storefront_oid, email_flow)

Insert email flow

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_flow import EmailFlow
from ultracart.model.email_flow_response import EmailFlowResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_flow = EmailFlow(
        allow_multiple_concurrent_enrollments=True,
        back_populating=True,
        click_rate_formatted="click_rate_formatted_example",
        created_dts="created_dts_example",
        deleted=True,
        email_communication_sequence_uuid="email_communication_sequence_uuid_example",
        email_flow_uuid="email_flow_uuid_example",
        end_once_customer_purchases=True,
        end_once_customer_purchases_anywhere=True,
        enrolled_customers=1,
        esp_domain_user="esp_domain_user_example",
        esp_domain_uuid="esp_domain_uuid_example",
        esp_flow_folder_uuid="esp_flow_folder_uuid_example",
        esp_friendly_name="esp_friendly_name_example",
        filter_profile_equation_json="filter_profile_equation_json_example",
        library_item_oid=1,
        maximum_enrolled=True,
        merchant_id="merchant_id_example",
        name="name_example",
        open_rate_formatted="open_rate_formatted_example",
        revenue_formatted="revenue_formatted_example",
        revenue_per_customer_formatted="revenue_per_customer_formatted_example",
        screenshot_large_full_url="screenshot_large_full_url_example",
        sms_esp_twilio_uuid="sms_esp_twilio_uuid_example",
        sms_phone_number="sms_phone_number_example",
        status="status_example",
        status_dts="status_dts_example",
        storefront_oid=1,
        trigger_parameter="trigger_parameter_example",
        trigger_parameter_name="trigger_parameter_name_example",
        trigger_type="trigger_type_example",
    ) # EmailFlow | Email flow

    # example passing only required values which don't have defaults set
    try:
        # Insert email flow
        api_response = api_instance.insert_email_flow(storefront_oid, email_flow)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_flow_folder**
> EmailFlowFolderResponse insert_email_flow_folder(storefront_oid, email_flow_folder)

Insert email flow folder

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_flow_folder_response import EmailFlowFolderResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_flow_folder import EmailFlowFolder
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_flow_folder = EmailFlowFolder(
        esp_flow_folder_uuid="esp_flow_folder_uuid_example",
        merchant_id="merchant_id_example",
        name="name_example",
        storefront_oid=1,
        system_generated=True,
    ) # EmailFlowFolder | Email flow folder

    # example passing only required values which don't have defaults set
    try:
        # Insert email flow folder
        api_response = api_instance.insert_email_flow_folder(storefront_oid, email_flow_folder)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_list**
> EmailListResponse insert_email_list(storefront_oid, email_list)

Insert email list

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_list_response import EmailListResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_list import EmailList
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list = EmailList(
        allow_csv_download=True,
        created_dts="created_dts_example",
        deleted=True,
        email_list_uuid="email_list_uuid_example",
        esp_list_segment_folder_uuid="esp_list_segment_folder_uuid_example",
        member_count=1,
        merchant_id="merchant_id_example",
        name="name_example",
        public_description="public_description_example",
        public_list=True,
        storefront_oid=1,
        used_by=[
            EmailListSegmentUsedBy(
                email_campaign_uuid="email_campaign_uuid_example",
                email_flow_uuid="email_flow_uuid_example",
                name="name_example",
            ),
        ],
    ) # EmailList | Email list

    # example passing only required values which don't have defaults set
    try:
        # Insert email list
        api_response = api_instance.insert_email_list(storefront_oid, email_list)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_list_segment_folder**
> EmailListSegmentFolderResponse insert_email_list_segment_folder(storefront_oid, email_list_segment_folder)

Insert email campaign folder

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_list_segment_folder_response import EmailListSegmentFolderResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_list_segment_folder import EmailListSegmentFolder
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list_segment_folder = EmailListSegmentFolder(
        esp_list_segment_folder_uuid="esp_list_segment_folder_uuid_example",
        merchant_id="merchant_id_example",
        name="name_example",
        storefront_oid=1,
        system_generated=True,
    ) # EmailListSegmentFolder | Email campaign folder

    # example passing only required values which don't have defaults set
    try:
        # Insert email campaign folder
        api_response = api_instance.insert_email_list_segment_folder(storefront_oid, email_list_segment_folder)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_postcard**
> EmailCommseqPostcardResponse insert_email_postcard(storefront_oid, email_commseq_postcard)

Insert email postcard

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq_postcard import EmailCommseqPostcard
from ultracart.model.email_commseq_postcard_response import EmailCommseqPostcardResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_commseq_postcard = EmailCommseqPostcard(
        deleted=True,
        edited_by_user="edited_by_user_example",
        email_communication_sequence_postcard_uuid="email_communication_sequence_postcard_uuid_example",
        filter_profile_equation_json="filter_profile_equation_json_example",
        merchant_id="merchant_id_example",
        postcard_back_container_cjson="postcard_back_container_cjson_example",
        postcard_back_container_uuid="postcard_back_container_uuid_example",
        postcard_container_cjson_last_modified_dts="postcard_container_cjson_last_modified_dts_example",
        postcard_front_container_cjson="postcard_front_container_cjson_example",
        postcard_front_container_uuid="postcard_front_container_uuid_example",
        screenshot_back_url="screenshot_back_url_example",
        screenshot_front_url="screenshot_front_url_example",
        storefront_oid=1,
    ) # EmailCommseqPostcard | Email postcard

    # example passing only required values which don't have defaults set
    try:
        # Insert email postcard
        api_response = api_instance.insert_email_postcard(storefront_oid, email_commseq_postcard)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_segment**
> EmailSegmentResponse insert_email_segment(storefront_oid, email_segment)

Insert email segment

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_segment import EmailSegment
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_segment_response import EmailSegmentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_segment = EmailSegment(
        allow_csv_download=True,
        allow_facebook_audiences=True,
        created_dts="created_dts_example",
        deleted=True,
        email_segment_uuid="email_segment_uuid_example",
        esp_list_segment_folder_uuid="esp_list_segment_folder_uuid_example",
        facebook_custom_audience=True,
        filter_profile_equation_json="filter_profile_equation_json_example",
        member_count=1,
        merchant_id="merchant_id_example",
        name="name_example",
        rank_json="rank_json_example",
        rebuild_percentage=3.14,
        rebuild_required=True,
        storefront_oid=1,
        thirdparty_join_add_tags=[
            "thirdparty_join_add_tags_example",
        ],
        thirdparty_join_remove_tags=[
            "thirdparty_join_remove_tags_example",
        ],
        thirdparty_leave_add_tags=[
            "thirdparty_leave_add_tags_example",
        ],
        thirdparty_leave_remove_tags=[
            "thirdparty_leave_remove_tags_example",
        ],
        thirdparty_list_id="thirdparty_list_id_example",
        thirdparty_provider_name="thirdparty_provider_name_example",
        used_by=[
            EmailListSegmentUsedBy(
                email_campaign_uuid="email_campaign_uuid_example",
                email_flow_uuid="email_flow_uuid_example",
                name="name_example",
            ),
        ],
    ) # EmailSegment | Email segment

    # example passing only required values which don't have defaults set
    try:
        # Insert email segment
        api_response = api_instance.insert_email_segment(storefront_oid, email_segment)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_screen_recording_segment**
> ScreenRecordingSegmentResponse insert_screen_recording_segment(storefront_oid, segment)

Insert screen recording segment

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_segment import ScreenRecordingSegment
from ultracart.model.error_response import ErrorResponse
from ultracart.model.screen_recording_segment_response import ScreenRecordingSegmentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    segment = ScreenRecordingSegment(
        create_dts="create_dts_example",
        description="description_example",
        filter=ScreenRecordingFilter(
            affiliate_email="affiliate_email_example",
            affiliate_id=1,
            communications_campaign_name="communications_campaign_name_example",
            communications_campaign_name_filter=True,
            communications_email_subject="communications_email_subject_example",
            communications_email_subject_filter=True,
            communications_flow_name="communications_flow_name_example",
            communications_flow_name_filter=True,
            email=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            email_domain="email_domain_example",
            email_domain_filter=True,
            email_identified=True,
            end_timestamp=ScreenRecordingFilterRangeDate(
                end="end_example",
                start="start_example",
            ),
            esp_customer_uuid="esp_customer_uuid_example",
            favorite=True,
            geolocation=ScreenRecordingFilterGeoDistance(
                distance=1,
                distance_uom="distance_uom_example",
                from_address="from_address_example",
                lat=3.14,
                lon=3.14,
            ),
            geolocation_country=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            geolocation_country_filter=True,
            geolocation_state=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            geolocation_state_filter=True,
            language_iso_code=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            language_iso_code_filter=True,
            last_x_days=1,
            max_filter_values=1,
            order_id=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            page_view_count=ScreenRecordingFilterRangeInteger(
                eq=1,
                gt=1,
                gte=1,
                lt=1,
                lte=1,
            ),
            page_views=[
                ScreenRecordingFilterPageView(
                    domain=ScreenRecordingFilterStringSearch(
                        does_not_exist=True,
                        exists=True,
                        _is="_is_example",
                        is_not="is_not_example",
                        starts_with="starts_with_example",
                    ),
                    domain_filter=True,
                    event_name_filter=True,
                    event_param_name_filter=True,
                    event_param_value_filter=True,
                    events=[
                        ScreenRecordingFilterPageViewEvent(
                            event_name="event_name_example",
                            event_params=[
                                ScreenRecordingFilterPageViewEventParam(
                                    name="name_example",
                                    value_bd=ScreenRecordingFilterRangeBigDecimal(
                                        eq=3.14,
                                        gt=3.14,
                                        gte=3.14,
                                        lt=3.14,
                                        lte=3.14,
                                    ),
                                    value_bool=True,
                                    value_num=ScreenRecordingFilterRangeInteger(
                                        eq=1,
                                        gt=1,
                                        gte=1,
                                        lt=1,
                                        lte=1,
                                    ),
                                    value_text=ScreenRecordingFilterStringSearch(
                                        does_not_exist=True,
                                        exists=True,
                                        _is="_is_example",
                                        is_not="is_not_example",
                                        starts_with="starts_with_example",
                                    ),
                                ),
                            ],
                        ),
                    ],
                    param_name_filter=True,
                    param_value_filter=True,
                    params=[
                        ScreenRecordingFilterPageViewParam(
                            name="name_example",
                            value=ScreenRecordingFilterStringSearch(
                                does_not_exist=True,
                                exists=True,
                                _is="_is_example",
                                is_not="is_not_example",
                                starts_with="starts_with_example",
                            ),
                        ),
                    ],
                    referrer=ScreenRecordingFilterStringSearch(
                        does_not_exist=True,
                        exists=True,
                        _is="_is_example",
                        is_not="is_not_example",
                        starts_with="starts_with_example",
                    ),
                    referrer_params=[
                        ScreenRecordingFilterPageViewReferrerParam(
                            name="name_example",
                            value=ScreenRecordingFilterStringSearch(
                                does_not_exist=True,
                                exists=True,
                                _is="_is_example",
                                is_not="is_not_example",
                                starts_with="starts_with_example",
                            ),
                        ),
                    ],
                    referrer_raw=ScreenRecordingFilterStringSearch(
                        does_not_exist=True,
                        exists=True,
                        _is="_is_example",
                        is_not="is_not_example",
                        starts_with="starts_with_example",
                    ),
                    time_on_page=ScreenRecordingFilterRangeInteger(
                        eq=1,
                        gt=1,
                        gte=1,
                        lt=1,
                        lte=1,
                    ),
                    time_on_page_max_filter=True,
                    time_on_page_min_filter=True,
                    url=ScreenRecordingFilterStringSearch(
                        does_not_exist=True,
                        exists=True,
                        _is="_is_example",
                        is_not="is_not_example",
                        starts_with="starts_with_example",
                    ),
                    url_filter=True,
                ),
            ],
            placed_order=True,
            preferred_language=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            preferred_language_filter=True,
            referrer_domain="referrer_domain_example",
            referrer_domain_filter=True,
            screen_recording_uuids=[
                "screen_recording_uuids_example",
            ],
            screen_sizes=[
                "screen_sizes_example",
            ],
            skip_filter_values=True,
            skip_histogram=True,
            skip_hits=True,
            start_timestamp=ScreenRecordingFilterRangeDate(
                end="end_example",
                start="start_example",
            ),
            tags=[
                "tags_example",
            ],
            time_on_site=ScreenRecordingFilterRangeInteger(
                eq=1,
                gt=1,
                gte=1,
                lt=1,
                lte=1,
            ),
            time_on_site_max_filter=True,
            time_on_site_min_filter=True,
            url_filter=True,
            user_agent_device_name="user_agent_device_name_example",
            user_agent_device_name_filter=True,
            user_agent_device_os_name_filter=True,
            user_agent_device_os_version_filter=True,
            user_agent_name="user_agent_name_example",
            user_agent_name_filter=True,
            user_agent_original=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            user_agent_original_filter=True,
            user_agent_os_name="user_agent_os_name_example",
            user_agent_os_version="user_agent_os_version_example",
            user_ip=ScreenRecordingFilterIpSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
            ),
            utm_campaign="utm_campaign_example",
            utm_campaign_filter=True,
            utm_source="utm_source_example",
            utm_source_filter=True,
            visitor_number=1,
            watched=True,
        ),
        histogram_data=[
            1,
        ],
        histogram_interval="histogram_interval_example",
        histogram_start_dts="histogram_start_dts_example",
        name="name_example",
        screen_recording_segment_oid=1,
        session_count=1,
        session_count_last_update_dts="session_count_last_update_dts_example",
    ) # ScreenRecordingSegment | Segment

    # example passing only required values which don't have defaults set
    try:
        # Insert screen recording segment
        api_response = api_instance.insert_screen_recording_segment(storefront_oid, segment)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepare_download_email_segment**
> EmailSegmentDownloadPrepareResponse prepare_download_email_segment(storefront_oid, email_segment_uuid)

Prepare download of email segment

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_segment_download_prepare_response import EmailSegmentDownloadPrepareResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_segment_uuid = "email_segment_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Prepare download of email segment
        api_response = api_instance.prepare_download_email_segment(storefront_oid, email_segment_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_library_item**
> LibraryItemResponse publish_library_item(library_item_oid, publish_library_request)

Publish library item.

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.library_item_response import LibraryItemResponse
from ultracart.model.publish_library_item_request import PublishLibraryItemRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    library_item_oid = 1 # int | 
    publish_library_request = PublishLibraryItemRequest(
        release_notes="release_notes_example",
    ) # PublishLibraryItemRequest | Publish library item request

    # example passing only required values which don't have defaults set
    try:
        # Publish library item.
        api_response = api_instance.publish_library_item(library_item_oid, publish_library_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_library_item**
> LibraryItemResponse purchase_library_item(library_item_oid)

Purchase public library item, which creates a copy of the item in your personal code library

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.library_item_response import LibraryItemResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    library_item_oid = 1 # int | 
    storefront_oid = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Purchase public library item, which creates a copy of the item in your personal code library
        api_response = api_instance.purchase_library_item(library_item_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->purchase_library_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Purchase public library item, which creates a copy of the item in your personal code library
        api_response = api_instance.purchase_library_item(library_item_oid, storefront_oid=storefront_oid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_email_commseq_step_waiting**
> release_email_commseq_step_waiting(storefront_oid, commseq_uuid, commseq_step_uuid)

Release email communication sequence customers waiting at the specified step

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 
    commseq_step_uuid = "commseq_step_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Release email communication sequence customers waiting at the specified step
        api_instance.release_email_commseq_step_waiting(storefront_oid, commseq_uuid, commseq_step_uuid)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review**
> EmailCommseqEmailSendTestResponse review(storefront_oid, commseq_email_uuid, email_commseq_email_review_request)

Request a review of an email

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseq_email_send_test_response import EmailCommseqEmailSendTestResponse
from ultracart.model.email_commseq_email_send_test_request import EmailCommseqEmailSendTestRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_email_uuid = "commseq_email_uuid_example" # str | 
    email_commseq_email_review_request = EmailCommseqEmailSendTestRequest(
        cart_id="cart_id_example",
        cart_item_ids=[
            "cart_item_ids_example",
        ],
        esp_commseq_email_uuid="esp_commseq_email_uuid_example",
        esp_commseq_step_uuid="esp_commseq_step_uuid_example",
        esp_commseq_uuid="esp_commseq_uuid_example",
        name="name_example",
        order_id="order_id_example",
        please_review=True,
        send_to_additional_emails=[
            "send_to_additional_emails_example",
        ],
        send_to_logged_in_user=True,
    ) # EmailCommseqEmailSendTestRequest | Email commseq email review request

    # example passing only required values which don't have defaults set
    try:
        # Request a review of an email
        api_response = api_instance.review(storefront_oid, commseq_email_uuid, email_commseq_email_review_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> LookupResponse search()

Searches for all matching values

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.lookup_response import LookupResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    category = "category_example" # str |  (optional)
    matches = "matches_example" # str |  (optional)
    storefront_oid = "storefront_oid_example" # str |  (optional)
    max_hits = 1 # int |  (optional)
    subcategory = "subcategory_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Searches for all matching values
        api_response = api_instance.search(category=category, matches=matches, storefront_oid=storefront_oid, max_hits=max_hits, subcategory=subcategory)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search2**
> LookupResponse search2(lookup_request)

Searches for all matching values (using POST)

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.lookup_response import LookupResponse
from ultracart.model.lookup_request import LookupRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    lookup_request = LookupRequest(
        category="category_example",
        matches="matches_example",
        max_hits=1,
        storefront_host_name="storefront_host_name_example",
        storefront_oid=1,
        subcategory="subcategory_example",
    ) # LookupRequest | LookupRequest

    # example passing only required values which don't have defaults set
    try:
        # Searches for all matching values (using POST)
        api_response = api_instance.search2(lookup_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_email_list_customers**
> EmailListCustomersResponse search_email_list_customers(storefront_oid, email_list_uuid)

Search email list customers

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_list_customers_response import EmailListCustomersResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list_uuid = "email_list_uuid_example" # str | 
    starts_with = "startsWith_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search email list customers
        api_response = api_instance.search_email_list_customers(storefront_oid, email_list_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->search_email_list_customers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search email list customers
        api_response = api_instance.search_email_list_customers(storefront_oid, email_list_uuid, starts_with=starts_with)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_email_segment_customers**
> EmailSegmentCustomersResponse search_email_segment_customers(storefront_oid, email_segment_uuid)

Search email segment customers

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_segment_customers_response import EmailSegmentCustomersResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_segment_uuid = "email_segment_uuid_example" # str | 
    starts_with = "startsWith_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search email segment customers
        api_response = api_instance.search_email_segment_customers(storefront_oid, email_segment_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->search_email_segment_customers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search email segment customers
        api_response = api_instance.search_email_segment_customers(storefront_oid, email_segment_uuid, starts_with=starts_with)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_library_items**
> LibraryItemsResponse search_library_items(item_query)

Retrieve library items

Retrieves a library items based on a query object.  If no parameters are specified, the API call will default to the merchant id only.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.library_items_response import LibraryItemsResponse
from ultracart.model.library_item_query import LibraryItemQuery
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    item_query = LibraryItemQuery(
        category="category_example",
        content_type="content_type_example",
        description="description_example",
        industry="industry_example",
        price_high=3.14,
        price_low=3.14,
        published_dts_begin="published_dts_begin_example",
        published_dts_end="published_dts_end_example",
        source_of_published=True,
        style="style_example",
        title="title_example",
        type="type_example",
    ) # LibraryItemQuery | Item query
    limit = 10000 # int | The maximum number of records to return on this one API call. (Maximum 10000) (optional) if omitted the server will use the default value of 10000
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve library items
        api_response = api_instance.search_library_items(item_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->search_library_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve library items
        api_response = api_instance.search_library_items(item_query, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->search_library_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_query** | [**LibraryItemQuery**](LibraryItemQuery.md)| Item query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 10000) | [optional] if omitted the server will use the default value of 10000
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]

### Return type

[**LibraryItemsResponse**](LibraryItemsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_published_items**
> LibraryItemsResponse search_published_items(item_query)

Retrieve library items

Retrieves a library items based on a query object.  If no parameters are specified, the API call will default to the merchant id only.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.library_items_response import LibraryItemsResponse
from ultracart.model.library_item_query import LibraryItemQuery
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    item_query = LibraryItemQuery(
        category="category_example",
        content_type="content_type_example",
        description="description_example",
        industry="industry_example",
        price_high=3.14,
        price_low=3.14,
        published_dts_begin="published_dts_begin_example",
        published_dts_end="published_dts_end_example",
        source_of_published=True,
        style="style_example",
        title="title_example",
        type="type_example",
    ) # LibraryItemQuery | Item query
    limit = 10000 # int | The maximum number of records to return on this one API call. (Maximum 10000) (optional) if omitted the server will use the default value of 10000
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve library items
        api_response = api_instance.search_published_items(item_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->search_published_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve library items
        api_response = api_instance.search_published_items(item_query, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->search_published_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_query** | [**LibraryItemQuery**](LibraryItemQuery.md)| Item query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 10000) | [optional] if omitted the server will use the default value of 10000
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]

### Return type

[**LibraryItemsResponse**](LibraryItemsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_review_items**
> LibraryItemsResponse search_review_items(item_query)

Retrieve library items needing review or rejected

Retrieves a library items based on a query object.  If no parameters are specified, the API call will default to the merchant id only.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.library_items_response import LibraryItemsResponse
from ultracart.model.library_item_query import LibraryItemQuery
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    item_query = LibraryItemQuery(
        category="category_example",
        content_type="content_type_example",
        description="description_example",
        industry="industry_example",
        price_high=3.14,
        price_low=3.14,
        published_dts_begin="published_dts_begin_example",
        published_dts_end="published_dts_end_example",
        source_of_published=True,
        style="style_example",
        title="title_example",
        type="type_example",
    ) # LibraryItemQuery | Item query
    limit = 10000 # int | The maximum number of records to return on this one API call. (Maximum 10000) (optional) if omitted the server will use the default value of 10000
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve library items needing review or rejected
        api_response = api_instance.search_review_items(item_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->search_review_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve library items needing review or rejected
        api_response = api_instance.search_review_items(item_query, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->search_review_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_query** | [**LibraryItemQuery**](LibraryItemQuery.md)| Item query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 10000) | [optional] if omitted the server will use the default value of 10000
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]

### Return type

[**LibraryItemsResponse**](LibraryItemsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_shared_items**
> LibraryItemsResponse search_shared_items(item_query)

Retrieve library items

Retrieves a library items based on a query object.  If no parameters are specified, the API call will default to the merchant id only.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.library_items_response import LibraryItemsResponse
from ultracart.model.library_item_query import LibraryItemQuery
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    item_query = LibraryItemQuery(
        category="category_example",
        content_type="content_type_example",
        description="description_example",
        industry="industry_example",
        price_high=3.14,
        price_low=3.14,
        published_dts_begin="published_dts_begin_example",
        published_dts_end="published_dts_end_example",
        source_of_published=True,
        style="style_example",
        title="title_example",
        type="type_example",
    ) # LibraryItemQuery | Item query
    limit = 10000 # int | The maximum number of records to return on this one API call. (Maximum 10000) (optional) if omitted the server will use the default value of 10000
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    sort = "_sort_example" # str | The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve library items
        api_response = api_instance.search_shared_items(item_query)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->search_shared_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve library items
        api_response = api_instance.search_shared_items(item_query, limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->search_shared_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_query** | [**LibraryItemQuery**](LibraryItemQuery.md)| Item query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 10000) | [optional] if omitted the server will use the default value of 10000
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the library items.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]

### Return type

[**LibraryItemsResponse**](LibraryItemsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_test**
> EmailCommseqEmailSendTestResponse send_email_test(storefront_oid, commseq_email_uuid, email_commseq_email_test_request)

Send email test

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseq_email_send_test_response import EmailCommseqEmailSendTestResponse
from ultracart.model.email_commseq_email_send_test_request import EmailCommseqEmailSendTestRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_email_uuid = "commseq_email_uuid_example" # str | 
    email_commseq_email_test_request = EmailCommseqEmailSendTestRequest(
        cart_id="cart_id_example",
        cart_item_ids=[
            "cart_item_ids_example",
        ],
        esp_commseq_email_uuid="esp_commseq_email_uuid_example",
        esp_commseq_step_uuid="esp_commseq_step_uuid_example",
        esp_commseq_uuid="esp_commseq_uuid_example",
        name="name_example",
        order_id="order_id_example",
        please_review=True,
        send_to_additional_emails=[
            "send_to_additional_emails_example",
        ],
        send_to_logged_in_user=True,
    ) # EmailCommseqEmailSendTestRequest | Email commseq email test request

    # example passing only required values which don't have defaults set
    try:
        # Send email test
        api_response = api_instance.send_email_test(storefront_oid, commseq_email_uuid, email_commseq_email_test_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_postcard_test**
> EmailCommseqPostcardSendTestResponse send_postcard_test(storefront_oid, commseq_postcard_uuid, email_commseq_postcard_test_request)

Send postcard test

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseq_postcard_send_test_response import EmailCommseqPostcardSendTestResponse
from ultracart.model.email_commseq_postcard_send_test_request import EmailCommseqPostcardSendTestRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_postcard_uuid = "commseq_postcard_uuid_example" # str | 
    email_commseq_postcard_test_request = EmailCommseqPostcardSendTestRequest(
        address_1="address_1_example",
        address_2="address_2_example",
        cart_id="cart_id_example",
        cart_item_ids=[
            "cart_item_ids_example",
        ],
        city="city_example",
        esp_commseq_postcard_uuid="esp_commseq_postcard_uuid_example",
        esp_commseq_step_uuid="esp_commseq_step_uuid_example",
        esp_commseq_uuid="esp_commseq_uuid_example",
        mail_card=True,
        name="name_example",
        order_id="order_id_example",
        postal_code="postal_code_example",
        state="state_example",
    ) # EmailCommseqPostcardSendTestRequest | Email commseq email test request

    # example passing only required values which don't have defaults set
    try:
        # Send postcard test
        api_response = api_instance.send_postcard_test(storefront_oid, commseq_postcard_uuid, email_commseq_postcard_test_request)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms_test**
> EmailCommseqSmsSendTestResponse send_sms_test(storefront_oid, commseq_uuid, commseq_step_uuid, email_commseq_sms_test_request)

Send SMS test

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseq_sms_send_test_response import EmailCommseqSmsSendTestResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq_sms_send_test_request import EmailCommseqSmsSendTestRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 
    commseq_step_uuid = "commseq_step_uuid_example" # str | 
    email_commseq_sms_test_request = EmailCommseqSmsSendTestRequest(
        esp_commseq_step_uuid="esp_commseq_step_uuid_example",
        esp_commseq_uuid="esp_commseq_uuid_example",
        send_to_cellphone_e164="send_to_cellphone_e164_example",
    ) # EmailCommseqSmsSendTestRequest | Email commseq sms test request

    # example passing only required values which don't have defaults set
    try:
        # Send SMS test
        api_response = api_instance.send_sms_test(storefront_oid, commseq_uuid, commseq_step_uuid, email_commseq_sms_test_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->send_sms_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **commseq_uuid** | **str**|  |
 **commseq_step_uuid** | **str**|  |
 **email_commseq_sms_test_request** | [**EmailCommseqSmsSendTestRequest**](EmailCommseqSmsSendTestRequest.md)| Email commseq sms test request |

### Return type

[**EmailCommseqSmsSendTestResponse**](EmailCommseqSmsSendTestResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_webhook_test**
> EmailCommseqWebhookSendTestResponse send_webhook_test(storefront_oid, email_commseq_webhook_test_request)

Send webhook test

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseq_webhook_send_test_request import EmailCommseqWebhookSendTestRequest
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq_webhook_send_test_response import EmailCommseqWebhookSendTestResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_commseq_webhook_test_request = EmailCommseqWebhookSendTestRequest(
        cart_id="cart_id_example",
        cart_item_ids=[
            "cart_item_ids_example",
        ],
        email="email_example",
        esp_commseq_step_uuid="esp_commseq_step_uuid_example",
        esp_commseq_uuid="esp_commseq_uuid_example",
        name="name_example",
        order_id="order_id_example",
    ) # EmailCommseqWebhookSendTestRequest | Email commseq webhook test request

    # example passing only required values which don't have defaults set
    try:
        # Send webhook test
        api_response = api_instance.send_webhook_test(storefront_oid, email_commseq_webhook_test_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->send_webhook_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **email_commseq_webhook_test_request** | [**EmailCommseqWebhookSendTestRequest**](EmailCommseqWebhookSendTestRequest.md)| Email commseq webhook test request |

### Return type

[**EmailCommseqWebhookSendTestResponse**](EmailCommseqWebhookSendTestResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sequence_test**
> EmailCommseqSequenceTestResponse sequence_test(storefront_oid, commseq_uuid, email_commseq_sequence_test_request)

Sequence test

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseq_sequence_test_request import EmailCommseqSequenceTestRequest
from ultracart.model.email_commseq_sequence_test_response import EmailCommseqSequenceTestResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 
    email_commseq_sequence_test_request = EmailCommseqSequenceTestRequest(
        address_1="address_1_example",
        address_2="address_2_example",
        cart_id="cart_id_example",
        cart_item_ids=[
            "cart_item_ids_example",
        ],
        city="city_example",
        esp_commseq_uuid="esp_commseq_uuid_example",
        mail_card=True,
        name="name_example",
        order_id="order_id_example",
        please_review=True,
        postal_code="postal_code_example",
        send_to_cellphone_e164="send_to_cellphone_e164_example",
        send_to_email="send_to_email_example",
        send_to_logged_in_user=True,
        state="state_example",
    ) # EmailCommseqSequenceTestRequest | Commseq test request

    # example passing only required values which don't have defaults set
    try:
        # Sequence test
        api_response = api_instance.sequence_test(storefront_oid, commseq_uuid, email_commseq_sequence_test_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->sequence_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **commseq_uuid** | **str**|  |
 **email_commseq_sequence_test_request** | [**EmailCommseqSequenceTestRequest**](EmailCommseqSequenceTestRequest.md)| Commseq test request |

### Return type

[**EmailCommseqSequenceTestResponse**](EmailCommseqSequenceTestResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_email_campaign**
> BaseResponse start_email_campaign(storefront_oid, email_campaign_uuid)

Start email campaign

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.base_response import BaseResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_campaign_uuid = "email_campaign_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Start email campaign
        api_response = api_instance.start_email_campaign(storefront_oid, email_campaign_uuid)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_to_email_list**
> EmailListSubscribeResponse subscribe_to_email_list(storefront_oid, email_list_uuid, customers)

Subscribe customers to email list

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_list_subscribe_response import EmailListSubscribeResponse
from ultracart.model.email_customer import EmailCustomer
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list_uuid = "email_list_uuid_example" # str | 
    customers = [
        EmailCustomer(
            active=True,
            email="email_example",
            email_customer_uuid="email_customer_uuid_example",
            first_name="first_name_example",
            global_unsubscribe=True,
            last_interaction_dts="last_interaction_dts_example",
            last_name="last_name_example",
            list_uuids=[
                "list_uuids_example",
            ],
        ),
    ] # [EmailCustomer] | Customers

    # example passing only required values which don't have defaults set
    try:
        # Subscribe customers to email list
        api_response = api_instance.subscribe_to_email_list(storefront_oid, email_list_uuid, customers)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->subscribe_to_email_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **email_list_uuid** | **str**|  |
 **customers** | [**[EmailCustomer]**](EmailCustomer.md)| Customers |

### Return type

[**EmailListSubscribeResponse**](EmailListSubscribeResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfavorite_screen_recording**
> unfavorite_screen_recording(storefront_oid, screen_recording_uuid)

Remove favorite flag on screen recording

Remove favorite flag on screen recording 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    screen_recording_uuid = "screen_recording_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove favorite flag on screen recording
        api_instance.unfavorite_screen_recording(storefront_oid, screen_recording_uuid)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_campaign**
> EmailCampaignResponse update_email_campaign(storefront_oid, email_campaign_uuid, email_campaign)

Update email campaign

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_campaign_response import EmailCampaignResponse
from ultracart.model.email_campaign import EmailCampaign
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_campaign_uuid = "email_campaign_uuid_example" # str | 
    email_campaign = EmailCampaign(
        click_rate_formatted="click_rate_formatted_example",
        created_dts="created_dts_example",
        deleted=True,
        email_campaign_uuid="email_campaign_uuid_example",
        email_communication_sequence_uuid="email_communication_sequence_uuid_example",
        end_once_customer_purchases=True,
        end_once_customer_purchases_anywhere=True,
        esp_campaign_folder_uuid="esp_campaign_folder_uuid_example",
        esp_domain_user="esp_domain_user_example",
        esp_domain_uuid="esp_domain_uuid_example",
        esp_friendly_name="esp_friendly_name_example",
        library_item_oid=1,
        memberships=[
            EmailListSegmentMembership(
                email_list_uuid="email_list_uuid_example",
                email_segment_uuid="email_segment_uuid_example",
                exclude=True,
                name="name_example",
            ),
        ],
        merchant_id="merchant_id_example",
        name="name_example",
        open_rate_formatted="open_rate_formatted_example",
        prevent_sending_due_to_spam=True,
        revenue_formatted="revenue_formatted_example",
        revenue_per_customer_formatted="revenue_per_customer_formatted_example",
        scheduled_dts="scheduled_dts_example",
        screenshot_large_full_url="screenshot_large_full_url_example",
        sms_esp_twilio_uuid="sms_esp_twilio_uuid_example",
        sms_phone_number="sms_phone_number_example",
        status="status_example",
        status_dts="status_dts_example",
        storefront_oid=1,
    ) # EmailCampaign | Email campaign

    # example passing only required values which don't have defaults set
    try:
        # Update email campaign
        api_response = api_instance.update_email_campaign(storefront_oid, email_campaign_uuid, email_campaign)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_campaign_folder**
> EmailCampaignFolderResponse update_email_campaign_folder(storefront_oid, email_campaign_folder_uuid, email_campaign_folder)

Update email campaign folder

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_campaign_folder import EmailCampaignFolder
from ultracart.model.email_campaign_folder_response import EmailCampaignFolderResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_campaign_folder_uuid = "email_campaign_folder_uuid_example" # str | 
    email_campaign_folder = EmailCampaignFolder(
        esp_campaign_folder_uuid="esp_campaign_folder_uuid_example",
        merchant_id="merchant_id_example",
        name="name_example",
        storefront_oid=1,
        system_generated=True,
    ) # EmailCampaignFolder | Email campaign folder

    # example passing only required values which don't have defaults set
    try:
        # Update email campaign folder
        api_response = api_instance.update_email_campaign_folder(storefront_oid, email_campaign_folder_uuid, email_campaign_folder)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_commseq**
> EmailCommseqResponse update_email_commseq(storefront_oid, commseq_uuid, email_commseq)

Update email commseq

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq import EmailCommseq
from ultracart.model.email_commseq_response import EmailCommseqResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_uuid = "commseq_uuid_example" # str | 
    email_commseq = EmailCommseq(
        email_communication_sequence_steps=[
            EmailCommseqStep(
                alt_child_email_communication_sequence_steps=[
                    EmailCommseqStep(),
                ],
                child_email_communication_sequence_steps=[
                    EmailCommseqStep(),
                ],
                email_communication_sequence_step_uuid="email_communication_sequence_step_uuid_example",
                email_pending_review=True,
                email_rejected=True,
                email_requires_review=True,
                filter_profile_equation_json="filter_profile_equation_json_example",
                merchant_notes="merchant_notes_example",
                step_config_json="step_config_json_example",
                type="begin",
            ),
        ],
        email_communication_sequence_uuid="email_communication_sequence_uuid_example",
        merchant_id="merchant_id_example",
        storefront_oid=1,
    ) # EmailCommseq | Email commseq

    # example passing only required values which don't have defaults set
    try:
        # Update email commseq
        api_response = api_instance.update_email_commseq(storefront_oid, commseq_uuid, email_commseq)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_customer**
> update_email_customer(storefront_oid, email_customer_uuid, email_customer)

Update email customer

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_customer import EmailCustomer
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_customer_uuid = "email_customer_uuid_example" # str | 
    email_customer = EmailCustomer(
        active=True,
        email="email_example",
        email_customer_uuid="email_customer_uuid_example",
        first_name="first_name_example",
        global_unsubscribe=True,
        last_interaction_dts="last_interaction_dts_example",
        last_name="last_name_example",
        list_uuids=[
            "list_uuids_example",
        ],
    ) # EmailCustomer | Email customer

    # example passing only required values which don't have defaults set
    try:
        # Update email customer
        api_instance.update_email_customer(storefront_oid, email_customer_uuid, email_customer)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_email**
> EmailCommseqEmailResponse update_email_email(storefront_oid, commseq_email_uuid, email_commseq_email)

Update email email

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_commseq_email_response import EmailCommseqEmailResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq_email import EmailCommseqEmail
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_email_uuid = "commseq_email_uuid_example" # str | 
    email_commseq_email = EmailCommseqEmail(
        deleted=True,
        edited_by_user="edited_by_user_example",
        email_communication_sequence_email_uuid="email_communication_sequence_email_uuid_example",
        email_communication_sequence_uuid="email_communication_sequence_uuid_example",
        email_container_cjson="email_container_cjson_example",
        email_container_cjson_last_modified_dts="email_container_cjson_last_modified_dts_example",
        email_template_vm_path="email_template_vm_path_example",
        filter_profile_equation_json="filter_profile_equation_json_example",
        individually_render=True,
        library_item_oid=1,
        magic_link=True,
        merchant_id="merchant_id_example",
        pending_review=True,
        preview_text="preview_text_example",
        rejected=True,
        requires_review=True,
        screenshot_large_full_url="screenshot_large_full_url_example",
        screenshot_large_viewport_url="screenshot_large_viewport_url_example",
        screenshot_small_full_url="screenshot_small_full_url_example",
        screenshot_small_viewport_url="screenshot_small_viewport_url_example",
        smart_sending=True,
        storefront_oid=1,
        subject="subject_example",
        suspended_for_spam=True,
        transactional_email=True,
        version=1,
    ) # EmailCommseqEmail | Email commseq email

    # example passing only required values which don't have defaults set
    try:
        # Update email email
        api_response = api_instance.update_email_email(storefront_oid, commseq_email_uuid, email_commseq_email)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_flow**
> EmailFlowResponse update_email_flow(storefront_oid, email_flow_uuid, email_flow)

Update email flow

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_flow import EmailFlow
from ultracart.model.email_flow_response import EmailFlowResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_flow_uuid = "email_flow_uuid_example" # str | 
    email_flow = EmailFlow(
        allow_multiple_concurrent_enrollments=True,
        back_populating=True,
        click_rate_formatted="click_rate_formatted_example",
        created_dts="created_dts_example",
        deleted=True,
        email_communication_sequence_uuid="email_communication_sequence_uuid_example",
        email_flow_uuid="email_flow_uuid_example",
        end_once_customer_purchases=True,
        end_once_customer_purchases_anywhere=True,
        enrolled_customers=1,
        esp_domain_user="esp_domain_user_example",
        esp_domain_uuid="esp_domain_uuid_example",
        esp_flow_folder_uuid="esp_flow_folder_uuid_example",
        esp_friendly_name="esp_friendly_name_example",
        filter_profile_equation_json="filter_profile_equation_json_example",
        library_item_oid=1,
        maximum_enrolled=True,
        merchant_id="merchant_id_example",
        name="name_example",
        open_rate_formatted="open_rate_formatted_example",
        revenue_formatted="revenue_formatted_example",
        revenue_per_customer_formatted="revenue_per_customer_formatted_example",
        screenshot_large_full_url="screenshot_large_full_url_example",
        sms_esp_twilio_uuid="sms_esp_twilio_uuid_example",
        sms_phone_number="sms_phone_number_example",
        status="status_example",
        status_dts="status_dts_example",
        storefront_oid=1,
        trigger_parameter="trigger_parameter_example",
        trigger_parameter_name="trigger_parameter_name_example",
        trigger_type="trigger_type_example",
    ) # EmailFlow | Email flow

    # example passing only required values which don't have defaults set
    try:
        # Update email flow
        api_response = api_instance.update_email_flow(storefront_oid, email_flow_uuid, email_flow)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_flow_folder**
> EmailFlowFolderResponse update_email_flow_folder(storefront_oid, email_flow_folder_uuid, email_flow_folder)

Update email flow folder

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_flow_folder_response import EmailFlowFolderResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_flow_folder import EmailFlowFolder
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_flow_folder_uuid = "email_flow_folder_uuid_example" # str | 
    email_flow_folder = EmailFlowFolder(
        esp_flow_folder_uuid="esp_flow_folder_uuid_example",
        merchant_id="merchant_id_example",
        name="name_example",
        storefront_oid=1,
        system_generated=True,
    ) # EmailFlowFolder | Email flow folder

    # example passing only required values which don't have defaults set
    try:
        # Update email flow folder
        api_response = api_instance.update_email_flow_folder(storefront_oid, email_flow_folder_uuid, email_flow_folder)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_global_settings**
> EmailGlobalSettingsResponse update_email_global_settings(global_settings)

Update email global settings

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_global_settings import EmailGlobalSettings
from ultracart.model.email_global_settings_response import EmailGlobalSettingsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    global_settings = EmailGlobalSettings(
        dedicated_ip=True,
    ) # EmailGlobalSettings | global settings request

    # example passing only required values which don't have defaults set
    try:
        # Update email global settings
        api_response = api_instance.update_email_global_settings(global_settings)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_list**
> EmailListResponse update_email_list(storefront_oid, email_list_uuid, email_list)

Update email list

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_list_response import EmailListResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_list import EmailList
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list_uuid = "email_list_uuid_example" # str | 
    email_list = EmailList(
        allow_csv_download=True,
        created_dts="created_dts_example",
        deleted=True,
        email_list_uuid="email_list_uuid_example",
        esp_list_segment_folder_uuid="esp_list_segment_folder_uuid_example",
        member_count=1,
        merchant_id="merchant_id_example",
        name="name_example",
        public_description="public_description_example",
        public_list=True,
        storefront_oid=1,
        used_by=[
            EmailListSegmentUsedBy(
                email_campaign_uuid="email_campaign_uuid_example",
                email_flow_uuid="email_flow_uuid_example",
                name="name_example",
            ),
        ],
    ) # EmailList | Email list

    # example passing only required values which don't have defaults set
    try:
        # Update email list
        api_response = api_instance.update_email_list(storefront_oid, email_list_uuid, email_list)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_list_segment_folder**
> EmailListSegmentFolderResponse update_email_list_segment_folder(storefront_oid, email_list_segment_folder_uuid, email_list_segment_folder)

Update email campaign folder

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_list_segment_folder_response import EmailListSegmentFolderResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_list_segment_folder import EmailListSegmentFolder
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_list_segment_folder_uuid = "email_list_segment_folder_uuid_example" # str | 
    email_list_segment_folder = EmailListSegmentFolder(
        esp_list_segment_folder_uuid="esp_list_segment_folder_uuid_example",
        merchant_id="merchant_id_example",
        name="name_example",
        storefront_oid=1,
        system_generated=True,
    ) # EmailListSegmentFolder | Email campaign folder

    # example passing only required values which don't have defaults set
    try:
        # Update email campaign folder
        api_response = api_instance.update_email_list_segment_folder(storefront_oid, email_list_segment_folder_uuid, email_list_segment_folder)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_plan**
> EmailPlanResponse update_email_plan(storefront_oid, settings)

Update email plan

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_plan import EmailPlan
from ultracart.model.email_plan_response import EmailPlanResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    settings = EmailPlan(
        additional_customers=1,
        additional_emails=1,
        additional_fee=3.14,
        allow_list_import=True,
        allow_tracking_emails=True,
        customer_tiers=[
            EmailPlanAdditional(
                active=True,
                can_downgrade=True,
                can_upgrade=True,
                cost=3.14,
                cost_change=3.14,
                cost_change_formatted="cost_change_formatted_example",
                cost_formatted="cost_formatted_example",
                customers=1,
                emails=1,
            ),
        ],
        initial_sending_limits=1,
        plan_customers=1,
        plan_emails=1,
        plan_name="plan_name_example",
        plan_name_formatted="plan_name_formatted_example",
        require_order_within_last_days=1,
        revenue_percent=1,
        spam_percent_limit=1,
        total_customers=1,
        total_emails=1,
        upgrade_to=1,
    ) # EmailPlan | plan request

    # example passing only required values which don't have defaults set
    try:
        # Update email plan
        api_response = api_instance.update_email_plan(storefront_oid, settings)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_postcard**
> EmailCommseqPostcardResponse update_email_postcard(storefront_oid, commseq_postcard_uuid, email_commseq_postcard)

Update email postcard

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_commseq_postcard import EmailCommseqPostcard
from ultracart.model.email_commseq_postcard_response import EmailCommseqPostcardResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    commseq_postcard_uuid = "commseq_postcard_uuid_example" # str | 
    email_commseq_postcard = EmailCommseqPostcard(
        deleted=True,
        edited_by_user="edited_by_user_example",
        email_communication_sequence_postcard_uuid="email_communication_sequence_postcard_uuid_example",
        filter_profile_equation_json="filter_profile_equation_json_example",
        merchant_id="merchant_id_example",
        postcard_back_container_cjson="postcard_back_container_cjson_example",
        postcard_back_container_uuid="postcard_back_container_uuid_example",
        postcard_container_cjson_last_modified_dts="postcard_container_cjson_last_modified_dts_example",
        postcard_front_container_cjson="postcard_front_container_cjson_example",
        postcard_front_container_uuid="postcard_front_container_uuid_example",
        screenshot_back_url="screenshot_back_url_example",
        screenshot_front_url="screenshot_front_url_example",
        storefront_oid=1,
    ) # EmailCommseqPostcard | Email commseq postcard

    # example passing only required values which don't have defaults set
    try:
        # Update email postcard
        api_response = api_instance.update_email_postcard(storefront_oid, commseq_postcard_uuid, email_commseq_postcard)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_segment**
> EmailSegmentResponse update_email_segment(storefront_oid, email_segment_uuid, email_segment)

Update email segment

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_segment import EmailSegment
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_segment_response import EmailSegmentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_segment_uuid = "email_segment_uuid_example" # str | 
    email_segment = EmailSegment(
        allow_csv_download=True,
        allow_facebook_audiences=True,
        created_dts="created_dts_example",
        deleted=True,
        email_segment_uuid="email_segment_uuid_example",
        esp_list_segment_folder_uuid="esp_list_segment_folder_uuid_example",
        facebook_custom_audience=True,
        filter_profile_equation_json="filter_profile_equation_json_example",
        member_count=1,
        merchant_id="merchant_id_example",
        name="name_example",
        rank_json="rank_json_example",
        rebuild_percentage=3.14,
        rebuild_required=True,
        storefront_oid=1,
        thirdparty_join_add_tags=[
            "thirdparty_join_add_tags_example",
        ],
        thirdparty_join_remove_tags=[
            "thirdparty_join_remove_tags_example",
        ],
        thirdparty_leave_add_tags=[
            "thirdparty_leave_add_tags_example",
        ],
        thirdparty_leave_remove_tags=[
            "thirdparty_leave_remove_tags_example",
        ],
        thirdparty_list_id="thirdparty_list_id_example",
        thirdparty_provider_name="thirdparty_provider_name_example",
        used_by=[
            EmailListSegmentUsedBy(
                email_campaign_uuid="email_campaign_uuid_example",
                email_flow_uuid="email_flow_uuid_example",
                name="name_example",
            ),
        ],
    ) # EmailSegment | Email segment

    # example passing only required values which don't have defaults set
    try:
        # Update email segment
        api_response = api_instance.update_email_segment(storefront_oid, email_segment_uuid, email_segment)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_sending_domain**
> EmailSendingDomainResponse update_email_sending_domain(domain, email_domain)

Update email sending domain

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.email_domain import EmailDomain
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_sending_domain_response import EmailSendingDomainResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    domain = "domain_example" # str | 
    email_domain = EmailDomain(
        comment="comment_example",
        dkim=[
            VerificationRecord(
                name="name_example",
                type="type_example",
                value="value_example",
            ),
        ],
        dkim_status="dkim_status_example",
        domain="domain_example",
        esp_domain_uuid="esp_domain_uuid_example",
        identity_status="identity_status_example",
        mailgun=Mailgun(
            api_key="api_key_example",
        ),
        merchant_id="merchant_id_example",
        provider="provider_example",
        spf=VerificationRecord(
            name="name_example",
            type="type_example",
            value="value_example",
        ),
        start_dkim_dts="start_dkim_dts_example",
        start_identity_dts="start_identity_dts_example",
        verification=VerificationRecord(
            name="name_example",
            type="type_example",
            value="value_example",
        ),
    ) # EmailDomain | EmailDomain

    # example passing only required values which don't have defaults set
    try:
        # Update email sending domain
        api_response = api_instance.update_email_sending_domain(domain, email_domain)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->update_email_sending_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  |
 **email_domain** | [**EmailDomain**](EmailDomain.md)| EmailDomain |

### Return type

[**EmailSendingDomainResponse**](EmailSendingDomainResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_settings**
> EmailSettingsResponse update_email_settings(storefront_oid, settings)

Update email settings

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.email_settings import EmailSettings
from ultracart.model.email_settings_response import EmailSettingsResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    settings = EmailSettings(
        marketing_esp_domain_user="marketing_esp_domain_user_example",
        marketing_esp_domain_uuid="marketing_esp_domain_uuid_example",
        marketing_esp_friendly_name="marketing_esp_friendly_name_example",
        postcard_from_address1="postcard_from_address1_example",
        postcard_from_address2="postcard_from_address2_example",
        postcard_from_city="postcard_from_city_example",
        postcard_from_name="postcard_from_name_example",
        postcard_from_postal_code="postcard_from_postal_code_example",
        postcard_from_state="postcard_from_state_example",
        reviews_io_configured=True,
        sms_esp_twilio_uuid="sms_esp_twilio_uuid_example",
        sms_phone_number="sms_phone_number_example",
        transactional_esp_domain_user="transactional_esp_domain_user_example",
        transactional_esp_domain_uuid="transactional_esp_domain_uuid_example",
        transactional_esp_friendly_name="transactional_esp_friendly_name_example",
    ) # EmailSettings | settings request

    # example passing only required values which don't have defaults set
    try:
        # Update email settings
        api_response = api_instance.update_email_settings(storefront_oid, settings)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_experiment**
> ExperimentResponse update_experiment(storefront_oid, storefront_experiment_oid, experiment)

Update experiment

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.experiment_response import ExperimentResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.experiment import Experiment
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    storefront_experiment_oid = 1 # int | 
    experiment = Experiment(
        container_id="container_id_example",
        duration_days=1,
        end_dts="end_dts_example",
        equal_weighting=True,
        experiment_type="experiment_type_example",
        id="id_example",
        name="name_example",
        notes="notes_example",
        objective="objective_example",
        objective_parameter="objective_parameter_example",
        openai_current_iteration=1,
        openai_element_type="headline",
        openai_model="openai_model_example",
        openai_total_iterations=1,
        optimization_type="optimization_type_example",
        p95_sessions_needed=1,
        p_value=3.14,
        session_count=1,
        start_dts="start_dts_example",
        status="Running",
        storefront_experiment_oid=1,
        storefront_oid=1,
        uri="uri_example",
        variations=[
            ExperimentVariation(
                add_to_cart_count=1,
                average_duration_seconds=1,
                average_objective_per_session=3.14,
                average_order_value=3.14,
                bounce_count=1,
                conversion_rate=3.14,
                daily_statistics=[
                    ExperimentVariationStat(
                        add_to_cart_count=1,
                        bounce_count=1,
                        duration_seconds_sum=1,
                        event_count=1,
                        initiate_checkout_count=1,
                        order_count=1,
                        order_item_count=1,
                        page_view_count=1,
                        revenue=3.14,
                        session_count=1,
                        sms_opt_in_count=1,
                        stat_dts="stat_dts_example",
                    ),
                ],
                duration_seconds_sum=1,
                event_count=1,
                initiate_checkout_count=1,
                order_count=1,
                order_item_count=1,
                original_traffic_percentage=3.14,
                page_view_count=1,
                paused=True,
                revenue=3.14,
                session_count=1,
                sms_opt_ins=1,
                traffic_percentage=3.14,
                url="url_example",
                variation_name="variation_name_example",
                variation_number=1,
                winner=True,
            ),
        ],
    ) # Experiment | Experiment

    # example passing only required values which don't have defaults set
    try:
        # Update experiment
        api_response = api_instance.update_experiment(storefront_oid, storefront_experiment_oid, experiment)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_library_item**
> LibraryItemResponse update_library_item(library_item_oid, library_item)

Update library item. Note that only certain fields may be updated via this method.

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.library_item_response import LibraryItemResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.library_item import LibraryItem
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    library_item_oid = 1 # int | 
    library_item = LibraryItem(
        assets=[
            LibraryItemAsset(
                mime_type="mime_type_example",
                url="url_example",
            ),
        ],
        attributes=[
            LibraryItemAttribute(
                name="name_example",
                value="value_example",
            ),
        ],
        categories=[
            "categories_example",
        ],
        content="content_example",
        content_type="content_type_example",
        description="description_example",
        industries=[
            "industries_example",
        ],
        library_item_oid=1,
        merchant_id="merchant_id_example",
        my_purchased_version=1,
        original_object_id="original_object_id_example",
        price=3.14,
        price_formatted="price_formatted_example",
        published=True,
        published_dts={},
        published_from_library_item_oid=1,
        published_meta=LibraryItemPublishedMeta(
            count_of_versions=1,
            library_item_published_oid=1,
            library_item_review_oid=1,
            rejected=True,
            rejected_reason="rejected_reason_example",
            release_version=1,
            review_version=1,
            under_review=True,
        ),
        published_version=1,
        purchased=True,
        purchased_from_library_item_oid=1,
        purchased_meta=LibraryItemPurchasedMeta(
            most_recent_version=1,
            my_purchased_version=1,
            upgrade_available=True,
        ),
        purchased_version=1,
        rejected=True,
        rejected_reason="rejected_reason_example",
        release_notes="release_notes_example",
        release_version=1,
        reviewed=True,
        reviewed_dts={},
        screenshots=[
            LibraryItemScreenshot(
                default_url=True,
                screenshot_url="screenshot_url_example",
            ),
        ],
        share_with_accounts=[
            LibraryItemAccount(
                library_item_account_oid=1,
                library_item_oid=1,
                other_merchant_id="other_merchant_id_example",
            ),
        ],
        share_with_other_emails=[
            LibraryItemEmail(
                email="email_example",
                library_item_email_oid=1,
                library_item_oid=1,
            ),
        ],
        shared=True,
        source=True,
        source_to_library_item_oid=1,
        source_version=1,
        style="style_example",
        times_purchased=1,
        title="title_example",
        type="type_example",
        under_review=True,
    ) # LibraryItem | Library item

    # example passing only required values which don't have defaults set
    try:
        # Update library item. Note that only certain fields may be updated via this method.
        api_response = api_instance.update_library_item(library_item_oid, library_item)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_screen_recording_merchant_notes**
> update_screen_recording_merchant_notes(storefront_oid, screen_recording_uuid, merchant_notes_request)

Update merchant notes on a screen recording

Update merchant notes on a screen recording 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_merchant_notes_request import ScreenRecordingMerchantNotesRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    screen_recording_uuid = "screen_recording_uuid_example" # str | 
    merchant_notes_request = ScreenRecordingMerchantNotesRequest(
        merchant_notes="merchant_notes_example",
    ) # ScreenRecordingMerchantNotesRequest | Merchant Notes

    # example passing only required values which don't have defaults set
    try:
        # Update merchant notes on a screen recording
        api_instance.update_screen_recording_merchant_notes(storefront_oid, screen_recording_uuid, merchant_notes_request)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_screen_recording_segment**
> ScreenRecordingSegmentResponse update_screen_recording_segment(storefront_oid, screen_recording_segment_oid, segment)

Update screen recording segment

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_segment import ScreenRecordingSegment
from ultracart.model.error_response import ErrorResponse
from ultracart.model.screen_recording_segment_response import ScreenRecordingSegmentResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    screen_recording_segment_oid = 1 # int | 
    segment = ScreenRecordingSegment(
        create_dts="create_dts_example",
        description="description_example",
        filter=ScreenRecordingFilter(
            affiliate_email="affiliate_email_example",
            affiliate_id=1,
            communications_campaign_name="communications_campaign_name_example",
            communications_campaign_name_filter=True,
            communications_email_subject="communications_email_subject_example",
            communications_email_subject_filter=True,
            communications_flow_name="communications_flow_name_example",
            communications_flow_name_filter=True,
            email=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            email_domain="email_domain_example",
            email_domain_filter=True,
            email_identified=True,
            end_timestamp=ScreenRecordingFilterRangeDate(
                end="end_example",
                start="start_example",
            ),
            esp_customer_uuid="esp_customer_uuid_example",
            favorite=True,
            geolocation=ScreenRecordingFilterGeoDistance(
                distance=1,
                distance_uom="distance_uom_example",
                from_address="from_address_example",
                lat=3.14,
                lon=3.14,
            ),
            geolocation_country=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            geolocation_country_filter=True,
            geolocation_state=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            geolocation_state_filter=True,
            language_iso_code=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            language_iso_code_filter=True,
            last_x_days=1,
            max_filter_values=1,
            order_id=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            page_view_count=ScreenRecordingFilterRangeInteger(
                eq=1,
                gt=1,
                gte=1,
                lt=1,
                lte=1,
            ),
            page_views=[
                ScreenRecordingFilterPageView(
                    domain=ScreenRecordingFilterStringSearch(
                        does_not_exist=True,
                        exists=True,
                        _is="_is_example",
                        is_not="is_not_example",
                        starts_with="starts_with_example",
                    ),
                    domain_filter=True,
                    event_name_filter=True,
                    event_param_name_filter=True,
                    event_param_value_filter=True,
                    events=[
                        ScreenRecordingFilterPageViewEvent(
                            event_name="event_name_example",
                            event_params=[
                                ScreenRecordingFilterPageViewEventParam(
                                    name="name_example",
                                    value_bd=ScreenRecordingFilterRangeBigDecimal(
                                        eq=3.14,
                                        gt=3.14,
                                        gte=3.14,
                                        lt=3.14,
                                        lte=3.14,
                                    ),
                                    value_bool=True,
                                    value_num=ScreenRecordingFilterRangeInteger(
                                        eq=1,
                                        gt=1,
                                        gte=1,
                                        lt=1,
                                        lte=1,
                                    ),
                                    value_text=ScreenRecordingFilterStringSearch(
                                        does_not_exist=True,
                                        exists=True,
                                        _is="_is_example",
                                        is_not="is_not_example",
                                        starts_with="starts_with_example",
                                    ),
                                ),
                            ],
                        ),
                    ],
                    param_name_filter=True,
                    param_value_filter=True,
                    params=[
                        ScreenRecordingFilterPageViewParam(
                            name="name_example",
                            value=ScreenRecordingFilterStringSearch(
                                does_not_exist=True,
                                exists=True,
                                _is="_is_example",
                                is_not="is_not_example",
                                starts_with="starts_with_example",
                            ),
                        ),
                    ],
                    referrer=ScreenRecordingFilterStringSearch(
                        does_not_exist=True,
                        exists=True,
                        _is="_is_example",
                        is_not="is_not_example",
                        starts_with="starts_with_example",
                    ),
                    referrer_params=[
                        ScreenRecordingFilterPageViewReferrerParam(
                            name="name_example",
                            value=ScreenRecordingFilterStringSearch(
                                does_not_exist=True,
                                exists=True,
                                _is="_is_example",
                                is_not="is_not_example",
                                starts_with="starts_with_example",
                            ),
                        ),
                    ],
                    referrer_raw=ScreenRecordingFilterStringSearch(
                        does_not_exist=True,
                        exists=True,
                        _is="_is_example",
                        is_not="is_not_example",
                        starts_with="starts_with_example",
                    ),
                    time_on_page=ScreenRecordingFilterRangeInteger(
                        eq=1,
                        gt=1,
                        gte=1,
                        lt=1,
                        lte=1,
                    ),
                    time_on_page_max_filter=True,
                    time_on_page_min_filter=True,
                    url=ScreenRecordingFilterStringSearch(
                        does_not_exist=True,
                        exists=True,
                        _is="_is_example",
                        is_not="is_not_example",
                        starts_with="starts_with_example",
                    ),
                    url_filter=True,
                ),
            ],
            placed_order=True,
            preferred_language=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            preferred_language_filter=True,
            referrer_domain="referrer_domain_example",
            referrer_domain_filter=True,
            screen_recording_uuids=[
                "screen_recording_uuids_example",
            ],
            screen_sizes=[
                "screen_sizes_example",
            ],
            skip_filter_values=True,
            skip_histogram=True,
            skip_hits=True,
            start_timestamp=ScreenRecordingFilterRangeDate(
                end="end_example",
                start="start_example",
            ),
            tags=[
                "tags_example",
            ],
            time_on_site=ScreenRecordingFilterRangeInteger(
                eq=1,
                gt=1,
                gte=1,
                lt=1,
                lte=1,
            ),
            time_on_site_max_filter=True,
            time_on_site_min_filter=True,
            url_filter=True,
            user_agent_device_name="user_agent_device_name_example",
            user_agent_device_name_filter=True,
            user_agent_device_os_name_filter=True,
            user_agent_device_os_version_filter=True,
            user_agent_name="user_agent_name_example",
            user_agent_name_filter=True,
            user_agent_original=ScreenRecordingFilterStringSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
                starts_with="starts_with_example",
            ),
            user_agent_original_filter=True,
            user_agent_os_name="user_agent_os_name_example",
            user_agent_os_version="user_agent_os_version_example",
            user_ip=ScreenRecordingFilterIpSearch(
                does_not_exist=True,
                exists=True,
                _is="_is_example",
                is_not="is_not_example",
            ),
            utm_campaign="utm_campaign_example",
            utm_campaign_filter=True,
            utm_source="utm_source_example",
            utm_source_filter=True,
            visitor_number=1,
            watched=True,
        ),
        histogram_data=[
            1,
        ],
        histogram_interval="histogram_interval_example",
        histogram_start_dts="histogram_start_dts_example",
        name="name_example",
        screen_recording_segment_oid=1,
        session_count=1,
        session_count_last_update_dts="session_count_last_update_dts_example",
    ) # ScreenRecordingSegment | Segment

    # example passing only required values which don't have defaults set
    try:
        # Update screen recording segment
        api_response = api_instance.update_screen_recording_segment(storefront_oid, screen_recording_segment_oid, segment)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_screen_recording_settings**
> ScreenRecordingSettingsResponse update_screen_recording_settings(storefront_oid, settings)

Update screen recording settings

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.screen_recording_settings import ScreenRecordingSettings
from ultracart.model.screen_recording_settings_response import ScreenRecordingSettingsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    settings = ScreenRecordingSettings(
        cost_per_thousand=3.14,
        enabled=True,
        retention_interval="retention_interval_example",
        sessions_current_billing_period=1,
        sessions_last_billing_period=1,
        sessions_trial_billing_period=1,
        trial_expiration="trial_expiration_example",
        trial_expired=True,
    ) # ScreenRecordingSettings | Settings

    # example passing only required values which don't have defaults set
    try:
        # Update screen recording settings
        api_response = api_instance.update_screen_recording_settings(storefront_oid, settings)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_screen_recording_tags**
> update_screen_recording_tags(storefront_oid, screen_recording_uuid, tags)

Update tags on a screen recording

Update tags on a screen recording 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.screen_recording_tags_request import ScreenRecordingTagsRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    screen_recording_uuid = "screen_recording_uuid_example" # str | 
    tags = ScreenRecordingTagsRequest(
        tags=[
            "tags_example",
        ],
    ) # ScreenRecordingTagsRequest | Tags

    # example passing only required values which don't have defaults set
    try:
        # Update tags on a screen recording
        api_instance.update_screen_recording_tags(storefront_oid, screen_recording_uuid, tags)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction_email**
> TransactionEmailResponse update_transaction_email(storefront_oid, email_id, transaction_email)

Updates a transaction email object

Updates a transactional email 

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.transaction_email_response import TransactionEmailResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.transaction_email import TransactionEmail
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    storefront_oid = 1 # int | 
    email_id = "email_id_example" # str | 
    transaction_email = TransactionEmail(
        content="content_example",
        esp_domain_uuid="esp_domain_uuid_example",
        esp_friendly_name="esp_friendly_name_example",
        esp_user="esp_user_example",
        file_exists=True,
        file_name="file_name_example",
        group="group_example",
        handlebar_variables=[
            "handlebar_variables_example",
        ],
        invalid=True,
        last_modified="last_modified_example",
        library_item_oid=1,
        options=[
            TransactionEmailOption(
                description="description_example",
                merchant_email_delivery_option_oid=1,
                merchant_id="merchant_id_example",
                name="name_example",
                selected=True,
                store_front_oid=1,
                template_display="template_display_example",
                template_type="template_type_example",
            ),
        ],
        path="path_example",
        size="size_example",
        store_front_fs_directory_oid=1,
        store_front_fs_file_oid=1,
        subject="subject_example",
        syntax_errors="syntax_errors_example",
        template_path_relative_path="template_path_relative_path_example",
        theme_relative_path="theme_relative_path_example",
    ) # TransactionEmail | TransactionEmail

    # example passing only required values which don't have defaults set
    try:
        # Updates a transaction email object
        api_response = api_instance.update_transaction_email(storefront_oid, email_id, transaction_email)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_twilio_account**
> TwilioResponse update_twilio_account(esp_twilio_uuid, twilio)

Update Twilio account

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.twilio_response import TwilioResponse
from ultracart.model.twilio import Twilio
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    esp_twilio_uuid = "esp_twilio_uuid_example" # str | 
    twilio = Twilio(
        account_sid="account_sid_example",
        auth_token="auth_token_example",
        esp_twilio_uuid="esp_twilio_uuid_example",
        phone_numbers=[
            "phone_numbers_example",
        ],
    ) # Twilio | Twilio

    # example passing only required values which don't have defaults set
    try:
        # Update Twilio account
        api_response = api_instance.update_twilio_account(esp_twilio_uuid, twilio)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_fs_file**
> upload_fs_file(id, upload_request)

This is the last step in uploading a file after 1) calling getUploadFsFileUrl and 2) uploading a file to the provided url, then finally 3) calling this method and providing the key to trigger the server into reading the S3 bucket and retrieving the file.

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.file_manager_upload_request import FileManagerUploadRequest
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    id = 1 # int | 
    upload_request = FileManagerUploadRequest(
        filename="filename_example",
        key="key_example",
        parent_storefront_fs_directory_oid=1,
    ) # FileManagerUploadRequest | UploadRequest

    # example passing only required values which don't have defaults set
    try:
        # This is the last step in uploading a file after 1) calling getUploadFsFileUrl and 2) uploading a file to the provided url, then finally 3) calling this method and providing the key to trigger the server into reading the S3 bucket and retrieving the file.
        api_instance.upload_fs_file(id, upload_request)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->upload_fs_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **upload_request** | [**FileManagerUploadRequest**](FileManagerUploadRequest.md)| UploadRequest |

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_ruler**
> RulerValidationResponse validate_ruler(ruler_validate_request)

Validate AWS Event Ruler

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import storefront_api
from ultracart.model.ruler_validation_response import RulerValidationResponse
from ultracart.model.error_response import ErrorResponse
from ultracart.model.ruler_validation_request import RulerValidationRequest
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    ruler_validate_request = RulerValidationRequest(
        ruler="ruler_example",
    ) # RulerValidationRequest | Ruler Validate Request

    # example passing only required values which don't have defaults set
    try:
        # Validate AWS Event Ruler
        api_response = api_instance.validate_ruler(ruler_validate_request)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling StorefrontApi->validate_ruler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruler_validate_request** | [**RulerValidationRequest**](RulerValidationRequest.md)| Ruler Validate Request |

### Return type

[**RulerValidationResponse**](RulerValidationResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

