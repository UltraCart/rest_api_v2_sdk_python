# SfvbFileSearchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_sensitive** | **bool** | Whether the text search is case sensitive.  Defaults to false. | [optional] 
**dynamic_html** | **bool** | Only dynamic HTML (arbitrary) files. | [optional] 
**file_name** | **str** | Comma separated file name patterns, matched case insensitively with wildcards. | [optional] 
**i18n_violations** | **bool** | Only files with internationalization violations. | [optional] 
**invalid** | **bool** | Only files that failed Velocity validation. | [optional] 
**max_results** | **int** | Maximum results to return.  Clamped to the server maximum. | [optional] 
**merge_conflicts** | **bool** | Only files with unresolved theme merge conflicts. | [optional] 
**mime_type** | **str** | Restrict to a mime type. | [optional] 
**modified_max** | **str** | Only files modified at or before this ISO-8601 timestamp. | [optional] 
**modified_min** | **str** | Only files modified at or after this ISO-8601 timestamp. | [optional] 
**offset** | **int** | Results to skip.  Send the next_offset from a truncated response to continue.  Ordering is by path with the file oid as a tie breaker, so pages do not overlap or skip entries between calls. | [optional] 
**path** | **str** | Restrict to a directory path.  Strongly recommended alongside text. | [optional] 
**size_max** | **int** | Maximum size in bytes. | [optional] 
**size_min** | **int** | Minimum size in bytes. | [optional] 
**sub_directories** | **bool** | Recurse below path.  Defaults to true. | [optional] 
**text** | **str** | Text to find inside files.  Only text/* files are searched.  This is the expensive filter; narrow with path or file_name where possible. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


