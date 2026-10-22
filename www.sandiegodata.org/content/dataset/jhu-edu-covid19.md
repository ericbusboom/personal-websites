---
title: "COVID-19 Data"
date: 2020-03-22T04:02:56+00:00
draft: false
categories: ["covid19", "Dataset"]
tags: ["covid19", "jhu.edu"]
author: "metapack"
description: "COVID 19 cases data from Johns Hopkins, augmented and reformtted"
---

_COVID 19 cases data from Johns Hopkins, augmented and reformtted_

`jhu.edu-covid19-2.4.38`. Modified 2020-07-08T04:59:37


## Resources

  * **[confirmed](<https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38/data/confirmed.csv>)**. Confirmed Non-US cases by date and country
  * **[deaths](<https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38/data/deaths.csv>)**. Non-US Death cases by date and country
  * **[recovered](<https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38/data/recovered.csv>)**. Non-US recoveries cases by date and country
  * **[confirmed_us](<https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38/data/confirmed_us.csv>)**. Confirmed US cases by date and country
  * **[deaths_us](<https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38/data/deaths_us.csv>)**. US Death cases by date and country


## Documentation

This dataset processed and augments the COVID-19 data provided by Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE). [The source data is checked into Github daily.](<https://github.com/CSSEGISandData/COVID-19/>) and is collected from a variety of sources.

This dataset reformats the data into tidy format, with dates expressed as values instead of column headings, and adds several fields that are useful for analysis.

The 'rate_t5d' column is the growth date from 5 days before the observation to the observation. For example, for a row with a current observation of value x_5, and a past observation of x_0, the rate_t5d is calculated as e^((log(x_5)-log(x_0)) / 5)-1 . The result is that x_5 = x_0 * (1+rate_t5d)^5, and rate_t5d from the previous 5 days

## Caveats

  * China's minimum cases in the dataset is 548, so it's value for days sincle 100 cases is shifted by 6 days. It's just a guess, but it looks good. 
  * Countries that haven't reached 100 cases yet will have a days since 100 cases value that is always negative.


### Documentation Links

  * [John Hopkins Project Homepage](<https://systems.jhu.edu/research/public-health/ncov/>)
  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38/index.html>)


## Contacts

  * **Origin**

[John Hopkins University Center for Systems Science and Engineering](<https://systems.jhu.edu/>)

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

confirmed | deaths | recovered | confirmed_us | deaths_us   


### confirmed

Column Name| Data Type| Description  
---|---|---  
country| string| Country  
province| string| Province, state, country or other region  
location| string| Combination of county and province  
date| datetime| Date of observation  
confirmed| integer| Cumulative number of confirmed positives  
date_10| datetime| Earliest date at which there were more than 10 cases  
days_10| integer| Number of days since the earliest date of 10 cases  
date_100| datetime| Earliest date at which there were more than 100 cases  
days_100| integer| Number of days since the earliest date of 100 cases  
rate_t5d| number| Growth rate, averaged over the following 5 days.  
confirmed_log| number| Log of the number of confirmed positive cases  
  
### deaths

Column Name| Data Type| Description  
---|---|---  
country| string| Country  
province| string| Province, state, country or other region  
location| string| Combination of county and province  
date| datetime| Date of observation  
death| integer| Cumulative number of deaths  
date_10| datetime| Earliest date at which there were more than 10 cases  
days_10| integer| Number of days since the earliest date of 10 cases  
date_100| string| Earliest date at which there were more than 100 cases  
days_100| integer| Number of days since the earliest date of 100 cases  
rate_t5d| number| Growth rate, averaged over the following 5 days.  
death_log| number| Log of the number of deaths  
  
### recovered

Column Name| Data Type| Description  
---|---|---  
country| string| Country  
province| string| Province, state, country or other region  
location| string| Combination of county and province  
date| datetime| Date of observation  
recovered| integer| Cumulative number of recoveries  
date_10| datetime| Earliest date at which there were more than 10 cases  
days_10| integer| Number of days since the earliest date of 10 cases  
date_100| datetime| Earliest date at which there were more than 100 cases  
days_100| integer| Number of days since the earliest date of 100 cases  
rate_t5d| number| Growth rate, averaged over the following 5 days.  
recovered_log| number| Log of the number of recoveries  
  
### confirmed_us

Column Name| Data Type| Description  
---|---|---  
uid| integer|   
date| datetime|   
confirmed| integer|   
date_10| datetime|   
days_10| integer|   
date_100| string|   
days_100| integer|   
rate_t5d| number|   
confirmed_log| number|   
iso2| string|   
iso3| string|   
code3| integer|   
fips| integer|   
admin2| string|   
province| string|   
country| string|   
lat| number|   
long| number|   
location| string|   
population| integer|   
  
### deaths_us

Column Name| Data Type| Description  
---|---|---  
uid| integer|   
date| datetime|   
death| integer|   
date_10| datetime|   
days_10| integer|   
date_100| string|   
days_100| integer|   
rate_t5d| number|   
death_log| number|   
iso2| string|   
iso3| string|   
code3| integer|   
fips| integer|   
admin2| string|   
province| string|   
country| string|   
lat| number|   
long| number|   
location| string|   
population| integer|   
  
## References

Urls used in the creation of this data package.

  * **[ts_base_url](<https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/>)**. Base URL for time series data
  * **[confirmed_ts_source](<https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv>)**. Source for time series of confirmed cases, excluding US
  * **[death_ts_source](<https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv>)**. Source for time series of deaths, excluding US
  * **[recov_ts_source](<https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv>)**. Source for time series of recoveries, excluding US
  * **[confirmed_ts_us_source](<https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv>)**. Source for time series of confirmed cases, US Only
  * **[death_ts_us_source](<https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv>)**. Source for time series of deaths, US Only


## Packages

  * **s3** s3://library.metatab.org/jhu.edu-covid19-2.4.38.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38.csv>
  * **source** <https://github.com/metatab-packages/metatab-packages.git>


### Accessing Data in Vanilla Pandas
```
import pandas as pd


confirmed_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38/data/confirmed.csv')
deaths_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38/data/deaths.csv')
recovered_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38/data/recovered.csv')
confirmed_us_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38/data/confirmed_us.csv')
deaths_us_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38/data/deaths_us.csv')
```

### Accessing Package in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/jhu.edu-covid19-2.4.38.csv')

# Create Dataframes
confirmed_df = pkg.resource('confirmed').dataframe()
deaths_df = pkg.resource('deaths').dataframe()
recovered_df = pkg.resource('recovered').dataframe()
confirmed_us_df = pkg.resource('confirmed_us').dataframe()
deaths_us_df = pkg.resource('deaths_us').dataframe()
```
