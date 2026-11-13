# SfvbPageMoveRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | True to run every check and report what would move, without moving anything or needing an approval. | [optional] 
**new_path** | **str** | Where the page goes, for example /lp/summer-sale/ or /sale/spring/.  Its parent page must exist, and nothing may be at this path yet. | [optional] 
**path** | **str** | The page to move, for example /lp/spring-sale/. | [optional] 
**redirect_note** | **str** | The note on that redirect rule.  Up to 500 characters.  A note naming the move is used when left out. | [optional] 
**redirect_old_url** | **str** | 301 to add one pattern redirect from the old path, sub-pages and items included, to the new one in the same call.  Leave it out to add none, and the old addresses answer 404. | [optional]  if omitted the server will use the default value of "301"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


