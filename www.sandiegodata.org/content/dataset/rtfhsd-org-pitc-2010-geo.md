---
title: "San Diego Point In Time Count 2010, Geo Points"
date: 2019-07-17T21:26:38+00:00
draft: false
categories: ["Dataset", "homelessness"]
tags: ["homelessness", "planning-project", "rtfhsd.org", "san_diego"]
author: "metapack"
description: "Point data for locations of homeless for the 2010 PiTC count in San Diego"
---

_Point data for locations of homeless for the 2010 PiTC count in San Diego county._

`rtfhsd.org-pitc-2010-geo-3`

Resources | Packages | Documentation| Contacts| Data Dictionary

## Resources

  * **[pitc](<https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2010-geo-3/data/pitc.csv>)**. Point in time count geo data for 2010
  * **[tracts](<https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2010-geo-3/data/tracts.csv>)**. Counts per shelter type per tract


## Documentation

This dataset is a digitized version of the points recorded on paper maps for the 2010 Point in Time Count of the unsheltered homeless. The dataset was not provided with any documentation, and the organization that digitized the data is not known.

The datapackage also includes counts aggregated to tracts, per type of shelter.

## Contacts

  * **Creator**

[San Diego Regional Task Force for the Homeless](<https://www.rtfhsd.org/>)

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2010-geo-3.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2010-geo-3.csv>
  * **source** <https://github.com/SDRDLAnalysts/data-projects.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2010-geo-3.zip')
    
    # Create Dataframes
    pitc_gdf = pkg.resource('pitc').geoframe()
    
    tracts_df = pkg.resource('tracts').dataframe()
[/code]

## Data Dictionary

pitc | tracts   


### pitc

Column Name| Data Type| Description  
---|---|---  
id| integer|   
tract| string| Census Tract ID  
observe| string| Type of shelter  
municiplty| string| City  
locaccurac| string|   
geometry| string| Approximate point position of the observation  
  
### tracts

Column Name| Data Type| Description  
---|---|---  
tract| integer| Tract Geoid  
handbuilt| integer| Count of homeless in handbuilt structures  
individual| integer| Count of unsheltered homeless  
vehicle| integer| Count of homeless in vehicles  
total| integer| Total count of homeless in tract  
  
Last Modified 2019-07-17T21:30:37

## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2010-geo-3.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2010-geo-3.csv>
  * **source** <https://github.com/SDRDLAnalysts/data-projects.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2010-geo-3.zip')
    
    # Create Dataframes
    pitc_gdf = pkg.resource('pitc').geoframe()
    
    tracts_df = pkg.resource('tracts').dataframe()
[/code]
