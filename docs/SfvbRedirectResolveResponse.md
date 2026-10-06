# SfvbRedirectResolveResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**final_path** | **str** | Where the shopper ends up.  The storefront sends them straight there in one redirect. | [optional] 
**final_status** | **str** | The status the shopper gets, 301, 302, rewrite, or none when no rule matches. | [optional] 
**lands_on** | **str** | live_page, hidden_page, item, not_found or other (a file or system path). | [optional] 
**path** | **str** | The path asked about. | [optional] 
**steps** | [**[SfvbRedirectResolveStep]**](SfvbRedirectResolveStep.md) | Each redirect followed, in order.  Empty when no rule matches. | [optional] 
**too_long** | **bool** | True when the chain is longer than the storefront follows. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


