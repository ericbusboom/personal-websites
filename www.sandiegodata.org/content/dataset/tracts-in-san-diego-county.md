---
title: "Tracts in San Diego County"
date: 2019-05-15T22:32:40+00:00
draft: false
categories: ["Dataset"]
tags: ["census.gov", "ckan"]
author: "metapack"
description: "<!-- wp:paragraph --> <p><em></em></p> <!-- /wp:paragraph -->  <!-- wp:paragraph --> <p><code>census.gov-tracts-2017-sandiego-1</code></p> <!-- /wp:paragraph -->  <!-- wp:paragraph --> <p>&lt;a href=&"
---

__

`census.gov-tracts-2017-sandiego-1`

Resources | Packages | Documentation| Contacts

## Resources

  * **[tracts](<https://library-metatab-org.s3.amazonaws.com/census.gov-tracts-2017-sandiego-1/data/tracts.csv>)**. 


## Documentation

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **csv** <https://library-metatab-org.s3.amazonaws.com/census.gov-tracts-2017-sandiego-1.csv>
  * **zip** <https://library-metatab-org.s3.amazonaws.com/census.gov-tracts-2017-sandiego-1.zip>
  * **source** <https://github.com/san-diego-water-quality/water-datasets.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/census.gov-tracts-2017-sandiego-1.zip')
    # CSV Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/census.gov-tracts-2017-sandiego-1.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

Last Modified 2018-08-09T14:59:41
