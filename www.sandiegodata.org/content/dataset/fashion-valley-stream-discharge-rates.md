---
title: "Fashion Valley Stream Discharge Rates"
date: 2019-05-15T22:35:03+00:00
draft: false
categories: ["Dataset"]
tags: ["ckan", "water-project", "waterservices.usgs.gov"]
author: "metapack"
description: "Stream discharge rates for the Fashion Valley station on the San Diego river,"
---

_Stream discharge rates for the Fashion Valley station on the San Diego river, from 1988 on_

`waterservices.usgs.gov-stream_discharge-fashion_valley_sd-2`

Resources | Packages | Documentation| Contacts

## Resources

  * **[fashion_valley](<http://library.metatab.org/waterservices.usgs.gov-stream_discharge-fashion_valley_sd-2/data/fashion_valley.csv>)**. Stream discharge rates for the San Diego River, Fashion Valley Station.


## Documentation

## Original Notice

The data file includes this comment header:
[code] 
        # ---------------------------------- WARNING ----------------------------------------
        # Some of the data that you have obtained from this U.S. Geological Survey database may not 
        # have received Director's approval.  Any such data values are qualified as provisional and 
        # are subject to revision.  Provisional data are released on the condition that neither the 
        # USGS nor the United States Government may be held liable for any damages resulting from its use.
        #  Go to http://help.waterdata.usgs.gov/policies/provisional-data-statement for more information.
        #
        # File-format description:  http://help.waterdata.usgs.gov/faq/about-tab-delimited-output
        # Automated-retrieval info: http://help.waterdata.usgs.gov/faq/automated-retrievals
        #
        # Contact:   gs-w_support_nwisweb@usgs.gov
        # retrieved: 2018-07-24 15:45:47 -04:00 (natwebcaas01)
        #
        # Data for the following 1 site(s) are contained in this file
        #    USGS 11023000 SAN DIEGO R A FASHION VALLEY AT SAN DIEGO CA
        # -----------------------------------------------------------------------------------
        #
        # TS_ID - An internal number representing a time series.
        # IV_TS_ID - An internal number representing the Instantaneous Value time series from which the daily statistic is calculated.
        #
        # Data provided for site 11023000
        #    TS_ID       Parameter    Statistic  IV_TS_ID       Description
        #    7745        00060        00003      14023          Discharge, cubic feet per second (Mean)
        #
        # Data-value qualification codes included in this output:
        #     A  Approved for publication -- Processing and review completed.
        #     e  Value has been estimated.
        #     P  Provisional data subject to revision.
        #
    
[/code]

### Documentation Links

  * [https://waterdata.usgs.gov/ca/nwis/uv?11023000](<Data access page>)Web page with links to graphs and downloads
  * [https://waterservices.usgs.gov/rest/DV-Test-Tool.html](<URL Generation>)USGS Daily Values Web Service URL Generation Tool


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <http://library.metatab.org/waterservices.usgs.gov-stream_discharge-fashion_valley_sd-2.zip>
  * **csv** <http://library.metatab.org/waterservices.usgs.gov-stream_discharge-fashion_valley_sd-2.csv>
  * **source** <https://github.com/san-diego-water-quality/water-datasets.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('http://library.metatab.org/waterservices.usgs.gov-stream_discharge-fashion_valley_sd-2.zip')
    # CSV Package
    pkg = mp.open_package('http://library.metatab.org/waterservices.usgs.gov-stream_discharge-fashion_valley_sd-2.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

Last Modified 2018-08-09T15:00:46
