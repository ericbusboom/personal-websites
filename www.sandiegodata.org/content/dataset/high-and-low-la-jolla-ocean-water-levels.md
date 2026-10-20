---
title: "High and Low La Jolla Ocean Water Levels"
date: 2019-05-15T22:34:44+00:00
draft: false
categories: ["Dataset"]
tags: ["ckan", "tidesandcurrents.noaa.gov", "water-project"]
author: "metapack"
description: "High and Low ocean water levels, at the La Jolla station, from year 2000 to"
---

_High and Low ocean water levels, at the La Jolla station, from year 2000 to present._

`tidesandcurrents.noaa.gov-water_levels-la_jolla-1`

Resources | Packages | Documentation| Contacts| References

## Resources

  * **[water_levels](<http://library.metatab.org/tidesandcurrents.noaa.gov-water_levels-la_jolla-1/data/water_levels.csv>)**. High and Low Ocean water levels for the La Jolla station.


## Documentation

## Access URls

To get the access URLs, visit the [web tool page](<https://tidesandcurrents.noaa.gov/waterlevels.html?id=9410230&bdate=20180628&edate=20180630&interval=hl>) and click on the "Show Data Listing" button. This will display a table. On the right side of the table, click the button "Web Services". This will pop up a dialog with URLs. On the line for "Water Levels" right click on the "CSV" badge and copy the URL.

### Documentation Links

  * [https://tidesandcurrents.noaa.gov/waterlevels.html?id=9410230&bdate=20180628&edate=20180630&interval=hl](<Data Access Page>)Web tool for exploring water level data


## Images

  * <http://library.metatab.org/tidesandcurrents.noaa.gov-water_levels-la_jolla-1/docs/water_levels.png>

## Contacts

    * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)

## Packages

    * **zip** <http://library.metatab.org/tidesandcurrents.noaa.gov-water_levels-la_jolla-1.zip>
    * **csv** <http://library.metatab.org/tidesandcurrents.noaa.gov-water_levels-la_jolla-1.csv>
    * **source** <https://github.com/san-diego-water-quality/water-datasets.git>

### Accessing Packages in Metapack
[code] import metapack as mp
    # ZIP Package
    pkg = mp.open_package('http://library.metatab.org/tidesandcurrents.noaa.gov-water_levels-la_jolla-1.zip')
    # CSV Package
    pkg = mp.open_package('http://library.metatab.org/tidesandcurrents.noaa.gov-water_levels-la_jolla-1.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

## References

Urls used in the creation of this data package.

    * **[url_template](<https://tidesandcurrents.noaa.gov/api/datagetter?product=high_low&application=NOS.COOPS.TAC.WL&begin_date={year}0101&end_date={year}1231&datum=MLLW&station=9410230&time_zone=GMT&units=english&format=csv>)**. 

Last Modified 2018-08-09T15:00:12
