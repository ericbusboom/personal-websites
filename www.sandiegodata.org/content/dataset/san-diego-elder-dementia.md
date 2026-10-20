---
title: "55+ ADOD and General Population Projections - SD County"
date: 2019-05-15T22:33:39+00:00
draft: false
categories: ["Dataset"]
tags: ["age-friendly-communities", "ckan", "health"]
author: "metapack"
description: "Current (2012) ADOD and General population data along with projections for 2020 and 2030 for San Diego county"
---

_Current (2012) ADOD and General population data along with projections for 2020 and 2030 for San Diego county_

`sdcounty.ca.gov-adod-2012-san-diego-county-1`

Resources | Packages | Documentation| Contacts

## Resources

  * **[adod-prevalence](<http://s3.amazonaws.com/library.metatab.org/sdcounty.ca.gov-adod-2012-san-diego-county-1/data/adod-prevalence.csv>)**. Table 1. Estimates of Prevalence of Alzheimer's Disease and Other Dementias by Subregional Area, 55 Years and Over, San Diego County, 2012 - 2030
  * **[hospital-discharge](<http://s3.amazonaws.com/library.metatab.org/sdcounty.ca.gov-adod-2012-san-diego-county-1/data/hospital-discharge.csv>)**. Table 2. Number of Emergency Department or Hospital Discharged Patients with Any Mention of Alzheimer's Disease and Other Dementias by Subregional Area, 55 Years and Over, San Diego County, 2012 - 2030
  * **[elder-population-2012](<http://s3.amazonaws.com/library.metatab.org/sdcounty.ca.gov-adod-2012-san-diego-county-1/data/elder-population-2012.csv>)**. Table 3. 2012 Population by Age Group and Subregional Area, 55 Years and Over, San Diego County
  * **[elder-population-2020](<http://s3.amazonaws.com/library.metatab.org/sdcounty.ca.gov-adod-2012-san-diego-county-1/data/elder-population-2020.csv>)**. Table 4. 2020 Population Projections by Age Group and Subregional Area, 55 Years and Over, San Diego County
  * **[elder-population-2030](<http://s3.amazonaws.com/library.metatab.org/sdcounty.ca.gov-adod-2012-san-diego-county-1/data/elder-population-2030.csv>)**. Table 5. 2030 Population Projections by Age Group and Subregional Area, 55 Years and Over, San Diego County


## Documentation

### Documentation Links

  * [http://www.sandiegocounty.gov/content/sdc/hhsa/programs/phs/community_health_statistics/reports.html](<SD County HHSA Reports>)
  * [docs/sd-county-hhsa-adod-packet-upates.pdf](<SD County HHSA ADOD Packet Upates>)Updates to the SD HHSA ADOD profiles in the county. All data is extracted from this document


## Contacts

  * **Origin**

sdcounty.ca.gov, [County of San Diego Health and Human Services Agency](<http://www.sandiegocounty.gov/hhsa/>)

  * **Creator**

[Lesie Ray](<mailto:Leslie.Ray@sdcounty.ca.gov.>), County of San Diego Health and Human Services Agency

  * **Wrangler**

[Rashmi Keshava Iyengar](<mailto:rashmi.k.iyengar@gmail.com>), [San Diego Regional Data Library](<http://www.sandiegodata.org>)

  * **Wrangler**

[Eric Busboom](<mailto:eric@sandiegodata.org>), [Civic Knowledge](<http://www.civicknowledge.com>)


## Packages

  * **xlsx** <http://s3.amazonaws.com/library.metatab.org/sdcounty.ca.gov-adod-2012-san-diego-county-1.xlsx>
  * **zip** <http://s3.amazonaws.com/library.metatab.org/sdcounty.ca.gov-adod-2012-san-diego-county-1.zip>
  * **csv** <http://s3.amazonaws.com/library.metatab.org/sdcounty.ca.gov-adod-2012-san-diego-county-1.csv>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('http://s3.amazonaws.com/library.metatab.org/sdcounty.ca.gov-adod-2012-san-diego-county-1.zip')
    # CSV Package
    pkg = mp.open_package('http://s3.amazonaws.com/library.metatab.org/sdcounty.ca.gov-adod-2012-san-diego-county-1.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

Last Modified
