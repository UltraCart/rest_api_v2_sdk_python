# ultracart.FraudApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decline_email**](FraudApi.md#decline_email) | **POST** /fraud/decline_email | Decline email during checkout fraud review
[**delete_fraud_rule**](FraudApi.md#delete_fraud_rule) | **DELETE** /fraud/rules/{fraud_rule_oid} | Delete a fraud rule
[**establish_fraud_rules_from_order**](FraudApi.md#establish_fraud_rules_from_order) | **POST** /fraud/rules/from_order | Establish fraud rules from an order
[**get_fraud_lookup_values**](FraudApi.md#get_fraud_lookup_values) | **GET** /fraud/lookup_values | Retrieve fraud rule lookup values
[**insert_fraud_rule**](FraudApi.md#insert_fraud_rule) | **POST** /fraud/rules | Insert a fraud rule
[**search_fraud_rules**](FraudApi.md#search_fraud_rules) | **POST** /fraud/rules/search | Search fraud rules


# **decline_email**
> decline_email(fraud_decline_emails_request)

Decline email during checkout fraud review

Adds one email address to the fraud decline list for this merchant account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import FraudApi
from ultracart.models import FraudDeclineEmailRequest
from samples import api_client


# decline_email is a shortcut for telling UltraCart to decline orders from a specific email
# address. It is the quick alternative to building a full "address email" fraud rule by hand.

def decline_email():
    fraud_api = FraudApi(api_client())

    decline_request = FraudDeclineEmailRequest()
    decline_request.email = 'chargeback-charlie@example.com'

    fraud_api.decline_email(decline_request)

    print(f"Declined email: {decline_request.email}")


if __name__ == "__main__":
    decline_email()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fraud_decline_emails_request** | [**FraudDeclineEmailRequest**](FraudDeclineEmailRequest.md)| Fraud decline emails request |

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
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fraud_rule**
> delete_fraud_rule(fraud_rule_oid)

Delete a fraud rule

Deletes a fraud rule for this merchant account. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import FraudApi
from ultracart.models import FraudRuleInsertRequest
from samples import api_client


# delete_fraud_rule removes a fraud rule by its oid.
#
# To keep this sample self-contained it first inserts a throwaway rule, then deletes it using
# the oid returned from the insert. In your own code you would already have the oid of the rule
# you want to remove (for example from search_fraud_rules).

def delete_fraud_rule():
    fraud_api = FraudApi(api_client())

    # Insert a rule so we have something to delete.
    rule = FraudRuleInsertRequest()
    rule.rule_type = 'credit card single transaction exceeds'
    rule.amount_threshold = 2500.00
    rule.failure_action = 'Flag For Review'
    rule.auto_note = 'Temporary rule created by the delete_fraud_rule sample'

    insert_response = fraud_api.insert_fraud_rule(rule)
    fraud_rule_oid = insert_response.fraud_rule.fraud_rule_oid
    print(f"Inserted temporary rule, oid = {fraud_rule_oid}")

    # Now delete it.
    fraud_api.delete_fraud_rule(fraud_rule_oid)
    print(f"Deleted fraud rule oid = {fraud_rule_oid}")


if __name__ == "__main__":
    delete_fraud_rule()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fraud_rule_oid** | **int**|  |

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
**204** | No Content |  -  |
**400** | Status Code 400: bad request input such as invalid json |  * UC-REST-ERROR - Contains human readable error message <br>  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **establish_fraud_rules_from_order**
> FraudRulesResponse establish_fraud_rules_from_order(fraud_rule_from_order_request)

Establish fraud rules from an order

Creates one or more fraud rules for this merchant account derived from an existing order, mirroring the 'establish fraud filter' action in the order processing screen. Select which filters to establish; all values are taken from the order. The IP rule is created against the order's /24 subnet (last octet masked). The credit card filter duplicates the order's stored card vault token, so no card number is sent through the API. Filters whose order data is missing (no stored card, no email, no usable IP, or no numeric street) are skipped and reported in the warning slot rather than failing the request. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import FraudApi
from ultracart.models import FraudRuleFromOrderRequest
from samples import api_client


# establish_fraud_rules_from_order is a shortcut that derives fraud rules from an existing order.
# Point it at an order you have identified as fraudulent and tell it which attributes of that
# order to turn into rules: the email, the credit card, the ip address, and/or the address.
# It creates the matching rules and returns them. This is the fast way to "block everything
# associated with this bad order" instead of building each rule by hand.
#
# Not every filter produces a rule; the order must actually have that attribute. For example an
# order with no stored card data will not produce a credit card rule.

def establish_fraud_rules_from_order():
    fraud_api = FraudApi(api_client())

    request = FraudRuleFromOrderRequest()
    request.order_id = 'DEMO-0009104434'
    request.establish_email_filter = True
    request.establish_card_filter = True
    request.establish_ip_filter = True
    request.establish_address_filter = True
    request.failure_action = 'Flag For Review'
    request.auto_note = 'Established from fraudulent order DEMO-0009104434'

    api_response = fraud_api.establish_fraud_rules_from_order(request)

    fraud_rules = api_response.fraud_rules
    print(f"Established {len(fraud_rules)} rule(s) from the order:")
    for fraud_rule in fraud_rules:
        rule = fraud_rule.to_dict()
        print(f"  oid {rule.get('fraud_rule_oid')} - {rule.get('rule_type')} - {rule.get('auto_note', '')}")


if __name__ == "__main__":
    establish_fraud_rules_from_order()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fraud_rule_from_order_request** | [**FraudRuleFromOrderRequest**](FraudRuleFromOrderRequest.md)| Fraud rule from order request |

### Return type

[**FraudRulesResponse**](FraudRulesResponse.md)

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

# **get_fraud_lookup_values**
> FraudLookupValuesResponse get_fraud_lookup_values()

Retrieve fraud rule lookup values

Returns the dropdown values required to build valid fraud rule insert and search requests. Includes rule types, failure actions, user actions, IP range types, AVS match types, the merchant's rotating transaction gateways, screen branding themes, countries, and affiliates. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import FraudApi
from samples import api_client


# get_fraud_lookup_values returns the lookup values used when building fraud rules:
# the allowed countries, affiliates, ip range types, rule groups, and rule types.
# Call this first when constructing a rule so you supply valid values.

def get_fraud_lookup_values():
    fraud_api = FraudApi(api_client())

    api_response = fraud_api.get_fraud_lookup_values()
    lookup_values = api_response.fraud_lookup_values

    print("Rule types:")
    print(lookup_values.rule_types)

    print("Rule groups:")
    print(lookup_values.rule_groups)

    print("IP range types:")
    print(lookup_values.ip_range_types)

    print("Countries:")
    print(lookup_values.countries)


if __name__ == "__main__":
    get_fraud_lookup_values()
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**FraudLookupValuesResponse**](FraudLookupValuesResponse.md)

### Authorization

[ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Status Code 401: invalid credentials supplied |  * UC-REST-ERROR - Contains human readable error message <br>  |
**410** | Status Code 410: Your authorized application has been disabled by UltraCart |  * UC-REST-ERROR - Contains human readable error message <br>  |
**429** | Status Code 429: you have exceeded the allowed API call rate limit for your application. |  * UC-REST-ERROR - Contains human readable error message <br>  |
**500** | Status Code 500: any server side error.  the body will contain a generic server error message |  * UC-REST-ERROR - Contains human readable error message <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_fraud_rule**
> FraudRuleResponse insert_fraud_rule(fraud_rule_insert_request)

Insert a fraud rule

Creates a fraud rule for this merchant account. Field names in the request body are semantic (eg amount_threshold, email, ip_address). Call GET /v2/fraud/lookup_values for the list of valid rule_type, failure_action, and related dropdown values. The 'credit card matches' rule type is not supported via REST. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import FraudApi
from ultracart.models import FraudRuleInsertRequest
from samples import api_client


# insert_fraud_rule creates a single fraud rule. Each rule has a rule_type (what it inspects),
# a failure_action (what happens when it matches), and type-specific fields such as an amount
# threshold, country code, ip address, or email.
#
# This sample has some fun and inserts several rules of different types in one run. Call
# get_fraud_lookup_values.py to see every valid rule_type and the other lookup values.

def insert_fraud_rule():
    fraud_api = FraudApi(api_client())

    rules = []

    # 1. Decline any order placed with a known-bad email address.
    rule = FraudRuleInsertRequest()
    rule.rule_type = 'address email'
    rule.email = 'chargeback-charlie@example.com'
    rule.failure_action = 'Decline Transaction'
    rule.auto_note = 'Known chargeback email - decline on sight'
    rules.append(rule)

    # 2. Flag large single credit card transactions over $1,000 for manual review.
    rule = FraudRuleInsertRequest()
    rule.rule_type = 'credit card single transaction exceeds'
    rule.amount_threshold = 1000.00
    rule.failure_action = 'Flag For Review'
    rule.auto_note = 'Large single transaction - review before shipping'
    rules.append(rule)

    # 3. Decline orders that ship outside the United States.
    rule = FraudRuleInsertRequest()
    rule.rule_type = 'address not in country'
    rule.country_code = 'US'
    rule.failure_action = 'Decline Transaction'
    rule.auto_note = 'Domestic shipping only'
    rules.append(rule)

    # 4. Decline transactions originating from a specific bad IP address.
    rule = FraudRuleInsertRequest()
    rule.rule_type = 'ip matches'
    rule.ip_address = '203.0.113.66'
    rule.ip_range_type = 'address'
    rule.failure_action = 'Decline Transaction'
    rule.auto_note = 'Blocked IP address'
    rules.append(rule)

    # 5. Flag prepaid credit cards for review.
    rule = FraudRuleInsertRequest()
    rule.rule_type = 'credit card block prepaid'
    rule.failure_action = 'Flag For Review'
    rule.auto_note = 'Prepaid card - take a closer look'
    rules.append(rule)

    # 6. Flag a customer IP making more than 10 transactions in a single day.
    rule = FraudRuleInsertRequest()
    rule.rule_type = 'ip daily transaction count exceeds'
    rule.count_threshold = 10
    rule.ip_range_type = 'address'
    rule.user_action = 'Attempted'
    rule.failure_action = 'Flag For Review'
    rule.auto_note = 'IP velocity - more than 10 orders in a day'
    rules.append(rule)

    for rule in rules:
        api_response = fraud_api.insert_fraud_rule(rule)
        created = api_response.fraud_rule
        print(f"Inserted '{rule.rule_type}' rule, oid = {created.fraud_rule_oid}")


if __name__ == "__main__":
    insert_fraud_rule()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fraud_rule_insert_request** | [**FraudRuleInsertRequest**](FraudRuleInsertRequest.md)| Fraud rule insert request |

### Return type

[**FraudRuleResponse**](FraudRuleResponse.md)

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

# **search_fraud_rules**
> FraudRulesResponse search_fraud_rules(fraud_rule_search_request)

Search fraud rules

Searches fraud rules for this merchant account using semantic filter fields. Pagination and sort are passed as query parameters (_limit, _offset, _sort). You will need to make multiple API calls in order to retrieve the entire result set since this API performs result set pagination. Results are capped at 10,000 records by ElasticSearch and the warning slot indicates when that cap was hit. Use more selective filters in that case. 

### Example

* OAuth Authentication (ultraCartOauth):
* Api Key Authentication (ultraCartSimpleApiKey):

```python
from ultracart.apis import FraudApi
from ultracart.models import FraudRuleSearchRequest
from samples import api_client


# search_fraud_rules returns the fraud rules that match the supplied criteria. Every field on the
# FraudRuleSearchRequest is optional; supply only the ones you want to filter on. Pagination and
# sort are passed as keyword arguments (limit, offset, sort).
#
# This sample searches for every rule whose action is "Decline Transaction".

def search_fraud_rules():
    fraud_api = FraudApi(api_client())

    search_request = FraudRuleSearchRequest()
    search_request.failure_action = 'Decline Transaction'

    api_response = fraud_api.search_fraud_rules(search_request, limit=200, offset=0)

    fraud_rules = api_response.fraud_rules
    print(f"Found {len(fraud_rules)} rule(s) with action 'Decline Transaction'")

    # Optional fields (such as auto_note) are not always present on a returned rule, so read
    # from to_dict() to avoid AttributeError on rules that do not have them set.
    for fraud_rule in fraud_rules:
        rule = fraud_rule.to_dict()
        print(f"  oid {rule.get('fraud_rule_oid')} - {rule.get('rule_type')} - {rule.get('auto_note', '')}")


if __name__ == "__main__":
    search_fraud_rules()
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fraud_rule_search_request** | [**FraudRuleSearchRequest**](FraudRuleSearchRequest.md)| Fraud rule search request |
 **limit** | **int**| The maximum number of records to return on this one API call. (Maximum 200) | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| Pagination of the record set.  Offset is a zero based index. | [optional] if omitted the server will use the default value of 0
 **sort** | **str**| The sort order of the fraud rules.  See Sorting documentation for examples of using multiple values and sorting by ascending and descending. | [optional]

### Return type

[**FraudRulesResponse**](FraudRulesResponse.md)

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

