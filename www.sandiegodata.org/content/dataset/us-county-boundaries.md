---
title: "US County Boundaries"
date: 2019-05-15T22:32:37+00:00
draft: false
categories: ["Dataset"]
tags: ["built_environment", "census.gov", "ckan"]
author: "metapack"
description: "US county boundaries 500k resolution."
---

_US county boundaries 500k resolution._

`census.gov-counties-2017-2`

Resources | Packages | Documentation| Contacts

## Resources

  * **[counties](<https://library-metatab-org.s3.amazonaws.com/census.gov-counties-2017-2/data/counties.csv>)**. 


## Documentation

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **csv** <https://library-metatab-org.s3.amazonaws.com/census.gov-counties-2017-2.csv>
  * **zip** <https://library-metatab-org.s3.amazonaws.com/census.gov-counties-2017-2.zip>
  * **source** <https://github.com/san-diego-water-quality/water-datasets.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/census.gov-counties-2017-2.zip')
    # CSV Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/census.gov-counties-2017-2.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

Last Modified 2018-08-09T14:59:28
