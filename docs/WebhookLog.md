# WebhookLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_dts** | **str** | Date/time of delivery | [optional] 
**duration** | **int** | Number of milliseconds to process the notification | [optional] 
**queue_delay** | **int** | Number of milliseconds of delay caused by queuing | [optional] 
**request** | **str** | Request payload (first 100,000 characters) | [optional] 
**request_headers** | [**[HTTPHeader]**](HTTPHeader.md) | Request headers sent to the server | [optional] 
**request_id** | **str** | Request id is a unique string that you can look up in the logs | [optional] 
**response** | **str** | Response payload (first 100,000 characters) | [optional] 
**response_headers** | [**[HTTPHeader]**](HTTPHeader.md) | Response headers received from the server | [optional] 
**status_code** | **int** | HTTP status code received from the server | [optional] 
**success** | **bool** | True if the delivery was successful | [optional] 
**uri** | **str** | URI of the webhook delivered to | [optional] 
**webhook_oid** | **int** | webhook oid | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


