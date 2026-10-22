---
title: "San Diego Roads"
date: 2019-06-13T04:42:44+00:00
draft: false
categories: ["build_environment", "Dataset", "planning", "planning-collection"]
tags: ["build_environment", "planning", "planning-collection", "sangis.org"]
author: "metapack"
description: "Extract from the Sangis Roads_all file, for roads in San Diego city"
---

_Extract from the Sangis Roads_all file, for roads in San Diego city_

`sangis.org-roads-sandiego-1`


## Resources

  * **[all_roads](<https://library-metatab-org.s3.amazonaws.com/sangis.org-roads-sandiego-1/data/all_roads.csv>)**. Original all roads file


## Documentation

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/sangis.org-roads-sandiego-1.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sangis.org-roads-sandiego-1.csv>
  * **source** <https://github.com/SDRDLAnalysts/data-projects.git>


### Accessing Packages in Metapack
```
import metapack as mp
# ZIP Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sangis.org-roads-sandiego-1.zip')
# CSV Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sangis.org-roads-sandiego-1.csv') 

resource = pkg.resource('resource_name') # Get a resource
df = resource.dataframe() # Create a pandas Dataframe
gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
```

## Data Dictionary

all_roads   


### all_roads

Column Name| Data Type| Description  
---|---|---  
id| integer|   
fnode| integer|   
tnode| integer|   
length| number|   
roadsegid| integer|   
postid| string|   
postdate| date|   
roadid| integer|   
rightway| integer|   
addsegdt| date|   
segstat| string|   
dedstat| string|   
funclass| string|   
oneway| string|   
subdivid| integer|   
segclass| string|   
ljurisdic| string|   
llowaddr| integer|   
lhighaddr| integer|   
rjurisdic| string|   
rlowaddr| integer|   
rhighaddr| integer|   
lmixaddr| string|   
rmixaddr| string|   
pending| string|   
abloaddr| integer|   
abhiaddr| integer|   
nad83n| number|   
nad83e| number|   
speed| integer|   
l_zip| integer|   
r_zip| integer|   
lpsjur| string|   
rpsjur| string|   
carto| string|   
obmh| string|   
firedriv| string|   
l_block| integer|   
r_block| integer|   
l_tract| integer|   
r_tract| integer|   
l_beat| integer|   
r_beat| integer|   
frxcoord| number|   
frycoord| number|   
midxcoord| number|   
midycoord| number|   
toxcoord| number|   
toycoord| number|   
f_level| integer|   
t_level| integer|   
l_psblock| integer|   
r_psblock| integer|   
rd20pred| string|   
rd20name| string|   
rd20sfx| string|   
rd20full| string|   
rd30pred| string|   
rd30name| string|   
rd30sfx| string|   
rd30postd| unknown|   
rd30full| string|   
shape_stle| number|   
geometry| string|   
  
Last Modified 2019-06-03T22:44:12
