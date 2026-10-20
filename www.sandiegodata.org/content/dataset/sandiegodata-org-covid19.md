---
title: "COVID-19 Cases For San Diego County"
date: 2020-03-22T17:43:47+00:00
draft: false
categories: ["covid19", "Dataset"]
tags: ["covid19", "sandiegodata.org"]
author: "metapack"
description: "Cases, deaths, hospitalizations and other data scraped from the San Diego COunty"
---

_Cases, deaths, hospitalizations and other data scraped from the San Diego COunty COVID-19 website._

`sandiegodata.org-covid19-1.2.43`. Modified 2020-04-27T05:49:38

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[sd_covid_cases](<http://library.metatab.org/sandiegodata.org-covid19-1.2.43/data/sd_covid_cases.csv>)**. Notebook for creating dataset.


## Documentation

This dataset is manually extracted from the daily updates to the [San Diego County Coronavirus Disease 2019 (COVID-19)](<https://www.sandiegocounty.gov/coronavirus/>) web page. The table on the web page is pulled into a [Google Spreadsheet](<https://docs.google.com/spreadsheets/d/1RkgOAgmZIcq7WdNvxn4dih_-aX6
im3fNd9yrfM1-0Ys/edit?usp=sharing>), and this dataset extracts the Summary tab of the Google spreadsheet.

## Caveats

  * The County changes the table format ocassionally, often adding columns, to not all variables are available for all dates. 
  * This dataset does not include the information for age groups that is available in the source tables. 
  * The `cases` value for March 14 is created by interpolating ( exponential ) from the values before and after it.


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **s3** s3://library.metatab.org/sandiegodata.org-covid19-1.2.43.csv
  * **csv** <http://library.metatab.org/sandiegodata.org-covid19-1.2.43.csv>
  * **source** <https://github.com/sandiegodata/covid19.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/sandiegodata.org-covid19-1.2.43.csv')
    
    # Create Dataframes
    
    sd_covid_cases_df = pkg.resource('sd_covid_cases').dataframe()
[/code]

## Data Dictionary

sd_covid_cases   


### sd_covid_cases

Column Name| Data Type| Description  
---|---|---  
date| date|   
cases| integer| Number of confirmed infections  
cases_male| integer| Number of case in males  
cases_female| integer| Number of cases in females  
hospitalized| integer| Number of hospitalizations  
intensive_care| integer| Number in intensive_care  
deaths| integer| Number of deaths  
notes| string| Notes on each days values.  
  
## References

Urls used in the creation of this data package.

  * **[spreadsheet](<https://docs.google.com/spreadsheets/d/1RkgOAgmZIcq7WdNvxn4dih_-aX6im3fNd9yrfM1-0Ys/edit#gid=1588490640>)**. Google spreadsheet, for humans
  * **gs:1RkgOAgmZIcq7WdNvxn4dih_-aX6im3fNd9yrfM1-0Ys#1588490640**. Machine readable source file


## Packages

  * **s3** s3://library.metatab.org/sandiegodata.org-covid19-1.2.43.csv
  * **csv** <http://library.metatab.org/sandiegodata.org-covid19-1.2.43.csv>
  * **source** <https://github.com/sandiegodata/covid19.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/sandiegodata.org-covid19-1.2.43.csv')
    
    # Create Dataframes
    
    sd_covid_cases_df = pkg.resource('sd_covid_cases').dataframe()
[/code]
