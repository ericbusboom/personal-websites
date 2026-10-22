---
title: "California and San Diego Alcohol Licenses"
date: 2020-11-26T20:39:01+00:00
draft: false
categories: ["Crime_Data", "Dataset"]
tags: ["abc.ca.gov", "crime", "Crime_Data", "law_enforcement", "police"]
author: "metapack"
description: "Records of alcohol licenses in california, from the CA ABC daily file, with"
---

_Records of alcohol licenses in california, from the CA ABC daily file, with improvements to geographic identifiers, and acompilation of areal densities of on-sale and off-sale licenses in San Diego county._

`abc.ca.gov-licenses-2.1.2`. Modified 2020-11-27T23:20:08


## Resources

  * **[ca_abc_licenses](<https://library-metatab-org.s3.amazonaws.com/abc.ca.gov-licenses-2.1.2/data/ca_abc_licenses.csv>)**. California Alcohol Beverage Control Licenses
  * **[sd_abc_density](<https://library-metatab-org.s3.amazonaws.com/abc.ca.gov-licenses-2.1.2/data/sd_abc_density.csv>)**. Areal density of on-sale and off-sale licenses in San Diego county


## Documentation

This package is a conversion of the California Daily ABC file, so it is current as of the modification date of the package. The main change is the addition of the `county` variable, the FIPS code for the county, and the `tract`, the ACS format geoid version of the tract identifier. 

For the values for the `license_type` field, see https://www.abc.ca.gov/licensing/license-types/. The codes have general categories roughly noted by the tens digit, so you can divide by 10 to group them: 

  * 0: Manufacturers and Distilleries
  * 1: Importers, Borkers and Wholesalers
  * 2: Off-sale (Sale for off-site consumption) and smalle wholesalers
  * 4: On-sale
  * 5: Clubs and caterers
  * 6: On-Sale Seasonal sales, B&B, Hospitals, Theater Companies, etc. 
  * 7: Events, Farmers Markets
  * 8: A Variety of odd types
  * 9: Special Use


The most common types are: 

  * 41; On-Sale Beer and Wine - Public
  * 47: On-Sale General - Eating
  * 21: Off-Sale General
  * 20: Off-sale Beer and Wine
  * 58: Catering
  * 48: On-Sale General -- Public ( Bars and Nightclubs )


### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/abc.ca.gov-licenses-2.1.2/index.html>)


## Images

  * [![](https://library-metatab-org.s3.amazonaws.com/abc.ca.gov-licenses-2.1.2/doc/OnsaleDensity.png)](<https://library-metatab-org.s3.amazonaws.com/abc.ca.gov-licenses-2.1.2/doc/OnsaleDensity.png> "On-Sale Density") Density of On-Sale permits in permits per square kilometer.


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

ca_abc_licenses | sd_abc_density   


### ca_abc_licenses

Column Name| Data Type| Description  
---|---|---  
license_type| integer|   
file_number| integer|   
lic_or_app| string|   
type_status| string|   
type_orig_iss_date| string|   
expir_date| string|   
fee_codes| string|   
dup_counts| string|   
master_ind| string|   
term_in_of_months| integer|   
geo_code| integer|   
district| integer|   
primary_name| text|   
prem_addr_1| string|   
prem_addr_2| string|   
prem_city| string|   
prem_state| string|   
prem_zip| string|   
dba_name| text|   
mail_addr_1| string|   
mail_addr_2| string|   
mail_city| string|   
mail_state| string|   
mail_zip| string|   
prem_county| string|   
prem_census_tract| string|   
county| integer| County FIPS code  
tract| string| Tract Geoid  
  
### sd_abc_density

Column Name| Data Type| Description  
---|---|---  
geoid| string| Tract geoid  
geometry| string| Tract geometry, in wkt format  
aland| integer| Land area of tract, in square meters  
offsale| integer| Count of off-sale licenses in tract, 20 & 21  
onsale| integer| Count of on-sale licenses in tract, 41, 47, 48  
offsale_den| number| Areal density of off-sale licences, per square km  
onsale_den| number| Areal density of on-sale licences, per square km  
community_name| string| Community name in San Diego, Cityname otherwise.  
  
## References

Urls used in the creation of this data package.

  * **abc_licenses_source (no longer available)**. Raw ABC data
  * **metapack+https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-geography-2018-13.csv**. San Diego geography
  * **metapack+https://library-metatab-org.s3.amazonaws.com/huduser.gov-zip_tract-2016-2.csv**. Zip to Tract mapping


## Packages

  * **s3** s3://library.metatab.org/abc.ca.gov-licenses-2.1.2.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/abc.ca.gov-licenses-2.1.2.csv>
  * **source** <https://github.com/metatab-packages/crime-sandiego-collection.git>


### Accessing Data in Vanilla Pandas
```
import pandas as pd


ca_abc_licenses_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/abc.ca.gov-licenses-2.1.2/data/ca_abc_licenses.csv')
sd_abc_density_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/abc.ca.gov-licenses-2.1.2/data/sd_abc_density.csv')
```

### Accessing Package in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/abc.ca.gov-licenses-2.1.2.csv')

# Create Dataframes
ca_abc_licenses_df = pkg.resource('ca_abc_licenses').dataframe()
sd_abc_density_gdf = pkg.resource('sd_abc_density').geoframe()
```
