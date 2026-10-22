---
title: "Monthly Retail Trade Report"
date: 2020-05-19T16:53:30+00:00
draft: false
categories: ["Dataset"]
tags: ["census.gov", "Economy"]
author: "metapack"
description: "Retail and Food Service sales volume, by months, since 1992"
---

_Retail and Food Service sales volume, by months, since 1992_

`census.gov-monthly_retail-1.2.1`. Modified 2020-05-19T20:08:06


## Resources

  * **[mrts_adjusted](<https://library-metatab-org.s3.amazonaws.com/census.gov-monthly_retail-1.2.1/data/mrts_adjusted.csv>)**. Monthly retail sales, adjusted
  * **[mrts_non_adjusted](<https://library-metatab-org.s3.amazonaws.com/census.gov-monthly_retail-1.2.1/data/mrts_non_adjusted.csv>)**. Monthly retail sales, non adjusted
  * **[mrts_combined](<https://library-metatab-org.s3.amazonaws.com/census.gov-monthly_retail-1.2.1/data/mrts_combined.csv>)**. Monthly retail sales, adjusted and non adjusted combined


## Documentation

The Monthly Retail Trade Report reports estimates of the monthly sales of retail and food service businesses, based on a survey. This dataset converts the Excel spreadsheet that the Census publishes, to better format the data for multi-year analysis. 

The `sales` column is in dollars, while the original data is in millions of dollars. 

The `flags` column describes the type of observation:

  * M regular monthly observations
  * PM Preliminary monthly estimate
  * CY Total of current year
  * PY Total of previous year


Other notes from the bottom of the Excel file worksheets: 
```
(p) Preliminary estimate
(S) Suppressed - Estimate does not meet publication standards because of high sampling variability (coefficient of variation is greater than 30%), poor response quality (total quantity response rate
is less than 50%), or other concerns about the estimate's quality.

(1) GAFO represents stores classified in the following NAICS codes:  442, 443, 448, 451, 452, and 4532. NAICS code 4532 includes office supplies, stationery, and gift stores.
(2) Estimates are adjusted for seasonal variations and holiday and trading-day differences, but not for price changes. Cumulative seasonally adjusted sales estimates are not tabulated.

Note: Estimates are not adjusted for price changes. Retail and food services total and other subsector totals may include data for kinds of business not shown.
For surveyed Retail companies, approximately 45.7% provided data for this reporting period, resulting in a total quantity response rate of 60.8% for sales.
Information on sample design, estimation procedures, and measures of sampling variability can be found on the internet at http://www.census.gov/retail/mrts/how_surveys_are_collected.html.
```

### Documentation Links

  * [homepage](<https://www.census.gov/retail/index.html>)Dataset home page


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **s3** s3://library.metatab.org/census.gov-monthly_retail-1.2.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/census.gov-monthly_retail-1.2.1.csv>
  * **source** <https://github.com/metatab-packages/census.gov-monthly_retail.git>


### Accessing Packages in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/census.gov-monthly_retail-1.2.1.csv')

# Create Dataframes
mrts_adjusted_df = pkg.resource('mrts_adjusted').dataframe()
mrts_non_adjusted_df = pkg.resource('mrts_non_adjusted').dataframe()
mrts_combined_df = pkg.resource('mrts_combined').dataframe()
```

## Data Dictionary

mrts_adjusted | mrts_non_adjusted | mrts_combined   


### mrts_adjusted

Column Name| Data Type| Description  
---|---|---  
naics| string| NAICS industry codes for the row  
category| string| Description of industry categories  
date| datetime| Year and month of observation, in ISO format. FOr CY and PY, the start of the year.  
year| integer| Year, extracted from the date  
month| integer| Month, of observation, for monthly observation  
sales| integer| Sales value, in dollars.  
flag| string| M for monthly observation, CY for current year total, PY for previous year total  
  
### mrts_non_adjusted

Column Name| Data Type| Description  
---|---|---  
naics| string| NAICS industry codes for the row  
category| string| Description of industry categories  
date| datetime| Year and month of observation, in ISO format. FOr CY and PY, the start of the year.  
year| integer| Year, extracted from the date  
month| integer| Month, of observation, for monthly observation  
sales| integer| Sales value, in dollars.  
flag| string| M for monthly observation, CY for current year total, PY for previous year total  
  
### mrts_combined

Column Name| Data Type| Description  
---|---|---  
naics| integer| NAICS industry codes for the row  
category| string| Description of industry categories  
date| datetime| Year and month of observation, in ISO format. FOr CY and PY, the start of the year.  
year| integer| Year, extracted from the date  
month| integer| Month, of observation, for monthly observation  
flag| string| M for monthly observation, CY for current year total, PY for previous year total  
sales_adj| integer| Adjusted sales, in dollars  
sales_nonadj| integer| Unadjusted sales, in dollars  
  
## References

Urls used in the creation of this data package.

  * **[marts_source](<https://www.census.gov/retail/mrts/www/mrtssales92-present.xls>)**. Retail and Food Service Sales spreadsheet


## Packages

  * **s3** s3://library.metatab.org/census.gov-monthly_retail-1.2.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/census.gov-monthly_retail-1.2.1.csv>
  * **source** <https://github.com/metatab-packages/census.gov-monthly_retail.git>


### Accessing Packages in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/census.gov-monthly_retail-1.2.1.csv')

# Create Dataframes
mrts_adjusted_df = pkg.resource('mrts_adjusted').dataframe()
mrts_non_adjusted_df = pkg.resource('mrts_non_adjusted').dataframe()
mrts_combined_df = pkg.resource('mrts_combined').dataframe()
```
