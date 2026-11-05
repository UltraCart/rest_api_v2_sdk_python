# SfvbCommsListDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_dts** | **str** | When the list was created. | [optional] 
**folder_uuid** | **str** | The list and segment folder it is filed in, or none. | [optional] 
**hash_sha256** | **str** | The hash of the name, folder and public settings.  Send it as If-Match to change or archive the list. | [optional] 
**list_uuid** | **str** | The list uuid. | [optional] 
**member_count** | **int** | How many customers are on the list. | [optional] 
**name** | **str** | The list name. | [optional] 
**public_description** | **str** | The description subscribers see for a public list. | [optional] 
**public_list** | **bool** | True when subscribers can choose this list on the storefront&#39;s email preferences page. | [optional] 
**used_by** | [**[SfvbCommsSegmentUsedBy]**](SfvbCommsSegmentUsedBy.md) | The campaigns that send to the list and the flows it starts, each with whether it is live. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


