# BulkJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **str** | When the job reached a terminal status | [optional] 
**duplicate_count** | **int** | Records short-circuited as duplicates | [optional] 
**error_code** | **str** | Job-level failure code when status is failed | [optional] 
**fail_count** | **int** | Records that failed | [optional] 
**job_id** | **str** | Public-facing job id (uc-bulk-&lt;ulid&gt;) | [optional] 
**object** | **str** | Object type this job processes | [optional] 
**operation** | **str** | Mutation mode this job runs (the bulk surface is write-only) | [optional] 
**processed_records** | **int** | Records processed so far | [optional] 
**queue_position** | **int** | Position behind the merchant&#39;s active job (queued jobs only) | [optional] 
**results_summary_url** | **str** | Presigned S3 URL to the full per-record results NDJSON (set when finished) | [optional] 
**started_at** | **str** | When the worker started the job | [optional] 
**status** | **str** | Job status | [optional] 
**submitted_at** | **str** | When the job was submitted | [optional] 
**success_count** | **int** | Records that landed | [optional] 
**total_records** | **int** | Total records counted on the first pass (null until counted) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


