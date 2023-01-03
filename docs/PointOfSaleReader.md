# PointOfSaleReader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_type** | **str** | The device type of the reader. | [optional] 
**label** | **str** | The label of the reader. | [optional] 
**merchant_id** | **str** | The merchant id that owns this point of sale reader. | [optional] 
**payment_provider** | **str** | The payment provider for the card reader. | [optional]  if omitted the server will use the default value of "stripe"
**pos_reader_id** | **int** | Object identifier of the point of sale reader. | [optional] 
**pos_register_oid** | **int** | Object identifier of the point of sale register this reader is assigned to. | [optional] 
**serial_number** | **str** | The serial number of the reader. | [optional] 
**stripe_account_id** | **str** | If the payment provider is Stripe, this is the Stripe account id | [optional] 
**stripe_reader_id** | **str** | If the payment provide is Stripe, this is the Stripe terminal reader id | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


