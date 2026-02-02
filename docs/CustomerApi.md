# ultracart.CustomerApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer_store_credit**](CustomerApi.md#add_customer_store_credit) | **POST** /customer/customers/{customer_profile_oid}/store_credit | Adds store credit to a customer
[**adjust_internal_certificate**](CustomerApi.md#adjust_internal_certificate) | **POST** /customer/customers/{customer_profile_oid}/adjust_cashback_balance | Updates the cashback balance for a customer by updating the internal gift certificate used, creating the gift certificate if needed.
[**delete_customer**](CustomerApi.md#delete_customer) | **DELETE** /customer/customers/{customer_profile_oid} | Delete a customer
[**delete_wish_list_item**](CustomerApi.md#delete_wish_list_item) | **DELETE** /customer/customers/{customer_profile_oid}/wishlist/{customer_wishlist_item_oid} | Delete a customer wishlist item
[**get_customer**](CustomerApi.md#get_customer) | **GET** /customer/customers/{customer_profile_oid} | Retrieve a customer
[**get_customer_by_email**](CustomerApi.md#get_customer_by_email) | **GET** /customer/customers/by_email/{email} | Retrieve a customer by Email
[**get_customer_editor_values**](CustomerApi.md#get_customer_editor_values) | **GET** /customer/editor_values | Retrieve values needed for a customer profile editor
[**get_customer_email_lists**](CustomerApi.md#get_customer_email_lists) | **GET** /customer/email_lists | Retrieve all email lists across all storefronts
[**get_customer_store_credit**](CustomerApi.md#get_customer_store_credit) | **GET** /customer/customers/{customer_profile_oid}/store_credit | Retrieve the customer store credit accumulated through loyalty programs
[**get_customer_wish_list**](CustomerApi.md#get_customer_wish_list) | **GET** /customer/customers/{customer_profile_oid}/wishlist | Retrieve wishlist items for customer
[**get_customer_wish_list_item**](CustomerApi.md#get_customer_wish_list_item) | **GET** /customer/customers/{customer_profile_oid}/wishlist/{customer_wishlist_item_oid} | Retrieve wishlist item for customer
[**get_customers**](CustomerApi.md#get_customers) | **GET** /customer/customers | Retrieve customers
[**get_customers_by_query**](CustomerApi.md#get_customers_by_query) | **POST** /customer/customers/query | Retrieve customers by query
[**get_customers_for_data_tables**](CustomerApi.md#get_customers_for_data_tables) | **POST** /customer/customers/dataTables | Retrieve customers for DataTables plugin
[**get_email_verification_token**](CustomerApi.md#get_email_verification_token) | **POST** /customer/customers/email_verify/get_token | Create a token that can be used to verify a customer email address
[**get_magic_link**](CustomerApi.md#get_magic_link) | **PUT** /customer/customers/{customer_profile_oid}/magic_link/{storefront_host_name} | getMagicLink
[**insert_customer**](CustomerApi.md#insert_customer) | **POST** /customer/customers | Insert a customer
[**insert_wish_list_item**](CustomerApi.md#insert_wish_list_item) | **POST** /customer/customers/{customer_profile_oid}/wishlist | Insert a customer wishlist item
[**merge_customer**](CustomerApi.md#merge_customer) | **PUT** /customer/customers/{customer_profile_oid}/merge | Merge customer into this customer
[**search_customer_profile_values**](CustomerApi.md#search_customer_profile_values) | **POST** /customer/search | Searches for all matching values (using POST)
[**search_customers**](CustomerApi.md#search_customers) | **GET** /customer/customers/search | Search for customers
[**update_customer**](CustomerApi.md#update_customer) | **PUT** /customer/customers/{customer_profile_oid} | Update a customer
[**update_customer_email_lists**](CustomerApi.md#update_customer_email_lists) | **POST** /customer/customers/{customer_profile_oid}/email_lists | Update email list subscriptions for a customer
[**update_wish_list_item**](CustomerApi.md#update_wish_list_item) | **PUT** /customer/customers/{customer_profile_oid}/wishlist/{customer_wishlist_item_oid} | Update a customer wishlist item
[**validate_email_verification_token**](CustomerApi.md#validate_email_verification_token) | **POST** /customer/customers/email_verify/validate_token | Validate a token that can be used to verify a customer email address


# **add_customer_store_credit**
> BaseResponse add_customer_store_credit(customer_profile_oid, store_credit_request)

Adds store credit to a customer

Adds store credit to a customer 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from samples import api_client
from ultracart.models import CustomerStoreCreditAddRequest

# Create the customer API instance
customer_api = CustomerApi(api_client())

# Set the email and retrieve customer
email = "test@ultracart.com"
customer = customer_api.get_customer_by_email(email).customer
customer_oid = customer.customer_profile_oid

# Create store credit request
store_credit_request = CustomerStoreCreditAddRequest(
    amount=20.00,
    description="Customer is super cool and I wanted to give them store credit.",
    expiration_days=365,  # or leave None for no expiration
    vesting_days=45  # customer has to wait 45 days to use it
)

# Add store credit
api_response = customer_api.add_customer_store_credit(customer_oid, store_credit_request)

# Check for errors
if api_response.error is not None:
    print(f"Developer Message: {api_response.error.developer_message}")
    print(f"User Message: {api_response.error.user_message}")
    exit()

# Print the success response
print(api_response.success)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid to credit. |
 **store_credit_request** | [**CustomerStoreCreditAddRequest**](CustomerStoreCreditAddRequest.md)| Store credit to add |

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **adjust_internal_certificate**
> AdjustInternalCertificateResponse adjust_internal_certificate(customer_profile_oid, adjust_internal_certificate_request)

Updates the cashback balance for a customer by updating the internal gift certificate used, creating the gift certificate if needed.

Updates the cashback balance for a customer by updating the internal gift certificate used, creating the gift certificate if needed. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from samples import api_client
from ultracart.models import AdjustInternalCertificateRequest

# Create the customer API instance
customer_api = CustomerApi(api_client())

# Set the email and retrieve customer
email = "test@ultracart.com"
customer = customer_api.get_customer_by_email(email).customer
customer_oid = customer.customer_profile_oid

# Create adjustment request
adjust_request = AdjustInternalCertificateRequest(
    description="Adjusting customer cashback balance because they called and complained about product.",
    expiration_days=365,  # expires in 365 days
    vesting_days=45,  # customer has to wait 45 days to use it
    adjustment_amount=59,  # add 59 to their balance
    order_id='DEMO-12345',  # or leave None. This ties the adjustment to a particular order
    entry_dts=None  # use current time
)

# Adjust internal certificate
api_response = customer_api.adjust_internal_certificate(customer_oid, adjust_request)

# Check for errors
if api_response.error is not None:
    print(f"Developer Message: {api_response.error.developer_message}")
    print(f"User Message: {api_response.error.user_message}")
    exit()

# Print response details
print(f"Success: {api_response.success}")
print(f"Adjustment Amount: {api_response.adjustment_amount}")
print(f"Balance Amount: {api_response.balance_amount}")

# Optional: full response inspection
print(api_response)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer profile oid |
 **adjust_internal_certificate_request** | [**AdjustInternalCertificateRequest**](AdjustInternalCertificateRequest.md)| adjustInternalCertificateRequest |

### Return type

[**AdjustInternalCertificateResponse**](AdjustInternalCertificateResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **delete_customer**
> delete_customer(customer_profile_oid)

Delete a customer

Delete a customer on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from customer_functions import insert_sample_customer, delete_sample_customer

def main():
    try:
        customer_oid = insert_sample_customer()
        delete_sample_customer(customer_oid)
    except Exception as e:
        print('An exception occurred. Please review the following error:')
        print(e)
        import sys
        sys.exit(1)

if __name__ == "__main__":
    main()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer_profile_oid to delete. |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_wish_list_item**
> delete_wish_list_item(customer_profile_oid, customer_wishlist_item_oid)

Delete a customer wishlist item

Delete a customer wishlist item 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from samples import api_client
from ultracart.models import CustomerWishListItem

from customer_functions import insert_sample_customer, delete_sample_customer
from item.item_functions import insert_sample_item_and_get_oid, delete_sample_item_by_oid

def main():
    try:
        # Create customer API instance
        customer_api = CustomerApi(api_client())

        # Create sample items
        first_item_oid = insert_sample_item_and_get_oid()
        second_item_oid = insert_sample_item_and_get_oid()

        # Create a sample customer
        customer_oid = insert_sample_customer()

        # Add first wish list item
        first_wish_item = CustomerWishListItem(
            customer_profile_oid=customer_oid,
            merchant_item_oid=first_item_oid,
            comments="I really want this for my birthday",
            priority=3  # Low priority
        )
        first_created_wish_item = customer_api.insert_wish_list_item(customer_oid, first_wish_item)

        # Add second wish list item
        second_wish_item = CustomerWishListItem(
            customer_profile_oid=customer_oid,
            merchant_item_oid=second_item_oid,
            comments="Christmas Idea!",
            priority=5  # High priority
        )
        second_created_wish_item = customer_api.insert_wish_list_item(customer_oid, second_wish_item)

        # Retrieve one wishlist item
        first_created_wish_item_copy = customer_api.get_customer_wish_list_item(
            customer_oid,
            first_created_wish_item.customer_wishlist_item_oid
        ).wishlist_item

        # Retrieve all wishlist items
        all_wish_list_items = customer_api.get_customer_wish_list(customer_oid).wishlist_items

        # Update an item
        second_created_wish_item.priority = 4
        updated_second_wish_item = customer_api.update_wish_list_item(
            customer_oid,
            second_created_wish_item.customer_wishlist_item_oid,
            second_created_wish_item
        )

        # Delete a wish list item
        customer_api.delete_wish_list_item(
            customer_oid,
            first_created_wish_item.customer_wishlist_item_oid
        )

        # Clean up
        delete_sample_customer(customer_oid)
        delete_sample_item_by_oid(first_item_oid)
        delete_sample_item_by_oid(second_item_oid)

    except Exception as e:
        print('An exception occurred. Please review the following error:')
        print(e)
        import sys
        sys.exit(1)

if __name__ == "__main__":
    main()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid for this wishlist. |
 **customer_wishlist_item_oid** | **int**| The wishlist oid for this wishlist item to delete. |

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_customer**
> CustomerResponse get_customer(customer_profile_oid)

Retrieve a customer

Retrieves a single customer using the specified customer profile oid. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from samples import api_client

from customer_functions import (
    insert_sample_customer,
    delete_sample_customer,
    create_random_email
)


def main():
    try:
        # Create a sample customer with a random email
        email = create_random_email()
        customer_oid = insert_sample_customer(email)

        # Create customer API instance
        customer_api = CustomerApi(api_client())

        # Retrieve customer by OID with expanded billing and shipping details
        # Most customer logic revolves around email, but this demonstrates
        # retrieval by customer OID
        api_response = customer_api.get_customer(customer_oid, expand="billing,shipping")
        customer = api_response.customer  # Assuming retrieval succeeded

        # Print customer details
        print(customer)

        # Clean up the sample customer
        delete_sample_customer(customer_oid)

    except Exception as e:
        print('An exception occurred. Please review the following error:')
        print(e)
        import sys
        sys.exit(1)


if __name__ == "__main__":
    main()
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

# **get_customer_by_email**
> CustomerResponse get_customer_by_email(email)

Retrieve a customer by Email

Retrieves a single customer using the specified customer email address. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from samples import api_client

from customer_functions import (
    insert_sample_customer,
    delete_sample_customer,
    create_random_email
)


def main():
    try:
        # Create a sample customer with a random email
        email = create_random_email()
        customer_oid = insert_sample_customer(email)

        # Create customer API instance
        customer_api = CustomerApi(api_client())

        # Retrieve customer by email with expanded billing and shipping details
        # Most customer logic revolves around email, not customer OID
        api_response = customer_api.get_customer_by_email(email, expand="billing,shipping")
        customer = api_response.customer  # Assuming retrieval succeeded

        # Print customer details
        print(customer)

        # Clean up the sample customer
        delete_sample_customer(customer_oid)

    except Exception as e:
        print('An exception occurred. Please review the following error:')
        print(e)
        import sys
        sys.exit(1)


if __name__ == "__main__":
    main()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address of the customer to retrieve. |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CustomerResponse**](CustomerResponse.md)

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

# **get_customer_editor_values**
> CustomerEditorValues get_customer_editor_values()

Retrieve values needed for a customer profile editor

Retrieve values needed for a customer profile editor. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# This is an internal method used by our Customer management screen.  It returns back all the static data needed
# for our dropdown lists, such as lists of state and countries.  You can call it if you like, but the data won't be
# of much use.
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerEditorValues**](CustomerEditorValues.md)

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

# **get_customer_email_lists**
> EmailListsResponse get_customer_email_lists()

Retrieve all email lists across all storefronts

Retrieve all email lists across all storefronts 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# This is an internal method used by our Email workflow engines.  It returns back all the email lists a customer
# is currently subscribed to.  It's geared towards our UI needs, so the data returned may appear cryptic.
#  We're not including a sample for it because we don't envision it being valuable to a merchant.
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**EmailListsResponse**](EmailListsResponse.md)

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

# **get_customer_store_credit**
> CustomerStoreCreditResponse get_customer_store_credit(customer_profile_oid)

Retrieve the customer store credit accumulated through loyalty programs

Retrieve the customer store credit accumulated through loyalty programs 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from ultracart.models import CustomerStoreCreditAddRequest
from ultracart.api_client import ApiException

from samples import api_client
from customer_functions import insert_sample_customer, delete_sample_customer

def add_customer_store_credit():
    try:
        # Create API instance
        customer_api = CustomerApi(api_client())

        # Create a customer
        customer_oid = insert_sample_customer()

        # First store credit addition
        add_request_1 = CustomerStoreCreditAddRequest(
            description='First credit add',
            vesting_days=10,
            expiration_days=20,  # that's not a lot of time!
            amount=20
        )
        customer_api.add_customer_store_credit(customer_oid, add_request_1)

        # Second store credit addition
        add_request_2 = CustomerStoreCreditAddRequest(
            description='Second credit add',
            vesting_days=0,  # immediately available
            expiration_days=90,
            amount=40
        )
        customer_api.add_customer_store_credit(customer_oid, add_request_2)

        # Retrieve store credit information
        api_response = customer_api.get_customer_store_credit(customer_oid)
        store_credit = api_response.customer_store_credit

        # Print store credit details
        print(store_credit)  # Using print instead of var_dump

        # Clean up the sample
        delete_sample_customer(customer_oid)

    except ApiException as e:
        print('An ApiException occurred. Please review the following error:')
        print(e)
        raise

# Run the function if the script is executed directly
if __name__ == '__main__':
    add_customer_store_credit()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid to retrieve. |

### Return type

[**CustomerStoreCreditResponse**](CustomerStoreCreditResponse.md)

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

# **get_customer_wish_list**
> CustomerWishListItemsResponse get_customer_wish_list(customer_profile_oid)

Retrieve wishlist items for customer

Retrieve wishlist items for customer. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from samples import api_client
from ultracart.models import CustomerWishListItem

from customer_functions import insert_sample_customer, delete_sample_customer
from item.item_functions import insert_sample_item_and_get_oid, delete_sample_item_by_oid

def main():
    try:
        # Create customer API instance
        customer_api = CustomerApi(api_client())

        # Create sample items
        first_item_oid = insert_sample_item_and_get_oid()
        second_item_oid = insert_sample_item_and_get_oid()

        # Create a sample customer
        customer_oid = insert_sample_customer()

        # Add first wish list item
        first_wish_item = CustomerWishListItem(
            customer_profile_oid=customer_oid,
            merchant_item_oid=first_item_oid,
            comments="I really want this for my birthday",
            priority=3  # Low priority
        )
        first_created_wish_item = customer_api.insert_wish_list_item(customer_oid, first_wish_item)

        # Add second wish list item
        second_wish_item = CustomerWishListItem(
            customer_profile_oid=customer_oid,
            merchant_item_oid=second_item_oid,
            comments="Christmas Idea!",
            priority=5  # High priority
        )
        second_created_wish_item = customer_api.insert_wish_list_item(customer_oid, second_wish_item)

        # Retrieve one wishlist item
        first_created_wish_item_copy = customer_api.get_customer_wish_list_item(
            customer_oid,
            first_created_wish_item.customer_wishlist_item_oid
        ).wishlist_item

        # Retrieve all wishlist items
        all_wish_list_items = customer_api.get_customer_wish_list(customer_oid).wishlist_items

        # Update an item
        second_created_wish_item.priority = 4
        updated_second_wish_item = customer_api.update_wish_list_item(
            customer_oid,
            second_created_wish_item.customer_wishlist_item_oid,
            second_created_wish_item
        )

        # Delete a wish list item
        customer_api.delete_wish_list_item(
            customer_oid,
            first_created_wish_item.customer_wishlist_item_oid
        )

        # Clean up
        delete_sample_customer(customer_oid)
        delete_sample_item_by_oid(first_item_oid)
        delete_sample_item_by_oid(second_item_oid)

    except Exception as e:
        print('An exception occurred. Please review the following error:')
        print(e)
        import sys
        sys.exit(1)

if __name__ == "__main__":
    main()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid for this wishlist. |

### Return type

[**CustomerWishListItemsResponse**](CustomerWishListItemsResponse.md)

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

# **get_customer_wish_list_item**
> CustomerWishListItemResponse get_customer_wish_list_item(customer_profile_oid, customer_wishlist_item_oid)

Retrieve wishlist item for customer

Retrieve wishlist item for customer. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from samples import api_client
from ultracart.models import CustomerWishListItem

from customer_functions import insert_sample_customer, delete_sample_customer
from item.item_functions import insert_sample_item_and_get_oid, delete_sample_item_by_oid

def main():
    try:
        # Create customer API instance
        customer_api = CustomerApi(api_client())

        # Create sample items
        first_item_oid = insert_sample_item_and_get_oid()
        second_item_oid = insert_sample_item_and_get_oid()

        # Create a sample customer
        customer_oid = insert_sample_customer()

        # Add first wish list item
        first_wish_item = CustomerWishListItem(
            customer_profile_oid=customer_oid,
            merchant_item_oid=first_item_oid,
            comments="I really want this for my birthday",
            priority=3  # Low priority
        )
        first_created_wish_item = customer_api.insert_wish_list_item(customer_oid, first_wish_item)

        # Add second wish list item
        second_wish_item = CustomerWishListItem(
            customer_profile_oid=customer_oid,
            merchant_item_oid=second_item_oid,
            comments="Christmas Idea!",
            priority=5  # High priority
        )
        second_created_wish_item = customer_api.insert_wish_list_item(customer_oid, second_wish_item)

        # Retrieve one wishlist item
        first_created_wish_item_copy = customer_api.get_customer_wish_list_item(
            customer_oid,
            first_created_wish_item.customer_wishlist_item_oid
        ).wishlist_item

        # Retrieve all wishlist items
        all_wish_list_items = customer_api.get_customer_wish_list(customer_oid).wishlist_items

        # Update an item
        second_created_wish_item.priority = 4
        updated_second_wish_item = customer_api.update_wish_list_item(
            customer_oid,
            second_created_wish_item.customer_wishlist_item_oid,
            second_created_wish_item
        )

        # Delete a wish list item
        customer_api.delete_wish_list_item(
            customer_oid,
            first_created_wish_item.customer_wishlist_item_oid
        )

        # Clean up
        delete_sample_customer(customer_oid)
        delete_sample_item_by_oid(first_item_oid)
        delete_sample_item_by_oid(second_item_oid)

    except Exception as e:
        print('An exception occurred. Please review the following error:')
        print(e)
        import sys
        sys.exit(1)

if __name__ == "__main__":
    main()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid for this wishlist. |
 **customer_wishlist_item_oid** | **int**| The wishlist oid for this wishlist item. |

### Return type

[**CustomerWishListItemResponse**](CustomerWishListItemResponse.md)

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

# **get_customers**
> CustomersResponse get_customers()

Retrieve customers

Retrieves customers from the account.  If no parameters are specified, all customers will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
from typing import List, Optional
from ultracart.apis import CustomerApi
from ultracart.api_client import ApiException

from samples import api_client


def get_customer_chunk(
        customer_api: CustomerApi,
        offset: int,
        limit: int
) -> List[dict]:
    """
    Retrieve a chunk of customers with specified expansion and pagination.

    Possible expansion values include:
    attachments, billing, cards, cc_emails, loyalty, orders_summary,
    pricing_tiers, privacy, properties, quotes_summary, reviewer,
    shipping, software_entitlements, tags, tax_codes
    """
    # Just the address fields. Contact support if unsure.
    expand = "shipping,billing"

    # Set all search parameters to None
    search_params = {
        'email': None,
        'qb_class': None,
        'quickbooks_code': None,
        'last_modified_dts_start': None,
        'last_modified_dts_end': None,
        'signup_dts_start': None,
        'signup_dts_end': None,
        'billing_first_name': None,
        'billing_last_name': None,
        'billing_company': None,
        'billing_city': None,
        'billing_state': None,
        'billing_postal_code': None,
        'billing_country_code': None,
        'billing_day_phone': None,
        'billing_evening_phone': None,
        'shipping_first_name': None,
        'shipping_last_name': None,
        'shipping_company': None,
        'shipping_city': None,
        'shipping_state': None,
        'shipping_postal_code': None,
        'shipping_country_code': None,
        'shipping_day_phone': None,
        'shipping_evening_phone': None,
        'pricing_tier_oid': None,
        'pricing_tier_name': None,
        'limit': limit,
        'offset': offset,
        'since': None,
        'sort': None,
        'expand': expand
    }

    # Remove keys with None values to match UltraCart API expectations
    filtered_params = {k: v for k, v in search_params.items() if v is not None}

    # Retrieve customer chunk
    api_response = customer_api.get_customers(**filtered_params)

    # Return customers or empty list
    return api_response.customers or []


def retrieve_all_customers():
    """
    Retrieve all customers using pagination.

    Note: TODO - Consider using getCustomersByQuery for easier retrieval.
    """
    # Initialize parameters
    customers = []
    iteration = 1
    offset = 0
    limit = 200
    more_records_to_fetch = True

    try:
        # Create API client
        customer_api = CustomerApi(api_client())

        # Pagination loop
        while more_records_to_fetch:
            print(f"executing iteration {iteration}")

            # Fetch customer chunk
            chunk_of_customers = get_customer_chunk(customer_api, offset, limit)

            # Merge customers
            customers.extend(chunk_of_customers)

            # Update pagination parameters
            offset += limit
            more_records_to_fetch = len(chunk_of_customers) == limit
            iteration += 1

    except ApiException as e:
        print(f'ApiException occurred on iteration {iteration}')
        print(e)
        raise

    # Return or print customers
    return customers


# Run the retrieval if script is executed directly
if __name__ == '__main__':
    try:
        # Simulate PHP's set_time_limit and ini_set
        # Note: In Python, these are typically handled differently depending on the environment
        # This is just a rough approximation
        start_time = time.time()
        max_execution_time = 3000  # 50 minutes

        all_customers = retrieve_all_customers()

        # Print or process customers
        print(f"Total customers retrieved: {len(all_customers)}")
        # Uncomment the following line to print full details (can be very verbose)
        # print(all_customers)

    except Exception as e:
        print("An error occurred:")
        print(e)
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
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **since** | **str**| Fetch customers that have been created/modified since this date/time. | [optional]
 **sort** | **str**| The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CustomersResponse**](CustomersResponse.md)

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

# **get_customers_by_query**
> CustomersResponse get_customers_by_query(customer_query)

Retrieve customers by query

Retrieves customers from the account.  If no parameters are specified, all customers will be returned.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
from typing import List, Optional
from ultracart.apis import CustomerApi
from ultracart.models import CustomerQuery
from ultracart.api_client import ApiException

from samples import api_client


def get_customer_chunk(
        customer_api: CustomerApi,
        offset: int,
        limit: int
) -> List[dict]:
    """
    Retrieve a chunk of customers using query method.

    Possible expansion values include:
    attachments, billing, cards, cc_emails, loyalty, orders_summary,
    pricing_tiers, privacy, properties, quotes_summary, reviewer,
    shipping, software_entitlements, tags, tax_codes
    """
    # Just the address fields. Contact support if unsure.
    expand = "shipping,billing"

    # Create a query object (currently with no filters)
    query = CustomerQuery()

    # Optional sorting
    sort = "email"
    since = None

    # Retrieve customer chunk
    api_response = customer_api.get_customers_by_query(
        query,
        offset,
        limit,
        since=since,
        sort=sort,
        expand=expand
    )

    # Return customers or empty list
    return api_response.customers or []


def retrieve_all_customers():
    """
    Retrieve all customers using pagination with query method.
    """
    # Initialize parameters
    customers = []
    iteration = 1
    offset = 0
    limit = 200
    more_records_to_fetch = True

    try:
        # Create API client
        customer_api = CustomerApi(api_client())

        # Pagination loop
        while more_records_to_fetch:
            print(f"executing iteration {iteration}")

            # Fetch customer chunk
            chunk_of_customers = get_customer_chunk(customer_api, offset, limit)

            # Extend customers list
            customers.extend(chunk_of_customers)

            # Update pagination parameters
            offset += limit
            more_records_to_fetch = len(chunk_of_customers) == limit
            iteration += 1

    except ApiException as e:
        print(f'ApiException occurred on iteration {iteration}')
        print(e)
        raise

    # Return or print customers
    return customers


# Run the retrieval if script is executed directly
if __name__ == '__main__':
    try:
        # Simulate PHP's set_time_limit and ini_set
        # Note: In Python, these are typically handled differently depending on the environment
        start_time = time.time()
        max_execution_time = 3000  # 50 minutes

        all_customers = retrieve_all_customers()

        # Print or process customers
        print(f"Total customers retrieved: {len(all_customers)}")
        # Uncomment the following line to print full details (can be very verbose)
        # print(all_customers)

    except Exception as e:
        print("An error occurred:")
        print(e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_query** | [**CustomerQuery**](CustomerQuery.md)| Customer query |
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
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

# **get_customers_for_data_tables**
> DataTablesServerSideResponse get_customers_for_data_tables()

Retrieve customers for DataTables plugin

Retrieves customers from the account.  If no searches are specified, all customers will be returned. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# This is an internal method used by our Customer management screen.  It won't be of much use to you, so we're
# not including a sample.  getCustomer, getCustomerByEmail, getCustomers and getCustomersByQuery are more useful
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

# **get_email_verification_token**
> EmailVerifyTokenResponse get_email_verification_token(token_request)

Create a token that can be used to verify a customer email address

Create a token that can be used to verify a customer email address.  The implementation of how a customer interacts with this token is left to the merchant. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from ultracart.models import EmailVerifyTokenRequest, EmailVerifyTokenValidateRequest

from samples import api_client


def email_verification_demo():
    """
    Demonstrates the email verification token process:
    1. Get an email verification token
    2. Validate the token

    In a real-world scenario, you would:
    - Email the token to the customer
    - Have the customer enter the token back into your system
    """
    # Create API client
    customer_api = CustomerApi(api_client())

    # Email and password for verification
    email = "test@ultracart.com"
    password = "squirrel"

    # Create token request
    token_request = EmailVerifyTokenRequest(
        email=email,
        password=password
    )

    try:
        # Get email verification token
        token_response = customer_api.get_email_verification_token(token_request)
        token = token_response.token

        # TODO: In a real application, email this token to the customer

        # Verify the token
        verify_request = EmailVerifyTokenValidateRequest(
            token=token
        )
        verify_response = customer_api.validate_email_verification_token(verify_request)

        # Print verification result
        print(f'Was the correct token provided? {verify_response.success}')

    except Exception as e:
        print("An error occurred during email verification:")
        print(e)


# Run the demo if script is executed directly
if __name__ == '__main__':
    email_verification_demo()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**EmailVerifyTokenRequest**](EmailVerifyTokenRequest.md)| Token request |

### Return type

[**EmailVerifyTokenResponse**](EmailVerifyTokenResponse.md)

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

# **get_magic_link**
> CustomerMagicLinkResponse get_magic_link(customer_profile_oid, storefront_host_name)

getMagicLink

Retrieves a magic link to allow a merchant to login as a customer.  This method is a PUT call intentionally. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import json
from ultracart.apis import CustomerApi
from samples import api_client

from customer_functions import insert_sample_customer


def main():
    try:
        # Create customer API instance
        customer_api = CustomerApi(api_client())

        # Create a sample customer
        customer_oid = insert_sample_customer()

        # Set storefront (required)
        storefront = "www.website.com"

        # Get magic link
        api_response = customer_api.get_magic_link(customer_oid, storefront)
        url = api_response.url

        # In a web application (like Flask), you would redirect to the URL
        # For this example, we'll just print the URL
        print(f"Magic Link URL: {url}")

        # Note: In a real web application, you would use a proper redirect
        # For example, in Flask:
        # return redirect(url)

        # Clean up note: Do not delete the customer if you want the magic link to work
        # deleteSampleCustomer(customer_oid)

    except Exception as e:
        print('An exception occurred. Please review the following error:')
        print(e)
        import sys
        sys.exit(1)


if __name__ == "__main__":
    main()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer_profile_oid of the customer. |
 **storefront_host_name** | **str**| The storefront to log into. |

### Return type

[**CustomerMagicLinkResponse**](CustomerMagicLinkResponse.md)

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

# **insert_customer**
> CustomerResponse insert_customer(customer)

Insert a customer

Insert a customer on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.api_client import ApiException

from customer_functions import insert_sample_customer, delete_sample_customer


def create_and_delete_customer():
    """
    Demonstrate creating and immediately deleting a sample customer.
    """
    try:
        # Insert a sample customer
        customer_oid = insert_sample_customer()

        # Delete the sample customer
        delete_sample_customer(customer_oid)

    except ApiException as e:
        print('An ApiException occurred. Please review the following error:')
        print(e)
        raise


# Run the function if the script is executed directly
if __name__ == '__main__':
    create_and_delete_customer()
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

# **insert_wish_list_item**
> CustomerWishListItem insert_wish_list_item(customer_profile_oid, wishlist_item)

Insert a customer wishlist item

Insert a customer wishlist item 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from samples import api_client
from ultracart.models import CustomerWishListItem

from customer_functions import insert_sample_customer, delete_sample_customer
from item.item_functions import insert_sample_item_and_get_oid, delete_sample_item_by_oid

def main():
    try:
        # Create customer API instance
        customer_api = CustomerApi(api_client())

        # Create sample items
        first_item_oid = insert_sample_item_and_get_oid()
        second_item_oid = insert_sample_item_and_get_oid()

        # Create a sample customer
        customer_oid = insert_sample_customer()

        # Add first wish list item
        first_wish_item = CustomerWishListItem(
            customer_profile_oid=customer_oid,
            merchant_item_oid=first_item_oid,
            comments="I really want this for my birthday",
            priority=3  # Low priority
        )
        first_created_wish_item = customer_api.insert_wish_list_item(customer_oid, first_wish_item)

        # Add second wish list item
        second_wish_item = CustomerWishListItem(
            customer_profile_oid=customer_oid,
            merchant_item_oid=second_item_oid,
            comments="Christmas Idea!",
            priority=5  # High priority
        )
        second_created_wish_item = customer_api.insert_wish_list_item(customer_oid, second_wish_item)

        # Retrieve one wishlist item
        first_created_wish_item_copy = customer_api.get_customer_wish_list_item(
            customer_oid,
            first_created_wish_item.customer_wishlist_item_oid
        ).wishlist_item

        # Retrieve all wishlist items
        all_wish_list_items = customer_api.get_customer_wish_list(customer_oid).wishlist_items

        # Update an item
        second_created_wish_item.priority = 4
        updated_second_wish_item = customer_api.update_wish_list_item(
            customer_oid,
            second_created_wish_item.customer_wishlist_item_oid,
            second_created_wish_item
        )

        # Delete a wish list item
        customer_api.delete_wish_list_item(
            customer_oid,
            first_created_wish_item.customer_wishlist_item_oid
        )

        # Clean up
        delete_sample_customer(customer_oid)
        delete_sample_item_by_oid(first_item_oid)
        delete_sample_item_by_oid(second_item_oid)

    except Exception as e:
        print('An exception occurred. Please review the following error:')
        print(e)
        import sys
        sys.exit(1)

if __name__ == "__main__":
    main()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid for this wishlist. |
 **wishlist_item** | [**CustomerWishListItem**](CustomerWishListItem.md)| Wishlist item to insert |

### Return type

[**CustomerWishListItem**](CustomerWishListItem.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **merge_customer**
> merge_customer(customer_profile_oid, customer)

Merge customer into this customer

Merge customer into this customer. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from ultracart.models import CustomerMergeRequest
from samples import api_client

from customer_functions import (
    insert_sample_customer,
    delete_sample_customer,
    create_random_email
)

def main():
    try:
        # Create first customer
        first_customer_oid = insert_sample_customer()

        # Create second customer with a different email
        second_email = create_random_email()
        second_customer_oid = insert_sample_customer(second_email)

        # Create merge request
        merge_request = CustomerMergeRequest(
            email=second_email
            # Alternatively, you could use:
            # customer_profile_oid=second_customer_oid
        )

        # Create customer API instance
        customer_api = CustomerApi(api_client())

        # Perform customer merge
        customer_api.merge_customer(first_customer_oid, merge_request)

        # Clean up first customer (second customer is automatically deleted by merge)
        delete_sample_customer(first_customer_oid)

    except Exception as e:
        print('An exception occurred. Please review the following error:')
        print(e)
        import sys
        sys.exit(1)

if __name__ == "__main__":
    main()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer_profile_oid to update. |
 **customer** | [**CustomerMergeRequest**](CustomerMergeRequest.md)| Customer to merge into this profile. |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

void (empty response body)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **search_customer_profile_values**
> LookupResponse search_customer_profile_values(lookup_request)

Searches for all matching values (using POST)

### Example

* Api Key Authentication (ultraCartBrowserApiKey):
* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# This is an internal method used by our Customer management screen.  It only searches customer tags and is geared
# towards our UI needs, so it's inflexible.  We're not including a sample for it because we don't envision it
# being valuable to a merchant.
# getCustomersByQuery is the merchant's search method.  It is completely full-featured and easy to use.
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookup_request** | [**LookupRequest**](LookupRequest.md)| LookupRequest |

### Return type

[**LookupResponse**](LookupResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

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

# **search_customers**
> CustomersResponse search_customers()

Search for customers

Retrieves customers from the account by matching the search value against most customer fields.  You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination.  This search also goes against the cache so updates should not be performed with these result objects.  Always re-query the individual customer profile if you are going to make updates. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):


(No example for this operation).



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**| Search | [optional]
 **signup_dts_start** | **str**| Signup date start | [optional]
 **signup_dts_end** | **str**| Signup date end | [optional]
 **limit** | **int**| The maximum number of records to return on this one API call. (Max 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **since** | **str**| Fetch customers that have been created/modified since this date/time. | [optional]
 **sort** | **str**| The sort order of the customers.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CustomersResponse**](CustomersResponse.md)

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

# **update_customer**
> CustomerResponse update_customer(customer_profile_oid, customer)

Update a customer

Update a customer on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from ultracart.api_client import ApiException

from samples import api_client
from customer_functions import insert_sample_customer, delete_sample_customer

def update_customer_example():
    """
    Demonstrate customer retrieval, update, and deletion:
    1. Insert a sample customer
    2. Retrieve customer details
    3. Update billing address
    4. Verify the update
    5. Delete the sample customer
    """
    try:
        # Insert a sample customer
        customer_oid = insert_sample_customer()

        # Create API client
        customer_api = CustomerApi(api_client())

        # Specify expansion fields (just want address fields)
        # See https://www.ultracart.com/api/#resource_customer.html for all expansion values
        expand = "billing,shipping"

        # Retrieve customer details
        customer = customer_api.get_customer(customer_oid, expand).customer

        # TODO: Modify customer details
        # Change billing address (assuming first billing entry)
        customer.billing[0].address2 = 'Apartment 101'

        # Update customer
        # Notice expand is passed to update to get back the same fields for comparison
        api_response = customer_api.update_customer(customer_oid, customer, expand)

        # Verify the update
        print(api_response.customer)

        # Clean up the sample customer
        delete_sample_customer(customer_oid)

    except ApiException as e:
        print('An ApiException occurred. Please review the following error:')
        print(e)
        raise

# Run the function if the script is executed directly
if __name__ == '__main__':
    update_customer_example()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer_profile_oid to update. |
 **customer** | [**Customer**](Customer.md)| Customer to update |
 **expand** | **str**| The object expansion to perform on the result.  See documentation for examples | [optional]

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **update_customer_email_lists**
> CustomerEmailListChanges update_customer_email_lists(customer_profile_oid, list_changes)

Update email list subscriptions for a customer

Update email list subscriptions for a customer 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
# This is an internal method used by our Email workflow engines.  It allows for updating the email lists a customer
# is currently subscribed to.  It's geared towards our UI needs, so its usage may appear cryptic.
#  We're not including a sample for it because we don't envision it being valuable to a merchant.
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer profile oid |
 **list_changes** | [**CustomerEmailListChanges**](CustomerEmailListChanges.md)| List changes |

### Return type

[**CustomerEmailListChanges**](CustomerEmailListChanges.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **update_wish_list_item**
> CustomerWishListItem update_wish_list_item(customer_profile_oid, customer_wishlist_item_oid, wishlist_item)

Update a customer wishlist item

Update a customer wishlist item 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from samples import api_client
from ultracart.models import CustomerWishListItem

from customer_functions import insert_sample_customer, delete_sample_customer
from item.item_functions import insert_sample_item_and_get_oid, delete_sample_item_by_oid

def main():
    try:
        # Create customer API instance
        customer_api = CustomerApi(api_client())

        # Create sample items
        first_item_oid = insert_sample_item_and_get_oid()
        second_item_oid = insert_sample_item_and_get_oid()

        # Create a sample customer
        customer_oid = insert_sample_customer()

        # Add first wish list item
        first_wish_item = CustomerWishListItem(
            customer_profile_oid=customer_oid,
            merchant_item_oid=first_item_oid,
            comments="I really want this for my birthday",
            priority=3  # Low priority
        )
        first_created_wish_item = customer_api.insert_wish_list_item(customer_oid, first_wish_item)

        # Add second wish list item
        second_wish_item = CustomerWishListItem(
            customer_profile_oid=customer_oid,
            merchant_item_oid=second_item_oid,
            comments="Christmas Idea!",
            priority=5  # High priority
        )
        second_created_wish_item = customer_api.insert_wish_list_item(customer_oid, second_wish_item)

        # Retrieve one wishlist item
        first_created_wish_item_copy = customer_api.get_customer_wish_list_item(
            customer_oid,
            first_created_wish_item.customer_wishlist_item_oid
        ).wishlist_item

        # Retrieve all wishlist items
        all_wish_list_items = customer_api.get_customer_wish_list(customer_oid).wishlist_items

        # Update an item
        second_created_wish_item.priority = 4
        updated_second_wish_item = customer_api.update_wish_list_item(
            customer_oid,
            second_created_wish_item.customer_wishlist_item_oid,
            second_created_wish_item
        )

        # Delete a wish list item
        customer_api.delete_wish_list_item(
            customer_oid,
            first_created_wish_item.customer_wishlist_item_oid
        )

        # Clean up
        delete_sample_customer(customer_oid)
        delete_sample_item_by_oid(first_item_oid)
        delete_sample_item_by_oid(second_item_oid)

    except Exception as e:
        print('An exception occurred. Please review the following error:')
        print(e)
        import sys
        sys.exit(1)

if __name__ == "__main__":
    main()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_profile_oid** | **int**| The customer oid for this wishlist. |
 **customer_wishlist_item_oid** | **int**| The wishlist oid for this wishlist item. |
 **wishlist_item** | [**CustomerWishListItem**](CustomerWishListItem.md)| Wishlist item to update |

### Return type

[**CustomerWishListItem**](CustomerWishListItem.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
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

# **validate_email_verification_token**
> EmailVerifyTokenValidateResponse validate_email_verification_token(validation_request)

Validate a token that can be used to verify a customer email address

Validate a token that can be used to verify a customer email address.  The implementation of how a customer interacts with this token is left to the merchant. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import CustomerApi
from ultracart.models import EmailVerifyTokenRequest, EmailVerifyTokenValidateRequest

from samples import api_client


def email_verification_demo():
    """
    Demonstrates the email verification token process:
    1. Get an email verification token
    2. Validate the token

    In a real-world scenario, you would:
    - Email the token to the customer
    - Have the customer enter the token back into your system
    """
    # Create API client
    customer_api = CustomerApi(api_client())

    # Email and password for verification
    email = "test@ultracart.com"
    password = "squirrel"

    # Create token request
    token_request = EmailVerifyTokenRequest(
        email=email,
        password=password
    )

    try:
        # Get email verification token
        token_response = customer_api.get_email_verification_token(token_request)
        token = token_response.token

        # TODO: In a real application, email this token to the customer

        # Verify the token
        verify_request = EmailVerifyTokenValidateRequest(
            token=token
        )
        verify_response = customer_api.validate_email_verification_token(verify_request)

        # Print verification result
        print(f'Was the correct token provided? {verify_response.success}')

    except Exception as e:
        print("An error occurred during email verification:")
        print(e)


# Run the demo if script is executed directly
if __name__ == '__main__':
    email_verification_demo()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_request** | [**EmailVerifyTokenValidateRequest**](EmailVerifyTokenValidateRequest.md)| Token validation request |

### Return type

[**EmailVerifyTokenValidateResponse**](EmailVerifyTokenValidateResponse.md)

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

