---
title: "PSID Active Savings 89 and 94"
date: 2023-06-06T23:18:50+00:00
draft: false
categories: ["Dataset", "Uncategorized"]
tags: ["isr.umich.edu"]
author: "metapack"
description: "Measurements of money flows into savings, housing and annuities."
---

_Measurements of money flows into savings, housing and annuities._

`isr.umich.edu-psid-89_94-actsav-1.1.1`. Modified 2023-06-06T23:18:39


## Resources

  * **[act94](<https://library-metatab-org.s3.amazonaws.com/isr.umich.edu-psid-89_94-actsav-1.1.1/data/act94.csv>)**. Active savings, 1994
  * **[act89](<https://library-metatab-org.s3.amazonaws.com/isr.umich.edu-psid-89_94-actsav-1.1.1/data/act89.csv>)**. Active savings, 1989


## Documentation

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/isr.umich.edu-psid-89_94-actsav-1.1.1/index.html>)
  * [Home Page](<https://psidonline.isr.umich.edu/default.aspx>) PSID home page


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

act89 | act94   


### act89

Column Name| Data Type| Description  
---|---|---  
act89v1| number| RELEASE NUMBER  
act89v2| integer| 1989 INTERVIEW NUMBER  
act89v3| integer| PUT INTO ANNUITY  
act89v4| integer| CASH IN ANNUITY  
act89v5| integer| BUY REAL ESTATE  
act89v6| integer| SELL REAL ESTATE  
act89v7| integer| HOME IMPROVEMENT  
act89v8| integer| BUY BUSINESS  
act89v9| integer| SELL BUSINESS  
act89v10| integer| ASSETS MOVE OUT  
act89v11| integer| DEBTS MOVE OUT  
act89v12| integer| ASSETS BROUGHT IN  
act89v13| integer| DEBTS BROUGHT IN  
act89v14| integer| FIRST GIFT/INHERITANCE  
act89v15| integer| SECOND GIFT/INHERITANCE  
act89v16| integer| NET INTO STOCK  
  
### act94

Column Name| Data Type| Description  
---|---|---  
act94v1| number| RELEASE NUMBER  
act94v2| integer| 1994 INTERVIEW NUMBER  
act94v3| integer| PUT INTO ANNUITY  
act94v4| integer| CASH IN ANNUITY  
act94v5| integer| BUY REAL ESTATE  
act94v6| integer| SELL REAL ESTATE  
act94v7| integer| HOME IMPROVEMENT  
act94v8| integer| BUY BUSINESS  
act94v9| integer| SELL BUSINESS  
act94v10| integer| ASSETS MOVE OUT  
act94v11| integer| DEBTS MOVE OUT  
act94v12| integer| ASSETS BROUGHT IN  
act94v13| integer| DEBTS BROUGHT IN  
act94v14| integer| FIRST GIFT/INHERITANCE  
act94v15| integer| SECOND GIFT/INHERITANCE  
act94v16| integer| THIRD GIFT/INHERITANCE  
act94v17| integer| NET INTO STOCK  
act94v18| integer| SELL MAIN HOME  
  
## References

Urls used in the creation of this data package.

  * **data/ActSavings89_94**. 


## Packages

  * **s3** s3://library.metatab.org/isr.umich.edu-psid-89_94-actsav-1.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/isr.umich.edu-psid-89_94-actsav-1.1.1.csv>


### Accessing Data in Vanilla Pandas
```
import pandas as pd


act94_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/isr.umich.edu-psid-89_94-actsav-1.1.1/data/act94.csv')
act89_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/isr.umich.edu-psid-89_94-actsav-1.1.1/data/act89.csv')
```

### Accessing Package in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/isr.umich.edu-psid-89_94-actsav-1.1.1.csv')

# Create Dataframes
act94_df = pkg.resource('act94').dataframe()
act89_df = pkg.resource('act89').dataframe()
```
