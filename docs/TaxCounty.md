# TaxCounty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_code** | **str** | Accounting code for programs such as QuickBooks | [optional] 
**cities** | [**list[TaxCity]**](TaxCity.md) | Cities within this city | [optional] 
**county** | **str** | County | [optional] 
**county_oid** | **int** | Tax record object identifier used internally by database | [optional] 
**dont_collect_city** | **bool** | Flag instructing engine to not collect city tax for this county | [optional] 
**dont_collect_county** | **bool** | Flag instructing engine to not collect county tax for this county | [optional] 
**dont_collect_postal_code** | **bool** | Flag instructing engine to not collect postal code tax for this county | [optional] 
**state_oid** | **int** | Tax record object identifier used internally by database | [optional] 
**tax_rate** | **float** | Tax Rate | [optional] 
**tax_rate_formatted** | **str** | Tax rate formatted | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


