# SfvbI18nLanguagesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed** | **bool** | On enable or disable, false when the language was already in that state and nothing was saved. | [optional] 
**character_estimate** | **int** | About how many characters of storefront text one language translates. | [optional] 
**default_language_code** | **str** | The code of the language shoppers start in.  The source of every string is still English. | [optional] 
**hash_sha256** | **str** | Send back as If-Match when enabling or disabling a language. | [optional] 
**languages** | [**[SfvbI18nLanguage]**](SfvbI18nLanguage.md) | Every language the storefront can be translated into, enabled or not, English first. | [optional] 
**per_language_cost** | **str** | The estimated machine translation cost of enabling one more language, formatted. | [optional] 
**storefront_oid** | **int** | The storefront. | [optional] 
**supports_i18n** | **bool** | False when the active theme takes its languages from locale files.  Language and message writes are refused then. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


