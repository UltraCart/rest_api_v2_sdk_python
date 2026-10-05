# SfvbLibraryAiReview


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**findings** | **bool, date, datetime, dict, float, int, list, str, none_type** | What the reviewers found.  detail is the category followed by the quoted evidence. | [optional] 
**prompt_version** | **str** | Version of the review policy that produced this verdict. | [optional] 
**reviewed_dts** | **str** | When the review ran, ISO 8601. | [optional] 
**screenshot_sha256** | **str** | The screenshot the review looked at, or absent when there was none. | [optional] 
**summary** | **str** | One or two sentences explaining the verdict. | [optional] 
**verdict** | **str** | approve, block, human or error.  block refuses any publish.  human or error refuses a public publish and is recorded on a shared one. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


