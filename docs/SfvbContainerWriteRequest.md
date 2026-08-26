# SfvbContainerWriteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_warnings** | **bool** | Store the container even if quality warnings were raised.  Warnings never block by default; this field exists so a caller can opt into treating them as blocking by setting it false. | [optional] 
**cjson** | **str** | The container JSON to store. | [optional] 
**comment** | **str** | Optional comment recorded against the version this write creates. | [optional] 
**marketing_email** | **bool** | For email containers, whether this is a marketing email.  Selects whether CAN-SPAM footer rules apply. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


