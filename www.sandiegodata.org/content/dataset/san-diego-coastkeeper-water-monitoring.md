---
title: "San Diego Coastkeeper Water Monitoring"
date: 2019-05-15T22:32:13+00:00
draft: false
categories: ["Dataset"]
tags: ["ceden.waterboards.ca.gov", "ckan", "natural-environment", "water-project"]
author: "metapack"
description: "Monitoring measurements for San Diego creeks. Temperature, pH, conductivity,"
---

_Monitoring measurements for San Diego creeks. Temperature, pH, conductivity, bacteria, turbidity and nutrients._

`ceden.waterboards.ca.gov-sdck_monitoring-2`


## Resources

  * **[sdck_monitoring](<https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-sdck_monitoring-2/data/sdck_monitoring.csv>)**. 


## Documentation

This dataset is San Diego Costkeeper's submission to CEDEN of almost 10 years of water monitoring in San Diego county creeks, rivers and wetlands. 

See the [Water project's station map](<http://water.sandiegodata.org/maps/stations>) for a view of the loacations of the monitoring stations.

### Documentation Links

  * [http://www.ceden.org/docs/2017_documentation/cedenfield_implan_2017_0103.pdf](<Field Data Submission Guidance Document>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-sdck_monitoring-2.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-sdck_monitoring-1.csv>
  * **source** <https://github.com/san-diego-water-quality/water-datasets.git>


### Accessing Packages in Metapack
```
import metapack as mp
# ZIP Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-sdck_monitoring-2.zip')
# CSV Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-sdck_monitoring-1.csv') 

resource = pkg.resource('resource_name') # Get a resource
df = resource.dataframe() # Create a pandas Dataframe
gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
```

Last Modified 2018-08-22T20:15:00
