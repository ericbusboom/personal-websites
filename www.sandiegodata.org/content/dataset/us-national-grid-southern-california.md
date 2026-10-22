---
title: "US National Grid, Southern California"
date: 2019-05-15T22:34:49+00:00
draft: false
categories: ["Dataset"]
tags: ["ckan", "usngcenter.org"]
author: "metapack"
description: "UTM Grid Zone 11"
---

_UTM Grid Zone 11_

`usngcenter.org-usng-ca11-1`

Resources | Packages | Documentation| Contacts

## Resources

  * **[ca11_usng](<https://library-metatab-org.s3.amazonaws.com/usngcenter.org-usng-ca11-1/data/ca11_usng.csv>)**. US National Grid for California, Zone 11


## Documentation

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **csv** <https://library-metatab-org.s3.amazonaws.com/usngcenter.org-usng-ca11-1.csv>
  * **zip** <https://library-metatab-org.s3.amazonaws.com/usngcenter.org-usng-ca11-1.zip>
  * **source** <https://github.com/san-diego-water-quality/water-datasets.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/usngcenter.org-usng-ca11-1.zip')
    # CSV Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/usngcenter.org-usng-ca11-1.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

Last Modified 2018-08-09T15:00:34
