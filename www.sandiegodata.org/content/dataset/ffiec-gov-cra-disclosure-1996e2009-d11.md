---
title: "Community Reinvestment Act Disclosure Files, Table D1-1,1996 through 2009"
date: 2020-10-17T22:05:21+00:00
draft: false
categories: ["Dataset"]
tags: ["ffiec.gov", "mdf-lending", "projects"]
author: "metapack"
description: "Multi-year CRA disclosures for small business originations, per county, year and"
---

_Multi-year CRA disclosures for small business originations, per county, year and bank._

`ffiec.gov-cra_disclosure-1996e2009-d11-3.1.1`. Modified 2020-10-23T19:30:39

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[sb_loan_orig](<http://library.metatab.org/ffiec.gov-cra_disclosure-1996e2009-d11-3.1.1/data/sb_loan_orig.csv>)**. Table D1-1, small business disclosure records, for years 1996 through 2009


## Documentation

The [Community Reinvestment Act](<https://www.ffiec.gov/cra/default.htm>) was enacted by congress in 1997 to encourage investment in underserved communities. The Act requires lenders record and publish data about loans on a per-community basis, specifically, Census tracts and MSAs. The Disclosure reports record individual lender's loans for MSAs, broken out by loan value and the Median Family income of tracts. 

The [original data releases](<https://www.ffiec.gov/cra/craflatfiles.htm>) are difficult to use, as each year's disclosures are packages as fixed-width records with all 6 tables in a single file, requiring substantial effort to extract specific record. This data package collects the Small Business Loan origination disclosure records ( D1-1 ) for the years 2010 to 2015, inclusive. 

This data package includes years 1996 through 2009. Another data package includes the years 2010 on. 

# Versions

  * 1.1.1 Initial version, for years 2010 to 2018
  * 2.1.1 Duplicated and changed years to 1996 to 2009
  * 3.1.1 Fixed schema to account for varitions in column width from year to year.


### Documentation Links

  * [Disclosure File Specifications](<https://www.ffiec.gov/cra/pdf/17FlatDiscSpecs.pdf>) File specifications for the 2017 Disclosure Flat File
  * [Documentation Page](<http://library.metatab.org/ffiec.gov-cra_disclosure-1996e2009-d11-3.1.1/index.html>)
  * [CRA Data Products](<https://www.ffiec.gov/cra/craproducts.htm>)
  * [Aggregate & Disclosure Flat Files](<https://www.ffiec.gov/cra/craflatfiles.htm>) Links to download the files.


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@sandiegodata.org>), [San Diego Regional Data Library](<http://www.sandiegodata.org>)


## Data Dictionary

cra_disclosure   


### cra_disclosure

Column Name| Data Type| Description  
---|---|---  
table_id| text| Value is D1-1  
respondent_id| text| Assigned by regulatory agency (same as HMDAID if applicable); Right justified with leading zeros  
agency| integer| Values are 1=OCC, 2=FRS, 3=FDIC, or 4=OTS  
year| integer| Four digit year (e.g. 2012)  
loan_type| integer| Value is 4 (Small Business)  
action| integer| Value is 1 (Originations)  
state| integer| FIPS code with leading zeros or blank for totals across all states  
county| integer| FIPS code with leading zeros or blank for totals across all counties  
msa| integer| As defined by OMB; Right justified with leading zeros, NA left justified for areas outside of MSA/MD or blank for totals across all MSA/MDs  
assessment_area| text| Values are 0001 through 9999; Right justified with leading zeros, NA left justified for areas outside of an Assessment Area (including predominately military areas) OR blank for totals across all Assessment Areas  
partial_county| text| Values are Y = Yes N = No OR blank for totals  
split_county| text| Values are Y = Yes N = No OR blank for totals  
pop_class| text| Values are S= counties with 500,000 in population OR blank for totals  
income_total| text| Values are 1= 120% of MFI 14= MFI not known (income percentage = 0) 15= Tract not Known (reported as NA) 101= Low Income ( 120% of MFI) 105= Income Not Known (0) 106= Tract not Known (NA) Right justified with leading zeros or blank for totals  
report_level| text| Values are 4= Total Inside & Outside Assessment Area (AA) (across all states) 6= Total Inside AA (across all states) 8= Total Outside AA (across all states) 10= State Total 20= Total Inside AA in State 30= Total Outside AA in State 40= County Total 50= Total Inside AA in County 60= Total Outside AA in County Right justified with leading zeros or blank if not a total  
num_orig_bus_lt100k| integer| Number of loans less than $100K  
tot_orig_bus_lt100k| integer| Total value of loans, in thousands  
num_orig_bus_lt250k| integer| Number of loans less than $250K, more than $100K  
tot_orig_bus_gt100k_lt250k| integer| Total value of loans, in thousands  
num_orig_bus_gt250k_lt1m| integer| Number of loans, less than $1M, more than $250K  
tot_orig_bus_gt250k_lt1m| integer| Total value of loans, in thousands  
num_orig_bus_lt1m| integer| Number of loans to businesses with gross revenues of less than $1m  
tot_orig_bus_lt1m| integer| Total value of loans, in thousands  
num_orig_bus_al| integer| Number of affiliate loans  
tot_orig_bus_al| integer| Total value of loans, in thousands  
  
## References

Urls used in the creation of this data package.

  * **[discl_96](<https://www.ffiec.gov/cra/xls/96exp_discl.zip>)**. 
  * **[discl_97](<https://www.ffiec.gov/cra/xls/97exp_discl.zip>)**. 
  * **[discl_98](<https://www.ffiec.gov/cra/xls/98exp_discl.zip>)**. 
  * **[discl_99](<https://www.ffiec.gov/cra/xls/99exp_discl.zip>)**. 
  * **[discl_00](<https://www.ffiec.gov/cra/xls/00exp_discl.zip>)**. 
  * **[discl_01](<https://www.ffiec.gov/cra/xls/01exp_discl.zip>)**. 
  * **[discl_02](<https://www.ffiec.gov/cra/xls/02exp_discl.zip>)**. 
  * **[discl_03](<https://www.ffiec.gov/cra/xls/03exp_discl.zip>)**. 
  * **[discl_04](<https://www.ffiec.gov/cra/xls/04exp_discl.zip>)**. 
  * **[discl_05](<https://www.ffiec.gov/cra/xls/05exp_discl.zip>)**. 
  * **[discl_06](<https://www.ffiec.gov/cra/xls/06exp_discl.zip>)**. 
  * **[discl_07](<https://www.ffiec.gov/cra/xls/07exp_discl.zip>)**. 
  * **[discl_08](<https://www.ffiec.gov/cra/xls/08exp_discl.zip>)**. 
  * **[discl_09](<https://www.ffiec.gov/cra/xls/09exp_discl.zip>)**. 


## Packages

  * **s3** s3://library.metatab.org/ffiec.gov-cra_disclosure-1996e2009-d11-3.1.1.csv
  * **csv** <http://library.metatab.org/ffiec.gov-cra_disclosure-1996e2009-d11-3.1.1.csv>
  * **source** <https://github.com/sandiegodata/data-projects.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    sb_loan_orig_df =  pd.read_csv('http://library.metatab.org/ffiec.gov-cra_disclosure-1996e2009-d11-3.1.1/data/sb_loan_orig.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/ffiec.gov-cra_disclosure-1996e2009-d11-3.1.1.csv')
    
    # Create Dataframes
    sb_loan_orig_df = pkg.resource('sb_loan_orig').dataframe()
    
[/code]
