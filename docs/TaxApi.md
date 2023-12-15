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
[**get_tax_provider_sovos**](TaxApi.md#get_tax_provider_sovos) | **GET** /tax/providers/sovos | Retrieve the Sovos tax provider
[**get_tax_provider_sovos_test**](TaxApi.md#get_tax_provider_sovos_test) | **GET** /tax/providers/sovos/test | Attempts to connect to Sovos and returns back the response
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
[**update_tax_provider_sovos**](TaxApi.md#update_tax_provider_sovos) | **POST** /tax/providers/sovos | Update the Sovos tax provider
[**update_tax_provider_tax_jar**](TaxApi.md#update_tax_provider_tax_jar) | **POST** /tax/providers/taxjar | Update the TaxJar tax provider
[**update_tax_provider_ultra_cart**](TaxApi.md#update_tax_provider_ultra_cart) | **POST** /tax/providers/ultracart | Update the UltraCart tax provider


# **delete_tax_provider_self_city**
> delete_tax_provider_self_city(city, tax_city)

Deletes a Self tax provider city

Deletes a Self tax provider city. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.tax_city import TaxCity
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    city = "city_example" # str | The city being deleted.
    tax_city = TaxCity(
        accounting_code="accounting_code_example",
        city="city_example",
        city_oid=1,
        county_oid=1,
        dont_collect_city=True,
        dont_collect_postal_code=True,
        postal_codes=[
            TaxPostalCode(
                accounting_code="accounting_code_example",
                city_oid=1,
                dont_collect_postal_code=True,
                postal_code="postal_code_example",
                postal_code_oid=1,
                tax_rate=3.14,
                tax_rate_formatted="tax_rate_formatted_example",
            ),
        ],
        tax_rate=3.14,
        tax_rate_formatted="tax_rate_formatted_example",
    ) # TaxCity | tax city to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Deletes a Self tax provider city
        api_instance.delete_tax_provider_self_city(city, tax_city)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tax_provider_self_country**
> delete_tax_provider_self_country(country_code, tax_country)

Deletes a Self tax provider country

Deletes a Self tax provider country. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_country import TaxCountry
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    country_code = "countryCode_example" # str | The country code being deleted.
    tax_country = TaxCountry(
        accounting_code="accounting_code_example",
        country_code="country_code_example",
        country_oid=1,
        states=[
            TaxState(
                accounting_code="accounting_code_example",
                counties=[
                    TaxCounty(
                        accounting_code="accounting_code_example",
                        cities=[
                            TaxCity(
                                accounting_code="accounting_code_example",
                                city="city_example",
                                city_oid=1,
                                county_oid=1,
                                dont_collect_city=True,
                                dont_collect_postal_code=True,
                                postal_codes=[
                                    TaxPostalCode(
                                        accounting_code="accounting_code_example",
                                        city_oid=1,
                                        dont_collect_postal_code=True,
                                        postal_code="postal_code_example",
                                        postal_code_oid=1,
                                        tax_rate=3.14,
                                        tax_rate_formatted="tax_rate_formatted_example",
                                    ),
                                ],
                                tax_rate=3.14,
                                tax_rate_formatted="tax_rate_formatted_example",
                            ),
                        ],
                        county="county_example",
                        county_oid=1,
                        dont_collect_city=True,
                        dont_collect_county=True,
                        dont_collect_postal_code=True,
                        state_oid=1,
                        tax_rate=3.14,
                        tax_rate_formatted="tax_rate_formatted_example",
                    ),
                ],
                country_oid=1,
                dont_collect_city=True,
                dont_collect_county=True,
                dont_collect_postal_code=True,
                dont_collect_state=True,
                exempt_digital_items=True,
                exempt_physical_items=True,
                exempt_service_items=True,
                state_code="state_code_example",
                state_oid=1,
                tax_gift_charge=True,
                tax_gift_wrap=True,
                tax_rate=3.14,
                tax_rate_formatted="tax_rate_formatted_example",
                tax_shipping=True,
                use_ultracart_managed_rates=True,
            ),
        ],
        tax_gift_charge=True,
        tax_gift_wrap=True,
        tax_rate=3.14,
        tax_rate_formatted="tax_rate_formatted_example",
        tax_shipping=True,
    ) # TaxCountry | tax country to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Deletes a Self tax provider country
        api_instance.delete_tax_provider_self_country(country_code, tax_country)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tax_provider_self_county**
> delete_tax_provider_self_county(county, tax_county)

Deletes a Self tax provider county

Deletes a Self tax provider county. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_county import TaxCounty
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    county = "county_example" # str | The county being deleted.
    tax_county = TaxCounty(
        accounting_code="accounting_code_example",
        cities=[
            TaxCity(
                accounting_code="accounting_code_example",
                city="city_example",
                city_oid=1,
                county_oid=1,
                dont_collect_city=True,
                dont_collect_postal_code=True,
                postal_codes=[
                    TaxPostalCode(
                        accounting_code="accounting_code_example",
                        city_oid=1,
                        dont_collect_postal_code=True,
                        postal_code="postal_code_example",
                        postal_code_oid=1,
                        tax_rate=3.14,
                        tax_rate_formatted="tax_rate_formatted_example",
                    ),
                ],
                tax_rate=3.14,
                tax_rate_formatted="tax_rate_formatted_example",
            ),
        ],
        county="county_example",
        county_oid=1,
        dont_collect_city=True,
        dont_collect_county=True,
        dont_collect_postal_code=True,
        state_oid=1,
        tax_rate=3.14,
        tax_rate_formatted="tax_rate_formatted_example",
    ) # TaxCounty | tax county to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Deletes a Self tax provider county
        api_instance.delete_tax_provider_self_county(county, tax_county)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tax_provider_self_postal_code**
> delete_tax_provider_self_postal_code(postal_code, tax_postal_code)

Deletes a Self tax provider postalCode

Deletes a Self tax provider postalCode. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_postal_code import TaxPostalCode
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    postal_code = "postal_code_example" # str | The postal code being deleted.
    tax_postal_code = TaxPostalCode(
        accounting_code="accounting_code_example",
        city_oid=1,
        dont_collect_postal_code=True,
        postal_code="postal_code_example",
        postal_code_oid=1,
        tax_rate=3.14,
        tax_rate_formatted="tax_rate_formatted_example",
    ) # TaxPostalCode | tax postal code to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Deletes a Self tax provider postalCode
        api_instance.delete_tax_provider_self_postal_code(postal_code, tax_postal_code)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tax_provider_self_state**
> delete_tax_provider_self_state(state_code, tax_state)

Deletes a Self tax provider state

Deletes a Self tax provider state. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_state import TaxState
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    state_code = "stateCode_example" # str | The state code being deleted.
    tax_state = TaxState(
        accounting_code="accounting_code_example",
        counties=[
            TaxCounty(
                accounting_code="accounting_code_example",
                cities=[
                    TaxCity(
                        accounting_code="accounting_code_example",
                        city="city_example",
                        city_oid=1,
                        county_oid=1,
                        dont_collect_city=True,
                        dont_collect_postal_code=True,
                        postal_codes=[
                            TaxPostalCode(
                                accounting_code="accounting_code_example",
                                city_oid=1,
                                dont_collect_postal_code=True,
                                postal_code="postal_code_example",
                                postal_code_oid=1,
                                tax_rate=3.14,
                                tax_rate_formatted="tax_rate_formatted_example",
                            ),
                        ],
                        tax_rate=3.14,
                        tax_rate_formatted="tax_rate_formatted_example",
                    ),
                ],
                county="county_example",
                county_oid=1,
                dont_collect_city=True,
                dont_collect_county=True,
                dont_collect_postal_code=True,
                state_oid=1,
                tax_rate=3.14,
                tax_rate_formatted="tax_rate_formatted_example",
            ),
        ],
        country_oid=1,
        dont_collect_city=True,
        dont_collect_county=True,
        dont_collect_postal_code=True,
        dont_collect_state=True,
        exempt_digital_items=True,
        exempt_physical_items=True,
        exempt_service_items=True,
        state_code="state_code_example",
        state_oid=1,
        tax_gift_charge=True,
        tax_gift_wrap=True,
        tax_rate=3.14,
        tax_rate_formatted="tax_rate_formatted_example",
        tax_shipping=True,
        use_ultracart_managed_rates=True,
    ) # TaxState | tax state to be deleted

    # example passing only required values which don't have defaults set
    try:
        # Deletes a Self tax provider state
        api_instance.delete_tax_provider_self_state(state_code, tax_state)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_avalara**
> TaxProviderAvalara get_tax_provider_avalara()

Retrieve the Avalara tax provider

Retrieves the Avalara tax provider. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_provider_avalara import TaxProviderAvalara
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve the Avalara tax provider
        api_response = api_instance.get_tax_provider_avalara()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling TaxApi->get_tax_provider_avalara: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderAvalara**](TaxProviderAvalara.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_avalara_companies**
> TaxProviderAvalaraCompaniesResult get_tax_provider_avalara_companies(tax_provider_avalara)

Returns Avalara Tax companies configured by the merchant

Returns Avalara Tax companies configured by the merchant 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_provider_avalara_companies_result import TaxProviderAvalaraCompaniesResult
from ultracart.model.tax_provider_avalara import TaxProviderAvalara
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    tax_provider_avalara = TaxProviderAvalara(
        configuration=AvalaraConfig(
            account_id="account_id_example",
            active=True,
            avalara_oid=1,
            company_id="company_id_example",
            enable_upc=True,
            estimate_only=True,
            guest_customer_code="guest_customer_code_example",
            last_test_dts="last_test_dts_example",
            license_key="license_key_example",
            sandbox=True,
            send_test_orders=True,
            service_url="service_url_example",
            test_results="test_results_example",
        ),
        description="description_example",
        selected=True,
        title="title_example",
    ) # TaxProviderAvalara | TaxProviderAvalara object

    # example passing only required values which don't have defaults set
    try:
        # Returns Avalara Tax companies configured by the merchant
        api_response = api_instance.get_tax_provider_avalara_companies(tax_provider_avalara)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_avalara_test**
> TaxProviderTestResult get_tax_provider_avalara_test()

Attempts to connect to Avalara and returns back the response

Attempts to connect to Avalara and returns back the response. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.tax_provider_test_result import TaxProviderTestResult
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Attempts to connect to Avalara and returns back the response
        api_response = api_instance.get_tax_provider_avalara_test()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling TaxApi->get_tax_provider_avalara_test: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderTestResult**](TaxProviderTestResult.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_self**
> TaxProviderSelf get_tax_provider_self()

Retrieve the Self tax provider

Retrieves the Self tax provider. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.tax_provider_self import TaxProviderSelf
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve the Self tax provider
        api_response = api_instance.get_tax_provider_self()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling TaxApi->get_tax_provider_self: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderSelf**](TaxProviderSelf.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_self_countries**
> TaxProviderSelfCountriesResponse get_tax_provider_self_countries()

Retrieve the Self tax provider countries

Retrieves the Self tax provider countries. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.tax_provider_self_countries_response import TaxProviderSelfCountriesResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve the Self tax provider countries
        api_response = api_instance.get_tax_provider_self_countries()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling TaxApi->get_tax_provider_self_countries: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderSelfCountriesResponse**](TaxProviderSelfCountriesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_self_regions_by_country_code**
> TaxProviderSelfRegionsResponse get_tax_provider_self_regions_by_country_code(country_code)

Retrieve the Self tax provider regions for a given country code

Retrieves the Self tax provider regions for a given country code. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_provider_self_regions_response import TaxProviderSelfRegionsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    country_code = "countryCode_example" # str | The country code regions desired.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the Self tax provider regions for a given country code
        api_response = api_instance.get_tax_provider_self_regions_by_country_code(country_code)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_sovos**
> TaxProviderSovos get_tax_provider_sovos()

Retrieve the Sovos tax provider

Retrieves the Sovos tax provider. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_provider_sovos import TaxProviderSovos
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve the Sovos tax provider
        api_response = api_instance.get_tax_provider_sovos()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling TaxApi->get_tax_provider_sovos: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderSovos**](TaxProviderSovos.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_sovos_test**
> TaxProviderTestResult get_tax_provider_sovos_test()

Attempts to connect to Sovos and returns back the response

Attempts to connect to Sovos and returns back the response. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.tax_provider_test_result import TaxProviderTestResult
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Attempts to connect to Sovos and returns back the response
        api_response = api_instance.get_tax_provider_sovos_test()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling TaxApi->get_tax_provider_sovos_test: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderTestResult**](TaxProviderTestResult.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_tax_jar**
> TaxProviderTaxJar get_tax_provider_tax_jar()

Retrieve the TaxJar tax provider

Retrieves the TaxJar tax provider. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_provider_tax_jar import TaxProviderTaxJar
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve the TaxJar tax provider
        api_response = api_instance.get_tax_provider_tax_jar()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling TaxApi->get_tax_provider_tax_jar: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderTaxJar**](TaxProviderTaxJar.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_tax_jar_test**
> TaxProviderTestResult get_tax_provider_tax_jar_test()

Attempts to connect to TaxJar and returns back the response

Attempts to connect to TaxJar and returns back the response. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.tax_provider_test_result import TaxProviderTestResult
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Attempts to connect to TaxJar and returns back the response
        api_response = api_instance.get_tax_provider_tax_jar_test()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling TaxApi->get_tax_provider_tax_jar_test: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderTestResult**](TaxProviderTestResult.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_provider_ultra_cart**
> TaxProviderUltraCart get_tax_provider_ultra_cart()

Retrieve the UltraCart tax provider

Retrieves the UltraCart tax provider. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_provider_ultra_cart import TaxProviderUltraCart
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve the UltraCart tax provider
        api_response = api_instance.get_tax_provider_ultra_cart()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling TaxApi->get_tax_provider_ultra_cart: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxProviderUltraCart**](TaxProviderUltraCart.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_providers**
> TaxProvidersResponse get_tax_providers()

Retrieve tax methods

Retrieves tax methods for this account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_providers_response import TaxProvidersResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) if omitted the server will use the default value of 100
    offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) if omitted the server will use the default value of 0
    expand = "_expand_example" # str | The object expansion to perform on the result.  See documentation for examples (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve tax methods
        api_response = api_instance.get_tax_providers(limit=limit, offset=offset, expand=expand)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling TaxApi->get_tax_providers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**TaxProvidersResponse**](TaxProvidersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_active_tax_provider**
> TaxProviderActivateResult set_active_tax_provider(provider_name)

Toggle a tax provider to active

Toggle a tax provider to active. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.tax_provider_activate_result import TaxProviderActivateResult
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    provider_name = "providerName_example" # str | The tax provider to set active.

    # example passing only required values which don't have defaults set
    try:
        # Toggle a tax provider to active
        api_response = api_instance.set_active_tax_provider(provider_name)
        pprint(api_response)
    except ultracart.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_avalara**
> TaxProviderAvalara update_tax_provider_avalara(tax_provider_avalara)

Update the Avalara tax provider

Update the Avalara tax provider. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_provider_avalara import TaxProviderAvalara
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    tax_provider_avalara = TaxProviderAvalara(
        configuration=AvalaraConfig(
            account_id="account_id_example",
            active=True,
            avalara_oid=1,
            company_id="company_id_example",
            enable_upc=True,
            estimate_only=True,
            guest_customer_code="guest_customer_code_example",
            last_test_dts="last_test_dts_example",
            license_key="license_key_example",
            sandbox=True,
            send_test_orders=True,
            service_url="service_url_example",
            test_results="test_results_example",
        ),
        description="description_example",
        selected=True,
        title="title_example",
    ) # TaxProviderAvalara | TaxProviderAvalara object

    # example passing only required values which don't have defaults set
    try:
        # Update the Avalara tax provider
        api_response = api_instance.update_tax_provider_avalara(tax_provider_avalara)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_self**
> TaxProviderSelf update_tax_provider_self(tax_provider_self)

Update the Self tax provider

Update the Self tax provider. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.tax_provider_self import TaxProviderSelf
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    tax_provider_self = TaxProviderSelf(
        configuration=SelfConfig(
            tax_billing=True,
        ),
        countries=[
            TaxCountry(
                accounting_code="accounting_code_example",
                country_code="country_code_example",
                country_oid=1,
                states=[
                    TaxState(
                        accounting_code="accounting_code_example",
                        counties=[
                            TaxCounty(
                                accounting_code="accounting_code_example",
                                cities=[
                                    TaxCity(
                                        accounting_code="accounting_code_example",
                                        city="city_example",
                                        city_oid=1,
                                        county_oid=1,
                                        dont_collect_city=True,
                                        dont_collect_postal_code=True,
                                        postal_codes=[
                                            TaxPostalCode(
                                                accounting_code="accounting_code_example",
                                                city_oid=1,
                                                dont_collect_postal_code=True,
                                                postal_code="postal_code_example",
                                                postal_code_oid=1,
                                                tax_rate=3.14,
                                                tax_rate_formatted="tax_rate_formatted_example",
                                            ),
                                        ],
                                        tax_rate=3.14,
                                        tax_rate_formatted="tax_rate_formatted_example",
                                    ),
                                ],
                                county="county_example",
                                county_oid=1,
                                dont_collect_city=True,
                                dont_collect_county=True,
                                dont_collect_postal_code=True,
                                state_oid=1,
                                tax_rate=3.14,
                                tax_rate_formatted="tax_rate_formatted_example",
                            ),
                        ],
                        country_oid=1,
                        dont_collect_city=True,
                        dont_collect_county=True,
                        dont_collect_postal_code=True,
                        dont_collect_state=True,
                        exempt_digital_items=True,
                        exempt_physical_items=True,
                        exempt_service_items=True,
                        state_code="state_code_example",
                        state_oid=1,
                        tax_gift_charge=True,
                        tax_gift_wrap=True,
                        tax_rate=3.14,
                        tax_rate_formatted="tax_rate_formatted_example",
                        tax_shipping=True,
                        use_ultracart_managed_rates=True,
                    ),
                ],
                tax_gift_charge=True,
                tax_gift_wrap=True,
                tax_rate=3.14,
                tax_rate_formatted="tax_rate_formatted_example",
                tax_shipping=True,
            ),
        ],
        description="description_example",
        selected=True,
        title="title_example",
    ) # TaxProviderSelf | TaxProviderSelf object

    # example passing only required values which don't have defaults set
    try:
        # Update the Self tax provider
        api_response = api_instance.update_tax_provider_self(tax_provider_self)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_self_city**
> TaxCity update_tax_provider_self_city(city, tax_city)

Updates a Self tax provider city

Updates a Self tax provider city. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.tax_city import TaxCity
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    city = "city_example" # str | The city being updated.
    tax_city = TaxCity(
        accounting_code="accounting_code_example",
        city="city_example",
        city_oid=1,
        county_oid=1,
        dont_collect_city=True,
        dont_collect_postal_code=True,
        postal_codes=[
            TaxPostalCode(
                accounting_code="accounting_code_example",
                city_oid=1,
                dont_collect_postal_code=True,
                postal_code="postal_code_example",
                postal_code_oid=1,
                tax_rate=3.14,
                tax_rate_formatted="tax_rate_formatted_example",
            ),
        ],
        tax_rate=3.14,
        tax_rate_formatted="tax_rate_formatted_example",
    ) # TaxCity | tax city to be updated

    # example passing only required values which don't have defaults set
    try:
        # Updates a Self tax provider city
        api_response = api_instance.update_tax_provider_self_city(city, tax_city)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_self_country**
> TaxCountry update_tax_provider_self_country(country_code, tax_country)

Updates a Self tax provider country

Updates a Self tax provider country. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_country import TaxCountry
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    country_code = "countryCode_example" # str | The country code being updated.
    tax_country = TaxCountry(
        accounting_code="accounting_code_example",
        country_code="country_code_example",
        country_oid=1,
        states=[
            TaxState(
                accounting_code="accounting_code_example",
                counties=[
                    TaxCounty(
                        accounting_code="accounting_code_example",
                        cities=[
                            TaxCity(
                                accounting_code="accounting_code_example",
                                city="city_example",
                                city_oid=1,
                                county_oid=1,
                                dont_collect_city=True,
                                dont_collect_postal_code=True,
                                postal_codes=[
                                    TaxPostalCode(
                                        accounting_code="accounting_code_example",
                                        city_oid=1,
                                        dont_collect_postal_code=True,
                                        postal_code="postal_code_example",
                                        postal_code_oid=1,
                                        tax_rate=3.14,
                                        tax_rate_formatted="tax_rate_formatted_example",
                                    ),
                                ],
                                tax_rate=3.14,
                                tax_rate_formatted="tax_rate_formatted_example",
                            ),
                        ],
                        county="county_example",
                        county_oid=1,
                        dont_collect_city=True,
                        dont_collect_county=True,
                        dont_collect_postal_code=True,
                        state_oid=1,
                        tax_rate=3.14,
                        tax_rate_formatted="tax_rate_formatted_example",
                    ),
                ],
                country_oid=1,
                dont_collect_city=True,
                dont_collect_county=True,
                dont_collect_postal_code=True,
                dont_collect_state=True,
                exempt_digital_items=True,
                exempt_physical_items=True,
                exempt_service_items=True,
                state_code="state_code_example",
                state_oid=1,
                tax_gift_charge=True,
                tax_gift_wrap=True,
                tax_rate=3.14,
                tax_rate_formatted="tax_rate_formatted_example",
                tax_shipping=True,
                use_ultracart_managed_rates=True,
            ),
        ],
        tax_gift_charge=True,
        tax_gift_wrap=True,
        tax_rate=3.14,
        tax_rate_formatted="tax_rate_formatted_example",
        tax_shipping=True,
    ) # TaxCountry | tax country to be updated

    # example passing only required values which don't have defaults set
    try:
        # Updates a Self tax provider country
        api_response = api_instance.update_tax_provider_self_country(country_code, tax_country)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_self_county**
> TaxCounty update_tax_provider_self_county(county, tax_county)

Updates a Self tax provider county

Updates a Self tax provider county. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_county import TaxCounty
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    county = "county_example" # str | The county being updated.
    tax_county = TaxCounty(
        accounting_code="accounting_code_example",
        cities=[
            TaxCity(
                accounting_code="accounting_code_example",
                city="city_example",
                city_oid=1,
                county_oid=1,
                dont_collect_city=True,
                dont_collect_postal_code=True,
                postal_codes=[
                    TaxPostalCode(
                        accounting_code="accounting_code_example",
                        city_oid=1,
                        dont_collect_postal_code=True,
                        postal_code="postal_code_example",
                        postal_code_oid=1,
                        tax_rate=3.14,
                        tax_rate_formatted="tax_rate_formatted_example",
                    ),
                ],
                tax_rate=3.14,
                tax_rate_formatted="tax_rate_formatted_example",
            ),
        ],
        county="county_example",
        county_oid=1,
        dont_collect_city=True,
        dont_collect_county=True,
        dont_collect_postal_code=True,
        state_oid=1,
        tax_rate=3.14,
        tax_rate_formatted="tax_rate_formatted_example",
    ) # TaxCounty | tax county to be updated

    # example passing only required values which don't have defaults set
    try:
        # Updates a Self tax provider county
        api_response = api_instance.update_tax_provider_self_county(county, tax_county)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_self_postal_code**
> TaxPostalCode update_tax_provider_self_postal_code(postal_code, tax_postal_code)

Updates a Self tax provider postalCode

Updates a Self tax provider postalCode. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_postal_code import TaxPostalCode
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    postal_code = "postal_code_example" # str | The postal code being updated.
    tax_postal_code = TaxPostalCode(
        accounting_code="accounting_code_example",
        city_oid=1,
        dont_collect_postal_code=True,
        postal_code="postal_code_example",
        postal_code_oid=1,
        tax_rate=3.14,
        tax_rate_formatted="tax_rate_formatted_example",
    ) # TaxPostalCode | tax postal code to be updated

    # example passing only required values which don't have defaults set
    try:
        # Updates a Self tax provider postalCode
        api_response = api_instance.update_tax_provider_self_postal_code(postal_code, tax_postal_code)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_self_state**
> TaxState update_tax_provider_self_state(state_code, tax_state)

Updates a Self tax provider state

Updates a Self tax provider state. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_state import TaxState
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    state_code = "stateCode_example" # str | The state code being updated.
    tax_state = TaxState(
        accounting_code="accounting_code_example",
        counties=[
            TaxCounty(
                accounting_code="accounting_code_example",
                cities=[
                    TaxCity(
                        accounting_code="accounting_code_example",
                        city="city_example",
                        city_oid=1,
                        county_oid=1,
                        dont_collect_city=True,
                        dont_collect_postal_code=True,
                        postal_codes=[
                            TaxPostalCode(
                                accounting_code="accounting_code_example",
                                city_oid=1,
                                dont_collect_postal_code=True,
                                postal_code="postal_code_example",
                                postal_code_oid=1,
                                tax_rate=3.14,
                                tax_rate_formatted="tax_rate_formatted_example",
                            ),
                        ],
                        tax_rate=3.14,
                        tax_rate_formatted="tax_rate_formatted_example",
                    ),
                ],
                county="county_example",
                county_oid=1,
                dont_collect_city=True,
                dont_collect_county=True,
                dont_collect_postal_code=True,
                state_oid=1,
                tax_rate=3.14,
                tax_rate_formatted="tax_rate_formatted_example",
            ),
        ],
        country_oid=1,
        dont_collect_city=True,
        dont_collect_county=True,
        dont_collect_postal_code=True,
        dont_collect_state=True,
        exempt_digital_items=True,
        exempt_physical_items=True,
        exempt_service_items=True,
        state_code="state_code_example",
        state_oid=1,
        tax_gift_charge=True,
        tax_gift_wrap=True,
        tax_rate=3.14,
        tax_rate_formatted="tax_rate_formatted_example",
        tax_shipping=True,
        use_ultracart_managed_rates=True,
    ) # TaxState | tax state to be updated

    # example passing only required values which don't have defaults set
    try:
        # Updates a Self tax provider state
        api_response = api_instance.update_tax_provider_self_state(state_code, tax_state)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_sovos**
> TaxProviderSovos update_tax_provider_sovos(tax_provider_sovos)

Update the Sovos tax provider

Update the Sovos tax provider. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_provider_sovos import TaxProviderSovos
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    tax_provider_sovos = TaxProviderSovos(
        configuration=SovosConfig(
            access_key="access_key_example",
            estimate_only=True,
            last_test_dts="last_test_dts_example",
            secret_key="secret_key_example",
            send_test_orders=True,
            test_results="test_results_example",
            uat=True,
        ),
        description="description_example",
        selected=True,
        title="title_example",
    ) # TaxProviderSovos | TaxProviderSovos object

    # example passing only required values which don't have defaults set
    try:
        # Update the Sovos tax provider
        api_response = api_instance.update_tax_provider_sovos(tax_provider_sovos)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling TaxApi->update_tax_provider_sovos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_provider_sovos** | [**TaxProviderSovos**](TaxProviderSovos.md)| TaxProviderSovos object |

### Return type

[**TaxProviderSovos**](TaxProviderSovos.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_tax_jar**
> TaxProviderTaxJar update_tax_provider_tax_jar(tax_provider_tax_jar)

Update the TaxJar tax provider

Update the TaxJar tax provider. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_provider_tax_jar import TaxProviderTaxJar
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    tax_provider_tax_jar = TaxProviderTaxJar(
        configuration=TaxJarConfig(
            active=True,
            api_key="api_key_example",
            estimate_only=True,
            send_outside_nexus=True,
            send_test_orders=True,
            skip_channel_orders=True,
            use_distribution_center_from=True,
        ),
        description="description_example",
        selected=True,
        title="title_example",
    ) # TaxProviderTaxJar | TaxProviderTaxJar object

    # example passing only required values which don't have defaults set
    try:
        # Update the TaxJar tax provider
        api_response = api_instance.update_tax_provider_tax_jar(tax_provider_tax_jar)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_provider_ultra_cart**
> TaxProviderUltraCart update_tax_provider_ultra_cart(tax_provider_ultracart)

Update the UltraCart tax provider

Update the UltraCart tax provider. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import tax_api
from ultracart.model.tax_provider_ultra_cart import TaxProviderUltraCart
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    tax_provider_ultracart = TaxProviderUltraCart(
        configuration=UltraCartConfig(
            tax_billing=True,
        ),
        description="description_example",
        selected=True,
        states=[
            TaxProviderUltraCartState(
                enabled=True,
                exempt_digital_items=True,
                exempt_physical_items=True,
                exempt_service_items=True,
                state_code="state_code_example",
                state_name="state_name_example",
                tax_gift_charge=True,
                tax_gift_wrap=True,
                tax_rate_formatted="tax_rate_formatted_example",
                tax_shipping=True,
            ),
        ],
        title="title_example",
    ) # TaxProviderUltraCart | TaxProviderUltraCart object

    # example passing only required values which don't have defaults set
    try:
        # Update the UltraCart tax provider
        api_response = api_instance.update_tax_provider_ultra_cart(tax_provider_ultracart)
        pprint(api_response)
    except ultracart.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

