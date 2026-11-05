# SfvbPostcardTrackingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cards** | [**[SfvbPostcardCard]**](SfvbPostcardCard.md) | This page of cards. | [optional] 
**customer_data** | **str** | masked, or shown when show_customer_data was sent. | [optional] 
**notes** | **[str]** | What to keep in mind, such as how to handle customer data that is shown. | [optional] 
**page** | **int** | The page number, from 1. | [optional] 
**page_cost** | **float** | The total cost of the cards on this page. | [optional] 
**page_size** | **int** | Cards per page. | [optional] 
**postcard_uuid** | **str** | The postcard. | [optional] 
**total_cards** | **int** | How many cards have been mailed for this postcard. | [optional] 
**total_pages** | **int** | How many pages there are. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


