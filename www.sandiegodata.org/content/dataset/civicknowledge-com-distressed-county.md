---
title: "Distressed Tracts By County"
date: 2020-06-23T04:50:48+00:00
draft: false
categories: ["Dataset"]
tags: ["civicknowledge.com"]
author: "metapack"
description: "Counts of FFEIC distressed tracts, by county."
---

_Counts of FFEIC distressed tracts, by county._

`civicknowledge.com-distressed-county-1.1.5`. Modified 2020-08-12T04:36:30

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[distressed_counties](<https://library-metatab-org.s3.amazonaws.com/civicknowledge.com-distressed-county-1.1.5/data/distressed_counties.csv>)**. Aggregation of FFEIC distressed tracts into counties


## Documentation

The [FFEIC publishes a very large dataset of Census variables](<https://www.ffiec.gov/censusapp.htm>) and flags indicating ways in which housing and populations in tracts are distressed. This dataset aggregates those tract flags into counts of distressed tracts per county.

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/civicknowledge.com-distressed-county-1.1.5/index.html>)


## Images

  * [![](https://library-metatab-org.s3.amazonaws.com/civicknowledge.com-distressed-county-1.1.5/doc/sample.png)](<https://library-metatab-org.s3.amazonaws.com/civicknowledge.com-distressed-county-1.1.5/doc/sample.png> "Distressed Population") Percentage of Poverty Distressed Population Per County


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

distressed_counties   


### distressed_counties

Column Name| Data Type| Description  
---|---|---  
geoid| string| County geoid  
stusab| string| State postal abbreviation  
state| integer| State FIPS code  
county| integer| County FIPS code  
year| integer| Year values were observed  
current_prior_distressed| integer| Count of tracts in county with flag: Meets at least one of current or previous year's CRA distressed/underserved tract criteria? 'X' - Yes, ' ' (blank space) - No  
current_prior_distressed_pct| number| Percentage of tracts in county with flag: Meets at least one of current or previous year's CRA distressed/underserved tract criteria? 'X' - Yes, ' ' (blank space) - No  
current_prior_distressed_pop| integer| Population in county in tracts with flag: Meets at least one of current or previous year's CRA distressed/underserved tract criteria? 'X' - Yes, ' ' (blank space) - No  
current_prior_distressed_pop_pct| number| Percentage of population in county in tracts with flag: Meets at least one of current or previous year's CRA distressed/underserved tract criteria? 'X' - Yes, ' ' (blank space) - No  
last_year_distressed| integer| Count of tracts in county with flag: Meets at least one of the previous year's CRA distressed criteria? 'X' - Yes , ' ' (blank space) - No  
last_year_distressed_pct| number| Percentage of tracts in county with flag: Meets at least one of the previous year's CRA distressed criteria? 'X' - Yes , ' ' (blank space) - No  
last_year_distressed_pop| integer| Population in county in tracts with flag: Meets at least one of the previous year's CRA distressed criteria? 'X' - Yes , ' ' (blank space) - No  
last_year_distressed_pop_pct| number| Percentage of population in county in tracts with flag: Meets at least one of the previous year's CRA distressed criteria? 'X' - Yes , ' ' (blank space) - No  
last_year_underserved| integer| Count of tracts in county with flag: Meets previous year's CRA underserved criterion? 'X' - Yes , ' ' (blank space) - No  
last_year_underserved_pct| number| Percentage of tracts in county with flag: Meets previous year's CRA underserved criterion? 'X' - Yes , ' ' (blank space) - No  
last_year_underserved_pop| integer| Population in county in tracts with flag: Meets previous year's CRA underserved criterion? 'X' - Yes , ' ' (blank space) - No  
last_year_underserved_pop_pct| number| Percentage of population in county in tracts with flag: Meets previous year's CRA underserved criterion? 'X' - Yes , ' ' (blank space) - No  
population_distressed| integer| Count of tracts in county with flag: Total persons  
population_distressed_pct| number| Percentage of tracts in county with flag: Total persons  
population_distressed_pop| integer| Population in county in tracts with flag: Total persons  
population_distressed_pop_pct| number| Percentage of population in county in tracts with flag: Total persons  
poverty_distressed| integer| Count of tracts in county with flag: Meets current year's poverty CRA distressed criterion? 'X' - Yes , ' ' (blank space) - No  
poverty_distressed_pct| number| Percentage of tracts in county with flag: Meets current year's poverty CRA distressed criterion? 'X' - Yes , ' ' (blank space) - No  
poverty_distressed_pop| integer| Population in county in tracts with flag: Meets current year's poverty CRA distressed criterion? 'X' - Yes , ' ' (blank space) - No  
poverty_distressed_pop_pct| number| Percentage of population in county in tracts with flag: Meets current year's poverty CRA distressed criterion? 'X' - Yes , ' ' (blank space) - No  
rural_underserved| integer| Count of tracts in county with flag: Meets current year's remote rural (low density) CRA underserved criterion? 'X' -Yes, ' ' (blank space) - No  
rural_underserved_pct| number| Percentage of tracts in county with flag: Meets current year's remote rural (low density) CRA underserved criterion? 'X' -Yes, ' ' (blank space) - No  
rural_underserved_pop| integer| Population in county in tracts with flag: Meets current year's remote rural (low density) CRA underserved criterion? 'X' -Yes, ' ' (blank space) - No  
rural_underserved_pop_pct| number| Percentage of population in county in tracts with flag: Meets current year's remote rural (low density) CRA underserved criterion? 'X' -Yes, ' ' (blank space) - No  
unemployment_distressed| integer| Count of tracts in county with flag: Meets current year's unemployment CRA distressed criterion? 'X' - Yes , ' ' (blank space) - No  
unemployment_distressed_pct| number| Percentage of tracts in county with flag: Meets current year's unemployment CRA distressed criterion? 'X' - Yes , ' ' (blank space) - No  
unemployment_distressed_pop| integer| Population in county in tracts with flag: Meets current year's unemployment CRA distressed criterion? 'X' - Yes , ' ' (blank space) - No  
unemployment_distressed_pop_pct| number| Percentage of population in county in tracts with flag: Meets current year's unemployment CRA distressed criterion? 'X' - Yes , ' ' (blank space) - No  
  
## References

Urls used in the creation of this data package.

  * **metapack+https://library-metatab-org.s3.amazonaws.com/ffeic.gov-census-tract.csv#ffeic_distressed**. Flags indicating FFEIC "distressed" designations, per tract.
  * **metapack+https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018.csv#county_500k**. County Boundaries


## Packages

  * **s3** s3://library.metatab.org/civicknowledge.com-distressed-county-1.1.5.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/civicknowledge.com-distressed-county-1.1.5.csv>
  * **source** <https://github.com/CivicKnowledge/tablecloth.io-collection.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    distressed_counties_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/civicknowledge.com-distressed-county-1.1.5/data/distressed_counties.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/civicknowledge.com-distressed-county-1.1.5.csv')
    
    # Create Dataframes
    distressed_counties_df = pkg.resource('distressed_counties').dataframe()
    
[/code]
