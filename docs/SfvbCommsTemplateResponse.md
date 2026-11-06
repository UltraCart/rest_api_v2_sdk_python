# SfvbCommsTemplateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_cjson** | **str** | The template&#39;s body, as CJSON. | [optional] 
**email_template_vm_path** | **str** | The Velocity template it renders inside, as stored.  It is looked up in the storefront&#39;s active theme. | [optional] 
**notes** | **[str]** | What isn&#39;t shown. | [optional] 
**template** | [**SfvbCommsTemplate**](SfvbCommsTemplate.md) |  | [optional] 
**template_exists** | **bool** | True when the file at template_path exists. | [optional] 
**template_note** | **str** | Why there is no template file, or null when there is one. | [optional] 
**template_path** | **str** | The theme file that template is, as a render finds it.  Read it with the files endpoints, whose read also reports valid and velocity_errors.  Null when it couldn&#39;t be worked out, with template_note saying why. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


