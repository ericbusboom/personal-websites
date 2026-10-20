---
title: "Gaslamp Homeless Counts"
date: 2019-10-01T00:12:22+00:00
draft: false
categories: ["Dataset", "homelessness"]
tags: ["downtownsandiego.org", "homelessness"]
author: "metapack"
description: "Monthly homeless counts for the Gaslamp district in Downtown San Diego"
---

_Monthly homeless counts for the Gaslamp district in Downtown San Diego_

`downtownsandiego.org-homeless_count-gaslamp-2`

Resources | Packages | Documentation| Contacts| Data Dictionary

## Resources

  * **[gaslamp](<http://library.metatab.org/downtownsandiego.org-homeless_count-gaslamp-2/data/gaslamp.csv>)**. 


## Documentation

Since 2014, the Downtown San Diego Partnership has been conducting monthly counts of the homeless in the Downtown neighborhood. The positions of homeless sleepers are recorded on paper maps, which are compiled into a spreadsheet. The San Diego Regional Data Library is running a project to digitize these paper maps](https://downtown-homelesness.sandiegodata.org/) into geographic datasets.

This dataset covers only the Gaslamp district, from 2014-01-01 to 2018-06-28. 

The data were digitized by students of Corri-Anne Burgess at Kearney Senior High as a year-end class project. The digitization procedure involved estimateing the positions of each point from a PDF scan of the each map, placing the digitized point on a map in a web form. Although the procedure is less accurate that traditional digitization points, spot checking suggests the additional digitization error is much less than the positional error of the original data collection and recording, and the result is suficient to place each point to a parcel.

## Corrections

Corrections made during wranging include: 

  * One point for map 42 was given the incorrect date of 2019-05-26, which was corrected to 2017005-26
  * The value "individual_sleeper" was shortened to 'ind'
  * In the rain column, the value 'na' was replaced with blanks.


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <http://library.metatab.org/downtownsandiego.org-homeless_count-gaslamp-2.zip>
  * **csv** <http://library.metatab.org/downtownsandiego.org-homeless_count-gaslamp-2.csv>
  * **source** <https://github.com/sandiegodata-projects/downtown-partnership.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('http://library.metatab.org/downtownsandiego.org-homeless_count-gaslamp-2.zip')
    # CSV Package
    pkg = mp.open_package('http://library.metatab.org/downtownsandiego.org-homeless_count-gaslamp-2.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

## Data Dictionary

gaslamp   


### gaslamp

Column Name| Data Type| Description  
---|---|---  
id| integer|   
date| date|   
neighborhood| string| Neighborhood name; always 'gaslamp'  
map_id| integer| Map number  
type| string| Type of group: 'ind' for individuals, or 'encampment'  
count| integer| Number of homeless people in the count point  
rain| string| Does the map record rain? 'yes', 'no' or blank if no record  
temperature| string| Temperature in F, if recorded on the map  
lon| number| Longitude of count point  
lat| number| Latitude of count point  
  
Last Modified 2019-09-30T22:07:44
