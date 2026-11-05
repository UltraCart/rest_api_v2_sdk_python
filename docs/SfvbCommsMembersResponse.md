# SfvbCommsMembersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_data** | **str** | masked, or shown when show_customer_data was sent. | [optional] 
**list_uuid** | **str** | The list, for a list&#39;s members. | [optional] 
**members** | [**[SfvbCommsMember]**](SfvbCommsMember.md) | This page of members. | [optional] 
**notes** | **[str]** | What to keep in mind, such as how to handle customer data that is shown. | [optional] 
**page** | **int** | The page number, from 1. | [optional] 
**page_size** | **int** | Members per page. | [optional] 
**rebuild_required** | **bool** | For a segment, true while it is being rebuilt, so the members are from the last rebuild. | [optional] 
**segment_uuid** | **str** | The segment, for a segment&#39;s members. | [optional] 
**total_members** | **int** | How many members there are. | [optional] 
**total_pages** | **int** | How many pages there are. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


