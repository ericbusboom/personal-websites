---
title: "HIC Facility Geocoded Addresses"
date: 2019-07-16T23:24:48+00:00
draft: false
categories: ["Dataset", "homelessness"]
tags: ["homelessness", "hudexchange.info", "sandiegodata.org"]
author: "metapack"
description: "Geocoded addresses for housing facilities in the San Diego CoC."
---

_Geocoded addresses for housing facilities in the San Diego CoC._

`sandiegodata.org-hic_geocode-1`

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[hic_geocode](<http://library.metatab.org/sandiegodata.org-hic_geocode-1/data/hic_geocode.csv>)**. Geocoded addresses from the HIC facility inventory


## Documentation

This dataset has geocoded addresses from the [HUD Housing Inventory Count](<http://data.sandiegodata.org/dataset/hudexchange-info-hic-project/>). The addressess are geocoded with the [US Census geocoder.](<https://geocoding.geo.census.gov/geocoder/geographies/addressbatch?fo
rm>)

## Caveats

Fairly few of the facilities in the inventory dataset have addresses, about 14K of 170K records.

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <http://library.metatab.org/sandiegodata.org-hic_geocode-1.zip>
  * **csv** <http://library.metatab.org/sandiegodata.org-hic_geocode-1.csv>
  * **source** <https://github.com/sandiegodata-projects/homelessness.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/sandiegodata.org-hic_geocode-1.zip')
    
    # Create Dataframes
    hic_geocode_gdf = pkg.resource('hic_geocode').geoframe()
    
[/code]

## Data Dictionary

hic_geocode   


### hic_geocode

Column Name| Data Type| Description  
---|---|---  
row| integer| Row number in original HIC inventory file  
year| integer| Inventory year  
organization_id| string| Organization id  
project_id| string| Project ID. Different projects for the same organization may have different addresses.  
coc_id| integer|   
hudnum| string|   
is_match| string| "Match" if the geocoder could match the address  
is_exact| string| 'Exact" if the geocoder found an exact address  
returned_address| string| The address for the geocoded point  
geoid| string| Tract geoid  
longitude| string|   
latitude| string|   
state_fips| string| State FIPS code  
county_fips| string| County FIPS code  
geometry| string| Position in WKT format  
  
## References

Urls used in the creation of this data package.

  * **metapack+http://library.metatab.org/hudexchange.info-hic-project-1.zip#hic**. 


Last Modified 2019-07-17T00:49:19

## Packages

  * **zip** <http://library.metatab.org/sandiegodata.org-hic_geocode-1.zip>
  * **csv** <http://library.metatab.org/sandiegodata.org-hic_geocode-1.csv>
  * **source** <https://github.com/sandiegodata-projects/homelessness.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/sandiegodata.org-hic_geocode-1.zip')
    
    # Create Dataframes
    hic_geocode_gdf = pkg.resource('hic_geocode').geoframe()
    
[/code]
