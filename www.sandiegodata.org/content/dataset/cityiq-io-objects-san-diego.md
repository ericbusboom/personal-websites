---
title: "San Diego City IQ Assets and Locations"
date: 2019-06-04T23:13:05+00:00
draft: false
categories: ["build_environment", "Dataset", "planning", "planning-collection"]
tags: ["build_environment", "cityiq", "cityiq.io", "planning", "planning-collection"]
author: "metapack"
description: "All assets types extracted form the San Diego City Iq system"
---

_All assets types extracted form the San Diego City Iq system_

`cityiq.io-objects-san_diego-5`. Modified 2020-04-12T16:44:03

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[assets](<https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5/data/assets.csv>)**. All assets
  * **[locations](<https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5/data/locations.csv>)**. All locations: walkways, traffic lanes and parking zones
  * **[walkways](<https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5/data/walkways.csv>)**. Walkways
  * **[traffic_lanes](<https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5/data/traffic_lanes.csv>)**. Traffic lanes
  * **[parking_zones](<https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5/data/parking_zones.csv>)**. Parking zones
  * **[cameras](<https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5/data/cameras.csv>)**. Cameras
  * **[mics](<https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5/data/mics.csv>)**. Microphones
  * **[nodes](<https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5/data/nodes.csv>)**. Nodes
  * **[em_sensors](<https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5/data/em_sensors.csv>)**. Electro-magnetic sensors
  * **[env_sensors](<https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5/data/env_sensors.csv>)**. Environmental sensors


## Documentation

These datafile are extracts of the assets and locations from the San Diego CityIQ system. Refer to the [CityIQ developer documentation](<https://ie-cities-docs.run.aws-usw02-pr.ice.predix.io/#c_overview
 _of_general_apis.html>) for details about these data records. The data are extracted using the [cityiq Python package](<https://pypi.org/project/cityiq/>). See the ExtractAssets.ipynb notebook for the extract process.

## Versions

  1. Development version
  2. Development version
  3. First release
  4. Added tract and community names
  5. Rebuild with recent data, and broke out asset and location types


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5.zip>
  * **xlsx** <https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5.xlsx>
  * **s3** s3://library.metatab.org/cityiq.io-objects-san_diego-5.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5.csv>
  * **source** <https://github.com/sandiegodata-projects/cityiq.io.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5.zip')
    
    # Create Dataframes
    assets_gdf = pkg.resource('assets').geoframe()
    locations_gdf = pkg.resource('locations').geoframe()
    walkways_gdf = pkg.resource('walkways').geoframe()
    traffic_lanes_gdf = pkg.resource('traffic_lanes').geoframe()
    parking_zones_gdf = pkg.resource('parking_zones').geoframe()
    cameras_gdf = pkg.resource('cameras').geoframe()
    mics_gdf = pkg.resource('mics').geoframe()
    nodes_gdf = pkg.resource('nodes').geoframe()
    em_sensors_gdf = pkg.resource('em_sensors').geoframe()
    env_sensors_gdf = pkg.resource('env_sensors').geoframe()
    
[/code]

## Data Dictionary

assets | locations   


### assets

Column Name| Data Type| Description  
---|---|---  
assetuid| string|   
assettype| string|   
parentassetuid| string|   
mediatype| string|   
events| string| What events the asset generates  
community_name| string| Name of San Diego planning community where asset is located  
tract_geoid| string| Geoid of the tract where the asset is located  
roadsegid| integer| SANDAG road segment id. Links to the SANDAG roads data  
speed| integer| Speed limit on the road segment  
oneway| string| Is the road segment one way?  
abloaddr| integer| Absolute lowest address on road segment  
abhiaddr| integer| Absolute highest address on road segment  
rd30full| string| Full street name  
geometry| string| WKT Geometry of parking zone  
  
### locations

Column Name| Data Type| Description  
---|---|---  
locationuid| string|   
locationtype| string|   
parentlocationuid| string|   
community_name| string| Name of San Diego planning community where location is located  
tract_geoid| string| Geoid of the tract where the location is located  
roadsegid| integer| SANDAG road segment id. Links to the SANDAG roads data  
speed| integer| Speed limit on the road segment  
oneway| string| Is the road segment one way?  
abloaddr| integer| Absolute lowest address on road segment  
abhiaddr| integer| Absolute highest address on road segment  
rd30full| string| Full street name  
geometry| string|   
  
## References

Urls used in the creation of this data package.

  * **metapack+https://library-metatab-org.s3.amazonaws.com/sangis.org-roads-sandiego-1.zip#all_roads**. Roads in San Diego
  * **metapack+https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-geography-2018.csv#tract_boundaries**. San Diego tracts and communities
  * **metapack+https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-geography-2018.csv#sd_community_boundaries**. San Diego tracts and communities


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5.zip>
  * **xlsx** <https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5.xlsx>
  * **s3** s3://library.metatab.org/cityiq.io-objects-san_diego-5.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5.csv>
  * **source** <https://github.com/sandiegodata-projects/cityiq.io.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/cityiq.io-objects-san_diego-5.zip')
    
    # Create Dataframes
    assets_gdf = pkg.resource('assets').geoframe()
    locations_gdf = pkg.resource('locations').geoframe()
    walkways_gdf = pkg.resource('walkways').geoframe()
    traffic_lanes_gdf = pkg.resource('traffic_lanes').geoframe()
    parking_zones_gdf = pkg.resource('parking_zones').geoframe()
    cameras_gdf = pkg.resource('cameras').geoframe()
    mics_gdf = pkg.resource('mics').geoframe()
    nodes_gdf = pkg.resource('nodes').geoframe()
    em_sensors_gdf = pkg.resource('em_sensors').geoframe()
    env_sensors_gdf = pkg.resource('env_sensors').geoframe()
    
[/code]
