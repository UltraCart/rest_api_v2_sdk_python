# FraudRulePublic


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_oid** | **int** |  | [optional] 
**amount_threshold** | **float** |  | [optional] 
**auto_note** | **str** |  | [optional] 
**avs_match_type** | **str** |  | [optional] 
**avs_response_codes** | **str** |  | [optional] 
**card_number** | **str** | Masked credit card number for rules tied to a specific card | [optional] 
**count_threshold** | **int** |  | [optional] 
**country_code** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_dts** | **str** | Created date | [optional] 
**credit_card_bins** | **bool, date, datetime, dict, float, int, list, str, none_type** | Credit card BINs blocked by the &#39;credit card block bin&#39; rule type. | [optional] 
**decline_message** | **str** |  | [optional] 
**description** | **str** | Human-readable description of the rule | [optional] 
**description_html** | **str** | HTML version of the rule description | [optional] 
**email** | **str** |  | [optional] 
**failure_action** | **str** | Action taken when this rule fires. | [optional] 
**fraud_rule_oid** | **int** | UltraCart unique identifier for this fraud rule | [optional] 
**gateway_response_codes** | **str** |  | [optional] 
**gateway_response_value** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**ip_range_type** | **str** |  | [optional] 
**item_filters** | [**[FraudRuleItemFilter]**](FraudRuleItemFilter.md) |  | [optional] 
**merchant_item_id** | **str** |  | [optional] 
**modify_custom_field1** | **str** |  | [optional] 
**modify_custom_field2** | **str** |  | [optional] 
**modify_custom_field3** | **str** |  | [optional] 
**modify_custom_field4** | **str** |  | [optional] 
**modify_custom_field5** | **str** |  | [optional] 
**modify_custom_field6** | **str** |  | [optional] 
**modify_custom_field7** | **str** |  | [optional] 
**modify_skip_affiliate** | **bool** |  | [optional] 
**modify_skip_affiliate_network_pixel** | **bool** |  | [optional] 
**rotating_transaction_gateway_filters** | [**[FraudRuleRotatingTransactionGatewayFilter]**](FraudRuleRotatingTransactionGatewayFilter.md) |  | [optional] 
**rule_group** | **str** | Group containing this rule type (eg &#39;creditCardRules&#39;). Deliberately not constrained by allowableValues on the response so SDK consumers do not hard-fail on an unexpected value if a future rule_type slips through the server-side mapping. Search REQUESTS still restrict rule_group to the known set. | [optional] 
**rule_type** | **str** | Rule type. | [optional] 
**storefront_filters** | [**[FraudRuleStorefrontFilter]**](FraudRuleStorefrontFilter.md) |  | [optional] 
**user_action** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


