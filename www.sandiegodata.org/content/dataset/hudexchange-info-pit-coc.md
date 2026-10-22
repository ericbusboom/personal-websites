---
title: "HUD Point in Time Counts by CoC"
date: 2019-07-07T19:58:05+00:00
draft: false
categories: ["Dataset", "homelessness"]
tags: ["homelessness", "hudexchange.com", "hudexchange.info"]
author: "metapack"
description: "Combined years of sheltered and unsheltered homeless counts, by CoC."
---

_Combined years of sheltered and unsheltered homeless counts, by CoC._

`hudexchange.info-pit-coc-1`


## Resources

  * **[pitc_coc](<https://library-metatab-org.s3.amazonaws.com/hudexchange.info-pit-coc-1/data/pitc_coc.csv>)**. Combined pitc, 2007 to 2018


## Documentation

HUD publishes an Excel workbook with sheltered and unsheltered counts, aggregated to CoC, for the whole country, for 2007 on. In this dataset, each year is in a seperate worksheet, and later years have more columns than earlier years, and most column names include the year as a suffix. 

This data package combines al of these years into a single file, with normalized column names. Cells in years that don't have a column that are in later years are filled with nulls, and each row is prefixed with the year of the file that the original row was sourced from.

For a graphic view of which columns are missing, by year ( actually by position in the dataset ) see the null map at the end of the [EDA notebook](<https://github.com/sandiegodata-projects/homelessness/blob/master/datasets/hudexchange.com-pit-coc/notebooks/eda-pitc_coc.ipynb>).

## Revisions to the Historic Point-in-Time Estimates

The data source file includes this note:

On rare occasions, the Point-in-Time estimates published in prior editions of the AHAR have been subsequently updated. The estimates described in this file represent the latest versions of these data (as of the publication of this file). The revisions are summarized below:

  1. Beginning in the 2014 AHAR Part 1, the PIT estimates of unsheltered people experiencing homelessness in the Los Angeles City and County CoC, CA-600, were updated for the years 2007–2013. Within the CoC, the adjustments subtracted: 20,746 total people from 2007 and 2008; 9,451 total people in 2009 and 2010; 10,800 total people in 2011 and 2012; and 18,274 total people from 2013. These adjustments also caused drops in the key unsheltered populations reported on the AHAR, individuals, people in families, veterans, and chronically homeless individuals. More details on the size of each adjustment, by population, can be found in the 2014 AHAR Part 1.

  2. Beginning in the 2014 AHAR Part 1, the PIT estimate of veterans experiencing homelessness in shelter projects in the Phoenix/Mesa/Maricopa County Regional CoC, AZ-502, was updated for the year 2013, increasing by 214 veterans. This update did not change the total number of people experiencing homelessness in shelter projects (or overall) in the CoC—just the number of those people who were classified as veterans.

  3. Beginning in the 2015 AHAR Part 1, the PIT estimates of unsheltered people experiencing homelessness in the Las Vegas/Clark County CoC, NV-500, were updated for the years 2007–2014. Within the CoC, the adjustments subtracted: 3,884 total people from 2007 and 2008; 3,389 total people in 2009 and 2010; 1,429 total people in 2011 and 2012; 1,404 total people from 2013; and 1,974 total people from 2014. These adjustments also caused drops in the key unsheltered populations reported on the AHAR, individuals, people in families, veterans, and chronically homeless individuals. More details on the size of each adjustment, by population, can be found in the 2015 AHAR Part 1.

  4. Beginning in the 2015 AHAR Part 1, the PIT estimates of veterans experiencing homelessness in the Anchorage CoC, AK-500, were updated for the year 2014. The sheltered estimate for this CoC increased by 71 veterans, and the unsheltered estimate increased by 18 veterans. Neither of these updates changed the total number of people experiencing homelessness in the CoC—just the number of those people who were classified as veterans.

  5. Beginning in the 2017 AHAR Part 2 and the 2018 AHAR Part 1, the PIT estimates of unsheltered people experiencing homelessness in the Los Angeles City and County CoC, CA-600, were updated for the year 2017, decreasing by a total of 2,746 people. The adjustment also caused drops in the key unsheltered populations reported on the AHAR, individuals, people in families, veterans, and chronically homeless individuals. More details on the size of each adjustment, by population, can be found in the 2017 AHAR Part 2 and the 2018 AHAR Part 1.


### Documentation Links

  * [EDA Notebook For pitc_coc](<https://github.com/sandiegodata-projects/homelessness/blob/master/datasets/hudexchange.com-pit-coc/notebooks/eda-pitc_coc.ipynb>)Jupyter EDA notebook.
  * [PIT and HIC Data Since 2007](<https://www.hudexchange.info/resource/3031/pit-and-hic-data-since-2007/>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)

  * **Publisher**

[US Department of Housing and Urban Development](<https://www.hud.gov/>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/hudexchange.info-pit-coc-1.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/hudexchange.info-pit-coc-1.csv>
  * **source** <https://github.com/sandiegodata-projects/homelessness.git>


### Accessing Packages in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/hudexchange.info-pit-coc-1.zip')

# Create Dataframes

pitc_coc_df = pkg.resource('pitc_coc').dataframe()
```

## Data Dictionary

pitc_coc   


### pitc_coc

Column Name| Data Type| Description  
---|---|---  
year| integer|   
coc_number| string|   
coc_name| text|   
coc_category| string|   
chronically_homeless| integer|   
chronically_homeless_individuals| integer|   
chronically_homeless_people_in_families| integer|   
homeless_children_of_parenting_youth| integer|   
homeless_family_households| integer|   
homeless_individuals| integer|   
homeless_parenting_youth_age_18_24| integer|   
homeless_parenting_youth_under_18| integer|   
homeless_parenting_youth_under_25| integer|   
homeless_people_in_families| integer|   
homeless_unaccompanied_youth_age_18_24| integer|   
homeless_unaccompanied_youth_under_18| integer|   
homeless_unaccompanied_youth_under_25| integer|   
homeless_veterans| integer|   
overall_homeless| integer|   
sheltered_es_chronically_homeless| integer|   
sheltered_es_chronically_homeless_individuals| integer|   
sheltered_es_chronically_homeless_people_in_families| integer|   
sheltered_es_homeless| integer|   
sheltered_es_homeless_children_of_parenting_youth| integer|   
sheltered_es_homeless_family_households| integer|   
sheltered_es_homeless_individuals| integer|   
sheltered_es_homeless_parenting_youth_age_18_24| integer|   
sheltered_es_homeless_parenting_youth_under_18| integer|   
sheltered_es_homeless_parenting_youth_under_25| integer|   
sheltered_es_homeless_people_in_families| integer|   
sheltered_es_homeless_unaccompanied_youth_age_18_24| integer|   
sheltered_es_homeless_unaccompanied_youth_under_18| integer|   
sheltered_es_homeless_unaccompanied_youth_under_25| integer|   
sheltered_es_homeless_veterans| integer|   
sheltered_sh_chronically_homeless| integer|   
sheltered_sh_chronically_homeless_individuals| integer|   
sheltered_sh_homeless| integer|   
sheltered_sh_homeless_individuals| integer|   
sheltered_sh_homeless_unaccompanied_youth_age_18_24| integer|   
sheltered_sh_homeless_unaccompanied_youth_under_18| integer|   
sheltered_sh_homeless_unaccompanied_youth_under_25| integer|   
sheltered_sh_homeless_veterans| integer|   
sheltered_th_homeless| integer|   
sheltered_th_homeless_children_of_parenting_youth| integer|   
sheltered_th_homeless_family_households| integer|   
sheltered_th_homeless_individuals| integer|   
sheltered_th_homeless_parenting_youth_age_18_24| integer|   
sheltered_th_homeless_parenting_youth_under_18| integer|   
sheltered_th_homeless_parenting_youth_under_25| integer|   
sheltered_th_homeless_people_in_families| integer|   
sheltered_th_homeless_unaccompanied_youth_age_18_24| integer|   
sheltered_th_homeless_unaccompanied_youth_under_18| integer|   
sheltered_th_homeless_unaccompanied_youth_under_25| integer|   
sheltered_th_homeless_veterans| integer|   
sheltered_total_chronically_homeless| integer|   
sheltered_total_chronically_homeless_individuals| integer|   
sheltered_total_chronically_homeless_people_in_families| integer|   
sheltered_total_homeless| integer|   
sheltered_total_homeless_children_of_parenting_youth| integer|   
sheltered_total_homeless_family_households| integer|   
sheltered_total_homeless_individuals| integer|   
sheltered_total_homeless_parenting_youth_age_18_24| integer|   
sheltered_total_homeless_parenting_youth_under_18| integer|   
sheltered_total_homeless_parenting_youth_under_25| integer|   
sheltered_total_homeless_people_in_families| integer|   
sheltered_total_homeless_unaccompanied_youth_age_18_24| integer|   
sheltered_total_homeless_unaccompanied_youth_under_18| integer|   
sheltered_total_homeless_unaccompanied_youth_under_25| integer|   
sheltered_total_homeless_veterans| integer|   
unsheltered_chronically_homeless| integer|   
unsheltered_chronically_homeless_individuals| integer|   
unsheltered_chronically_homeless_people_in_families| integer|   
unsheltered_homeless| integer|   
unsheltered_homeless_children_of_parenting_youth| integer|   
unsheltered_homeless_family_households| integer|   
unsheltered_homeless_individuals| integer|   
unsheltered_homeless_parenting_youth_age_18_24| integer|   
unsheltered_homeless_parenting_youth_under_18| integer|   
unsheltered_homeless_parenting_youth_under_25| integer|   
unsheltered_homeless_people_in_families| integer|   
unsheltered_homeless_unaccompanied_youth_age_18_24| integer|   
unsheltered_homeless_unaccompanied_youth_under_18| integer|   
unsheltered_homeless_unaccompanied_youth_under_25| integer|   
unsheltered_homeless_veterans| integer|   
  
## References

Urls used in the creation of this data package.

  * **[pitc_coc_2018](<https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-CoC.xlsx#2018>)**. 2007 - 2018 PIT Counts by CoC; 2018 workbook
  * **[pitc_coc_2017](<https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-CoC.xlsx#2017>)**. 2006 - 2018 PIT Counts by CoC; 2017 workbook
  * **[pitc_coc_2016](<https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-CoC.xlsx#2016>)**. 2005 - 2018 PIT Counts by CoC; 2016 workbook
  * **[pitc_coc_2015](<https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-CoC.xlsx#2015>)**. 2004 - 2018 PIT Counts by CoC; 2015 workbook
  * **[pitc_coc_2014](<https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-CoC.xlsx#2014>)**. 2003 - 2018 PIT Counts by CoC; 2014 workbook
  * **[pitc_coc_2013](<https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-CoC.xlsx#2013>)**. 2002 - 2018 PIT Counts by CoC; 2013 workbook
  * **[pitc_coc_2012](<https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-CoC.xlsx#2012>)**. 2001 - 2018 PIT Counts by CoC; 2012 workbook
  * **[pitc_coc_2011](<https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-CoC.xlsx#2011>)**. 2000 - 2018 PIT Counts by CoC; 2011 workbook
  * **[pitc_coc_2010](<https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-CoC.xlsx#2010>)**. 1999 - 2018 PIT Counts by CoC; 2010 workbook
  * **[pitc_coc_2009](<https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-CoC.xlsx#2009>)**. 1998 - 2018 PIT Counts by CoC; 2009 workbook
  * **[pitc_coc_2008](<https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-CoC.xlsx#2008>)**. 1997 - 2018 PIT Counts by CoC; 2008 workbook
  * **[pitc_coc_2007](<https://www.hudexchange.info/resources/documents/2007-2018-PIT-Counts-by-CoC.xlsx#2007>)**. 1996 - 2018 PIT Counts by CoC; 2007 workbook


Last Modified 2019-07-12T05:00:57

## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/hudexchange.info-pit-coc-1.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/hudexchange.info-pit-coc-1.csv>
  * **source** <https://github.com/sandiegodata-projects/homelessness.git>


### Accessing Packages in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/hudexchange.info-pit-coc-1.zip')

# Create Dataframes

pitc_coc_df = pkg.resource('pitc_coc').dataframe()
```
