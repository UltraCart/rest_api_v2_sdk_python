# ultracart.TaxApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tax_provider_self_city**](TaxApi.md#delete_tax_provider_self_city) | **DELETE** /tax/providers/self/city/{city} | Deletes a Self tax provider city
[**delete_tax_provider_self_country**](TaxApi.md#delete_tax_provider_self_country) | **DELETE** /tax/providers/self/country/{countryCode} | Deletes a Self tax provider country
[**delete_tax_provider_self_county**](TaxApi.md#delete_tax_provider_self_county) | **DELETE** /tax/providers/self/county/{county} | Deletes a Self tax provider county
[**delete_tax_provider_self_postal_code**](TaxApi.md#delete_tax_provider_self_postal_code) | **DELETE** /tax/providers/self/postalCode/{postal_code} | Deletes a Self tax provider postalCode
[**delete_tax_provider_self_state**](TaxApi.md#delete_tax_provider_self_state) | **DELETE** /tax/providers/self/state/{stateCode} | Deletes a Self tax provider state
[**get_tax_provider_avalara**](TaxApi.md#get_tax_provider_avalara) | **GET** /tax/providers/avalara | Retrieve the Avalara tax provider
[**get_tax_provider_avalara_companies**](TaxApi.md#get_tax_provider_avalara_companies) | **POST** /tax/providers/avalara/companies | Returns Avalara Tax companies configured by the merchant
[**get_tax_provider_avalara_test**](TaxApi.md#get_tax_provider_avalara_test) | **GET** /tax/providers/avalara/test | Attempts to connect to Avalara and returns back the response
[**get_tax_provider_self**](TaxApi.md#get_tax_provider_self) | **GET** /tax/providers/self | Retrieve the Self tax provider
[**get_tax_provider_self_countries**](TaxApi.md#get_tax_provider_self_countries) | **GET** /tax/providers/self/countries | Retrieve the Self tax provider countries
[**get_tax_provider_self_regions_by_country_code**](TaxApi.md#get_tax_provider_self_regions_by_country_code) | **GET** /tax/providers/self/regions/{countryCode} | Retrieve the Self tax provider regions for a given country code
[**get_tax_provider_tax_jar**](TaxApi.md#get_tax_provider_tax_jar) | **GET** /tax/providers/taxjar | Retrieve the TaxJar tax provider
[**get_tax_provider_tax_jar_test**](TaxApi.md#get_tax_provider_tax_jar_test) | **GET** /tax/providers/taxjar/test | Attempts to connect to TaxJar and returns back the response
[**get_tax_provider_ultra_cart**](TaxApi.md#get_tax_provider_ultra_cart) | **GET** /tax/providers/ultracart | Retrieve the UltraCart tax provider
[**get_tax_providers**](TaxApi.md#get_tax_providers) | **GET** /tax/providers | Retrieve tax methods
[**set_active_tax_provider**](TaxApi.md#set_active_tax_provider) | **POST** /tax/providers/setActive/{providerName} | Toggle a tax provider to active
[**update_tax_provider_avalara**](TaxApi.md#update_tax_provider_avalara) | **POST** /tax/providers/avalara | Update the Avalara tax provider
[**update_tax_provider_self**](TaxApi.md#update_tax_provider_self) | **POST** /tax/providers/self | Update the Self tax provider
[**update_tax_provider_self_city**](TaxApi.md#update_tax_provider_self_city) | **POST** /tax/providers/self/city/{city} | Updates a Self tax provider city
[**update_tax_provider_self_country**](TaxApi.md#update_tax_provider_self_country) | **POST** /tax/providers/self/country/{countryCode} | Updates a Self tax provider country
[**update_tax_provider_self_county**](TaxApi.md#update_tax_provider_self_county) | **POST** /tax/providers/self/county/{county} | Updates a Self tax provider county
[**update_tax_provider_self_postal_code**](TaxApi.md#update_tax_provider_self_postal_code) | **POST** /tax/providers/self/postalCode/{postal_code} | Updates a Self tax provider postalCode
[**update_tax_provider_self_state**](TaxApi.md#update_tax_provider_self_state) | **POST** /tax/providers/self/state/{stateCode} | Updates a Self tax provider state
[**update_tax_provider_tax_jar**](TaxApi.md#update_tax_provider_tax_jar) | **POST** /tax/providers/taxjar | Update the TaxJar tax provider
[**update_tax_provider_ultra_cart**](TaxApi.md#update_tax_provider_ultra_cart) | **POST** /tax/providers/ultracart | Update the UltraCart tax provider


# **delete_tax_provider_self_city**
> delete_tax_provider_self_city(city, tax_city)

Deletes a Self tax provider city

Deletes a Self tax provider city. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
city = 'city_example' # str | The city being deleted.
tax_city = ultracart.TaxCity() # TaxCity | tax city to be deleted

try: 
    # Deletes a Self tax provider city
    api_instance.delete_tax_provider_self_city(city, tax_city)
except ApiException as e:
    print("Exception when calling TaxApi->delete_tax_provider_self_city: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | **str**| The city being deleted. | 
 **tax_city** | [**TaxCity**](TaxCity.md)| tax city to be deleted | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tax_provider_self_country**
> delete_tax_provider_self_country(country_code, tax_country)

Deletes a Self tax provider country

Deletes a Self tax provider country. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
country_code = 'country_code_example' # str | The country code being deleted.
tax_country = ultracart.TaxCountry() # TaxCountry | tax country to be deleted

try: 
    # Deletes a Self tax provider country
    api_instance.delete_tax_provider_self_country(country_code, tax_country)
except ApiException as e:
    print("Exception when calling TaxApi->delete_tax_provider_self_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The country code being deleted. | 
 **tax_country** | [**TaxCountry**](TaxCountry.md)| tax country to be deleted | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tax_provider_self_county**
> delete_tax_provider_self_county(county, tax_county)

Deletes a Self tax provider county

Deletes a Self tax provider county. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
county = 'county_example' # str | The county being deleted.
tax_county = ultracart.TaxCounty() # TaxCounty | tax county to be deleted

try: 
    # Deletes a Self tax provider county
    api_instance.delete_tax_provider_self_county(county, tax_county)
except ApiException as e:
    print("Exception when calling TaxApi->delete_tax_provider_self_county: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **county** | **str**| The county being deleted. | 
 **tax_county** | [**TaxCounty**](TaxCounty.md)| tax county to be deleted | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tax_provider_self_postal_code**
> delete_tax_provider_self_postal_code(postal_code, tax_postal_code)

Deletes a Self tax provider postalCode

Deletes a Self tax provider postalCode. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
postal_code = 'postal_code_example' # str | The postal code being deleted.
tax_postal_code = ultracart.TaxPostalCode() # TaxPostalCode | tax postal code to be deleted

try: 
    # Deletes a Self tax provider postalCode
    api_instance.delete_tax_provider_self_postal_code(postal_code, tax_postal_code)
except ApiException as e:
    print("Exception when calling TaxApi->delete_tax_provider_self_postal_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postal_code** | **str**| The postal code being deleted. | 
 **tax_postal_code** | [**TaxPostalCode**](TaxPostalCode.md)| tax postal code to be deleted | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tax_provider_self_state**
> delete_tax_provider_self_state(state_code, tax_state)

Deletes a Self tax provider state

Deletes a Self tax provider state. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
state_code = 'state_code_example' # str | The state code being deleted.
tax_state = ultracart.TaxState() # TaxState | tax state to be deleted

try: 
    # Deletes a Self tax provider state
    api_instance.delete_tax_provider_self_state(state_code, tax_state)
except ApiException as e:
    print("Exception when calling TaxApi->delete_tax_provider_self_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_code** | **str**| The state code being deleted. | 
 **tax_state** | [**TaxState**](TaxState.md)| tax state to be deleted | 

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_avalara**
> TaxProviderAvalara get_tax_provider_avalara()

Retrieve the Avalara tax provider

Retrieves the Avalara tax provider. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))

try: 
    # Retrieve the Avalara tax provider
    api_response = api_instance.get_tax_provider_avalara()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->get_tax_provider_avalara: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderAvalara**](TaxProviderAvalara.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_avalara_companies**
> TaxProviderAvalaraCompaniesResult get_tax_provider_avalara_companies(tax_provider_avalara)

Returns Avalara Tax companies configured by the merchant

Returns Avalara Tax companies configured by the merchant 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
tax_provider_avalara = ultracart.TaxProviderAvalara() # TaxProviderAvalara | TaxProviderAvalara object

try: 
    # Returns Avalara Tax companies configured by the merchant
    api_response = api_instance.get_tax_provider_avalara_companies(tax_provider_avalara)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->get_tax_provider_avalara_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_provider_avalara** | [**TaxProviderAvalara**](TaxProviderAvalara.md)| TaxProviderAvalara object | 

### Return type

[**TaxProviderAvalaraCompaniesResult**](TaxProviderAvalaraCompaniesResult.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_avalara_test**
> TaxProviderTestResult get_tax_provider_avalara_test()

Attempts to connect to Avalara and returns back the response

Attempts to connect to Avalara and returns back the response. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))

try: 
    # Attempts to connect to Avalara and returns back the response
    api_response = api_instance.get_tax_provider_avalara_test()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->get_tax_provider_avalara_test: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderTestResult**](TaxProviderTestResult.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_self**
> TaxProviderSelf get_tax_provider_self()

Retrieve the Self tax provider

Retrieves the Self tax provider. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))

try: 
    # Retrieve the Self tax provider
    api_response = api_instance.get_tax_provider_self()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->get_tax_provider_self: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderSelf**](TaxProviderSelf.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_self_countries**
> TaxProviderSelfCountriesResponse get_tax_provider_self_countries()

Retrieve the Self tax provider countries

Retrieves the Self tax provider countries. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))

try: 
    # Retrieve the Self tax provider countries
    api_response = api_instance.get_tax_provider_self_countries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->get_tax_provider_self_countries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderSelfCountriesResponse**](TaxProviderSelfCountriesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_self_regions_by_country_code**
> TaxProviderSelfRegionsResponse get_tax_provider_self_regions_by_country_code(country_code)

Retrieve the Self tax provider regions for a given country code

Retrieves the Self tax provider regions for a given country code. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
country_code = 'country_code_example' # str | The country code regions desired.

try: 
    # Retrieve the Self tax provider regions for a given country code
    api_response = api_instance.get_tax_provider_self_regions_by_country_code(country_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->get_tax_provider_self_regions_by_country_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The country code regions desired. | 

### Return type

[**TaxProviderSelfRegionsResponse**](TaxProviderSelfRegionsResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_tax_jar**
> TaxProviderTaxJar get_tax_provider_tax_jar()

Retrieve the TaxJar tax provider

Retrieves the TaxJar tax provider. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))

try: 
    # Retrieve the TaxJar tax provider
    api_response = api_instance.get_tax_provider_tax_jar()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->get_tax_provider_tax_jar: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderTaxJar**](TaxProviderTaxJar.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_tax_jar_test**
> TaxProviderTestResult get_tax_provider_tax_jar_test()

Attempts to connect to TaxJar and returns back the response

Attempts to connect to TaxJar and returns back the response. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))

try: 
    # Attempts to connect to TaxJar and returns back the response
    api_response = api_instance.get_tax_provider_tax_jar_test()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->get_tax_provider_tax_jar_test: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderTestResult**](TaxProviderTestResult.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_ultra_cart**
> TaxProviderUltraCart get_tax_provider_ultra_cart()

Retrieve the UltraCart tax provider

Retrieves the UltraCart tax provider. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))

try: 
    # Retrieve the UltraCart tax provider
    api_response = api_instance.get_tax_provider_ultra_cart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->get_tax_provider_ultra_cart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderUltraCart**](TaxProviderUltraCart.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_providers**
> TaxProvidersResponse get_tax_providers(limit=limit, offset=offset, expand=expand)

Retrieve tax methods

Retrieves tax methods for this account. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve tax methods
    api_response = api_instance.get_tax_providers(limit=limit, offset=offset, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->get_tax_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**TaxProvidersResponse**](TaxProvidersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_active_tax_provider**
> TaxProviderActivateResult set_active_tax_provider(provider_name)

Toggle a tax provider to active

Toggle a tax provider to active. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
provider_name = 'provider_name_example' # str | The tax provider to set active.

try: 
    # Toggle a tax provider to active
    api_response = api_instance.set_active_tax_provider(provider_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->set_active_tax_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**| The tax provider to set active. | 

### Return type

[**TaxProviderActivateResult**](TaxProviderActivateResult.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_avalara**
> TaxProviderAvalara update_tax_provider_avalara(tax_provider_avalara)

Update the Avalara tax provider

Update the Avalara tax provider. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
tax_provider_avalara = ultracart.TaxProviderAvalara() # TaxProviderAvalara | TaxProviderAvalara object

try: 
    # Update the Avalara tax provider
    api_response = api_instance.update_tax_provider_avalara(tax_provider_avalara)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->update_tax_provider_avalara: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_provider_avalara** | [**TaxProviderAvalara**](TaxProviderAvalara.md)| TaxProviderAvalara object | 

### Return type

[**TaxProviderAvalara**](TaxProviderAvalara.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_self**
> TaxProviderSelf update_tax_provider_self(tax_provider_self)

Update the Self tax provider

Update the Self tax provider. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
tax_provider_self = ultracart.TaxProviderSelf() # TaxProviderSelf | TaxProviderSelf object

try: 
    # Update the Self tax provider
    api_response = api_instance.update_tax_provider_self(tax_provider_self)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->update_tax_provider_self: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_provider_self** | [**TaxProviderSelf**](TaxProviderSelf.md)| TaxProviderSelf object | 

### Return type

[**TaxProviderSelf**](TaxProviderSelf.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_self_city**
> TaxCity update_tax_provider_self_city(city, tax_city)

Updates a Self tax provider city

Updates a Self tax provider city. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
city = 'city_example' # str | The city being updated.
tax_city = ultracart.TaxCity() # TaxCity | tax city to be updated

try: 
    # Updates a Self tax provider city
    api_response = api_instance.update_tax_provider_self_city(city, tax_city)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->update_tax_provider_self_city: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | **str**| The city being updated. | 
 **tax_city** | [**TaxCity**](TaxCity.md)| tax city to be updated | 

### Return type

[**TaxCity**](TaxCity.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_self_country**
> TaxCountry update_tax_provider_self_country(country_code, tax_country)

Updates a Self tax provider country

Updates a Self tax provider country. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
country_code = 'country_code_example' # str | The country code being updated.
tax_country = ultracart.TaxCountry() # TaxCountry | tax country to be updated

try: 
    # Updates a Self tax provider country
    api_response = api_instance.update_tax_provider_self_country(country_code, tax_country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->update_tax_provider_self_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The country code being updated. | 
 **tax_country** | [**TaxCountry**](TaxCountry.md)| tax country to be updated | 

### Return type

[**TaxCountry**](TaxCountry.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_self_county**
> TaxCounty update_tax_provider_self_county(county, tax_county)

Updates a Self tax provider county

Updates a Self tax provider county. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
county = 'county_example' # str | The county being updated.
tax_county = ultracart.TaxCounty() # TaxCounty | tax county to be updated

try: 
    # Updates a Self tax provider county
    api_response = api_instance.update_tax_provider_self_county(county, tax_county)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->update_tax_provider_self_county: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **county** | **str**| The county being updated. | 
 **tax_county** | [**TaxCounty**](TaxCounty.md)| tax county to be updated | 

### Return type

[**TaxCounty**](TaxCounty.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_self_postal_code**
> TaxPostalCode update_tax_provider_self_postal_code(postal_code, tax_postal_code)

Updates a Self tax provider postalCode

Updates a Self tax provider postalCode. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
postal_code = 'postal_code_example' # str | The postal code being updated.
tax_postal_code = ultracart.TaxPostalCode() # TaxPostalCode | tax postal code to be updated

try: 
    # Updates a Self tax provider postalCode
    api_response = api_instance.update_tax_provider_self_postal_code(postal_code, tax_postal_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->update_tax_provider_self_postal_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postal_code** | **str**| The postal code being updated. | 
 **tax_postal_code** | [**TaxPostalCode**](TaxPostalCode.md)| tax postal code to be updated | 

### Return type

[**TaxPostalCode**](TaxPostalCode.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_self_state**
> TaxState update_tax_provider_self_state(state_code, tax_state)

Updates a Self tax provider state

Updates a Self tax provider state. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
state_code = 'state_code_example' # str | The state code being updated.
tax_state = ultracart.TaxState() # TaxState | tax state to be updated

try: 
    # Updates a Self tax provider state
    api_response = api_instance.update_tax_provider_self_state(state_code, tax_state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->update_tax_provider_self_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_code** | **str**| The state code being updated. | 
 **tax_state** | [**TaxState**](TaxState.md)| tax state to be updated | 

### Return type

[**TaxState**](TaxState.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_tax_jar**
> TaxProviderTaxJar update_tax_provider_tax_jar(tax_provider_tax_jar)

Update the TaxJar tax provider

Update the TaxJar tax provider. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
tax_provider_tax_jar = ultracart.TaxProviderTaxJar() # TaxProviderTaxJar | TaxProviderTaxJar object

try: 
    # Update the TaxJar tax provider
    api_response = api_instance.update_tax_provider_tax_jar(tax_provider_tax_jar)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->update_tax_provider_tax_jar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_provider_tax_jar** | [**TaxProviderTaxJar**](TaxProviderTaxJar.md)| TaxProviderTaxJar object | 

### Return type

[**TaxProviderTaxJar**](TaxProviderTaxJar.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_ultra_cart**
> TaxProviderUltraCart update_tax_provider_ultra_cart(tax_provider_ultracart)

Update the UltraCart tax provider

Update the UltraCart tax provider. 

### Example 
```python
from __future__ import print_function
import time
import ultracart
from ultracart.rest import ApiException
from pprint import pprint



configuration = ultracart.Configuration()

# this key is valid only in the UltraCart development system.  You need to supply a valid simple key here.
# See: https://ultracart.atlassian.net/wiki/spaces/ucdoc/pages/38688545/API+Simple+Key
configuration.api_key['x-ultracart-simple-key'] \
    = '4256aaf6dfedfa01582fe9a961ab0100216d737b874a4801582fe9a961ab0100'

configuration.debug = True
configuration.verify_ssl = True  # Development only.  Set to True for production.

api_client = ApiClient(configuration=configuration, header_name='X-UltraCart-Api-Version', header_value='2017-03-01')

api_instance = ultracart.TaxApi(ultracart.ApiClient(configuration))
tax_provider_ultracart = ultracart.TaxProviderUltraCart() # TaxProviderUltraCart | TaxProviderUltraCart object

try: 
    # Update the UltraCart tax provider
    api_response = api_instance.update_tax_provider_ultra_cart(tax_provider_ultracart)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxApi->update_tax_provider_ultra_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_provider_ultracart** | [**TaxProviderUltraCart**](TaxProviderUltraCart.md)| TaxProviderUltraCart object | 

### Return type

[**TaxProviderUltraCart**](TaxProviderUltraCart.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

