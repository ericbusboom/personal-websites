---
title: "Hospital Utilization Forecasts"
date: 2020-04-01T00:07:50+00:00
draft: false
categories: ["covid19", "Dataset"]
tags: ["covid19", "healthdata.org"]
author: "metapack"
description: "Forecasts for state and national utilization of hospital beads, ICUs and deaths"
---

_Forecasts for state and national utilization of hospital beads, ICUs and deaths ventilators_

`healthdata.org-hospitalizations-1.2.11`. Modified 2020-06-22T00:17:43


## Resources

  * **[hospitalizations](<https://library-metatab-org.s3.amazonaws.com/healthdata.org-hospitalizations-1.2.11/data/hospitalizations.csv>)**. All utilization estimates for state and the US from the model.


## Documentation

This dataset supports a projection of hospital utilization created by [IHME](<http://www.healthdata.org/>) The data is presented in an [interactive vizualization](<https://covid19.healthdata.org/projections>).

### Documentation Links

  * [Research Report](<http://www.healthdata.org/sites/default/files/files/research_articles/2020/COVID-forecasting-03252020_4.pdf>) Overview and summary of the model.
  * [IHME Homepage](<http://www.healthdata.org/>)
  * [Vizualization](<https://covid19.healthdata.org/projections>) Interactive vizualization of the report


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

hospitalizations   


### hospitalizations

Column Name| Data Type| Description  
---|---|---  
location_name| string|   
date| date|   
allbed_mean| number|   
allbed_lower| number|   
allbed_upper| number|   
icubed_mean| number|   
icubed_lower| number|   
icubed_upper| number|   
invven_mean| number|   
invven_lower| number|   
invven_upper| number|   
deaths_mean| number|   
deaths_lower| number|   
deaths_upper| number|   
admis_mean| number|   
admis_lower| number|   
admis_upper| number|   
newicu_mean| number|   
newicu_lower| number|   
newicu_upper| number|   
totdea_mean| number|   
totdea_lower| number|   
totdea_upper| number|   
bedover_mean| number|   
bedover_lower| number|   
bedover_upper| number|   
icuover_mean| number|   
icuover_lower| number|   
icuover_upper| number|   
  
## Packages

  * **s3** s3://library.metatab.org/healthdata.org-hospitalizations-1.2.11.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/healthdata.org-hospitalizations-1.2.11.csv>
  * **source** <https://github.com/sandiegodata/covid19.git>


### Accessing Packages in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/healthdata.org-hospitalizations-1.2.11.csv')

# Create Dataframes
hospitalizations_df = pkg.resource('hospitalizations').dataframe()
```
