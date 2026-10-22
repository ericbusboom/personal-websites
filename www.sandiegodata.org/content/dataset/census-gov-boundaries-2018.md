---
title: "Census Cartographic Boundary Files, 2018 vintage"
date: 2020-05-20T20:59:09+00:00
draft: false
categories: ["Dataset"]
tags: ["census.gov"]
author: "metapack"
description: "The cartographic boundary files are simplified representations of selected"
---

_The cartographic boundary files are simplified representations of selected geographic areas from the Census Bureau’s MAF/TIGER geographic database. These boundary files are specifically designed for small scale thematic mapping._

`census.gov-boundaries-2018-1.2.8`. Modified 2020-08-12T04:35:14

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[state_500k](<https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/state_500k.csv>)**. State boundaries, scale 500K:1
  * **[state_5m](<https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/state_5m.csv>)**. State boundaries, scale 5M:1
  * **[state_20m](<https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/state_20m.csv>)**. State boundaries, scale 20M:1
  * **[county_500k](<https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/county_500k.csv>)**. County boundaries, scale 500K:1
  * **[county_5m](<https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/county_5m.csv>)**. County boundaries, scale 5M:1
  * **[county_20m](<https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/county_20m.csv>)**. County boundaries, scale 20M:1
  * **[nation_5m](<https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/nation_5m.csv>)**. National boundary, 5M:1
  * **[nation_20m](<https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/nation_20m.csv>)**. National boundary 20M:1
  * **[zcta_500k](<https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/zcta_500k.csv>)**. ZCTA (Zip Codes), scale 500K:1


## Documentation

This data package collects a selection of the US Census cartographic shape files, which are designed to be used in creating maps. For each type of region, they come in a varity of resolutions, so they are more suitable for creating web maps than the much larger TIGER files.

![](https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.4/notebooks/continental.png)

These files have been processed to all have the same schema and use ACS style Geoids. The original files have AFF style geoids, which have extra '00' characters in them.

The use of a single schema means that in some files, some columns are consistently empty. For instance, ZCTA ( which are similar to ZIP code regions) may not be entirely within a single state or county, so they don't have a well-defined state and county. In these cases, the `state_fips` `stusab` and `county_fips` columns will be empty.

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/index.html>)
  * [Homepage](<https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html>) Page with links to all of the files


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

boundary_schema   


### boundary_schema

Column Name| Data Type| Description  
---|---|---  
geoid| string| ACS style geoid  
name| string| Name of region  
stusab| string| US state abbreviation  
state_fips| integer| State FIPS code  
county_fips| integer| County FIPS code  
land_area| integer| Land area, in square meters  
water_area| integer| Water area, in square meters  
geometry| string| Geometry in WKT format.  
  
## References

Urls used in the creation of this data package.

  * **shape+https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_state_500k.zip**. State boundaries, scale 500K:1
  * **shape+https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_state_5m.zip**. State boundaries, scale 5M:1
  * **shape+https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_state_20m.zip**. State boundaries, scale 20M:1
  * **shape+https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_county_500k.zip**. County boundaries, scale 500K:1
  * **shape+https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_county_5m.zip**. County boundaries, scale 5M:1
  * **shape+https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_county_20m.zip**. County boundaries, scale 20M:1
  * **shape+https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_nation_5m.zip**. National boundary, 5M:1
  * **shape+https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_nation_20m.zip**. National boundary 20M:1
  * **shape+https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_zcta510_500k.zip**. ZCTA (Zip Codes), scale 500K:1


## Packages

  * **s3** s3://library.metatab.org/census.gov-boundaries-2018-1.2.8.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8.csv>
  * **source** <https://github.com/CivicKnowledge/tablecloth.io.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    state_500k_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/state_500k.csv')
    state_5m_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/state_5m.csv')
    state_20m_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/state_20m.csv')
    county_500k_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/county_500k.csv')
    county_5m_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/county_5m.csv')
    county_20m_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/county_20m.csv')
    nation_5m_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/nation_5m.csv')
    nation_20m_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/nation_20m.csv')
    zcta_500k_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8/data/zcta_500k.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018-1.2.8.csv')
    
    # Create Dataframes
    state_500k_gdf = pkg.resource('state_500k').geoframe()
    state_5m_gdf = pkg.resource('state_5m').geoframe()
    state_20m_gdf = pkg.resource('state_20m').geoframe()
    county_500k_gdf = pkg.resource('county_500k').geoframe()
    county_5m_gdf = pkg.resource('county_5m').geoframe()
    county_20m_gdf = pkg.resource('county_20m').geoframe()
    nation_5m_gdf = pkg.resource('nation_5m').geoframe()
    nation_20m_gdf = pkg.resource('nation_20m').geoframe()
    zcta_500k_gdf = pkg.resource('zcta_500k').geoframe()
    
[/code]
