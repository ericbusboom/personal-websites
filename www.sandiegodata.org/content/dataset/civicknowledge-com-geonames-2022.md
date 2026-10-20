---
title: "Geographical Region Names"
date: 2023-02-21T01:41:35+00:00
draft: false
categories: ["Dataset", "Uncategorized"]
tags: ["civicknowledge.com"]
author: "metapack"
description: "Country names, and names for US countries, metros, cities and states."
---

_Country names, and names for US countries, metros, cities and states._

`civicknowledge.com-geonames-2022-1.2.43`. Modified 2023-02-23T18:37:42

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[names](<https://library.metatab.org/civicknowledge.com-geonames-2022-1.2.43/data/names.csv>)**. Geographic names


## Documentation

### Documentation Links

  * [Documentation Page](<https://library.metatab.org/civicknowledge.com-geonames-2022-1.2.43/index.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

names   


### names

Column Name| Data Type| Description  
---|---|---  
ref| string|   
geoid| string|   
category| string|   
weight| integer|   
name| text|   
  
## References

Urls used in the creation of this data package.

  * **[country_codes](<https://datahub.io/core/country-codes/r/country-codes.csv>)**. Country codes, from https://datahub.io/core/country-codes
  * **censusgeo://2022/5/US/state**. 
  * **censusgeo://2020/5/US/CBSA**. 
  * **censusgeo://2022/5/US/county**. 
  * **censusgeo://2020/5/{}/place**. 


## Packages

  * **s3** s3://library.metatab.org/civicknowledge.com-geonames-2022-1.2.43.csv
  * **csv** <https://library.metatab.org/civicknowledge.com-geonames-2022-1.2.43.csv>
  * **source** <https://github.com/metatab-packages/civicknowledge.com-geonames-2022.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    names_df =  pd.read_csv('https://library.metatab.org/civicknowledge.com-geonames-2022-1.2.43/data/names.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library.metatab.org/civicknowledge.com-geonames-2022-1.2.43.csv')
    
    # Create Dataframes
    names_df = pkg.resource('names').dataframe()
    
[/code]
