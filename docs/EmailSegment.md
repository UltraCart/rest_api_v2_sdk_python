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
**rebuild_required** | **bool** | True if a rebuild is required because some part of the segment has changed | [optional] 
**storefront_oid** | **int** | Storefront oid | [optional] 
**used_by** | [**list[EmailListSegmentUsedBy]**](EmailListSegmentUsedBy.md) | Details on the flows or campaigns that use this list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


