# SfvbDocsGap


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duplicate** | **bool** | On submit, true when this account had already sent the same report.  The earlier report_id is returned and nothing new is kept. | [optional] 
**received_at** | **str** | When UltraCart received the report. | [optional] 
**report_id** | **str** | The report&#39;s id.  Quote it to UltraCart, or look the report up with GET docs/gaps/{report_id}. | [optional] 
**status** | **str** | received until UltraCart staff look at it, then accepted, declined or fixed. | [optional] 
**status_at** | **str** | When the status last changed.  Absent while the report is received. | [optional] 
**storefront_oid** | **int** | The storefront named when the report was sent, if one was. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


