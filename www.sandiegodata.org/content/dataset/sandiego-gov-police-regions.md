---
title: "San Diego Police Regions and Demographics"
date: 2019-12-04T00:15:52+00:00
draft: false
categories: ["Crime_Data", "Dataset", "Police Data", "police_data_collection"]
tags: ["crime", "Crime_Data", "law_enforcement", "police", "police_data_collection", "sandiego.gov"]
author: "metapack"
description: "Boundary shapes for San Diego neighborhoods, beats and divisions, with ACS 2019"
---

_Boundary shapes for San Diego neighborhoods, beats and divisions, with ACS 2019 estimates for populations, by race._

`sandiego.gov-police_regions-2.1.2`. Modified 2021-02-25T19:08:44

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[pd_beats](<http://library.metatab.org/sandiego.gov-police_regions-2.1.2/data/pd_beats.csv>)**. Police beats
  * **[pd_divisions](<http://library.metatab.org/sandiego.gov-police_regions-2.1.2/data/pd_divisions.csv>)**. Police Divisions
  * **[pd_neighborhoods](<http://library.metatab.org/sandiego.gov-police_regions-2.1.2/data/pd_neighborhoods.csv>)**. Police Neighborhoods
  * **[beat_demographics](<http://library.metatab.org/sandiego.gov-police_regions-2.1.2/data/beat_demographics.csv>)**. Counts of people in the beat, by race.


## Documentation

This package links shapefiles for San Diego police beats to Census tracts and merges in ACS estimates for population, by race, from the 2016 5 year ACS. When a police beat boundry crosses a tract, the tract population is allocated to beats by the proportion of the overlap by area. See the [Jupyter notebook](<https://nbviewer.jupyter.org/github/metatab-packages/sandiego.gov-police_regions/blob/master/notebooks/BeatPopulations.ipynb>) that performs the procedure for details.

For the race/ethicty statistics, Hispanic ('hisp') refers to Hispanics of any race, while all other races refer to non-Hispanics of that race.

### Documentation Links

  * [Documentation Page](<http://library.metatab.org/sandiego.gov-police_regions-2.1.2/index.html>)
  * [Police Divisions Repository Page](<https://data.sandiego.gov/datasets/pd-divisions/>) Data repository page that links to original files.


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

beat_demographics | pd_beats | pd_divisions | pd_neighborhoods   


### beat_demographics

Column Name| Data Type| Description  
---|---|---  
beat| integer| Beat number  
total| integer| Total population of beat  
white| integer| White population of beat  
black| integer| Black population of beat  
aian| integer| American Indian population of beat  
asian| integer| Asian population of beat  
nhopi| integer| Hawaiian population of beat  
hisp| integer| Hispanic population of beat  
  
### pd_beats

Column Name| Data Type| Description  
---|---|---  
objectid| integer|   
beat| integer|   
div| integer|   
serv| integer|   
name| string|   
geometry| string|   
  
### pd_divisions

Column Name| Data Type| Description  
---|---|---  
objectid| integer|   
div_num| integer|   
div_name| string|   
geometry| string|   
  
### pd_neighborhoods

Column Name| Data Type| Description  
---|---|---  
objectid| integer|   
div_num| integer|   
div_name| string|   
geometry| string|   
  
## References

Urls used in the creation of this data package.

  * **censusgeo://2019/5/CA/tract**. Census tracts from 2016 5 year ACS, for San Diego county
  * **census://2019/5/CA/tract/B03002**. Race, by tract, in San Diego county
  * **shape+http://seshat.datasd.org/sde/pd/pd_beats_datasd.zip**. Police beats
  * **shape+http://seshat.datasd.org/sde/pd/pd_divisions_datasd.zip**. Police Divisions
  * **shape+http://seshat.datasd.org/sde/pd/pd_divisions_datasd.zip**. Police Neighborhoods


## Packages

  * **s3** s3://library.metatab.org/sandiego.gov-police_regions-2.1.2.csv
  * **csv** <http://library.metatab.org/sandiego.gov-police_regions-2.1.2.csv>
  * **source** <https://github.com/metatab-packages/sandiego.gov-police_regions.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    pd_beats_df =  pd.read_csv('http://library.metatab.org/sandiego.gov-police_regions-2.1.2/data/pd_beats.csv')
    pd_divisions_df =  pd.read_csv('http://library.metatab.org/sandiego.gov-police_regions-2.1.2/data/pd_divisions.csv')
    pd_neighborhoods_df =  pd.read_csv('http://library.metatab.org/sandiego.gov-police_regions-2.1.2/data/pd_neighborhoods.csv')
    beat_demographics_df =  pd.read_csv('http://library.metatab.org/sandiego.gov-police_regions-2.1.2/data/beat_demographics.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/sandiego.gov-police_regions-2.1.2.csv')
    
    # Create Dataframes
    pd_beats_gdf = pkg.resource('pd_beats').geoframe()
    pd_divisions_gdf = pkg.resource('pd_divisions').geoframe()
    pd_neighborhoods_gdf = pkg.resource('pd_neighborhoods').geoframe()
    beat_demographics_df = pkg.resource('beat_demographics').dataframe()
    
[/code]
