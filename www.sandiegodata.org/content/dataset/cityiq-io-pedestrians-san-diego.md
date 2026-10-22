---
title: "San Diego Pedestrian Counts"
date: 2019-06-09T18:47:22+00:00
draft: false
categories: ["build_environment", "Dataset", "planning", "planning-collection"]
tags: ["build_environment", "cityiq.io", "planning", "planning-collection"]
author: "metapack"
description: "Counts of pedestrian traffic from the San Diego CityIQ system"
---

_Counts of pedestrian traffic from the San Diego CityIQ system_

`cityiq.io-pedestrians-san_diego-1`


## Resources

  * **[pedestrians](<https://library-metatab-org.s3.amazonaws.com/cityiq.io-pedestrians-san_diego-1/data/pedestrians.csv>)**. Pedestrians


## Documentation

This dataset is pedestrian directions and counts for walkwaks in the San Diego CityIQ system. The package includes pedestrian counts for most walkway locations in the San Diego CityIQ system, but not all of them. The date range for the data is 1 August 2018 to the last full month before the package was built. For Version 1, then end date is 1 June 2019.

## Building the Source Package

Before generating this package, you must have scraped all of the events to be included in the package. After creating a `.city-iq.yaml` configuration file, run:
```
$ ciq_events -s ped # Scrape the events
$ ciq_aggregate ped # Convert JSON to CSV
```

The first process `ciq_events` may run for several days and consume up to 300G of disk space. The second process, `ciq_aggregate` may run for a few hours and consume a few more gigabytes of disk space.

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/cityiq.io-pedestrians-san_diego-1.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/cityiq.io-pedestrians-san_diego-1.csv>
  * **source** <https://github.com/sandiegodata-projects/cityiq.io.git>


### Accessing Packages in Metapack
```
import metapack as mp
# ZIP Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/cityiq.io-pedestrians-san_diego-1.zip')
# CSV Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/cityiq.io-pedestrians-san_diego-1.csv') 

resource = pkg.resource('resource_name') # Get a resource
df = resource.dataframe() # Create a pandas Dataframe
gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
```

## Data Dictionary

pedestrians   


### pedestrians

Column Name| Data Type| Description  
---|---|---  
timestamp| datetime| Time of event, quantized to 15 minute intervals  
locationuid| string| Locationuid for the walkway  
direction| integer| Direction of pedestrian's travel, in degrees. Only two values per walkway, 180 degrees apart.  
speed| number| Speed of pedestrians, in meters per second  
count| integer| Number of pedestrians, per locationuid, per direction.  
  
Last Modified 2019-06-09T16:47:37
