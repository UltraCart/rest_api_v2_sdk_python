# FraudRuleSearchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_oid_or_email** | **str** | Affiliate oid (integer) or affiliate email. Email is resolved to oid before searching. | [optional] 
**amount_threshold_begin** | **float** | Lower bound on amount/score/percentage thresholds (rules backed by the same numeric column). | [optional] 
**amount_threshold_end** | **float** |  | [optional] 
**auto_note** | **str** | Wildcard search on the rule&#39;s auto_note. Use &#39;*&#39; for wildcards. | [optional] 
**count_threshold_begin** | **int** | Lower bound on count thresholds (rules backed by the same integer count column). | [optional] 
**count_threshold_end** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_date_begin** | **str** | Rule creation date begin (MM/dd/yyyy) | [optional] 
**created_date_end** | **str** | Rule creation date end (MM/dd/yyyy) | [optional] 
**credit_card_partial** | **str** | Partial credit card number for matching &#39;credit card matches&#39; rules. Use &#39;*&#39; wildcards. | [optional] 
**decline_message** | **str** | Wildcard search on the rule&#39;s decline_message. Use &#39;*&#39; for wildcards. | [optional] 
**failure_action** | **str** |  | [optional] 
**gateway_code** | **str** |  | [optional] 
**merchant_item_id** | **str** |  | [optional] 
**modifier_value** | **str** | Wildcard search on the rule&#39;s secondary modifier (eg &#39;address&#39;/&#39;subnet&#39;, gateway codes, avs match types). | [optional] 
**modify_custom_field1** | **str** |  | [optional] 
**modify_custom_field2** | **str** |  | [optional] 
**modify_custom_field3** | **str** |  | [optional] 
**modify_custom_field4** | **str** |  | [optional] 
**modify_custom_field5** | **str** |  | [optional] 
**modify_custom_field6** | **str** |  | [optional] 
**modify_custom_field7** | **str** |  | [optional] 
**modify_skip_affiliate** | **bool** |  | [optional] 
**modify_skip_affiliate_network_pixel** | **bool** |  | [optional] 
**rule_group** | **str** | Rule group to filter by. | [optional] 
**rule_type** | **str** | Rule type to filter by. | [optional] 
**search_linked_accounts** | **bool** | Include rules from accounts linked to this merchant. Defaults to false. | [optional] 
**storefront_hostname** | **str** |  | [optional] 
**text_value** | **str** | Wildcard search on the rule&#39;s text parameter (email / ip / bin / country / item id / avs codes - the backend disambiguates by rule_type). | [optional] 
**theme_code** | **str** |  | [optional] 
**user_action** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


