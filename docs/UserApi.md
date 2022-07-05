# ultracart.UserApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_group**](UserApi.md#delete_group) | **DELETE** /user/groups/{group_oid} | Delete a group
[**delete_user**](UserApi.md#delete_user) | **DELETE** /user/users/{user_id} | Delete a user
[**get_group**](UserApi.md#get_group) | **GET** /user/groups/{group_oid} | Retrieve a group
[**get_groups**](UserApi.md#get_groups) | **GET** /user/groups | Get groups
[**get_user**](UserApi.md#get_user) | **GET** /user/users/{user_id} | Retrieve a user
[**get_user_logins**](UserApi.md#get_user_logins) | **GET** /user/users/{user_id}/logins | Retrieve a user&#39;s login history
[**get_users**](UserApi.md#get_users) | **GET** /user/users | Get users
[**insert_group**](UserApi.md#insert_group) | **POST** /user/groups | Insert a group
[**insert_user**](UserApi.md#insert_user) | **POST** /user/users | Insert a user
[**update_group**](UserApi.md#update_group) | **PUT** /user/groups/{group_oid} | Update a group
[**update_user**](UserApi.md#update_user) | **PUT** /user/users/{user_id} | Update a user


# **delete_group**
> delete_group(group_oid)

Delete a group

Delete a group on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import user_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    group_oid = 1 # int | The group_oid to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a group
        api_instance.delete_group(group_oid)
    except ultracart.ApiException as e:
        print("Exception when calling UserApi->delete_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_oid** | **int**| The group_oid to delete. |

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

# **delete_user**
> delete_user(user_id)

Delete a user

Delete a user on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import user_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    user_id = 1 # int | The user_id to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete a user
        api_instance.delete_user(user_id)
    except ultracart.ApiException as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user_id to delete. |

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

# **get_group**
> get_group(group_oid)

Retrieve a group

Retrieves a single group using the specified group id. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import user_api
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    group_oid = 1 # int | The group id to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a group
        api_instance.get_group(group_oid)
    except ultracart.ApiException as e:
        print("Exception when calling UserApi->get_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_oid** | **int**| The group id to retrieve. |

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

# **get_groups**
> GroupsResponse get_groups()

Get groups

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import user_api
from ultracart.model.groups_response import GroupsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get groups
        api_response = api_instance.get_groups()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling UserApi->get_groups: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupsResponse**](GroupsResponse.md)

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

# **get_user**
> UserResponse get_user(user_id)

Retrieve a user

Retrieves a single user using the specified user id. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import user_api
from ultracart.model.error_response import ErrorResponse
from ultracart.model.user_response import UserResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    user_id = 1 # int | The user id to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a user
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user id to retrieve. |

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user_logins**
> UserLoginsResponse get_user_logins(user_id)

Retrieve a user's login history

Retrieves logins for a single user using the specified user id. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import user_api
from ultracart.model.user_logins_response import UserLoginsResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    user_id = 1 # int | The user id to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a user's login history
        api_response = api_instance.get_user_logins(user_id)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling UserApi->get_user_logins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user id to retrieve. |

### Return type

[**UserLoginsResponse**](UserLoginsResponse.md)

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

# **get_users**
> UsersResponse get_users()

Get users

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import user_api
from ultracart.model.users_response import UsersResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())


    # example, this endpoint has no required or optional parameters
    try:
        # Get users
        api_response = api_instance.get_users()
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling UserApi->get_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UsersResponse**](UsersResponse.md)

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

# **insert_group**
> GroupResponse insert_group(group)

Insert a group

Insert a group on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import user_api
from ultracart.model.group import Group
from ultracart.model.group_response import GroupResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    group = Group(
        group_oid=1,
        name="name_example",
        notifications=[
            Notification(
                can_filter_by_distribution_centers=True,
                can_include_affiliate=True,
                can_include_order=True,
                can_include_order_plain_text=True,
                distribution_center_filters=[
                    "distribution_center_filters_example",
                ],
                include_affiliate=True,
                include_order=True,
                include_order_plain_text=True,
                name="name_example",
                notification_group="notification_group_example",
                selected=True,
            ),
        ],
        permissions=[
            Permission(
                permission_group="permission_group_example",
                permission_name="permission_name_example",
                selected=True,
            ),
        ],
        users=[
            GroupUserMembership(
                email="email_example",
                full_name="full_name_example",
                login="login_example",
                member=True,
                user_id=1,
            ),
        ],
    ) # Group | Group to insert

    # example passing only required values which don't have defaults set
    try:
        # Insert a group
        api_response = api_instance.insert_group(group)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling UserApi->insert_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | [**Group**](Group.md)| Group to insert |

### Return type

[**GroupResponse**](GroupResponse.md)

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

# **insert_user**
> UserResponse insert_user(user)

Insert a user

Insert a user on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import user_api
from ultracart.model.user import User
from ultracart.model.error_response import ErrorResponse
from ultracart.model.user_response import UserResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    user = User(
        api_ip_address_masks=[
            "api_ip_address_masks_example",
        ],
        change_ftp_password_to="change_ftp_password_to_example",
        change_password_to="change_password_to_example",
        email="email_example",
        full_name="full_name_example",
        groups=[
            UserGroupMembership(
                group_oid=1,
                member=True,
                name="name_example",
            ),
        ],
        linked_accounts=[
            LinkedAccount(
                company="company_example",
                merchant_id="merchant_id_example",
                selected=True,
            ),
        ],
        login="login_example",
        login_histories=[
            UserLogin(
                ip_address="ip_address_example",
                login="login_example",
                login_dts="login_dts_example",
                user_agent="user_agent_example",
            ),
        ],
        notifications=[
            Notification(
                can_filter_by_distribution_centers=True,
                can_include_affiliate=True,
                can_include_order=True,
                can_include_order_plain_text=True,
                distribution_center_filters=[
                    "distribution_center_filters_example",
                ],
                include_affiliate=True,
                include_order=True,
                include_order_plain_text=True,
                name="name_example",
                notification_group="notification_group_example",
                selected=True,
            ),
        ],
        otp_serial_number="otp_serial_number_example",
        permissions=[
            Permission(
                permission_group="permission_group_example",
                permission_name="permission_name_example",
                selected=True,
            ),
        ],
        phone="phone_example",
        user_id=1,
    ) # User | User to insert

    # example passing only required values which don't have defaults set
    try:
        # Insert a user
        api_response = api_instance.insert_user(user)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling UserApi->insert_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| User to insert |

### Return type

[**UserResponse**](UserResponse.md)

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

# **update_group**
> GroupResponse update_group(group_oid, group)

Update a group

Update a group on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import user_api
from ultracart.model.group import Group
from ultracart.model.group_response import GroupResponse
from ultracart.model.error_response import ErrorResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    group_oid = 1 # int | The group_oid to update.
    group = Group(
        group_oid=1,
        name="name_example",
        notifications=[
            Notification(
                can_filter_by_distribution_centers=True,
                can_include_affiliate=True,
                can_include_order=True,
                can_include_order_plain_text=True,
                distribution_center_filters=[
                    "distribution_center_filters_example",
                ],
                include_affiliate=True,
                include_order=True,
                include_order_plain_text=True,
                name="name_example",
                notification_group="notification_group_example",
                selected=True,
            ),
        ],
        permissions=[
            Permission(
                permission_group="permission_group_example",
                permission_name="permission_name_example",
                selected=True,
            ),
        ],
        users=[
            GroupUserMembership(
                email="email_example",
                full_name="full_name_example",
                login="login_example",
                member=True,
                user_id=1,
            ),
        ],
    ) # Group | Group to update

    # example passing only required values which don't have defaults set
    try:
        # Update a group
        api_response = api_instance.update_group(group_oid, group)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling UserApi->update_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_oid** | **int**| The group_oid to update. |
 **group** | [**Group**](Group.md)| Group to update |

### Return type

[**GroupResponse**](GroupResponse.md)

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

# **update_user**
> UserResponse update_user(user_id, user)

Update a user

Update a user on the UltraCart account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
import time
import ultracart
from ultracart.api import user_api
from ultracart.model.user import User
from ultracart.model.error_response import ErrorResponse
from ultracart.model.user_response import UserResponse
from samples import api_client  # https://github.com/UltraCart/sdk_samples/blob/master/python/samples.py
from pprint import pprint

# This example is based on our samples_sdk project, but still contains auto-generated content from our sdk generators.
# As such, this might not be the best way to use this object.
# Please see https://github.com/UltraCart/sdk_samples for working examples.

api_instance = GiftCertificateApi(api_client())

    user_id = 1 # int | The user_id to update.
    user = User(
        api_ip_address_masks=[
            "api_ip_address_masks_example",
        ],
        change_ftp_password_to="change_ftp_password_to_example",
        change_password_to="change_password_to_example",
        email="email_example",
        full_name="full_name_example",
        groups=[
            UserGroupMembership(
                group_oid=1,
                member=True,
                name="name_example",
            ),
        ],
        linked_accounts=[
            LinkedAccount(
                company="company_example",
                merchant_id="merchant_id_example",
                selected=True,
            ),
        ],
        login="login_example",
        login_histories=[
            UserLogin(
                ip_address="ip_address_example",
                login="login_example",
                login_dts="login_dts_example",
                user_agent="user_agent_example",
            ),
        ],
        notifications=[
            Notification(
                can_filter_by_distribution_centers=True,
                can_include_affiliate=True,
                can_include_order=True,
                can_include_order_plain_text=True,
                distribution_center_filters=[
                    "distribution_center_filters_example",
                ],
                include_affiliate=True,
                include_order=True,
                include_order_plain_text=True,
                name="name_example",
                notification_group="notification_group_example",
                selected=True,
            ),
        ],
        otp_serial_number="otp_serial_number_example",
        permissions=[
            Permission(
                permission_group="permission_group_example",
                permission_name="permission_name_example",
                selected=True,
            ),
        ],
        phone="phone_example",
        user_id=1,
    ) # User | User to update

    # example passing only required values which don't have defaults set
    try:
        # Update a user
        api_response = api_instance.update_user(user_id, user)
        pprint(api_response)
    except ultracart.ApiException as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user_id to update. |
 **user** | [**User**](User.md)| User to update |

### Return type

[**UserResponse**](UserResponse.md)

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

