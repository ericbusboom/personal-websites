---
title: "Raw San Diego County Crime Incidents 2012-2017"
date: 2019-05-15T22:27:51+00:00
draft: false
categories: ["Crime_Data", "Dataset"]
tags: ["autogen", "crime", "crime_data_collection", "law_enforcement", "police", "sandag.org"]
author: "metapack"
description: "Unprocessed crime incident files from SANDAG"
---

_Unprocessed crime incident files from SANDAG_

`sandag.org-crime-2012e2017-raw-2.1.1`. Modified 2020-11-22T22:18:25

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[crime-incidents-2012](<https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/data/crime-incidents-2012.csv>)**. Crime Incidents 2012
  * **[crime-incidents-2013](<https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/data/crime-incidents-2013.csv>)**. Crime Incidents, 2013
  * **[crime-incidents-2014](<https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/data/crime-incidents-2014.csv>)**. Crime Incidents, 2014
  * **[crime-incidents-2015](<https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/data/crime-incidents-2015.csv>)**. Crime Incidents, 2015
  * **[crime-incidents-2016](<https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/data/crime-incidents-2016.csv>)**. Crime Incidents, 2016
  * **[crime-incidents-2017](<https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/data/crime-incidents-2017.csv>)**. Crime Incidents, 2017


## Documentation

These are files of crime incidents from SANDAG. These records come from two public records requests, one in 2016, and one in Feb 2019. The second request returned two files for 2015, which different numbers of records: 

  * 2015.xlsx 208854 records
  * 2015-2019-request.xlsx 165796


We don't know why the earlier request has more records.

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/index.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@sandiegodata.org>), [San Diego Regional Data Library](<http://www.sandiegodata.org>)


## Data Dictionary

crime-incidents   


### crime-incidents

Column Name| Data Type| Description  
---|---|---  
reportingYear| integer|   
reportingMonth| integer|   
agency| string|   
activityStatus| string|   
activitydate| datetime|   
numberActualReported| integer|   
BLOCK_ADDRESS| string|   
city| string|   
zipCode| integer|   
censusTract| integer|   
censusBlock| integer|   
CrimeCategory| string|   
CrimeDescription| string|   
  
## References

Urls used in the creation of this data package.

  * **[crime-incidents-2015-2019](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandag.org/2015-2019-request.xlsx>)**. A difference version of the 2015 data, from a reuestion in 2019


## Packages

  * **s3** s3://library.metatab.org/sandag.org-crime-2012e2017-raw-2.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1.csv>
  * **source** <https://github.com/metatab-packages/sandag.org-crime-2012e2017-raw.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    crime-incidents-2012_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/data/crime-incidents-2012.csv')
    crime-incidents-2013_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/data/crime-incidents-2013.csv')
    crime-incidents-2014_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/data/crime-incidents-2014.csv')
    crime-incidents-2015_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/data/crime-incidents-2015.csv')
    crime-incidents-2016_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/data/crime-incidents-2016.csv')
    crime-incidents-2017_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1/data/crime-incidents-2017.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2012e2017-raw-2.1.1.csv')
    
    # Create Dataframes
    crime-incidents-2012_df = pkg.resource('crime-incidents-2012').dataframe()
    crime-incidents-2013_df = pkg.resource('crime-incidents-2013').dataframe()
    crime-incidents-2014_df = pkg.resource('crime-incidents-2014').dataframe()
    crime-incidents-2015_df = pkg.resource('crime-incidents-2015').dataframe()
    crime-incidents-2016_df = pkg.resource('crime-incidents-2016').dataframe()
    crime-incidents-2017_df = pkg.resource('crime-incidents-2017').dataframe()
    
[/code]
