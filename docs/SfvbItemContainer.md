# SfvbItemContainer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cjson_size** | **int** | Size of the CJSON in UTF-8 bytes, which is the same unit the container version size and the upsell offer cjson_size use. | [optional] 
**container_name** | **str** | The slot name.  This is the value an itemcontainer element&#39;s itemContainerName setting holds, which is what ties a container to the element that renders it. | [optional] 
**hash_sha256** | **str** | SHA-256 of the container&#39;s CJSON.  Identical to the value a read of the container returns, so a listing is enough to start an If-Match write without reading first. | [optional] 
**last_modified** | **str** | When the container was last written.  Absent for a container untouched since the storage began recording the time, so read an absent value as unknown rather than as never modified. | [optional] 
**merchant_item_id** | **str** | The owning item&#39;s merchant item id.  This is the identifier a storefront carries and a merchant recognizes; the oid appears nowhere on a rendered page.  Send it as owner_type itemid to address the same container without converting it first. | [optional] 
**owner_object_id** | **str** | The merchant item oid, spelled the way containers/item/{owner_object_id} takes it. | [optional] 
**owner_type** | **str** | Always item.  Carried so a row is usable as an address without the caller having to know which listing it came from. | [optional]  if omitted the server will use the default value of "item"
**used_elements** | **[str]** | The element types this container uses, recorded by the storage when it was written.  A large cjson_size beside a handful of element types is the signature of markup pasted into a single html element.  Absent on a container written before the storage began recording this. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


