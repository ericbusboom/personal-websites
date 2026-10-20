---
title: "Reimbursement Rates"
date: 2019-05-23T03:37:44+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "education"]
author: "metapack"
description: "Child Nutrition Program meal program reimbursement rates."
---

_Child Nutrition Program meal program reimbursement rates._

`cde.ca.gov-reimbursements-1.1.1`. Modified 2021-03-11T00:14:44

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[cacfpreimburse](<http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1/data/cacfpreimburse.csv>)**. Child and Adult Care Food Program
  * **[nslpreimburse](<http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1/data/nslpreimburse.csv>)**. National School Lunch Program
  * **[sbpreimburse](<http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1/data/sbpreimburse.csv>)**. School Breakfast Program
  * **[snackreimburse](<http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1/data/snackreimburse.csv>)**. Meal Supplements (After-School Snacks) in the National School Lunch Program
  * **[summerreimburse](<http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1/data/summerreimburse.csv>)**. Summer Food Service Program


## Documentation

Reimbursement rates that were manually scraped from CDE web pages, then combined into this data package.

### Documentation Links

  * [Documentation Page](<http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1/index.html>)
  * [Homepage](<https://www.cde.ca.gov/ls/nu/rs/index.asp>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

cacfpreimburse | nslpreimburse | sbpreimburse | snackreimburse | summerreimburse   


### cacfpreimburse

Column Name| Data Type| Description  
---|---|---  
year| int|   
meal| string|   
free| float|   
reduced_price| float|   
base| float|   
  
### nslpreimburse

Column Name| Data Type| Description  
---|---|---  
year| integer|   
category| text|   
free| float|   
free_6_cents| float|   
reduced_price| float|   
reduced_price_6_cents| float|   
paid| float|   
paid_6_cents| float|   
  
### sbpreimburse

Column Name| Data Type| Description  
---|---|---  
year| integer|   
category| string|   
free| float|   
reduced_price| float|   
paid| float|   
  
### snackreimburse

Column Name| Data Type| Description  
---|---|---  
year| integer|   
category| string|   
free| float|   
reduced_price| float|   
paid| float|   
  
### summerreimburse

Column Name| Data Type| Description  
---|---|---  
year| integer|   
meal| string|   
rural_or_self_prep| float|   
other_site_type| float|   
  
## References

Urls used in the creation of this data package.

  * **file:data/cacfpreimburse_2013.csv# &encoding=ascii**. 
  * **file:data/cacfpreimburse_2014.csv# &encoding=ascii**. 
  * **file:data/cacfpreimburse_2015.csv# &encoding=ascii**. 
  * **file:data/cacfpreimburse_2016.csv# &encoding=ascii**. 
  * **file:data/cacfpreimburse_2017.csv# &encoding=ascii**. 
  * **file:data/cacfpreimburse_2018.csv# &encoding=ascii**. 
  * **file:data/nslpreimburse_2013.csv# &encoding=latin1**. 
  * **file:data/nslpreimburse_2014.csv# &encoding=latin1**. 
  * **file:data/nslpreimburse_2015.csv# &encoding=latin1**. 
  * **file:data/nslpreimburse_2016.csv# &encoding=latin1**. 
  * **file:data/nslpreimburse_2017.csv# &encoding=latin1**. 
  * **file:data/nslpreimburse_2018.csv# &encoding=latin1**. 
  * **file:data/sbpreimburse_2013.csv# &encoding=ascii**. 
  * **file:data/sbpreimburse_2014.csv# &encoding=ascii**. 
  * **file:data/sbpreimburse_2015.csv# &encoding=ascii**. 
  * **file:data/sbpreimburse_2016.csv# &encoding=ascii**. 
  * **file:data/sbpreimburse_2017.csv# &encoding=ascii**. 
  * **file:data/sbpreimburse_2018.csv# &encoding=ascii**. 
  * **file:data/snackreimburse_2013.csv# &encoding=ascii**. 
  * **file:data/snackreimburse_2014.csv# &encoding=ascii**. 
  * **file:data/snackreimburse_2015.csv# &encoding=ascii**. 
  * **file:data/snackreimburse_2016.csv# &encoding=ascii**. 
  * **file:data/snackreimburse_2017.csv# &encoding=ascii**. 
  * **file:data/snackreimburse_2018.csv# &encoding=ascii**. 
  * **file:data/summerreimburse_2013.csv# &encoding=ascii**. 
  * **file:data/summerreimburse_2014.csv# &encoding=ascii**. 
  * **file:data/summerreimburse_2015.csv# &encoding=ascii**. 
  * **file:data/summerreimburse_2016.csv# &encoding=ascii**. 
  * **file:data/summerreimburse_2017.csv# &encoding=ascii**. 
  * **file:data/summerreimburse_2018.csv# &encoding=ascii**. 


## Packages

  * **s3** s3://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1.csv
  * **csv** <http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1.csv>
  * **source** <https://github.com/sandiegodata-projects/sandiegohungercoalition.org.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    cacfpreimburse_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1/data/cacfpreimburse.csv')
    nslpreimburse_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1/data/nslpreimburse.csv')
    sbpreimburse_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1/data/sbpreimburse.csv')
    snackreimburse_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1/data/snackreimburse.csv')
    summerreimburse_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1/data/summerreimburse.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://cde.metatab.org/cde.ca.gov-reimbursements-1.1.1.csv')
    
    # Create Dataframes
    cacfpreimburse_df = pkg.resource('cacfpreimburse').dataframe()
    nslpreimburse_df = pkg.resource('nslpreimburse').dataframe()
    sbpreimburse_df = pkg.resource('sbpreimburse').dataframe()
    snackreimburse_df = pkg.resource('snackreimburse').dataframe()
    summerreimburse_df = pkg.resource('summerreimburse').dataframe()
    
[/code]
