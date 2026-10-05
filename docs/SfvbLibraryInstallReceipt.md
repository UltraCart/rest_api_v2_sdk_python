# SfvbLibraryInstallReceipt


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cjson** | **str** | The fragment, with its file paths rewritten to where they were installed.  Ready to place. | [optional] 
**conflicts** | [**[SfvbLibraryInstallConflict]**](SfvbLibraryInstallConflict.md) | Paths that already held a different file.  With on_conflict fail these refuse the install. | [optional] 
**content_manifest** | [**SfvbLibraryContentManifest**](SfvbLibraryContentManifest.md) |  | [optional] 
**files_skipped** | **[str]** | Paths not written, because an identical or chosen existing file was kept, or the file could not be fetched. | [optional] 
**files_written** | **[str]** | Storefront paths this install wrote. | [optional] 
**library_oid** | **int** | The entry. | [optional] 
**revision_number** | **int** | The revision installed. | [optional] 
**unresolved_parameters** | **[str]** | Required parameters with no default.  Replace them in the cjson before placing it. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


