---
title: "SEZ Lights, Rings and Buffers"
date: 2021-09-08T22:56:54+00:00
draft: false
categories: ["Dataset", "sez"]
tags: ["sandiegodata.org", "sez", "special_economic_zones"]
author: "metapack"
description: "Sums of pixel values representing nighttime light intensit, for buffers and"
---

_Sums of pixel values representing nighttime light intensit, for buffers and rings around Special Economic Zones._

`sandiegodata.org-sez_lights-1.1.2`. Modified 2021-09-13T20:27:23

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[mean_lights](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sez_lights-1.1.2/data/mean_lights.csv>)**. Pixel light sums for buffers and rings around the SEZ.


## Documentation

This dataset provides sums of the pixel values in the [nighttime lights data](<http://data.sandiegodata.org/dataset/figshare-com-harmonized-ntl/>) in regions around the SEZs from the [World Bank's SEZ dataset](<http://data.sandiegodata.org/dataset/worldbank-org-sez/>). The buffers are a circle for a specified radius around each SEZ, and the rings have a minimum radius of the specific radius, and a maximum radius of (1+sqrt(2)) times larger, so the area of the ring for a radius is equal to the area of the buffer circle.

Here is an example of the buffer and ring for an SEZ in South Korea:

![](https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sez_lights-1.1.2/doc/ring_raster.png)

This file can be joined to the SEZ data on the `unique_id` column. For each SEZ and year of the NTL data, this file includes the sum of the pixel values from the NTL rasters for both the ring and the buffer, and the radius specified in the `radius` column. The `*_count` column is the number of non-null pixels in each region.

## Example Analysis

See this [Jupyter notebook](<https://github.com/sandiegodata-projects/chartercitiesinstitute.org-sez/blob/master/notebooks/ericbusboom/05%20Mean%20Lights%20File.ipynb>) for an example of using this file.

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sez_lights-1.1.2/index.html>)


## Images

  * [![](https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sez_lights-1.1.2/doc/ring_raster.png)](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sez_lights-1.1.2/doc/ring_raster.png> "Rings & Rasters") Example of a 5km buffer and the ring around it.


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

mean_lights   


### mean_lights

Column Name| Data Type| Description  
---|---|---  
year| integer| Year of night time lights data  
unique_id| string| Unique id for the SEZ  
buffer_pix_sum| integer| Sum of the pixel values for pixels within radius of SEZ point  
buffer_pix_count| integer| Number of non-null pixels in buffer region  
ring_pix_sum| integer| Sum of pixel values in ring area, outsize of buffer area. Area of ring is equal to area of the buffer.  
ring_pix_count| integer| Number of non-null pixels in ring region  
buffer_area| number| Area of buffer area in square meters  
ring_area| number| Area of ring area in square meters  
radius| integer| Radius of buffer circle, and inner radius of ring.  
  
## References

Urls used in the creation of this data package.

  * **metapack+https://library-metatab-org.s3.amazonaws.com/worldbank.org-sez-1.1.1.csv#sez**. SEZ Locations and data
  * **metapack+https://library-metatab-org.s3.amazonaws.com/figshare.com-harmonized_ntl-1.1.1.csv**. Harmonized Nighttime lights


## Packages

  * **s3** s3://library.metatab.org/sandiegodata.org-sez_lights-1.1.2.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sez_lights-1.1.2.csv>
  * **source** <https://github.com/metatab-packages/sandiegodata.org-sez_lights.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    mean_lights_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sez_lights-1.1.2/data/mean_lights.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-sez_lights-1.1.2.csv')
    
    # Create Dataframes
    mean_lights_df = pkg.resource('mean_lights').dataframe()
    
[/code]
