# SfvbUpsellPath


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the path runs.  Setting it true, or changing a path that is active, needs the sfvb_publish scope. | [optional] 
**archived** | **bool** | Read only here.  Filed out of the default list.  Change it with the archive and unarchive calls. | [optional] 
**customer_type** | **str** | Which customers the path runs for.  all (the default), new or existing. | [optional] 
**hash_sha256** | **str** | Read only.  Hash of the path&#39;s writable fields.  Send it in If-Match on an update. | [optional] 
**item_logic_suppression** | [**SfvbUpsellItemLogic**](SfvbUpsellItemLogic.md) |  | [optional] 
**item_logic_trigger** | [**SfvbUpsellItemLogic**](SfvbUpsellItemLogic.md) |  | [optional] 
**location** | **str** | Where in checkout the path runs.  pre checkout or post checkout (the default). | [optional] 
**maximum_offers** | **int** | Most offers one shopper is shown on this path.  Omitted or null for no limit. | [optional] 
**name** | **str** | Path name, at most 100 characters. | [optional] 
**path_order** | **int** | Read only here.  Position among this storefront&#39;s paths, first to last.  Change it with the move call. | [optional] 
**path_type** | **str** | cascading (the default) or single. | [optional] 
**towerdata_trigger** | [**SfvbUpsellTowerData**](SfvbUpsellTowerData.md) |  | [optional] 
**trigger_item_ids** | **[str]** | Read only.  The legacy flat trigger list, derived from item_logic_trigger when its logic is contains_any and empty otherwise. | [optional] 
**trigger_tags** | **[str]** | Customer tags that trigger the path. | [optional] 
**upsell_path_oid** | **int** | Read only.  Upsell path oid. | [optional] 
**variations** | [**[SfvbUpsellVariation]**](SfvbUpsellVariation.md) | The variations shoppers are split between.  At least one. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


