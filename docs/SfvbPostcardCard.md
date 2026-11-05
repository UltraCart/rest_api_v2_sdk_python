# SfvbPostcardCard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_dts** | **str** | When the customer ordered after it. | [optional] 
**cost** | **float** | What the account is billed for this card. | [optional] 
**customer_uuid** | **str** | The customer it was mailed to. | [optional] 
**delivered_dts** | **str** | When it was delivered. | [optional] 
**_from** | [**SfvbPostcardAddress**](SfvbPostcardAddress.md) |  | [optional] 
**mailed_dts** | **str** | When it was mailed. | [optional] 
**order_id** | **str** | The order it converted to. | [optional] 
**print_record_uuid** | **str** | The print vendor&#39;s record for this card. | [optional] 
**status** | **str** | The vendor&#39;s latest status. | [optional] 
**submit_dts** | **str** | When it was sent to the printer. | [optional] 
**to** | [**SfvbPostcardAddress**](SfvbPostcardAddress.md) |  | [optional] 
**tracking_description** | **str** | The vendor&#39;s own words for the latest status.  Only when customer data was asked for, since it can name where the card went. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


