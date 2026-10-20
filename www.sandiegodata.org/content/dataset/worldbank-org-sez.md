---
title: "Special economic zones"
date: 2021-07-10T02:51:44+00:00
draft: false
categories: ["Dataset", "sez"]
tags: ["sez", "special_economic_zones", "worldbank.org"]
author: "metapack"
description: "Information on special economic zones have been individually collected and"
---

_Information on special economic zones have been individually collected and researched in a study focusing on the governance of SEZ. This is just a subset (586) of the extant global SEZs, which have been estimated at 3500-4000._

`worldbank.org-sez-1.1.1`. Modified 2021-07-12T20:47:42

Resources | Packages | Documentation| Contacts| Data Dictionary

## Resources

  * **[sez](<http://library.metatab.org/worldbank.org-sez-1.1.1/data/sez.csv>)**. Special Economic Zones


## Documentation

### Documentation Links

  * [Documentation Page](<http://library.metatab.org/worldbank.org-sez-1.1.1/index.html>)
  * [Dataset webpage](<https://datacatalog.worldbank.org/dataset/special-economic-zones-sez>)
  * [Dataset viewer web application](<http://devseed.com/sez-viewer/#/BGD6>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

sez   


### sez

Column Name| Data Type| Description  
---|---|---  
id| integer|   
unique_id| string|   
check| string|   
latitude| number|   
longitude| number|   
country_code| string|   
country_type_combo| string|   
region| string|   
country| string|   
zone_type| string|   
zone_name| text|   
operational_date| text|   
size| string|   
management_type| string|   
management_company| text|   
legal_framework| text|   
legalframework_type| string|   
legalframework_year| string|   
regulatory_authority| string|   
authority_independence| string|   
private_participation| string|   
private_participation2| string|   
developer_incentive| string|   
decade_ofoperation| string|   
size_range| string|   
standard_corptax| string|   
corptax_type| string|   
corptax_exemp| string|   
corptax_duration| string|   
corptax_grace| string|   
total_duration| string|   
duration_type| string|   
investment_min| string|   
export_min| string|   
req_other| string|   
importduty_type| string|   
importduty_input| string|   
input_duration| string|   
importduty_capex| string|   
capex_duration| string|   
repatriation| string|   
capital_gains| string|   
withholding| string|   
property_land| string|   
vat_sales| string|   
employment| string|   
other| string|   
nearest_port| string|   
nearest_portdist| integer|   
nearest_airport| text|   
nearest_airportdist| integer|   
populous_city| string|   
populous_citydist| integer|   
city_1m| string|   
city_1mdist| integer|   
city_500k| string|   
city_500kdist| integer|   
500kcity_range| string|   
city_300k| string|   
city_300kdist| integer|   
note| string|   
geometry| string|   
  
## Packages

  * **s3** s3://library.metatab.org/worldbank.org-sez-1.1.1.csv
  * **csv** <http://library.metatab.org/worldbank.org-sez-1.1.1.csv>
  * **source** <https://github.com/sandiegodata-projects/chartercitiesinstitute.org-sez>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    sez_df =  pd.read_csv('http://library.metatab.org/worldbank.org-sez-1.1.1/data/sez.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/worldbank.org-sez-1.1.1.csv')
    
    # Create Dataframes
    sez_gdf = pkg.resource('sez').geoframe()
    
[/code]
