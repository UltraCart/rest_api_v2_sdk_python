# ultracart.SfvbApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_sfvb_page_blog_posts**](SfvbApi.md#add_sfvb_page_blog_posts) | **POST** /sfvb/storefronts/{storefront_oid}/pages/blog_posts/add | Assign blog posts to a page
[**add_sfvb_page_items**](SfvbApi.md#add_sfvb_page_items) | **POST** /sfvb/storefronts/{storefront_oid}/pages/items/add | Assign items to a page
[**archive_sfvb_campaign**](SfvbApi.md#archive_sfvb_campaign) | **PUT** /sfvb/storefronts/{storefront_oid}/campaigns/{campaign_uuid}/archive | Archive or unarchive a campaign
[**archive_sfvb_comms_list**](SfvbApi.md#archive_sfvb_comms_list) | **PUT** /sfvb/storefronts/{storefront_oid}/lists/{list_uuid}/archive | Archive an email list
[**archive_sfvb_comms_segment**](SfvbApi.md#archive_sfvb_comms_segment) | **PUT** /sfvb/storefronts/{storefront_oid}/segments/{segment_uuid}/archive | Archive a segment
[**archive_sfvb_flow**](SfvbApi.md#archive_sfvb_flow) | **PUT** /sfvb/storefronts/{storefront_oid}/flows/{flow_uuid}/archive | Archive or unarchive a flow
[**archive_sfvb_upsell_path**](SfvbApi.md#archive_sfvb_upsell_path) | **POST** /sfvb/storefronts/{storefront_oid}/upsell_paths/{upsell_path_oid}/archive | Archive an upsell path
[**attach_sfvb_blog_post_image**](SfvbApi.md#attach_sfvb_blog_post_image) | **POST** /sfvb/storefronts/{storefront_oid}/blog_posts/{blog_post_oid}/images/attach | Attach an image to a blog post
[**check_sfvb_redirect**](SfvbApi.md#check_sfvb_redirect) | **POST** /sfvb/storefronts/{storefront_oid}/redirects/check | Check a redirect rule without creating it
[**clear_sfvb_library_screenshot**](SfvbApi.md#clear_sfvb_library_screenshot) | **DELETE** /sfvb/storefronts/{storefront_oid}/library/{library_oid}/screenshot | Remove a library entry&#39;s screenshot
[**clone_sfvb_campaign**](SfvbApi.md#clone_sfvb_campaign) | **POST** /sfvb/storefronts/{storefront_oid}/campaigns/{campaign_uuid}/clone | Copy a campaign on the same storefront
[**clone_sfvb_flow**](SfvbApi.md#clone_sfvb_flow) | **POST** /sfvb/storefronts/{storefront_oid}/flows/{flow_uuid}/clone | Copy a flow on the same storefront
[**compile_sfvb_cjson**](SfvbApi.md#compile_sfvb_cjson) | **POST** /sfvb/cjson/compile | Compile CJSON to Velocity
[**create_sfvb_campaign**](SfvbApi.md#create_sfvb_campaign) | **POST** /sfvb/storefronts/{storefront_oid}/campaigns | Create a draft campaign
[**create_sfvb_flow**](SfvbApi.md#create_sfvb_flow) | **POST** /sfvb/storefronts/{storefront_oid}/flows | Create a draft flow
[**create_sfvb_library_entry**](SfvbApi.md#create_sfvb_library_entry) | **POST** /sfvb/storefronts/{storefront_oid}/library | Save a fragment to the library
[**create_sfvb_preview_access**](SfvbApi.md#create_sfvb_preview_access) | **POST** /sfvb/storefronts/{storefront_oid}/preview_access | One time link that opens a preview in a browser with no UltraCart login
[**create_sfvb_preview_session**](SfvbApi.md#create_sfvb_preview_session) | **POST** /sfvb/storefronts/{storefront_oid}/preview_sessions | Create a preview session
[**delete_sfvb_affiliate_network**](SfvbApi.md#delete_sfvb_affiliate_network) | **DELETE** /sfvb/storefronts/{storefront_oid}/tracking/affiliate_networks/{affiliate_network_oid} | Delete an affiliate network
[**delete_sfvb_approval**](SfvbApi.md#delete_sfvb_approval) | **DELETE** /sfvb/approvals/{approval_id} | Cancel a pending approval request
[**delete_sfvb_blog_post**](SfvbApi.md#delete_sfvb_blog_post) | **DELETE** /sfvb/storefronts/{storefront_oid}/blog_posts/{blog_post_oid} | Delete a blog post
[**delete_sfvb_comms_folder**](SfvbApi.md#delete_sfvb_comms_folder) | **DELETE** /sfvb/storefronts/{storefront_oid}/list_segment_folders/{folder_uuid} | Delete a list and segment folder
[**delete_sfvb_comms_sending_domain**](SfvbApi.md#delete_sfvb_comms_sending_domain) | **DELETE** /sfvb/comms/sending_domains/{domain} | Remove a sending domain
[**delete_sfvb_comms_twilio_account**](SfvbApi.md#delete_sfvb_comms_twilio_account) | **DELETE** /sfvb/comms/twilio_account | Remove the Twilio account
[**delete_sfvb_file**](SfvbApi.md#delete_sfvb_file) | **DELETE** /sfvb/storefronts/{storefront_oid}/files | Delete a storefront file
[**delete_sfvb_item_attribute**](SfvbApi.md#delete_sfvb_item_attribute) | **DELETE** /sfvb/storefronts/{storefront_oid}/items/attributes | Delete an attribute from an item
[**delete_sfvb_item_multimedia**](SfvbApi.md#delete_sfvb_item_multimedia) | **DELETE** /sfvb/storefronts/{storefront_oid}/items/multimedia | Detach an image from an item
[**delete_sfvb_library_entry**](SfvbApi.md#delete_sfvb_library_entry) | **DELETE** /sfvb/storefronts/{storefront_oid}/library/{library_oid} | Delete or retire a library entry
[**delete_sfvb_not_found_entry**](SfvbApi.md#delete_sfvb_not_found_entry) | **DELETE** /sfvb/storefronts/{storefront_oid}/not_found/{not_found_id} | Remove a 404 path from the log
[**delete_sfvb_page_multimedia**](SfvbApi.md#delete_sfvb_page_multimedia) | **DELETE** /sfvb/storefronts/{storefront_oid}/pages/multimedia | Detach an image from a page
[**delete_sfvb_preview_session**](SfvbApi.md#delete_sfvb_preview_session) | **DELETE** /sfvb/storefronts/{storefront_oid}/preview_sessions/{preview_session_id} | Delete a preview session
[**delete_sfvb_redirect**](SfvbApi.md#delete_sfvb_redirect) | **DELETE** /sfvb/storefronts/{storefront_oid}/redirects/{redirect_id} | Delete a redirect rule
[**delete_sfvb_redirects**](SfvbApi.md#delete_sfvb_redirects) | **POST** /sfvb/storefronts/{storefront_oid}/redirects/delete | Delete up to 5,000 redirect rules in one call
[**delete_sfvb_secret_request**](SfvbApi.md#delete_sfvb_secret_request) | **DELETE** /sfvb/secrets/{request_id} | Cancel a pending secret request
[**delete_sfvb_sequence_step**](SfvbApi.md#delete_sfvb_sequence_step) | **DELETE** /sfvb/storefronts/{storefront_oid}/sequences/{sequence_uuid}/steps/{step_uuid} | Remove one step
[**delete_sfvb_smart_attribution**](SfvbApi.md#delete_sfvb_smart_attribution) | **DELETE** /sfvb/storefronts/{storefront_oid}/smart_attribution | Delete a storefront&#39;s Smart Attribution configuration
[**delete_sfvb_tracking_provider**](SfvbApi.md#delete_sfvb_tracking_provider) | **DELETE** /sfvb/storefronts/{storefront_oid}/tracking/providers/{provider} | Clear one tracking provider
[**delete_sfvb_utm_shortcode**](SfvbApi.md#delete_sfvb_utm_shortcode) | **DELETE** /sfvb/storefronts/{storefront_oid}/utm_shortcodes/{shortcode_oid} | Delete a UTM shortcode
[**detach_sfvb_blog_post_image**](SfvbApi.md#detach_sfvb_blog_post_image) | **POST** /sfvb/storefronts/{storefront_oid}/blog_posts/{blog_post_oid}/images/detach | Detach an image from a blog post
[**disable_sfvb_i18n_language**](SfvbApi.md#disable_sfvb_i18n_language) | **POST** /sfvb/storefronts/{storefront_oid}/i18n/languages/{code}/disable | Disable a language
[**disable_sfvb_upsell_offer**](SfvbApi.md#disable_sfvb_upsell_offer) | **POST** /sfvb/storefronts/{storefront_oid}/upsell_offers/{upsell_offer_oid}/disable | Disable an upsell offer
[**disable_sfvb_upsell_path**](SfvbApi.md#disable_sfvb_upsell_path) | **POST** /sfvb/storefronts/{storefront_oid}/upsell_paths/{upsell_path_oid}/disable | Disable an upsell path
[**download_sfvb_file**](SfvbApi.md#download_sfvb_file) | **GET** /sfvb/storefronts/{storefront_oid}/files/download | Read a storefront file&#39;s raw bytes
[**dry_run_sfvb_item_attribute_batch**](SfvbApi.md#dry_run_sfvb_item_attribute_batch) | **POST** /sfvb/storefronts/{storefront_oid}/items/attributes/batch/dry_run | Check attribute changes across many items without writing them
[**dry_run_sfvb_redirect_delete**](SfvbApi.md#dry_run_sfvb_redirect_delete) | **POST** /sfvb/storefronts/{storefront_oid}/redirects/delete/dry_run | Check a batch delete of redirect rules without writing it
[**dry_run_sfvb_redirect_import**](SfvbApi.md#dry_run_sfvb_redirect_import) | **POST** /sfvb/storefronts/{storefront_oid}/redirects/import/dry_run | Check a redirect import without writing it
[**duplicate_sfvb_library_entry**](SfvbApi.md#duplicate_sfvb_library_entry) | **POST** /sfvb/storefronts/{storefront_oid}/library/{library_oid}/duplicate | Copy a library entry into a new private entry
[**duplicate_sfvb_page**](SfvbApi.md#duplicate_sfvb_page) | **POST** /sfvb/storefronts/{storefront_oid}/pages/duplicate | Copy a page to a new path
[**duplicate_sfvb_theme**](SfvbApi.md#duplicate_sfvb_theme) | **POST** /sfvb/storefronts/{storefront_oid}/themes/{theme_oid}/duplicate | Duplicate a theme
[**duplicate_sfvb_upsell_offer**](SfvbApi.md#duplicate_sfvb_upsell_offer) | **POST** /sfvb/storefronts/{storefront_oid}/upsell_offers/{upsell_offer_oid}/duplicate | Duplicate an upsell offer
[**duplicate_sfvb_upsell_path**](SfvbApi.md#duplicate_sfvb_upsell_path) | **POST** /sfvb/storefronts/{storefront_oid}/upsell_paths/{upsell_path_oid}/duplicate | Duplicate an upsell path or one of its variations
[**enable_sfvb_i18n_language**](SfvbApi.md#enable_sfvb_i18n_language) | **POST** /sfvb/storefronts/{storefront_oid}/i18n/languages/{code}/enable | Enable a language
[**enable_sfvb_smart_attribution**](SfvbApi.md#enable_sfvb_smart_attribution) | **POST** /sfvb/storefronts/{storefront_oid}/smart_attribution/enable | Turn Smart Attribution on in report_only mode
[**enable_sfvb_upsell_offer**](SfvbApi.md#enable_sfvb_upsell_offer) | **POST** /sfvb/storefronts/{storefront_oid}/upsell_offers/{upsell_offer_oid}/enable | Enable an upsell offer
[**enable_sfvb_upsell_path**](SfvbApi.md#enable_sfvb_upsell_path) | **POST** /sfvb/storefronts/{storefront_oid}/upsell_paths/{upsell_path_oid}/enable | Enable an upsell path
[**end_sfvb_experiment**](SfvbApi.md#end_sfvb_experiment) | **POST** /sfvb/storefronts/{storefront_oid}/experiments/{experiment_oid}/end | End an experiment
[**export_sfvb_not_found**](SfvbApi.md#export_sfvb_not_found) | **GET** /sfvb/storefronts/{storefront_oid}/not_found/export | Export the open 404 paths
[**favorite_sfvb_library_entry**](SfvbApi.md#favorite_sfvb_library_entry) | **PUT** /sfvb/storefronts/{storefront_oid}/library/{library_oid}/favorite | Favorite a library entry
[**fix_sfvb_not_found_entry**](SfvbApi.md#fix_sfvb_not_found_entry) | **POST** /sfvb/storefronts/{storefront_oid}/not_found/{not_found_id}/fixed | Mark a 404 path fixed
[**get_sfvb_affiliate_network**](SfvbApi.md#get_sfvb_affiliate_network) | **GET** /sfvb/storefronts/{storefront_oid}/tracking/affiliate_networks/{affiliate_network_oid} | Read one affiliate network
[**get_sfvb_affiliate_networks**](SfvbApi.md#get_sfvb_affiliate_networks) | **GET** /sfvb/storefronts/{storefront_oid}/tracking/affiliate_networks | List a storefront&#39;s affiliate networks
[**get_sfvb_approval**](SfvbApi.md#get_sfvb_approval) | **GET** /sfvb/approvals/{approval_id} | Read one approval request
[**get_sfvb_approvals**](SfvbApi.md#get_sfvb_approvals) | **GET** /sfvb/approvals | List this sign-in&#39;s approval requests
[**get_sfvb_blog_post**](SfvbApi.md#get_sfvb_blog_post) | **GET** /sfvb/storefronts/{storefront_oid}/blog_posts/{blog_post_oid} | Read a blog post
[**get_sfvb_campaign**](SfvbApi.md#get_sfvb_campaign) | **GET** /sfvb/storefronts/{storefront_oid}/campaigns/{campaign_uuid} | Get a campaign
[**get_sfvb_cjson_used_elements**](SfvbApi.md#get_sfvb_cjson_used_elements) | **POST** /sfvb/cjson/elements | Element types used by a container
[**get_sfvb_comms_dashboard_stats**](SfvbApi.md#get_sfvb_comms_dashboard_stats) | **GET** /sfvb/storefronts/{storefront_oid}/comms/stats/dashboard | Read every flow&#39;s and campaign&#39;s counts over a window, with the account&#39;s daily sending
[**get_sfvb_comms_email_clicks**](SfvbApi.md#get_sfvb_comms_email_clicks) | **GET** /sfvb/storefronts/{storefront_oid}/comms/sequences/{commseq_uuid}/emails/{email_uuid}/clicks | Read each link in one email and how often it was clicked
[**get_sfvb_comms_folder**](SfvbApi.md#get_sfvb_comms_folder) | **GET** /sfvb/storefronts/{storefront_oid}/list_segment_folders/{folder_uuid} | Read one list and segment folder
[**get_sfvb_comms_folders**](SfvbApi.md#get_sfvb_comms_folders) | **GET** /sfvb/storefronts/{storefront_oid}/list_segment_folders | List the list and segment folders
[**get_sfvb_comms_list**](SfvbApi.md#get_sfvb_comms_list) | **GET** /sfvb/storefronts/{storefront_oid}/lists/{list_uuid} | Read one email list
[**get_sfvb_comms_list_members**](SfvbApi.md#get_sfvb_comms_list_members) | **GET** /sfvb/storefronts/{storefront_oid}/lists/{list_uuid}/members | Read one page of a list&#39;s members
[**get_sfvb_comms_plan**](SfvbApi.md#get_sfvb_comms_plan) | **GET** /sfvb/storefronts/{storefront_oid}/comms/plan | Read the account&#39;s communications plan and sending health
[**get_sfvb_comms_providers**](SfvbApi.md#get_sfvb_comms_providers) | **GET** /sfvb/storefronts/{storefront_oid}/comms/providers | List the email providers the account can import lists from
[**get_sfvb_comms_segment**](SfvbApi.md#get_sfvb_comms_segment) | **GET** /sfvb/storefronts/{storefront_oid}/segments/{segment_uuid} | Read one segment, with its rule
[**get_sfvb_comms_segment_members**](SfvbApi.md#get_sfvb_comms_segment_members) | **GET** /sfvb/storefronts/{storefront_oid}/segments/{segment_uuid}/members | Read one page of a segment&#39;s members
[**get_sfvb_comms_sending_domain**](SfvbApi.md#get_sfvb_comms_sending_domain) | **GET** /sfvb/comms/sending_domains/{domain} | Read a sending domain
[**get_sfvb_comms_sending_domains**](SfvbApi.md#get_sfvb_comms_sending_domains) | **GET** /sfvb/comms/sending_domains | List the sending domains
[**get_sfvb_comms_sequence_stats**](SfvbApi.md#get_sfvb_comms_sequence_stats) | **GET** /sfvb/storefronts/{storefront_oid}/comms/sequences/{commseq_uuid}/stats | Read a flow&#39;s or campaign&#39;s counts, overall and step by step
[**get_sfvb_comms_settings**](SfvbApi.md#get_sfvb_comms_settings) | **GET** /sfvb/storefronts/{storefront_oid}/comms/settings | Read a storefront&#39;s communications settings
[**get_sfvb_comms_template**](SfvbApi.md#get_sfvb_comms_template) | **GET** /sfvb/storefronts/{storefront_oid}/comms/templates/{email_template_oid} | Read one saved email template&#39;s body
[**get_sfvb_comms_templates**](SfvbApi.md#get_sfvb_comms_templates) | **GET** /sfvb/storefronts/{storefront_oid}/comms/templates | List the email templates a new email can start from
[**get_sfvb_comms_twilio_account**](SfvbApi.md#get_sfvb_comms_twilio_account) | **GET** /sfvb/comms/twilio_account | Read the Twilio account
[**get_sfvb_container**](SfvbApi.md#get_sfvb_container) | **GET** /sfvb/storefronts/{storefront_oid}/containers/{owner_type}/{owner_object_id} | Read a container stored outside the file system
[**get_sfvb_container_version**](SfvbApi.md#get_sfvb_container_version) | **GET** /sfvb/storefronts/{storefront_oid}/container_versions/{container_history_oid} | Read the CJSON stored in one container history entry
[**get_sfvb_element**](SfvbApi.md#get_sfvb_element) | **GET** /sfvb/elements/{element_type} | Configuration schema and field card for one element type
[**get_sfvb_email**](SfvbApi.md#get_sfvb_email) | **GET** /sfvb/storefronts/{storefront_oid}/emails/{email_uuid} | Get a flow or campaign email&#39;s subject and preview text
[**get_sfvb_events**](SfvbApi.md#get_sfvb_events) | **GET** /sfvb/events | Replay events
[**get_sfvb_events_authorization**](SfvbApi.md#get_sfvb_events_authorization) | **PUT** /sfvb/events/auth | Open the event stream
[**get_sfvb_experiment**](SfvbApi.md#get_sfvb_experiment) | **GET** /sfvb/storefronts/{storefront_oid}/experiments/{experiment_oid} | Read one experiment and its statistics
[**get_sfvb_experiment_objectives**](SfvbApi.md#get_sfvb_experiment_objectives) | **GET** /sfvb/storefronts/{storefront_oid}/experiments/objectives | List the objectives an experiment can optimize
[**get_sfvb_file_content**](SfvbApi.md#get_sfvb_file_content) | **GET** /sfvb/storefronts/{storefront_oid}/files/content | Read a storefront file
[**get_sfvb_file_upload_url**](SfvbApi.md#get_sfvb_file_upload_url) | **GET** /sfvb/storefronts/{storefront_oid}/files/upload_url/{extension} | Get a URL to upload a binary asset to
[**get_sfvb_flow**](SfvbApi.md#get_sfvb_flow) | **GET** /sfvb/storefronts/{storefront_oid}/flows/{flow_uuid} | Get a flow
[**get_sfvb_i18n_glossary**](SfvbApi.md#get_sfvb_i18n_glossary) | **GET** /sfvb/storefronts/{storefront_oid}/i18n/glossary | Read the storefront&#39;s translation glossary
[**get_sfvb_i18n_languages**](SfvbApi.md#get_sfvb_i18n_languages) | **GET** /sfvb/storefronts/{storefront_oid}/i18n/languages | List a storefront&#39;s languages
[**get_sfvb_i18n_machine_translations**](SfvbApi.md#get_sfvb_i18n_machine_translations) | **GET** /sfvb/storefronts/{storefront_oid}/i18n/machine_translations | Read where a widget setting&#39;s translations come from
[**get_sfvb_i18n_message**](SfvbApi.md#get_sfvb_i18n_message) | **GET** /sfvb/storefronts/{storefront_oid}/i18n/messages/{key} | Read one built-in message
[**get_sfvb_i18n_message_machine_translations**](SfvbApi.md#get_sfvb_i18n_message_machine_translations) | **GET** /sfvb/storefronts/{storefront_oid}/i18n/messages/{key}/machine_translations | Read where a message&#39;s translations come from
[**get_sfvb_item**](SfvbApi.md#get_sfvb_item) | **GET** /sfvb/storefronts/{storefront_oid}/items | Read an item&#39;s storefront facing content
[**get_sfvb_item_pricing**](SfvbApi.md#get_sfvb_item_pricing) | **GET** /sfvb/storefronts/{storefront_oid}/items/pricing | Read what an item charges
[**get_sfvb_item_related**](SfvbApi.md#get_sfvb_item_related) | **GET** /sfvb/storefronts/{storefront_oid}/items/related | Read an item&#39;s related items
[**get_sfvb_library_entry**](SfvbApi.md#get_sfvb_library_entry) | **GET** /sfvb/storefronts/{storefront_oid}/library/{library_oid} | Read one library entry including its CJSON
[**get_sfvb_library_history**](SfvbApi.md#get_sfvb_library_history) | **GET** /sfvb/storefronts/{storefront_oid}/library/{library_oid}/history | List a library entry&#39;s published revisions
[**get_sfvb_library_share_targets**](SfvbApi.md#get_sfvb_library_share_targets) | **GET** /sfvb/storefronts/{storefront_oid}/library/share_targets | List the accounts a library entry can be shared with
[**get_sfvb_library_taxonomy**](SfvbApi.md#get_sfvb_library_taxonomy) | **GET** /sfvb/storefronts/{storefront_oid}/library/taxonomy | List the allowed library tags
[**get_sfvb_menu**](SfvbApi.md#get_sfvb_menu) | **GET** /sfvb/storefronts/{storefront_oid}/menus/{code} | Read one store menu and its entries
[**get_sfvb_menus**](SfvbApi.md#get_sfvb_menus) | **GET** /sfvb/storefronts/{storefront_oid}/menus | List a storefront&#39;s store menus
[**get_sfvb_not_found**](SfvbApi.md#get_sfvb_not_found) | **GET** /sfvb/storefronts/{storefront_oid}/not_found | List the paths that answered 404
[**get_sfvb_not_found_entry**](SfvbApi.md#get_sfvb_not_found_entry) | **GET** /sfvb/storefronts/{storefront_oid}/not_found/{not_found_id} | Read one 404 path with its recent hits
[**get_sfvb_not_found_page**](SfvbApi.md#get_sfvb_not_found_page) | **GET** /sfvb/storefronts/{storefront_oid}/not_found_page | What renders the storefront&#39;s 404 page
[**get_sfvb_not_found_summary**](SfvbApi.md#get_sfvb_not_found_summary) | **GET** /sfvb/storefronts/{storefront_oid}/not_found/summary | The 404 log&#39;s trend
[**get_sfvb_page**](SfvbApi.md#get_sfvb_page) | **GET** /sfvb/storefronts/{storefront_oid}/pages | Read a page&#39;s attributes and images
[**get_sfvb_page_blog_posts**](SfvbApi.md#get_sfvb_page_blog_posts) | **GET** /sfvb/storefronts/{storefront_oid}/pages/blog_posts | Read the blog posts assigned to a page
[**get_sfvb_page_items**](SfvbApi.md#get_sfvb_page_items) | **GET** /sfvb/storefronts/{storefront_oid}/pages/items | Read the items assigned to a page
[**get_sfvb_page_selectors**](SfvbApi.md#get_sfvb_page_selectors) | **GET** /sfvb/storefronts/{storefront_oid}/pages/selectors | Read a page&#39;s selectors
[**get_sfvb_postcard_tracking**](SfvbApi.md#get_sfvb_postcard_tracking) | **GET** /sfvb/storefronts/{storefront_oid}/postcards/{postcard_uuid}/tracking | Read one page of the cards mailed for a postcard
[**get_sfvb_preview_url**](SfvbApi.md#get_sfvb_preview_url) | **GET** /sfvb/storefronts/{storefront_oid}/preview_sessions/{preview_session_id}/url | URL that renders a preview session
[**get_sfvb_recording**](SfvbApi.md#get_sfvb_recording) | **GET** /sfvb/storefronts/{storefront_oid}/recordings/{screen_recording_uuid} | Get a screen recording
[**get_sfvb_recording_page_view_events**](SfvbApi.md#get_sfvb_recording_page_view_events) | **GET** /sfvb/storefronts/{storefront_oid}/recordings/{screen_recording_uuid}/page_views/{screen_recording_page_view_uuid}/events | Get one recorded page view&#39;s replay events
[**get_sfvb_recording_settings**](SfvbApi.md#get_sfvb_recording_settings) | **GET** /sfvb/storefronts/{storefront_oid}/recording_settings | Get the storefront&#39;s screen recording settings
[**get_sfvb_redirect**](SfvbApi.md#get_sfvb_redirect) | **GET** /sfvb/storefronts/{storefront_oid}/redirects/{redirect_id} | Read one redirect rule
[**get_sfvb_redirects**](SfvbApi.md#get_sfvb_redirects) | **GET** /sfvb/storefronts/{storefront_oid}/redirects | List the storefront&#39;s redirect rules
[**get_sfvb_secret_kinds**](SfvbApi.md#get_sfvb_secret_kinds) | **GET** /sfvb/secrets/kinds | List the secrets this server collects
[**get_sfvb_secret_request**](SfvbApi.md#get_sfvb_secret_request) | **GET** /sfvb/secrets/{request_id} | Read one secret request
[**get_sfvb_secret_requests**](SfvbApi.md#get_sfvb_secret_requests) | **GET** /sfvb/secrets | List this sign-in&#39;s secret requests
[**get_sfvb_sequence**](SfvbApi.md#get_sfvb_sequence) | **GET** /sfvb/storefronts/{storefront_oid}/sequences/{sequence_uuid} | Get a campaign&#39;s or flow&#39;s steps as a tree
[**get_sfvb_sequence_step_dispatch_logs**](SfvbApi.md#get_sfvb_sequence_step_dispatch_logs) | **GET** /sfvb/storefronts/{storefront_oid}/sequences/{sequence_uuid}/steps/{step_uuid}/dispatch_logs | Read a flow or campaign step&#39;s dispatch log and counts
[**get_sfvb_server_log**](SfvbApi.md#get_sfvb_server_log) | **GET** /sfvb/storefronts/{storefront_oid}/logs/{log_id} | Get one storefront render log
[**get_sfvb_site_attributes**](SfvbApi.md#get_sfvb_site_attributes) | **GET** /sfvb/storefronts/{storefront_oid}/attributes | Read a storefront&#39;s site attributes
[**get_sfvb_site_seo**](SfvbApi.md#get_sfvb_site_seo) | **GET** /sfvb/storefronts/{storefront_oid}/seo | Read a storefront&#39;s search engine settings
[**get_sfvb_sitemaps**](SfvbApi.md#get_sfvb_sitemaps) | **GET** /sfvb/storefronts/{storefront_oid}/sitemaps | Read a storefront&#39;s sitemaps and robots.txt
[**get_sfvb_smart_attribution**](SfvbApi.md#get_sfvb_smart_attribution) | **GET** /sfvb/storefronts/{storefront_oid}/smart_attribution | Read a storefront&#39;s Smart Attribution configuration
[**get_sfvb_test_orders**](SfvbApi.md#get_sfvb_test_orders) | **GET** /sfvb/storefronts/{storefront_oid}/test_orders | List recent test orders
[**get_sfvb_theme**](SfvbApi.md#get_sfvb_theme) | **GET** /sfvb/storefronts/{storefront_oid}/themes/{theme_oid} | Get a theme
[**get_sfvb_theme_attributes**](SfvbApi.md#get_sfvb_theme_attributes) | **GET** /sfvb/storefronts/{storefront_oid}/themes/{theme_oid}/attributes | Read a theme&#39;s colors, fonts and settings
[**get_sfvb_theme_job**](SfvbApi.md#get_sfvb_theme_job) | **GET** /sfvb/storefronts/{storefront_oid}/theme_jobs/{job_id} | Status of an asynchronous theme job
[**get_sfvb_tracking_html**](SfvbApi.md#get_sfvb_tracking_html) | **GET** /sfvb/storefronts/{storefront_oid}/tracking/html/{slot} | Read one custom tracking HTML slot
[**get_sfvb_tracking_html_slots**](SfvbApi.md#get_sfvb_tracking_html_slots) | **GET** /sfvb/storefronts/{storefront_oid}/tracking/html | List a storefront&#39;s custom tracking HTML slots
[**get_sfvb_tracking_provider**](SfvbApi.md#get_sfvb_tracking_provider) | **GET** /sfvb/storefronts/{storefront_oid}/tracking/providers/{provider} | Read one tracking provider
[**get_sfvb_tracking_providers**](SfvbApi.md#get_sfvb_tracking_providers) | **GET** /sfvb/storefronts/{storefront_oid}/tracking/providers | List a storefront&#39;s tracking providers
[**get_sfvb_tracking_settings**](SfvbApi.md#get_sfvb_tracking_settings) | **GET** /sfvb/storefronts/{storefront_oid}/tracking | Read a storefront&#39;s privacy rules and advanced conversion settings
[**get_sfvb_transactional_email**](SfvbApi.md#get_sfvb_transactional_email) | **GET** /sfvb/storefronts/{storefront_oid}/transactional_emails/{file_name} | Read a transactional email&#39;s subject, delivery options and sender
[**get_sfvb_transactional_emails**](SfvbApi.md#get_sfvb_transactional_emails) | **GET** /sfvb/storefronts/{storefront_oid}/transactional_emails | List the transactional emails a storefront sends
[**get_sfvb_upsell_offer**](SfvbApi.md#get_sfvb_upsell_offer) | **GET** /sfvb/storefronts/{storefront_oid}/upsell_offers/{upsell_offer_oid} | Get an upsell offer
[**get_sfvb_upsell_path**](SfvbApi.md#get_sfvb_upsell_path) | **GET** /sfvb/storefronts/{storefront_oid}/upsell_paths/{upsell_path_oid} | Get an upsell path
[**get_sfvb_utm_shortcode**](SfvbApi.md#get_sfvb_utm_shortcode) | **GET** /sfvb/storefronts/{storefront_oid}/utm_shortcodes/{shortcode_oid} | Read one UTM shortcode
[**get_sfvb_utm_shortcodes**](SfvbApi.md#get_sfvb_utm_shortcodes) | **GET** /sfvb/storefronts/{storefront_oid}/utm_shortcodes | List a storefront&#39;s UTM shortcodes
[**get_sfvb_version**](SfvbApi.md#get_sfvb_version) | **GET** /sfvb/version | Compiler version for this merchant
[**get_sfvb_whoami**](SfvbApi.md#get_sfvb_whoami) | **GET** /sfvb/whoami | Who this token is
[**ignore_sfvb_not_found_entry**](SfvbApi.md#ignore_sfvb_not_found_entry) | **POST** /sfvb/storefronts/{storefront_oid}/not_found/{not_found_id}/ignore | Ignore a 404 path
[**import_sfvb_comms_provider_lists**](SfvbApi.md#import_sfvb_comms_provider_lists) | **POST** /sfvb/storefronts/{storefront_oid}/comms/providers/import | Import lists from another email provider
[**import_sfvb_redirects**](SfvbApi.md#import_sfvb_redirects) | **POST** /sfvb/storefronts/{storefront_oid}/redirects/import | Apply a reviewed redirect import
[**insert_sfvb_affiliate_network**](SfvbApi.md#insert_sfvb_affiliate_network) | **POST** /sfvb/storefronts/{storefront_oid}/tracking/affiliate_networks | Add an affiliate network
[**insert_sfvb_approval**](SfvbApi.md#insert_sfvb_approval) | **POST** /sfvb/approvals | Request a human approval
[**insert_sfvb_blog_post**](SfvbApi.md#insert_sfvb_blog_post) | **POST** /sfvb/storefronts/{storefront_oid}/blog_posts | Create a blog post
[**insert_sfvb_comms_folder**](SfvbApi.md#insert_sfvb_comms_folder) | **POST** /sfvb/storefronts/{storefront_oid}/list_segment_folders | Create a list and segment folder
[**insert_sfvb_comms_list**](SfvbApi.md#insert_sfvb_comms_list) | **POST** /sfvb/storefronts/{storefront_oid}/lists | Create an email list
[**insert_sfvb_comms_segment**](SfvbApi.md#insert_sfvb_comms_segment) | **POST** /sfvb/storefronts/{storefront_oid}/segments | Create a segment
[**insert_sfvb_comms_sending_domain**](SfvbApi.md#insert_sfvb_comms_sending_domain) | **POST** /sfvb/comms/sending_domains | Add a sending domain
[**insert_sfvb_comms_twilio_account**](SfvbApi.md#insert_sfvb_comms_twilio_account) | **POST** /sfvb/comms/twilio_account | Connect the Twilio account
[**insert_sfvb_page**](SfvbApi.md#insert_sfvb_page) | **POST** /sfvb/storefronts/{storefront_oid}/pages | Create a page
[**insert_sfvb_redirect**](SfvbApi.md#insert_sfvb_redirect) | **POST** /sfvb/storefronts/{storefront_oid}/redirects | Create a 301 redirect rule
[**insert_sfvb_secret_request**](SfvbApi.md#insert_sfvb_secret_request) | **POST** /sfvb/secrets | Ask a person to enter secret values
[**insert_sfvb_sequence_step**](SfvbApi.md#insert_sfvb_sequence_step) | **POST** /sfvb/storefronts/{storefront_oid}/sequences/{sequence_uuid}/steps | Add an email step, with its new email, a wait step, or a postcard step, with its new postcard
[**insert_sfvb_upsell_offer**](SfvbApi.md#insert_sfvb_upsell_offer) | **POST** /sfvb/storefronts/{storefront_oid}/upsell_offers | Create an upsell offer
[**insert_sfvb_upsell_path**](SfvbApi.md#insert_sfvb_upsell_path) | **POST** /sfvb/storefronts/{storefront_oid}/upsell_paths | Create an upsell path
[**insert_sfvb_utm_shortcode**](SfvbApi.md#insert_sfvb_utm_shortcode) | **POST** /sfvb/storefronts/{storefront_oid}/utm_shortcodes | Create a UTM shortcode
[**install_sfvb_library_entry**](SfvbApi.md#install_sfvb_library_entry) | **POST** /sfvb/storefronts/{storefront_oid}/library/{library_oid}/install | Install a library entry into a storefront
[**list_sfvb_blog_posts**](SfvbApi.md#list_sfvb_blog_posts) | **GET** /sfvb/storefronts/{storefront_oid}/blog_posts | List the storefront&#39;s blog posts
[**list_sfvb_campaigns**](SfvbApi.md#list_sfvb_campaigns) | **GET** /sfvb/storefronts/{storefront_oid}/campaigns | List the storefront&#39;s campaigns
[**list_sfvb_code_library_emails**](SfvbApi.md#list_sfvb_code_library_emails) | **GET** /sfvb/storefronts/{storefront_oid}/code_library/emails | Email items from the code library that can start a new email step
[**list_sfvb_comms_lists**](SfvbApi.md#list_sfvb_comms_lists) | **GET** /sfvb/storefronts/{storefront_oid}/lists | List the storefront&#39;s email lists
[**list_sfvb_comms_segments**](SfvbApi.md#list_sfvb_comms_segments) | **GET** /sfvb/storefronts/{storefront_oid}/segments | List the storefront&#39;s segments
[**list_sfvb_container_versions**](SfvbApi.md#list_sfvb_container_versions) | **GET** /sfvb/storefronts/{storefront_oid}/container_versions | Version history for a container stored outside the file system
[**list_sfvb_elements**](SfvbApi.md#list_sfvb_elements) | **GET** /sfvb/elements | List every SFVB element type
[**list_sfvb_experiments**](SfvbApi.md#list_sfvb_experiments) | **GET** /sfvb/storefronts/{storefront_oid}/experiments | List the storefront&#39;s experiments
[**list_sfvb_file_versions**](SfvbApi.md#list_sfvb_file_versions) | **GET** /sfvb/storefronts/{storefront_oid}/files/versions | Version history for a storefront file
[**list_sfvb_files**](SfvbApi.md#list_sfvb_files) | **GET** /sfvb/storefronts/{storefront_oid}/files | List a storefront directory
[**list_sfvb_flows**](SfvbApi.md#list_sfvb_flows) | **GET** /sfvb/storefronts/{storefront_oid}/flows | List the storefront&#39;s flows
[**list_sfvb_i18n_messages**](SfvbApi.md#list_sfvb_i18n_messages) | **GET** /sfvb/storefronts/{storefront_oid}/i18n/messages | List built-in messages
[**list_sfvb_item_containers**](SfvbApi.md#list_sfvb_item_containers) | **GET** /sfvb/storefronts/{storefront_oid}/item_containers | List the item containers on the account
[**list_sfvb_library_installs**](SfvbApi.md#list_sfvb_library_installs) | **GET** /sfvb/storefronts/{storefront_oid}/library/installs | List the library entries installed on a storefront
[**list_sfvb_pages**](SfvbApi.md#list_sfvb_pages) | **GET** /sfvb/storefronts/{storefront_oid}/pages/list | List the storefront&#39;s pages
[**list_sfvb_server_logs**](SfvbApi.md#list_sfvb_server_logs) | **GET** /sfvb/storefronts/{storefront_oid}/logs | List recent storefront render logs
[**list_sfvb_storefronts**](SfvbApi.md#list_sfvb_storefronts) | **GET** /sfvb/storefronts | List storefronts
[**list_sfvb_templates**](SfvbApi.md#list_sfvb_templates) | **GET** /sfvb/storefronts/{storefront_oid}/templates | List the active theme&#39;s templates
[**list_sfvb_themes**](SfvbApi.md#list_sfvb_themes) | **GET** /sfvb/storefronts/{storefront_oid}/themes | List themes for a storefront
[**list_sfvb_upsell_offers**](SfvbApi.md#list_sfvb_upsell_offers) | **GET** /sfvb/storefronts/{storefront_oid}/upsell_offers | List upsell offers
[**list_sfvb_upsell_paths**](SfvbApi.md#list_sfvb_upsell_paths) | **GET** /sfvb/storefronts/{storefront_oid}/upsell_paths | List upsell paths
[**move_sfvb_sequence_step**](SfvbApi.md#move_sfvb_sequence_step) | **POST** /sfvb/storefronts/{storefront_oid}/sequences/{sequence_uuid}/steps/{step_uuid}/move | Move one step
[**move_sfvb_upsell_path**](SfvbApi.md#move_sfvb_upsell_path) | **POST** /sfvb/storefronts/{storefront_oid}/upsell_paths/{upsell_path_oid}/move | Move an upsell path
[**proof_sfvb_sequence_postcard**](SfvbApi.md#proof_sfvb_sequence_postcard) | **POST** /sfvb/storefronts/{storefront_oid}/sequences/{sequence_uuid}/steps/{step_uuid}/postcard_proof | Proof a postcard step without mailing it
[**publish_sfvb_library_entry**](SfvbApi.md#publish_sfvb_library_entry) | **POST** /sfvb/storefronts/{storefront_oid}/library/{library_oid}/publish | Publish a library entry&#39;s draft
[**put_sfvb_container**](SfvbApi.md#put_sfvb_container) | **PUT** /sfvb/storefronts/{storefront_oid}/containers/{owner_type}/{owner_object_id} | Write a container stored outside the file system
[**put_sfvb_experiment_variation**](SfvbApi.md#put_sfvb_experiment_variation) | **PUT** /sfvb/storefronts/{storefront_oid}/experiments/{experiment_oid}/variations/{variation_number} | Pause or resume a variation
[**put_sfvb_file_content**](SfvbApi.md#put_sfvb_file_content) | **PUT** /sfvb/storefronts/{storefront_oid}/files/content | Write a storefront file
[**put_sfvb_i18n_glossary**](SfvbApi.md#put_sfvb_i18n_glossary) | **PUT** /sfvb/storefronts/{storefront_oid}/i18n/glossary | Replace the storefront&#39;s translation glossary
[**put_sfvb_i18n_message**](SfvbApi.md#put_sfvb_i18n_message) | **PUT** /sfvb/storefronts/{storefront_oid}/i18n/messages/{key} | Change one built-in message
[**put_sfvb_item_attributes**](SfvbApi.md#put_sfvb_item_attributes) | **PUT** /sfvb/storefronts/{storefront_oid}/items/attributes | Change some of an item&#39;s attributes
[**put_sfvb_item_content**](SfvbApi.md#put_sfvb_item_content) | **PUT** /sfvb/storefronts/{storefront_oid}/items/content | Change an item&#39;s title or long description
[**put_sfvb_item_multimedia**](SfvbApi.md#put_sfvb_item_multimedia) | **PUT** /sfvb/storefronts/{storefront_oid}/items/multimedia | Attach an image to an item
[**put_sfvb_item_multimedia_description**](SfvbApi.md#put_sfvb_item_multimedia_description) | **PUT** /sfvb/storefronts/{storefront_oid}/items/multimedia/description | Change an item image&#39;s description
[**put_sfvb_item_pricing**](SfvbApi.md#put_sfvb_item_pricing) | **PUT** /sfvb/storefronts/{storefront_oid}/items/pricing | Change what an item charges
[**put_sfvb_item_related**](SfvbApi.md#put_sfvb_item_related) | **PUT** /sfvb/storefronts/{storefront_oid}/items/related | Replace an item&#39;s related items
[**put_sfvb_item_seo**](SfvbApi.md#put_sfvb_item_seo) | **PUT** /sfvb/storefronts/{storefront_oid}/items/seo | Change an item&#39;s search metadata
[**put_sfvb_menu**](SfvbApi.md#put_sfvb_menu) | **PUT** /sfvb/storefronts/{storefront_oid}/menus/{code} | Replace a store menu&#39;s entries
[**put_sfvb_page_attributes**](SfvbApi.md#put_sfvb_page_attributes) | **PUT** /sfvb/storefronts/{storefront_oid}/pages/attributes | Change a page&#39;s attributes
[**put_sfvb_page_multimedia**](SfvbApi.md#put_sfvb_page_multimedia) | **PUT** /sfvb/storefronts/{storefront_oid}/pages/multimedia | Attach an image to a page
[**put_sfvb_page_selectors**](SfvbApi.md#put_sfvb_page_selectors) | **PUT** /sfvb/storefronts/{storefront_oid}/pages/selectors | Replace a page&#39;s selectors
[**put_sfvb_page_settings**](SfvbApi.md#put_sfvb_page_settings) | **PUT** /sfvb/storefronts/{storefront_oid}/pages/settings | Change a page&#39;s settings
[**put_sfvb_preview_session**](SfvbApi.md#put_sfvb_preview_session) | **PUT** /sfvb/storefronts/{storefront_oid}/preview_sessions/{preview_session_id} | Push containers into a preview session
[**put_sfvb_recording_settings**](SfvbApi.md#put_sfvb_recording_settings) | **PUT** /sfvb/storefronts/{storefront_oid}/recording_settings | Turn the storefront&#39;s screen recording on or off
[**put_sfvb_site_attributes**](SfvbApi.md#put_sfvb_site_attributes) | **PUT** /sfvb/storefronts/{storefront_oid}/attributes | Change a storefront&#39;s site attributes
[**put_sfvb_theme_attributes**](SfvbApi.md#put_sfvb_theme_attributes) | **PUT** /sfvb/storefronts/{storefront_oid}/themes/{theme_oid}/attributes | Change a theme&#39;s colors, fonts and settings
[**refresh_sfvb_comms_sending_domain_status**](SfvbApi.md#refresh_sfvb_comms_sending_domain_status) | **POST** /sfvb/comms/sending_domains/{domain}/status | Check a sending domain&#39;s verification
[**refresh_sfvb_page**](SfvbApi.md#refresh_sfvb_page) | **POST** /sfvb/storefronts/{storefront_oid}/pages/refresh | Drop one page&#39;s cached copy
[**remove_sfvb_page_blog_posts**](SfvbApi.md#remove_sfvb_page_blog_posts) | **POST** /sfvb/storefronts/{storefront_oid}/pages/blog_posts/remove | Take blog posts off a page
[**remove_sfvb_page_items**](SfvbApi.md#remove_sfvb_page_items) | **POST** /sfvb/storefronts/{storefront_oid}/pages/items/remove | Take items off a page
[**render_sfvb_email**](SfvbApi.md#render_sfvb_email) | **POST** /sfvb/storefronts/{storefront_oid}/emails/{email_uuid}/render | Render a flow or campaign email without sending it
[**render_sfvb_transactional_email**](SfvbApi.md#render_sfvb_transactional_email) | **POST** /sfvb/storefronts/{storefront_oid}/transactional_emails/{file_name}/render | Render a transactional email without sending it
[**render_sfvb_widgets**](SfvbApi.md#render_sfvb_widgets) | **POST** /sfvb/storefronts/{storefront_oid}/themes/{theme_oid}/render | Render a CJSON node to HTML
[**reserve_sfvb_widget_ids**](SfvbApi.md#reserve_sfvb_widget_ids) | **POST** /sfvb/storefronts/{storefront_oid}/widget_ids | Reserve a block of widget ids
[**reset_sfvb_i18n_message**](SfvbApi.md#reset_sfvb_i18n_message) | **DELETE** /sfvb/storefronts/{storefront_oid}/i18n/messages/{key} | Reset one built-in message
[**resolve_sfvb_redirect**](SfvbApi.md#resolve_sfvb_redirect) | **GET** /sfvb/storefronts/{storefront_oid}/redirects/resolve | What a shopper gets for a path
[**resolve_sfvb_redirect_batch**](SfvbApi.md#resolve_sfvb_redirect_batch) | **POST** /sfvb/storefronts/{storefront_oid}/redirects/resolve_batch | What a shopper gets for each of many paths
[**resolve_sfvb_template**](SfvbApi.md#resolve_sfvb_template) | **GET** /sfvb/storefronts/{storefront_oid}/templates/resolve | Resolve a template name to the file a page renders
[**revert_sfvb_container**](SfvbApi.md#revert_sfvb_container) | **POST** /sfvb/storefronts/{storefront_oid}/containers/{owner_type}/{owner_object_id}/revert | Revert a container stored outside the file system
[**revert_sfvb_file**](SfvbApi.md#revert_sfvb_file) | **POST** /sfvb/storefronts/{storefront_oid}/files/revert | Revert a storefront file to an earlier version
[**review_sfvb_email**](SfvbApi.md#review_sfvb_email) | **POST** /sfvb/storefronts/{storefront_oid}/emails/{email_uuid}/review | Request a content review of a flow or campaign email
[**revoke_sfvb_secret_request**](SfvbApi.md#revoke_sfvb_secret_request) | **POST** /sfvb/secrets/{request_id}/revoke | Revoke a fulfilled request&#39;s unused handles
[**search_sfvb_files**](SfvbApi.md#search_sfvb_files) | **POST** /sfvb/storefronts/{storefront_oid}/files/search | Search storefront files
[**search_sfvb_library**](SfvbApi.md#search_sfvb_library) | **GET** /sfvb/storefronts/{storefront_oid}/library | Search the element library
[**set_sfvb_library_screenshot**](SfvbApi.md#set_sfvb_library_screenshot) | **PUT** /sfvb/storefronts/{storefront_oid}/library/{library_oid}/screenshot | Set a library entry&#39;s screenshot
[**share_sfvb_library_entry**](SfvbApi.md#share_sfvb_library_entry) | **POST** /sfvb/storefronts/{storefront_oid}/library/{library_oid}/shares | Share a published library entry with a linked account
[**start_sfvb_experiment**](SfvbApi.md#start_sfvb_experiment) | **POST** /sfvb/storefronts/{storefront_oid}/experiments | Start an experiment
[**test_sfvb_comms_email**](SfvbApi.md#test_sfvb_comms_email) | **POST** /sfvb/storefronts/{storefront_oid}/comms/sequences/{commseq_uuid}/steps/{step_uuid}/test_email | Send one test of an email step&#39;s email to a user on this account
[**test_sfvb_comms_postcard**](SfvbApi.md#test_sfvb_comms_postcard) | **POST** /sfvb/storefronts/{storefront_oid}/comms/sequences/{commseq_uuid}/steps/{step_uuid}/test_postcard | Print and mail one real test postcard
[**test_sfvb_comms_sms**](SfvbApi.md#test_sfvb_comms_sms) | **POST** /sfvb/storefronts/{storefront_oid}/comms/sequences/{commseq_uuid}/steps/{step_uuid}/test_sms | Send one test of an SMS step to a user on this account
[**unarchive_sfvb_upsell_path**](SfvbApi.md#unarchive_sfvb_upsell_path) | **POST** /sfvb/storefronts/{storefront_oid}/upsell_paths/{upsell_path_oid}/unarchive | Unarchive an upsell path
[**unfavorite_sfvb_library_entry**](SfvbApi.md#unfavorite_sfvb_library_entry) | **DELETE** /sfvb/storefronts/{storefront_oid}/library/{library_oid}/favorite | Remove a library entry from favorites
[**unignore_sfvb_not_found_entry**](SfvbApi.md#unignore_sfvb_not_found_entry) | **DELETE** /sfvb/storefronts/{storefront_oid}/not_found/{not_found_id}/ignore | Stop ignoring a 404 path
[**unpublish_sfvb_library_entry**](SfvbApi.md#unpublish_sfvb_library_entry) | **POST** /sfvb/storefronts/{storefront_oid}/library/{library_oid}/unpublish | Narrow who can see a library entry
[**unshare_sfvb_library_entry**](SfvbApi.md#unshare_sfvb_library_entry) | **DELETE** /sfvb/storefronts/{storefront_oid}/library/{library_oid}/shares/{merchant_id} | Stop sharing a library entry with an account
[**update_sfvb_affiliate_network**](SfvbApi.md#update_sfvb_affiliate_network) | **PUT** /sfvb/storefronts/{storefront_oid}/tracking/affiliate_networks/{affiliate_network_oid} | Change an affiliate network
[**update_sfvb_blog_post**](SfvbApi.md#update_sfvb_blog_post) | **PUT** /sfvb/storefronts/{storefront_oid}/blog_posts/{blog_post_oid} | Change a blog post
[**update_sfvb_campaign**](SfvbApi.md#update_sfvb_campaign) | **PUT** /sfvb/storefronts/{storefront_oid}/campaigns/{campaign_uuid} | Change a campaign
[**update_sfvb_comms_folder**](SfvbApi.md#update_sfvb_comms_folder) | **PUT** /sfvb/storefronts/{storefront_oid}/list_segment_folders/{folder_uuid} | Rename a list and segment folder
[**update_sfvb_comms_list**](SfvbApi.md#update_sfvb_comms_list) | **PUT** /sfvb/storefronts/{storefront_oid}/lists/{list_uuid} | Change an email list&#39;s name, folder or public settings
[**update_sfvb_comms_segment**](SfvbApi.md#update_sfvb_comms_segment) | **PUT** /sfvb/storefronts/{storefront_oid}/segments/{segment_uuid} | Change a segment&#39;s name, rule or folder
[**update_sfvb_comms_sending_domain**](SfvbApi.md#update_sfvb_comms_sending_domain) | **PUT** /sfvb/comms/sending_domains/{domain} | Update a sending domain
[**update_sfvb_comms_settings**](SfvbApi.md#update_sfvb_comms_settings) | **PUT** /sfvb/storefronts/{storefront_oid}/comms/settings | Change a storefront&#39;s communications settings
[**update_sfvb_comms_twilio_account**](SfvbApi.md#update_sfvb_comms_twilio_account) | **PUT** /sfvb/comms/twilio_account | Update the Twilio account
[**update_sfvb_email**](SfvbApi.md#update_sfvb_email) | **PUT** /sfvb/storefronts/{storefront_oid}/emails/{email_uuid} | Change a flow or campaign email&#39;s subject or preview text
[**update_sfvb_flow**](SfvbApi.md#update_sfvb_flow) | **PUT** /sfvb/storefronts/{storefront_oid}/flows/{flow_uuid} | Change a flow
[**update_sfvb_flow_status**](SfvbApi.md#update_sfvb_flow_status) | **PUT** /sfvb/storefronts/{storefront_oid}/flows/{flow_uuid}/status | Turn a flow on or off
[**update_sfvb_item_attribute_batch**](SfvbApi.md#update_sfvb_item_attribute_batch) | **POST** /sfvb/storefronts/{storefront_oid}/items/attributes/batch | Change attributes across many items in one call
[**update_sfvb_library_entry**](SfvbApi.md#update_sfvb_library_entry) | **PUT** /sfvb/storefronts/{storefront_oid}/library/{library_oid} | Update a library entry&#39;s draft
[**update_sfvb_redirect**](SfvbApi.md#update_sfvb_redirect) | **PUT** /sfvb/storefronts/{storefront_oid}/redirects/{redirect_id} | Change a redirect rule
[**update_sfvb_sequence_step**](SfvbApi.md#update_sfvb_sequence_step) | **PUT** /sfvb/storefronts/{storefront_oid}/sequences/{sequence_uuid}/steps/{step_uuid} | Change one step&#39;s settings or audience filter
[**update_sfvb_site_seo**](SfvbApi.md#update_sfvb_site_seo) | **PUT** /sfvb/storefronts/{storefront_oid}/seo | Change a storefront&#39;s search engine settings
[**update_sfvb_smart_attribution**](SfvbApi.md#update_sfvb_smart_attribution) | **PUT** /sfvb/storefronts/{storefront_oid}/smart_attribution | Change a storefront&#39;s Smart Attribution configuration
[**update_sfvb_tracking_advanced**](SfvbApi.md#update_sfvb_tracking_advanced) | **PUT** /sfvb/storefronts/{storefront_oid}/tracking/advanced | Change a storefront&#39;s advanced conversion settings
[**update_sfvb_tracking_html**](SfvbApi.md#update_sfvb_tracking_html) | **PUT** /sfvb/storefronts/{storefront_oid}/tracking/html/{slot} | Write one custom tracking HTML slot
[**update_sfvb_tracking_privacy**](SfvbApi.md#update_sfvb_tracking_privacy) | **PUT** /sfvb/storefronts/{storefront_oid}/tracking/privacy | Change a storefront&#39;s privacy rules
[**update_sfvb_tracking_provider**](SfvbApi.md#update_sfvb_tracking_provider) | **PUT** /sfvb/storefronts/{storefront_oid}/tracking/providers/{provider} | Change one tracking provider
[**update_sfvb_transactional_email**](SfvbApi.md#update_sfvb_transactional_email) | **PUT** /sfvb/storefronts/{storefront_oid}/transactional_emails/{file_name} | Change a transactional email&#39;s subject, delivery options or sender
[**update_sfvb_upsell_offer**](SfvbApi.md#update_sfvb_upsell_offer) | **PUT** /sfvb/storefronts/{storefront_oid}/upsell_offers/{upsell_offer_oid} | Update an upsell offer
[**update_sfvb_upsell_path**](SfvbApi.md#update_sfvb_upsell_path) | **PUT** /sfvb/storefronts/{storefront_oid}/upsell_paths/{upsell_path_oid} | Update an upsell path
[**update_sfvb_utm_shortcode**](SfvbApi.md#update_sfvb_utm_shortcode) | **PUT** /sfvb/storefronts/{storefront_oid}/utm_shortcodes/{shortcode_oid} | Change a UTM shortcode
[**upload_sfvb_file**](SfvbApi.md#upload_sfvb_file) | **POST** /sfvb/storefronts/{storefront_oid}/files/upload | Store a binary asset that was already uploaded
[**validate_sfvb_cjson**](SfvbApi.md#validate_sfvb_cjson) | **POST** /sfvb/cjson/validate | Validate CJSON
[**validate_sfvb_velocity**](SfvbApi.md#validate_sfvb_velocity) | **POST** /sfvb/storefronts/{storefront_oid}/themes/{theme_oid}/velocity/validate | Validate a Velocity template against a theme


# **add_sfvb_page_blog_posts**
> SfvbPageBlogPostsResponse add_sfvb_page_blog_posts(storefront_oid, path, page_blog_posts_request)

Assign blog posts to a page

Adds posts by blog_post_oid, at most 500 at a time.  Every oid must be a post on this storefront, and one that is not changes nothing.  Refused on a page whose selectors choose its blog posts.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /blog/ |
 **page_blog_posts_request** | [**SfvbPageBlogPostsRequest**](SfvbPageBlogPostsRequest.md)| Blog posts to assign |

### Return type

[**SfvbPageBlogPostsResponse**](SfvbPageBlogPostsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_sfvb_page_items**
> SfvbPageItemsResponse add_sfvb_page_items(storefront_oid, path, page_items_add_request)

Assign items to a page

Adds items by item id, at most 500 at a time, or changes the sort order or url part of items already on the page.  Every id is checked first and one unknown id changes nothing.  Refused on a page whose selectors choose its items.  sort_order is refused unless the page sorts its items by a custom order.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /lp/spring-sale/ |
 **page_items_add_request** | [**SfvbPageItemsAddRequest**](SfvbPageItemsAddRequest.md)| Items to assign |

### Return type

[**SfvbPageItemsResponse**](SfvbPageItemsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_sfvb_campaign**
> SfvbCampaign archive_sfvb_campaign(storefront_oid, campaign_uuid, if_match, archive_request)

Archive or unarchive a campaign

Archiving alone never stops a send, so archiving a scheduled campaign also sets it back to draft, and notes says so.  A campaign whose send is under way is refused with sfvb.campaign_sending.  Send the hash_sha256 you read as If-Match.  A scheduled, sending or sent campaign needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **campaign_uuid** | **str**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **archive_request** | [**SfvbArchiveRequest**](SfvbArchiveRequest.md)| Whether to archive |

### Return type

[**SfvbCampaign**](SfvbCampaign.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_sfvb_comms_list**
> SfvbCommsListResponse archive_sfvb_comms_list(storefront_oid, list_uuid, if_match)

Archive an email list

Hides the list from the lists list and the admin, and keeps its members.  Refused with sfvb.in_use_live, naming each one, while a live campaign or flow uses it; notes names any that use it but aren't live, which can no longer use it.  Send the list's hash_sha256 as If-Match. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **list_uuid** | **str**|  |
 **if_match** | **str**| The list&#39;s hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |

### Return type

[**SfvbCommsListResponse**](SfvbCommsListResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_sfvb_comms_segment**
> SfvbCommsSegmentResponse archive_sfvb_comms_segment(storefront_oid, segment_uuid, if_match)

Archive a segment

Hides the segment from the segments list and the admin.  Refused with sfvb.in_use_live, naming each one, while a live campaign or flow uses it; notes names any that use it but aren't live, which can no longer use it.  Send the segment's hash_sha256 as If-Match. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **segment_uuid** | **str**|  |
 **if_match** | **str**| The segment&#39;s hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |

### Return type

[**SfvbCommsSegmentResponse**](SfvbCommsSegmentResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_sfvb_flow**
> SfvbFlow archive_sfvb_flow(storefront_oid, flow_uuid, if_match, archive_request)

Archive or unarchive a flow

A flow that is still enrolling customers is refused, because archiving would only hide it.  Set its status to inactive first.  Send the hash_sha256 you read as If-Match. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **flow_uuid** | **str**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **archive_request** | [**SfvbArchiveRequest**](SfvbArchiveRequest.md)| Whether to archive |

### Return type

[**SfvbFlow**](SfvbFlow.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_sfvb_upsell_path**
> SfvbUpsellPath archive_sfvb_upsell_path(storefront_oid, upsell_path_oid)

Archive an upsell path

Files the path out of the default list.  An archived path does not run.  Archiving one that is switched on is a live change and needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_path_oid** | **int**|  |

### Return type

[**SfvbUpsellPath**](SfvbUpsellPath.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_sfvb_blog_post_image**
> SfvbBlogPostDetail attach_sfvb_blog_post_image(storefront_oid, blog_post_oid, blog_post_image_request)

Attach an image to a blog post

Three calls, like the admin blog editor's upload.  Request an upload URL with files/upload_url, send the bytes to it, then attach with the key and a filename.  No storefront file is created, and the key is redeemed, so it cannot be used twice.  default_image replaces the post's default image and code replaces the image with that code; with neither, the image is added for use in the body at the url the response reports.  JPEG, PNG, GIF or WebP, checked by content.  A post that is not a draft needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **blog_post_oid** | **int**|  |
 **blog_post_image_request** | [**SfvbBlogPostImageRequest**](SfvbBlogPostImageRequest.md)| Image to attach |

### Return type

[**SfvbBlogPostDetail**](SfvbBlogPostDetail.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**413** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_sfvb_redirect**
> SfvbRedirectCheckResponse check_sfvb_redirect(storefront_oid, redirect_request)

Check a redirect rule without creating it

Runs every check a create runs (loops, chains, duplicates, missing or external targets, system paths, live pages, the rule limit) and returns the findings.  Writes nothing. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **redirect_request** | [**SfvbRedirectRequest**](SfvbRedirectRequest.md)| The request |

### Return type

[**SfvbRedirectCheckResponse**](SfvbRedirectCheckResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_sfvb_library_screenshot**
> SfvbLibraryEntry clear_sfvb_library_screenshot(storefront_oid, library_oid, if_match)

Remove a library entry's screenshot

Owner only, with the draft's hash_sha256 as If-Match.  Clears the screenshot and thumbnail.  Published revisions and copies that used the image keep it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |

### Return type

[**SfvbLibraryEntry**](SfvbLibraryEntry.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_sfvb_campaign**
> SfvbCampaign clone_sfvb_campaign(storefront_oid, campaign_uuid)

Copy a campaign on the same storefront

A draft copy with copies of its emails and postcards, named Copy of and the original name, never archived and never scheduled.  Steps keep their settings, including a paused rate limiter or an experiment winner, and notes names each one. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **campaign_uuid** | **str**|  |

### Return type

[**SfvbCampaign**](SfvbCampaign.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_sfvb_flow**
> SfvbFlow clone_sfvb_flow(storefront_oid, flow_uuid)

Copy a flow on the same storefront

A draft copy with copies of its emails and postcards, named Copy of and the original name, never archived.  It enrolls nobody until it is turned on.  Steps keep their settings, including a paused rate limiter or an experiment winner, and notes names each one. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **flow_uuid** | **str**|  |

### Return type

[**SfvbFlow**](SfvbFlow.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compile_sfvb_cjson**
> SfvbCompileResponse compile_sfvb_cjson(compile_request)

Compile CJSON to Velocity

Compiles a container document to Velocity without storing anything.  Supply theme_oid to compile with the theme's inherit groups applied; omit it to compile standalone. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compile_request** | [**SfvbCompileRequest**](SfvbCompileRequest.md)| CJSON to compile |

### Return type

[**SfvbCompileResponse**](SfvbCompileResponse.md)

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
**413** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sfvb_campaign**
> SfvbCampaign create_sfvb_campaign(storefront_oid, campaign_write_request)

Create a draft campaign

A new draft campaign with an empty communication sequence.  name is required.  The sender defaults to the storefront's marketing sending settings.  Nothing here starts a campaign. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **campaign_write_request** | [**SfvbCampaignWriteRequest**](SfvbCampaignWriteRequest.md)| The campaign to create |

### Return type

[**SfvbCampaign**](SfvbCampaign.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sfvb_flow**
> SfvbFlow create_sfvb_flow(storefront_oid, flow_write_request)

Create a draft flow

A new draft flow with an empty communication sequence.  name and trigger_type are required.  A list or segment trigger needs trigger_parameter, the uuid of a list or segment on this storefront.  The sender defaults to the storefront's marketing sending settings.  A draft flow enrolls nobody until it is turned on. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **flow_write_request** | [**SfvbFlowWriteRequest**](SfvbFlowWriteRequest.md)| The flow to create |

### Return type

[**SfvbFlow**](SfvbFlow.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sfvb_library_entry**
> SfvbLibraryEntry create_sfvb_library_entry(storefront_oid, library_entry)

Save a fragment to the library

Creates a private draft owned by the calling user.  The fragment is one widget and its children, and it must validate.  Images it references on this storefront are copied into the entry before this returns, so it installs anywhere with its images.  The fragment is scanned; card skimming or obfuscation signals are refused outright.  Nothing other merchants or shoppers see changes, so sfvb_write is enough.  Publish it to share it.  An optional screenshot takes a staged PNG key, exactly as the library screenshot endpoint does; a refused screenshot refuses the whole create. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_entry** | [**SfvbLibraryEntryRequest**](SfvbLibraryEntryRequest.md)| The entry |

### Return type

[**SfvbLibraryEntry**](SfvbLibraryEntry.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**413** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sfvb_preview_access**
> SfvbPreviewAccessResponse create_sfvb_preview_access(storefront_oid)

One time link that opens a preview in a browser with no UltraCart login

The preview URL only works in a browser already signed in to UltraCart on the storefront's own host, and an agent's built in browser never is.  This returns a single use access_url on the storefront host instead.  Opening it gets past the storefront lock, shows the requested theme and applies the requested preview session for the rest of that browser session, then redirects to path.  It expires two minutes after issue or on first use.  With a preview session, pages opened afterwards carry an X-UltraCart-Preview header of applied or not-applied.  Without one, the pages are the live content and carry no X-UltraCart-Preview header.  Requires a token that resolves to a user, so use the device authorization flow. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **preview_access** | [**SfvbPreviewAccessRequest**](SfvbPreviewAccessRequest.md)| What the browser should see | [optional]

### Return type

[**SfvbPreviewAccessResponse**](SfvbPreviewAccessResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sfvb_preview_session**
> SfvbPreviewSessionResponse create_sfvb_preview_session(storefront_oid)

Create a preview session

Returns a server generated session id to push containers into, and opens the session so that id exists rather than merely being random.  The id is not caller supplied, because concurrent agents choosing their own would be free to collide, and the browser editor's habit of minting one with Math.random is not a property worth carrying into an API.  Expires after eight hours and can be deleted sooner.  Requires a token that resolves to a user, so use the device authorization flow. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbPreviewSessionResponse**](SfvbPreviewSessionResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_affiliate_network**
> delete_sfvb_affiliate_network(storefront_oid, affiliate_network_oid, if_match, approval_id)

Delete an affiliate network

Visits from the network stop being recognized and its pixel stops firing.  Refused with 409 while Smart Attribution names the network as a platform.  Send the network's hash_sha256 as If-Match.  Needs sfvb_publish and an approved affiliate_network.delete request (Approval-Id). 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **affiliate_network_oid** | **int**|  |
 **if_match** | **str**| The network&#39;s hash_sha256 from the last read.  428 when absent, 412 when stale. |
 **approval_id** | **str**| The approval_id of an approved affiliate_network.delete request for this network.  See POST /sfvb/approvals. |

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
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_approval**
> delete_sfvb_approval(approval_id)

Cancel a pending approval request

Withdraws a request nobody has decided yet, which frees one of the five pending slots a sign-in has.  A request that was already decided, used or expired cannot be cancelled. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_id** | **str**|  |

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
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_blog_post**
> delete_sfvb_blog_post(storefront_oid, blog_post_oid)

Delete a blog post

Takes the post off every page and deletes it.  There is no undo.  A post that is not a draft needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **blog_post_oid** | **int**|  |
 **approval_id** | **str**| The approval_id of an approved blog_post.delete request for this post.  See POST /sfvb/approvals. | [optional]

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
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_comms_folder**
> SfvbCommsFolderResponse delete_sfvb_comms_folder(storefront_oid, folder_uuid, if_match)

Delete a list and segment folder

Its lists and segments are kept and filed under no folder, as the admin does; items names each one.  Send the folder's hash_sha256 as If-Match.  A folder the admin made itself (system_generated) can't be deleted here. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **folder_uuid** | **str**|  |
 **if_match** | **str**| The folder&#39;s hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |

### Return type

[**SfvbCommsFolderResponse**](SfvbCommsFolderResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_comms_sending_domain**
> delete_sfvb_comms_sending_domain(domain)

Remove a sending domain

Removes the domain from UltraCart and from Amazon SES.  Needs an approved sending_domain.delete request for it (POST approvals, params.domain). 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  |
 **approval_id** | **str**| The approval_id of an approved sending_domain.delete request for this domain.  See POST /sfvb/approvals. | [optional]

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
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |
**502** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_comms_twilio_account**
> delete_sfvb_comms_twilio_account()

Remove the Twilio account

Removes the account's Twilio account and its credentials from UltraCart.  The account stays at Twilio.  Needs an approved twilio_account.delete request for it (POST approvals, params.esp_twilio_uuid). 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_id** | **str**| The approval_id of an approved twilio_account.delete request for this account.  See POST /sfvb/approvals. | [optional]

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
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_file**
> delete_sfvb_file(storefront_oid, if_match)

Delete a storefront file

Recoverable from the recycle bin. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **if_match** | **str**| Content hash of the file being deleted.  Required; 428 when absent, 412 when stale. |
 **path** | **str**|  | [optional]
 **approval_id** | **str**| The approval_id of an approved file.delete request for this exact path.  See POST /sfvb/approvals. | [optional]

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_item_attribute**
> SfvbItemResponse delete_sfvb_item_attribute(storefront_oid, name)

Delete an attribute from an item

Removes one attribute that no template on the item's pages declares - a test name, a misspelling, one a retired template used.  A declared attribute is refused, because the template would list it again, empty; send an empty value through the attributes update to clear one of those instead. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **name** | **str**| The attribute name, matched without regard to case |
 **merchant_item_id** | **str**|  | [optional]
 **merchant_item_oid** | **int**|  | [optional]

### Return type

[**SfvbItemResponse**](SfvbItemResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_item_multimedia**
> SfvbItemResponse delete_sfvb_item_multimedia(storefront_oid)

Detach an image from an item

Removes the item's copy of the image in one slot.  The file you uploaded is left where it is, so the same source can be attached again or used elsewhere. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **merchant_item_id** | **str**|  | [optional]
 **merchant_item_oid** | **int**|  | [optional]
 **code** | **str**| The image code to detach | [optional]
 **default** | **bool**| Detach the default image instead of a coded one | [optional]

### Return type

[**SfvbItemResponse**](SfvbItemResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_library_entry**
> SfvbLibraryDeleteResult delete_sfvb_library_entry(storefront_oid, library_oid, if_match)

Delete or retire a library entry

Owner only, with the draft's hash_sha256 as If-Match.  An entry that was never published, installed or shared is deleted.  Anything else is retired - kept so the storefronts that installed it still resolve, but out of search and refusing new installs and publishes.  The result says which happened. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |

### Return type

[**SfvbLibraryDeleteResult**](SfvbLibraryDeleteResult.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_not_found_entry**
> delete_sfvb_not_found_entry(storefront_oid, not_found_id)

Remove a 404 path from the log

The admin's Permanent Ignore button.  Despite that label, the next hit on the path records it again as a new entry.  To stop counting a path, ignore it instead. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **not_found_id** | **str**|  |

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
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_page_multimedia**
> SfvbPageResponse delete_sfvb_page_multimedia(storefront_oid, path)

Detach an image from a page

Name exactly one of code or default.  Removes the page's copy of the image; the source file in the page folder is left alone.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /catalog/dispensers/ |
 **code** | **str**| Image code to detach | [optional]
 **default** | **bool**| True to detach the default image | [optional]

### Return type

[**SfvbPageResponse**](SfvbPageResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_preview_session**
> delete_sfvb_preview_session(storefront_oid, preview_session_id)

Delete a preview session

Releases the session before its eight hour expiry.  Without this the only way to free one is to wait, which is a poor answer for a tool that may open a dozen in an afternoon. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **preview_session_id** | **str**|  |

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_redirect**
> delete_sfvb_redirect(storefront_oid, redirect_id, if_match)

Delete a redirect rule

Deletes one rule.  The source path answers again as it would without the rule.  Send the hash_sha256 you read as If-Match.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **redirect_id** | **int**|  |
 **if_match** | **str**| hash_sha256 from the last read.  428 when absent, 412 when stale. |

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_redirects**
> SfvbRedirectDeleteResponse delete_sfvb_redirects(storefront_oid, redirect_delete_request)

Delete up to 5,000 redirect rules in one call

Deletes exactly the rows of a dry run, given its plan_hash, in one transaction.  Every row needs its hash_sha256.  A rule changed since its hash was read is skipped and reported as stale, and a missing one as not_found; the other rows still go through.  Needs the approval of the person who signed in the CLI, as an approved redirect.delete_batch request for exactly these rows in the Approval-Id header, and sfvb_publish.  Deleting rules lets add and import work again once the storefront is back under 5,000 rules. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **redirect_delete_request** | [**SfvbRedirectDeleteRequest**](SfvbRedirectDeleteRequest.md)| The request |
 **approval_id** | **str**| The approval_id of an approved redirect.delete_batch request for exactly these rows.  Required.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbRedirectDeleteResponse**](SfvbRedirectDeleteResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**413** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_secret_request**
> SfvbSecretRequest delete_sfvb_secret_request(request_id)

Cancel a pending secret request

Withdraws a request nobody has filled in yet, with its handles, which frees one of the five pending slots a sign-in has.  A fulfilled request cannot be cancelled; revoke its handles instead. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  |

### Return type

[**SfvbSecretRequest**](SfvbSecretRequest.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_sequence_step**
> SfvbSequenceStepDeleteResponse delete_sfvb_sequence_step(storefront_oid, sequence_uuid, step_uuid, if_match)

Remove one step

Removes the step from its list and links the step before it to the step after it, in one transaction.  An email, experiment or postcard step's email or postcard is archived with it.  Refused while any customer is waiting on the step, for the begin, end, continue and merge markers, for a condition, split or inboxgeek step with steps on a side, and for a step whose email a resend step re-sends.  Send the step's hash_sha256 as If-Match.  A sequence whose campaign or flow is live needs sfvb_publish and an approved sequence_step.delete approval (Approval-Id); a draft or inactive one needs neither.  An email or postcard another step still uses is left as it is. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **sequence_uuid** | **str**|  |
 **step_uuid** | **str**|  |
 **if_match** | **str**| The step&#39;s hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **approval_id** | **str**| When the sequence is live, the approval_id of an approved sequence_step.delete request for this step.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbSequenceStepDeleteResponse**](SfvbSequenceStepDeleteResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_smart_attribution**
> delete_sfvb_smart_attribution(storefront_oid, if_match)

Delete a storefront's Smart Attribution configuration

Every platform goes back to being sent conversions as it was before Smart Attribution, and the settings are gone.  Send the hash_sha256 you read as If-Match.  Needs sfvb_publish and an approved smart_attribution.delete request (Approval-Id).  An unconfigured storefront is 404. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **if_match** | **str**| hash_sha256 from the Smart Attribution read.  428 when absent, 412 when stale. |
 **approval_id** | **str**| The approval_id of an approved smart_attribution.delete request.  Required.  See POST /sfvb/approvals. | [optional]

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
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_tracking_provider**
> SfvbTrackingProvider delete_sfvb_tracking_provider(storefront_oid, provider, if_match)

Clear one tracking provider

Clears every field and secret the API can change, the consent gate and the events, and turns off Google Tag Gateway.  The provider stops being sent anything.  An OAuth connection is left alone, and notes say to disconnect it in the admin.  Send the provider's hash_sha256 as If-Match.  Needs sfvb_publish.  No approval. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **provider** | **str**|  |
 **if_match** | **str**| The provider&#39;s hash_sha256 from the last read.  428 when absent, 412 when stale. |

### Return type

[**SfvbTrackingProvider**](SfvbTrackingProvider.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |
**502** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sfvb_utm_shortcode**
> delete_sfvb_utm_shortcode(storefront_oid, shortcode_oid, if_match)

Delete a UTM shortcode

The shortcode stops attributing at once.  A link that uses it as a path segment still opens its page, without the UTM values.  Send the hash_sha256 you read as If-Match.  Needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **shortcode_oid** | **int**|  |
 **if_match** | **str**| The shortcode&#39;s hash_sha256 from the last read.  428 when absent, 412 when stale. |

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
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_sfvb_blog_post_image**
> SfvbBlogPostDetail detach_sfvb_blog_post_image(storefront_oid, blog_post_oid, blog_post_image_request)

Detach an image from a blog post

Name exactly one of default_image, code or blog_post_multimedia_oid.  Removes the image from the post and deletes its stored copy.  Take it out of the body too, or the body keeps a broken image.  A post that is not a draft needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **blog_post_oid** | **int**|  |
 **blog_post_image_request** | [**SfvbBlogPostImageRequest**](SfvbBlogPostImageRequest.md)| Image to detach |

### Return type

[**SfvbBlogPostDetail**](SfvbBlogPostDetail.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_sfvb_i18n_language**
> SfvbI18nLanguagesResponse disable_sfvb_i18n_language(storefront_oid, code, if_match)

Disable a language

Stops serving a language.  Its hand and machine translations are kept and come back when it is enabled again.  The default language cannot be disabled.  Already disabled answers changed false.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **code** | **str**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |

### Return type

[**SfvbI18nLanguagesResponse**](SfvbI18nLanguagesResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_sfvb_upsell_offer**
> SfvbUpsellOffer disable_sfvb_upsell_offer(storefront_oid, upsell_offer_oid)

Disable an upsell offer

Switches the offer off.  Disabling one that is switched on is a live change and needs sfvb_publish.  An offer that is already off is returned unchanged.  There is no delete. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_offer_oid** | **int**|  |

### Return type

[**SfvbUpsellOffer**](SfvbUpsellOffer.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_sfvb_upsell_path**
> SfvbUpsellPath disable_sfvb_upsell_path(storefront_oid, upsell_path_oid)

Disable an upsell path

Switches the path off.  Disabling a running path is a live change and needs sfvb_publish.  A path that is already off is returned unchanged.  There is no delete. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_path_oid** | **int**|  |

### Return type

[**SfvbUpsellPath**](SfvbUpsellPath.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_sfvb_file**
> download_sfvb_file(storefront_oid)

Read a storefront file's raw bytes

Returns the file itself rather than a JSON envelope, for any type including binaries that files/content refuses.  Use this to verify what you uploaded, and note it is the only way to read a file inside a theme that is not active - such a file is served to nobody until the theme is promoted, so it has no public URL to fetch instead.  On success the body is the file; on failure it is the usual JSON error object, so do not assume the content type without checking the status. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dry_run_sfvb_item_attribute_batch**
> SfvbItemAttributeBatchResponse dry_run_sfvb_item_attribute_batch(storefront_oid, item_attribute_batch_request)

Check attribute changes across many items without writing them

Checks up to 2,000 rows on up to 200 items, each with the single attribute update's checks, and answers every row as change, unchanged, stale (expected_value differs from the current value), not_found or invalid, with the current value and its current_sha256, plus a plan_hash over the change rows.  Writes nothing.  SEO attributes are refused; a batch never touches them or any attribute it does not name. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **item_attribute_batch_request** | [**SfvbItemAttributeBatchRequest**](SfvbItemAttributeBatchRequest.md)| The rows |

### Return type

[**SfvbItemAttributeBatchResponse**](SfvbItemAttributeBatchResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**413** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dry_run_sfvb_redirect_delete**
> SfvbRedirectDeleteResponse dry_run_sfvb_redirect_delete(storefront_oid, redirect_delete_request)

Check a batch delete of redirect rules without writing it

Checks up to 5,000 rules by redirect_id and returns each one as deletable, stale (its hash_sha256 differs from the one sent) or not_found, with its current hash, source, target, status, type and note, and a plan_hash.  Writes nothing.  Rows may leave out hash_sha256; the result carries the current one to send when deleting. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **redirect_delete_request** | [**SfvbRedirectDeleteRequest**](SfvbRedirectDeleteRequest.md)| The request |

### Return type

[**SfvbRedirectDeleteResponse**](SfvbRedirectDeleteResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**413** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dry_run_sfvb_redirect_import**
> SfvbRedirectImportResponse dry_run_sfvb_redirect_import(storefront_oid, redirect_import_request)

Check a redirect import without writing it

Checks up to 5,000 rows against the existing rules and each other, and returns the findings per row with a plan_hash.  Writes nothing.  Rows are merged with the existing rules; nothing is ever deleted. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **redirect_import_request** | [**SfvbRedirectImportRequest**](SfvbRedirectImportRequest.md)| The request |

### Return type

[**SfvbRedirectImportResponse**](SfvbRedirectImportResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**413** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_sfvb_library_entry**
> SfvbLibraryEntry duplicate_sfvb_library_entry(storefront_oid, library_oid)

Copy a library entry into a new private entry

The copy is owned by the calling user and private.  From an entry you own it copies the draft; from one shared with you it copies the published revision.  It is scanned on its own and inherits nothing but content, its images and its screenshot. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |
 **name** | **str**| Name for the copy.  Defaults to Copy of and the source name. | [optional]

### Return type

[**SfvbLibraryEntry**](SfvbLibraryEntry.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_sfvb_page**
> SfvbPageResponse duplicate_sfvb_page(storefront_oid, page_duplicate_request)

Copy a page to a new path

Copies what the store admin's duplicate copies - settings, items, blog posts, permissions, attributes, selectors, images and the page folder with its body.  The copy goes to the path you choose, under any existing page, with the same path rules as creating a page, and a 409 with the code sfvb.page_exists when that path is taken.  The root page and pages with pages under them cannot be copied.  A page whose folder holds a started experiment is refused, because the copy would share the experiment - end it first.  Translated title and description text is not copied.  Always needs sfvb_publish, because the copy is live as soon as it exists. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **page_duplicate_request** | [**SfvbPageDuplicateRequest**](SfvbPageDuplicateRequest.md)| The page to copy and where |

### Return type

[**SfvbPageResponse**](SfvbPageResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_sfvb_theme**
> SfvbThemeJobResponse duplicate_sfvb_theme(storefront_oid, theme_oid, duplicate_request)

Duplicate a theme

Copies a theme into a new one and returns a job handle to poll.  Asynchronous, because copying a theme copies every file in it.  Needs sfvb_write rather than sfvb_publish, because the job explicitly does not activate what it creates, so the worst outcome of a mistaken call is a spare theme.  This is how you get somewhere safe to work - duplicate, edit the copy with an ordinary write scope, and let a human promote it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **theme_oid** | **int**|  |
 **duplicate_request** | [**SfvbThemeDuplicateRequest**](SfvbThemeDuplicateRequest.md)| Theme duplication details |

### Return type

[**SfvbThemeJobResponse**](SfvbThemeJobResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_sfvb_upsell_offer**
> SfvbUpsellOffer duplicate_sfvb_upsell_offer(storefront_oid, upsell_offer_oid)

Duplicate an upsell offer

A copy named Copy of, switched off, with its own copy of the container.  Put it on a path with a path update to have it shown. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_offer_oid** | **int**|  |

### Return type

[**SfvbUpsellOffer**](SfvbUpsellOffer.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_sfvb_upsell_path**
> SfvbUpsellPath duplicate_sfvb_upsell_path(storefront_oid, upsell_path_oid)

Duplicate an upsell path or one of its variations

Without a variation, copies the whole path right after it, switched off.  With a variation, appends a copy of that variation to the same path, which needs sfvb_publish when the path is running.  Every offer the copy uses is copied too and switched off.  Within this storefront only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_path_oid** | **int**|  |
 **duplicate_request** | [**SfvbUpsellPathDuplicateRequest**](SfvbUpsellPathDuplicateRequest.md)| What to duplicate | [optional]

### Return type

[**SfvbUpsellPath**](SfvbUpsellPath.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_sfvb_i18n_language**
> SfvbI18nLanguagesResponse enable_sfvb_i18n_language(storefront_oid, code, if_match, language_enable_request)

Enable a language

Turns a language on.  It is served to shoppers and machine translated, which is billed per character, so acknowledge_cost must be true and the caller must be a person (device authorization).  Records the same billing note as the merchant admin.  Already enabled answers changed false.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **code** | **str**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **language_enable_request** | [**SfvbI18nLanguageEnableRequest**](SfvbI18nLanguageEnableRequest.md)| The cost acknowledgement |

### Return type

[**SfvbI18nLanguagesResponse**](SfvbI18nLanguagesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_sfvb_smart_attribution**
> SfvbSmartAttribution enable_sfvb_smart_attribution(storefront_oid)

Turn Smart Attribution on in report_only mode

What the admin's Enable button saves: report_only, position_based, a 40/20/40 split, a 7 day lookback and every detected platform.  report_only records decisions and changes nothing any platform is sent.  A storefront that already has a configuration is 409 sfvb.smart_attribution_configured.  Needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbSmartAttribution**](SfvbSmartAttribution.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_sfvb_upsell_offer**
> SfvbUpsellOffer enable_sfvb_upsell_offer(storefront_oid, upsell_offer_oid)

Enable an upsell offer

Switches the offer on.  The only way to switch one on - create and update refuse active true on an offer that is off.  Needs sfvb_publish and the approval of the person who signed in the CLI, an approved upsell.enable request for this offer (see POST /sfvb/approvals).  An offer that is already on is returned unchanged, and no approval is used. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_offer_oid** | **int**|  |
 **approval_id** | **str**| The approval_id of an approved upsell.enable request for this offer.  Required when the offer is off.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbUpsellOffer**](SfvbUpsellOffer.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_sfvb_upsell_path**
> SfvbUpsellPath enable_sfvb_upsell_path(storefront_oid, upsell_path_oid)

Enable an upsell path

Switches the path on, so it starts running.  The only way to switch one on - create, update and unarchive refuse to.  An archived path is refused; unarchive it first.  Needs sfvb_publish and the approval of the person who signed in the CLI, an approved upsell.enable request for this path (see POST /sfvb/approvals).  A path that is already on is returned unchanged, and no approval is used. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_path_oid** | **int**|  |
 **approval_id** | **str**| The approval_id of an approved upsell.enable request for this path.  Required when the path is off.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbUpsellPath**](SfvbUpsellPath.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_sfvb_experiment**
> SfvbExperiment end_sfvb_experiment(storefront_oid, experiment_oid)

End an experiment

Ends a running experiment.  With winner_variation_number the winner gets every visitor, including visitors already assigned to another variation, and a page experiment's winning content is promoted into the page by the completion job on its next run, which also emails the merchant.  Without a winner a page experiment's id is cleared from its page body so the page shows variation 0, and a url experiment sends everyone to variation 0.  Always needs sfvb_publish, and the approval of the person who signed in the CLI - an approved experiment.end request for this experiment and winner.  An end with a winner always needs a fresh authenticator code; an end without a winner can be covered by the person's approval session (see POST /sfvb/approvals). 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **experiment_oid** | **int**|  |
 **approval_id** | **str**| The approval_id of an approved experiment.end request for this experiment and winner.  Required.  See POST /sfvb/approvals. | [optional]
 **experiment_end_request** | [**SfvbExperimentEndRequest**](SfvbExperimentEndRequest.md)| The winner, if any | [optional]

### Return type

[**SfvbExperiment**](SfvbExperiment.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_sfvb_not_found**
> SfvbNotFoundResponse export_sfvb_not_found(storefront_oid)

Export the open 404 paths

Up to 5,000 open paths, most hits first, as the admin's mapping spreadsheet reads them, each with where a redirect rule already sends it.  Fixed, mapped and ignored paths are never included.  Paths only bots have hit are left out unless include_bots is true.  Tokens in paths are redacted unless include_tokens is true.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **include_bots** | **bool**|  | [optional]
 **include_tokens** | **bool**|  | [optional]

### Return type

[**SfvbNotFoundResponse**](SfvbNotFoundResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorite_sfvb_library_entry**
> favorite_sfvb_library_entry(storefront_oid, library_oid)

Favorite a library entry

Bookmarks the entry for the calling user.  Idempotent.  Owner or anyone the entry is shared with. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |

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
**204** | No Content |  -  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fix_sfvb_not_found_entry**
> SfvbNotFoundEntry fix_sfvb_not_found_entry(storefront_oid, not_found_id)

Mark a 404 path fixed

For a path fixed by creating the page rather than a redirect.  It leaves the list; the next hit on the path clears the mark and lists it again.  The admin's Mark Fixed. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **not_found_id** | **str**|  |

### Return type

[**SfvbNotFoundEntry**](SfvbNotFoundEntry.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_affiliate_network**
> SfvbAffiliateNetwork get_sfvb_affiliate_network(storefront_oid, affiliate_network_oid)

Read one affiliate network

The network with its conversion_pixel, and the hash_sha256 an update or delete sends back as If-Match. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **affiliate_network_oid** | **int**|  |

### Return type

[**SfvbAffiliateNetwork**](SfvbAffiliateNetwork.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_affiliate_networks**
> SfvbAffiliateNetworksResponse get_sfvb_affiliate_networks(storefront_oid)

List a storefront's affiliate networks

Every affiliate network pixel, by name, with its settings and hash_sha256.  conversion_pixel is left out; its size and hash are shown.  Read one network for it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbAffiliateNetworksResponse**](SfvbAffiliateNetworksResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_approval**
> SfvbApproval get_sfvb_approval(approval_id)

Read one approval request

Poll this every interval_seconds after requesting an approval.  status is pending until the person decides, then approved or denied, and expired if nobody acts in 10 minutes.  Once the gated call has used it, status is used and outcome says whether the call succeeded.  Used with no outcome means the result is unknown, so check the target - never repeat the call. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_id** | **str**|  |

### Return type

[**SfvbApproval**](SfvbApproval.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_approvals**
> SfvbApprovalsResponse get_sfvb_approvals()

List this sign-in's approval requests

Requests made with this sign-in in the last 24 hours, newest first, at most 50, with their status and outcome.  Use it to find a request whose id was lost, or to see what an earlier run did. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters
This endpoint does not need any parameter.

### Return type

[**SfvbApprovalsResponse**](SfvbApprovalsResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_blog_post**
> SfvbBlogPostDetail get_sfvb_blog_post(storefront_oid, blog_post_oid)

Read a blog post

The whole post - body, excerpt, tags, images and where it is shown.  An image's url is the address to use for it in the body. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **blog_post_oid** | **int**|  |

### Return type

[**SfvbBlogPostDetail**](SfvbBlogPostDetail.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_campaign**
> SfvbCampaign get_sfvb_campaign(storefront_oid, campaign_uuid)

Get a campaign

One campaign, the same object as its list entry, with its emails and postcards in step order.  A deleted campaign is returned with deleted true. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **campaign_uuid** | **str**|  |

### Return type

[**SfvbCampaign**](SfvbCampaign.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_cjson_used_elements**
> SfvbElementsResponse get_sfvb_cjson_used_elements(compile_request)

Element types used by a container

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compile_request** | [**SfvbCompileRequest**](SfvbCompileRequest.md)| CJSON to inspect |

### Return type

[**SfvbElementsResponse**](SfvbElementsResponse.md)

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
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_dashboard_stats**
> SfvbCommsDashboardResponse get_sfvb_comms_dashboard_stats(storefront_oid)

Read every flow's and campaign's counts over a window, with the account's daily sending

rows cover each flow and campaign with activity in the last days (1 to 365, default 30); daily is the account's last 31 days of sending, whatever the window.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **days** | **int**| The window for the rows, 1 to 365 days (default 30). | [optional]

### Return type

[**SfvbCommsDashboardResponse**](SfvbCommsDashboardResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_email_clicks**
> SfvbCommsClicksResponse get_sfvb_comms_email_clicks(storefront_oid, commseq_uuid, email_uuid)

Read each link in one email and how often it was clicked

The email must be sent by an email or experiment step of this flow's or campaign's sequence; any other is 404.  Most clicked first, over the last days (1 to 365, default 30).  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **commseq_uuid** | **str**|  |
 **email_uuid** | **str**|  |
 **days** | **int**| The window, 1 to 365 days (default 30). | [optional]

### Return type

[**SfvbCommsClicksResponse**](SfvbCommsClicksResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_folder**
> SfvbCommsFolderResponse get_sfvb_comms_folder(storefront_oid, folder_uuid)

Read one list and segment folder

The folder, with the name and uuid of each list and segment filed in it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **folder_uuid** | **str**|  |

### Return type

[**SfvbCommsFolderResponse**](SfvbCommsFolderResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_folders**
> SfvbCommsFoldersResponse get_sfvb_comms_folders(storefront_oid)

List the list and segment folders

Each folder with how many lists and segments are filed in it, whether the admin made it, and its hash_sha256. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbCommsFoldersResponse**](SfvbCommsFoldersResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_list**
> SfvbCommsListResponse get_sfvb_comms_list(storefront_oid, list_uuid)

Read one email list

The list's name, folder, member count, public settings, and the campaigns and flows that use it, each with whether it is live.  hash_sha256 is the If-Match for a change or an archive.  Never its members. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **list_uuid** | **str**|  |

### Return type

[**SfvbCommsListResponse**](SfvbCommsListResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_list_members**
> SfvbCommsMembersResponse get_sfvb_comms_list_members(storefront_oid, list_uuid)

Read one page of a list's members

Each member's customer uuid, email and the date they joined.  Email addresses are masked (w***a@example.com) and customer_data is masked, unless show_customer_data is true, which returns the real addresses and needs the sfvb_publish scope.  Every such read is logged.  Ask for them only when the merchant needs a person's address.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **list_uuid** | **str**|  |
 **page** | **int**| The page, from 1 | [optional]
 **page_size** | **int**| Members per page, 1 to 100 (default 50) | [optional]
 **show_customer_data** | **bool**| True to return the real email addresses instead of masked ones | [optional]

### Return type

[**SfvbCommsMembersResponse**](SfvbCommsMembersResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_plan**
> SfvbCommsPlanResponse get_sfvb_comms_plan(storefront_oid)

Read the account's communications plan and sending health

The plan, its customer and email caps, what has been sent against them, and the spam pause, with notes on anything that stops sends.  Account-wide.  Never a price, fee or upgrade option; the plan is changed in the admin.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbCommsPlanResponse**](SfvbCommsPlanResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_providers**
> SfvbCommsProvidersResponse get_sfvb_comms_providers(storefront_oid)

List the email providers the account can import lists from

Each provider that can share list members, connected or not, with a connected one's lists.  Each call asks the providers themselves, so it is rate limited.  No credential or connect URL is returned.  import_allowed says whether the account may import.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbCommsProvidersResponse**](SfvbCommsProvidersResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_segment**
> SfvbCommsSegmentResponse get_sfvb_comms_segment(storefront_oid, segment_uuid)

Read one segment, with its rule

The segment's name, folder, rule, member count at its last rebuild, whether a rebuild is still due, and the campaigns and flows that use it, each with whether it is live.  hash_sha256 is the If-Match for an update.  Never its members, its Facebook audience, its ranking or its third party sync settings. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **segment_uuid** | **str**|  |

### Return type

[**SfvbCommsSegmentResponse**](SfvbCommsSegmentResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_segment_members**
> SfvbCommsMembersResponse get_sfvb_comms_segment_members(storefront_oid, segment_uuid)

Read one page of a segment's members

Each member's customer uuid, email and the date they joined.  Email addresses are masked (w***a@example.com) and customer_data is masked, unless show_customer_data is true, which returns the real addresses and needs the sfvb_publish scope.  Every such read is logged.  Ask for them only when the merchant needs a person's address.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **segment_uuid** | **str**|  |
 **page** | **int**| The page, from 1 | [optional]
 **page_size** | **int**| Members per page, 1 to 100 (default 50) | [optional]
 **show_customer_data** | **bool**| True to return the real email addresses instead of masked ones | [optional]

### Return type

[**SfvbCommsMembersResponse**](SfvbCommsMembersResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_sending_domain**
> SfvbCommsSendingDomain get_sfvb_comms_sending_domain(domain)

Read a sending domain

One sending domain as stored.  To check an amazon domain's DNS again, use the status call. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  |

### Return type

[**SfvbCommsSendingDomain**](SfvbCommsSendingDomain.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_sending_domains**
> SfvbCommsSendingDomainsResponse get_sfvb_comms_sending_domains()

List the sending domains

Every domain the account sends email from, with its provider, verification status and the DNS records an amazon domain needs.  mailgun_api_key is always a mask. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters
This endpoint does not need any parameter.

### Return type

[**SfvbCommsSendingDomainsResponse**](SfvbCommsSendingDomainsResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_sequence_stats**
> SfvbCommsSequenceStatsResponse get_sfvb_comms_sequence_stats(storefront_oid, commseq_uuid)

Read a flow's or campaign's counts, overall and step by step

overall covers all time; each email, SMS, postcard and branch step covers the last days (1 to 365, default 30).  Each step reports only the counts its channel records and names the rest in not_measured, so a missing count is never zero.  Bounces, opens and spam are counts here, not separate reports.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **commseq_uuid** | **str**|  |
 **days** | **int**| The window for the step counts, 1 to 365 days (default 30). | [optional]

### Return type

[**SfvbCommsSequenceStatsResponse**](SfvbCommsSequenceStatsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_settings**
> SfvbCommsSettingsResponse get_sfvb_comms_settings(storefront_oid)

Read a storefront's communications settings

The postcard return address, the default marketing and transactional senders, and the default SMS number, with what each one drives in notes.  Read only.  hash_sha256 is the If-Match for an update. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbCommsSettingsResponse**](SfvbCommsSettingsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_template**
> SfvbCommsTemplateResponse get_sfvb_comms_template(storefront_oid, email_template_oid)

Read one saved email template's body

A system template or one saved on this storefront; any other is 404.  container_cjson is the body.  The Velocity template it renders inside is named in email_template_vm_path, not shown.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **email_template_oid** | **int**|  |

### Return type

[**SfvbCommsTemplateResponse**](SfvbCommsTemplateResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_templates**
> SfvbCommsTemplatesResponse get_sfvb_comms_templates(storefront_oid)

List the email templates a new email can start from

One list: UltraCart's system templates and this storefront's saved ones (each with email_template_oid), then base templates, the active theme's files an email renders inside (each with path).  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbCommsTemplatesResponse**](SfvbCommsTemplatesResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_comms_twilio_account**
> SfvbCommsTwilioAccountResponse get_sfvb_comms_twilio_account()

Read the Twilio account

The account's Twilio account, used for SMS and the phone system, or none.  An account has at most one.  auth_token is always a mask. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters
This endpoint does not need any parameter.

### Return type

[**SfvbCommsTwilioAccountResponse**](SfvbCommsTwilioAccountResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_container**
> SfvbContainerResponse get_sfvb_container(storefront_oid, owner_type, owner_object_id)

Read a container stored outside the file system

owner_type is one of upsell, email, postcardfront, postcardback, item or itemid.  It also says how owner_object_id is read - item and upsell take an oid, itemid takes a merchant item id, and the rest take an esp uuid.  itemid reaches the same containers as item and is the way to address one from a storefront, where data-context-item-id carries the merchant item id and the oid appears nowhere.  Item containers also require container_name.  Theme and page containers are files; read those through files/content. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **owner_type** | **str**|  |
 **owner_object_id** | **str**|  |
 **container_name** | **str**|  | [optional]

### Return type

[**SfvbContainerResponse**](SfvbContainerResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_container_version**
> SfvbContainerVersion get_sfvb_container_version(storefront_oid, container_history_oid)

Read the CJSON stored in one container history entry

Inspect or diff an earlier version without reverting to it.  The version is addressed through the container that owns it, so a history oid belonging to some other resource cannot be read through this route.  owner_type also says how owner_object_id is read, and itemid addresses an item container by merchant item id. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **container_history_oid** | **int**|  |
 **owner_type** | **str**|  | [optional]
 **owner_object_id** | **str**|  | [optional]
 **container_name** | **str**|  | [optional]

### Return type

[**SfvbContainerVersion**](SfvbContainerVersion.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_element**
> SfvbElementSchemaResponse get_sfvb_element(element_type)

Configuration schema and field card for one element type

schema is the draft-07 JSON schema for the element config object and doc is the markdown field card, both as strings.  Either is omitted when none has been published for the element, which is still a 200.  The catalog is published by the visual builder release process, and a republish can take up to an hour to appear here. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **element_type** | **str**|  |

### Return type

[**SfvbElementSchemaResponse**](SfvbElementSchemaResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_email**
> SfvbEmail get_sfvb_email(storefront_oid, email_uuid)

Get a flow or campaign email's subject and preview text

The subject, preview text and hash_sha256 to send as If-Match when updating them, with whether the email is live and its review state.  The body is the email container (owner type email).  Find the uuid in the storefront's campaigns and flows. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **email_uuid** | **str**|  |

### Return type

[**SfvbEmail**](SfvbEmail.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_events**
> SfvbEventsResponse get_sfvb_events()

Replay events

The signed-in person's events after the cursor, oldest first.  Events are kept 72 hours; an older cursor returns resync_required, and then the caller re-lists what it was waiting on.  Events about one sign-in's requests, such as approvals, are only returned to that sign-in.  limit is 1 to 500, default 100. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Return events after this event_id.  Leave it out for every event kept. | [optional]
 **storefront_oid** | **int**| Only events about this storefront, plus merchant-level ones. | [optional]
 **limit** | **int**| At most this many events, 1 to 500. | [optional]

### Return type

[**SfvbEventsResponse**](SfvbEventsResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_events_authorization**
> SfvbEventsAuthResponse get_sfvb_events_authorization()

Open the event stream

Returns a websocket URL and a single-use token, valid for 5 minutes, for the signed-in person's event stream.  Events are thin hints, type and ids only, and the stream is at most once.  Re-read the object before acting, and after every reconnect replay from the last event_id with GET events.  Send ping messages to keep the connection open, and reconnect with a new token before two hours.  Requires a token that resolves to a user, so use the device authorization flow. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **events_auth_request** | [**SfvbEventsAuthRequest**](SfvbEventsAuthRequest.md)| Optional storefront filter | [optional]

### Return type

[**SfvbEventsAuthResponse**](SfvbEventsAuthResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_experiment**
> SfvbExperiment get_sfvb_experiment(storefront_oid, experiment_oid)

Read one experiment and its statistics

The experiment, its variations and their statistics, and with daily=true each variation's daily rows.  p95_sessions_needed is estimated only after 1000 sessions, and sessions_needed_computed_dts says when.  For a url experiment, router_url is the address visitors must enter through. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **experiment_oid** | **int**|  |
 **daily** | **bool**| Include each variation&#39;s daily statistics | [optional]

### Return type

[**SfvbExperiment**](SfvbExperiment.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_experiment_objectives**
> SfvbExperimentObjectivesResponse get_sfvb_experiment_objectives(storefront_oid)

List the objectives an experiment can optimize

Each objective with what is measured per session and compared between variations, the usual optimization type, and whether it needs an event name. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbExperimentObjectivesResponse**](SfvbExperimentObjectivesResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_file_content**
> SfvbFileContentResponse get_sfvb_file_content(storefront_oid)

Read a storefront file

Returns the current content, or an earlier version when version is supplied.  Send the body's hash_sha256 back as If-Match when writing.  The ETag header carries the same hash, but a compressing proxy may append a suffix such as -gzip to it, so prefer the body value. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**|  | [optional]
 **version** | **int**|  | [optional]

### Return type

[**SfvbFileContentResponse**](SfvbFileContentResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**413** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_file_upload_url**
> SfvbFileUploadUrlResponse get_sfvb_file_upload_url(storefront_oid, extension)

Get a URL to upload a binary asset to

Binary content does not travel through this API as JSON, so uploading an image, font, video or PDF is two steps.  Ask here for a URL, PUT the raw bytes straight to it, then call uploadSfvbFile quoting the key you were given.  The bytes never pass through the API server.  The extension is checked against the accepted type list before a URL is issued, so an unsupported type fails here rather than after you have sent the file.  The URL is short lived and the key is bound to your account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **extension** | **str**|  |

### Return type

[**SfvbFileUploadUrlResponse**](SfvbFileUploadUrlResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_flow**
> SfvbFlow get_sfvb_flow(storefront_oid, flow_uuid)

Get a flow

One flow, the same object as its list entry, with its emails and postcards in step order.  A deleted flow is returned with deleted true. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **flow_uuid** | **str**|  |

### Return type

[**SfvbFlow**](SfvbFlow.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_i18n_glossary**
> SfvbI18nGlossary get_sfvb_i18n_glossary(storefront_oid)

Read the storefront's translation glossary

The storefront's glossary, plain markdown with terms not to translate, required translations, tone and words to avoid.  Read it before translating anything.  Empty when none has been saved.  Each storefront has its own, because a storefront is often its own brand. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbI18nGlossary**](SfvbI18nGlossary.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_i18n_languages**
> SfvbI18nLanguagesResponse get_sfvb_i18n_languages(storefront_oid)

List a storefront's languages

Every language the storefront can be translated into, with UltraCart's three-letter code (ESP for Spanish), the other spellings accepted, whether it is enabled, the default and right to left.  Language maps in CJSON and render take the code.  English is the source of every string.  Also gives the machine translation estimate for one more language, and the hash_sha256 an enable or disable sends back. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbI18nLanguagesResponse**](SfvbI18nLanguagesResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_i18n_machine_translations**
> SfvbI18nMachineTranslationsResponse get_sfvb_i18n_machine_translations(storefront_oid)

Read where a widget setting's translations come from

For one multilingual widget setting, named by widget_id and property on a theme (the active theme unless theme_oid is given), each enabled language's text and whether a shopper sees a hand translation from the language map, a machine translation, one still queued (pending) or none yet.  The setting is registered when its container is saved.  Nothing is generated by reading it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **theme_oid** | **int**|  | [optional]
 **widget_id** | **str**|  | [optional]
 **_property** | **str**|  | [optional]

### Return type

[**SfvbI18nMachineTranslationsResponse**](SfvbI18nMachineTranslationsResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_i18n_message**
> SfvbI18nMessage get_sfvb_i18n_message(storefront_oid, key)

Read one built-in message

One message by key, with the hash_sha256 a set or reset sends back. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **key** | **str**|  |
 **theme_oid** | **int**|  | [optional]

### Return type

[**SfvbI18nMessage**](SfvbI18nMessage.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_i18n_message_machine_translations**
> SfvbI18nMachineTranslationsResponse get_sfvb_i18n_message_machine_translations(storefront_oid, key)

Read where a message's translations come from

For one message, each enabled language's text and whether a shopper sees a hand translation, a machine translation, one still queued (pending) or none yet.  Nothing is generated by reading it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **key** | **str**|  |
 **theme_oid** | **int**|  | [optional]

### Return type

[**SfvbI18nMachineTranslationsResponse**](SfvbI18nMachineTranslationsResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_item**
> SfvbItemResponse get_sfvb_item(storefront_oid)

Read an item's storefront facing content

The attributes, images, title, description and search metadata a StoreFront element can render, reconciled against the templates behind the pages this item sits on.  An attribute a template declares but nothing has set comes back present with an empty value, which is how you discover what the page is asking for.  Pricing and related items have their own calls, items/pricing and items/related.  Shipping, inventory, tax, variants and kit structure stay with the item API.  Address by merchant_item_id, the value data-context-item-id carries, or by merchant_item_oid. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **merchant_item_id** | **str**| The merchant item id, as a storefront carries it | [optional]
 **merchant_item_oid** | **int**| The item oid.  Send this or merchant_item_id, not both | [optional]

### Return type

[**SfvbItemResponse**](SfvbItemResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_item_pricing**
> SfvbItemPricing get_sfvb_item_pricing(storefront_oid)

Read what an item charges

Price, sale (with whether it applies now), MSRP and retail volume pricing - what itemprice, itemsale, itemmsrp, itemsavings and itemvolumediscounts render - with a hash_sha256 to send as If-Match when changing it.  Wholesale pricing tiers are not shown.  Address by merchant_item_id or merchant_item_oid. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **merchant_item_id** | **str**|  | [optional]
 **merchant_item_oid** | **int**|  | [optional]

### Return type

[**SfvbItemPricing**](SfvbItemPricing.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_item_related**
> SfvbItemRelated get_sfvb_item_related(storefront_oid)

Read an item's related items

What itemrelateditemslist lists - the merchant's own related items (user, addon, complementary) and the ones UltraCart calculates (system), with a hash_sha256 to send as If-Match when changing them. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **merchant_item_id** | **str**|  | [optional]
 **merchant_item_oid** | **int**|  | [optional]

### Return type

[**SfvbItemRelated**](SfvbItemRelated.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_library_entry**
> SfvbLibraryEntry get_sfvb_library_entry(storefront_oid, library_oid)

Read one library entry including its CJSON

The owner gets the draft with its hash_sha256, which an update, delete or publish sends back as If-Match.  Everyone else gets the latest published revision.  Pin a published revision with revision_number.  Read content_manifest before installing.  If the fragment references images or other storefront files those paths will not resolve on this storefront until the entry is installed, so use install rather than this when the intent is to place the fragment. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |
 **revision_number** | **int**| A published revision to read instead of the default. | [optional]

### Return type

[**SfvbLibraryEntry**](SfvbLibraryEntry.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_library_history**
> SfvbLibraryHistoryResponse get_sfvb_library_history(storefront_oid, library_oid)

List a library entry's published revisions

Newest first, each with its release notes and hash.  Read one with getSfvbLibraryEntry and revision_number.  The owner and anyone the entry is shared with can list it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |

### Return type

[**SfvbLibraryHistoryResponse**](SfvbLibraryHistoryResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_library_share_targets**
> SfvbLibraryShareTargetsResponse get_sfvb_library_share_targets(storefront_oid)

List the accounts a library entry can be shared with

The calling account's linked accounts, each with its merchant id and company.  These are the only merchants a share can name. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbLibraryShareTargetsResponse**](SfvbLibraryShareTargetsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_library_taxonomy**
> SfvbLibraryTaxonomyCatalog get_sfvb_library_taxonomy(storefront_oid)

List the allowed library tags

The fixed tag list for purpose, section, industry and style, each tag with a one line description.  Saving an entry refuses any tag not on it with sfvb.library_taxonomy_unknown, naming the closest one.  The same tags are the facet_purpose, facet_section, facet_industry and facet_style search facets. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbLibraryTaxonomyCatalog**](SfvbLibraryTaxonomyCatalog.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_menu**
> SfvbMenu get_sfvb_menu(storefront_oid, code)

Read one store menu and its entries

The whole tree, in render order.  Page entries carry the page_path they resolve to and item entries the merchant_item_id, rather than the oids the storage keeps.  Menu item oids are not returned at all because a write regenerates every one of them.  Keep hash_sha256 - it is the If-Match a write needs. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **code** | **str**| Menu code, matched without regard to case |

### Return type

[**SfvbMenu**](SfvbMenu.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_menus**
> SfvbMenusResponse get_sfvb_menus(storefront_oid)

List a storefront's store menus

The menus a menu element's menuName can name, sorted by code and without their entries.  A code the active theme's templates ask for but nothing has created is included with unconfigured true - that code renders an empty list today, and writing it creates it.  A menu no template names is marked undeclared, which usually means a menuName is misspelled. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbMenusResponse**](SfvbMenusResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_not_found**
> SfvbNotFoundResponse get_sfvb_not_found(storefront_oid)

List the paths that answered 404

The paths shoppers asked for that answered 404, most hits first or by last_seen.  Paths only, never query strings.  Bots are left out unless include_bots.  Token-like path segments show as {token} unless include_tokens.  A path stays listed after a redirect rule catches it, with redirected_to set.  redirected=false lists only paths no rule catches yet, and redirected=true only those one does.  limit is 1 to 100, default 50. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **since** | **str**|  | [optional]
 **sort** | **str**|  | [optional]
 **include_bots** | **bool**|  | [optional]
 **include_tokens** | **bool**|  | [optional]
 **q** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **redirected** | **bool**|  | [optional]

### Return type

[**SfvbNotFoundResponse**](SfvbNotFoundResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_not_found_entry**
> SfvbNotFoundEntryResponse get_sfvb_not_found_entry(storefront_oid, not_found_id)

Read one 404 path with its recent hits

One entry with up to 100 recent hits, each with its time, the linking host, the user agent and whether it was a bot.  Client IP addresses are never returned. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **not_found_id** | **str**|  |
 **include_tokens** | **bool**|  | [optional]

### Return type

[**SfvbNotFoundEntryResponse**](SfvbNotFoundEntryResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_not_found_page**
> SfvbNotFoundPage get_sfvb_not_found_page(storefront_oid)

What renders the storefront's 404 page

The site_404.vm the active theme renders for a 404, found the way the storefront finds it, and whether it exists.  Without it the storefront serves a plain fallback.  Edit it with the file endpoints. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbNotFoundPage**](SfvbNotFoundPage.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_not_found_summary**
> SfvbNotFoundSummary get_sfvb_not_found_summary(storefront_oid)

The 404 log's trend

The admin's 404 charts: hits per day for 30 and 7 days and per hour for 24 hours, bots included, plus up to 10 open paths first seen in the last 30 days.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbNotFoundSummary**](SfvbNotFoundSummary.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_page**
> SfvbPageResponse get_sfvb_page(storefront_oid, path)

Read a page's attributes and images

What the pageattribute and pageimage elements render for this page.  These are not in any file, which is why a page folder can be empty and its elements still render something.  Attributes and image codes a template declares but nothing has set are included, so the response describes what the page can show rather than only what has been saved. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /catalog/dispensers/ |

### Return type

[**SfvbPageResponse**](SfvbPageResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_page_blog_posts**
> SfvbPageBlogPostsResponse get_sfvb_page_blog_posts(storefront_oid, path)

Read the blog posts assigned to a page

The posts the page shows.  uses_selectors is true when the page's blog post selectors choose them instead. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /blog/ |

### Return type

[**SfvbPageBlogPostsResponse**](SfvbPageBlogPostsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_page_items**
> SfvbPageItemsResponse get_sfvb_page_items(storefront_oid, path)

Read the items assigned to a page

The items on the page with their sort order and url part.  uses_selectors is true when the page's selectors choose its items instead. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /lp/spring-sale/ |

### Return type

[**SfvbPageItemsResponse**](SfvbPageItemsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_page_selectors**
> SfvbPageSelectors get_sfvb_page_selectors(storefront_oid, path)

Read a page's selectors

The conditions that choose the page's items and blog posts, and whether each set must all match. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /lp/spring-sale/ |

### Return type

[**SfvbPageSelectors**](SfvbPageSelectors.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_postcard_tracking**
> SfvbPostcardTrackingResponse get_sfvb_postcard_tracking(storefront_oid, postcard_uuid)

Read one page of the cards mailed for a postcard

Every printed card mailed for the postcard, newest first, with its status, cost, dates and the order it converted to.  Recipients are masked (the name an initial, the street lines hidden, city, state and postal code kept) and the vendor's status text is left out, unless show_customer_data is true, which needs the sfvb_publish scope and is logged.  The return address is the merchant's own.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **postcard_uuid** | **str**|  |
 **page** | **int**| The page, from 1 | [optional]
 **page_size** | **int**| Cards per page, 1 to 100 (default 50) | [optional]
 **show_customer_data** | **bool**| True to return the recipients&#39; real names and street addresses | [optional]

### Return type

[**SfvbPostcardTrackingResponse**](SfvbPostcardTrackingResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_preview_url**
> SfvbPreviewUrlResponse get_sfvb_preview_url(storefront_oid, preview_session_id)

URL that renders a preview session

Refuses a session that does not exist, so a URL you receive is for a session that was really there.  expires_in_seconds is the time actually remaining, not the configured lifetime.  Needs a token that resolves to a user, because a preview session belongs to the person who created it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **preview_session_id** | **str**|  |
 **path** | **str**|  | [optional]

### Return type

[**SfvbPreviewUrlResponse**](SfvbPreviewUrlResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_recording**
> SfvbRecordingResponse get_sfvb_recording(storefront_oid, screen_recording_uuid)

Get a screen recording

One recorded visitor session and its page views, with each page view's named events such as rage clicks, script errors and checkout errors, but without the replay data.  Fetch a page view's replay events separately.  Find recordings to look at from the heatmaps or the analytics warehouse.  The visitor's email, IP address and visitor id are not returned, nor what they typed into form fields.  Reading a recording does not mark it watched. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **screen_recording_uuid** | **str**|  |

### Return type

[**SfvbRecordingResponse**](SfvbRecordingResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_recording_page_view_events**
> SfvbRecordingEventsResponse get_sfvb_recording_page_view_events(storefront_oid, screen_recording_uuid, screen_recording_page_view_uuid)

Get one recorded page view's replay events

The rrweb events for one page view, as a JSON array in a string, for replaying on the caller's own machine.  Card fields are masked by the recorder, but other text the visitor typed can appear.  Limited per account to 30 page views a minute, 300 an hour and 1000 a day.  Reading the events does not mark the recording watched. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **screen_recording_uuid** | **str**|  |
 **screen_recording_page_view_uuid** | **str**|  |

### Return type

[**SfvbRecordingEventsResponse**](SfvbRecordingEventsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_recording_settings**
> SfvbRecordingSettingsResponse get_sfvb_recording_settings(storefront_oid)

Get the storefront's screen recording settings

Whether real shoppers' sessions on this storefront are being recorded, what recording costs per 1,000 sessions after the 14 day free trial, how long recordings are kept, and how many sessions were recorded in the current and last billing periods.  Recording only collects from the moment it is turned on, so when it is on but was turned on recently, check the analytics warehouse for rows before reporting that there is no data. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbRecordingSettingsResponse**](SfvbRecordingSettingsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_redirect**
> SfvbRedirect get_sfvb_redirect(storefront_oid, redirect_id)

Read one redirect rule

One rule, with the hash_sha256 to send as If-Match when updating or deleting it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **redirect_id** | **int**|  |

### Return type

[**SfvbRedirect**](SfvbRedirect.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_redirects**
> SfvbRedirectsResponse get_sfvb_redirects(storefront_oid)

List the storefront's redirect rules

Every redirect rule, exact and pattern.  Filter with q (searches source, target and note), type (exact or pattern) and status (301, 302 or rewrite).  count and limit say how close the storefront is to its rule limit. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **q** | **str**|  | [optional]
 **type** | **str**|  | [optional]
 **status** | **str**|  | [optional]

### Return type

[**SfvbRedirectsResponse**](SfvbRedirectsResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_secret_kinds**
> SfvbSecretKindsResponse get_sfvb_secret_kinds()

List the secrets this server collects

The kinds of secret value, with what each looks like, and the secret fields (sinks) a handle can be written to.  Request a handle for a sink with POST secrets. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters
This endpoint does not need any parameter.

### Return type

[**SfvbSecretKindsResponse**](SfvbSecretKindsResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_secret_request**
> SfvbSecretRequest get_sfvb_secret_request(request_id)

Read one secret request

Poll this every interval_seconds after making a request.  status is pending until a person enters the values, then fulfilled, and expired if nobody does within 24 hours.  handles lists each handle with its own status, and a fingerprint (the last few characters as a mask shows them) once its value is entered.  Never a value. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  |

### Return type

[**SfvbSecretRequest**](SfvbSecretRequest.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_secret_requests**
> SfvbSecretRequestsResponse get_sfvb_secret_requests()

List this sign-in's secret requests

Requests made with this sign-in in the last 24 hours, newest first, at most 50, without their handles.  Read one request for its handles. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters
This endpoint does not need any parameter.

### Return type

[**SfvbSecretRequestsResponse**](SfvbSecretRequestsResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_sequence**
> SfvbSequence get_sfvb_sequence(storefront_oid, sequence_uuid)

Get a campaign's or flow's steps as a tree

The communication sequence named by a campaign's or flow's communication_sequence_uuid, with its steps from the start in order.  Only condition, split and InboxGeek steps branch, and each holds its two sides in branches.  Each step has its type, the admin's label, its settings (a webhook's header and parameter values masked), its audience filter, the emails, postcard, lists or items it names, and the hash_sha256 to send as If-Match when changing it.  waiting adds how many customers are waiting on each step now.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **sequence_uuid** | **str**|  |
 **waiting** | **bool**| Include how many customers are waiting on each step | [optional]

### Return type

[**SfvbSequence**](SfvbSequence.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_sequence_step_dispatch_logs**
> SfvbStepDispatchLogsResponse get_sfvb_sequence_step_dispatch_logs(storefront_oid, sequence_uuid, step_uuid)

Read a flow or campaign step's dispatch log and counts

Why customers were sent, skipped or ended at this step, newest first, as the admin's Dispatch Logs screen shows it, with the step's counts.  An email step's counts are its email's; any other step's are its own over 90 days.  Email addresses and phone numbers in the text are masked.  since is 15m, 2h or 7d, or an ISO-8601 time, default 7d; entries are kept 90 days.  limit is 1 to 200, default 50; send next_offset as offset for the next page.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **sequence_uuid** | **str**|  |
 **step_uuid** | **str**|  |
 **since** | **str**|  | [optional]
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]

### Return type

[**SfvbStepDispatchLogsResponse**](SfvbStepDispatchLogsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_server_log**
> SfvbServerLogDetail get_sfvb_server_log(storefront_oid, log_id)

Get one storefront render log

One render's server log with its lines, each with a level, a category such as VELOCITY or FLOW, and the message.  log_id comes from the list, or from the X-UltraCart-Storefront-Log-Id header a page sends inside an SFVB preview session.  min_level is debug, info, warn or error, default debug. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **log_id** | **str**|  |
 **min_level** | **str**|  | [optional]

### Return type

[**SfvbServerLogDetail**](SfvbServerLogDetail.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_site_attributes**
> SfvbSiteAttributesResponse get_sfvb_site_attributes(storefront_oid)

Read a storefront's site attributes

The values the siteattribute element and $site.attr render.  These are not in any file or theme.  Attributes a template declares but nothing has set are included with the template's default, so the response describes what the templates can render rather than only what has been saved.  Credentials stored as site attributes are never included. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbSiteAttributesResponse**](SfvbSiteAttributesResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_site_seo**
> SfvbSiteSeo get_sfvb_site_seo(storefront_oid)

Read a storefront's search engine settings

Canonical Links, Schema.org and Prevent Indexing as true or false, with the default meta description and keywords and the hash to send as If-Match on a change. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbSiteSeo**](SfvbSiteSeo.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_sitemaps**
> SfvbSitemapsResponse get_sfvb_sitemaps(storefront_oid)

Read a storefront's sitemaps and robots.txt

The sitemaps the admin SEO Sitemaps screen lists, with their child files and build times, the Sitemap lines robots.txt serves, and whether Prevent Indexing is on.  Read only.  The files are rebuilt nightly, so a page change shows in them after the next build. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbSitemapsResponse**](SfvbSitemapsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_smart_attribution**
> SfvbSmartAttribution get_sfvb_smart_attribution(storefront_oid)

Read a storefront's Smart Attribution configuration

The mode, model, global credit split, lookback and platforms, the platforms detected from the tracking integrations that are not configured yet, and the hash_sha256 a change or delete sends back as If-Match.  When configured is false the values are the defaults an enable would save. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbSmartAttribution**](SfvbSmartAttribution.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_test_orders**
> SfvbTestOrdersResponse get_sfvb_test_orders(storefront_oid)

List recent test orders

Test orders on this account only, newest first, with no customer details, so an agent can render the order pages (receipt, order tracking, digital downloads, auto order pages) with one.  Use an order_id as a render's context_order_id; a real customer's order is refused there.  The last 7 days are searched, widening to 30 and then 90 until enough are found.  digital_items and auto_order keep only orders with downloads or an auto order.  limit is 1 to 25, default 10. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **limit** | **int**|  | [optional]
 **digital_items** | **bool**|  | [optional]
 **auto_order** | **bool**|  | [optional]

### Return type

[**SfvbTestOrdersResponse**](SfvbTestOrdersResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_theme**
> SfvbTheme get_sfvb_theme(storefront_oid, theme_oid)

Get a theme

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **theme_oid** | **int**|  |

### Return type

[**SfvbTheme**](SfvbTheme.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_theme_attributes**
> SfvbThemeAttributesResponse get_sfvb_theme_attributes(storefront_oid, theme_oid)

Read a theme's colors, fonts and settings

The values theme.css and the compiled containers resolve at render time.  These do NOT live in any file.  settings.json contains a palette and looks like the answer, but it is the theme's factory template - it supplies defaults for slots that have never been set and is ignored for slots that have, so editing it will not change a color and reading it will not tell you the current one.  Slots a template declares but nothing has ever set are included here, carrying the default they will render with, so the response describes the whole theme rather than the rows that happen to exist. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **theme_oid** | **int**|  |

### Return type

[**SfvbThemeAttributesResponse**](SfvbThemeAttributesResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_theme_job**
> SfvbThemeJobResponse get_sfvb_theme_job(storefront_oid, job_id)

Status of an asynchronous theme job

Poll until complete is true, then check success.  Note that the new theme's oid is not returned.  The job's product is a plain text report rather than a structured result, so once it completes, list themes and match on the target_path the start call gave you. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **job_id** | **int**|  |

### Return type

[**SfvbThemeJobResponse**](SfvbThemeJobResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_tracking_html**
> SfvbTrackingHtml get_sfvb_tracking_html(storefront_oid, slot)

Read one custom tracking HTML slot

The HTML with its Velocity tokens as stored, and the hash_sha256 a write sends back as If-Match. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **slot** | **str**| tracking or conversion |

### Return type

[**SfvbTrackingHtml**](SfvbTrackingHtml.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_tracking_html_slots**
> SfvbTrackingHtmlResponse get_sfvb_tracking_html_slots(storefront_oid)

List a storefront's custom tracking HTML slots

tracking (every page but the receipt) and conversion (the receipt only), each with its size and hash_sha256.  Read one slot for its content. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbTrackingHtmlResponse**](SfvbTrackingHtmlResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_tracking_provider**
> SfvbTrackingProvider get_sfvb_tracking_provider(storefront_oid, provider)

Read one tracking provider

The provider as the list shows it, with the hash_sha256 a change or clear sends back as If-Match. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **provider** | **str**|  |

### Return type

[**SfvbTrackingProvider**](SfvbTrackingProvider.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_tracking_providers**
> SfvbTrackingProvidersResponse get_sfvb_tracking_providers(storefront_oid)

List a storefront's tracking providers

Every provider on the admin's Google and Other tabs, with each field's type and value, its consent gate, events, OAuth connection state and hash_sha256.  A secret's value is never returned, only whether one is set, its mask and the sink to request a handle for.  configured=true lists only the providers that are on. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **configured** | **bool**|  | [optional]

### Return type

[**SfvbTrackingProvidersResponse**](SfvbTrackingProvidersResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_tracking_settings**
> SfvbTrackingSettingsResponse get_sfvb_tracking_settings(storefront_oid)

Read a storefront's privacy rules and advanced conversion settings

The five privacy rules (which shoppers each applies to) and the advanced conversion settings, each section with the hash_sha256 a write sends back as If-Match.  The order hash secret key is shared by every storefront on the account and is reported only as set or not. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbTrackingSettingsResponse**](SfvbTrackingSettingsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_transactional_email**
> SfvbTransactionalEmailResponse get_sfvb_transactional_email(storefront_oid, file_name)

Read a transactional email's subject, delivery options and sender

file_name is the template file from the transactional email list, such as receipt_html.vm, or its display name.  The sender is shared by every storefront on the same screen branding theme (sender_shared_with); a sender that sends through the merchant's own mail server shows smtp true and never its credentials.  hash_sha256 is the If-Match for an update.  The template itself is a theme file. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **file_name** | **str**|  |

### Return type

[**SfvbTransactionalEmailResponse**](SfvbTransactionalEmailResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_transactional_emails**
> SfvbTransactionalEmailsResponse get_sfvb_transactional_emails(storefront_oid)

List the transactional emails a storefront sends

The order, shipment, auto order and other transactional emails this storefront sends, with their template files and the body container a draft replaces.  Forgot password and chat verification are not listed, because they have no preview. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbTransactionalEmailsResponse**](SfvbTransactionalEmailsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_upsell_offer**
> SfvbUpsellOffer get_sfvb_upsell_offer(storefront_oid, upsell_offer_oid)

Get an upsell offer

The whole offer, with the hash an update sends back in If-Match, which upsell items are out of stock now, and whether loyalty, TowerData and Everflow are set up.  Stats as on the path list. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_offer_oid** | **int**|  |
 **stats** | **bool**| Include stats | [optional]
 **stats_start** | **str**| Stats window start, YYYY-MM-DD | [optional]
 **stats_end** | **str**| Stats window end, YYYY-MM-DD | [optional]
 **stats_weekdays** | **str**| Only these weekdays, comma separated mon to sun | [optional]

### Return type

[**SfvbUpsellOffer**](SfvbUpsellOffer.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_upsell_path**
> SfvbUpsellPath get_sfvb_upsell_path(storefront_oid, upsell_path_oid)

Get an upsell path

The whole path, with the hash an update sends back in If-Match.  Stats as on the list. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_path_oid** | **int**|  |
 **stats** | **bool**| Include stats | [optional]
 **stats_start** | **str**| Stats window start, YYYY-MM-DD | [optional]
 **stats_end** | **str**| Stats window end, YYYY-MM-DD | [optional]
 **stats_weekdays** | **str**| Only these weekdays, comma separated mon to sun | [optional]

### Return type

[**SfvbUpsellPath**](SfvbUpsellPath.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_utm_shortcode**
> SfvbUtmShortcode get_sfvb_utm_shortcode(storefront_oid, shortcode_oid)

Read one UTM shortcode

The shortcode with the hash_sha256 an update or delete sends back as If-Match.  A deleted shortcode is 404. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **shortcode_oid** | **int**|  |

### Return type

[**SfvbUtmShortcode**](SfvbUtmShortcode.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_utm_shortcodes**
> SfvbUtmShortcodesResponse get_sfvb_utm_shortcodes(storefront_oid)

List a storefront's UTM shortcodes

Every live shortcode, sorted by code, each with its hash_sha256.  q matches the code or the description, ignoring case. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **q** | **str**|  | [optional]

### Return type

[**SfvbUtmShortcodesResponse**](SfvbUtmShortcodesResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_version**
> SfvbVersionResponse get_sfvb_version()

Compiler version for this merchant

The visual builder release channel is per merchant, so a CLI holding cached schema or element data should compare against this to know when it has gone stale. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters
This endpoint does not need any parameter.

### Return type

[**SfvbVersionResponse**](SfvbVersionResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sfvb_whoami**
> SfvbWhoamiResponse get_sfvb_whoami()

Who this token is

Returns the merchant, user, granted scopes and reachable storefronts for the calling token.  Declared for any scope so an application can always discover which account it is connected to. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters
This endpoint does not need any parameter.

### Return type

[**SfvbWhoamiResponse**](SfvbWhoamiResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ignore_sfvb_not_found_entry**
> SfvbNotFoundEntry ignore_sfvb_not_found_entry(storefront_oid, not_found_id)

Ignore a 404 path

Hides one path from the list and stops counting its hits, for example scanner noise.  Reversible. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **not_found_id** | **str**|  |

### Return type

[**SfvbNotFoundEntry**](SfvbNotFoundEntry.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_sfvb_comms_provider_lists**
> SfvbCommsProviderImportResponse import_sfvb_comms_provider_lists(storefront_oid, provider_import_request)

Import lists from another email provider

Each list becomes a new list of the same name on this storefront and every member is subscribed, in the background; the signed-in user is emailed when it finishes.  Needs the account to be allowed to import, sfvb_publish, and an approved comms_list.import request for exactly these lists.  At most 20 lists.  dry_run checks the provider and the list ids and names what would be created, without importing or using an approval. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **provider_import_request** | [**SfvbCommsProviderImportRequest**](SfvbCommsProviderImportRequest.md)| The provider and lists to import |
 **approval_id** | **str**| The approval_id of an approved comms_list.import request for exactly these lists.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbCommsProviderImportResponse**](SfvbCommsProviderImportResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_sfvb_redirects**
> SfvbRedirectImportResponse import_sfvb_redirects(storefront_oid, redirect_import_request)

Apply a reviewed redirect import

Applies exactly the rows of a dry run, given its plan_hash, in one transaction.  Refused with 412 when the rows or the storefront's rules changed since the dry run, and refused when any row has a blocking finding.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **redirect_import_request** | [**SfvbRedirectImportRequest**](SfvbRedirectImportRequest.md)| The request |

### Return type

[**SfvbRedirectImportResponse**](SfvbRedirectImportResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**413** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_affiliate_network**
> SfvbAffiliateNetwork insert_sfvb_affiliate_network(storefront_oid, affiliate_network_request)

Add an affiliate network

network_name, parameter_name and parameter_value are required; the rest start from the admin's defaults.  Internal affiliate oids must be the account's own.  Needs sfvb_publish.  A network with a conversion_pixel that a custom or server_to_server network will use needs an approved affiliate_network.change request for exactly this create (Approval-Id), which UltraCart reviews first.  dry_run says whether it needs one, without saving. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **affiliate_network_request** | [**SfvbAffiliateNetworkRequest**](SfvbAffiliateNetworkRequest.md)| The network |
 **approval_id** | **str**| For a network with a conversion pixel it will use, the approval_id of an approved affiliate_network.change request for exactly this create.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbAffiliateNetwork**](SfvbAffiliateNetwork.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**413** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_approval**
> SfvbApproval insert_sfvb_approval(approval_request)

Request a human approval

Asks the person who signed in the CLI to approve one gated action on one exact target.  Name the storefront with the storefront_oid query parameter.  The target is checked the way the action will check it, so nobody is asked to approve a call that would fail.  Show the person approval_url and user_code, poll GET approvals/{approval_id} every interval_seconds, and once it is approved repeat the gated call with the approval_id in the Approval-Id header.  Asking again for the same thing returns the pending request (200) rather than a new one (201).  A request lapses after 10 minutes.  Requires a token that resolves to a user, so use the device authorization flow.  For file.put_script send the script as content, or params.version for a revert; for tracking_html.put send the HTML as content and params.slot; for affiliate_network.change send affiliate_network.  These three start as reviewing while UltraCart's scanner and two AI models read the content, then become pending with the review attached, or refused.  Keep polling, and show approval_url only once it is pending.  Only the hash is kept, so the write must send the same content. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_request** | [**SfvbApprovalCreateRequest**](SfvbApprovalCreateRequest.md)| The request |
 **storefront_oid** | **int**| The storefront the action runs on.  Required for storefront actions, left out for account-wide ones. | [optional]

### Return type

[**SfvbApproval**](SfvbApproval.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_blog_post**
> SfvbBlogPostDetail insert_sfvb_blog_post(storefront_oid, blog_post_request)

Create a blog post

title and url_part are required.  The post is a draft unless visibility says otherwise, and anything but a draft needs sfvb_publish.  The body and excerpt are refused with sfvb.unsafe_html if they could run script, and a url_part another post uses is refused with a 409 and sfvb.blog_post_exists.  Assign the post to a page with pages/blog_posts/add, or let the page's selectors choose it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **blog_post_request** | [**SfvbBlogPostRequest**](SfvbBlogPostRequest.md)| The blog post to create |

### Return type

[**SfvbBlogPostDetail**](SfvbBlogPostDetail.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_comms_folder**
> SfvbCommsFolderResponse insert_sfvb_comms_folder(storefront_oid, folder_write_request)

Create a list and segment folder

A new, empty folder.  File a list or segment in it by setting its folder_uuid. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **folder_write_request** | [**SfvbCommsFolderWriteRequest**](SfvbCommsFolderWriteRequest.md)| The new folder&#39;s name |

### Return type

[**SfvbCommsFolderResponse**](SfvbCommsFolderResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_comms_list**
> SfvbCommsListResponse insert_sfvb_comms_list(storefront_oid, list_write_request)

Create an email list

A new, empty list with the name, folder and public settings given.  public_description is plain text, since subscribers see it on the email preferences page. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **list_write_request** | [**SfvbCommsListWriteRequest**](SfvbCommsListWriteRequest.md)| The new list&#39;s name, folder and public settings |

### Return type

[**SfvbCommsListResponse**](SfvbCommsListResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_comms_segment**
> SfvbCommsSegmentResponse insert_sfvb_comms_segment(storefront_oid, segment_write_request)

Create a segment

A new segment with the name, rule and folder given.  The rule needs at least one group, each with at least one function of a rule type the segment rebuild knows, and any list or segment it names must be on this storefront.  The segment starts empty and rebuilds in the background; member_count is out of date until rebuild_required is false. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **segment_write_request** | [**SfvbCommsSegmentWriteRequest**](SfvbCommsSegmentWriteRequest.md)| The new segment&#39;s name, rule and folder |

### Return type

[**SfvbCommsSegmentResponse**](SfvbCommsSegmentResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_comms_sending_domain**
> SfvbCommsSendingDomain insert_sfvb_comms_sending_domain(sending_domain)

Add a sending domain

Adds a domain to send email from.  An amazon domain starts verification with Amazon SES and returns the DNS records to publish; the person signed in also gets them by email.  A mailgun domain needs mailgun_api_key as a secret handle made for the domain (POST secrets, sink mailgun.domain.api_key), never the key itself.  UltraCart sets up its webhooks on the Mailgun domain with the key; if Mailgun refuses, nothing is saved and the handle is given back unused. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sending_domain** | [**SfvbCommsSendingDomain**](SfvbCommsSendingDomain.md)| The sending domain |

### Return type

[**SfvbCommsSendingDomain**](SfvbCommsSendingDomain.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |
**502** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_comms_twilio_account**
> SfvbCommsTwilioAccountResponse insert_sfvb_comms_twilio_account(twilio_account)

Connect the Twilio account

Connects the account's Twilio account with account_sid and auth_token.  Send auth_token as a secret handle made for that account SID (POST secrets, sink twilio.account.auth_token), never the token itself.  UltraCart checks the token with Twilio, then makes its API key, TwiML apps and voice encryption key on the account, as the admin does.  If Twilio refuses, nothing is saved and the handle is given back unused.  An account has at most one Twilio account, so this is refused when one exists; update it instead. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **twilio_account** | [**SfvbCommsTwilioAccount**](SfvbCommsTwilioAccount.md)| The Twilio account |

### Return type

[**SfvbCommsTwilioAccountResponse**](SfvbCommsTwilioAccountResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |
**502** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_page**
> SfvbPageResponse insert_sfvb_page(storefront_oid, page_create_request)

Create a page

Creates the page and its folder, the way the store admin's add page does.  The parent page must already exist, and the last part of the path may only contain letters, digits, hyphens and underscores - it is refused, not cleaned.  A path that already has a page is refused with a 409 and the code sfvb.page_exists.  Without a group_template the page inherits its parent's templates, or catalog_group.vm directly under the root.  Set attributes and images afterwards with the page attribute and image endpoints, and push the body to the page folder.  Always needs sfvb_publish, because the page is live as soon as it exists.  Deleting, moving and renaming pages stay in the store admin. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **page_create_request** | [**SfvbPageCreateRequest**](SfvbPageCreateRequest.md)| The page to create |

### Return type

[**SfvbPageResponse**](SfvbPageResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_redirect**
> SfvbRedirectResponse insert_sfvb_redirect(storefront_oid, redirect_request)

Create a 301 redirect rule

Creates one permanent (301) redirect, live for shoppers at once.  Refused for a loop, a chain longer than the storefront follows, a duplicate source, a target that is missing or on another site, a system path, a live page (unless over_live_page) and a full storefront.  A chain is allowed with a warning naming the final target.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **redirect_request** | [**SfvbRedirectRequest**](SfvbRedirectRequest.md)| The request |

### Return type

[**SfvbRedirectResponse**](SfvbRedirectResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_secret_request**
> SfvbSecretRequest insert_sfvb_secret_request(secret_request)

Ask a person to enter secret values

Never ask for a credential in the conversation.  This makes a handle for each sink (and each key, for a bulk request) at once, pending until a person enters the values on request_url.  Show the person request_url and user_code and never open or fill in the page yourself.  Poll GET secrets/{request_id} every interval_seconds until status is fulfilled, then send each handle in its secret field.  The server writes the value in its place.  A handle works only for this sign-in, its sink and its target, for ttl_seconds and uses writes.  A request lapses after 24 hours, and shares the five pending requests a sign-in has with approvals.  Asking again for the same thing returns the pending request (200) rather than a new one (201).  Requires a token that resolves to a user, so use the device authorization flow.  A secret request is never an approval. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_request** | [**SfvbSecretRequestCreate**](SfvbSecretRequestCreate.md)| The request |

### Return type

[**SfvbSecretRequest**](SfvbSecretRequest.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_sequence_step**
> SfvbSequenceStepCreateResponse insert_sfvb_sequence_step(storefront_oid, sequence_uuid, if_match, sequence_step_create_request)

Add an email step, with its new email, a wait step, or a postcard step, with its new postcard

type email (the default) creates a new email with the subject and preview text and adds the email step that sends it, together, so a failure leaves neither.  The email has no body yet, and gets the content review flags the admin gives a new email here.  With library_item_oid the email starts from a code library email item instead (listSfvbCodeLibraryEmails): its body with new element ids, and its subject and preview text where the request gives none.  The item must be this account's own, shared with it, or published, approved by UltraCart and free; it must pass the library content scanner and the email container rules, and executable elements need acknowledge_executable true.  Its PNG, JPEG and GIF image files are copied into the storefront first, never over an existing file; any other file is skipped and listed.  type wait adds a wait step with config_json as its settings: delay_duration and delay_duration_unit (minutes, hours, days, weeks or months), or a delay_until option; a wait that would pass customers on at once is refused.  type post_card creates a new postcard with the admin's default front and back and adds the postcard step that mails it, together; the step starts disabled, so nothing is printed or mailed until it is turned on with set-config, and the response names the front and back containers.  Any goes right after after_step_uuid, or first on one side of a condition, split or inboxgeek step (branch_step_uuid with side).  Send that step's hash_sha256 as If-Match.  A sequence with no steps yet takes neither place and If-Match *, and gets begin and end steps around the new step, as the admin's editor adds them.  A sequence whose campaign or flow is live needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **sequence_uuid** | **str**|  |
 **if_match** | **str**| The hash_sha256 of the step it goes after, or of the branching step, or * for the first step of a sequence with no steps.  Required; 428 when absent, 412 when stale. |
 **sequence_step_create_request** | [**SfvbSequenceStepCreateRequest**](SfvbSequenceStepCreateRequest.md)| Where the step goes, and the new email&#39;s subject and preview text or code library item, the wait&#39;s config_json, or the postcard step&#39;s name |

### Return type

[**SfvbSequenceStepCreateResponse**](SfvbSequenceStepCreateResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_upsell_offer**
> SfvbUpsellOffer insert_sfvb_upsell_offer(storefront_oid, upsell_offer)

Create an upsell offer

Every item it names must exist, and every shipping method, payment method and loyalty tier must be one the merchant has.  Put it on a path with a path update to have it shown.  It must be created with active false, and switched on with the enable call, which needs approval.  upsell_item_id_javascript or offsite_content_url needs sfvb_publish.  Its page content is its container, written with the container endpoints and owner type upsell. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_offer** | [**SfvbUpsellOffer**](SfvbUpsellOffer.md)| The offer to create |

### Return type

[**SfvbUpsellOffer**](SfvbUpsellOffer.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_upsell_path**
> SfvbUpsellPath insert_sfvb_upsell_path(storefront_oid, upsell_path)

Create an upsell path

Placed last in path order.  Every offer a step names must be an offer of this storefront, and every item in the item logic must exist.  It must be created with active false, and switched on with the enable call, which needs approval. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_path** | [**SfvbUpsellPath**](SfvbUpsellPath.md)| The path to create |

### Return type

[**SfvbUpsellPath**](SfvbUpsellPath.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_sfvb_utm_shortcode**
> SfvbUtmShortcode insert_sfvb_utm_shortcode(storefront_oid, utm_shortcode_request)

Create a UTM shortcode

code is letters, digits, underscore and hyphen, 1 to 50 characters, and at least one UTM or ITM value is required.  A code another live shortcode has, ignoring case, is 409 sfvb.utm_shortcode_exists.  A code that is one of the account's affiliate short codes is 409 sfvb.utm_shortcode_affiliate_conflict, because the storefront checks those first and this one would never fire.  Up to 5,000 per storefront.  Needs sfvb_write only, because no link sent before it existed changes. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **utm_shortcode_request** | [**SfvbUtmShortcodeRequest**](SfvbUtmShortcodeRequest.md)| The shortcode |

### Return type

[**SfvbUtmShortcode**](SfvbUtmShortcode.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_sfvb_library_entry**
> SfvbLibraryInstallReceipt install_sfvb_library_entry(storefront_oid, library_oid)

Install a library entry into a storefront

Copies the fragment's referenced files into the storefront file system and returns a receipt with the CJSON's paths resolved, ready to place.  It never places the CJSON.  Read content_manifest first; executable content needs acknowledge_executable true.  A file that already exists with different content is a conflict - on_conflict fail (the default) refuses with 409 and writes nothing, skip keeps the existing file, overwrite replaces it.  A recipient installs a published revision.  This writes, which is why it is a POST, and it requires sfvb_publish because the files land in the shared storefront file system, which is served to shoppers whichever theme is active. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |
 **install_request** | [**SfvbLibraryInstallRequest**](SfvbLibraryInstallRequest.md)| Revision, conflict handling and acknowledgement | [optional]

### Return type

[**SfvbLibraryInstallReceipt**](SfvbLibraryInstallReceipt.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_blog_posts**
> SfvbBlogPostsResponse list_sfvb_blog_posts(storefront_oid)

List the storefront's blog posts

One page of blog posts, newest first, without their bodies.  search matches the title, body, excerpt, url part or author, or a tag exactly.  unassigned marks posts no page shows yet.  Use a post's blog_post_oid to assign it to a page. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **search** | **str**| Text to search for | [optional]
 **page** | **int**| Page number, starting at 1 | [optional]
 **page_size** | **int**| Posts per page, 1 to 100, default 50 | [optional]

### Return type

[**SfvbBlogPostsResponse**](SfvbBlogPostsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_campaigns**
> SfvbCampaignsResponse list_sfvb_campaigns(storefront_oid)

List the storefront's campaigns

One page of campaigns, newest first, each with its emails and postcards in step order, without their container JSON.  search matches the campaign name.  Deleted campaigns are left out unless include_deleted is true.  live is true unless the status sends nothing (draft or archived), so a change to one of its emails reaches customers at once. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **search** | **str**| Text to search for in the name | [optional]
 **page** | **int**| Page number, starting at 1 | [optional]
 **page_size** | **int**| Campaigns per page, 1 to 100, default 50 | [optional]
 **include_deleted** | **bool**| Include deleted campaigns | [optional]

### Return type

[**SfvbCampaignsResponse**](SfvbCampaignsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_code_library_emails**
> SfvbCodeLibraryEmailsResponse list_sfvb_code_library_emails(storefront_oid)

Email items from the code library that can start a new email step

The code library is the one the admin's \"start from library\" uses; it isn't the Visual Builder element library.  Lists the email items this account may use, by title: its own (source owned), those shared with it (shared), and those published for everyone, approved by UltraCart and free (public).  search matches part of the title, with case.  Each kind is capped at 100 items, and truncated says when there were more.  Send an item's library_item_oid on the step insert to start a new email from it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **search** | **str**| Part of the title to match, with case.  Up to 100 characters. | [optional]

### Return type

[**SfvbCodeLibraryEmailsResponse**](SfvbCodeLibraryEmailsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_comms_lists**
> SfvbCommsListsResponse list_sfvb_comms_lists(storefront_oid)

List the storefront's email lists

Each list's uuid, name and member count, by name, for a campaign's memberships or a list trigger.  Never its members.  Archived lists are left out. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbCommsListsResponse**](SfvbCommsListsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_comms_segments**
> SfvbCommsSegmentsResponse list_sfvb_comms_segments(storefront_oid)

List the storefront's segments

Each segment's uuid, name and member count at its last rebuild, by name, for a campaign's memberships or a segment trigger.  Never its members or its rule.  Archived segments are left out. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbCommsSegmentsResponse**](SfvbCommsSegmentsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_container_versions**
> SfvbContainerVersionsResponse list_sfvb_container_versions(storefront_oid)

Version history for a container stored outside the file system

Addressed the same way as the container itself, so owner_type also says how owner_object_id is read and itemid lists the history of the item container that merchant item id names. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **owner_type** | **str**|  | [optional]
 **owner_object_id** | **str**|  | [optional]
 **container_name** | **str**|  | [optional]

### Return type

[**SfvbContainerVersionsResponse**](SfvbContainerVersionsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_elements**
> SfvbElementsResponse list_sfvb_elements()

List every SFVB element type

The authoritative vocabulary, taken from the same lookup the compiler uses.  A type absent from this list compiles to a literal placeholder line in the page rather than failing, which is why validation treats an unknown type as an error. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters
This endpoint does not need any parameter.

### Return type

[**SfvbElementsResponse**](SfvbElementsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_experiments**
> SfvbExperimentsResponse list_sfvb_experiments(storefront_oid)

List the storefront's experiments

Every experiment that is not deleted, with its variations and their statistics - the same numbers the store admin shows.  Filter by status, by type (page, url, theme, openai), or by the page an experiment runs on.  auto_ends_at says when the engine will end an experiment by itself, and p_value is a one-way ANOVA across all variations.  Read one experiment for its daily statistics. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **status** | **str**| Running or Ended | [optional]
 **type** | **str**| page, url, theme or openai | [optional]
 **path** | **str**| Only experiments on this page, for example /lp/spring-sale/ | [optional]

### Return type

[**SfvbExperimentsResponse**](SfvbExperimentsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_file_versions**
> SfvbFileVersionsResponse list_sfvb_file_versions(storefront_oid)

Version history for a storefront file

Version history is the undo for anything in the storefront file system, which is what makes an agent's writes recoverable. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**|  | [optional]

### Return type

[**SfvbFileVersionsResponse**](SfvbFileVersionsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_files**
> SfvbFilesResponse list_sfvb_files(storefront_oid)

List a storefront directory

Directories first, then files, each sorted by name.  Address by path or by directory oid; supplying theme_oid also retries a path that does not resolve at the storefront root relative to that theme, so /theme/css/ works without knowing the theme's directory name.  Each file carries its content hash, so a listing is enough to start an If-Match write without a separate read. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**|  | [optional]
 **storefront_fs_directory_oid** | **int**|  | [optional]
 **theme_oid** | **int**|  | [optional]
 **max_entries** | **int**|  | [optional]

### Return type

[**SfvbFilesResponse**](SfvbFilesResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_flows**
> SfvbFlowsResponse list_sfvb_flows(storefront_oid)

List the storefront's flows

One page of flows, newest first, each with its trigger and its emails and postcards in step order, without their container JSON.  search matches the flow name.  Deleted flows are left out unless include_deleted is true.  live is true unless the status sends nothing (draft or inactive); a paused flow still holds enrolled customers, so it counts as live. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **search** | **str**| Text to search for in the name | [optional]
 **page** | **int**| Page number, starting at 1 | [optional]
 **page_size** | **int**| Flows per page, 1 to 100, default 50 | [optional]
 **include_deleted** | **bool**| Include deleted flows | [optional]

### Return type

[**SfvbFlowsResponse**](SfvbFlowsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_i18n_messages**
> SfvbI18nMessagesResponse list_sfvb_i18n_messages(storefront_oid)

List built-in messages

The system text templates render by key, such as checkout labels, for one theme (the active theme unless theme_oid is given).  Each message has its English, whether it was edited, and each enabled language's text with its source (hand, machine, pending or none).  A message appears the first time a page renders it.  q matches the key or the English.  overridden keeps messages with an edited English or a hand translation.  Paged by offset and limit (default 200, at most 500). 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **theme_oid** | **int**|  | [optional]
 **q** | **str**|  | [optional]
 **language** | **str**|  | [optional]
 **overridden** | **bool**|  | [optional]
 **offset** | **int**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**SfvbI18nMessagesResponse**](SfvbI18nMessagesResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_item_containers**
> SfvbItemContainersResponse list_sfvb_item_containers(storefront_oid)

List the item containers on the account

An itemcontainer element renders nothing of its own.  It names a slot, and a separate container is resolved per item for that slot, so a catalog of five hundred products with three slots is fifteen hundred containers.  This says which of them exist.  Filter by container_name to find every item carrying one slot, or by merchant_item_id to see what one item has.  Which items are missing a slot is a set difference against pages/items, because a listing can only report containers that exist.  Each row carries hash_sha256, so a listing is enough to start an If-Match write without reading the container first.  Item containers are stored per account rather than per storefront, so storefront_oid identifies the caller's storefront but does not narrow the result. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **merchant_item_id** | **str**| Restrict to one item, by the merchant item id a storefront carries | [optional]
 **merchant_item_oid** | **int**| Restrict to one item, by oid.  Send this or merchant_item_id, not both | [optional]
 **container_name** | **str**| Restrict to one slot name, matched without regard to case | [optional]
 **max_results** | **int**|  | [optional]
 **offset** | **int**|  | [optional]

### Return type

[**SfvbItemContainersResponse**](SfvbItemContainersResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_library_installs**
> SfvbLibraryInstallsResponse list_sfvb_library_installs(storefront_oid)

List the library entries installed on a storefront

Each entry's most recently installed revision, its latest published revision and update_available.  Nothing updates automatically.  An entry this account can no longer see is listed without its name. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbLibraryInstallsResponse**](SfvbLibraryInstallsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_pages**
> SfvbPageListResponse list_sfvb_pages(storefront_oid)

List the storefront's pages

Every page with its settings, sorted by path with the root first.  Hidden pages are included.  Pass under to list one page and everything below it.  Read from the same cached catalog the admin page tree uses, so a page created a moment ago can take a moment to appear here - read it directly with the single-page read to confirm a write. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **under** | **str**| Only this page and the pages below it, for example /lp/ | [optional]

### Return type

[**SfvbPageListResponse**](SfvbPageListResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_server_logs**
> SfvbServerLogsResponse list_sfvb_server_logs(storefront_oid)

List recent storefront render logs

The server log the storefront Developer Tools panel shows, one per page render, newest first and without the log text.  Each carries counts of error and warning lines, including Velocity problems such as a null #set, so a failing render stands out without reading every log.  Filter by uri (a case insensitive contains match on the rendered address) and errors_only.  since is 15m, 2h or 1d, or an ISO-8601 time, default 1h; logs are kept for seven days and only the newest 1000.  With a filter the newest 200 logs in the window are searched, and more_available says whether older ones were left unread. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **uri** | **str**|  | [optional]
 **since** | **str**|  | [optional]
 **errors_only** | **bool**|  | [optional]
 **limit** | **int**|  | [optional]

### Return type

[**SfvbServerLogsResponse**](SfvbServerLogsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_storefronts**
> SfvbStorefrontsResponse list_sfvb_storefronts()

List storefronts

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters
This endpoint does not need any parameter.

### Return type

[**SfvbStorefrontsResponse**](SfvbStorefrontsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_templates**
> SfvbTemplatesResponse list_sfvb_templates(storefront_oid)

List the active theme's templates

Each template with the page type it declares and what it can render - items, sub-pages, blog posts, pagination, visual builder containers.  A page's group_template names one of these.  The storefront's fixed templates, such as checkout and my account, are flagged system and must never be assigned to a page. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **page_type** | **str**| Only templates declaring this page type, for example group | [optional]

### Return type

[**SfvbTemplatesResponse**](SfvbTemplatesResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_themes**
> SfvbThemesResponse list_sfvb_themes(storefront_oid)

List themes for a storefront

Exactly one theme is flagged active.  Writing to the active theme is writing live and requires the sfvb_publish scope. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |

### Return type

[**SfvbThemesResponse**](SfvbThemesResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_upsell_offers**
> SfvbUpsellOffersResponse list_sfvb_upsell_offers(storefront_oid)

List upsell offers

Every offer on one of this storefront's paths that are not archived, the same list the admin shows, with each offer's full settings but not its container JSON.  An offer on no path yet is still read by oid.  A large container size alongside a small element count is the signature of markup pasted into a single html element.  Stats as on the path list. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **stats** | **bool**| Include stats | [optional]
 **stats_start** | **str**| Stats window start, YYYY-MM-DD | [optional]
 **stats_end** | **str**| Stats window end, YYYY-MM-DD | [optional]
 **stats_weekdays** | **str**| Only these weekdays, comma separated mon to sun | [optional]

### Return type

[**SfvbUpsellOffersResponse**](SfvbUpsellOffersResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sfvb_upsell_paths**
> SfvbUpsellPathsResponse list_sfvb_upsell_paths(storefront_oid)

List upsell paths

In path order, first to last.  status current (the default) leaves out archived paths.  Stats are computed only with stats=true, over stats_start to stats_end (YYYY-MM-DD, the last 30 days when both are omitted, at most 366 days), because they are the expensive part of the read. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **status** | **str**| current, archived or all | [optional]
 **location** | **str**| pre checkout or post checkout | [optional]
 **search** | **str**| Only paths whose name contains this | [optional]
 **stats** | **bool**| Include stats | [optional]
 **stats_start** | **str**| Stats window start, YYYY-MM-DD | [optional]
 **stats_end** | **str**| Stats window end, YYYY-MM-DD | [optional]
 **stats_weekdays** | **str**| Only these weekdays, comma separated mon to sun | [optional]
 **max_results** | **int**| Page size, 1 to 500, default 100 | [optional]
 **offset** | **int**| Offset of the first path returned | [optional]

### Return type

[**SfvbUpsellPathsResponse**](SfvbUpsellPathsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_sfvb_sequence_step**
> SfvbSequenceStepMoveResponse move_sfvb_sequence_step(storefront_oid, sequence_uuid, step_uuid, if_match, sequence_step_move_request)

Move one step

Moves the step, in one transaction, to right after after_step_uuid (the begin step puts it first in the sequence) or to the start of one side of a condition, split or inboxgeek step (branch_step_uuid with side).  The step keeps its uuid, settings and the email or postcard it sends: nothing is archived or created.  Refused for the begin, end, continue and merge markers, for a condition, split or inboxgeek step, while any customer is waiting on the step, and when the new place is the one it is in.  Send the step's hash_sha256 as If-Match, and the hash_sha256 of after_step_uuid or branch_step_uuid as anchor_hash_sha256.  A sequence whose campaign or flow is live needs sfvb_publish and an approved sequence_step.move approval (Approval-Id); a draft or inactive one needs neither. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **sequence_uuid** | **str**|  |
 **step_uuid** | **str**|  |
 **if_match** | **str**| The moved step&#39;s hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **sequence_step_move_request** | [**SfvbSequenceStepMoveRequest**](SfvbSequenceStepMoveRequest.md)| Where the step moves, and the hash of the step it goes next to |
 **approval_id** | **str**| When the sequence is live, the approval_id of an approved sequence_step.move request for exactly this move.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbSequenceStepMoveResponse**](SfvbSequenceStepMoveResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_sfvb_upsell_path**
> SfvbUpsellPath move_sfvb_upsell_path(storefront_oid, upsell_path_oid, move_request)

Move an upsell path

Up, down, to the top or to the bottom of the storefront's paths.  Order decides which running path a shopper meets first, so moving a running path needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_path_oid** | **int**|  |
 **move_request** | [**SfvbUpsellPathMoveRequest**](SfvbUpsellPathMoveRequest.md)| Where to move it |

### Return type

[**SfvbUpsellPath**](SfvbUpsellPath.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proof_sfvb_sequence_postcard**
> SfvbPostcardProofResponse proof_sfvb_sequence_postcard(storefront_oid, sequence_uuid, step_uuid, postcard_proof_request)

Proof a postcard step without mailing it

Renders both sides of the step's postcard as a send renders them, then has the print vendor render the card as a dry run.  Returns the HTML of each side, the PNG image of each side that the vendor prints from, the vendor's thumbnails and its proof PDF.  The QR code is the short link a send prints.  No card is printed or mailed, nothing is billed, the step is not changed, and no coupon is created.  A unique coupon code shows as PREVIEW-UNIQUE.  The image urls are public.  html_only returns the HTML alone, with no vendor render.  An order must be a test order.  cart_item_ids fills the cart a cart flow card shows.  Works whether the step is on or off. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **sequence_uuid** | **str**|  |
 **step_uuid** | **str**|  |
 **postcard_proof_request** | [**SfvbPostcardProofRequest**](SfvbPostcardProofRequest.md)| Who the card is addressed to, and the order or cart it shows |

### Return type

[**SfvbPostcardProofResponse**](SfvbPostcardProofResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |
**502** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_sfvb_library_entry**
> SfvbLibraryEntry publish_sfvb_library_entry(storefront_oid, library_oid, if_match, publish_request)

Publish a library entry's draft

Freezes the draft as a published revision at its revision_number and sets who can see it.  Owner only, with the draft's hash_sha256 as If-Match.  Always needs sfvb_publish, because it changes what other merchants can install.  Images, fonts, stylesheets and media must be relative paths, and credential shaped strings are refused.  Public also needs the library publisher property on the account and no executable content at all - no script, html, embed, css or velocity elements.  After those checks an automated AI review reads the fragment, which can take up to about a minute.  A clear violation both of its models agree on refuses any publish with sfvb.library_ai_review_blocked.  A public publish also needs its approval, otherwise sfvb.library_ai_review_inconclusive.  The result is in content_manifest.ai_review. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **publish_request** | [**SfvbLibraryPublishRequest**](SfvbLibraryPublishRequest.md)| Visibility and release notes |

### Return type

[**SfvbLibraryEntry**](SfvbLibraryEntry.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_container**
> SfvbContainerResponse put_sfvb_container(storefront_oid, owner_type, owner_object_id, if_match, container_write_request)

Write a container stored outside the file system

Validation is mandatory and runs here regardless of whether the caller validated first.  The previous value is snapshotted before the write, so the change can be reverted.  Side effects the visual builder performs on save, such as upsell screenshot regeneration and email content review flagging, are applied too.  owner_type also says how owner_object_id is read; send itemid to address an item container by merchant item id rather than by oid.  Either way the history records the one canonical address, so a container written under one spelling is listed and reverted under the other. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **owner_type** | **str**|  |
 **owner_object_id** | **str**|  |
 **if_match** | **str**| CJSON hash from the last read.  Required; 428 when absent, 412 when stale. |
 **container_write_request** | [**SfvbContainerWriteRequest**](SfvbContainerWriteRequest.md)| Container CJSON to write |
 **container_name** | **str**|  | [optional]

### Return type

[**SfvbContainerResponse**](SfvbContainerResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_experiment_variation**
> SfvbExperiment put_sfvb_experiment_variation(storefront_oid, experiment_oid, variation_number, experiment_variation_update_request)

Pause or resume a variation

Stops or resumes sending new visitors to one variation of a running experiment.  Visitors already assigned keep seeing it.  Variation 0 cannot be paused, because the split falls back to it, and the last variation still receiving visitors cannot be paused.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **experiment_oid** | **int**|  |
 **variation_number** | **int**|  |
 **experiment_variation_update_request** | [**SfvbExperimentVariationUpdateRequest**](SfvbExperimentVariationUpdateRequest.md)| Pause or resume |

### Return type

[**SfvbExperiment**](SfvbExperiment.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_file_content**
> SfvbFileWriteResponse put_sfvb_file_content(storefront_oid, if_match, file_write_request)

Write a storefront file

Runs the template sandbox, Velocity validation and the internationalization check, records a version, and compiles the sibling .vm when the file is a .cjson under a theme.  Send If-Match with the hash from the last read to avoid clobbering a concurrent change.  Writing into the active theme requires sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **if_match** | **str**| Content hash from the last read.  Required; 428 when absent, 412 when stale. |
 **file_write_request** | [**SfvbFileWriteRequest**](SfvbFileWriteRequest.md)| File content to write |
 **path** | **str**|  | [optional]
 **approval_id** | **str**| For a .js or .mjs file, the approval_id of an approved file.put_script request for exactly these bytes.  Required for scripts.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbFileWriteResponse**](SfvbFileWriteResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**413** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_i18n_glossary**
> SfvbI18nGlossary put_sfvb_i18n_glossary(storefront_oid, glossary_request)

Replace the storefront's translation glossary

Replaces the whole glossary, plain markdown up to 64 KB.  The server stores it and never interprets it; the agent follows it.  Send the hash_sha256 you read as If-Match, except for the first save.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **glossary_request** | [**SfvbI18nGlossaryRequest**](SfvbI18nGlossaryRequest.md)| The glossary |
 **if_match** | **str**| hash_sha256 from the last read.  Not needed for the first save; otherwise 428 when absent, 412 when stale. | [optional]

### Return type

[**SfvbI18nGlossary**](SfvbI18nGlossary.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |
**413** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_i18n_message**
> SfvbI18nMessage put_sfvb_i18n_message(storefront_oid, key, if_match, message_write_request)

Change one built-in message

Sets one message in any number of languages.  ENG replaces the English, which drops its machine translations so they regenerate.  Any other language becomes a hand translation.  Languages not named are left alone.  Empty text removes that language's translation so machine translation fills it again (not allowed for ENG); it is the undo for an imported message, which can't be reset.  Shoppers see it at once.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **key** | **str**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **message_write_request** | [**SfvbI18nMessageWriteRequest**](SfvbI18nMessageWriteRequest.md)| The languages to change |
 **theme_oid** | **int**|  | [optional]

### Return type

[**SfvbI18nMessage**](SfvbI18nMessage.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_item_attributes**
> SfvbItemResponse put_sfvb_item_attributes(storefront_oid, item_attribute_update_request)

Change some of an item's attributes

Partial - only the attributes named change, and an empty value empties one but keeps it on the item.  To remove an attribute no template declares, use the attribute DELETE.  Every entry is validated before any is written, so a refusal leaves the item untouched.  The list types are checked against the shape their renderer actually parses, which matters more than it sounds: a definition list is a bare array with one letter keys, a video list is a wrapper object with keys spelled out, and an item set is comma separated text rather than JSON.  A shape the renderer cannot read is not reported at render time - it renders exactly like an attribute nobody ever set. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **item_attribute_update_request** | [**SfvbItemAttributeUpdateRequest**](SfvbItemAttributeUpdateRequest.md)| Attributes to change |
 **merchant_item_id** | **str**|  | [optional]
 **merchant_item_oid** | **int**|  | [optional]

### Return type

[**SfvbItemResponse**](SfvbItemResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_item_content**
> SfvbItemResponse put_sfvb_item_content(storefront_oid, item_content_request)

Change an item's title or long description

Partial - a field left out is untouched, a field sent empty is cleared, and those are different things.  These are what itemtitle and itemdescription render.  Writing the matching config keys into a container does nothing, because they are dialog buffers bound to the item and the render never reads them.  Both are the catalog's own fields, so a change here reaches the item everywhere, not only on this storefront. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **item_content_request** | [**SfvbItemContentRequest**](SfvbItemContentRequest.md)| Title and description to change |
 **merchant_item_id** | **str**|  | [optional]
 **merchant_item_oid** | **int**|  | [optional]

### Return type

[**SfvbItemResponse**](SfvbItemResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_item_multimedia**
> SfvbItemResponse put_sfvb_item_multimedia(storefront_oid, item_multimedia_request)

Attach an image to an item

One slot at a time - the default image or one code - and every other image on the item is left alone.  That is the difference from the item API, where images are reachable only through a full item update whose multimedia array is reconciled destructively, so adding one means resending the rest or losing them.  Upload the file with files/upload first and name its storefront path here; unlike a page image it does not have to live in any particular folder, because the bytes are copied into the item's own storage on attach. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **item_multimedia_request** | [**SfvbItemMultimediaRequest**](SfvbItemMultimediaRequest.md)| Image to attach |
 **merchant_item_id** | **str**|  | [optional]
 **merchant_item_oid** | **int**|  | [optional]

### Return type

[**SfvbItemResponse**](SfvbItemResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_item_multimedia_description**
> SfvbItemResponse put_sfvb_item_multimedia_description(storefront_oid, item_multimedia_description_request)

Change an item image's description

Changes the description (alt text) of one image already attached to the item, in place.  The image is not touched.  Name it by merchant_item_multimedia_oid, or by exactly one of code or default; gallery images often have no code.  An empty description clears it, so the render falls back again.  Send the description_sha256 you read as current_sha256 so a change made since is not overwritten.  A description written here takes the place of the machine description, and image recognition never overwrites it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **item_multimedia_description_request** | [**SfvbItemMultimediaDescriptionRequest**](SfvbItemMultimediaDescriptionRequest.md)| The image and its new description |
 **merchant_item_id** | **str**|  | [optional]
 **merchant_item_oid** | **int**|  | [optional]

### Return type

[**SfvbItemResponse**](SfvbItemResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_item_pricing**
> SfvbItemPricing put_sfvb_item_pricing(storefront_oid, if_match, item_pricing_request)

Change what an item charges

Partial - a field left out is untouched.  A sale needs sale_cost, sale_start and sale_end together, the end after the start; clear_sale removes it.  msrp must be more than 0 (0 only when the price is 0); clear_msrp removes it.  volume_discounts replaces the retail quantity breaks.  Shoppers pay the new price at once, so this needs sfvb_publish, If-Match with the pricing hash_sha256, and the approval of the person who signed in the CLI - an approved item.pricing request for this item and exactly this change.  A change that sets every field to what it already is returns the pricing unchanged and uses no approval. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **if_match** | **str**| hash_sha256 from the pricing read.  Required; 428 when absent, 412 when stale. |
 **item_pricing_request** | [**SfvbItemPricingRequest**](SfvbItemPricingRequest.md)| The change |
 **merchant_item_id** | **str**|  | [optional]
 **merchant_item_oid** | **int**|  | [optional]
 **approval_id** | **str**| The approval_id of an approved item.pricing request for this item and change.  Required.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbItemPricing**](SfvbItemPricing.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_item_related**
> SfvbItemRelated put_sfvb_item_related(storefront_oid, if_match, item_related_request)

Replace an item's related items

Replaces the merchant's own related items, in order, and keeps the ones UltraCart calculates.  Each must be an item of this account and not the item itself, named once, up to 50.  No link back is added to the other items.  Needs sfvb_publish and If-Match with the related hash_sha256. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **if_match** | **str**| hash_sha256 from the related read.  Required; 428 when absent, 412 when stale. |
 **item_related_request** | [**SfvbItemRelatedRequest**](SfvbItemRelatedRequest.md)| The related items |
 **merchant_item_id** | **str**|  | [optional]
 **merchant_item_oid** | **int**|  | [optional]

### Return type

[**SfvbItemRelated**](SfvbItemRelated.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_item_seo**
> SfvbItemResponse put_sfvb_item_seo(storefront_oid, item_seo_request)

Change an item's search metadata

Partial - a field left out is untouched, a field sent empty is cleared and the page falls back to what it fell back to before.  Underneath these are three item attributes with reserved names, so this and the attributes endpoint reach the same storage; it exists separately because the names are not discoverable from the templates.  Two things worth knowing.  A title set here changes the document title only - og:title and twitter:title render the item's description either way.  And there is no canonical or noindex field, because both are site wide switches rather than per item values. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **item_seo_request** | [**SfvbItemSeoRequest**](SfvbItemSeoRequest.md)| Search metadata to change |
 **merchant_item_id** | **str**|  | [optional]
 **merchant_item_oid** | **int**|  | [optional]

### Return type

[**SfvbItemResponse**](SfvbItemResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_menu**
> SfvbMenu put_sfvb_menu(storefront_oid, code, menu_write_request)

Replace a store menu's entries

A whole menu replace, not a merge - what you send is what the menu holds afterwards, so read it, change the tree and send it back.  Omitting items changes only the title; sending an empty array empties the menu.  Writing a code that does not exist creates it.  Every entry is checked before any of it is written, including that a merchant_item_id and a page_path actually resolve, so a tree with one bad entry changes nothing.  Always needs sfvb_publish, because a menu is shared by every theme and there is no dormant copy to change instead. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **code** | **str**| Menu code, matched without regard to case |
 **menu_write_request** | [**SfvbMenuWriteRequest**](SfvbMenuWriteRequest.md)| The menu&#39;s replacement contents |
 **if_match** | **str**| Content hash from the last read.  Required when the menu already exists; 428 when absent, 412 when stale. | [optional]

### Return type

[**SfvbMenu**](SfvbMenu.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_page_attributes**
> SfvbPageResponse put_sfvb_page_attributes(storefront_oid, path, page_attribute_update_request)

Change a page's attributes

A partial update.  Only the attributes you name are changed.  Every entry is checked before any is written.  List, slider, item set, page collection and video list attributes are refused - edit those in the page editor.  Always needs sfvb_publish, because a page's attributes are shared by every theme and there is no dormant copy to change instead. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /catalog/dispensers/ |
 **page_attribute_update_request** | [**SfvbPageAttributeUpdateRequest**](SfvbPageAttributeUpdateRequest.md)| Attributes to change |

### Return type

[**SfvbPageResponse**](SfvbPageResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_page_multimedia**
> SfvbPageResponse put_sfvb_page_multimedia(storefront_oid, path, page_multimedia_request)

Attach an image to a page

Upload the image with files/upload to the page path followed by a filename first, then name that filename here as either the default image or an image code.  The default image is what a pageimage element with no pageImageCode renders, and what a subgroup tile shows.  Replaces whatever that slot held.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /catalog/dispensers/ |
 **page_multimedia_request** | [**SfvbPageMultimediaRequest**](SfvbPageMultimediaRequest.md)| Image to attach |

### Return type

[**SfvbPageResponse**](SfvbPageResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_page_selectors**
> SfvbPageSelectors put_sfvb_page_selectors(storefront_oid, path, page_selectors_request)

Replace a page's selectors

Each list you send replaces that whole set, and an empty list clears it.  A list you leave out is not touched.  The page's items or blog posts are recalculated from the new selectors straight away.  While a page has item selectors its items cannot be assigned by hand.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /lp/spring-sale/ |
 **page_selectors_request** | [**SfvbPageSelectors**](SfvbPageSelectors.md)| The selector sets to replace |

### Return type

[**SfvbPageSelectors**](SfvbPageSelectors.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_page_settings**
> SfvbPageResponse put_sfvb_page_settings(storefront_oid, path, page_settings_request)

Change a page's settings

A partial update.  Only the fields you send change - title, description, templates, visibility, sitemap exclusion, sort orders, items per page and page type.  Unlike the store admin's page save, the page's attributes, images, items, selectors and permissions are left exactly as they are.  Fields that would move or rename the page, and fields this endpoint does not know, are refused.  The root page cannot be hidden.  Always needs sfvb_publish, because page settings are live. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /lp/spring-sale/ |
 **page_settings_request** | [**SfvbPageSettingsRequest**](SfvbPageSettingsRequest.md)| The settings to change |

### Return type

[**SfvbPageResponse**](SfvbPageResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_preview_session**
> SfvbPreviewSessionResponse put_sfvb_preview_session(storefront_oid, preview_session_id, preview_session)

Push containers into a preview session

Stores compiled containers against a session created by createSfvbPreviewSession.  Replaces whatever the session held.  The session must exist - this does not create one, so a deleted, expired or never issued id is a 404 rather than a new session.  Nothing durable is written.  Requires a token that resolves to a user, so use the device authorization flow. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **preview_session_id** | **str**|  |
 **preview_session** | [**SfvbPreviewSessionRequest**](SfvbPreviewSessionRequest.md)| Containers to stage in the preview session |
 **theme_oid** | **int**|  | [optional]

### Return type

[**SfvbPreviewSessionResponse**](SfvbPreviewSessionResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_recording_settings**
> SfvbRecordingSettingsResponse put_sfvb_recording_settings(storefront_oid, recording_settings_request)

Turn the storefront's screen recording on or off

Turning it on records real shoppers' sessions from that moment, with no history before it.  The first time starts a 14 day free trial, after which recorded sessions are billed per 1,000.  Only change it when the merchant has asked for it.  Asking for the state it is already in changes nothing, and changed comes back false.  Always needs sfvb_publish, in both directions, because it decides whether live shoppers are recorded.  Limited per storefront to 5 changes a minute, 20 an hour and 50 a day. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **recording_settings_request** | [**SfvbRecordingSettingsRequest**](SfvbRecordingSettingsRequest.md)| Whether to record |

### Return type

[**SfvbRecordingSettingsResponse**](SfvbRecordingSettingsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_site_attributes**
> SfvbSiteAttributesResponse put_sfvb_site_attributes(storefront_oid, site_attribute_update_request)

Change a storefront's site attributes

A partial update.  Only the attributes you name are changed.  Every entry is checked before any is written.  List, video list, mailing list and item set attributes are refused, and so are the General screen settings other than the title, the SEO description and keywords and the social account names.  Credentials are refused.  Always needs sfvb_publish, because every theme reads the same attributes and there is no dormant copy to change instead.  The admin General screen saves the whole storefront, so a merchant with it open can still overwrite a change made here. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **site_attribute_update_request** | [**SfvbSiteAttributeUpdateRequest**](SfvbSiteAttributeUpdateRequest.md)| Attributes to change |

### Return type

[**SfvbSiteAttributesResponse**](SfvbSiteAttributesResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sfvb_theme_attributes**
> SfvbThemeAttributesResponse put_sfvb_theme_attributes(storefront_oid, theme_oid, attribute_update_request)

Change a theme's colors, fonts and settings

A partial update.  Only the slots you name are changed and every other slot on the theme keeps its value, so there is no need to send the whole set back to change one color.  Send a whole palette in one call rather than one call per color - they are applied together, so the storefront never renders half of a change.  Needs sfvb_publish when the theme is the one serving live traffic, because a color is referenced by name from every template that uses it and one write repaints the whole storefront at once.  On a dormant theme sfvb_write is enough, which is what makes duplicate-then-restyle work. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **theme_oid** | **int**|  |
 **attribute_update_request** | [**SfvbThemeAttributeUpdateRequest**](SfvbThemeAttributeUpdateRequest.md)| Slots to change |

### Return type

[**SfvbThemeAttributesResponse**](SfvbThemeAttributesResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_sfvb_comms_sending_domain_status**
> SfvbCommsSendingDomain refresh_sfvb_comms_sending_domain_status(domain)

Check a sending domain's verification

Asks Amazon SES again whether an amazon domain's DNS records are in place, and restarts a verification that failed (its records then change).  A mailgun domain comes back as it is; Mailgun checks its own records. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  |

### Return type

[**SfvbCommsSendingDomain**](SfvbCommsSendingDomain.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |
**502** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_sfvb_page**
> SfvbPageRefreshResponse refresh_sfvb_page(storefront_oid, page_refresh_request)

Drop one page's cached copy

The next request renders the page fresh.  Use it when a write succeeded, a read shows the new value, and the public page still shows the old one.  Writes normally refresh the pages they affect, so a stale page after a write is a bug worth reporting with its URL.  One page per request.  The response says whether the page had a cached copy and whether anything was dropped. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **page_refresh_request** | [**SfvbPageRefreshRequest**](SfvbPageRefreshRequest.md)| The page to refresh |

### Return type

[**SfvbPageRefreshResponse**](SfvbPageRefreshResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_sfvb_page_blog_posts**
> SfvbPageBlogPostsResponse remove_sfvb_page_blog_posts(storefront_oid, path, page_blog_posts_request)

Take blog posts off a page

Removes posts by blog_post_oid, at most 500 at a time.  Every oid must be on the page, and one that is not changes nothing.  The posts themselves are not touched.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /blog/ |
 **page_blog_posts_request** | [**SfvbPageBlogPostsRequest**](SfvbPageBlogPostsRequest.md)| Blog posts to take off the page |

### Return type

[**SfvbPageBlogPostsResponse**](SfvbPageBlogPostsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_sfvb_page_items**
> SfvbPageItemsResponse remove_sfvb_page_items(storefront_oid, path, page_items_remove_request)

Take items off a page

Removes items by item id, at most 500 at a time.  Every id must be on the page, and one that is not changes nothing.  The items themselves are not touched.  Refused on a page whose selectors choose its items.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**| Page path, for example /lp/spring-sale/ |
 **page_items_remove_request** | [**SfvbPageItemsRemoveRequest**](SfvbPageItemsRemoveRequest.md)| Items to take off the page |

### Return type

[**SfvbPageItemsResponse**](SfvbPageItemsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_sfvb_email**
> SfvbEmailRenderResponse render_sfvb_email(storefront_oid, email_uuid, email_render_request)

Render a flow or campaign email without sending it

Renders a flow or campaign email exactly as its send would, and returns the subject, preview text, HTML and text.  Nothing is sent, saved or created.  A unique coupon code, click id and magic link token are placeholders.  A missing footer token, which a send skips the email for, is a warning.  Give cjson to render an unsaved draft of the email container in place of the saved one.  An order must be a test order.  cart_item_ids fills the cart a cart flow email shows. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **email_uuid** | **str**|  |
 **email_render_request** | [**SfvbEmailRenderRequest**](SfvbEmailRenderRequest.md)| What to render the email with |

### Return type

[**SfvbEmailRenderResponse**](SfvbEmailRenderResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_sfvb_transactional_email**
> SfvbEmailRenderResponse render_sfvb_transactional_email(storefront_oid, file_name, email_render_request)

Render a transactional email without sending it

Renders a transactional email, such as the order receipt, exactly as it is sent, and returns the subject, HTML and text.  Nothing is sent or saved.  file_name is the template file, such as receipt_html.vm, or the display name.  Give cjson to render an unsaved draft of the email's body container in place of the saved one.  The order must be a test order.  Without one the email renders with a made up order. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **file_name** | **str**|  |
 **email_render_request** | [**SfvbEmailRenderRequest**](SfvbEmailRenderRequest.md)| What to render the email with |

### Return type

[**SfvbEmailRenderResponse**](SfvbEmailRenderResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_sfvb_widgets**
> SfvbRenderResponse render_sfvb_widgets(storefront_oid, theme_oid, render_request)

Render a CJSON node to HTML

Renders one node in the context of a theme and a page.  Unlike compile this is stateful.  Rendering resolves merchant data, so an element bound to an item renders wrongly, and silently, without a context item id.  One node per call, so a node that fails to render fails on its own rather than taking a batch with it, and a failure says why.  By default the node renders as a shopper sees it, with conditions, prices and sale state evaluated against the context item.  Set edit_mode to render every branch the way the builder shows it, for styling content a shopper only sometimes sees. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **theme_oid** | **int**|  |
 **render_request** | [**SfvbRenderRequest**](SfvbRenderRequest.md)| Widgets to render |

### Return type

[**SfvbRenderResponse**](SfvbRenderResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reserve_sfvb_widget_ids**
> SfvbWidgetIdsResponse reserve_sfvb_widget_ids(storefront_oid)

Reserve a block of widget ids

Widget ids are allocated by the server, not invented by the caller.  Reserve a block, then form ids as elementType-number.  This is the single most likely thing to get wrong on a first write.  A POST rather than a GET because it consumes a sequence.  A GET that mutates will eventually be prefetched, retried or cached by something that assumed it was safe. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **count** | **int**|  | [optional]

### Return type

[**SfvbWidgetIdsResponse**](SfvbWidgetIdsResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_sfvb_i18n_message**
> SfvbI18nResetResponse reset_sfvb_i18n_message(storefront_oid, key, if_match)

Reset one built-in message

Puts a message back to the template's text.  The merchant's English edit and hand translations stop serving at once and every language falls back to machine translation; the message comes back the next time a page renders it.  A message imported from an older theme's locale file is refused.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **key** | **str**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **theme_oid** | **int**|  | [optional]

### Return type

[**SfvbI18nResetResponse**](SfvbI18nResetResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_sfvb_redirect**
> SfvbRedirectResolveResponse resolve_sfvb_redirect(storefront_oid)

What a shopper gets for a path

Follows the redirect rules for a path exactly as the storefront does and reports each step, the final path, its status and what it lands on (a live page, a hidden page, an item, a 404 or something else).  Read only.  Use it to check every change. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **path** | **str**|  | [optional]

### Return type

[**SfvbRedirectResolveResponse**](SfvbRedirectResolveResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_sfvb_redirect_batch**
> SfvbRedirectResolveBatchResponse resolve_sfvb_redirect_batch(storefront_oid, redirect_resolve_batch_request)

What a shopper gets for each of many paths

Up to 1,000 paths in one call, each followed through the redirect rules exactly as the single resolve does, with counts of how many redirect and how many end on a 404.  For checking every old URL of a migrated store.  Read only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **redirect_resolve_batch_request** | [**SfvbRedirectResolveBatchRequest**](SfvbRedirectResolveBatchRequest.md)| The paths |

### Return type

[**SfvbRedirectResolveBatchResponse**](SfvbRedirectResolveBatchResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_sfvb_template**
> SfvbTemplateResolveResponse resolve_sfvb_template(storefront_oid, name)

Resolve a template name to the file a page renders

A page stores only its template's file name.  This runs the storefront's own template search for that name and returns the file a page naming it renders, relative to the theme.  It also lists the theme's resource paths in search order with every file of that name below each, so a theme copy overriding a shared core copy, or a copy in a snippets folder that is never used, is visible.  exists is false when a page naming the template cannot render. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **name** | **str**| The template file name, such as catalog.vm |
 **theme_oid** | **int**| Resolve in this theme instead of the active theme | [optional]

### Return type

[**SfvbTemplateResolveResponse**](SfvbTemplateResolveResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_sfvb_container**
> SfvbContainerResponse revert_sfvb_container(storefront_oid, owner_type, owner_object_id, if_match, container_revert_request)

Revert a container stored outside the file system

The restore is itself snapshotted, so a revert can be undone in turn.  Reverting to an entry recorded before the container existed removes it again.  Addressed through the owning container and guarded by If-Match, because a revert overwrites live content just as much as an ordinary write does.  owner_type also says how owner_object_id is read, so a version written by oid can be reverted by merchant item id and the other way round. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **owner_type** | **str**|  |
 **owner_object_id** | **str**|  |
 **if_match** | **str**| CJSON hash of the container being reverted.  Required; 428 when absent, 412 when stale. |
 **container_revert_request** | [**SfvbContainerRevertRequest**](SfvbContainerRevertRequest.md)| Version to revert the container to |
 **container_name** | **str**|  | [optional]

### Return type

[**SfvbContainerResponse**](SfvbContainerResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_sfvb_file**
> SfvbFileWriteResponse revert_sfvb_file(storefront_oid, if_match, file_revert_request)

Revert a storefront file to an earlier version

The revert lands as a new version, so it is itself undoable. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **if_match** | **str**| Content hash of the file being reverted.  Required; 428 when absent, 412 when stale. |
 **file_revert_request** | [**SfvbFileRevertRequest**](SfvbFileRevertRequest.md)| Version to revert the file to |
 **approval_id** | **str**| For a .js or .mjs file, the approval_id of an approved file.put_script request naming this version.  Required for scripts.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbFileWriteResponse**](SfvbFileWriteResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review_sfvb_email**
> SfvbEmail review_sfvb_email(storefront_oid, email_uuid, email_review_request)

Request a content review of a flow or campaign email

Starts a review the way the admin's Request Review does.  The review runs in the background and no test copy is sent.  The email is marked pending_review at once, and the signed-in user gets the approved or rejected notice, so read the email again for the ruling.  Refused with sfvb.review_not_needed when it doesn't need review, is already waiting for one, or was rejected and not changed since.  An email in a flow triggered by an order or an auto order needs order_id, a test order.  Needs a signed-in user, not an API key alone. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **email_uuid** | **str**|  |
 **email_review_request** | [**SfvbEmailReviewRequest**](SfvbEmailReviewRequest.md)| The test order, for an email in an order-triggered flow |

### Return type

[**SfvbEmail**](SfvbEmail.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_sfvb_secret_request**
> SfvbSecretRequest revoke_sfvb_secret_request(request_id)

Revoke a fulfilled request's unused handles

Every handle of the request that no write has used up stops working at once, and its value is deleted.  A handle a write is using right now is left to that write.  Use it when the plan changed, or a handle may have leaked. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  |

### Return type

[**SfvbSecretRequest**](SfvbSecretRequest.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_sfvb_files**
> SfvbFileSearchResponse search_sfvb_files(storefront_oid, search_request)

Search storefront files

Searches names and, when text is supplied, file contents.  For a CLI with no local copy this is the only way to answer where something is defined without walking the whole tree.  Results are capped and truncation is always reported. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **search_request** | [**SfvbFileSearchRequest**](SfvbFileSearchRequest.md)| File search |

### Return type

[**SfvbFileSearchResponse**](SfvbFileSearchResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_sfvb_library**
> SfvbLibraryResponse search_sfvb_library(storefront_oid)

Search the element library

Known-good CJSON fragments a human already built out of real elements.  This is what a lint warning about a monolithic html element should point at - a warning that names a fragment solving the same problem is an instruction, where a warning on its own is only criticism.  Results are terse; fetch a single entry for its CJSON.  Narrow with a query parameter named after a facet, such as facet_purpose, whose value is the facet name, a colon and one of its options.  Besides element type and author, the facets include purpose, section, industry and style from library/taxonomy, and the search text matches those tags too.  Results follow the same rules as reading one entry, so others see published revisions only. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **segment** | **str**|  | [optional]
 **search** | **str**|  | [optional]
 **page_number** | **int**|  | [optional]
 **results_per_page** | **int**|  | [optional]

### Return type

[**SfvbLibraryResponse**](SfvbLibraryResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_sfvb_library_screenshot**
> SfvbLibraryEntry set_sfvb_library_screenshot(storefront_oid, library_oid, if_match, screenshot_request)

Set a library entry's screenshot

Three calls, like the other uploads.  Request an upload URL with files/upload_url/png, PUT the PNG bytes to it, then call this with the key, the sha256 of those bytes and where the image came from.  Owner only, with the draft's hash_sha256 as If-Match.  The PNG must be at most 5 MB and 4096 pixels a side; it is re-encoded, which drops any metadata, and a thumbnail is made from it before this returns.  Capture it with test data only.  A refused image leaves the previous screenshot in place.  Other merchants see a new screenshot only after the next publish, whose review checks it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **screenshot_request** | [**SfvbLibraryScreenshotRequest**](SfvbLibraryScreenshotRequest.md)| The staged PNG |

### Return type

[**SfvbLibraryEntry**](SfvbLibraryEntry.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**413** |  |  -  |
**428** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_sfvb_library_entry**
> SfvbLibraryEntry share_sfvb_library_entry(storefront_oid, library_oid, share_request)

Share a published library entry with a linked account

Owner only, and always needs sfvb_publish.  The merchant must be one share_targets lists, and the entry must have a published revision, which is what the recipient sees.  The published revision is checked again for absolute asset URLs and credentials.  Idempotent. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |
 **share_request** | [**SfvbLibraryShareRequest**](SfvbLibraryShareRequest.md)| The linked account |

### Return type

[**SfvbLibraryEntry**](SfvbLibraryEntry.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_sfvb_experiment**
> SfvbExperiment start_sfvb_experiment(storefront_oid, experiment_start_request)

Start an experiment

type page starts an experiment element already saved in a page body - send path, slot and widget_id, and its name, objective, duration and variations are read from the element with the builder's rules (2 to 5 variations numbered 0 up with no gaps, 3 to 90 days, traffic on all or none adding up to 100).  The new id is written into the element and the body is saved, so pull it again before the next edit.  type url splits visitors between existing pages at router_url, and always ends by itself after duration_days.  Always needs sfvb_publish, because visitors are split as soon as it starts, and the approval of the person who signed in the CLI - an approved experiment.start request for exactly this start (see POST /sfvb/approvals). 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **experiment_start_request** | [**SfvbExperimentStartRequest**](SfvbExperimentStartRequest.md)| The experiment to start |
 **approval_id** | **str**| The approval_id of an approved experiment.start request for exactly this start.  Required.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbExperiment**](SfvbExperiment.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** |  |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_sfvb_comms_email**
> SfvbCommsTestSendResponse test_sfvb_comms_email(storefront_oid, commseq_uuid, step_uuid, test_email_request)

Send one test of an email step's email to a user on this account

to_email must be the email address of a user on this account; a test is never sent to customers or anyone else.  It reaches a real inbox and counts against the plan's email quota.  Needs sfvb_publish and the sign-in of a person.  Rate limited per merchant to 10 an hour and 50 a day.  The email render shows the same email without sending it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **commseq_uuid** | **str**|  |
 **step_uuid** | **str**|  |
 **test_email_request** | [**SfvbCommsTestEmailRequest**](SfvbCommsTestEmailRequest.md)| The email and the recipient |

### Return type

[**SfvbCommsTestSendResponse**](SfvbCommsTestSendResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_sfvb_comms_postcard**
> SfvbCommsTestSendResponse test_sfvb_comms_postcard(storefront_oid, commseq_uuid, step_uuid, test_postcard_request)

Print and mail one real test postcard

It is printed and mailed at the account's cost and can't be recalled.  mail_card must be true; the postcard proof shows the card without mailing it.  Postcards must be turned on for the account by UltraCart.  Needs sfvb_publish, the sign-in of a person, and an approved postcard.test_mail request for exactly this card and address, with a fresh code every time.  dry_run checks everything and shows the cost.  Rate limited per merchant to 3 an hour and 10 a day.  The answer says whether a card was mailed. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **commseq_uuid** | **str**|  |
 **step_uuid** | **str**|  |
 **test_postcard_request** | [**SfvbCommsTestPostcardRequest**](SfvbCommsTestPostcardRequest.md)| The address and mail_card |
 **approval_id** | **str**| The approval_id of an approved postcard.test_mail request for exactly this card and address.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbCommsTestSendResponse**](SfvbCommsTestSendResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_sfvb_comms_sms**
> SfvbCommsTestSendResponse test_sfvb_comms_sms(storefront_oid, commseq_uuid, step_uuid, test_sms_request)

Send one test of an SMS step to a user on this account

to_phone must be the cell phone of a user on this account, in E.164 form.  It is billed per segment through the account's Twilio account, from the flow's or campaign's SMS number; with none it is refused.  Needs sfvb_publish and the sign-in of a person.  Rate limited per merchant to 5 an hour and 20 a day. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **commseq_uuid** | **str**|  |
 **step_uuid** | **str**|  |
 **test_sms_request** | [**SfvbCommsTestSmsRequest**](SfvbCommsTestSmsRequest.md)| The recipient |

### Return type

[**SfvbCommsTestSendResponse**](SfvbCommsTestSendResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_sfvb_upsell_path**
> SfvbUpsellPath unarchive_sfvb_upsell_path(storefront_oid, upsell_path_oid)

Unarchive an upsell path

Brings the path back into the default list.  A path that is switched on is refused, because unarchiving it would start it without approval - disable it, unarchive it, then enable it. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_path_oid** | **int**|  |

### Return type

[**SfvbUpsellPath**](SfvbUpsellPath.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfavorite_sfvb_library_entry**
> unfavorite_sfvb_library_entry(storefront_oid, library_oid)

Remove a library entry from favorites

Removes the calling user's bookmark.  Idempotent. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |

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
**204** | No Content |  -  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unignore_sfvb_not_found_entry**
> SfvbNotFoundEntry unignore_sfvb_not_found_entry(storefront_oid, not_found_id)

Stop ignoring a 404 path

The path lists and counts hits again. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **not_found_id** | **str**|  |

### Return type

[**SfvbNotFoundEntry**](SfvbNotFoundEntry.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpublish_sfvb_library_entry**
> SfvbLibraryEntry unpublish_sfvb_library_entry(storefront_oid, library_oid, unpublish_request)

Narrow who can see a library entry

Sets visibility to shared or private.  Owner only, and always needs sfvb_publish.  Published revisions are kept and storefronts that already installed the entry keep their copies. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |
 **unpublish_request** | [**SfvbLibraryPublishRequest**](SfvbLibraryPublishRequest.md)| The narrower visibility |

### Return type

[**SfvbLibraryEntry**](SfvbLibraryEntry.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unshare_sfvb_library_entry**
> SfvbLibraryUnshareResult unshare_sfvb_library_entry(storefront_oid, library_oid, merchant_id)

Stop sharing a library entry with an account

Owner only, and always needs sfvb_publish.  Stops further installs by that account.  Its existing installs keep their copies and are listed in the result.  Idempotent, and still works while the library is turned off. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |
 **merchant_id** | **str**|  |

### Return type

[**SfvbLibraryUnshareResult**](SfvbLibraryUnshareResult.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_affiliate_network**
> SfvbAffiliateNetwork update_sfvb_affiliate_network(storefront_oid, affiliate_network_oid, if_match, affiliate_network_request)

Change an affiliate network

A partial update: only the fields sent change.  Send the network's hash_sha256 as If-Match.  Needs sfvb_publish.  Changing the conversion_pixel, or the conversion_type, of a network whose pixel will be used needs an approved affiliate_network.change request for exactly this change (Approval-Id), which UltraCart reviews first.  Other fields, and emptying the pixel, need none.  dry_run says whether it needs one, without saving. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **affiliate_network_oid** | **int**|  |
 **if_match** | **str**| The network&#39;s hash_sha256 from the last read.  428 when absent, 412 when stale. |
 **affiliate_network_request** | [**SfvbAffiliateNetworkRequest**](SfvbAffiliateNetworkRequest.md)| The change |
 **approval_id** | **str**| When the change sets a conversion pixel the network will use, the approval_id of an approved affiliate_network.change request for exactly this change.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbAffiliateNetwork**](SfvbAffiliateNetwork.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**413** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_blog_post**
> SfvbBlogPostDetail update_sfvb_blog_post(storefront_oid, blog_post_oid, blog_post_request)

Change a blog post

Only the fields sent change; tags, when sent, replaces every tag.  The post's images and attributes are left alone.  Publish or unpublish with visibility.  A post that is not a draft before or after the change needs sfvb_publish.  The same content rules as create apply. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **blog_post_oid** | **int**|  |
 **blog_post_request** | [**SfvbBlogPostRequest**](SfvbBlogPostRequest.md)| The fields to change |

### Return type

[**SfvbBlogPostDetail**](SfvbBlogPostDetail.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_campaign**
> SfvbCampaign update_sfvb_campaign(storefront_oid, campaign_uuid, if_match, campaign_write_request)

Change a campaign

A field left out keeps its value; memberships replaces the whole set.  The status is never changed here.  Send the hash_sha256 you read as If-Match.  A scheduled, sending or sent campaign needs sfvb_publish, and a change to a scheduled one applies to the send that is coming.  notes lists any emails a sending domain change put back to needing review. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **campaign_uuid** | **str**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **campaign_write_request** | [**SfvbCampaignWriteRequest**](SfvbCampaignWriteRequest.md)| The fields to change |

### Return type

[**SfvbCampaign**](SfvbCampaign.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_comms_folder**
> SfvbCommsFolderResponse update_sfvb_comms_folder(storefront_oid, folder_uuid, if_match, folder_write_request)

Rename a list and segment folder

Send the folder's hash_sha256 as If-Match.  A folder the admin made itself (system_generated) can't be renamed here. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **folder_uuid** | **str**|  |
 **if_match** | **str**| The folder&#39;s hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **folder_write_request** | [**SfvbCommsFolderWriteRequest**](SfvbCommsFolderWriteRequest.md)| The new name |

### Return type

[**SfvbCommsFolderResponse**](SfvbCommsFolderResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_comms_list**
> SfvbCommsListResponse update_sfvb_comms_list(storefront_oid, list_uuid, if_match, list_write_request)

Change an email list's name, folder or public settings

A field left out stays as it is; an empty folder_uuid or public_description clears it.  Send the list's hash_sha256 as If-Match; the change applies only while the name, folder and public settings are still what was read.  The members and member count are never changed here. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **list_uuid** | **str**|  |
 **if_match** | **str**| The list&#39;s hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **list_write_request** | [**SfvbCommsListWriteRequest**](SfvbCommsListWriteRequest.md)| The fields to change |

### Return type

[**SfvbCommsListResponse**](SfvbCommsListResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_comms_segment**
> SfvbCommsSegmentResponse update_sfvb_comms_segment(storefront_oid, segment_uuid, if_match, segment_write_request)

Change a segment's name, rule or folder

A field left out stays as it is.  Send the segment's hash_sha256 as If-Match; the change applies only while the name, rule and folder are still what was read.  A changed rule is checked as on a create and starts a rebuild.  Changing the rule of a segment a live campaign or flow uses needs sfvb_publish and an approved segment.update approval (Approval-Id); a name or folder change, or a segment nothing live uses, needs neither. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **segment_uuid** | **str**|  |
 **if_match** | **str**| The segment&#39;s hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **segment_write_request** | [**SfvbCommsSegmentWriteRequest**](SfvbCommsSegmentWriteRequest.md)| The fields to change |
 **approval_id** | **str**| When the rule changes and a live campaign or flow uses the segment, the approval_id of an approved segment.update request for this change.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbCommsSegmentResponse**](SfvbCommsSegmentResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_comms_sending_domain**
> SfvbCommsSendingDomain update_sfvb_comms_sending_domain(domain, sending_domain)

Update a sending domain

Only a mailgun domain's mailgun_api_key can change.  Send it as a secret handle made for the domain to replace it, or as the mask it was read with to keep it.  A new key sets up UltraCart's webhooks again with it; if Mailgun refuses, nothing is saved and the handle is given back unused. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  |
 **sending_domain** | [**SfvbCommsSendingDomain**](SfvbCommsSendingDomain.md)| The changes |

### Return type

[**SfvbCommsSendingDomain**](SfvbCommsSendingDomain.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |
**502** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_comms_settings**
> SfvbCommsSettingsResponse update_sfvb_comms_settings(storefront_oid, if_match, comms_settings_update_request)

Change a storefront's communications settings

A field left out stays as it is.  A return address change needs sfvb_write and If-Match.  A change to the default marketing or transactional sender, or the default SMS number, also needs sfvb_publish and an approved comms_settings.update request for exactly this change.  A sending domain must be on this account and the SMS number on one of its Twilio accounts.  dry_run checks and shows the change without writing or using an approval. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **if_match** | **str**| The settings&#39; hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **comms_settings_update_request** | [**SfvbCommsSettingsUpdateRequest**](SfvbCommsSettingsUpdateRequest.md)| The settings to change |
 **approval_id** | **str**| The approval_id of an approved comms_settings.update request for exactly this change, when a sender or the SMS number changes.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbCommsSettingsResponse**](SfvbCommsSettingsResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_comms_twilio_account**
> SfvbCommsTwilioAccountResponse update_sfvb_comms_twilio_account(twilio_account)

Update the Twilio account

Changes the account's Twilio account.  Leave a field out to keep it.  Send auth_token as the mask it was read with to keep it, or as a secret handle made for the account SID to replace it.  A new account_sid needs a new auth_token with it.  A new token is checked with Twilio and UltraCart's API key, TwiML apps and voice encryption key are made again; if Twilio refuses, nothing is saved and the handle is given back unused.  phone_numbers, when sent, replaces the list. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **twilio_account** | [**SfvbCommsTwilioAccount**](SfvbCommsTwilioAccount.md)| The changes |

### Return type

[**SfvbCommsTwilioAccountResponse**](SfvbCommsTwilioAccountResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |
**502** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_email**
> SfvbEmail update_sfvb_email(storefront_oid, email_uuid, if_match, email_update_request)

Change a flow or campaign email's subject or preview text

A field left out keeps its value.  Each is 5 to 150 characters on one line.  Send the hash_sha256 you read as If-Match.  An email in a sending flow or campaign needs sfvb_publish, as a body push does.  The merchant's content review rule applies, so an email waiting for review or rejected goes back to needing review.  An email suspended for spam is refused with sfvb.email_suspended. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **email_uuid** | **str**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **email_update_request** | [**SfvbEmailUpdateRequest**](SfvbEmailUpdateRequest.md)| The subject or preview text to change |

### Return type

[**SfvbEmail**](SfvbEmail.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_flow**
> SfvbFlow update_sfvb_flow(storefront_oid, flow_uuid, if_match, flow_write_request)

Change a flow

A field left out keeps its value.  The trigger changes only while the flow is off (sfvb.flow_trigger_live otherwise), and customers already in the flow continue.  The status is never changed here.  Send the hash_sha256 you read as If-Match.  A flow that is enrolling customers needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **flow_uuid** | **str**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **flow_write_request** | [**SfvbFlowWriteRequest**](SfvbFlowWriteRequest.md)| The fields to change |

### Return type

[**SfvbFlow**](SfvbFlow.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_flow_status**
> SfvbFlow update_sfvb_flow_status(storefront_oid, flow_uuid, if_match, flow_status_request)

Turn a flow on or off

active enrolls customers as they trigger the flow from now on, and they receive its emails.  inactive stops new enrollments.  Always needs sfvb_publish.  Send the hash_sha256 you read as If-Match. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **flow_uuid** | **str**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **flow_status_request** | [**SfvbFlowStatusRequest**](SfvbFlowStatusRequest.md)| The status to set |

### Return type

[**SfvbFlow**](SfvbFlow.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_item_attribute_batch**
> SfvbItemAttributeBatchResponse update_sfvb_item_attribute_batch(storefront_oid, item_attribute_batch_request)

Change attributes across many items in one call

Applies exactly the change rows of a dry run, given its plan_hash, each with its merchant_item_oid and current_sha256.  Each item is saved once with all of its rows; a row whose value changed since the dry run is skipped as stale and never overwritten, and an item that cannot be saved does not stop the others.  Only the named attributes change.  Needs sfvb_publish and the approval of the person who signed in the CLI, an approved item.attribute_batch request for exactly these rows in the Approval-Id header. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **item_attribute_batch_request** | [**SfvbItemAttributeBatchRequest**](SfvbItemAttributeBatchRequest.md)| The dry run&#39;s change rows and plan_hash |
 **approval_id** | **str**| The approval_id of an approved item.attribute_batch request for exactly these rows.  Required.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbItemAttributeBatchResponse**](SfvbItemAttributeBatchResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**413** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_library_entry**
> SfvbLibraryEntry update_sfvb_library_entry(storefront_oid, library_oid, if_match, library_entry)

Update a library entry's draft

A full replace of the draft's fields.  Owner only.  Send the hash_sha256 you read as If-Match.  Every save increments revision_number; nothing other merchants see changes until the draft is published.  A changed fragment is re-scanned and its images copied again, and screenshot_stale tells you to retake the screenshot. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **library_oid** | **int**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **library_entry** | [**SfvbLibraryEntryRequest**](SfvbLibraryEntryRequest.md)| The whole entry |

### Return type

[**SfvbLibraryEntry**](SfvbLibraryEntry.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**413** |  |  -  |
**428** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_redirect**
> SfvbRedirectResponse update_sfvb_redirect(storefront_oid, redirect_id, if_match, redirect_request)

Change a redirect rule

Changes the source, target or note, and can turn an admin rule into a 301.  Fields left out keep their value.  A changed source or target is checked like a new rule.  Send the hash_sha256 you read as If-Match.  Always needs sfvb_publish. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **redirect_id** | **int**|  |
 **if_match** | **str**| hash_sha256 from the last read.  428 when absent, 412 when stale. |
 **redirect_request** | [**SfvbRedirectRequest**](SfvbRedirectRequest.md)| The request |

### Return type

[**SfvbRedirectResponse**](SfvbRedirectResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_sequence_step**
> SfvbSequenceStepUpdateResponse update_sfvb_sequence_step(storefront_oid, sequence_uuid, step_uuid, if_match, sequence_step_update_request)

Change one step's settings or audience filter

Replaces the step's settings (config_json), its audience filter (filter_profile_equation_json), or both.  Nothing else about the step or the sequence changes.  Send the step's hash_sha256 as If-Match; the write only lands if the step is still what you read.  Email, experiment, resend, webhook, begin, end, continue and merge steps are refused.  On a post_card step only disabled, name and info change, and not its filter.  A sequence whose campaign or flow is live needs sfvb_publish.  Turning a post_card step on, live or not, needs an approved sequence_step.enable_postcard approval (Approval-Id): once on, it mails printed cards whenever the campaign or flow runs. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **sequence_uuid** | **str**|  |
 **step_uuid** | **str**|  |
 **if_match** | **str**| The step&#39;s hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **sequence_step_update_request** | [**SfvbSequenceStepUpdateRequest**](SfvbSequenceStepUpdateRequest.md)| The settings, the filter, or both |
 **approval_id** | **str**| When the change turns a post_card step on, the approval_id of an approved sequence_step.enable_postcard request for this step.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbSequenceStepUpdateResponse**](SfvbSequenceStepUpdateResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_site_seo**
> SfvbSiteSeo update_sfvb_site_seo(storefront_oid, if_match, site_seo_request)

Change a storefront's search engine settings

A partial update of Canonical Links, Schema.org and Prevent Indexing.  Send the hash_sha256 you read as If-Match.  dry_run reports each change, whether it needs approval and whether that approval needs a fresh code, without saving.  Turning Canonical Links or Schema.org on needs no approval.  Turning either off, or turning Prevent Indexing on or off, needs an approved site_seo.change request for exactly this change (Approval-Id), and turning Prevent Indexing on asks for an authenticator code even inside an approval session.  Always needs sfvb_publish, because the settings apply to every page as soon as they are saved.  The admin saves the whole storefront, so a merchant with the screen open can still overwrite a change made here. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **if_match** | **str**| The hash_sha256 from the last read.  428 when absent, 412 when stale. |
 **site_seo_request** | [**SfvbSiteSeoRequest**](SfvbSiteSeoRequest.md)| The switches to change |
 **approval_id** | **str**| When the change turns Canonical Links or Schema.org off, or turns Prevent Indexing on or off, the approval_id of an approved site_seo.change request for this change.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbSiteSeo**](SfvbSiteSeo.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_smart_attribution**
> SfvbSmartAttribution update_sfvb_smart_attribution(storefront_oid, if_match, smart_attribution_request)

Change a storefront's Smart Attribution configuration

A partial update of the mode, model, global split and lookback.  platforms, when sent, replaces the whole list.  The global split must total exactly 1 and the lookback is 7 to 365.  On an unconfigured storefront it creates the configuration.  Send the hash_sha256 you read as If-Match.  Needs sfvb_publish, and when the mode is active or the change makes it active, an approved smart_attribution.change request for exactly this change (Approval-Id), because active mode decides which conversions each platform is sent.  A change that stores what is already stored returns the configuration unchanged and uses no approval. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **if_match** | **str**| hash_sha256 from the Smart Attribution read.  428 when absent, 412 when stale. |
 **smart_attribution_request** | [**SfvbSmartAttributionRequest**](SfvbSmartAttributionRequest.md)| The change |
 **approval_id** | **str**| When the mode is or becomes active, the approval_id of an approved smart_attribution.change request for this change.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbSmartAttribution**](SfvbSmartAttribution.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_tracking_advanced**
> SfvbTrackingSettingsResponse update_sfvb_tracking_advanced(storefront_oid, if_match, tracking_advanced_request)

Change a storefront's advanced conversion settings

A partial update.  Fields left out keep their value, and a text setting is cleared by naming it in unset.  URLs are a path starting with / or an absolute http or https URL, and one over its limit is refused rather than cut short.  The currency must be one the read lists.  The order hash secret key cannot be changed here.  Every field is checked before any is written.  Send the advanced hash_sha256 you read as If-Match.  dry_run reports the changes without saving.  Always needs sfvb_publish, because the settings apply to shoppers as soon as they are saved.  The admin saves the whole tab, so a merchant with it open can still overwrite a change made here. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **if_match** | **str**| The advanced hash_sha256 from the last read.  428 when absent, 412 when stale. |
 **tracking_advanced_request** | [**SfvbTrackingAdvancedRequest**](SfvbTrackingAdvancedRequest.md)| The settings to change |

### Return type

[**SfvbTrackingSettingsResponse**](SfvbTrackingSettingsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_tracking_html**
> SfvbTrackingHtml update_sfvb_tracking_html(storefront_oid, slot, if_match, tracking_html_request)

Write one custom tracking HTML slot

Replaces the whole slot, at most 256 KB.  Content the storefront's templates may not use is refused with its lines.  Send the slot's hash_sha256 as If-Match.  Needs sfvb_publish.  Any HTML but an empty string needs an approved tracking_html.put request for exactly this content (Approval-Id), which UltraCart reviews first.  An empty string empties the slot without one.  dry_run says whether the write needs one, without saving. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **slot** | **str**| tracking or conversion |
 **if_match** | **str**| The slot&#39;s hash_sha256 from the last read.  428 when absent, 412 when stale. |
 **tracking_html_request** | [**SfvbTrackingHtmlRequest**](SfvbTrackingHtmlRequest.md)| The content |
 **approval_id** | **str**| For any content but an empty string, the approval_id of an approved tracking_html.put request for exactly this content.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbTrackingHtml**](SfvbTrackingHtml.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**413** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_tracking_privacy**
> SfvbTrackingSettingsResponse update_sfvb_tracking_privacy(storefront_oid, if_match, tracking_privacy_request)

Change a storefront's privacy rules

A partial update.  Each rule named is set to all, eea, non_us or off, and rules left out keep their value.  Every rule is checked before any is written.  Send the privacy hash_sha256 you read as If-Match.  dry_run reports the changes without saving.  Always needs sfvb_publish, because the rules apply to shoppers as soon as they are saved.  The admin saves the whole tab, so a merchant with it open can still overwrite a change made here. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **if_match** | **str**| The privacy hash_sha256 from the last read.  428 when absent, 412 when stale. |
 **tracking_privacy_request** | [**SfvbTrackingPrivacyRequest**](SfvbTrackingPrivacyRequest.md)| The rules to change |

### Return type

[**SfvbTrackingSettingsResponse**](SfvbTrackingSettingsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_tracking_provider**
> SfvbTrackingProvider update_sfvb_tracking_provider(storefront_oid, provider, if_match, tracking_provider_request)

Change one tracking provider

A partial update of the provider's fields, secrets (as secret handles), consent gate, events and, for google_analytics, wholesale account numbers.  Every value is checked for its field's type before anything is written.  Send the provider's hash_sha256 as If-Match.  dry_run reports the changes without saving.  Needs sfvb_publish.  Turning the provider on, loosening its consent gate, or turning on Google Tag Gateway (which also needs accept_cost true) needs an approved tracking_provider.change request for exactly this change (Approval-Id).  OAuth connections are made in the admin. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **provider** | **str**|  |
 **if_match** | **str**| The provider&#39;s hash_sha256 from the last read.  428 when absent, 412 when stale. |
 **tracking_provider_request** | [**SfvbTrackingProviderRequest**](SfvbTrackingProviderRequest.md)| The change |
 **approval_id** | **str**| When the change turns the provider on, loosens its consent gate or turns on Google Tag Gateway, the approval_id of an approved tracking_provider.change request for this change.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbTrackingProvider**](SfvbTrackingProvider.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |
**502** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_transactional_email**
> SfvbTransactionalEmailResponse update_sfvb_transactional_email(storefront_oid, file_name, if_match, transactional_email_update_request)

Change a transactional email's subject, delivery options or sender

A field left out stays as it is.  It goes to every matching order from the moment it is saved, so every change needs sfvb_publish, the email's hash_sha256 as If-Match, and an approved transactional_email.update request for exactly this change (params.path the template file).  dry_run checks and shows the change without writing or using an approval.  Delivery options are named by name.  A sender change reaches every storefront on the same screen branding theme, and is refused for one that sends through the merchant's own mail server. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **file_name** | **str**|  |
 **if_match** | **str**| The email&#39;s hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **transactional_email_update_request** | [**SfvbTransactionalEmailUpdateRequest**](SfvbTransactionalEmailUpdateRequest.md)| The fields to change |
 **approval_id** | **str**| The approval_id of an approved transactional_email.update request for exactly this change.  See POST /sfvb/approvals. | [optional]

### Return type

[**SfvbTransactionalEmailResponse**](SfvbTransactionalEmailResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_upsell_offer**
> SfvbUpsellOffer update_sfvb_upsell_offer(storefront_oid, upsell_offer_oid, if_match, upsell_offer)

Update an upsell offer

A full replace.  Send back the whole offer you read, changed, with its hash_sha256 in If-Match.  Read only fields are ignored and a writable field left out is cleared.  Changing an offer that is switched on, or changing upsell_item_id_javascript or offsite_content_url, needs sfvb_publish.  An update cannot switch an offer on; that is the enable call, which needs approval.  Settings the API does not show, such as the offer's screenshots, are kept. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_offer_oid** | **int**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **upsell_offer** | [**SfvbUpsellOffer**](SfvbUpsellOffer.md)| The whole offer |

### Return type

[**SfvbUpsellOffer**](SfvbUpsellOffer.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_upsell_path**
> SfvbUpsellPath update_sfvb_upsell_path(storefront_oid, upsell_path_oid, if_match, upsell_path)

Update an upsell path

A full replace.  Send back the whole path you read, changed, with its hash_sha256 in If-Match.  Read only fields are ignored and a writable field left out is cleared.  Order and archived keep their stored values; change them with the move, archive and unarchive calls.  Changing a running path needs sfvb_publish.  An update cannot switch a path on; that is the enable call, which needs approval. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **upsell_path_oid** | **int**|  |
 **if_match** | **str**| hash_sha256 from the last read.  Required; 428 when absent, 412 when stale. |
 **upsell_path** | [**SfvbUpsellPath**](SfvbUpsellPath.md)| The whole path |

### Return type

[**SfvbUpsellPath**](SfvbUpsellPath.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sfvb_utm_shortcode**
> SfvbUtmShortcode update_sfvb_utm_shortcode(storefront_oid, shortcode_oid, if_match, utm_shortcode_request)

Change a UTM shortcode

A partial update.  Fields left out keep their value, and an empty string clears a value.  A changed code is checked like a new one.  The creation date is kept.  Send the hash_sha256 you read as If-Match.  Needs sfvb_publish, because links already in emails and ads that use the code are attributed differently from now on. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **shortcode_oid** | **int**|  |
 **if_match** | **str**| The shortcode&#39;s hash_sha256 from the last read.  428 when absent, 412 when stale. |
 **utm_shortcode_request** | [**SfvbUtmShortcodeRequest**](SfvbUtmShortcodeRequest.md)| The change |

### Return type

[**SfvbUtmShortcode**](SfvbUtmShortcode.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**409** |  |  -  |
**412** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_sfvb_file**
> SfvbFileWriteResponse upload_sfvb_file(storefront_oid, file_upload_request)

Store a binary asset that was already uploaded

The second half of the two step upload.  The bytes are fetched from the key, checked against the extension they claim to be, and written exactly as a text write is - so the same If-Match precondition, the same read only refusal and the same publish gate apply.  An SVG is sanitized before it is stored.  Writing outside /themes/ requires sfvb_publish, because anything served off the storefront root is live by definition. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **file_upload_request** | [**SfvbFileUploadRequest**](SfvbFileUploadRequest.md)| Where to store the uploaded bytes |
 **if_match** | **str**| Content hash from the last read.  Required when the file already exists; 428 when absent, 412 when stale. | [optional]

### Return type

[**SfvbFileWriteResponse**](SfvbFileWriteResponse.md)

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
**403** | Status Code 403: forbidden |  * UC-REST-ERROR - Contains human readable error message <br>  |
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**412** |  |  -  |
**413** |  |  -  |
**428** |  |  -  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_sfvb_cjson**
> SfvbValidationResponse validate_sfvb_cjson(validate_request)

Validate CJSON

Runs the structural schema, the contextual business rules for the destination owner type, and the quality lint.  A document that fails returns HTTP 200 with valid false rather than a transport error - the request was well formed, the document was not. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_request** | [**SfvbValidateRequest**](SfvbValidateRequest.md)| CJSON to validate |

### Return type

[**SfvbValidationResponse**](SfvbValidationResponse.md)

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
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_sfvb_velocity**
> SfvbValidationResponse validate_sfvb_velocity(storefront_oid, theme_oid, velocity_validate_request)

Validate a Velocity template against a theme

Theme scoped rather than stateless.  Validation builds a theme template context and evaluates against it.  Also applies the template sandbox, so an agent learns the rule before a write fails. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **int**|  |
 **theme_oid** | **int**|  |
 **velocity_validate_request** | [**SfvbVelocityValidateRequest**](SfvbVelocityValidateRequest.md)| Velocity template to validate |

### Return type

[**SfvbValidationResponse**](SfvbValidationResponse.md)

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
**404** | Status Code 404: not found |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

