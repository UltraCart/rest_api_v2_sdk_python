# FraudRuleSearchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_oid_or_email** | **str** | Affiliate oid (integer) or affiliate email. Email is resolved to oid before searching. | [optional] 
**amount_threshold_begin** | **float** | Lower bound on amount/score/percentage thresholds (rules backed by the same numeric column). | [optional] 
**amount_threshold_end** | **float** | Upper bound on amount/score/percentage thresholds (rules backed by the same numeric column). | [optional] 
**auto_note** | **str** | Wildcard search on the rule&#39;s auto_note. Use &#39;*&#39; for wildcards. | [optional] 
**count_threshold_begin** | **int** | Lower bound on count thresholds (rules backed by the same integer count column). | [optional] 
**count_threshold_end** | **int** | Upper bound on count thresholds (rules backed by the same integer count column). | [optional] 
**created_by** | **str** | Filter to rules created by this user login. | [optional] 
**created_date_begin** | **str** | Rule creation date begin (MM/dd/yyyy) | [optional] 
**created_date_end** | **str** | Rule creation date end (MM/dd/yyyy) | [optional] 
**credit_card_partial** | **str** | Partial credit card number for matching &#39;credit card matches&#39; rules. Use &#39;*&#39; wildcards. | [optional] 
**decline_message** | **str** | Wildcard search on the rule&#39;s decline_message. Use &#39;*&#39; for wildcards. | [optional] 
**failure_action** | **str** |  | [optional] 
**gateway_code** | **str** | Filter to rules with this rotating transaction gateway code in their rotating_transaction_gateway_filters list. | [optional] 
**merchant_item_id** | **str** | Filter to rules with this merchant item id in their item_filters list. | [optional] 
**modifier_value** | **str** | Wildcard search on the rule&#39;s secondary modifier (eg &#39;address&#39;/&#39;subnet&#39;, gateway codes, avs match types). | [optional] 
**modify_custom_field1** | **str** | Wildcard search on rules&#39; modify_custom_field1 value. | [optional] 
**modify_custom_field2** | **str** | Wildcard search on rules&#39; modify_custom_field2 value. | [optional] 
**modify_custom_field3** | **str** | Wildcard search on rules&#39; modify_custom_field3 value. | [optional] 
**modify_custom_field4** | **str** | Wildcard search on rules&#39; modify_custom_field4 value. | [optional] 
**modify_custom_field5** | **str** | Wildcard search on rules&#39; modify_custom_field5 value. | [optional] 
**modify_custom_field6** | **str** | Wildcard search on rules&#39; modify_custom_field6 value. | [optional] 
**modify_custom_field7** | **str** | Wildcard search on rules&#39; modify_custom_field7 value. | [optional] 
**modify_skip_affiliate** | **bool** | Filter to rules whose modify_skip_affiliate flag matches this value. | [optional] 
**modify_skip_affiliate_network_pixel** | **bool** | Filter to rules whose modify_skip_affiliate_network_pixel flag matches this value. | [optional] 
**rule_group** | **str** | Rule group to filter by. | [optional] 
**rule_type** | **str** | Rule type to filter by. | [optional] 
**search_linked_accounts** | **bool** | Include rules from accounts linked to this merchant. Defaults to false. | [optional] 
**storefront_hostname** | **str** | Filter to rules with this storefront hostname in their screen_branding_theme_filters list. | [optional] 
**text_value** | **str** | Wildcard search on the rule&#39;s text parameter (email / ip / bin / country / item id / avs codes - the backend disambiguates by rule_type). | [optional] 
**theme_code** | **str** | Filter to rules with this screen branding theme code in their screen_branding_theme_filters list. | [optional] 
**user_action** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


