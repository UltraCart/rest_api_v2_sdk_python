# SfvbUtmShortcode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The shortcode.  Matched ignoring case. | [optional] 
**creation_dts** | **str** | When the shortcode was created, ISO 8601. | [optional] 
**description** | **str** | What the shortcode is for.  Null when blank. | [optional] 
**hash_sha256** | **str** | The hash of the code, description and values.  Send it as If-Match when changing or deleting the shortcode. | [optional] 
**itm_campaign** | **str** | ITM campaign the shortcode applies.  Null when blank. | [optional] 
**itm_content** | **str** | ITM content the shortcode applies.  Null when blank. | [optional] 
**itm_id** | **str** | ITM id the shortcode applies.  Null when blank. | [optional] 
**itm_medium** | **str** | ITM medium the shortcode applies.  Null when blank. | [optional] 
**itm_source** | **str** | ITM (internal tracking) source the shortcode applies.  Null when blank. | [optional] 
**itm_term** | **str** | ITM term the shortcode applies.  Null when blank. | [optional] 
**last_modified_dts** | **str** | When the shortcode last changed, ISO 8601. | [optional] 
**path_segment** | **str** | Append this to a storefront path (as its last segment) to apply the shortcode.  Fires only where that full path is not itself a page. | [optional] 
**query_parameter** | **str** | Add this query parameter to a link on any page running UC Analytics, including other sites, to apply the shortcode. | [optional] 
**shortcode_oid** | **int** | The shortcode&#39;s id on this storefront. | [optional] 
**utm_campaign** | **str** | UTM campaign the shortcode applies.  Null when blank. | [optional] 
**utm_content** | **str** | UTM content the shortcode applies.  Null when blank. | [optional] 
**utm_id** | **str** | UTM id the shortcode applies.  Null when blank. | [optional] 
**utm_medium** | **str** | UTM medium the shortcode applies.  Null when blank. | [optional] 
**utm_source** | **str** | UTM source the shortcode applies.  Null when blank. | [optional] 
**utm_term** | **str** | UTM term the shortcode applies.  Null when blank. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


