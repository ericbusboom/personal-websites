---
title: "California Notary County Codes"
date: 2019-06-18T01:47:50+00:00
draft: false
categories: ["Dataset"]
tags: ["sandiegodata.org"]
author: "metapack"
description: "Numeric county codes used by California government."
---

_Numeric county codes used by California government._

`sandiegodata.org-county_codes-ca-3`


## Resources

  * **[ca_county_codes](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-county_codes-ca-3/data/ca_county_codes.csv>)**. California Notary codes for counties.


## Documentation

These county codes are used in California Department of Education CDS identification numbers, and a variety of other places. They are different from the FIPS codes for counties used by the US Census.

These codes were scraped from a website. 

## Versions

  1. Initial version
  2. Added Census FIPS codes and Census county names
  3. Fixed error


### Documentation Links

  * [Codes page](<http://dts.edatatrace.com/dts3/content/doc/whelp/mergedProjects/dts2tt/mergedProjects/dts2ttcs/not_code_list_kern.htm>)The webpage the codes were scraped from


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-county_codes-ca-3.zip>
  * **s3** s3://library.metatab.org/sandiegodata.org-county_codes-ca-3.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-county_codes-ca-3.csv>
  * **source** <https://github.com/sandiegodata-projects/planning-database.git>


### Accessing Packages in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-county_codes-ca-3.zip')

# Create Dataframes

ca_county_codes_df = pkg.resource('ca_county_codes').dataframe()
```

## Data Dictionary

ca_county_codes   


### ca_county_codes

Column Name| Data Type| Description  
---|---|---  
notary_code| string| County code used by the California notary and Secretary of State  
fips_code| string| County code used by the US Census  
simple_name| string| Simple county name  
census_name| string| County name in the US Census  
  
Last Modified 2019-08-08T20:13:28

## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-county_codes-ca-3.zip>
  * **s3** s3://library.metatab.org/sandiegodata.org-county_codes-ca-3.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-county_codes-ca-3.csv>
  * **source** <https://github.com/sandiegodata-projects/planning-database.git>


### Accessing Packages in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-county_codes-ca-3.zip')

# Create Dataframes

ca_county_codes_df = pkg.resource('ca_county_codes').dataframe()
```
