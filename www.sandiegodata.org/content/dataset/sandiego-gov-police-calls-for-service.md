---
title: "San Diego Police Calls for Service"
date: 2020-06-17T23:58:23+00:00
draft: false
categories: ["Dataset", "Police Data"]
tags: ["crime", "law_enforcement", "police", "police_data_collection", "sandiego.gov"]
author: "metapack"
description: "San Diego Police Calls for Service, linked to related datasets"
---

_San Diego Police Calls for Service, linked to related datasets_

`sandiego.gov-police_calls_for_service-1.1.1`. Modified 2020-06-17T23:58:13

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[sdpd_calls_dispositions](<https://library-metatab-org.s3.amazonaws.com/sandiego.gov-police_calls_for_service-1.1.1/data/sdpd_calls_dispositions.csv>)**. San Diego Police Calls for Service, 2015 to 2020
  * **[sdpd_beats](<https://library-metatab-org.s3.amazonaws.com/sandiego.gov-police_calls_for_service-1.1.1/data/sdpd_beats.csv>)**. San Diego Police beats
  * **[sdpd_call_type](<https://library-metatab-org.s3.amazonaws.com/sandiego.gov-police_calls_for_service-1.1.1/data/sdpd_call_type.csv>)**. San Diego Police call type codes
  * **[sdpd_calls_for_service](<https://library-metatab-org.s3.amazonaws.com/sandiego.gov-police_calls_for_service-1.1.1/data/sdpd_calls_for_service.csv>)**. San Diego Police Calls for Service, 2015 to 2020
  * **[ct_map](<https://library-metatab-org.s3.amazonaws.com/sandiego.gov-police_calls_for_service-1.1.1/data/ct_map.csv>)**. Map from call type descriptions to simpler call types.


## Documentation

This dataset links to the San Dieg Police Calls for Service datasets, from multiple years, combine the years and lints to the destriptions of disposition codes and beat neighborhoods. 

# Caveats and Adjustments

The meaning of the numbers in the `day_of_week` column has changed from earlier to later years. Earlier years use values from 0 to 6, while later years use vlaues from 1 to 7. Because of this, the `day_of_week` vlaues have been re-calculated to the span from 0 to 6, where 0 is Monday and 6 is Sunday.

### Documentation Links

  * [Priority codes](<http://seshat.datasd.org/pd/pd_cfs_priority_defs_datasd.pdf>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

sdpd_calls_dispositions | sdpd_beats | sdpd_calls_for_service | sdpd_call_type | ct_map   


### sdpd_calls_dispositions

Column Name| Data Type| Description  
---|---|---  
disposition| string|   
description| string|   
  
### sdpd_beats

Column Name| Data Type| Description  
---|---|---  
beat| string|   
neighborhood| string|   
  
### sdpd_calls_for_service

Column Name| Data Type| Description  
---|---|---  
incident_num| string|   
date_time| datetime|   
day_of_week| integer|   
address_number_primary| integer|   
address_dir_primary| string|   
address_road_primary| string|   
address_sfx_primary| string|   
address_dir_intersecting| string|   
address_road_intersecting| string|   
address_sfx_intersecting| string|   
call_type| string|   
disposition| string|   
beat| string|   
priority| integer|   
  
### sdpd_call_type

Column Name| Data Type| Description  
---|---|---  
call_type| string|   
description| string|   
  
### ct_map

Column Name| Data Type| Description  
---|---|---  
call_type_desc| string|   
simple_ct| string|   
  
## References

Urls used in the creation of this data package.

  * **[calls_for_service_source_2015](<http://seshat.datasd.org/pd/pd_calls_for_service_2015_datasd_v1.csv>)**. San Diego Police Calls for Service, 2015
  * **[calls_for_service_source_2016](<http://seshat.datasd.org/pd/pd_calls_for_service_2016_datasd_v1.csv>)**. San Diego Police Calls for Service, 2016
  * **[calls_for_service_source_2017](<http://seshat.datasd.org/pd/pd_calls_for_service_2017_datasd_v1.csv>)**. San Diego Police Calls for Service, 2017
  * **[calls_for_service_source_2018](<http://seshat.datasd.org/pd/pd_calls_for_service_2018_datasd.csv>)**. San Diego Police Calls for Service, 2018
  * **[calls_for_service_source_2019](<http://seshat.datasd.org/pd/pd_calls_for_service_2019_datasd.csv>)**. San Diego Police Calls for Service, 2019
  * **[calls_for_service_source_2020](<http://seshat.datasd.org/pd/pd_calls_for_service_2020_datasd.csv>)**. San Diego Police Calls for Service, 2020
  * **[disp_codes_2017](<http://seshat.datasd.org/pd/pd_dispo_codes_historical_datasd.csv>)**. Disposition Codes, prior to October 17, 2017
  * **[disp_codes](<http://seshat.datasd.org/pd/pd_dispo_codes_datasd.csv>)**. Current disposition codes
  * **[beat_codes](<http://seshat.datasd.org/pd/pd_beat_neighborhoods_datasd.csv>)**. Beat Neighborhood Codes
  * **[call_type_codes](<http://seshat.datasd.org/pd/pd_cfs_calltypes_datasd.csv>)**. Call type codes


## Packages

  * **s3** s3://library.metatab.org/sandiego.gov-police_calls_for_service-1.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiego.gov-police_calls_for_service-1.1.1.csv>
  * **source** <https://github.com/metatab-packages/policedata-collection.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiego.gov-police_calls_for_service-1.1.1.csv')
    
    # Create Dataframes
    sdpd_calls_dispositions_df = pkg.resource('sdpd_calls_dispositions').dataframe()
    sdpd_beats_df = pkg.resource('sdpd_beats').dataframe()
    sdpd_call_type_df = pkg.resource('sdpd_call_type').dataframe()
    sdpd_calls_for_service_df = pkg.resource('sdpd_calls_for_service').dataframe()
    ct_map_df = pkg.resource('ct_map').dataframe()
    
[/code]
