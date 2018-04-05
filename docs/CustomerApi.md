# ultracart.CustomerApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_customer**](CustomerApi.md#delete_customer) | **DELETE** /customer/customers/{customer_profile_oid} | Delete a customer
[**get_customer**](CustomerApi.md#get_customer) | **GET** /customer/customers/{customer_profile_oid} | Retrieve a customer
[**get_customers**](CustomerApi.md#get_customers) | **GET** /customer/customers | Retrieve customers
[**get_customers_by_query**](CustomerApi.md#get_customers_by_query) | **GET** /customer/customers/query | Retrieve customers by query
[**get_customers_for_data_tables**](CustomerApi.md#get_customers_for_data_tables) | **POST** /customer/customers/dataTables | Retrieve customers for DataTables plugin
[**get_editor_values**](CustomerApi.md#get_editor_values) | **GET** /customer/editor_values | Retrieve values needed for a customer profile editor
[**insert_customer**](CustomerApi.md#insert_customer) | **POST** /customer/customers | Insert a customer
[**update_customer**](CustomerApi.md#update_customer) | **PUT** /customer/customers/{customer_profile_oid} | Update a customer


# **delete_customer**
> CustomerResponse delete_customer(customer_profile_oid)

Delete a customer

Delete a customer on the UltraCart account. 

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

api_instance = ultracart.CustomerApi(ultracart.ApiClient(configuration))
customer_profile_oid = 56 # int | The customer_profile_oid to delete.

try: 
    # Delete a customer
    api_response = api_instance.delete_customer(customer_profile_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->delete_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer_profile_oid to delete. | 

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer**
> CustomerResponse get_customer(customer_profile_oid, expand=expand)

Retrieve a customer

Retrieves a single customer using the specified customer profile oid. 

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

api_instance = ultracart.CustomerApi(ultracart.ApiClient(configuration))
customer_profile_oid = 56 # int | The customer oid to retrieve.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve a customer
    api_response = api_instance.get_customer(customer_profile_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid to retrieve. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers**
> CustomersResponse get_customers(email=email, qb_class=qb_class, quickbooks_code=quickbooks_code, last_modified_dts_start=last_modified_dts_start, last_modified_dts_end=last_modified_dts_end, signup_dts_start=signup_dts_start, signup_dts_end=signup_dts_end, billing_first_name=billing_first_name, billing_last_name=billing_last_name, billing_company=billing_company, billing_city=billing_city, billing_state=billing_state, billing_postal_code=billing_postal_code, billing_country_code=billing_country_code, billing_day_phone=billing_day_phone, billing_evening_phone=billing_evening_phone, shipping_first_name=shipping_first_name, shipping_last_name=shipping_last_name, shipping_company=shipping_company, shipping_city=shipping_city, shipping_state=shipping_state, shipping_postal_code=shipping_postal_code, shipping_country_code=shipping_country_code, shipping_day_phone=shipping_day_phone, shipping_evening_phone=shipping_evening_phone, pricing_tier_oid=pricing_tier_oid, pricing_tier_name=pricing_tier_name, limit=limit, offset=offset, since=since, sort=sort, expand=expand)

Retrieve customers

Retrieves customers from the account.  If no parameters are specified, all customers will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

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

api_instance = ultracart.CustomerApi(ultracart.ApiClient(configuration))
email = 'email_example' # str | Email (optional)
qb_class = 'qb_class_example' # str | Quickbooks class (optional)
quickbooks_code = 'quickbooks_code_example' # str | Quickbooks code (optional)
last_modified_dts_start = 'last_modified_dts_start_example' # str | Last modified date start (optional)
last_modified_dts_end = 'last_modified_dts_end_example' # str | Last modified date end (optional)
signup_dts_start = 'signup_dts_start_example' # str | Signup date start (optional)
signup_dts_end = 'signup_dts_end_example' # str | Signup date end (optional)
billing_first_name = 'billing_first_name_example' # str | Billing first name (optional)
billing_last_name = 'billing_last_name_example' # str | Billing last name (optional)
billing_company = 'billing_company_example' # str | Billing company (optional)
billing_city = 'billing_city_example' # str | Billing city (optional)
billing_state = 'billing_state_example' # str | Billing state (optional)
billing_postal_code = 'billing_postal_code_example' # str | Billing postal code (optional)
billing_country_code = 'billing_country_code_example' # str | Billing country code (optional)
billing_day_phone = 'billing_day_phone_example' # str | Billing day phone (optional)
billing_evening_phone = 'billing_evening_phone_example' # str | Billing evening phone (optional)
shipping_first_name = 'shipping_first_name_example' # str | Shipping first name (optional)
shipping_last_name = 'shipping_last_name_example' # str | Shipping last name (optional)
shipping_company = 'shipping_company_example' # str | Shipping company (optional)
shipping_city = 'shipping_city_example' # str | Shipping city (optional)
shipping_state = 'shipping_state_example' # str | Shipping state (optional)
shipping_postal_code = 'shipping_postal_code_example' # str | Shipping postal code (optional)
shipping_country_code = 'shipping_country_code_example' # str | Shipping country code (optional)
shipping_day_phone = 'shipping_day_phone_example' # str | Shipping day phone (optional)
shipping_evening_phone = 'shipping_evening_phone_example' # str | Shipping evening phone (optional)
pricing_tier_oid = 56 # int | Pricing tier oid (optional)
pricing_tier_name = 'pricing_tier_name_example' # str | Pricing tier name (optional)
limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
since = 'since_example' # str | Fetch customers that have been created/modified since this date/time. (optional)
sort = 'sort_example' # str | The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve customers
    api_response = api_instance.get_customers(email=email, qb_class=qb_class, quickbooks_code=quickbooks_code, last_modified_dts_start=last_modified_dts_start, last_modified_dts_end=last_modified_dts_end, signup_dts_start=signup_dts_start, signup_dts_end=signup_dts_end, billing_first_name=billing_first_name, billing_last_name=billing_last_name, billing_company=billing_company, billing_city=billing_city, billing_state=billing_state, billing_postal_code=billing_postal_code, billing_country_code=billing_country_code, billing_day_phone=billing_day_phone, billing_evening_phone=billing_evening_phone, shipping_first_name=shipping_first_name, shipping_last_name=shipping_last_name, shipping_company=shipping_company, shipping_city=shipping_city, shipping_state=shipping_state, shipping_postal_code=shipping_postal_code, shipping_country_code=shipping_country_code, shipping_day_phone=shipping_day_phone, shipping_evening_phone=shipping_evening_phone, pricing_tier_oid=pricing_tier_oid, pricing_tier_name=pricing_tier_name, limit=limit, offset=offset, since=since, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email | [optional] 
 **qb_class** | **str**| Quickbooks class | [optional] 
 **quickbooks_code** | **str**| Quickbooks code | [optional] 
 **last_modified_dts_start** | **str**| Last modified date start | [optional] 
 **last_modified_dts_end** | **str**| Last modified date end | [optional] 
 **signup_dts_start** | **str**| Signup date start | [optional] 
 **signup_dts_end** | **str**| Signup date end | [optional] 
 **billing_first_name** | **str**| Billing first name | [optional] 
 **billing_last_name** | **str**| Billing last name | [optional] 
 **billing_company** | **str**| Billing company | [optional] 
 **billing_city** | **str**| Billing city | [optional] 
 **billing_state** | **str**| Billing state | [optional] 
 **billing_postal_code** | **str**| Billing postal code | [optional] 
 **billing_country_code** | **str**| Billing country code | [optional] 
 **billing_day_phone** | **str**| Billing day phone | [optional] 
 **billing_evening_phone** | **str**| Billing evening phone | [optional] 
 **shipping_first_name** | **str**| Shipping first name | [optional] 
 **shipping_last_name** | **str**| Shipping last name | [optional] 
 **shipping_company** | **str**| Shipping company | [optional] 
 **shipping_city** | **str**| Shipping city | [optional] 
 **shipping_state** | **str**| Shipping state | [optional] 
 **shipping_postal_code** | **str**| Shipping postal code | [optional] 
 **shipping_country_code** | **str**| Shipping country code | [optional] 
 **shipping_day_phone** | **str**| Shipping day phone | [optional] 
 **shipping_evening_phone** | **str**| Shipping evening phone | [optional] 
 **pricing_tier_oid** | **int**| Pricing tier oid | [optional] 
 **pricing_tier_name** | **str**| Pricing tier name | [optional] 
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **since** | **str**| Fetch customers that have been created/modified since this date/time. | [optional] 
 **sort** | **str**| The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CustomersResponse**](CustomersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers_by_query**
> CustomersResponse get_customers_by_query(customer_query, limit=limit, offset=offset, since=since, sort=sort, expand=expand)

Retrieve customers by query

Retrieves customers from the account.  If no parameters are specified, all customers will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

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

api_instance = ultracart.CustomerApi(ultracart.ApiClient(configuration))
customer_query = ultracart.CustomerQuery() # CustomerQuery | Customer query
limit = 100 # int | The maximum number of records to return on this one API call. (Max 200) (optional) (default to 100)
offset = 0 # int | Pagination of the record set.  Offset is a zero based index. (optional) (default to 0)
since = 'since_example' # str | Fetch customers that have been created/modified since this date/time. (optional)
sort = 'sort_example' # str | The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. (optional)
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve customers by query
    api_response = api_instance.get_customers_by_query(customer_query, limit=limit, offset=offset, since=since, sort=sort, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_customers_by_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_query** | [**CustomerQuery**](CustomerQuery.md)| Customer query | 
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] [default to 100]
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] [default to 0]
 **since** | **str**| Fetch customers that have been created/modified since this date/time. | [optional] 
 **sort** | **str**| The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional] 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CustomersResponse**](CustomersResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customers_for_data_tables**
> DataTablesServerSideResponse get_customers_for_data_tables(expand=expand)

Retrieve customers for DataTables plugin

Retrieves customers from the account.  If no searches are specified, all customers will be returned. 

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

api_instance = ultracart.CustomerApi(ultracart.ApiClient(configuration))
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Retrieve customers for DataTables plugin
    api_response = api_instance.get_customers_for_data_tables(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_customers_for_data_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**DataTablesServerSideResponse**](DataTablesServerSideResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_editor_values**
> CustomerEditorValues get_editor_values()

Retrieve values needed for a customer profile editor

Retrieve values needed for a customer profile editor. 

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

api_instance = ultracart.CustomerApi(ultracart.ApiClient(configuration))

try: 
    # Retrieve values needed for a customer profile editor
    api_response = api_instance.get_editor_values()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->get_editor_values: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerEditorValues**](CustomerEditorValues.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_customer**
> CustomerResponse insert_customer(customer, expand=expand)

Insert a customer

Insert a customer on the UltraCart account. 

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

api_instance = ultracart.CustomerApi(ultracart.ApiClient(configuration))
customer = ultracart.Customer() # Customer | Customer to insert
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Insert a customer
    api_response = api_instance.insert_customer(customer, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->insert_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | [**Customer**](Customer.md)| Customer to insert | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> CustomerResponse update_customer(customer, customer_profile_oid, expand=expand)

Update a customer

Update a customer on the UltraCart account. 

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

api_instance = ultracart.CustomerApi(ultracart.ApiClient(configuration))
customer = ultracart.Customer() # Customer | Customer to update
customer_profile_oid = 56 # int | The customer_profile_oid to update.
expand = 'expand_example' # str | The object expansion to perform on the result.  See documentation for examples (optional)

try: 
    # Update a customer
    api_response = api_instance.update_customer(customer, customer_profile_oid, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->update_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | [**Customer**](Customer.md)| Customer to update | 
 **customer_profile_oid** | **int**| The customer_profile_oid to update. | 
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional] 

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

