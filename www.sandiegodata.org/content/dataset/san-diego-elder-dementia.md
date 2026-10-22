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


## Resources

  * **[adod-prevalence](<https://library-metatab-org.s3.amazonaws.com/sdcounty.ca.gov-adod-2012-san-diego-county-1/data/adod-prevalence.csv>)**. Table 1. Estimates of Prevalence of Alzheimer's Disease and Other Dementias by Subregional Area, 55 Years and Over, San Diego County, 2012 - 2030
  * **[hospital-discharge](<https://library-metatab-org.s3.amazonaws.com/sdcounty.ca.gov-adod-2012-san-diego-county-1/data/hospital-discharge.csv>)**. Table 2. Number of Emergency Department or Hospital Discharged Patients with Any Mention of Alzheimer's Disease and Other Dementias by Subregional Area, 55 Years and Over, San Diego County, 2012 - 2030
  * **[elder-population-2012](<https://library-metatab-org.s3.amazonaws.com/sdcounty.ca.gov-adod-2012-san-diego-county-1/data/elder-population-2012.csv>)**. Table 3. 2012 Population by Age Group and Subregional Area, 55 Years and Over, San Diego County
  * **[elder-population-2020](<https://library-metatab-org.s3.amazonaws.com/sdcounty.ca.gov-adod-2012-san-diego-county-1/data/elder-population-2020.csv>)**. Table 4. 2020 Population Projections by Age Group and Subregional Area, 55 Years and Over, San Diego County
  * **[elder-population-2030](<https://library-metatab-org.s3.amazonaws.com/sdcounty.ca.gov-adod-2012-san-diego-county-1/data/elder-population-2030.csv>)**. Table 5. 2030 Population Projections by Age Group and Subregional Area, 55 Years and Over, San Diego County


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

[Rashmi Keshava Iyengar](<mailto:rashmi.k.iyengar@gmail.com>), [San Diego Regional Data Library](</>)

  * **Wrangler**

[Eric Busboom](<mailto:eric@sandiegodata.org>), [Civic Knowledge](<http://www.civicknowledge.com>)


## Packages

  * **xlsx** <https://library-metatab-org.s3.amazonaws.com/sdcounty.ca.gov-adod-2012-san-diego-county-1.xlsx>
  * **zip** <https://library-metatab-org.s3.amazonaws.com/sdcounty.ca.gov-adod-2012-san-diego-county-1.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sdcounty.ca.gov-adod-2012-san-diego-county-1.csv>


### Accessing Packages in Metapack
```
import metapack as mp
# ZIP Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sdcounty.ca.gov-adod-2012-san-diego-county-1.zip')
# CSV Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sdcounty.ca.gov-adod-2012-san-diego-county-1.csv') 

resource = pkg.resource('resource_name') # Get a resource
df = resource.dataframe() # Create a pandas Dataframe
gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
```

Last Modified
