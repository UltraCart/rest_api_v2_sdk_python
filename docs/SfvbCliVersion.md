# SfvbCliVersion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cutoff** | **str** | The date (yyyy-MM-dd) the minimum will be raised to the recommended version.  Omitted when none is announced. | [optional] 
**minimum** | **str** | The lowest supported version.  Omitted when none is set. | [optional] 
**recommended** | **str** | The version to upgrade to.  Omitted when none is set. | [optional] 
**reported** | **str** | The version the CLI sent in X-UltraCart-CLI-Version.  Omitted when it sent none, which is read as 0.0.0. | [optional] 
**status** | **str** | ok, deprecated (below recommended - keep working, tell the merchant to upgrade) or unsupported (below minimum - every other call is refused with 426 sfvb.cli_upgrade_required). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


