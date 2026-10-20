---
title: "Community and City and Tract Boundaries in San Diego County"
date: 2019-05-15T22:33:45+00:00
draft: false
categories: ["Dataset"]
tags: ["ckan", "geography", "infrastructure", "planning-project", "sandiegodata.org"]
author: "metapack"
description: "Combines  geographic boundary files for communities, cities and tracts in San"
---

_Combines geographic boundary files for communities, cities and tracts in San Diego County._

`sandiegodata.org-geography-2018-13`

Resources | Packages | Documentation| Contacts| References

## Resources

  * **[tracts](<http://library.metatab.org/sandiegodata.org-geography-2018-13/data/tracts.csv>)**. Tract census information
  * **[places](<http://library.metatab.org/sandiegodata.org-geography-2018-13/data/places.csv>)**. Census place information, which includes incorporated cities and unincorporated towns like Julian and Romona
  * **[places_boundaries](<http://library.metatab.org/sandiegodata.org-geography-2018-13/data/places_boundaries.csv>)**. Census place boundaries, which includes incorporated cities and unincorporated towns like Julian and Romona
  * **[city_boundaries](<http://library.metatab.org/sandiegodata.org-geography-2018-13/data/city_boundaries.csv>)**. Boundary shapes for cities
  * **[sd_community_boundaries](<http://library.metatab.org/sandiegodata.org-geography-2018-13/data/sd_community_boundaries.csv>)**. Boundary shapes for SD City communities
  * **[county_boundaries](<http://library.metatab.org/sandiegodata.org-geography-2018-13/data/county_boundaries.csv>)**. Boundary shapes for unincorporated County areas
  * **[district_boundaries](<http://library.metatab.org/sandiegodata.org-geography-2018-13/data/district_boundaries.csv>)**. Boundaries for special districts, such as the Promize Zone
  * **[county_communities_boundaries](<http://library.metatab.org/sandiegodata.org-geography-2018-13/data/county_communities_boundaries.csv>)**. Boundaries for county communities
  * **[combined_boundaries](<http://library.metatab.org/sandiegodata.org-geography-2018-13/data/combined_boundaries.csv>)**. Boundary shapes for all communities, county regions and cities combined
  * **[tract_boundaries](<http://library.metatab.org/sandiegodata.org-geography-2018-13/data/tract_boundaries.csv>)**. Tract boundary shapes
  * **[tract_communities](<http://library.metatab.org/sandiegodata.org-geography-2018-13/data/tract_communities.csv>)**. Link between tracts and cities, communities and county regions, with one record per tract. No geometry.
  * **[sd_county_boundary](<http://library.metatab.org/sandiegodata.org-geography-2018-13/data/sd_county_boundary.csv>)**. Boundary shape for SD County


## Documentation

This package combines three SANGIS datasets for communities and cities in San Diego county into a single file, in the `communities` resource, with Census tract definitions for San Diego count. The source files are:

  * Municipal boundaries, of incorporated cities and the rest of the county
  * Communities in unincorporated county areas
  * Communities in San Diego. 
  * Census tract boundaries for 2016
  * Census places and counties


In addition to simply combining these four boundary files, the dataset also links tracts into the other three regions, in the `tracts_links` and `tracts_all_regions` datasets. Using these datasets, you can get all of the tracts in Escondido, or all of the tracts in the San Diego community of Clairemont. The join is performed by containment of the Internal Point, which is defined by the census for each tract. Because tract boundaries are not always coincident with municipal boundaries, there are many cases where the collection of tracts for a city or community will have a different boundary than the actual region. Smaller, less densely populated regions, like San Marcos, or particuarly afected.

The `tracts_links` dataset is probably the most useful. It joins tracts to regions, and has two sets of columns, for city and community. This dataset includes every tract in the county, and each appears only once. If a tract is included in both a city and community, then there is a name and code for both the city columns and the community columns. Regions not in a city have a city value of "County" and a city code of "CN".

The `communities` dataset, has a `type` field to distinguish the types of area, which is one of:

  * city
  * county_community
  * sd_community
  * community


The `tracts_all_regions` dataset may have more than one row for each tract; the tract will appear once for each of the four region types that it is in, but no tract is in more than 2 regions. For instance, a tract in a community of San Diego will appear twice, once for the community, and once for the City.

## Versions

  1. Added county outline
  2. Broke out seperate files for non-tract geographies.


### Documentation Links

  * [http://library.metatab.org/sandiegodata.org-geography-2018-13/doc/Community_Plan_SD.pdf](<San Diego City Community Shapefile Documentation>)
  * [http://library.metatab.org/sandiegodata.org-geography-2018-13/doc/Community_Plan_CN.pdf](<San Diego County Community Shapefile Documentation>)
  * [http://library.metatab.org/sandiegodata.org-geography-2018-13/doc/Municipal_Boundaries.pdf](<City Boundary Shapefile Documentation>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)

  * **Publisher**

[San Diego Regional Data Library](<mailto:eric@sandiegodata.org>), [San Diego Regional Data Library](<http://sandieogdata.org>)


## Packages

  * **zip** <http://library.metatab.org/sandiegodata.org-geography-2018-13.zip>
  * **csv** <http://library.metatab.org/sandiegodata.org-geography-2018-13.csv>
  * **source** <https://github.com/sandiegodata/planning-database.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('http://library.metatab.org/sandiegodata.org-geography-2018-13.zip')
    # CSV Package
    pkg = mp.open_package('http://library.metatab.org/sandiegodata.org-geography-2018-13.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

## References

Urls used in the creation of this data package.

  * **censusgeo://2016/5/CA/140**. Tract boundary shapes
  * **file:data/community-acronyms.csv**. Acronyms for communities
  * **shape+file:data/Promise_Zone_SD.zip**. Promise zone boundary
  * **shape+file:data/Municipal_Boundaries.zip**. Converted source of boundaries for cities in San Diego county
  * **shape+file:data/Community_Plan_CN.ZIP**. Converted source of boundaries for communities in unincorporated San Diego county
  * **shape+file:data/Community_Plan_SD.zip**. Converted source of boundaries for communities in the city of San Diego.
  * **metapack+http://library.metatab.org/census.gov-counties-2017-2.csv#counties**. County boundaries shapes
  * **censusgeo://CA/place**. Census Defined Places


Last Modified 2019-03-02T19:18:39
