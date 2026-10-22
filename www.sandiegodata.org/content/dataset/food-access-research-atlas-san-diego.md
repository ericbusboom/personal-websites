---
title: "Food Access Research Atlas, San Diego"
date: 2019-05-15T22:34:46+00:00
draft: false
categories: ["Dataset"]
tags: ["ckan", "planning-project", "usda.gov"]
author: "metapack"
description: "The Atlas presents spatial data about supermarket accessibility and provides"
---

_The Atlas presents spatial data about supermarket accessibility and provides census-tract level data for food access_

`usda.gov-food_access-1`


## Resources

  * **[sd_food_atlas](<https://library-metatab-org.s3.amazonaws.com/usda.gov-food_access-1/data/sd_food_atlas.csv>)**. Food atlas, San Diego county tracts only


## Documentation

The Food Access Research Atlas:

  * Presents a spatial overview of food access indicators for low-income and other census tracts using different measures of supermarket accessibility;
  * Provides food access data for populations within census tracts; and
  * Offers census-tract-level data on food access that can be downloaded for community planning or research purposes.


This version of the Atlas dataset has only tracts in San Diego couny, and tract identifiers have been converted from Tiger format Geoids to ACS format. 

## What can you do with the Atlas?

  * Create maps showing food access indicators by census tract using different measures and indicators of supermarket accessibility;
  * Compare food access measures based on 2015 data with the previous 2010 measures;
  * View indicators of food access for selected subpopulations; and
  * Download census-tract-level data on food access measures.


# Processing Notes

While the URL for the source file is available online, this data package is produced from the CSV file saved from the Excel source, because large Excel files are very slow to load and process. The file's source URL is included in the References section of the metadata.

### Documentation Links

  * [https://www.ers.usda.gov/data-products/food-access-research-atlas/](<Homepage>)
  * [https://www.ers.usda.gov/webdocs/DataFiles/80591/documentation.pdf?v=0](<Documentation>)Documentation from last year; current year documentation not available.


## Contacts

  * **Creator**

[Michele Ver Ploeg](<mailto:sverploeg@ers.usda.gov>), [USDA Economic Research Service](<https://www.ers.usda.gov/authors/ers-staff-directory/michele-ver-ploeg/>)

  * **Creator**

[Vince Breneman](<mailto:breneman@ers.usda.gov>), [USDA Economic Research Service](<https://www.ers.usda.gov/authors/ers-staff-directory/vince-breneman/>)

  * **Creator**

[Alana Rhone](<mailto:alana.y.rhone@ers.usda.gov>), [USDA Economic Research Service](<https://www.ers.usda.gov/authors/ers-staff-directory/alana-rhone/>)

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/usda.gov-food_access-1.zip>
  * **source** <https://github.com/Metatab/metatab-packages.git>


### Accessing Packages in Metapack
```
import metapack as mp
# ZIP Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/usda.gov-food_access-1.zip')


resource = pkg.resource('resource_name') # Get a resource
df = resource.dataframe() # Create a pandas Dataframe
gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
```

## References

Urls used in the creation of this data package.

  * **[food_atlas_url](<https://www.ers.usda.gov/webdocs/DataFiles/80591/DataDownload2015.xlsx?v=0>)**. 
  * **file:data/food_atlas.csv# &encoding=ascii**. Food atlas, with tracts for whole US


Last Modified 2018-09-21T22:18:34
