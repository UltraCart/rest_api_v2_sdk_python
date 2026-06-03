# FraudLookupValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliates** | [**[FraudLookupAffiliate]**](FraudLookupAffiliate.md) | Affiliates with non-empty email, sorted by email. | [optional] 
**avs_match_types** | **[str]** | Valid values for avs_match_type on the &#39;address street and zip avs&#39; rule type. | [optional] 
**countries** | **[str]** | ISO country codes available to this merchant. | [optional] 
**failure_actions** | **[str]** | Valid values for failure_action on insert and search requests. | [optional] 
**ip_range_types** | **[str]** | Valid values for ip_range_type on IP-based rules. | [optional] 
**linked_accounts** | **bool** | True when this merchant has at least one linked merchant account. | [optional] 
**rotating_transaction_gateways** | [**[FraudLookupGateway]**](FraudLookupGateway.md) | Rotating transaction gateways configured for this merchant. Use the oid as a value in rotating_transaction_gateway_filters on insert. | [optional] 
**rule_groups** | **[str]** | Valid values for rule_group on search requests. | [optional] 
**rule_types** | **[str]** | Valid values for rule_type on insert and search requests. | [optional] 
**screen_branding_themes** | [**[FraudLookupTheme]**](FraudLookupTheme.md) | Screen branding themes configured for this merchant. Use the oid as a value in screen_branding_theme_filters on insert. | [optional] 
**user_actions** | **[str]** | Valid values for user_action on rule types that distinguish between attempted and approved transactions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


