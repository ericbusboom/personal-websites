---
title: "San Diego Downtown Homless Computer Vision Package"
date: 2019-09-12T23:41:39+00:00
draft: false
categories: ["Dataset"]
tags: ["sandiegodata.org"]
author: "metapack"
description: "Files and code for analyzing San Diego downtown homelessness  data with computer"
---

_Files and code for analyzing San Diego downtown homelessness data with computer vision_

`sandiegodata.org-downtown_cv-5`

Resources | Packages | Documentation| Contacts| Data Dictionary

## Resources

  * **[gcp](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-downtown_cv-5/data/gcp.csv>)**. Ground control points
  * **[intersection_regions](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-downtown_cv-5/data/intersection_regions.csv>)**. Polygon transformations for each the intersections of each map
  * **[intersections](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-downtown_cv-5/data/intersections.csv>)**. List of intersections.
  * **[file_annotations](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-downtown_cv-5/data/file_annotations.csv>)**. File annotations on count files
  * **[counts](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-downtown_cv-5/data/counts.csv>)**. Annotation position, types and counts of handwritten marks


## Documentation

This dataset collects records related to a conversion of 5 years of paper maps that record positions of homeless sleepers in downtown San Diego. The San Diego Regional Data Library is [converting these paper maps to a digital form](<http://downtown-homelessness.sandiegodata.org/>) with a manual process that uses an image annotation tool, and theses annotations can be used to train computer vision algorithms to georeference maps and recognize handwritten marks.

These datasets link to map urls and annotations, for three kinds of annotations:

  * Ground Control Points, which identify the map image locations for known intersections, linking image coordinates ( in pixels ) to geographic coordinates.
  * Image locations of handwritten marks and the number written in the mark.
  * File annotations, for other handwritten notes such as the temperature and presence of rain. 


## More Information:

  * [Blog Post](<http://www.sandiegodata.org/2019/09/computer-vision-for-greater-good/>). For more discussion about the GCP and handwritten marks, and the tasks in volved in developing computer vision algorithms for these data, see our recent blog post on the subject.
  * [Clustering Notebook](<https://nbviewer.jupyter.org/github/sandiegodata-projects/downtown-partnership/blob/master/datasets/sandiegodata.org-downtown_cv/notebooks/Template%20Matching%20Clusters.ipynb>). For some examples of using OpenCV to extract and match templates, to georeference maps, see the Templates and Clustering Jupyter Notebook].
  * [Extract Marks Notebook](<https://nbviewer.jupyter.org/github/sandiegodata-projects/downtown-partnership/blob/master/datasets/sandiegodata.org-downtown_cv/notebooks/Extract%20Marks.ipynb>). For examples of extracting ( but not recognizing ) handwritten marks, see this notebook. 


## Developer notes

After anotation JSON files are copied into S#, the list of S# urls must be updated. To refresh the list of urls run
[code] 
    $  bin/update_s3.sh <s3-profile>
    
[/code]

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-downtown_cv-5.zip>
  * **s3** s3://library.metatab.org/sandiegodata.org-downtown_cv-5.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-downtown_cv-5.csv>
  * **source** <https://github.com/sandiegodata-projects/homelessness.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-downtown_cv-5.zip')
    
    # Create Dataframes
    
    gcp_df = pkg.resource('gcp').dataframe()
    intersection_regions_df = pkg.resource('intersection_regions').dataframe()intersections_gdf = pkg.resource('intersections').geoframe()
    
    file_annotations_df = pkg.resource('file_annotations').dataframe()
    counts_df = pkg.resource('counts').dataframe()
[/code]

## Data Dictionary

gcp | intersections | intersection_regions | file_annotations | counts   


### gcp

Column Name| Data Type| Description  
---|---|---  
image_url| string| Map image url  
x| integer| X position of upper left of region rectangle, in pixels  
y| integer| Y position of upper left of region rectangle, in pixels  
width| integer| Width of selection region rectangle in pixels  
height| integer| Height of selection region rectangle in pixels  
intersection| string| Name of intersection  
  
### intersections

Column Name| Data Type| Description  
---|---|---  
geometry| string| WKT format geometry of intersection point  
neighborhood| string| Neighborhood intersection is in  
intersection| string| Name of intersection  
  
### intersection_regions

Column Name| Data Type| Description  
---|---|---  
image_url| string| Url to a map image  
neighborhood| string| Name of the neighborhood for the maps  
year| integer| Year portion of the data collection date.  
month| integer| Month portion of the data collection date.  
intersections_id| string| A string composed of the names of the four intersections.  
intersection_group| string| A name, based on the neighbrhood, that identifies distinct intersection_id strings.  
map_name| string| A name based on the neighborhood and map changes in 2016 and 2017  
source_inv| string| The intersection polygon, fromed from the intersection points, in WKT format, in the pixel coordinate space. This version is inverted, with the Y coordinate being subtracted from 2000, so the orientation of the Y axis is the same as the EPSG:2230 geographic coordinate space.  
source| string| Like source_inv, but the Y axis is not inverted, so the coordinates are the same as the image.  
source_area| number| Area of source shape, in square pixels  
source_shape| string| (X,Y) shape of source polygon bounding box  
source_shape_x| integer| X value of source_shape  
source_shape_y| integer| Y value of source_shape  
dest| string| The intersection polygon, but in EPSG:2230 (State plane 6, California, Feet) coordinates.  
matrix| string| An affine transformation matric that transforms from the coorinates of source_inv to dest. When pixel locations are properly inverted, this matrix transforms from pixel locations to geographic locations.  
  
### file_annotations

Column Name| Data Type| Description  
---|---|---  
image_url| string| Url to a map image  
url_year| integer| Year, from url  
url_month| integer| Month, from url  
date| datetime| Date, from file annotation, or from url if the annotation is empty  
neighborhood| string| Neighborhood  
url_neighborhood| string| Neighborhood from url  
total_count| number| Total count of handwritten marks, or may be the processed value, with the structure and vehicle counts multipled by conversion factors.  
temp| integer| Temperature, if it was given on the map  
rain| string| Rain, if it was recorded on the map.  
  
### counts

Column Name| Data Type| Description  
---|---|---  
image_url| string| Map image URL  
cx| integer| X value of the center of the circle region, in pixels  
cy| integer| Y value of the center of the circle region in pixels  
r| integer| Radius of the circle region, in pixels  
type| string| Type of sleeper: Individual, Vehicle or Structure  
count| string| Count of sleepers  
  
Last Modified 2019-09-13T04:52:40

## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-downtown_cv-5.zip>
  * **s3** s3://library.metatab.org/sandiegodata.org-downtown_cv-5.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-downtown_cv-5.csv>
  * **source** <https://github.com/sandiegodata-projects/homelessness.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-downtown_cv-5.zip')
    
    # Create Dataframes
    
    gcp_df = pkg.resource('gcp').dataframe()
    intersection_regions_df = pkg.resource('intersection_regions').dataframe()intersections_gdf = pkg.resource('intersections').geoframe()
    
    file_annotations_df = pkg.resource('file_annotations').dataframe()
    counts_df = pkg.resource('counts').dataframe()
[/code]
