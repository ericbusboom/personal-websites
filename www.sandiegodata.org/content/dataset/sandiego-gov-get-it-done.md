---
title: "Get It Done Reports"
date: 2022-05-20T21:17:41+00:00
draft: false
categories: ["Dataset"]
tags: ["sandiego.gov"]
author: "metapack"
description: "Reports of non-emergency problems submitted by users of Get It Done"
---

_Reports of non-emergency problems submitted by users of Get It Done_

`sandiego.gov-get_it_done-1.1.2`. Modified 2022-05-20T21:17:32

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[gid_requests](<http://library.metatab.org/sandiego.gov-get_it_done-1.1.2/data/gid_requests.csv>)**. Get It Done requests
  * **[gid_rast](<http://library.metatab.org/sandiego.gov-get_it_done-1.1.2/data/gid_rast.csv>)**. Get It Done requests, in a format for rasterization


## Documentation

The Get It Done program allows residents and visitors to report certain types of non-emergency problems to the City using the Get It Done mobile app, web app, or by telephone. This dataset contains all Get It Done reports the City has received since the program launched in May 2016. 

This data package combines multiple years of the source data into a single file and adds a WKT format geometry.

### Documentation Links

  * [Download Page](<https://data.sandiego.gov/datasets/get-it-done-311/>) Reports of non-emergency problems submitted by users of Get It Done
  * [Documentation Page](<http://library.metatab.org/sandiego.gov-get_it_done-1.1.2/index.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

gid_requests | gid_rast   


### gid_requests

Column Name| Data Type| Description  
---|---|---  
index| integer|   
service_request_id| integer| A unique identifier for each request that also serves as a customer's report number for tracking purposes  
service_request_parent_id| integer| If the request has been determined to be a duplicate of an existing, open request, the original request is the parent and subsequent requests are children. All children will have the service_request_id of the parent in this field.  
sap_notification_number| integer| If the request is managed in the City's SAP system, this field will contain a unique identifier for the request used within SAP.  
date_requested| datetime|   
case_age_days| integer| The number of days, rounded to the nearest whole day, between request submission and request closure  
case_record_type| string| A higher-level grouping of service names that corresponds to the City staff group responsible for responding to the request  
service_name| string| A classification of the type of service to be performed  
date_closed| datetime|   
status| string| The current state of the service request  
lat| number| Latitude for request location  
lng| number|   
street_address| text|   
zipcode| integer|   
council_district| integer| If available, the council district where the service was requested  
comm_plan_code| integer| If available, a numeric code corresponding to the community where the service was requested  
comm_plan_name| string| If available, the community name where the service was requested  
park_name| string| If applicable, the park or open space area where the service was requested  
case_origin| string| Method by which the requestor submitted the request  
referred| string| When a case has a status of referred, this field indicates to where the case was referred  
public_description| string| The description submitted by the reporting party  
iamfloc| string|   
floc| string|   
geometry| string|   
in_county| string|   
  
### gid_rast

Column Name| Data Type| Description  
---|---|---  
service_code| string|   
geometry| string|   
  
## References

Urls used in the creation of this data package.

  * **[gid_2016](<https://seshat.datasd.org/get_it_done_311/get_it_done_2016_requests_datasd_v1.csv>)**. Get It Done requests, 2016
  * **[gid_2017](<https://seshat.datasd.org/get_it_done_311/get_it_done_2017_requests_datasd_v1.csv>)**. Get It Done requests, 2017
  * **[gid_2018](<https://seshat.datasd.org/get_it_done_311/get_it_done_2018_requests_datasd_v1.csv>)**. Get It Done requests, 2018
  * **[gid_2019](<https://seshat.datasd.org/get_it_done_311/get_it_done_2019_requests_datasd_v1.csv>)**. Get It Done requests, 2019
  * **[gid_2020](<https://seshat.datasd.org/get_it_done_311/get_it_done_2020_requests_datasd_v1.csv>)**. Get It Done requests, 2020
  * **[gid_2021](<https://seshat.datasd.org/get_it_done_311/get_it_done_2021_requests_datasd_v1.csv>)**. Get It Done requests, 2021
  * **[gid_2022](<https://seshat.datasd.org/get_it_done_311/get_it_done_2022_requests_datasd_v1.csv>)**. Get It Done requests, 2022
  * **[data_dictionary](<https://seshat.datasd.org/get_it_done_311/get_it_done_requests_dictionary_datasd.csv>)**. Data Dictionary
  * **[services](<https://seshat.datasd.org/get_it_done_311/get_it_done_311_services_datasd.csv>)**. Services


## Packages

  * **zip** <http://library.metatab.org/sandiego.gov-get_it_done-1.1.2.zip>
  * **s3** s3://library.metatab.org/sandiego.gov-get_it_done-1.1.2.csv
  * **csv** <http://library.metatab.org/sandiego.gov-get_it_done-1.1.2.csv>
  * **source** <https://github.com/metatab-packages/sandiego.gov-get_it_done.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    gid_requests_df =  pd.read_csv('http://library.metatab.org/sandiego.gov-get_it_done-1.1.2/data/gid_requests.csv')
    gid_rast_df =  pd.read_csv('http://library.metatab.org/sandiego.gov-get_it_done-1.1.2/data/gid_rast.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/sandiego.gov-get_it_done-1.1.2.zip')
    
    # Create Dataframes
    gid_requests_gdf = pkg.resource('gid_requests').geoframe()
    gid_rast_gdf = pkg.resource('gid_rast').geoframe()
    
[/code]
