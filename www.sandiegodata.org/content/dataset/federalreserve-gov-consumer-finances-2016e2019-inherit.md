---
title: "Survey of Consumer Finances, Inheritance Extract"
date: 2020-08-19T17:30:05+00:00
draft: false
categories: ["Dataset"]
tags: ["federalreserve.gov"]
author: "metapack"
description: "An Extract from the survey of consumer finances for studying networth and"
---

_An Extract from the survey of consumer finances for studying networth and ineritance, from multiple years_

`federalreserve.gov-consumer_finances-2016e2019-inherit-1.2.6`. Modified 2020-12-23T22:43:08

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[inherit_scf_16_19](<https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances-2016e2019-inherit-1.2.6/data/inherit_scf_16_19.csv>)**. Extract of the 2016 and 2019 SCF for inheritance and networth,uninflated
  * **[inherit_scf_16_19_i](<https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances-2016e2019-inherit-1.2.6/data/inherit_scf_16_19_i.csv>)**. Extract of the 2016 and 2019 SCF for inheritance and networth, inflated to 2020 dollars


## Documentation

This is an extract of the 2016 and 2019 Survey of Consumer Finances, with extracted variables and recoded variables oriented toward studying inheritance.

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances-2016e2019-inherit-1.2.6/index.html>)


## Images

  * [![](https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances-2016e2019-inherit-1.2.6/docs/networth_race_inc.png)](<https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances-2016e2019-inherit-1.2.6/docs/networth_race_inc.png> "networth_race_inc") Net Worth by Income Percentile and Race


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

inherit_scf_16_19   


### inherit_scf_16_19

Column Name| Data Type| Description  
---|---|---  
year| integer| Year of the SCL reelase the record was drawn from  
case_id| integer|   
record_id| integer|   
implicate_id| integer| Impicate number, 1 to 5  
age_1| integer| Age of first household adult  
age_2| integer| Age of second household adult.  
hisp| integer| Is the HH Hispanic  
race| string| Simpified race for HH  
addtional_race| integer|   
unusual_income| integer|   
ed_1| string| Education of person 1  
ed_2| string| Education of person 2  
ed_mother_1| string| Education of person 1's mother  
ed_father_1| string| Education of person 1's father  
ed_mother_2| string| Education of person 2's mother  
ed_father_2| string| Education of person 2's father  
occ_1| integer| Occupation of person 1  
occ_2| integer| Occupation of person 2  
gi_other_value| integer|   
fin_risk| integer| Tolerance for financial risk  
shop_credit| integer|   
shop_credit_2| integer|   
fin_know| integer|   
borrow_vacation| integer| Is R willing to borrow to pay for a vacation.  
plan_horizon| integer|   
spend_exceeds| integer| Does spending exceed income?  
spend_exceeds_excl_house| integer| Does spending, excluding house payments, exceed income?  
wt0| number| HH weight  
gi_type_1| string|   
gi_value_1| integer|   
gi_year_1| integer|   
gi_from_1| integer|   
gi_type_2| string|   
gi_value_2| integer|   
gi_year_2| integer|   
gi_from_2| integer|   
gi_type_3| string|   
gi_value_3| integer|   
gi_year_3| integer|   
gi_from_3| integer|   
networth| number|   
income| number|   
nwcat| integer|   
nwpctlecat| integer| Networth percentile category  
norminc| number| Normal income  
ninccat| integer| Normal income category  
ninc2cat| integer| Normal income category, with fewer categories  
nincpctlecat| integer| Normal income percentil category  
occat1| integer| Occupational category for person 1  
occat2| integer| Occupational category for person 2  
edcl| string| Educational class  
lifecl| integer| Life stage category  
famstruct| integer| Family structure category  
married| integer| Is person 1 married?  
agecl| string| Age group category  
housecl| integer| House ownership category  
racecl| integer| Race category  
racecl4| integer| Race, with 4 categories  
asset| number|   
liq| number|   
bond| number|   
fin| number|   
nfin| number|   
debt| number|   
indcat| integer|   
equity| number|   
homeeq| number|   
revpay| number|   
bnkruplast5| integer|   
debt2inc| number|   
hsaving| integer|   
saved| integer|   
education| string|   
occ| integer|   
lt_planner| integer|   
nincpctle| integer|   
ninc| integer|   
nwpctle| integer|   
gi_sum| integer| Sum of the value of gift, trust or inheritance transfers  
n_gift| integer| Number of gift transfers  
n_inherit| integer| Number of inheritance transfers  
n_trust| integer| Number of trust transfers  
n_transfer| integer| Number of gift, trust or inheritance transfers  
any_transfer| integer| Has HH recieved any transfer?  
any_inherit| integer| Has HH recieved and inheritance?  
hhsize| integer| Household size. Actually the number of financially contributing adults in the analysis unit, either 1 or 2.  
networthpc| number| Networth divided by hhsize  
assetpc| number| Assets divided by hhsize  
gi_pv_10| number| Value of each gift or transfer, compounded ot the present at 10%  
gi_pv_7| number| Value of each gift or transfer, compounded ot the present at 7%  
gi_pv_5| number| Value of each gift or transfer, compounded ot the present at 5%  
gi_value_cd| number| Sum of transfers, with each transfer inflated to current dollars  
  
## References

Urls used in the creation of this data package.

  * **metapack+https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances.csv**. Survey of consumer finances data packages
  * **[cpi](<https://fred.stlouisfed.org/graph/fredgraph.csv?&id=CPIAUCSL>)**. Consumer Price Index


## Packages

  * **s3** s3://library.metatab.org/federalreserve.gov-consumer_finances-2016e2019-inherit-1.2.6.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances-2016e2019-inherit-1.2.6.csv>
  * **source** <https://github.com/insights-civickowledge-com/survey_consumer_finances.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    inherit_scf_16_19_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances-2016e2019-inherit-1.2.6/data/inherit_scf_16_19.csv')
    inherit_scf_16_19_i_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances-2016e2019-inherit-1.2.6/data/inherit_scf_16_19_i.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances-2016e2019-inherit-1.2.6.csv')
    
    # Create Dataframes
    inherit_scf_16_19_df = pkg.resource('inherit_scf_16_19').dataframe()
    inherit_scf_16_19_i_df = pkg.resource('inherit_scf_16_19_i').dataframe()
    
[/code]
