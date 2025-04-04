# EmailSegment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_csv_download** | **bool** | True if the current user has the rights to download this segment. | [optional] 
**allow_facebook_audiences** | **bool** | True if this StoreFront has the Facebook Analytics app connected and supports them | [optional] 
**created_dts** | **str** | Created date | [optional] 
**deleted** | **bool** | True if this campaign was deleted | [optional] 
**email_segment_uuid** | **str** | Email segment UUID | [optional] 
**esp_list_segment_folder_uuid** | **str** | List/Segment folder UUID | [optional] 
**facebook_custom_audience** | **bool** | True if you want to sync to a facebook custom audience | [optional] 
**filter_profile_equation_json** | **str** | File profile equation json | [optional] 
**member_count** | **int** | Count of members in this segment | [optional] 
**merchant_id** | **str** | Merchant ID | [optional] 
**name** | **str** | Name of email segment | [optional] 
**rank_json** | **str** | Rank settings json | [optional] 
**rebuild_percentage** | **float** | Percentage of completion for a rebuild.  The value range will be 0-1.  Multiply by 100 to format for display. | [optional] 
**rebuild_required** | **bool** | True if a rebuild is required because some part of the segment has changed | [optional] 
**storefront_oid** | **int** | Storefront oid | [optional] 
**thirdparty_join_add_tags** | **[str]** | Third party provider tags to add when a customer joins the segment. | [optional] 
**thirdparty_join_remove_tags** | **[str]** | Third party provider tags to remove when a customer joins the segment. | [optional] 
**thirdparty_leave_add_tags** | **[str]** | Third party provider tags to add when a customer leaves the segment. | [optional] 
**thirdparty_leave_remove_tags** | **[str]** | Third party provider tags to remove when a customer leaves the segment. | [optional] 
**thirdparty_list_id** | **str** | List id of third party provider to sync with. | [optional] 
**thirdparty_provider_name** | **str** | Name of third party provider to sync segment to a list with. | [optional] 
**used_by** | [**[EmailListSegmentUsedBy]**](EmailListSegmentUsedBy.md) | Details on the flows or campaigns that use this list. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


