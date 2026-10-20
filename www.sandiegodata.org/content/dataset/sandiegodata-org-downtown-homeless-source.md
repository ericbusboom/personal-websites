---
title: "Downtown Homelessness Source Package"
date: 2019-09-26T19:49:11+00:00
draft: false
categories: ["Dataset", "homelessness"]
tags: ["homelessness", "sandiegodata.org"]
author: "metapack"
description: "Source files for San Diego Downtown homeless sleeper counts"
---

_Source files for San Diego Downtown homeless sleeper counts_

`sandiegodata.org-downtown_homeless-source-7.2.3`. Modified 2024-11-26T06:18:18

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[intersections_2019](<https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/intersections_2019.csv>)**. Street intersections used for Ground Control Points, 2019
  * **[intersections_2023](<https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/intersections_2023.csv>)**. Street intersections used for Ground Control Points, 2023 update
  * **[counts](<https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/counts.csv>)**. Final homeless sleeper counts
  * **[files](<https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/files.csv>)**. Final file annotations, including total counts, temperature and weather.
  * **[gcp_transforms](<https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/gcp_transforms.csv>)**. Final ground control points and affine transformation matrices
  * **[raw_count_annotations](<https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/raw_count_annotations.csv>)**. Lightly processed count annotations
  * **[raw_file_annotations](<https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/raw_file_annotations.csv>)**. Lightly processed file annotations
  * **[raw_gcp](<https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/raw_gcp.csv>)**. Lightly processed Ground Control Points


## Documentation

This dataset provides geographic locations for homeless sleepers in Downtown San Diego, as counted by enumerators from the Downtown San Diego Partnership. These counts have been done monthly since 2012, and this dataset provides counts since 2014. 

This is the source package, use to generate analysis packages. Analysts should probably use one of the analysis packages. See the [Data Library's Homelessness Collection](<https://data.sandiegodata.org/collections/homelessness/>) for all of the available datasets. 

The count is done on paper maps with handwritten count marks. The San Diego Regional Data Library's [Downton Homelessness project](<http://downtown-homelessness.sandiegodata.org/>) converted these scanned count maps using a [web based image annotation tool, VIA](<http://www.robots.ox.ac.uk/~vgg/software/via/>). These data are extracted from the JSON output from VIA. 

This package has two top level files, and four predecessor files. The top level files are: 

  * `counts`. One record for each handwritten count marking on a map. 
  * `files`. One record for each of the scanned, handmarked maps. 


The predecessor files are: 

  * `raw_file_annotations`. File annotations extracted from the VIA output.
  * `raw_count_annotations`. Count annotations extracted from the VIA output.
  * `raw_gcp`. Ground control point annotations ( street intersections ) extracted from VIA.
  * `gcp_transforms`. Ground control points, in both image and geographic coordinates, with an affine transformation matrix to convert between them. 
  * `intersections`. Geographic positions and names of the street intersections used as ground control points. 


## Caveats

Because this data is extracted, manually, from manually recorded maps, there are a lot of quality issues. 

## Missing Months

Because of conversion errors and some complications with the source maps, there are several months of data that are excluded from this dataset

  * **August 2014**. In the original datasets, August 2014 was a duplicate of September 2014. 
  * **September 2014**. Comfusion related to the duplication of September and August resulted in September being incompletely processed. 
  * **June 2015**. All of the map images for this month were blank. An alternate source PDF exists that is not blank, but this file was not used. 


## Not Using Ocupancy Multipliers

Since about 2017, HUD has instructed point-in-time homeless counts to multiply the counts of sleepers in structures and vehicles by factors to account for people who may be obsured and not directly countable. From April 2017 on, Downtown San Diego Partnership has been using these factors.

However, this dataset does not use the occupancy factors, to allow analysts to apply these factors consistently across all months of data. As a result, the counts from this dataset diverge from the official counts after March 2017.

## Other Issues

  * The `total_count` often does not match the sum of counts on the map. These sums were made by hand, by the enumerator who made the counts, so there are occasional arithmetic errors. 
  * There are many instances of missing values for `rain` or `temp`
  * Some dates include the day of the month, but many don't These dates have a day of month of 1.
  * Date day of month is generally unreliable. Only the year and month are reliable, except for files noted above. 
  * The `neighborhood` value is based on the map names, so in some months the East Village neighborhood is separated into `east_village` and `east_village_south`


## Comparison to Official Published Counts

This plot shows, per month, the offical published counts from San Diego Downtown Partnership versus the total from this dataset. Note the discrepancies dues to issues noted above, including missing months, minor differences in some months, and the divergence after March 2017 due to occupancy multipliers. 

![](/uploads/6/2019/10/homeless-new-vs-official-1024x452.png)

## Versions

  1. Initial Release
  2. Remap some neighborhoods
  3. Map null neighborhood name ( '' ) to Gaslamp
  4. Fixed missing dates in Columbia, 2016, incorrect dates in Marina 2016, and other errors
  5. Excluded several months with quality problems, improved documentation
  6. Added column for source file, removed duplicated data form marina, 2016
  7. Added data for 2023 update.


## Acknowledgements

The May 2023 update was done by researchers at the Homelessness Hub at UC San Diego:

  * Zhongqi Zheng
  * Daniel Sjoholm
  * Yao Fu


The 2024 update was performed by:

  * Zhongqi Zheng
  * Daniel Sjoholm
  * Michael Yang
  * Patricia Estaris
  * Lily Keefauver *


### Documentation Links

  * [Documentation Page](<https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/index.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)

  * **Origin**

[Downtown San Diego Partnership](<https://downtownsandiego.org/>)


## Data Dictionary

counts | files | raw_file_annotations | gcp_transforms | raw_gcp | raw_count_annotations | intersections   


### counts

Column Name| Data Type| Description  
---|---|---  
file_id| string| Link to files table  
neighborhood| string| Neighborhood name  
date| date| Date of the count, or the first of the month if the day of the date isn't specified.  
count| integer| Number of sleepers counted in the observation  
type| string| "Individual", "Structure" or "Vehicle"  
x| number| Geographic X position, EPSG:2230, California State Plane 6  
y| number| Geographic Y position, EPSG:2230, California State Plane 6  
  
### files

Column Name| Data Type| Description  
---|---|---  
image_url| string| Url to the original scanned, hand-marked map  
file_id| string| Hash of image_url, to identify files.  
source_file| string| Source file for the annotation data  
url_year| integer| Year of the observation, from the URL to the image  
url_month| integer| Month of the observation, from the URL of the image  
date| date| Date of the observation, either from the annotation on the map, or from the URL.  
neighborhood| string| Neighborhood name  
url_neighborhood| string| Neighborhood name, from the URL  
total_count| number| Total count for all sleepers.  
temp| integer| Temperature, F  
rain| string| Rain or clear  
  
### raw_file_annotations

Column Name| Data Type| Description  
---|---|---  
image_url| string| Url to the original scanned, hand-marked map  
date| date| Date of the count, or the first of the month if the day of the date isn't specified.  
neighborhood| string| Neighborhood name  
total_count| number| Total count for all sleepers.  
temp| integer| Temperature, F  
rain| string| Rain or clear  
source_file| string| Source file for the annotation data  
  
### gcp_transforms

Column Name| Data Type| Description  
---|---|---  
url| string| Url to the original scanned, hand-marked map  
neighborhood| string| Neighborhood name  
source| string| The intersection polygon, formed from the intersection points, in WKT format, in the pixel coordinate space. This version is inverted from the coordinates of the image, with the Y coordinate being subtracted from 2000, so the orientation of the Y axis is the same as the EPSG:2230 geographic coordinate space.  
dest| string| The intersection polygon, but in EPSG:2230 (State plane 6, California, Feet) coordinates.  
matrix| string| An affine transformation matrix that transforms from the coordinates of source_inv to dest. When pixel locations are properly inverted, this matrix transforms from pixel locations to geographic locations.  
  
### raw_gcp

Column Name| Data Type| Description  
---|---|---  
image_url| string| Url to the original scanned, hand-marked map  
x| integer| X position of upper left of region rectangle, in pixels  
y| integer| Y position of upper left of region rectangle, in pixels  
width| integer| Width of selection region rectangle in pixels  
height| integer| Height of selection region rectangle in pixels  
intersection| string| Name of intersection  
  
### raw_count_annotations

Column Name| Data Type| Description  
---|---|---  
image_url| string| Url to the original scanned, hand-marked map  
cx| integer| X value of the center of the circle region, in pixels  
cy| integer| Y value of the center of the circle region in pixels  
r| number| Radius of the circle region, in pixels  
type| string| Type of sleeper: Individual, Vehicle or Structure  
count| integer| Count of sleepers  
  
### intersections

Column Name| Data Type| Description  
---|---|---  
geometry| string| Point position of center of intersection, EPSG:2230, California State Plane 6  
neighborhood| string| Neighborhood name  
intersection| string| Intersection name  
  
## References

Urls used in the creation of this data package.

  * **data/2019**. Source directory for 2019 files
  * **data/2023/SDDT_102923/output**. Source directory for 2023 files


## Packages

  * **s3** s3://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3.csv
  * **csv** <https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3.csv>
  * **source** <https://github.com/metatab-packages/sandiegodata.org-downtown_homeless-source.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    intersections_2019_df =  pd.read_csv('https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/intersections_2019.csv')
    intersections_2023_df =  pd.read_csv('https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/intersections_2023.csv')
    counts_df =  pd.read_csv('https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/counts.csv')
    files_df =  pd.read_csv('https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/files.csv')
    gcp_transforms_df =  pd.read_csv('https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/gcp_transforms.csv')
    raw_count_annotations_df =  pd.read_csv('https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/raw_count_annotations.csv')
    raw_file_annotations_df =  pd.read_csv('https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/raw_file_annotations.csv')
    raw_gcp_df =  pd.read_csv('https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3/data/raw_gcp.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library.metatab.org/sandiegodata.org-downtown_homeless-source-7.2.3.csv')
    
    # Create Dataframes
    intersections_2019_gdf = pkg.resource('intersections_2019').geoframe()
    intersections_2023_gdf = pkg.resource('intersections_2023').geoframe()
    counts_df = pkg.resource('counts').dataframe()
    files_df = pkg.resource('files').dataframe()
    gcp_transforms_df = pkg.resource('gcp_transforms').dataframe()
    raw_count_annotations_df = pkg.resource('raw_count_annotations').dataframe()
    raw_file_annotations_df = pkg.resource('raw_file_annotations').dataframe()
    raw_gcp_df = pkg.resource('raw_gcp').dataframe()
    
[/code]
