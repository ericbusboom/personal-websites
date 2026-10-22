---
title: "Raw San Diego County Crime Incidents, 2007- 2013"
date: 2019-05-15T22:27:49+00:00
draft: false
categories: ["Crime_Data", "Dataset"]
tags: ["autogen", "crime", "crime_data_collection", "law_enforcement", "police", "sandag.org"]
author: "metapack"
description: "Unprocessed crime incident files from SANDAG"
---

_Unprocessed crime incident files from SANDAG_

`sandag.org-crime-2017e2013-raw-1.1.1`. Modified 2020-11-22T22:18:08

Resources | Packages | Documentation| Contacts| Data Dictionary

## Resources

  * **[crime_2007_2013](<https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2017e2013-raw-1.1.1/data/crime_2007_2013.csv>)**. San Diego crime incidents, 2007 to 2013


## Documentation

**NOTE: These are original files from SANDAG. You probably want to work with the[cleaned version](<http://data.sandiegodata.org/dataset/clarinova_com-crime-incidents-casnd-7ba4-extract>).**

Crime incidents obtained from SANDAG through PRA request 12-075, presented as zipped CSV files. The request was for 1.5M incident records, and was delivered in April of 2013. Records start on Jan 1, 2007 and end on 31 March, 2013, for about 1008525 records.

These records are not cleaned, processed or geocoded. As is, they will only be useful for either further cleaning, or for time-series analysis.

This a later extract of the same data as in [Revision 1](<http://data.sandiegodata.org/dataset/raw-san-diego-county-crime-incidents-2007-2013-rev-1>). Revision one is being kept for historical comparisons; this data set is probably the one you want.

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2017e2013-raw-1.1.1/index.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@sandiegodata.org>), [San Diego Regional Data Library](<http://www.sandiegodata.org>)


## Data Dictionary

crime_2007_2013   


### crime_2007_2013

Column Name| Data Type| Description  
---|---|---  
activitytype| string|   
agency| string|   
activitydate| datetime|   
legend| string|   
charge_description| string|   
block_address| text|   
city_name| string|   
zipcode| integer|   
  
## Packages

  * **s3** s3://library.metatab.org/sandag.org-crime-2017e2013-raw-1.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2017e2013-raw-1.1.1.csv>
  * **source** <https://github.com/metatab-packages/sandag.org-crime-2017e2013-raw.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    crime_2007_2013_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2017e2013-raw-1.1.1/data/crime_2007_2013.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandag.org-crime-2017e2013-raw-1.1.1.csv')
    
    # Create Dataframes
    crime_2007_2013_df = pkg.resource('crime_2007_2013').dataframe()
    
[/code]
