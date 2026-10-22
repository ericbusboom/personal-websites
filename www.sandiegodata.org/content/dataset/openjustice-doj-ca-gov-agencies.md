---
title: "California Law Enforcement Agencies"
date: 2020-06-17T21:37:37+00:00
draft: false
categories: ["Dataset", "Police Data"]
tags: ["crime", "law_enforcement", "openjustice.doj.ca.gov", "police", "police_data_collection"]
author: "metapack"
description: "California's county and agency level context data"
---

_California's county and agency level context data_

`openjustice.doj.ca.gov-agencies-1.1.1`. Modified 2020-06-17T21:37:32

Resources | Packages | Documentation| Contacts| Data Dictionary

## Resources

  * **[ca_lea_demo](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-agencies-1.1.1/data/ca_lea_demo.csv>)**. California Law Enforcement Agencies and demographic statistics for their service areas.
  * **[ca_lea_ncic](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-agencies-1.1.1/data/ca_lea_ncic.csv>)**. California LEA NCIC codes, names, and years they actively reported.


## Documentation

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

ca_lea_demo | ca_lea_ncic   


### ca_lea_demo

Column Name| Data Type| Description  
---|---|---  
year| integer|   
county| string|   
agency_name| string|   
agency_code| string|   
less_than_high_school| number|   
high_school_or_higher| number|   
bachelors_or_higher| number|   
per_capita_income| integer|   
median_income| integer|   
poverty_rate| number|   
employment_rate| number|   
unemployment_rate| number|   
  
### ca_lea_ncic

Column Name| Data Type| Description  
---|---|---  
cntycode| integer|   
county| string|   
code| string|   
agency| string|   
start| date|   
end| date|   
  
## Packages

  * **s3** s3://library.metatab.org/openjustice.doj.ca.gov-agencies-1.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-agencies-1.1.1.csv>
  * **source** <https://github.com/metatab-packages/policedata-collection.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-agencies-1.1.1.csv')
    
    # Create Dataframes
    ca_lea_demo_df = pkg.resource('ca_lea_demo').dataframe()
    ca_lea_ncic_df = pkg.resource('ca_lea_ncic').dataframe()
    
[/code]
