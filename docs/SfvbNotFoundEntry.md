# SfvbNotFoundEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_hits** | **int** | Bot hits since bot counting began on this entry.  Empty when not yet counted. | [optional] 
**bot_share** | **bool, date, datetime, dict, float, int, list, str, none_type** | bot_hits divided by counted_hits, 0 to 1.  Empty when not yet counted. | [optional] 
**counted_hits** | **int** | Hits since bot counting began, the base for bot_share. | [optional] 
**first_seen_dts** | **str** | First hit, ISO 8601. | [optional] 
**hits** | **int** | Every recorded hit, bots included. | [optional] 
**ignored** | **bool** | True when the entry is ignored and no longer counts. | [optional] 
**last_seen_dts** | **str** | Latest hit, ISO 8601. | [optional] 
**not_found_id** | **str** | The entry&#39;s id. | [optional] 
**path** | **str** | The path, without its query string.  Token-like segments show as {token} unless asked for. | [optional] 
**redirected_to** | **str** | Where a redirect rule now sends this path, when one does. | [optional] 
**referrer_hosts** | **[str]** | Hosts of the pages that linked to it. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


