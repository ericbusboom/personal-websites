---
title: "Pedestrian Density By Block and Time"
date: 2019-10-09T00:16:40+00:00
draft: false
categories: ["Dataset"]
tags: ["sandiegodata.org"]
author: "metapack"
description: "Pedestrian densities, based on data from San Diego's CityIQ system, aggregated"
---

_Pedestrian densities, based on data from San Diego's CityIQ system, aggregated by city block, day of week and time of day._

`sandiegodata.org-pedestrian-blocks-1`

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[ped_blocks](<http://library.metatab.org/sandiegodata.org-pedestrian-blocks-1/data/ped_blocks.csv>)**. Pedestrian density per time by walkway, time of day and day of week
  * **[blocks](<http://library.metatab.org/sandiegodata.org-pedestrian-blocks-1/data/blocks.csv>)**. Geographic data for San Diego city census blocks


## Documentation

This datasets aggregates the `cityiq.io-pedestrians-san_diego` dataset by census block, time of day and day of week. The time of day is represented as:

  * morning: 6:00 to 11:00
  * lunch: 11:00 to 13:00
  * afternoon: 13:00 to 15:00
  * evening: 17:00 to 22:00
  * night: 22:00 to 6:00


Pedestrian densities are in terms of the average of the pedestrians per hour for the walkways in a block, but the density value should only be used as a relative value.

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <http://library.metatab.org/sandiegodata.org-pedestrian-blocks-1.zip>
  * **csv** <http://library.metatab.org/sandiegodata.org-pedestrian-blocks-1.csv>
  * **source** <https://github.com/sandiegodata-projects/downtown-partnership.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/sandiegodata.org-pedestrian-blocks-1.zip')
    
    # Create Dataframes
    
    ped_blocks_df = pkg.resource('ped_blocks').dataframe()blocks_gdf = pkg.resource('blocks').geoframe()
    
[/code]

## Data Dictionary

blocks | ped_blocks   


### blocks

Column Name| Data Type| Description  
---|---|---  
geoid| string| Block geoid  
geometry| string| Block geometry  
  
### ped_blocks

Column Name| Data Type| Description  
---|---|---  
geoid| string| Block geoid  
dow| integer| Day of week  
tod| string| Time of day  
density| number| Pedestrian density  
z| number| Density z-score  
rank| number| Density percentile / rank  
  
## References

Urls used in the creation of this data package.

  * **metapack+http://library.metatab.org/cityiq.io-pedestrians-san_diego-1.zip#pedestrians**. 
  * **metapack+http://library.metatab.org/cityiq.io-objects-san_diego-5.zip#walkways**. 
  * **shape+https://www2.census.gov/geo/pvs/tiger2010st/06_California/06073/tl_2010_06073_tabblock10.zip**. 2010 Census blocks for San Diego County


Last Modified 2019-10-08T23:05:23

## Packages

  * **zip** <http://library.metatab.org/sandiegodata.org-pedestrian-blocks-1.zip>
  * **csv** <http://library.metatab.org/sandiegodata.org-pedestrian-blocks-1.csv>
  * **source** <https://github.com/sandiegodata-projects/downtown-partnership.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/sandiegodata.org-pedestrian-blocks-1.zip')
    
    # Create Dataframes
    
    ped_blocks_df = pkg.resource('ped_blocks').dataframe()blocks_gdf = pkg.resource('blocks').geoframe()
    
[/code]
