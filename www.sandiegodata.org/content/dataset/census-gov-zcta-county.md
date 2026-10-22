---
title: "Zip code (zcta) To County Crosswalk"
date: 2020-11-09T22:15:02+00:00
draft: false
categories: ["Dataset"]
tags: ["census.gov"]
author: "metapack"
description: "Maps Cenus zip-code tabulation areas to Counties"
---

_Maps Cenus zip-code tabulation areas to Counties_

`census.gov-zcta_county-2.1.2`. Modified 2022-04-25T18:11:42


## Resources

  * **[county_zcta](<https://library-metatab-org.s3.amazonaws.com/census.gov-zcta_county-2.1.2/data/county_zcta.csv>)**. County to Zcta Crosswalk


## Documentation

This file links Ztca regions -- the Census version of ZIP codes, to counties, by associating a Zcta with the county that contains the Zctas centroid. 

There are only about 1/2 the number of Zctas in this file ( 33K ) as there are ZIP codes ( about 77K )

## Caveats

Note that the ZCTA regions are joined to counties after converting the geometries to EPSG 4326 (WGS84), from the original 4269 (NAD 83). The discrepancy between these CRS is only a few meters, so this should not make a difference.

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/census.gov-zcta_county-2.1.2/index.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

county_zcta   


### county_zcta

Column Name| Data Type| Description  
---|---|---  
state| string| State FIPS code  
county| string| County FIPS code  
zcta| string| Zcta (zip) code  
zcta_geoid| string| Zcta geoid  
county_geoid| string| County geoid  
  
## References

Urls used in the creation of this data package.

  * **censusgeo://2018/5/CA/zcta/**. ZCTA Geography file
  * **censusgeo://2018/5/US/county/**. Counties geography file


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/census.gov-zcta_county-2.1.2.zip>
  * **s3** s3://library.metatab.org/census.gov-zcta_county-2.1.2.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/census.gov-zcta_county-2.1.2.csv>
  * **source** <https://github.com/metatab-packages/census.gov-zcta_county.git>


### Accessing Data in Vanilla Pandas
```
import pandas as pd


county_zcta_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-zcta_county-2.1.2/data/county_zcta.csv')
```

### Accessing Package in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/census.gov-zcta_county-2.1.2.zip')

# Create Dataframes
county_zcta_df = pkg.resource('county_zcta').dataframe()
```
