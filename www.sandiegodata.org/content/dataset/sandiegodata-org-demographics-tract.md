---
title: "San Diego Demographics By Tract"
date: 2020-11-26T02:47:34+00:00
draft: false
categories: ["Dataset"]
tags: ["sandiegodata.org"]
author: "metapack"
description: "Age, Race, Sex and Ethnicity, by tract for San Diego county"
---

_Age, Race, Sex and Ethnicity, by tract for San Diego county_

`sandiegodata.org-demographics-tract-1.1.1`. Modified 2020-11-26T02:47:27


## Resources

  * **[tracts](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-demographics-tract-1.1.1/data/tracts.csv>)**. San Diego county tract boundaries
  * **[age_sex](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-demographics-tract-1.1.1/data/age_sex.csv>)**. Age and sex per San Diego tract
  * **[total_populaltion](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-demographics-tract-1.1.1/data/total_populaltion.csv>)**. Total population of San Diego tracts
  * **[raceeth](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-demographics-tract-1.1.1/data/raceeth.csv>)**. Race and Ethnicity for SaN Diego tracts


## Documentation

The dataset includes three files all from the Census, detailing age and sex and race ethnicity. All of the files are built from Census data; see the References section for the specific dates and releases. 

## Age and Sex

The `age_sex` data comes from B01001 and the associated race iterations. The file combines all of the race iteration tables and adds columns for sex, race/ethnicity codes and age groups. 

THe race ethnicity codes are: 

  * white 
  * nhwhite
  * black
  * aian
  * asian
  * nhopi
  * other
  * many
  * hisp


For each of the race/ethnicity values except nhwhite and hisp, the category sums the associated 'nh__' and 'hisp__ ' categories from the raceeth table. 

## Race And Ethnicity

The `raceeth` is based on the census table [C03002: Hispanic or Latino Origin by Race](<https://censusreporter.org/tables/C03002/>), but recormats the structure, use a code for race/ethnicity in the `raceeth` column to indicate the oricinal clumn name in the Census dataset. These codes are: 

  * total: B03002_001 Total
  * nonhisp: B03002_002 Not Hispanic or Latino
  * nh_white: B03002_003 Not Hispanic or Latino - White alone
  * nh_black: B03002_004 Not Hispanic or Latino - Black or African American alone
  * nh_aian: B03002_005 Not Hispanic or Latino - American Indian and Alaska Native alone
  * nh_asian: B03002_006 Not Hispanic or Latino - Asian alone
  * nh_nhopi: B03002_007 Not Hispanic or Latino - Native Hawaiian and Other Pacific Islander alone
  * nh_other: B03002_008 Not Hispanic or Latino - Some other race alone
  * nh_multiple: B03002_009 Not Hispanic or Latino - Two or more races
  * nh_multiple_other: B03002_010 Not Hispanic or Latino - Two or more races - Two races including Some other race
  * nh_multiple_more: B03002_011 Not Hispanic or Latino - Two or more races - Two races excluding Some other race and three or more races
  * hisp: B03002_012 Hispanic or Latino
  * hisp_white: B03002_013 Hispanic or Latino - White alone
  * hisp_black: B03002_014 Hispanic or Latino - Black or African American alone
  * hisp_aian: B03002_015 Hispanic or Latino - American Indian and Alaska Native alone
  * hisp_asian: B03002_016 Hispanic or Latino - Asian alone
  * hisp_nhopi: B03002_017 Hispanic or Latino - Native Hawaiian and Other Pacific Islander alone
  * hisp_other: B03002_018 Hispanic or Latino - Some other race alone
  * hisp_multiple: B03002_019 Hispanic or Latino - Two or more races
  * hisp_multiple_other: B03002_020 Hispanic or Latino - Two or more races - Two races including Some other race
  * hisp_multiple_more: B03002_021 Hispanic or Latino - Two or more races - Two races excluding Some other race and three or more races


For the most part you will use the `nh_*` for all races, `hisp_white` for hispanics, and `nh_white` for whites.

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-demographics-tract-1.1.1/index.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

tracts | age_sex | total_populaltion | raceeth   


### tracts

Column Name| Data Type| Description  
---|---|---  
statefp| integer| State FIPS code  
countyfp| integer| County FIPS code  
tractce| integer| Census tract id  
geoid| string| Tract geoid  
name| number| Name of tract. Mostly useless.  
namelsad| string| Longer name for trace. More useless.  
mtfcc| string| Feature class code. https://www.census.gov/library/reference/code-lists/mt-feature-class-codes.html  
funcstat| string| Functional status. https://www.census.gov/library/reference/code-lists/functional-status-codes.html  
aland| integer| Area of land in square meters  
awater| integer| Area of water in square meters  
intptlat| number| Lattitude of an internal point, usually the centroid  
intptlon| number| Longitude of the internal point, usually the centroid  
geometry| string| Geometry of boundary, in WKT format.  
  
### age_sex

Column Name| Data Type| Description  
---|---|---  
geoid| string| Tract geoid  
column| string| ID of original census table column  
sex| string| Sex category  
age| string| Age group  
min_age| integer| Minimum age in age group  
max_age| integer| Maximum age in age group  
raceeth| string| Race/ethnicity.  
estimate| integer| Population estimate  
margin| integer| 90% margin of error  
  
### total_populaltion

Column Name| Data Type| Description  
---|---|---  
geoid| string| Tract geoid  
total_population| integer| Total population of tract  
total_popualtion_m90| integer| 90% margin of error of tract  
  
### raceeth

Column Name| Data Type| Description  
---|---|---  
geoid| string| Tract geoid  
raceeth| string| Race/ethnicity code  
estimate| integer| Population estimate  
margin| integer| 90% margin of error  
  
## References

Urls used in the creation of this data package.

  * **census://2018/5/CA/tract**. Census Tract boundaries for tracts in California
  * **census://2018/5/CA/tract/B01003**. Total tract population
  * **census://2018/5/CA/tract/b03002**. Hispanic or Latino Origin by Race


## Packages

  * **s3** s3://library.metatab.org/sandiegodata.org-demographics-tract-1.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-demographics-tract-1.1.1.csv>


### Accessing Data in Vanilla Pandas
```
import pandas as pd


tracts_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-demographics-tract-1.1.1/data/tracts.csv')
age_sex_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-demographics-tract-1.1.1/data/age_sex.csv')
total_populaltion_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-demographics-tract-1.1.1/data/total_populaltion.csv')
raceeth_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-demographics-tract-1.1.1/data/raceeth.csv')
```

### Accessing Package in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-demographics-tract-1.1.1.csv')

# Create Dataframes
tracts_gdf = pkg.resource('tracts').geoframe()
age_sex_df = pkg.resource('age_sex').dataframe()
total_populaltion_df = pkg.resource('total_populaltion').dataframe()
raceeth_df = pkg.resource('raceeth').dataframe()
```
