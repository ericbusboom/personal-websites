---
title: "Links between LA Tracts and Land Use Codes"
date: 2019-05-15T22:33:55+00:00
draft: false
categories: ["Dataset"]
tags: ["ckan", "sandiegodata.org"]
author: "metapack"
description: "<!-- wp:paragraph --> <p><em></em></p> <!-- /wp:paragraph -->  <!-- wp:paragraph --> <p><code>sandiegodata.org-la_parcels-2</code></p> <!-- /wp:paragraph -->  <!-- wp:paragraph --> <p>&lt;a href=&quot"
---

__

`sandiegodata.org-la_parcels-2`


## Resources

  * **[la-planning-code](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-la_parcels-2/data/la-planning-code.csv>)**. 
  * **[tract_to_parcels](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-la_parcels-2/data/tract_to_parcels.csv>)**. 


## Documentation

Static files for links between LA parcels and LA tracts. 

See the notebooks directory for the code bits thatgenerated the files. They are slow and take a lot of memory, since there are about 2M parcels in the file

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-la_parcels-2.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-la_parcels-2.csv>
  * **source** <https://github.com/SDRDLAnalysts/data-projects.git>


### Accessing Packages in Metapack
```
import metapack as mp
# ZIP Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-la_parcels-2.zip')
# CSV Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-la_parcels-2.csv') 

resource = pkg.resource('resource_name') # Get a resource
df = resource.dataframe() # Create a pandas Dataframe
gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
```

## References

Urls used in the creation of this data package.

  * **[la_land_use](<http://gisdata-scag.opendata.arcgis.com/datasets/general-plan-land-use-los-angeles>)**. Download page for the LA Land Use File


Last Modified 2019-01-21T04:10:42
