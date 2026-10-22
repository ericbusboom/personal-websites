---
title: "San Diego County Total Maximum Daily Load"
date: 2019-05-15T22:32:21+00:00
draft: false
categories: ["Dataset"]
tags: ["ceden.waterboards.ca.gov", "ckan", "natural-environment", "water-project"]
author: "metapack"
description: "TMDL data for San Diego county, through September 2015."
---

_TMDL data for San Diego county, through September 2015._

`ceden.waterboards.ca.gov-tmdl-sandiego-2`

Resources | Packages | Documentation| Contacts

## Resources

  * **[tmdl-sd](<https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-tmdl-sandiego-2/data/tmdl-sd.csv>)**. San Diego Total Maximum Daily Load data


## Documentation

### Documentation Links

  * [https://ceden.waterboards.ca.gov/AdvancedQueryTool](<source_page>)CEDEN advanced query tool page
  * [https://www.waterboards.ca.gov/sandiego/water_issues/programs/tmdls/bacteria.html](<overview>)Overview of TMDL project


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **csv** <https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-tmdl-sandiego-1.csv>
  * **zip** <https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-tmdl-sandiego-2.zip>
  * **source** <https://github.com/san-diego-water-quality/water-datasets.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-tmdl-sandiego-2.zip')
    # CSV Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-tmdl-sandiego-1.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

Last Modified 2018-08-09T14:59:16
