# ItemEbay


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | True if the item is active for listing | [optional] 
**category_id** | **int** | e-Bay category ID | [optional] 
**category_specifics** | [**[ItemEbayCategorySpecific]**](ItemEbayCategorySpecific.md) | Answers to category specific questions | [optional] 
**condition_description** | **str** | Description of the condition (e-Bay constant) | [optional] 
**condition_id** | **int** | Numerical ID of the condition (e-Bay constant) | [optional] 
**consecutive_failures** | **int** | Number of consecutive failures trying to list this item | [optional] 
**custom_category1** | **int** | e-Bay Store category 1 | [optional] 
**custom_category2** | **int** | e-Bay Store category 2 | [optional] 
**dispatch_time_max** | **int** | Maximum number of days it will take to ship the item | [optional] 
**domestic_1_additional_cost** | **float** | Domestic 1 method additional item cost | [optional] 
**domestic_1_first_cost** | **float** | Domestic 1 method first item cost | [optional] 
**domestic_2_additional_cost** | **float** | Domestic 2 method additional item cost | [optional] 
**domestic_2_first_cost** | **float** | Domestic 2 method first item cost | [optional] 
**domestic_3_additional_cost** | **float** | Domestic 3 method additional item cost | [optional] 
**domestic_3_first_cost** | **float** | Domestic 3 method first item cost | [optional] 
**domestic_4_additional_cost** | **float** | Domestic 4 method additional item cost | [optional] 
**domestic_4_first_cost** | **float** | Domestic 4 method first item cost | [optional] 
**ebay_auction_id** | **str** | If listed, this is the e-Bay auction id | [optional] 
**ebay_specific_inventory** | **int** | e-Bay specific inventory | [optional] 
**ebay_template_name** | **str** | The template name to use hwen rendering the e-Bay listing | [optional] 
**ebay_template_oid** | **int** | The template object identifier to use when rendering the e-Bay listing | [optional] 
**end_time** | **str** | Date/time of the auction end | [optional] 
**free_shipping** | **bool** | True if item receives free shipping | [optional] 
**free_shipping_method** | **str** | The method that is free for free shipping | [optional] 
**international_1_additional_cost** | **float** | International 1 method additional item cost | [optional] 
**international_1_first_cost** | **float** | International 1 method first item cost | [optional] 
**international_2_additional_cost** | **float** | International 2 method additional item cost | [optional] 
**international_2_first_cost** | **float** | International 2 method first item cost | [optional] 
**international_3_additional_cost** | **float** | International 3 method additional item cost | [optional] 
**international_3_first_cost** | **float** | International 3 method first item cost | [optional] 
**international_4_additional_cost** | **float** | International 4 method additional item cost | [optional] 
**international_4_first_cost** | **float** | International 4 method first item cost | [optional] 
**last_status_dts** | **str** | Date/time of the last status check | [optional] 
**listed_dispatch_time_max** | **int** | Current listing dispatch time maximum | [optional] 
**listed_ebay_template_oid** | **int** | The template object identifier used for the listing | [optional] 
**listing_dts** | **str** | Date/time of the listing | [optional] 
**listing_duration** | **str** | The duration of the listing | [optional] 
**listing_price** | **float** | Price to list the item at | [optional] 
**listing_price_override** | **float** | The price to list the item at if different than the regular UltraCart item price | [optional] 
**listing_type** | **str** | The type of e-Bay listing | [optional] 
**marketplace_analysis** | [**ItemEbayMarketPlaceAnalysis**](ItemEbayMarketPlaceAnalysis.md) |  | [optional] 
**marketplace_analysis_perform** | **bool** | True if marketplace analysis should be performed | [optional] 
**marketplace_final_value_fee_percentage** | **float** | Marketplace FVF percentage | [optional] 
**marketplace_last_check_dts** | **str** | Date/time of the marketplace analysis last check | [optional] 
**marketplace_lowest** | **bool** | True if we are the lowest offer in the marketplace | [optional] 
**marketplace_map_violation** | **bool** | True if another seller is violating MAP | [optional] 
**marketplace_multiplier** | **float** | Marketplace multiplier | [optional] 
**marketplace_other_price** | **float** | Marketplace other price | [optional] 
**marketplace_other_seller** | **str** | Marketplace other seller | [optional] 
**marketplace_other_shipping** | **float** | Marketplace other shipping | [optional] 
**marketplace_other_total** | **float** | Marketplace other total | [optional] 
**marketplace_our_additional_profit_potential** | **float** | Marketplace our additional profit potential | [optional] 
**marketplace_our_price** | **float** | Marketplace our price | [optional] 
**marketplace_our_profit** | **float** | Marketplace our profit | [optional] 
**marketplace_our_shipping** | **float** | Marketplace our shipping | [optional] 
**marketplace_our_total** | **float** | Marketplace our total | [optional] 
**marketplace_overhead** | **float** | Marketplace overhead | [optional] 
**marketplace_profitable** | **bool** | True if our listing is profitable to sell | [optional] 
**next_attempt_dts** | **str** | Date/time for the next attempt to list | [optional] 
**next_listing_duration** | **str** | The next listing duration to use when the current listing ends. | [optional] 
**no_promotional_shipping** | **bool** | True if the item should not qualify for promotional shipping | [optional] 
**packaging_handling_costs** | **float** | Packaging and handling costs | [optional] 
**previous_ebay_auction_id** | **str** | Previous e-Bay auction id | [optional] 
**quantity** | **int** | Quantity available of the item | [optional] 
**reserve_price** | **float** | Reserve price | [optional] 
**send_dimensions_and_weight** | **str** | How to send the item dimensions and weights to e-Bay | [optional] 
**start_time** | **str** | Date/time of the auction start | [optional] 
**status** | **str** | Status of the item&#39;s listing | [optional] 
**target_dispatch_time_max** | **int** | Typical number of days it will take to ship the item | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


