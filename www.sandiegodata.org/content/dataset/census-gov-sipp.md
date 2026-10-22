---
title: "Survey of Income and Program Participation"
date: 2020-12-28T19:45:40+00:00
draft: false
categories: ["Dataset"]
tags: ["census.gov"]
author: "metapack"
description: "SIPP collects data and measures change for many topics including: economic well-"
---

_SIPP collects data and measures change for many topics including: economic well- being, family dynamics, education, assets, health insurance, childcare, and food security._

`census.gov-sipp-1.1.1`. Modified 2020-12-28T19:45:33


## Documentation

SIPP is the premier source of information for income and program participation. SIPP collects data and measures change for many topics including: economic well-being, family dynamics, education, assets, health insurance, childcare, and food security.

Theis data package collects links to the SIP website and main data files. It does not include any data.

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/census.gov-sipp-1.1.1/index.html>)
  * [Program home page](<https://www.census.gov/programs-surveys/sipp.html>)
  * [2018 data page](<https://www.census.gov/programs-surveys/sipp/data/datasets/2018-data/2018.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

  


## References

Urls used in the creation of this data package.

  * **[pu2018_dta](<https://www2.census.gov/programs-surveys/sipp/data/datasets/2018/pu2018_dta.zip#pu2018.dta>)**. 2018 SIPP primary data, stata format
  * **[rw2018_dta](<https://www2.census.gov/programs-surveys/sipp/data/datasets/2018/rw2018_sasdata.zip>)**. 2018 SIPP replicate weights, stata format
  * **[pu2018_csv](<https://www2.census.gov/programs-surveys/sipp/data/datasets/2018/pu2018_csv.zip>)**. 2018 SIPP primary data, CSV format
  * **[rw2018_csv](<https://www2.census.gov/programs-surveys/sipp/data/datasets/2018/rw2018_csv.zip>)**. 2018 SIPP replicate weights, CSV format
  * **[pu2018_schema](<https://www2.census.gov/programs-surveys/sipp/data/datasets/2018/pu2018_schema.json>)**. 2018 Primary data schema
  * **[rw2018_schema](<https://www2.census.gov/programs-surveys/sipp/data/datasets/2018/rw2018_schema.json>)**. 2018 Replicate weights schema


## Packages

  * **s3** s3://library.metatab.org/census.gov-sipp-1.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/census.gov-sipp-1.1.1.csv>
  * **source** <https://github.com/metatab-packages/inequality-collection.git>


### Accessing Data in Vanilla Pandas
```
import pandas as pd
```

### Accessing Package in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/census.gov-sipp-1.1.1.csv')

# Create Dataframes
```
