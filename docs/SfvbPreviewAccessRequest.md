# SfvbPreviewAccessRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Storefront path to land on, beginning with a slash.  Defaults to / | [optional] 
**preview_session_id** | **str** | Staged preview session to show.  It must be one this user created and it must not have expired.  Leave it out to show the saved containers with nothing staged. | [optional] 
**theme_oid** | **int** | Theme to show, which may be inactive.  Must belong to this storefront.  Defaults to the active theme. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


