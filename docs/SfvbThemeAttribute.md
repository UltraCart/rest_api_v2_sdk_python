# SfvbThemeAttribute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_value** | **str** | What the declaring template falls back to when this slot has no value. | [optional] 
**deprecated** | **bool** | True when the theme marks this slot as on its way out.  Prefer not to build on it. | [optional] 
**description** | **str** | What this slot is for, where the theme author documented it. | [optional] 
**font** | [**SfvbThemeFont**](SfvbThemeFont.md) |  | [optional] 
**name** | **str** | Slot name, for example Theme Color 01.  Returned in the casing the theme&#39;s templates declare, which may differ from the casing you wrote.  Compare case insensitively. | [optional] 
**type** | **str** | What kind of slot this is, taken from the template that declares it rather than guessed from the value.  orphan means nothing declares it. | [optional] 
**undeclared** | **bool** | True when no template in this theme references this name.  Writing such a name is allowed and is how the builder stores its own settings, but if you did not mean to create one this is a misspelling and the write changed nothing visible. | [optional] 
**unused** | **bool** | True when the slot is declared but nothing in the theme actually reads it, so setting it has no visible effect. | [optional] 
**value** | **str** | The applied value.  For a colour this is a hex or rgb string, for a boolean the text true or false, for a font the raw JSON document also given in the font field.  When the stored value is empty the current preset&#39;s default is filled in here. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


