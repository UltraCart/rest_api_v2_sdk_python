# FraudRuleInsertRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_email** | **str** | Affiliate email. Used by the &#39;affiliate matches&#39; rule type when affiliate_oid is not supplied. | [optional] 
**affiliate_oid** | **int** | Affiliate OID. Used by the &#39;affiliate matches&#39; rule type. If omitted, affiliate_email is required. | [optional] 
**amount_threshold** | **float** | Monetary or score threshold. Used by *transaction amount exceeds*, *fraud score exceeds*, and *decline percentage exceeds* rules. | [optional] 
**auto_note** | **str** | Note automatically appended to the order&#39;s merchant note when this rule fires. | [optional] 
**avs_match_type** | **str** | AVS match type for the zip portion. Used by the &#39;address street and zip avs&#39; rule type. | [optional] 
**avs_response_codes** | **str** | AVS response codes (street). Used by the &#39;address street and zip avs&#39; rule type. | [optional] 
**count_threshold** | **int** | Integer count threshold. Used by *count exceeds*, *change number*, *quantity exceeds*, and *purchased within last hours* rules. | [optional] 
**country_code** | **str** | ISO country code. Used by the &#39;address not in country&#39; rule type. | [optional] 
**credit_card_bins** | **bool, date, datetime, dict, float, int, list, str, none_type** | Credit card BINs to block (max 20). Used by the &#39;credit card block bin&#39; rule type. | [optional] 
**email** | **str** | Email address. Used by the &#39;address email&#39; rule type. | [optional] 
**failure_action** | **str** | Action to take when this rule fires. | [optional] 
**gateway_response_codes** | **str** | Gateway response code key. Used by the &#39;gateway response&#39; rule type. | [optional] 
**gateway_response_value** | **str** | Gateway response code value. Used by the &#39;gateway response&#39; rule type. | [optional] 
**ip_address** | **str** | IP address or subnet (eg &#39;192.168.1.1&#39; or &#39;10.0.0.0/8&#39;). Used by &#39;exempt ip&#39; and &#39;ip matches&#39; rules. | [optional] 
**ip_range_type** | **str** | Specifies whether an IP rule applies to a single address or a subnet. | [optional] 
**item_filters** | **bool, date, datetime, dict, float, int, list, str, none_type** | Optional list of merchant item ids restricting this rule to orders containing one or more of these items. | [optional] 
**merchant_item_id** | **str** | Merchant item id. Used by the &#39;item matches&#39; rule type. | [optional] 
**modify_custom_field1** | **str** |  | [optional] 
**modify_custom_field2** | **str** |  | [optional] 
**modify_custom_field3** | **str** |  | [optional] 
**modify_custom_field4** | **str** |  | [optional] 
**modify_custom_field5** | **str** |  | [optional] 
**modify_custom_field6** | **str** |  | [optional] 
**modify_custom_field7** | **str** |  | [optional] 
**modify_skip_affiliate** | **bool** |  | [optional] 
**modify_skip_affiliate_network_pixel** | **bool** |  | [optional] 
**rotating_transaction_gateway_filters** | **bool, date, datetime, dict, float, int, list, str, none_type** | Optional list of rotating transaction gateway oids restricting this rule to orders processed by one of these gateways. | [optional] 
**rule_type** | **str** | Rule type. Also returned by GET /v2/fraud/lookup_values. | [optional] 
**screen_branding_theme_filters** | **bool, date, datetime, dict, float, int, list, str, none_type** | Optional list of screen branding theme oids restricting this rule to orders associated with one or more storefronts. | [optional] 
**user_action** | **str** | Only used by rule types that distinguish between attempted and approved transactions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


