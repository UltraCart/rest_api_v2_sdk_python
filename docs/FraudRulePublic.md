# FraudRulePublic


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_oid** | **int** | Affiliate oid for the &#39;affiliate matches&#39; rule type. | [optional] 
**amount_threshold** | **float** | Monetary or score threshold for amount/score/percentage rule types. | [optional] 
**auto_note** | **str** | Note automatically appended to the order&#39;s merchant note when this rule fires. | [optional] 
**avs_match_type** | **str** |  | [optional] 
**avs_response_codes** | **str** | AVS response codes for the &#39;address street and zip avs&#39; rule type. | [optional] 
**card_number** | **str** | Masked credit card number for rules tied to a specific card | [optional] 
**count_threshold** | **int** | Integer count threshold for count/quantity/hours rule types. | [optional] 
**country_code** | **str** | ISO country code for the &#39;address not in country&#39; rule type. | [optional] 
**created_by** | **str** |  | [optional] 
**created_dts** | **str** | Created date | [optional] 
**credit_card_bins** | **[str]** | Credit card BINs blocked by the &#39;credit card block bin&#39; rule type. | [optional] 
**decline_message** | **str** | Message shown in the A/R review screen when this rule fires. | [optional] 
**description** | **str** | Human-readable description of the rule | [optional] 
**description_html** | **str** | HTML version of the rule description | [optional] 
**email** | **str** | Email address for the &#39;address email&#39; rule type. | [optional] 
**failure_action** | **str** | Action taken when this rule fires. | [optional] 
**fraud_rule_oid** | **int** | UltraCart unique identifier for this fraud rule | [optional] 
**gateway_response_codes** | **str** | Gateway response code key for the &#39;gateway response&#39; rule type. | [optional] 
**gateway_response_value** | **str** | Gateway response code value for the &#39;gateway response&#39; rule type. | [optional] 
**ip_address** | **str** | IP address or subnet for &#39;exempt ip&#39; and &#39;ip matches&#39; rule types. | [optional] 
**ip_range_type** | **str** |  | [optional] 
**item_filters** | [**[FraudRuleItemFilter]**](FraudRuleItemFilter.md) | Item filters restricting this rule to orders containing one or more of these items. | [optional] 
**merchant_item_id** | **str** | Merchant item id for the &#39;item matches&#39; rule type. | [optional] 
**modify_custom_field1** | **str** | Value the rule sets on order custom field 1 (only meaningful for &#39;Process Payment and Modify&#39;). | [optional] 
**modify_custom_field2** | **str** | Value the rule sets on order custom field 2 (only meaningful for &#39;Process Payment and Modify&#39;). | [optional] 
**modify_custom_field3** | **str** | Value the rule sets on order custom field 3 (only meaningful for &#39;Process Payment and Modify&#39;). | [optional] 
**modify_custom_field4** | **str** | Value the rule sets on order custom field 4 (only meaningful for &#39;Process Payment and Modify&#39;). | [optional] 
**modify_custom_field5** | **str** | Value the rule sets on order custom field 5 (only meaningful for &#39;Process Payment and Modify&#39;). | [optional] 
**modify_custom_field6** | **str** | Value the rule sets on order custom field 6 (only meaningful for &#39;Process Payment and Modify&#39;). | [optional] 
**modify_custom_field7** | **str** | Value the rule sets on order custom field 7 (only meaningful for &#39;Process Payment and Modify&#39;). | [optional] 
**modify_skip_affiliate** | **bool** | When true, the rule strips the affiliate from the order (only meaningful for &#39;Process Payment and Modify&#39;). | [optional] 
**modify_skip_affiliate_network_pixel** | **bool** | When true, the rule suppresses the affiliate network pixel (only meaningful for &#39;Process Payment and Modify&#39;). | [optional] 
**rotating_transaction_gateway_filters** | [**[FraudRuleRotatingTransactionGatewayFilter]**](FraudRuleRotatingTransactionGatewayFilter.md) | Gateway filters restricting this rule to orders processed by one of these rotating transaction gateways. | [optional] 
**rule_group** | **str** | Group containing this rule type (eg &#39;creditCardRules&#39;). Deliberately not constrained by allowableValues on the response so SDK consumers do not hard-fail on an unexpected value if a future rule_type slips through the server-side mapping. Search REQUESTS still restrict rule_group to the known set. | [optional] 
**rule_type** | **str** | Rule type. | [optional] 
**storefront_filters** | [**[FraudRuleStorefrontFilter]**](FraudRuleStorefrontFilter.md) | Storefront filters restricting this rule to orders placed on one of these storefronts. | [optional] 
**user_action** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


