---
title: "San Diego Unified School Enrollment Boundaries"
date: 2019-08-14T15:38:18+00:00
draft: false
categories: ["Dataset"]
tags: ["sandiegounified.org"]
author: "metapack"
description: "Geographic boundaries for schools in the San Diego Unified school district"
---

_Geographic boundaries for schools in the San Diego Unified school district_

`sandiegounified.org-enrollment_zones-2014-1`

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[sdusd_boundaries](<http://library.metatab.org/sandiegounified.org-enrollment_zones-2014-1/data/sdusd_boundaries.csv>)**. Select boundaries of school enrollments areas in San Diego Unified school district.
  * **[school_tract_xwalk](<http://library.metatab.org/sandiegounified.org-enrollment_zones-2014-1/data/school_tract_xwalk.csv>)**. Porportions of overlap between tracts and school enrollment areas.


## Documentation

## Building

The `data/sdusd.zip` file is built manually from the three data/*zip files, using the `notebooks/CombineFiles.ipynb` notebook

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), Civic Knowledge


## Packages

  * **zip** <http://library.metatab.org/sandiegounified.org-enrollment_zones-2014-1.zip>
  * **s3** s3://library.metatab.org/sandiegounified.org-enrollment_zones-2014-1.csv
  * **csv** <http://library.metatab.org/sandiegounified.org-enrollment_zones-2014-1.csv>
  * **source** <https://github.com/metatab-packages/metatab-packages.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/sandiegounified.org-enrollment_zones-2014-1.zip')
    
    # Create Dataframes
    sdusd_boundaries_gdf = pkg.resource('sdusd_boundaries').geoframe()
    
    school_tract_xwalk_df = pkg.resource('school_tract_xwalk').dataframe()
[/code]

## Data Dictionary

sdusd_boundaries | school_tract_xwalk   


### sdusd_boundaries

Column Name| Data Type| Description  
---|---|---  
id| integer|   
school| string| School name  
cdscode| integer| SDUSD CDS code for school  
ncesdist| integer| National Center for Educational Statistics ( NCES) district code  
ncesschool| integer| NCES School code  
soctype| string| The School Ownership Code is a numeric code used to identify the type of school. See http://data.sandiegodata.org/dataset/cde-ca-gov-schools/#data_dictionary_public_schools for details.  
eilcode| string| The Educational Instruction Level Code is a short text description of the institution’s type relative to the grade range served. See http://data.sandiegodata.org/dataset/cde-ca-gov-schools/#data_dictionary_public_schools for details.  
eilname| string| Name associated with eilcode  
group| string| Code for source of record among three original files: ELEM, MID or HIGH  
latitude| number| Geographic position of school  
longitude| number| Geographic position of school  
geometry| string| Geometry of boundary, in WKT format.  
  
### school_tract_xwalk

Column Name| Data Type| Description  
---|---|---  
cdscode| integer| CDS code for a school  
geoid| string| Geoid of a Census tract  
school_in_tract| number| Portion of the school enrollment area in the tract  
tract_in_school| number| Portion of the tract in the school enrollment area  
  
## References

Urls used in the creation of this data package.

  * **shape+file:data/elem1415.zip**. Elementary school boundaries
  * **shape+file:data/mid1415.zip**. Middle school boundaries
  * **shape+file:data/high1415.zip**. High school boundaries.
  * **notebooks/CombineFiles.ipynb**. This is a manually run notebook that combines the three shapefiles in the data directory
  * **metapack+http://library.metatab.org/cde.ca.gov-schools.csv#public_schools**. California public schools


Last Modified 2019-08-14T15:37:04

## Packages

  * **zip** <http://library.metatab.org/sandiegounified.org-enrollment_zones-2014-1.zip>
  * **s3** s3://library.metatab.org/sandiegounified.org-enrollment_zones-2014-1.csv
  * **csv** <http://library.metatab.org/sandiegounified.org-enrollment_zones-2014-1.csv>
  * **source** <https://github.com/metatab-packages/metatab-packages.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/sandiegounified.org-enrollment_zones-2014-1.zip')
    
    # Create Dataframes
    sdusd_boundaries_gdf = pkg.resource('sdusd_boundaries').geoframe()
    
    school_tract_xwalk_df = pkg.resource('school_tract_xwalk').dataframe()
[/code]
