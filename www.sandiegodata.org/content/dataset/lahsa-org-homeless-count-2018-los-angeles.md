---
title: "LAHSA Homeless Count"
date: 2019-05-15T22:33:01+00:00
draft: false
categories: ["Dataset", "homelessness"]
tags: ["ckan", "homelessness", "lahsa.org", "los_angeles"]
author: "metapack"
description: "Counts of homeless per tract, from the Los Angeles Point In Time Count, for 2018"
---

_Counts of homeless per tract, from the Los Angeles Point In Time Count, for 2018_

`lahsa.org-homeless_count-2018-los_angeles-2`

Resources | Packages | Documentation| Contacts| Data Dictionary

## Resources

  * **[codebook](<https://library-metatab-org.s3.amazonaws.com/lahsa.org-homeless_count-2018-los_angeles-1/data/codebook.csv>)**. 
  * **[tracts](<https://library-metatab-org.s3.amazonaws.com/lahsa.org-homeless_count-2018-los_angeles-1/data/tracts.csv>)**. 
  * **[communities](<https://library-metatab-org.s3.amazonaws.com/lahsa.org-homeless_count-2018-los_angeles-1/data/communities.csv>)**. 


## Documentation

There are notes in the source Excel file, but they are embedded as an image, so these following notes are from OCR: 
[code] 
    Data Prepared by Los Angeles Homeless Services Authority
    
    Last updated 08/23/2018
    
    Components of the Homeless Count
    
    Street Count (all census tracts): Captures a point in time estimate of the
    unsheltered population.
    
    Shelter Count (from Homeless Management Integration System): Captures the
    homeless population in emergency shelters, transitional housing, and safe
    havens. The shelter count in this dataset excludes Cal WORKS hotel/ motel
    vouchers and domestic violence shelters for confidentiality reasons.
    
    Youth Count (sample census tracts): Collaborative process with youth
    stakeholders to better understand and identify homeless youth.
    
    Demographic Survey (sample census tracts): Captures the demographic
    characteristics of the unsheltered homeless population.
    
    Notes
    
    LAHSA does not recommend aggregating census tract-level data to calculate
    numbers for other geographic levels. Due to rounding, the census tract-level
    data may not add up to the total for Los Angeles City Council District,
    Supervisorial District, Service Planning Area, or the Los Angeles Continuum of
    Care.
    
    The Los Angeles Continuum of Care does not include the Cities of Long Beach,
    Glendale, and Pasadena and will not equal the countywide Homeless Count Total.
    
    Street Count Data include persons found outside, including persons found living
    in cars, vans, ca mpers/RVs, tents, and makeshift shelters. The conversion
    factors used to estimate the number of persons found Iivi ng outside are the
    following: For fa milies- Makeshift Shelter = 2.42, Car = 2.96, Van = 2.43, Ca
    mper/RV = 3.35, Tent = 2.75; For Individuals- Makeshift Shelter 1.67, Car =
    1.54, Van = 1.62, Camper/RV = 1.76, Tent = 1.52.
    
    Please visit https://www.lahsa.org/homeless-count/home to view and download
    data.
    
    Last updated 08/23/2018
    
    Eagle Rock/Arroyo Seco Boundaries were updated
    
[/code]

### Documentation Links

  * [Los Angeles Homeless Services Authority](<https://www.lahsa.org/>)
  * [Download](<https://www.lahsa.org/documents?id=2065-homeless-count-2018-results-by-census-tract.xlsx>)Dataset in downloadable form.


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)

  * **Creator**

Los Angeles Homeless Services Authority, <https://www.lahsa.org/>


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/lahsa.org-homeless_count-2018-los_angeles-1.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/lahsa.org-homeless_count-2018-los_angeles-1.csv>
  * **source** <https://github.com/SDRDLAnalysts/data-projects.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/lahsa.org-homeless_count-2018-los_angeles-1.zip')
    
    # Create Dataframes
    
    codebook_df = pkg.resource('codebook').dataframe()
    tracts_df = pkg.resource('tracts').dataframe()
    communities_df = pkg.resource('communities').dataframe()
[/code]

## Data Dictionary

codebook | tracts | communities   


### codebook

Column Name| Data Type| Description  
---|---|---  
column_name| string|   
description| string|   
  
### tracts

Column Name| Data Type| Description  
---|---|---  
tract| geoid| 2010 US Census Tract Code  
year| integer| Year Tract was Counted  
city| string| City Name  
lacity| integer| Whether tract in Los Angeles city (=1,0=county)  
community_name| string| Community Name  
detailed_name| string| City, Community, or Los Angeles Neighborhood Council  
spa| integer| Service Planning Area  
sd| integer| LA County Supervisorial District  
cd| integer| City Council District  
ca_ssd| integer| State Senate District  
ca_sad| integer| State Assembly District  
us_cd| integer| US Congressional District  
demogsurvct| integer| # Valid Adult Demographic Surveys  
youthsurvct| integer| # Valid Youth Demographic Surveys  
shelthmisct| integer| # Valid HMIS Individual Records  
sheltercountany| integer| Whether any shelters reported in tract  
streetcountany| integer| Whether PIT count reported in tract  
totstreetsingadult| integer| Single adults over 24 years old counted during the Street Count  
totstreetfamhh| integer| Family households counted during the Street Count  
totstreetfammem| integer| Total family members counted during the Street Count  
totcars| integer| Cars tabulated during the Street Count  
totvans| integer| Vans tabulated during the Street Count  
totcampers| integer| Campers tabulated during the Street Count  
tottents| integer| Tents tabulated during the Street Count  
totmakeshift| integer| Makeshift shelters tabulated during the Street Count  
totcarpeople| number| People calculated living in cars  
totvanpeople| number| People calculated living in vans  
totcamperpeople| number| People calculated living in campers  
tottentpeople| number| People calculated living in Tents  
totmakeshiftpeople| number| People calculated living in encampments (makeshift shelters)  
famcarhh| number| Family Households calculated living in cars  
famvanhh| number| Family Households calculated living in vans  
famcamperhh| number| Family Households calculated living in campers  
famtenthh| number| Family Households calculated living in Tents  
fammakeshifthh| number| Family Households calculated living in encampments (makeshift shelters)  
famcarpeople| number| Family Members calculated living in cars  
famvanpeople| number| Family Members calculated living in vans  
famcamperpeople| number| Family Members calculated living in campers  
famtentpeople| number| Family Members calculated living in Tents  
fammakeshiftpeople| number| Family Members calculated living in encampments (makeshift shelters)  
indcarpeople| number| Individuals calculated living in cars  
indvanpeople| number| Individuals calculated living in vans  
indcamperpeople| number| Individuals calculated living in campers  
indtentpeople| number| Individuals calculated living in Tents  
indmakeshiftpeople| number| Individuals calculated living in encampments (makeshift shelters)  
totesadultsingadult| integer| Total single adults over 24 years old in emergency shelter  
totesadultfamhh| integer| Total family households, with head of household over 24, in emergency shelter  
totesadultfammem| integer| Total family members, with head of household over 24, in emergency shelter  
totesyouthsingyouth| integer| Total youth ages 18 to 24 counted in emergency shelter  
totesyouthfamhh| integer| Total family households, with head of household age 18 to 24, in emergency shelter  
totesyouthfammem| integer| Total family members, with head of household 18 to 24, in emergency shelter  
totesyouthunaccyouth| integer| Total unaccompanied minors, under 18 years in emergency shelter  
totthadultsingadult| integer| Total single adults over 24 years old in transitional housing  
totthadultfamhh| integer| Total family households, with head of household over 24, in transitional housing  
totthadultfammem| integer| Total family members, with head of household over 24, in transitional housing  
totthyouthsingyouth| integer| Total youth ages 18 to 24 counted in transitional housing  
totthyouthfamhh| integer| Total family households, with head of household age 18 to 24, in transitional housing  
totthyouthfammem| integer| Total family members, with head of household 18 to 24, in transitional housing  
totthyouthunaccyouth| integer| Total unaccompanied minors, under 18 years in transitional housing  
totshadultsingadult| integer| Total single adults over 24 years old in safe havens  
totshadultfamhh| integer| Total family households, with head of household over 24, in safe havens  
totshadultfammem| integer| Total family members, with head of household over 24, in safe havens  
totshyouthsingyouth| integer| Total youth ages 18 to 24 counted in safe havens  
totshyouthfamhh| integer| Total family households, with head of household age 18 to 24, in safe havens  
totshyouthfammem| integer| Total family members, with head of household 18 to 24, in safe havens  
totshyouthunaccyouth| integer| Total unaccompanied minors, under 18 years in safe havens  
totunsheltpeople| number| Total population of unsheltered homeless persons  
totespeople| integer| Total population in emergency shelter  
totthpeople| integer| Total population in transitional housing  
totshpeople| integer| Total population in safe havens  
totsheltpeople| integer| Total population of sheltered homeless persons  
totpeople| number| Total population of sheltered and unsheltered homeless persons  
  
### communities

Column Name| Data Type| Description  
---|---|---  
year| integer| Year Tract was Counted  
community_name| text| Community Name  
city| text| City Name  
lacity| integer| Whether tract in Los Angeles city (=1,0=county)  
spa| integer| Service Planning Area  
sd| integer| LA County Supervisorial District  
demogsurvct| integer| # Valid Adult Demographic Surveys  
youthsurvct| integer| # Valid Youth Demographic Surveys  
shelthmisct| integer| # Valid HMIS Individual Records  
totstreetsingadult| integer| Single adults over 24 years old counted during the Street Count  
totstreetfamhh| integer| Family households counted during the Street Count  
totstreetfammem| integer| Total family members counted during the Street Count  
totcars| integer| Cars tabulated during the Street Count  
totvans| integer| Vans tabulated during the Street Count  
totcampers| integer| Campers tabulated during the Street Count  
tottents| integer| Tents tabulated during the Street Count  
totmakeshift| integer| Makeshift shelters tabulated during the Street Count  
totcarpeople| number| People calculated living in cars  
totvanpeople| number| People calculated living in vans  
totcamperpeople| number| People calculated living in campers  
tottentpeople| number| People calculated living in Tents  
totmakeshiftpeople| number| People calculated living in encampments (makeshift shelters)  
famcarhh| number| Family Households calculated living in cars  
famvanhh| number| Family Households calculated living in vans  
famcamperhh| number| Family Households calculated living in campers  
famtenthh| number| Family Households calculated living in Tents  
fammakeshifthh| number| Family Households calculated living in encampments (makeshift shelters)  
famcarpeople| number| Family Members calculated living in cars  
famvanpeople| number| Family Members calculated living in vans  
famcamperpeople| number| Family Members calculated living in campers  
famtentpeople| number| Family Members calculated living in Tents  
fammakeshiftpeople| number| Family Members calculated living in encampments (makeshift shelters)  
indcarpeople| number| Individuals calculated living in cars  
indvanpeople| number| Individuals calculated living in vans  
indcamperpeople| number| Individuals calculated living in campers  
indtentpeople| number| Individuals calculated living in Tents  
indmakeshiftpeople| number| Individuals calculated living in encampments (makeshift shelters)  
totesadultsingadult| integer| Total single adults over 24 years old in emergency shelter  
totesadultfamhh| integer| Total family households, with head of household over 24, in emergency shelter  
totesadultfammem| integer| Total family members, with head of household over 24, in emergency shelter  
totesyouthsingyouth| integer| Total youth ages 18 to 24 counted in emergency shelter  
totesyouthfamhh| integer| Total family households, with head of household age 18 to 24, in emergency shelter  
totesyouthfammem| integer| Total family members, with head of household 18 to 24, in emergency shelter  
totesyouthunaccyouth| integer| Total unaccompanied minors, under 18 years in emergency shelter  
totthadultsingadult| integer| Total single adults over 24 years old in transitional housing  
totthadultfamhh| integer| Total family households, with head of household over 24, in transitional housing  
totthadultfammem| integer| Total family members, with head of household over 24, in transitional housing  
totthyouthsingyouth| integer| Total youth ages 18 to 24 counted in transitional housing  
totthyouthfamhh| integer| Total family households, with head of household age 18 to 24, in transitional housing  
totthyouthfammem| integer| Total family members, with head of household 18 to 24, in transitional housing  
totthyouthunaccyouth| integer| Total unaccompanied minors, under 18 years in transitional housing  
totshadultsingadult| integer| Total single adults over 24 years old in safe havens  
totshadultfamhh| integer| Total family households, with head of household over 24, in safe havens  
totshadultfammem| integer| Total family members, with head of household over 24, in safe havens  
totshyouthsingyouth| integer| Total youth ages 18 to 24 counted in safe havens  
totshyouthfamhh| integer| Total family households, with head of household age 18 to 24, in safe havens  
totshyouthfammem| integer| Total family members, with head of household 18 to 24, in safe havens  
totshyouthunaccyouth| integer| Total unaccompanied minors, under 18 years in safe havens  
totunsheltpeople| number| Total population of unsheltered homeless persons  
totespeople| integer| Total population in emergency shelter  
totthpeople| integer| Total population in transitional housing  
totshpeople| integer| Total population in safe havens  
totsheltpeople| integer| Total population of sheltered homeless persons  
totpeople| number| Total population of sheltered and unsheltered homeless persons  
  
Last Modified 2019-07-04T23:08:29

## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/lahsa.org-homeless_count-2018-los_angeles-1.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/lahsa.org-homeless_count-2018-los_angeles-1.csv>
  * **source** <https://github.com/SDRDLAnalysts/data-projects.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/lahsa.org-homeless_count-2018-los_angeles-1.zip')
    
    # Create Dataframes
    
    codebook_df = pkg.resource('codebook').dataframe()
    tracts_df = pkg.resource('tracts').dataframe()
    communities_df = pkg.resource('communities').dataframe()
[/code]
