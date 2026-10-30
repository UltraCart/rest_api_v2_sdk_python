# SfvbCommsSegmentDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_dts** | **str** | When it was created (ISO 8601, UTC). | [optional] 
**filter_profile_equation_json** | **str** | The rule, as JSON text in the admin editor&#39;s shape.  Every entry in groups must hold, and inside a group one function is enough. | [optional] 
**folder_uuid** | **str** | The list and segment folder it is filed in, or absent. | [optional] 
**hash_sha256** | **str** | Send as If-Match on an update.  Covers the name, the rule and the folder. | [optional] 
**member_count** | **int** | How many customers it held at its last rebuild.  Out of date while rebuild_required is true. | [optional] 
**name** | **str** | The segment name. | [optional] 
**rebuild_nightly** | **bool** | True when the rule has a date range, so the segment is also rebuilt every night. | [optional] 
**rebuild_percentage** | **float** | How far the current rebuild has got, when one is running. | [optional] 
**rebuild_required** | **bool** | True when the rule changed and the segment has not finished rebuilding. | [optional] 
**segment_uuid** | **str** | The segment uuid. | [optional] 
**used_by** | [**[SfvbCommsSegmentUsedBy]**](SfvbCommsSegmentUsedBy.md) | The campaigns that send to it and the flows it starts. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


