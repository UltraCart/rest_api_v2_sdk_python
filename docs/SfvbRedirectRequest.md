# SfvbRedirectRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Why the rule exists, up to 500 characters. | [optional] 
**over_live_page** | **bool** | Allow a source that is a live, visible page or item, which the rule then hides. | [optional] 
**source** | **str** | The path to catch, starting with /.  End it with /* to catch everything below. | [optional] 
**status** | **str** | Updates only.  301 turns an admin rule into a permanent redirect.  Leave empty to keep the rule&#39;s status.  New rules are always 301. | [optional] 
**target** | **str** | A path on the storefront, or a URL on one of its own hosts. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


