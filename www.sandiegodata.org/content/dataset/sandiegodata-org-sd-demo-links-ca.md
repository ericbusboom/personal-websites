---
title: "California School District Links to US Census"
date: 2019-08-08T19:04:44+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "education", "sandiegodata.org"]
author: "metapack"
description: "Links between CDS codes, NCES codes and school district geoids in the US census"
---

_Links between CDS codes, NCES codes and school district geoids in the US census_

`sandiegodata.org-sd_demo_links-ca-4`

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[ca_sd_links](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sd_demo_links-ca-4/data/ca_sd_links.csv>)**. Links between NCES, CDS and Geoids for California school districts


## Documentation

Links between three identification codes for California districts:

  * CD Codes, the County/District codes used in most CDE data files. 
  * NCES, codes used by the National Center for Educational Statistics
  * Census geoids, codes used in the US Census and American Community Survey. 


This linkage file can be used to connect data fiels from the California Department of education to US Census demographics. 

## Versions

  1. Initial version
  2. Added county codes
  3. Fixed datatype ( to string ) for county codes
  4. Update to get FIPS codes to have 3 digits.


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sd_demo_links-ca-4.zip>
  * **s3** s3://library.metatab.org/sandiegodata.org-sd_demo_links-ca-4.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sd_demo_links-ca-4.csv>
  * **source** <https://github.com/metatab-packages/cde.ca.gov.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sd_demo_links-ca-4.zip')
    
    # Create Dataframes
    
    ca_sd_links_df = pkg.resource('ca_sd_links').dataframe()
[/code]

## Data Dictionary

ca_sd_links   


### ca_sd_links

Column Name| Data Type| Description  
---|---|---  
nces_code| integer| NCES code for district  
geoid| string| Census Geoid for district  
cd_code| integer| California County/District code  
district_name| text| Census name for district  
sd_type| string| Type of district: Elementary (elem), Secondary (sec) or Unified (uni)  
notary_county_code| string| California Notary / Secretary of State county code  
fips_county_code| string| US Census county / FIPS code.  
  
## References

Urls used in the creation of this data package.

  * **census://2015/5/CA/sdelm/B01003**. Census elementary school districts for California
  * **census://2015/5/CA/sdsec/B01003**. Census secondary school districts for California
  * **census://2015/5/CA/sduni/B01003**. Census unified school districts for California
  * **metapack+https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-county_codes-ca.csv#ca_county_codes**. Noarty and Census county codes for California
  * **metapack+https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-schools-1.zip#public_schools**. California public schools
  * **metapack+https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-schools-1.zip#school_districts**. California school districts


Last Modified 2019-08-08T20:18:28

## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sd_demo_links-ca-4.zip>
  * **s3** s3://library.metatab.org/sandiegodata.org-sd_demo_links-ca-4.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sd_demo_links-ca-4.csv>
  * **source** <https://github.com/metatab-packages/cde.ca.gov.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sd_demo_links-ca-4.zip')
    
    # Create Dataframes
    
    ca_sd_links_df = pkg.resource('ca_sd_links').dataframe()
[/code]
