---
title: "Starbucks Locations"
date: 2021-02-24T05:31:02+00:00
draft: false
categories: ["Dataset"]
tags: ["chrismeller.github.com"]
author: "metapack"
description: "A list of Starbucks locations, scraped from the web in 2017"
---

_A list of Starbucks locations, scraped from the web in 2017_

`chrismeller.github.com-starbucks-2.1.1`. Modified 2021-04-02T14:52:09

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[all_starbucks](<http://s3.amazonaws.com/radius.civicknowledge.com/chrismeller.github.com-starbucks-2.1.1/data/all_starbucks.csv>)**. List of Starbucks locations.
  * **[us_starbucks](<http://s3.amazonaws.com/radius.civicknowledge.com/chrismeller.github.com-starbucks-2.1.1/data/us_starbucks.csv>)**. Geo file of starbucks in the US


## Documentation

Starbucks locations scraped from the Starbucks website by Chris Meller. From the original README:
[code] 
    Contains a single commit for each day that batches up all changes to the
    Starbucks dataset as a CSV file.
    
    Deletes will obviously be stores that seem to have closed and adds are new
    stores that have opened.
    
    This is a work in progress. There is additional data that needs to be
    included in this dataset and it needs to get properly automated so we hav e
    a regular commit daily at a particular time.
    
[/code]

This dataset release re-geocodes all of the addresses, for the `us_starbucks` dataset. The original datafile has lat and lon values truncated to 2 decimal places, about 1km in North America. The re-geocoded addressss are much more precise.

### Documentation Links

  * [Documentation Page](<http://s3.amazonaws.com/radius.civicknowledge.com/chrismeller.github.com-starbucks-2.1.1/index.html>)
  * [Source](<https://github.com/chrismeller/StarbucksLocations>) Github page for the datafile source


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

all_starbucks | us_starbucks   


### all_starbucks

Column Name| Data Type| Description  
---|---|---  
id| string|   
starbucksid| integer|   
name| text|   
brandname| string|   
storenumber| string|   
phonenumber| string|   
ownershiptype| string|   
street1| text|   
street2| text|   
street3| text|   
city| text|   
countrysubdivisioncode| string|   
countrycode| string|   
postalcode| string|   
longitude| number|   
latitude| number|   
timezoneoffset| integer|   
timezoneid| string|   
timezoneolsonid| string|   
firstseen| datetime|   
lastseen| datetime|   
  
### us_starbucks

Column Name| Data Type| Description  
---|---|---  
id| string|   
starbucksid| integer|   
name| text|   
brandname| string|   
storenumber| string|   
phonenumber| string|   
ownershiptype| string|   
street1| string|   
street2| string|   
street3| string|   
city| string|   
countrysubdivisioncode| string|   
countrycode| string|   
postalcode| integer|   
source_longitude| number|   
source_latitude| number|   
timezoneoffset| integer|   
timezoneid| string|   
timezoneolsonid| string|   
firstseen| datetime|   
lastseen| datetime|   
geocoder| string|   
lat| number|   
lon| number|   
geoid| string|   
geometry| string|   
  
## References

Urls used in the creation of this data package.

  * **censusgeo://2019/5/US/state**. US States
  * **data/geocodes.csv**. geocoded addresses


## Packages

  * **s3** s3://radius.civicknowledge.com/chrismeller.github.com-starbucks-2.1.1.csv
  * **csv** <http://s3.amazonaws.com/radius.civicknowledge.com/chrismeller.github.com-starbucks-2.1.1.csv>
  * **source** <https://github.com/metatab-packages/chrismeller.github.com-starbucks.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    all_starbucks_df =  pd.read_csv('http://s3.amazonaws.com/radius.civicknowledge.com/chrismeller.github.com-starbucks-2.1.1/data/all_starbucks.csv')
    us_starbucks_df =  pd.read_csv('http://s3.amazonaws.com/radius.civicknowledge.com/chrismeller.github.com-starbucks-2.1.1/data/us_starbucks.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://s3.amazonaws.com/radius.civicknowledge.com/chrismeller.github.com-starbucks-2.1.1.csv')
    
    # Create Dataframes
    all_starbucks_df = pkg.resource('all_starbucks').dataframe()
    us_starbucks_gdf = pkg.resource('us_starbucks').geoframe()
    
[/code]
