---
title: "ZIP-Tract Crosswalk"
date: 2019-05-15T22:32:56+00:00
draft: false
categories: ["Dataset"]
tags: ["age-friendly-communities", "build_environment", "ckan"]
author: "metapack"
description: "Data files linking ZIP codes to 2010 Census tracts."
---

_Data files linking ZIP codes to 2010 Census tracts._

`OrderedDict([('time', '2016'), ('origin', 'huduser.gov'), ('dataset', 'zip-tract'), ('version', '2'), ('@value', 'huduser.gov-zip_tract-2016-2')])`

Resources | Packages | Documentation| Contacts

## Resources

  * **[zip-tract](<http://s3.amazonaws.com/library.metatab.org/huduser.gov-zip_tract-2016-2/data/zip-tract.csv>)**. ZIP to Tract crosswalk
  * **[tract-zip](<http://s3.amazonaws.com/library.metatab.org/huduser.gov-zip_tract-2016-2/data/tract-zip.csv>)**. Tract to ZIP crosswalk


## Documentation

### Documentation Links

  * [https://www.huduser.gov/portal/datasets/usps_crosswalk.html](<Homepage>)
  * [docs/codebook.html](<Codebook>)


## Contacts

  * **Origin**

[U.S. Department of Housing and Urban Development](<https://www.huduser.gov>)

  * **Creator**

[Robert Renner](<mailto:Robert.N.Renner@hud.gov>), [U.S. Department of Housing and Urban Development](<https://www.huduser.gov>)

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **xlsx** <http://s3.amazonaws.com/library.metatab.org/huduser.gov-zip_tract-2016-2.xlsx>
  * **zip** <http://s3.amazonaws.com/library.metatab.org/huduser.gov-zip_tract-2016-2.zip>
  * **csv** <http://s3.amazonaws.com/library.metatab.org/huduser.gov-zip_tract-2016-2.csv>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('http://s3.amazonaws.com/library.metatab.org/huduser.gov-zip_tract-2016-2.zip')
    # CSV Package
    pkg = mp.open_package('http://s3.amazonaws.com/library.metatab.org/huduser.gov-zip_tract-2016-2.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

Last Modified 2017-04-03T19:58:57
