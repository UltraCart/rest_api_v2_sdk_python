# SfvbTrackingCheckPlan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_version** | **int** | The tracking provider catalog version the plan was built from. | [optional] 
**consent** | **str** | The consent state the plan assumes.  none, all, or the granted categories in the order statistics, preferences, marketing.  Left out when the plan lists every gate instead. | [optional] 
**event** | **str** | page_view, or purchase for a test order receipt. | [optional] 
**notes** | **[str]** | What the plan assumes about the browser and the page. | [optional] 
**order_id** | **str** | The test order a purchase plan is for.  Left out for a page view. | [optional] 
**path** | **str** | The page path the plan is for, as given. | [optional] 
**plan_id** | **str** | The lowercase SHA-256 hex of the UTF-8 bytes of this response written as JSON without plan_id and snippet, with object keys sorted, no white space, and keys whose value is null left out, as JavaScript JSON.stringify writes values.  A results file carries it, so the CLI can tell which plan the results belong to. | [optional] 
**providers** | [**[SfvbTrackingCheckPlanProvider]**](SfvbTrackingCheckPlanProvider.md) | One entry per provider the storefront turns on for this event, then one per host found in custom or affiliate network HTML. | [optional] 
**region** | **str** | Where the browser is, which decides which gates apply.  eea, non-us or other.  Left out when the plan lists every gate instead. | [optional] 
**server_side** | [**[SfvbTrackingCheckPlanServerSide]**](SfvbTrackingCheckPlanServerSide.md) | What providers send from UltraCart servers for this event.  The browser never sees these, so they are reported as not checked. | [optional] 
**snippet** | **str** | The collector, the source of one JavaScript async arrow function.  Run it with addInitScript before the action so it starts before the page scripts, then run it again with evaluate after the action.  The second run waits for 3 seconds of quiet, or 15 seconds at most, and returns plan_id, page, collected_at, requests (url, initiator) and events (via, name, params).  URLs keep only the query params the plan names for that host, and events only the params the plan names.  It never reads cookies, storage or form fields and sends nothing anywhere. | [optional] 
**storefront_oid** | **int** | The storefront. | [optional] 
**unchecked** | [**[SfvbTrackingCheckPlanUnchecked]**](SfvbTrackingCheckPlanUnchecked.md) | What the plan could not predict, and why. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


