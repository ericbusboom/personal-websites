---
title: "COVID 19 Statistics San Diego County"
date: 2020-04-29T17:31:11+00:00
draft: false
categories: ["covid19", "Dataset"]
tags: ["covid19", "sandiegocounty.gov"]
author: "metapack"
description: "Official COVID-19 statistics for San Diego County."
---

_Official COVID-19 statistics for San Diego County._

`sandiegocounty.gov-covid19-1.1.40`. Modified 2020-08-14T18:09:29

Resources | Packages | Documentation| Contacts| Data Dictionary

## Resources

  * **[covid_stats](<http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40/data/covid_stats.csv>)**. COVID-19 cases in San Diego County, by sex and age
  * **[covid_jurisdiction](<http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40/data/covid_jurisdiction.csv>)**. COVID-19 cases by San Diego jurisdiction
  * **[covid_jurisdiction_geo](<http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40/data/covid_jurisdiction_geo.csv>)**. COVID-19 cases by San Diego jurisdiction, geographic
  * **[covid_zip](<http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40/data/covid_zip.csv>)**. COVID-19 cases by zip code
  * **[covid_zip_geo](<http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40/data/covid_zip_geo.csv>)**. COVID-19 cases by zip code, geographic


## Documentation

### Documentation Links

  * [Documentation Page](<http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40/index.html>)
  * [Homepage](<http://sdgis-sandag.opendata.arcgis.com/datasets/covid-19-statistics-san-diego-county>) One of the pages linking to COVID-19 data posted on arcgis.com


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)

  * **Origin**

County of San Diego, Health and Human Services Agency, Public Health Services, Epidemiology and Immunization Services Branch


## Data Dictionary

covid_stats | covid_jurisdiction | covid_jurisdiction_geo | covid_zip | covid_zip_geo   


### covid_stats

Column Name| Data Type| Description  
---|---|---  
x| number|   
y| number|   
fid| integer|   
date| datetime|   
tests| integer|   
positives| integer|   
hospitalized| integer|   
icu| integer|   
deaths| integer|   
newcases| integer|   
age_9| integer|   
age10_19| integer|   
age40_49| integer|   
age50_59| integer|   
age60_69| integer|   
age70_79| integer|   
age80_plus| integer|   
ageunknow| integer|   
age20_29| integer|   
genderfemale| integer|   
gendermale| integer|   
gendeunk| integer|   
age30_39| integer|   
globalid| string|   
newtests| integer|   
  
### covid_jurisdiction

Column Name| Data Type| Description  
---|---|---  
x| number|   
y| number|   
fid| integer|   
name| string|   
loctype| string|   
lastupdate| datetime|   
confirmedcases| integer|   
globalid| string|   
  
### covid_jurisdiction_geo

Column Name| Data Type| Description  
---|---|---  
id| integer|   
fid| integer|   
name| string|   
loctype| string|   
lastupdate| date|   
confirmedc| integer|   
globalid| string|   
geometry| string|   
  
### covid_zip

Column Name| Data Type| Description  
---|---|---  
x| number|   
y| number|   
fid| integer|   
zipcode_zip| integer|   
ziptext| integer|   
case_count| integer|   
updatedate| datetime|   
created_date| datetime|   
created_user| string|   
last_edited_date| datetime|   
last_edited_user| string|   
globalid| string|   
  
### covid_zip_geo

Column Name| Data Type| Description  
---|---|---  
id| integer|   
fid| integer|   
zipcode_zi| integer|   
ziptext| integer|   
case_count| integer|   
updatedate| date|   
created_da| date|   
created_us| string|   
last_edite| date|   
last_edi_1| string|   
globalid| string|   
geometry| string|   
  
## Packages

  * **s3** s3://library.metatab.org/sandiegocounty.gov-covid19-1.1.40.csv
  * **csv** <http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40.csv>
  * **source** <https://github.com/sandiegodata/covid19.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    covid_stats_df =  pd.read_csv('http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40/data/covid_stats.csv')
    covid_jurisdiction_df =  pd.read_csv('http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40/data/covid_jurisdiction.csv')
    covid_jurisdiction_geo_df =  pd.read_csv('http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40/data/covid_jurisdiction_geo.csv')
    covid_zip_df =  pd.read_csv('http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40/data/covid_zip.csv')
    covid_zip_geo_df =  pd.read_csv('http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40/data/covid_zip_geo.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/sandiegocounty.gov-covid19-1.1.40.csv')
    
    # Create Dataframes
    covid_stats_df = pkg.resource('covid_stats').dataframe()
    covid_jurisdiction_df = pkg.resource('covid_jurisdiction').dataframe()
    covid_jurisdiction_geo_gdf = pkg.resource('covid_jurisdiction_geo').geoframe()
    covid_zip_df = pkg.resource('covid_zip').dataframe()
    covid_zip_geo_gdf = pkg.resource('covid_zip_geo').geoframe()
    
[/code]
