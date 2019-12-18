# ultracart.StorefrontApi

All URIs are relative to *https://secure.ultracart.com/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_email_list**](StorefrontApi.md#archive_email_list) | **POST** /storefront/{storefront_oid}/email/lists/{email_list_uuid}/archive | Archive email list
[**archive_email_segment**](StorefrontApi.md#archive_email_segment) | **POST** /storefront/{storefront_oid}/email/segments/{email_segment_uuid}/archive | Archive email segment
[**check_download_email_segment**](StorefrontApi.md#check_download_email_segment) | **POST** /storefront/{storefront_oid}/email/segments/{email_segment_uuid}/downloadPrepare/{email_segment_rebuild_uuid} | Check download of email segment
[**clone_email_campaign**](StorefrontApi.md#clone_email_campaign) | **POST** /storefront/{storefront_oid}/email/campaigns/{email_campaign_uuid}/clone | Clone email campaign
[**clone_email_flow**](StorefrontApi.md#clone_email_flow) | **POST** /storefront/{storefront_oid}/email/flows/{email_flow_uuid}/clone | Clone email flow
[**create_email_sending_domain**](StorefrontApi.md#create_email_sending_domain) | **POST** /storefront/email/sending_domains/{domain}/create | Create email campaign
[**delete_email_email**](StorefrontApi.md#delete_email_email) | **DELETE** /storefront/{storefront_oid}/email/emails/{commseq_email_uuid} | Delete email email
[**delete_email_list_customer**](StorefrontApi.md#delete_email_list_customer) | **DELETE** /storefront/{storefront_oid}/email/lists/{email_list_uuid}/customers/{email_customer_uuid} | Delete email list customer
[**delete_email_sending_domain**](StorefrontApi.md#delete_email_sending_domain) | **DELETE** /storefront/email/sending_domains/{domain} | delete email campaign
[**delete_experiment**](StorefrontApi.md#delete_experiment) | **DELETE** /storefront/{storefront_oid}/experiments/{storefront_experiment_oid} | Delete experiment
[**geocode_address**](StorefrontApi.md#geocode_address) | **POST** /storefront/{storefront_oid}/email/geocode | Obtain lat/long for an address
[**get_countries**](StorefrontApi.md#get_countries) | **GET** /storefront/{storefront_oid}/email/countries | Get countries
[**get_email_base_templates**](StorefrontApi.md#get_email_base_templates) | **GET** /storefront/{storefront_oid}/email/baseTemplates | Get email communication base templates
[**get_email_campaign**](StorefrontApi.md#get_email_campaign) | **GET** /storefront/{storefront_oid}/email/campaigns/{email_campaign_uuid} | Get email campaign
[**get_email_campaigns**](StorefrontApi.md#get_email_campaigns) | **GET** /storefront/{storefront_oid}/email/campaigns | Get email campaigns
[**get_email_campaigns_with_stats**](StorefrontApi.md#get_email_campaigns_with_stats) | **GET** /storefront/{storefront_oid}/email/campaignsWithStats/{stat_days} | Get email campaigns with stats
[**get_email_commseq**](StorefrontApi.md#get_email_commseq) | **GET** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid} | Get email commseq
[**get_email_commseq_email_stats**](StorefrontApi.md#get_email_commseq_email_stats) | **POST** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/emailStats | Get email communication sequence emails stats
[**get_email_commseq_stat_overall**](StorefrontApi.md#get_email_commseq_stat_overall) | **GET** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/stat | Get communication sequence stats overall
[**get_email_commseq_step_waiting**](StorefrontApi.md#get_email_commseq_step_waiting) | **POST** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid}/waiting | Get email communication sequence customers waiting at each requested step
[**get_email_commseqs**](StorefrontApi.md#get_email_commseqs) | **GET** /storefront/{storefront_oid}/email/commseqs | Get email commseqs
[**get_email_dashboard_activity**](StorefrontApi.md#get_email_dashboard_activity) | **GET** /storefront/{storefront_oid}/email/dashboard_activity | Get email dashboard activity
[**get_email_dashboard_stats**](StorefrontApi.md#get_email_dashboard_stats) | **GET** /storefront/{storefront_oid}/email/dashboard_stats | Get dashboard stats
[**get_email_email**](StorefrontApi.md#get_email_email) | **GET** /storefront/{storefront_oid}/email/emails/{commseq_email_uuid} | Get email email
[**get_email_emails**](StorefrontApi.md#get_email_emails) | **GET** /storefront/{storefront_oid}/email/emails | Get email emails
[**get_email_emails_multiple**](StorefrontApi.md#get_email_emails_multiple) | **POST** /storefront/{storefront_oid}/email/emails/multiple | Get email emails multiple
[**get_email_flow**](StorefrontApi.md#get_email_flow) | **GET** /storefront/{storefront_oid}/email/flows/{email_flow_uuid} | Get email flow
[**get_email_flows**](StorefrontApi.md#get_email_flows) | **GET** /storefront/{storefront_oid}/email/flows | Get email flows
[**get_email_list**](StorefrontApi.md#get_email_list) | **GET** /storefront/{storefront_oid}/email/lists/{email_list_uuid} | Get email list
[**get_email_list_customer_editor_url**](StorefrontApi.md#get_email_list_customer_editor_url) | **GET** /storefront/{storefront_oid}/email/lists/{email_list_uuid}/customers/{email_customer_uuid}/editor_url | Get email list customers
[**get_email_list_customers**](StorefrontApi.md#get_email_list_customers) | **GET** /storefront/{storefront_oid}/email/lists/{email_list_uuid}/customers | Get email list customers
[**get_email_lists**](StorefrontApi.md#get_email_lists) | **GET** /storefront/{storefront_oid}/email/lists | Get email lists
[**get_email_segment**](StorefrontApi.md#get_email_segment) | **GET** /storefront/{storefront_oid}/email/segments/{email_segment_uuid} | Get email segment
[**get_email_segment_customer_editor_url**](StorefrontApi.md#get_email_segment_customer_editor_url) | **GET** /storefront/{storefront_oid}/email/segments/{email_segment_uuid}/customers/{email_customer_uuid}/editor_url | Get email segment customers editor URL
[**get_email_segment_customers**](StorefrontApi.md#get_email_segment_customers) | **GET** /storefront/{storefront_oid}/email/segments/{email_segment_uuid}/customers | Get email segment customers
[**get_email_segments**](StorefrontApi.md#get_email_segments) | **GET** /storefront/{storefront_oid}/email/segments | Get email segments
[**get_email_sending_domain**](StorefrontApi.md#get_email_sending_domain) | **GET** /storefront/email/sending_domain/{domain} | Get email sending domain
[**get_email_sending_domain_status**](StorefrontApi.md#get_email_sending_domain_status) | **POST** /storefront/email/sending_domains/{domain}/status | Get email sending domain status
[**get_email_sending_domains**](StorefrontApi.md#get_email_sending_domains) | **GET** /storefront/email/sending_domains | Get email sending domains
[**get_email_template**](StorefrontApi.md#get_email_template) | **GET** /storefront/{storefront_oid}/email/templates/{email_template_oid} | Get email template
[**get_email_templates**](StorefrontApi.md#get_email_templates) | **GET** /storefront/{storefront_oid}/email/templates | Get email templates
[**get_email_third_party_providers**](StorefrontApi.md#get_email_third_party_providers) | **GET** /storefront/{storefront_oid}/email/third_party_providers | Get a list of third party email providers
[**get_experiments**](StorefrontApi.md#get_experiments) | **GET** /storefront/{storefront_oid}/experiments | Get experiments
[**get_histogram_property_names**](StorefrontApi.md#get_histogram_property_names) | **GET** /storefront/{storefront_oid}/email/histogram/property_names | Get histogram property names
[**get_histogram_property_values**](StorefrontApi.md#get_histogram_property_values) | **GET** /storefront/{storefront_oid}/email/histogram/property_values | Get histogram property values
[**import_email_third_party_provider_list**](StorefrontApi.md#import_email_third_party_provider_list) | **POST** /storefront/{storefront_oid}/email/third_party_providers/import | Import a third party provider list
[**insert_email_campaign**](StorefrontApi.md#insert_email_campaign) | **POST** /storefront/{storefront_oid}/email/campaigns | Insert email campaign
[**insert_email_commseq**](StorefrontApi.md#insert_email_commseq) | **POST** /storefront/{storefront_oid}/email/commseqs | Insert email commseq
[**insert_email_email**](StorefrontApi.md#insert_email_email) | **POST** /storefront/{storefront_oid}/email/emails | Insert email email
[**insert_email_flow**](StorefrontApi.md#insert_email_flow) | **POST** /storefront/{storefront_oid}/email/flows | Insert email flow
[**insert_email_list**](StorefrontApi.md#insert_email_list) | **POST** /storefront/{storefront_oid}/email/lists | Insert email list
[**insert_email_segment**](StorefrontApi.md#insert_email_segment) | **POST** /storefront/{storefront_oid}/email/segments | Insert email segment
[**prepare_download_email_segment**](StorefrontApi.md#prepare_download_email_segment) | **POST** /storefront/{storefront_oid}/email/segments/{email_segment_uuid}/downloadPrepare | Prepare download of email segment
[**search**](StorefrontApi.md#search) | **GET** /storefront/search | Searches for all matching values
[**search_email_list_customers**](StorefrontApi.md#search_email_list_customers) | **GET** /storefront/{storefront_oid}/email/lists/{email_list_uuid}/search | Search email list customers
[**search_email_segment_customers**](StorefrontApi.md#search_email_segment_customers) | **GET** /storefront/{storefront_oid}/email/segments/{email_segment_uuid}/search | Search email segment customers
[**start_email_campaign**](StorefrontApi.md#start_email_campaign) | **PUT** /storefront/{storefront_oid}/email/campaigns/{email_campaign_uuid}/start | Start email campaign
[**subscribe_to_email_list**](StorefrontApi.md#subscribe_to_email_list) | **POST** /storefront/{storefront_oid}/email/lists/{email_list_uuid}/subscribe | Subscribe customers to email list
[**update_email_campaign**](StorefrontApi.md#update_email_campaign) | **PUT** /storefront/{storefront_oid}/email/campaigns/{email_campaign_uuid} | Update email campaign
[**update_email_commseq**](StorefrontApi.md#update_email_commseq) | **PUT** /storefront/{storefront_oid}/email/commseqs/{commseq_uuid} | Update email commseq
[**update_email_email**](StorefrontApi.md#update_email_email) | **PUT** /storefront/{storefront_oid}/email/emails/{commseq_email_uuid} | Update email email
[**update_email_flow**](StorefrontApi.md#update_email_flow) | **PUT** /storefront/{storefront_oid}/email/flows/{email_flow_uuid} | Update email flow
[**update_email_list**](StorefrontApi.md#update_email_list) | **PUT** /storefront/{storefront_oid}/email/lists/{email_list_uuid} | Update email list
[**update_email_segment**](StorefrontApi.md#update_email_segment) | **PUT** /storefront/{storefront_oid}/email/segments/{email_segment_uuid} | Update email segment
[**update_experiment**](StorefrontApi.md#update_experiment) | **PUT** /storefront/{storefront_oid}/experiments/{storefront_experiment_oid} | Update experiment


# **archive_email_list**
> EmailListArchiveResponse archive_email_list(storefront_oid, email_list_uuid)

Archive email list

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_list_uuid = 'email_list_uuid_example' # str | null

try: 
    # Archive email list
    api_response = api_instance.archive_email_list(storefront_oid, email_list_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->archive_email_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_list_uuid** | **str**| null | 

### Return type

[**EmailListArchiveResponse**](EmailListArchiveResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_email_segment**
> EmailSegmentArchiveResponse archive_email_segment(storefront_oid, email_segment_uuid)

Archive email segment

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_segment_uuid = 'email_segment_uuid_example' # str | null

try: 
    # Archive email segment
    api_response = api_instance.archive_email_segment(storefront_oid, email_segment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->archive_email_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_segment_uuid** | **str**| null | 

### Return type

[**EmailSegmentArchiveResponse**](EmailSegmentArchiveResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_download_email_segment**
> EmailSegmentDownloadPrepareResponse check_download_email_segment(storefront_oid, email_segment_uuid, email_segment_rebuild_uuid)

Check download of email segment

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_segment_uuid = 'email_segment_uuid_example' # str | null
email_segment_rebuild_uuid = 'email_segment_rebuild_uuid_example' # str | null

try: 
    # Check download of email segment
    api_response = api_instance.check_download_email_segment(storefront_oid, email_segment_uuid, email_segment_rebuild_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->check_download_email_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_segment_uuid** | **str**| null | 
 **email_segment_rebuild_uuid** | **str**| null | 

### Return type

[**EmailSegmentDownloadPrepareResponse**](EmailSegmentDownloadPrepareResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_email_campaign**
> EmailCampaignResponse clone_email_campaign(storefront_oid, email_campaign_uuid)

Clone email campaign

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_campaign_uuid = 'email_campaign_uuid_example' # str | null

try: 
    # Clone email campaign
    api_response = api_instance.clone_email_campaign(storefront_oid, email_campaign_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->clone_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_campaign_uuid** | **str**| null | 

### Return type

[**EmailCampaignResponse**](EmailCampaignResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_email_flow**
> EmailFlowResponse clone_email_flow(storefront_oid, email_flow_uuid)

Clone email flow

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_flow_uuid = 'email_flow_uuid_example' # str | null

try: 
    # Clone email flow
    api_response = api_instance.clone_email_flow(storefront_oid, email_flow_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->clone_email_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_flow_uuid** | **str**| null | 

### Return type

[**EmailFlowResponse**](EmailFlowResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_email_sending_domain**
> EmailSendingDomainResponse create_email_sending_domain(domain)

Create email campaign

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
domain = 'domain_example' # str | null

try: 
    # Create email campaign
    api_response = api_instance.create_email_sending_domain(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->create_email_sending_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| null | 

### Return type

[**EmailSendingDomainResponse**](EmailSendingDomainResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_email**
> BaseResponse delete_email_email(storefront_oid, commseq_email_uuid)

Delete email email

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
commseq_email_uuid = 'commseq_email_uuid_example' # str | null

try: 
    # Delete email email
    api_response = api_instance.delete_email_email(storefront_oid, commseq_email_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_email_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **commseq_email_uuid** | **str**| null | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_list_customer**
> BaseResponse delete_email_list_customer(storefront_oid, email_list_uuid, email_customer_uuid)

Delete email list customer

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_list_uuid = 'email_list_uuid_example' # str | null
email_customer_uuid = 'email_customer_uuid_example' # str | null

try: 
    # Delete email list customer
    api_response = api_instance.delete_email_list_customer(storefront_oid, email_list_uuid, email_customer_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_email_list_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_list_uuid** | **str**| null | 
 **email_customer_uuid** | **str**| null | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_sending_domain**
> BaseResponse delete_email_sending_domain(domain)

delete email campaign

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
domain = 'domain_example' # str | null

try: 
    # delete email campaign
    api_response = api_instance.delete_email_sending_domain(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_email_sending_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| null | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_experiment**
> delete_experiment(storefront_oid, storefront_experiment_oid)

Delete experiment

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
storefront_experiment_oid = 56 # int | null

try: 
    # Delete experiment
    api_instance.delete_experiment(storefront_oid, storefront_experiment_oid)
except ApiException as e:
    print("Exception when calling StorefrontApi->delete_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **storefront_experiment_oid** | **int**| null | 

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geocode_address**
> GeocodeResponse geocode_address(storefront_oid, geocode_request)

Obtain lat/long for an address

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
geocode_request = ultracart.GeocodeRequest() # GeocodeRequest | geocode request

try: 
    # Obtain lat/long for an address
    api_response = api_instance.geocode_address(storefront_oid, geocode_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->geocode_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **geocode_request** | [**GeocodeRequest**](GeocodeRequest.md)| geocode request | 

### Return type

[**GeocodeResponse**](GeocodeResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries**
> CountriesResponse get_countries(storefront_oid)

Get countries

Obtain a list of all the countries 

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null

try: 
    # Get countries
    api_response = api_instance.get_countries(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_countries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_base_templates**
> EmailBaseTemplateListResponse get_email_base_templates(storefront_oid)

Get email communication base templates

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null

try: 
    # Get email communication base templates
    api_response = api_instance.get_email_base_templates(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_base_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 

### Return type

[**EmailBaseTemplateListResponse**](EmailBaseTemplateListResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaign**
> EmailCampaignResponse get_email_campaign(storefront_oid, email_campaign_uuid)

Get email campaign

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_campaign_uuid = 'email_campaign_uuid_example' # str | null

try: 
    # Get email campaign
    api_response = api_instance.get_email_campaign(storefront_oid, email_campaign_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_campaign_uuid** | **str**| null | 

### Return type

[**EmailCampaignResponse**](EmailCampaignResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaigns**
> EmailCampaignsResponse get_email_campaigns(storefront_oid)

Get email campaigns

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null

try: 
    # Get email campaigns
    api_response = api_instance.get_email_campaigns(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 

### Return type

[**EmailCampaignsResponse**](EmailCampaignsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_campaigns_with_stats**
> EmailCampaignsResponse get_email_campaigns_with_stats(storefront_oid, stat_days)

Get email campaigns with stats

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
stat_days = 'stat_days_example' # str | null

try: 
    # Get email campaigns with stats
    api_response = api_instance.get_email_campaigns_with_stats(storefront_oid, stat_days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_campaigns_with_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **stat_days** | **str**| null | 

### Return type

[**EmailCampaignsResponse**](EmailCampaignsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq**
> EmailCommseqResponse get_email_commseq(storefront_oid, commseq_uuid)

Get email commseq

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
commseq_uuid = 'commseq_uuid_example' # str | null

try: 
    # Get email commseq
    api_response = api_instance.get_email_commseq(storefront_oid, commseq_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseq: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **commseq_uuid** | **str**| null | 

### Return type

[**EmailCommseqResponse**](EmailCommseqResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_email_stats**
> EmailStatSummaryResponse get_email_commseq_email_stats(storefront_oid, commseq_uuid, stats_request)

Get email communication sequence emails stats

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
commseq_uuid = 'commseq_uuid_example' # str | null
stats_request = ultracart.EmailStatSummaryRequest() # EmailStatSummaryRequest | StatsRequest

try: 
    # Get email communication sequence emails stats
    api_response = api_instance.get_email_commseq_email_stats(storefront_oid, commseq_uuid, stats_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseq_email_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **commseq_uuid** | **str**| null | 
 **stats_request** | [**EmailStatSummaryRequest**](EmailStatSummaryRequest.md)| StatsRequest | 

### Return type

[**EmailStatSummaryResponse**](EmailStatSummaryResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_stat_overall**
> EmailCommseqStatResponse get_email_commseq_stat_overall(storefront_oid, commseq_uuid)

Get communication sequence stats overall

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
commseq_uuid = 'commseq_uuid_example' # str | null

try: 
    # Get communication sequence stats overall
    api_response = api_instance.get_email_commseq_stat_overall(storefront_oid, commseq_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseq_stat_overall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **commseq_uuid** | **str**| null | 

### Return type

[**EmailCommseqStatResponse**](EmailCommseqStatResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseq_step_waiting**
> EmailStepWaitingResponse get_email_commseq_step_waiting(storefront_oid, commseq_uuid, waiting_request)

Get email communication sequence customers waiting at each requested step

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
commseq_uuid = 'commseq_uuid_example' # str | null
waiting_request = ultracart.EmailStepWaitingRequest() # EmailStepWaitingRequest | WaitingRequest

try: 
    # Get email communication sequence customers waiting at each requested step
    api_response = api_instance.get_email_commseq_step_waiting(storefront_oid, commseq_uuid, waiting_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseq_step_waiting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **commseq_uuid** | **str**| null | 
 **waiting_request** | [**EmailStepWaitingRequest**](EmailStepWaitingRequest.md)| WaitingRequest | 

### Return type

[**EmailStepWaitingResponse**](EmailStepWaitingResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_commseqs**
> EmailCommseqsResponse get_email_commseqs(storefront_oid)

Get email commseqs

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null

try: 
    # Get email commseqs
    api_response = api_instance.get_email_commseqs(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_commseqs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 

### Return type

[**EmailCommseqsResponse**](EmailCommseqsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_dashboard_activity**
> EmailDashboardActivityResponse get_email_dashboard_activity(storefront_oid, last_records=last_records)

Get email dashboard activity

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
last_records = 56 # int | null (optional)

try: 
    # Get email dashboard activity
    api_response = api_instance.get_email_dashboard_activity(storefront_oid, last_records=last_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_dashboard_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **last_records** | **int**| null | [optional] 

### Return type

[**EmailDashboardActivityResponse**](EmailDashboardActivityResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_dashboard_stats**
> EmailDashboardStatsResponse get_email_dashboard_stats(storefront_oid, days=days)

Get dashboard stats

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
days = 56 # int | null (optional)

try: 
    # Get dashboard stats
    api_response = api_instance.get_email_dashboard_stats(storefront_oid, days=days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_dashboard_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **days** | **int**| null | [optional] 

### Return type

[**EmailDashboardStatsResponse**](EmailDashboardStatsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_email**
> EmailCommseqEmailResponse get_email_email(storefront_oid, commseq_email_uuid)

Get email email

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
commseq_email_uuid = 'commseq_email_uuid_example' # str | null

try: 
    # Get email email
    api_response = api_instance.get_email_email(storefront_oid, commseq_email_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **commseq_email_uuid** | **str**| null | 

### Return type

[**EmailCommseqEmailResponse**](EmailCommseqEmailResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_emails**
> EmailCommseqEmailsResponse get_email_emails(storefront_oid)

Get email emails

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null

try: 
    # Get email emails
    api_response = api_instance.get_email_emails(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 

### Return type

[**EmailCommseqEmailsResponse**](EmailCommseqEmailsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_emails_multiple**
> EmailCommseqEmailsResponse get_email_emails_multiple(storefront_oid, email_commseq_emails_request)

Get email emails multiple

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_commseq_emails_request = ultracart.EmailCommseqEmailsRequest() # EmailCommseqEmailsRequest | Request of email uuids

try: 
    # Get email emails multiple
    api_response = api_instance.get_email_emails_multiple(storefront_oid, email_commseq_emails_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_emails_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_commseq_emails_request** | [**EmailCommseqEmailsRequest**](EmailCommseqEmailsRequest.md)| Request of email uuids | 

### Return type

[**EmailCommseqEmailsResponse**](EmailCommseqEmailsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_flow**
> EmailFlowResponse get_email_flow(storefront_oid, email_flow_uuid)

Get email flow

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_flow_uuid = 'email_flow_uuid_example' # str | null

try: 
    # Get email flow
    api_response = api_instance.get_email_flow(storefront_oid, email_flow_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_flow_uuid** | **str**| null | 

### Return type

[**EmailFlowResponse**](EmailFlowResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_flows**
> EmailFlowsResponse get_email_flows(storefront_oid)

Get email flows

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null

try: 
    # Get email flows
    api_response = api_instance.get_email_flows(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_flows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 

### Return type

[**EmailFlowsResponse**](EmailFlowsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list**
> EmailListResponse get_email_list(storefront_oid, email_list_uuid)

Get email list

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_list_uuid = 'email_list_uuid_example' # str | null

try: 
    # Get email list
    api_response = api_instance.get_email_list(storefront_oid, email_list_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_list_uuid** | **str**| null | 

### Return type

[**EmailListResponse**](EmailListResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list_customer_editor_url**
> EmailCustomerEditorUrlResponse get_email_list_customer_editor_url(storefront_oid, email_list_uuid, email_customer_uuid)

Get email list customers

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_list_uuid = 'email_list_uuid_example' # str | null
email_customer_uuid = 'email_customer_uuid_example' # str | null

try: 
    # Get email list customers
    api_response = api_instance.get_email_list_customer_editor_url(storefront_oid, email_list_uuid, email_customer_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_list_customer_editor_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_list_uuid** | **str**| null | 
 **email_customer_uuid** | **str**| null | 

### Return type

[**EmailCustomerEditorUrlResponse**](EmailCustomerEditorUrlResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_list_customers**
> EmailListCustomersResponse get_email_list_customers(storefront_oid, email_list_uuid, page_number=page_number, page_size=page_size)

Get email list customers

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_list_uuid = 'email_list_uuid_example' # str | null
page_number = 56 # int | null (optional)
page_size = 56 # int | null (optional)

try: 
    # Get email list customers
    api_response = api_instance.get_email_list_customers(storefront_oid, email_list_uuid, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_list_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_list_uuid** | **str**| null | 
 **page_number** | **int**| null | [optional] 
 **page_size** | **int**| null | [optional] 

### Return type

[**EmailListCustomersResponse**](EmailListCustomersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_lists**
> EmailListsResponse get_email_lists(storefront_oid)

Get email lists

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null

try: 
    # Get email lists
    api_response = api_instance.get_email_lists(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 

### Return type

[**EmailListsResponse**](EmailListsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_segment**
> EmailSegmentResponse get_email_segment(storefront_oid, email_segment_uuid)

Get email segment

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_segment_uuid = 'email_segment_uuid_example' # str | null

try: 
    # Get email segment
    api_response = api_instance.get_email_segment(storefront_oid, email_segment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_segment_uuid** | **str**| null | 

### Return type

[**EmailSegmentResponse**](EmailSegmentResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_segment_customer_editor_url**
> EmailCustomerEditorUrlResponse get_email_segment_customer_editor_url(storefront_oid, email_segment_uuid, email_customer_uuid)

Get email segment customers editor URL

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_segment_uuid = 'email_segment_uuid_example' # str | null
email_customer_uuid = 'email_customer_uuid_example' # str | null

try: 
    # Get email segment customers editor URL
    api_response = api_instance.get_email_segment_customer_editor_url(storefront_oid, email_segment_uuid, email_customer_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_segment_customer_editor_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_segment_uuid** | **str**| null | 
 **email_customer_uuid** | **str**| null | 

### Return type

[**EmailCustomerEditorUrlResponse**](EmailCustomerEditorUrlResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_segment_customers**
> EmailSegmentCustomersResponse get_email_segment_customers(storefront_oid, email_segment_uuid, page_number=page_number, page_size=page_size)

Get email segment customers

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_segment_uuid = 'email_segment_uuid_example' # str | null
page_number = 56 # int | null (optional)
page_size = 56 # int | null (optional)

try: 
    # Get email segment customers
    api_response = api_instance.get_email_segment_customers(storefront_oid, email_segment_uuid, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_segment_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_segment_uuid** | **str**| null | 
 **page_number** | **int**| null | [optional] 
 **page_size** | **int**| null | [optional] 

### Return type

[**EmailSegmentCustomersResponse**](EmailSegmentCustomersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_segments**
> EmailSegmentsResponse get_email_segments(storefront_oid)

Get email segments

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null

try: 
    # Get email segments
    api_response = api_instance.get_email_segments(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 

### Return type

[**EmailSegmentsResponse**](EmailSegmentsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_sending_domain**
> EmailSendingDomainResponse get_email_sending_domain(domain)

Get email sending domain

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
domain = 'domain_example' # str | null

try: 
    # Get email sending domain
    api_response = api_instance.get_email_sending_domain(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_sending_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| null | 

### Return type

[**EmailSendingDomainResponse**](EmailSendingDomainResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_sending_domain_status**
> EmailSendingDomainResponse get_email_sending_domain_status(domain)

Get email sending domain status

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
domain = 'domain_example' # str | null

try: 
    # Get email sending domain status
    api_response = api_instance.get_email_sending_domain_status(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_sending_domain_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| null | 

### Return type

[**EmailSendingDomainResponse**](EmailSendingDomainResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_sending_domains**
> EmailSendingDomainsResponse get_email_sending_domains()

Get email sending domains

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))

try: 
    # Get email sending domains
    api_response = api_instance.get_email_sending_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_sending_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EmailSendingDomainsResponse**](EmailSendingDomainsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_template**
> EmailTemplate get_email_template(storefront_oid, email_template_oid)

Get email template

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_template_oid = 56 # int | null

try: 
    # Get email template
    api_response = api_instance.get_email_template(storefront_oid, email_template_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_template_oid** | **int**| null | 

### Return type

[**EmailTemplate**](EmailTemplate.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_templates**
> EmailTemplatesResponse get_email_templates(storefront_oid, trigger_type=trigger_type)

Get email templates

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
trigger_type = 'trigger_type_example' # str | null (optional)

try: 
    # Get email templates
    api_response = api_instance.get_email_templates(storefront_oid, trigger_type=trigger_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **trigger_type** | **str**| null | [optional] 

### Return type

[**EmailTemplatesResponse**](EmailTemplatesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_third_party_providers**
> EmailThirdPartyProvidersResponse get_email_third_party_providers(storefront_oid)

Get a list of third party email providers

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null

try: 
    # Get a list of third party email providers
    api_response = api_instance.get_email_third_party_providers(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_email_third_party_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 

### Return type

[**EmailThirdPartyProvidersResponse**](EmailThirdPartyProvidersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiments**
> ExperimentsResponse get_experiments(storefront_oid)

Get experiments

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null

try: 
    # Get experiments
    api_response = api_instance.get_experiments(storefront_oid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_experiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 

### Return type

[**ExperimentsResponse**](ExperimentsResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_histogram_property_names**
> EmailHistogramPropertyNamesResponse get_histogram_property_names(storefront_oid, property_type=property_type)

Get histogram property names

Obtain a list of property names for a given property type 

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
property_type = 'property_type_example' # str | null (optional)

try: 
    # Get histogram property names
    api_response = api_instance.get_histogram_property_names(storefront_oid, property_type=property_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_histogram_property_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **property_type** | **str**| null | [optional] 

### Return type

[**EmailHistogramPropertyNamesResponse**](EmailHistogramPropertyNamesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_histogram_property_values**
> EmailHistogramPropertyValuesResponse get_histogram_property_values(storefront_oid, property_name=property_name, property_type=property_type, limit=limit)

Get histogram property values

Obtain a list of property values for a given property name and type 

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
property_name = 'property_name_example' # str | null (optional)
property_type = 'property_type_example' # str | null (optional)
limit = 56 # int | null (optional)

try: 
    # Get histogram property values
    api_response = api_instance.get_histogram_property_values(storefront_oid, property_name=property_name, property_type=property_type, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->get_histogram_property_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **property_name** | **str**| null | [optional] 
 **property_type** | **str**| null | [optional] 
 **limit** | **int**| null | [optional] 

### Return type

[**EmailHistogramPropertyValuesResponse**](EmailHistogramPropertyValuesResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_email_third_party_provider_list**
> import_email_third_party_provider_list(storefront_oid, import_request)

Import a third party provider list

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
import_request = ultracart.EmailThirdPartyListImportRequest() # EmailThirdPartyListImportRequest | lists to import

try: 
    # Import a third party provider list
    api_instance.import_email_third_party_provider_list(storefront_oid, import_request)
except ApiException as e:
    print("Exception when calling StorefrontApi->import_email_third_party_provider_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **import_request** | [**EmailThirdPartyListImportRequest**](EmailThirdPartyListImportRequest.md)| lists to import | 

### Return type

void (empty response body)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_campaign**
> EmailCampaignResponse insert_email_campaign(storefront_oid, email_campaign)

Insert email campaign

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_campaign = ultracart.EmailCampaign() # EmailCampaign | Email campaign

try: 
    # Insert email campaign
    api_response = api_instance.insert_email_campaign(storefront_oid, email_campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_campaign** | [**EmailCampaign**](EmailCampaign.md)| Email campaign | 

### Return type

[**EmailCampaignResponse**](EmailCampaignResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_commseq**
> EmailCommseqResponse insert_email_commseq(storefront_oid, email_commseq)

Insert email commseq

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_commseq = ultracart.EmailCommseq() # EmailCommseq | Email commseq

try: 
    # Insert email commseq
    api_response = api_instance.insert_email_commseq(storefront_oid, email_commseq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_commseq: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_commseq** | [**EmailCommseq**](EmailCommseq.md)| Email commseq | 

### Return type

[**EmailCommseqResponse**](EmailCommseqResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_email**
> EmailCommseqEmailResponse insert_email_email(storefront_oid, email_commseq_email)

Insert email email

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_commseq_email = ultracart.EmailCommseqEmail() # EmailCommseqEmail | Email email

try: 
    # Insert email email
    api_response = api_instance.insert_email_email(storefront_oid, email_commseq_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_commseq_email** | [**EmailCommseqEmail**](EmailCommseqEmail.md)| Email email | 

### Return type

[**EmailCommseqEmailResponse**](EmailCommseqEmailResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_flow**
> EmailFlowResponse insert_email_flow(storefront_oid, email_flow)

Insert email flow

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_flow = ultracart.EmailFlow() # EmailFlow | Email flow

try: 
    # Insert email flow
    api_response = api_instance.insert_email_flow(storefront_oid, email_flow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_flow** | [**EmailFlow**](EmailFlow.md)| Email flow | 

### Return type

[**EmailFlowResponse**](EmailFlowResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_list**
> EmailListResponse insert_email_list(storefront_oid, email_list)

Insert email list

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_list = ultracart.EmailList() # EmailList | Email list

try: 
    # Insert email list
    api_response = api_instance.insert_email_list(storefront_oid, email_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_list** | [**EmailList**](EmailList.md)| Email list | 

### Return type

[**EmailListResponse**](EmailListResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_email_segment**
> EmailSegmentResponse insert_email_segment(storefront_oid, email_segment)

Insert email segment

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_segment = ultracart.EmailSegment() # EmailSegment | Email segment

try: 
    # Insert email segment
    api_response = api_instance.insert_email_segment(storefront_oid, email_segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->insert_email_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_segment** | [**EmailSegment**](EmailSegment.md)| Email segment | 

### Return type

[**EmailSegmentResponse**](EmailSegmentResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepare_download_email_segment**
> EmailSegmentDownloadPrepareResponse prepare_download_email_segment(storefront_oid, email_segment_uuid)

Prepare download of email segment

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_segment_uuid = 'email_segment_uuid_example' # str | null

try: 
    # Prepare download of email segment
    api_response = api_instance.prepare_download_email_segment(storefront_oid, email_segment_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->prepare_download_email_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_segment_uuid** | **str**| null | 

### Return type

[**EmailSegmentDownloadPrepareResponse**](EmailSegmentDownloadPrepareResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> LookupResponse search(category=category, matches=matches, max_hits=max_hits)

Searches for all matching values

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
category = 'category_example' # str | null (optional)
matches = 'matches_example' # str | null (optional)
max_hits = 56 # int | null (optional)

try: 
    # Searches for all matching values
    api_response = api_instance.search(category=category, matches=matches, max_hits=max_hits)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| null | [optional] 
 **matches** | **str**| null | [optional] 
 **max_hits** | **int**| null | [optional] 

### Return type

[**LookupResponse**](LookupResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_email_list_customers**
> EmailListCustomersResponse search_email_list_customers(storefront_oid, email_list_uuid, starts_with=starts_with)

Search email list customers

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_list_uuid = 'email_list_uuid_example' # str | null
starts_with = 'starts_with_example' # str | null (optional)

try: 
    # Search email list customers
    api_response = api_instance.search_email_list_customers(storefront_oid, email_list_uuid, starts_with=starts_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->search_email_list_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_list_uuid** | **str**| null | 
 **starts_with** | **str**| null | [optional] 

### Return type

[**EmailListCustomersResponse**](EmailListCustomersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_email_segment_customers**
> EmailSegmentCustomersResponse search_email_segment_customers(storefront_oid, email_segment_uuid, starts_with=starts_with)

Search email segment customers

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_segment_uuid = 'email_segment_uuid_example' # str | null
starts_with = 'starts_with_example' # str | null (optional)

try: 
    # Search email segment customers
    api_response = api_instance.search_email_segment_customers(storefront_oid, email_segment_uuid, starts_with=starts_with)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->search_email_segment_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_segment_uuid** | **str**| null | 
 **starts_with** | **str**| null | [optional] 

### Return type

[**EmailSegmentCustomersResponse**](EmailSegmentCustomersResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_email_campaign**
> BaseResponse start_email_campaign(storefront_oid, email_campaign_uuid)

Start email campaign

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_campaign_uuid = 'email_campaign_uuid_example' # str | null

try: 
    # Start email campaign
    api_response = api_instance.start_email_campaign(storefront_oid, email_campaign_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->start_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_campaign_uuid** | **str**| null | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_to_email_list**
> EmailListSubscribeResponse subscribe_to_email_list(storefront_oid, email_list_uuid, customers)

Subscribe customers to email list

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_list_uuid = 'email_list_uuid_example' # str | null
customers = [ultracart.EmailCustomer()] # list[EmailCustomer] | Customers

try: 
    # Subscribe customers to email list
    api_response = api_instance.subscribe_to_email_list(storefront_oid, email_list_uuid, customers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->subscribe_to_email_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_list_uuid** | **str**| null | 
 **customers** | [**list[EmailCustomer]**](EmailCustomer.md)| Customers | 

### Return type

[**EmailListSubscribeResponse**](EmailListSubscribeResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_campaign**
> EmailCampaignResponse update_email_campaign(storefront_oid, email_campaign_uuid, email_campaign)

Update email campaign

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_campaign_uuid = 'email_campaign_uuid_example' # str | null
email_campaign = ultracart.EmailCampaign() # EmailCampaign | Email campaign

try: 
    # Update email campaign
    api_response = api_instance.update_email_campaign(storefront_oid, email_campaign_uuid, email_campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_campaign_uuid** | **str**| null | 
 **email_campaign** | [**EmailCampaign**](EmailCampaign.md)| Email campaign | 

### Return type

[**EmailCampaignResponse**](EmailCampaignResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_commseq**
> EmailCommseqResponse update_email_commseq(storefront_oid, commseq_uuid, email_commseq)

Update email commseq

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
commseq_uuid = 'commseq_uuid_example' # str | null
email_commseq = ultracart.EmailCommseq() # EmailCommseq | Email commseq

try: 
    # Update email commseq
    api_response = api_instance.update_email_commseq(storefront_oid, commseq_uuid, email_commseq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_commseq: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **commseq_uuid** | **str**| null | 
 **email_commseq** | [**EmailCommseq**](EmailCommseq.md)| Email commseq | 

### Return type

[**EmailCommseqResponse**](EmailCommseqResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_email**
> EmailCommseqEmailResponse update_email_email(storefront_oid, commseq_email_uuid, email_commseq_email)

Update email email

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
commseq_email_uuid = 'commseq_email_uuid_example' # str | null
email_commseq_email = ultracart.EmailCommseqEmail() # EmailCommseqEmail | Email commseq email

try: 
    # Update email email
    api_response = api_instance.update_email_email(storefront_oid, commseq_email_uuid, email_commseq_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **commseq_email_uuid** | **str**| null | 
 **email_commseq_email** | [**EmailCommseqEmail**](EmailCommseqEmail.md)| Email commseq email | 

### Return type

[**EmailCommseqEmailResponse**](EmailCommseqEmailResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_flow**
> EmailFlowResponse update_email_flow(storefront_oid, email_flow_uuid, email_flow)

Update email flow

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_flow_uuid = 'email_flow_uuid_example' # str | null
email_flow = ultracart.EmailFlow() # EmailFlow | Email flow

try: 
    # Update email flow
    api_response = api_instance.update_email_flow(storefront_oid, email_flow_uuid, email_flow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_flow_uuid** | **str**| null | 
 **email_flow** | [**EmailFlow**](EmailFlow.md)| Email flow | 

### Return type

[**EmailFlowResponse**](EmailFlowResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_list**
> EmailListResponse update_email_list(storefront_oid, email_list_uuid, email_list)

Update email list

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_list_uuid = 'email_list_uuid_example' # str | null
email_list = ultracart.EmailList() # EmailList | Email list

try: 
    # Update email list
    api_response = api_instance.update_email_list(storefront_oid, email_list_uuid, email_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_list_uuid** | **str**| null | 
 **email_list** | [**EmailList**](EmailList.md)| Email list | 

### Return type

[**EmailListResponse**](EmailListResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_segment**
> EmailSegmentResponse update_email_segment(storefront_oid, email_segment_uuid, email_segment)

Update email segment

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
email_segment_uuid = 'email_segment_uuid_example' # str | null
email_segment = ultracart.EmailSegment() # EmailSegment | Email segment

try: 
    # Update email segment
    api_response = api_instance.update_email_segment(storefront_oid, email_segment_uuid, email_segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_email_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **email_segment_uuid** | **str**| null | 
 **email_segment** | [**EmailSegment**](EmailSegment.md)| Email segment | 

### Return type

[**EmailSegmentResponse**](EmailSegmentResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_experiment**
> ExperimentResponse update_experiment(storefront_oid, storefront_experiment_oid, experiment)

Update experiment

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

api_instance = ultracart.StorefrontApi(ultracart.ApiClient(configuration))
storefront_oid = 'storefront_oid_example' # str | null
storefront_experiment_oid = 56 # int | null
experiment = ultracart.Experiment() # Experiment | Experiment

try: 
    # Update experiment
    api_response = api_instance.update_experiment(storefront_oid, storefront_experiment_oid, experiment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorefrontApi->update_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storefront_oid** | **str**| null | 
 **storefront_experiment_oid** | **int**| null | 
 **experiment** | [**Experiment**](Experiment.md)| Experiment | 

### Return type

[**ExperimentResponse**](ExperimentResponse.md)

### Authorization

[ultraCartBrowserApiKey](../README.md#ultraCartBrowserApiKey), [ultraCartOauth](../README.md#ultraCartOauth), [ultraCartSimpleApiKey](../README.md#ultraCartSimpleApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

