# SfvbItemPricing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** | The price. | [optional] 
**currency_code** | **str** | The currency every amount is in.  Read only here. | [optional] 
**hash_sha256** | **str** | The hash of the pricing above.  Send it as If-Match to change it. | [optional] 
**merchant_item_id** | **str** | The item&#39;s merchant item id. | [optional] 
**merchant_item_oid** | **int** | The item. | [optional] 
**msrp** | **float** | The manufacturer suggested retail price, when set. | [optional] 
**sale_active** | **bool** | Whether the sale price applies right now. | [optional] 
**sale_cost** | **float** | The sale price, when a sale is set. | [optional] 
**sale_end** | **str** | When the sale ends, ISO 8601. | [optional] 
**sale_start** | **str** | When the sale starts, ISO 8601. | [optional] 
**volume_discounts** | [**[SfvbItemVolumeDiscount]**](SfvbItemVolumeDiscount.md) | Retail quantity breaks, lowest quantity first.  Wholesale pricing tiers are not shown or changed here. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


