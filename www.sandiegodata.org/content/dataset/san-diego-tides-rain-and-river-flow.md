---
title: "San Diego Tides, Rain and River Flow"
date: 2019-05-15T22:34:15+00:00
draft: false
categories: ["Dataset"]
tags: ["ckan", "sandiegodata.org", "water-project"]
author: "metapack"
description: "A combined dataset of NOAA weather reports, USGS flow rates for the Sn Diego"
---

_A combined dataset of NOAA weather reports, USGS flow rates for the Sn Diego River and NOAA tide levels for La Jolla._

`sandiegodata.org-tides_rain_river-6`

Resources | Packages | Documentation| Contacts| References

## Resources

  * **[tides_river_rain](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-tides_rain_river-6/data/tides_river_rain.csv>)**. Combined max, min tides, San Diego river flow and daily precipitation


## Documentation

This package combines three other datasets for use in the water quality data ptoject:
[code] 
    * waterservices.usgs.gov-stream_discharge-fashion_valley_sd
    * tidesandcurrents.noaa.gov-water_levels-la_jolla#water_levels
    * noaa.gov-localclimate-200808_201807-san#lcd-san
    
[/code]

The resulting dataset has daily values for rainfall, flow rate for the San Diego river, and the max and min tide level at La Jolla.

See the [EDA Notebook](<https://github.com/san-diego-water-quality/water-datasets/blob/master/derived/sandiegodata.org-tides_rain_river/notebooks/eda-tides_river_rain.ipynb>) for details of the structure of the data, in particular, the time coverage in the Nulls section.

# Versions

  1. Initial
  2. Continued development
  3. First release
  4. Added rolling averages
  5. Changed name


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-tides_rain_river-6.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-tides_rain_river-5.csv>
  * **source** <https://github.com/san-diego-water-quality/water-datasets.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-tides_rain_river-6.zip')
    # CSV Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-tides_rain_river-5.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

## References

Urls used in the creation of this data package.

  * **index:waterservices.usgs.gov-stream_discharge-fashion_valley_sd#fashion_valley**. Stream discharge rates for the San Diego River, Fashion Valley Station.
  * **index:tidesandcurrents.noaa.gov-water_levels-la_jolla#water_levels**. High and Low Ocean water levels for the La Jolla station.
  * **index:noaa.gov-localclimate-200808_201807-san#lcd-san**. Local climate data for San Diego


Last Modified 2018-08-15T23:43:08
