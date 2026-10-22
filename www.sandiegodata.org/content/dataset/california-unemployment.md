---
title: "California Unemployment"
date: 2019-05-15T22:31:30+00:00
draft: false
categories: ["Dataset"]
tags: ["bls.gov", "ckan"]
author: "metapack"
description: "BLS employment measures for California"
---

_BLS employment measures for California_

`bls.gov-laus-ca-1`

Resources | Packages | Documentation| Contacts| References

## Resources

  * **[la_areas](<https://library-metatab-org.s3.amazonaws.com/bls.gov-laus-ca-1/data/la_areas.csv>)**. Area Codes
  * **[laus_ca](<https://library-metatab-org.s3.amazonaws.com/bls.gov-laus-ca-1/data/laus_ca.csv>)**. Local Area Unemployment


## Documentation

This file is a conversion of the BLS Local Area Unemployment (LAUS) file for California. The conversion breaks out parts of the series_id code, and includes a Census ACS geoid for most areas. 

## Measure Codes

The `measure_code` value indicates the type of measure: 
[code] 
    measure_code    measure_text
    03              unemployment rate
    04              unemployment
    05              employment
    06              labor force
    
[/code]

## Local Area Unemployment Statistics Series Identifier

The following is a sample format description of the Local Area Unemployment Statistics' series identifier:
[code] 
                          1         2
                 12345678901234567890
    Series ID    LAUCN281070000000003
    Positions    Value            Field Name
    1-2          LA               Prefix
    3            U                [Seasonal Adjustment Code](https://www.bls.gov/help/hlpseas.htm)
    4-18         CN2810700000000  [Area Code](https://www.bls.gov/help/def/la.htm#area)
    19-20        03               [Measure Code](https://www.bls.gov/help/def/la.htm#measure )
    
[/code]

### Documentation Links

  * [https://download.bls.gov/pub/time.series/la/la.txt](<Primary Documentation>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/bls.gov-laus-ca-1.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/bls.gov-laus-ca-1.csv>
  * **source** <https://github.com/sandiegodata/planning-database.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/bls.gov-laus-ca-1.zip')
    # CSV Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/bls.gov-laus-ca-1.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

## References

Urls used in the creation of this data package.

  * **[laus_ca_source](<https://download.bls.gov/pub/time.series/la/la.data.11.California#target_format=tsv>)**. Link to source file
  * **metapack+https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-geography-2018.csv#sd_county_boundary**. San Diego County Boundary
  * **censusgeo://US/cbsa**. Census Core-Based Statistical Areas
  * **censusgeo://US/csa**. Census Combined Statistical Areas
  * **censusgeo://CA/place**. Census Defined Places
  * **censusgeo://CA/county**. Census Counties
  * **censusgeo://US/state**. Census States


Last Modified 2019-01-03T22:56:36
