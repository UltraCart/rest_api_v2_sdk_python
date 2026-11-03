# SfvbTrackingHtmlResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_bytes** | **int** | The largest HTML the API writes to a slot, in UTF-8 bytes.  The admin allows larger, but UltraCart&#39;s review must read the whole of it. | [optional] 
**slots** | [**[SfvbTrackingHtml]**](SfvbTrackingHtml.md) | tracking and conversion, each with its size and hash_sha256.  Read one slot for its content. | [optional] 
**storefront_oid** | **int** | The storefront. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


