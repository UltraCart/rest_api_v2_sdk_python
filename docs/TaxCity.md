# TaxCity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_code** | **str** | Accounting code for programs such as QuickBooks | [optional] 
**city** | **str** | City | [optional] 
**city_oid** | **int** | Tax record object identifier used internally by database | [optional] 
**county_oid** | **int** | Tax record object identifier used internally by database | [optional] 
**dont_collect_city** | **bool** | Flag instructing engine to not collect city tax for this city | [optional] 
**dont_collect_postal_code** | **bool** | Flag instructing engine to not collect postal code tax for this city | [optional] 
**postal_codes** | [**[TaxPostalCode]**](TaxPostalCode.md) | Postal Codes within this city | [optional] 
**tax_rate** | **float** | Tax Rate | [optional] 
**tax_rate_formatted** | **str** | Tax rate formatted | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


