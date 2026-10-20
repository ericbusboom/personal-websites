---
title: "COVID19 Data scraped from global sources"
date: 2020-03-23T22:05:03+00:00
draft: false
categories: ["covid19", "Dataset"]
tags: ["coronadatascraper.com", "covid19"]
author: "metapack"
description: "A very conprehensive collection of automatically scraped data."
---

_A very conprehensive collection of automatically scraped data._

`coronadatascraper.com-covid19-1.2.24`. Modified 2020-07-08T15:54:25

Resources | Packages | Documentation| Contacts| Data Dictionary

## Resources

  * **[source_tidy](<http://library.metatab.org/coronadatascraper.com-covid19-1.2.24/data/source_tidy.csv>)**. Scraped coronavirus data, with one row for each type of observation.
  * **[source_jhu](<http://library.metatab.org/coronadatascraper.com-covid19-1.2.24/data/source_jhu.csv>)**. Scraped coronavirus data, in format similar to JHU
  * **[source](<http://library.metatab.org/coronadatascraper.com-covid19-1.2.24/data/source.csv>)**. Scraped coronavirus data, with one row per region per day and one type of observation per column.


## Documentation

The [Corona Data Scraper](<https://coronadatascraper.com/#home>) scrapes data from a wide variety of sources to produce a dataset with both global scope and regional granularity. See the project page for more details.

### Documentation Links

  * [homepage](<https://coronadatascraper.com/#home>) Project homepage, sith links to files and documentation
  * [Documentation Page](<http://library.metatab.org/coronadatascraper.com-covid19-1.2.24/index.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

source_tidy | source | source_jhu   


### source_tidy

Column Name| Data Type| Description  
---|---|---  
name| text|   
level| string|   
city| string| City Name  
county| string| County Name  
state| text| State Name  
country| string| Country code  
population| integer| Total population of the region  
lat| number| Latitude  
long| number| Longitude  
aggregate| string|   
tz| string|   
date| date| Observation Date  
type| string| Type of observation: cases, deaths, recovered or active  
value| number| Value of the observatoin.  
  
### source

Column Name| Data Type| Description  
---|---|---  
name| text|   
level| string|   
city| string| City Name  
county| string| County Name  
state| text| State Name  
country| string| Country code  
population| number| Total population of the region  
lat| number| Latitude  
long| number| Longitude  
url| string| Source Url  
aggregate| string|   
tz| string|   
cases| integer| Sum of deaths, recoveries and active.  
deaths| integer| Cumulative number of deaths  
recovered| integer| Cumulative number of recoveries  
active| integer| Cumulative number of active confirmed infections.  
tested| integer| Number tested  
growthfactor| number| Growth factor, compared to previous observation. 1+ growth rate  
date| date| Observation Date  
  
### source_jhu

Column Name| Data Type| Description  
---|---|---  
name| text|   
level| string|   
city| string|   
county| text|   
state| text|   
country| text|   
lat| number|   
long| number|   
population| integer|   
url| string|   
aggregate| string|   
tz| string|   
2020_01_22| integer|   
2020_01_23| integer|   
2020_01_24| integer|   
2020_01_25| integer|   
2020_01_26| integer|   
2020_01_27| integer|   
2020_01_28| integer|   
2020_01_29| integer|   
2020_01_30| integer|   
2020_01_31| integer|   
2020_02_01| integer|   
2020_02_02| integer|   
2020_02_03| integer|   
2020_02_04| integer|   
2020_02_05| integer|   
2020_02_06| integer|   
2020_02_07| integer|   
2020_02_08| integer|   
2020_02_09| integer|   
2020_02_10| integer|   
2020_02_11| integer|   
2020_02_12| integer|   
2020_02_13| integer|   
2020_02_14| integer|   
2020_02_15| integer|   
2020_02_16| integer|   
2020_02_17| integer|   
2020_02_18| integer|   
2020_02_19| integer|   
2020_02_20| integer|   
2020_02_21| integer|   
2020_02_22| integer|   
2020_02_23| integer|   
2020_02_24| integer|   
2020_02_25| integer|   
2020_02_26| integer|   
2020_02_27| integer|   
2020_02_28| integer|   
2020_02_29| integer|   
2020_03_01| integer|   
2020_03_02| integer|   
2020_03_03| integer|   
2020_03_04| integer|   
2020_03_05| integer|   
2020_03_06| integer|   
2020_03_07| integer|   
2020_03_08| integer|   
2020_03_09| integer|   
2020_03_10| integer|   
2020_03_11| integer|   
2020_03_12| integer|   
2020_03_13| integer|   
2020_03_14| integer|   
2020_03_15| integer|   
2020_03_16| integer|   
2020_03_17| integer|   
2020_03_18| integer|   
2020_03_19| integer|   
2020_03_20| integer|   
2020_03_21| integer|   
2020_03_22| integer|   
2020_03_23| integer|   
2020_03_24| integer|   
2020_03_25| integer|   
2020_03_26| integer|   
2020_03_27| integer|   
2020_03_28| integer|   
2020_03_29| integer|   
2020_03_30| integer|   
2020_03_31| integer|   
2020_04_01| integer|   
2020_04_02| integer|   
2020_04_03| integer|   
2020_04_04| integer|   
2020_04_05| integer|   
2020_04_06| integer|   
2020_04_07| integer|   
2020_04_08| integer|   
2020_04_09| integer|   
2020_04_10| integer|   
2020_04_11| integer|   
2020_04_12| integer|   
2020_04_13| integer|   
2020_04_14| integer|   
2020_04_15| integer|   
2020_04_16| integer|   
2020_04_17| integer|   
2020_04_18| integer|   
2020_04_19| integer|   
2020_04_20| integer|   
2020_04_21| integer|   
2020_04_22| integer|   
2020_04_23| integer|   
2020_04_24| integer|   
  
## Packages

  * **s3** s3://library.metatab.org/coronadatascraper.com-covid19-1.2.24.csv
  * **csv** <http://library.metatab.org/coronadatascraper.com-covid19-1.2.24.csv>
  * **source** <https://github.com/sandiegodata/covid19.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    source_tidy_df =  pd.read_csv('http://library.metatab.org/coronadatascraper.com-covid19-1.2.24/data/source_tidy.csv')
    source_jhu_df =  pd.read_csv('http://library.metatab.org/coronadatascraper.com-covid19-1.2.24/data/source_jhu.csv')
    source_df =  pd.read_csv('http://library.metatab.org/coronadatascraper.com-covid19-1.2.24/data/source.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/coronadatascraper.com-covid19-1.2.24.csv')
    
    # Create Dataframes
    source_tidy_df = pkg.resource('source_tidy').dataframe()
    source_jhu_df = pkg.resource('source_jhu').dataframe()
    source_df = pkg.resource('source').dataframe()
    
[/code]
