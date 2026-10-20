---
title: "State and County COVID-19 Cases"
date: 2020-03-23T22:05:25+00:00
draft: false
categories: ["covid19", "Dataset"]
tags: ["covid19", "covidtracking.com"]
author: "metapack"
description: "State and country observations from the Covid Tracking Project"
---

_State and country observations from the Covid Tracking Project_

`covidtracking.com-covid19-3.1.51`. Modified 2020-07-08T04:54:16

Resources | Packages | Documentation| Contacts| Data Dictionary

## Resources

  * **[states](<http://library.metatab.org/covidtracking.com-covid19-3.1.51/data/states.csv>)**. Cumulative cases, deaths, hospitalizations, etc for US states


## Documentation

The COVID Tracking Project collects information from 50 US states, the District of Columbia, and 5 other US territories to provide the most comprehensive testing data we can collect for the novel coronavirus, SARS-CoV-2. They attempt to include positive and negative results, pending tests, and total people tested for each state or district currently reporting that data.

### Documentation Links

  * [Documentation Page](<http://library.metatab.org/covidtracking.com-covid19-3.1.51/index.html>)
  * [Homepage](<https://covidtracking.com/>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

counties | states   


### counties

Column Name| Data Type| Description  
---|---|---  
state| string|   
county| string|   
covid19site| string|   
datasite| unknown|   
mainsite| string|   
twitter| unknown|   
pui| string|   
  
### states

Column Name| Data Type| Description  
---|---|---  
date| integer|   
state| string|   
positive| integer|   
negative| integer|   
pending| integer|   
hospitalizedcurrently| integer|   
hospitalizedcumulative| integer|   
inicucurrently| integer|   
inicucumulative| integer|   
onventilatorcurrently| integer|   
onventilatorcumulative| integer|   
recovered| integer|   
hash| string|   
datechecked| datetime|   
death| integer|   
hospitalized| integer|   
total| integer|   
totaltestresults| integer|   
posneg| integer|   
fips| integer|   
deathincrease| integer|   
hospitalizedincrease| integer|   
negativeincrease| integer|   
positiveincrease| integer|   
totaltestresultsincrease| integer|   
  
## Packages

  * **s3** s3://library.metatab.org/covidtracking.com-covid19-3.1.51.csv
  * **csv** <http://library.metatab.org/covidtracking.com-covid19-3.1.51.csv>
  * **source** <https://github.com/sandiegodata/covid19.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    states_df =  pd.read_csv('http://library.metatab.org/covidtracking.com-covid19-3.1.51/data/states.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/covidtracking.com-covid19-3.1.51.csv')
    
    # Create Dataframes
    states_df = pkg.resource('states').dataframe()
    
[/code]
