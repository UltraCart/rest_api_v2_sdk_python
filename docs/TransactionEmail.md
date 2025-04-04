# TransactionEmail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Actual template contents | [optional] 
**esp_domain_uuid** | **str** | The uuid of the sending domain | [optional] 
**esp_friendly_name** | **str** | Friendly from that will appear in customer email clients. | [optional] 
**esp_user** | **str** | The username of the sending email.  This is not the full email.  Only the username which is everything before the @ sign. | [optional] 
**file_exists** | **bool** | An internal identifier used to aid in retrieving templates from the filesystem. | [optional] 
**file_name** | **str** | File name | [optional] 
**group** | **str** | Group | [optional] 
**handlebar_variables** | **[str]** | Handlebar Variables available for email template | [optional] 
**invalid** | **bool** | Invalid will be true if the template cannot compile | [optional] 
**last_modified** | **str** | Last modified timestamp | [optional] 
**library_item_oid** | **int** | If this item was ever added to the Code Library, this is the oid for that library item, or 0 if never added before.  This value is used to determine if a library item should be inserted or updated. | [optional] 
**options** | [**[TransactionEmailOption]**](TransactionEmailOption.md) | Options that help govern how and when this template is used | [optional] 
**path** | **str** | directory path where template is stored in file system | [optional] 
**size** | **str** | Size of file in friendly description | [optional] 
**store_front_fs_directory_oid** | **int** | Internal identifier used to store and retrieve template from filesystem | [optional] 
**store_front_fs_file_oid** | **int** | Internal identifier used to store and retrieve template from filesystem | [optional] 
**subject** | **str** | Subject | [optional] 
**syntax_errors** | **str** | Any syntax errors contained within the tempalate | [optional] 
**template_path_relative_path** | **str** | Internal value used to locate the template in the filesystem | [optional] 
**theme_relative_path** | **str** | Theme relative path in the filesystem. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


