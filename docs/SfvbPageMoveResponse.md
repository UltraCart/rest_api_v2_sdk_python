# SfvbPageMoveResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | True when nothing was moved. | [optional] 
**new_path** | **str** | The page&#39;s path after the move. | [optional] 
**page** | [**SfvbPageResponse**](SfvbPageResponse.md) |  | [optional] 
**pages_moved** | **int** | How many pages moved, the page itself included. | [optional] 
**path** | **str** | The page&#39;s path before the move. | [optional] 
**redirect** | [**SfvbRedirect**](SfvbRedirect.md) |  | [optional] 
**redirect_source** | **str** | The pattern the old addresses redirect from, when a redirect was asked for. | [optional] 
**warnings** | [**[SfvbErrorDetail]**](SfvbErrorDetail.md) | Findings that did not block the move, such as a redirect chain. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


