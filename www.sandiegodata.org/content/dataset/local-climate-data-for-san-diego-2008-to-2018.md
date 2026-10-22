---
title: "Local Climate Data For San Diego 2008 to 2018"
date: 2019-05-15T22:33:17+00:00
draft: false
categories: ["Dataset"]
tags: ["ckan", "natural-environment", "noaa.gov", "water-project"]
author: "metapack"
description: "<!-- wp:paragraph --> <p><em></em></p> <!-- /wp:paragraph -->  <!-- wp:paragraph --> <p><code>noaa.gov-localclimate-200808_201807-san-4</code></p> <!-- /wp:paragraph -->  <!-- wp:paragraph --> <p>&lt;"
---

__

`noaa.gov-localclimate-200808_201807-san-4`

Resources | Packages | Documentation| Contacts

## Resources

  * **[lcd-san](<https://library-metatab-org.s3.amazonaws.com/noaa.gov-localclimate-200808_201807-san-4/data/lcd-san.csv>)**. Local climate data for San Diego


## Documentation

This dataset is an extract from the NOAA's Local Climatological Data, via the online tool. 

  * Station: WBAN:23188 ( San Diego ) 
  * Begin Date: 2008-08-01 00:00
  * End Date: 2018-07-05 23:59


### Documentation Links

  * [https://www1.ncdc.noaa.gov/pub/data/cdo/documentation/LCD_documentation.pdf](<documentation>)Local Climatological Data (LCD) Dataset Documentation


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **csv** <https://library-metatab-org.s3.amazonaws.com/noaa.gov-localclimate-200808_201807-san-4.csv>
  * **zip** <https://library-metatab-org.s3.amazonaws.com/noaa.gov-localclimate-200808_201807-san-4.zip>
  * **source** <https://github.com/san-diego-water-quality/water-datasets.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/noaa.gov-localclimate-200808_201807-san-4.zip')
    # CSV Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/noaa.gov-localclimate-200808_201807-san-4.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

Last Modified 2018-08-09T14:59:58
