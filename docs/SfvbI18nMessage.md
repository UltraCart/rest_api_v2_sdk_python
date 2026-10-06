# SfvbI18nMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edited** | **bool** | True when the English was changed from the template&#39;s text. | [optional] 
**english_text** | **str** | The English text, the source every other language is translated from. | [optional] 
**hash_sha256** | **str** | Send back as If-Match when setting or resetting this message. | [optional] 
**imported** | **bool** | True when the message came from an older theme&#39;s locale file.  It cannot be reset. | [optional] 
**key** | **str** | The message key. | [optional] 
**theme_oid** | **int** | The theme the message belongs to.  Messages are kept per storefront and theme. | [optional] 
**translations** | [**[SfvbI18nTranslation]**](SfvbI18nTranslation.md) | Each enabled language other than English, with its text and where it comes from. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


