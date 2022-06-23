# TaxCountry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_code** | **str** | Accounting code for programs such as QuickBooks | [optional] 
**country_code** | **str** | Country code (2 characters | [optional] 
**country_oid** | **int** | Tax record object identifier used internally by database | [optional] 
**states** | [**[TaxState]**](TaxState.md) | States (or regions or territories) within this country | [optional] 
**tax_gift_charge** | **bool** | True if taxation within this jurisdiction should charge tax on gift charge | [optional] 
**tax_gift_wrap** | **bool** | True if taxation within this jurisdiction should charge tax on gift wrap | [optional] 
**tax_rate** | **float** | Tax Rate | [optional] 
**tax_rate_formatted** | **str** | Tax rate formatted | [optional] 
**tax_shipping** | **bool** | True if taxation within this jurisdiction should charge tax on shipping | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


