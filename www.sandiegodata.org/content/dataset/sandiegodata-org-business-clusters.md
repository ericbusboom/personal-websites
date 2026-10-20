---
title: "San Diego Business Clusters"
date: 2021-03-21T19:06:14+00:00
draft: false
categories: ["Dataset"]
tags: ["sandiegodata.org"]
author: "metapack"
description: "Business in San Diego linked to entertainment clusters and population density."
---

_Business in San Diego linked to entertainment clusters and population density._

`sandiegodata.org-business_clusters-1.1.5`. Modified 2021-03-21T19:41:52

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[sb_mbl](<http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5/data/sb_mbl.csv>)**. Businesses registered in San DIego, from the Master BusinessList
  * **[sd_business_clusters](<http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5/data/sd_business_clusters.csv>)**. Geographic boundaries of business clusters
  * **[sd_businesses](<http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5/data/sd_businesses.csv>)**. San Diego Businesses, geocoded
  * **[sd_custered_businesses](<http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5/data/sd_custered_businesses.csv>)**. San Diego Businesses, geocodes and linked to clusters.
  * **[naics](<http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5/data/naics.csv>)**. Naics codes for San Diego businesses


## Documentation

This dataset processes the City of San Diego Master Business file to add geocoded addresses and links to business clusters. San Diego publishes two lists of businesses, which are based on payment of the San Diego City business tax: the Master Business File, and a [SANGIS file that includes geographic information. ](<http://data.sandiegodata.org/dataset/sangis-org-business-sites/>) Unfortunatel y, these files are quite different and cannot be linked. The SANGIS file is oriented toward the tax assessors parcel that the business occupies, and the Master Business List has account numbers and addresses, but there is no common key between the files.

The files in this package add address geocodes to the Master Business List, and links the businesses to clusters of businesses. The Clusters are created by collecting nearby businesses from Open Street Map data. The cluster types are:

  * NA: No cluster, 31787 businesses
  * shop: OSM tags 'shop', 'clothes', 'supermarket', 'bank', 'laundry', 'parking', 14615 businesses
  * ent: Entertainment, OSM tags 'cafe', 'restaurant', 'bar', 14320 businesses
  * casual: Fast food and convenience stores, OSM tags 'fast_food', 'convenience', 10991 businesses


The `sd_business_clusters` file has the clusters and their WKT geographies. The `sd_custered_businesses` links San Diego businesses to clusters, and a single business may be in more than one cluster because the clusters of different tyoes overlap.

## NAICS Codes

It appears that the NAICS codes used in the Master Business List are vintage 2007. The code '72221' appears frequently, which is valid in 2007 NAICS, but not in 2012 or 2016 NAICS. 

## Geocoding

The geocoding was performed with a local installation of Pelias. There are some notable errors in the geocoding. For instance, Ba Ho Liquor and Deli, with address of '4031 AVATI DR SUITE I SAN DIEGO 92117-4403, CA', was geocoded to 4144 Avati, moving the location from a neighborhood mini-mall to a residence. It is unknown how many such error there are, so use the geocodes with caution.

### Documentation Links

  * [Documentation Page](<http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5/index.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

sb_mbl | sd_business_clusters | sd_businesses | sd_custered_businesses | naics   


### sb_mbl

Column Name| Data Type| Description  
---|---|---  
business_acct| integer|   
dba_name| string|   
ownership_type| string|   
address| string|   
city| string|   
zip| string|   
state| string|   
business_phone| string|   
owner_name| string|   
creation_dt| date|   
start_dt| date|   
exp_dt| date|   
naics| integer| 2007 NAICS code  
activity_desc| string|   
  
### sd_business_clusters

Column Name| Data Type| Description  
---|---|---  
cluster_n| integer| Cluster number  
cluster_type| string| Cluster type: ent, shop, or casual  
geometry| string|   
  
### sd_businesses

Column Name| Data Type| Description  
---|---|---  
account| integer|   
gc_address| string| Address used for geocoding  
lat| number| Geocoded latitude  
lon| number| Geocoded longitude  
dba_name| string|   
ownership_type| string|   
creation_dt| date|   
start_dt| date|   
exp_dt| date|   
owner_name| string|   
naics| integer|   
activity_desc| string|   
geometry| string| Geocoded position, in WKT format  
geoid| string| Geoid of the Census block group that contain the business point.  
pop| integer| Population of the bock group, from 2019 5 year ACS  
area| integer| Area of the block group in square meters.  
  
### sd_custered_businesses

Column Name| Data Type| Description  
---|---|---  
account| integer|   
gc_address| string|   
lat| number|   
lon| number|   
geoid| string|   
pop| integer|   
area| integer|   
dba_name| string|   
ownership_type| string|   
creation_dt| date|   
start_dt| date|   
exp_dt| date|   
owner_name| string|   
naics| integer|   
activity_desc| string|   
cluster_n| integer| Cluster number  
cluster_type| string| Cluster type: ent, shop, or casual  
geometry| string| Point location of the business, in WKT format  
  
### naics

Column Name| Data Type| Description  
---|---|---  
account| integer| Business account number  
naics| integer| Full NAICS code  
naics_2| integer| 2 digit NAICS prefix  
naics_3| integer| 3 digit NAICS prefix  
naics_4| integer| 4 digit NAICS prefix  
naics_5| integer| 5 digit NAICS prefix  
naics_6| integer| 6 digit NAICS prefix  
naics_desc| string| Description of the NAICS code  
naics_2_desc| string|   
naics_3_desc| string|   
naics_4_desc| string|   
naics_5_desc| string|   
naics_6_desc| string|   
  
## References

Urls used in the creation of this data package.

  * **index:civicknowledge.com-osm-demosearch-2.1.1#business_clusters**. US business clusters
  * **[sd_businesses_ak](<https://www.sandiego.gov/sites/default/files/tr_active1.csv>)**. San Diego Businesses A-K
  * **[sd_businesses_lz](<https://www.sandiego.gov/sites/default/files/tr_active2.csv>)**. San Diego Businesses L-Z
  * **metapack+http://library.metatab.org/sangis.org-business_sites.csv#business_sites**. San DIego Business locations, from SANGIS
  * **metapack+http://library.metatab.org/sandiegodata.org-geography-2018-13.csv#sd_county_boundary**. San Diego County Geo boundry
  * **[naics_index_2007](<https://www.census.gov/naics/2007NAICS/2007_NAICS_Index_File.xls>)**. NAICS index file, 2007.
  * **[naics_index_2007_26](<https://www.census.gov/naics/2017NAICS/2-6%20digit_2017_Codes.xlsx>)**. NAICS index file, 2007, 2 to 6 digit codes
  * **censusgeo://2019/5/CA/blockgroup**. CA Census Blocks
  * **census://2019/5/CA/blockgroup/B01003**. Total population by blocks


## Packages

  * **s3** s3://library.metatab.org/sandiegodata.org-business_clusters-1.1.5.csv
  * **csv** <http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5.csv>
  * **source** <https://github.com/CivicKnowledge/radius-search.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    sb_mbl_df =  pd.read_csv('http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5/data/sb_mbl.csv')
    sd_business_clusters_df =  pd.read_csv('http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5/data/sd_business_clusters.csv')
    sd_businesses_df =  pd.read_csv('http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5/data/sd_businesses.csv')
    sd_custered_businesses_df =  pd.read_csv('http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5/data/sd_custered_businesses.csv')
    naics_df =  pd.read_csv('http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5/data/naics.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/sandiegodata.org-business_clusters-1.1.5.csv')
    
    # Create Dataframes
    sb_mbl_df = pkg.resource('sb_mbl').dataframe()
    sd_business_clusters_gdf = pkg.resource('sd_business_clusters').geoframe()
    sd_businesses_gdf = pkg.resource('sd_businesses').geoframe()
    sd_custered_businesses_gdf = pkg.resource('sd_custered_businesses').geoframe()
    naics_df = pkg.resource('naics').dataframe()
    
[/code]
