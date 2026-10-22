---
title: "Unduplicated Pupil Counts"
date: 2019-05-23T03:37:23+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "education"]
author: "metapack"
description: "Downloadable files for the Unduplicated Pupil Count (UPC) of free or reduced"
---

_Downloadable files for the Unduplicated Pupil Count (UPC) of free or reduced price meal (FRPM) eligibility, English learner (EL), and foster youth data from the California Longitudinal Pupil Achievement Data System (CALPADS)._

`cde.ca.gov-calpads_upc-1.1.1`. Modified 2021-03-11T00:51:50


## Resources

  * **[upc_13_lea](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_13_lea.csv>)**. Unduplicated pupil count, academic year 2013, LEA Level
  * **[upc_13_school](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_13_school.csv>)**. Unduplicated pupil count, academic year 2013, School Level
  * **[upc_14_lea](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_14_lea.csv>)**. Unduplicated pupil count, academic year 2014, LEA Level
  * **[upc_14_school](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_14_school.csv>)**. Unduplicated pupil count, academic year 2014, School Level
  * **[upc_15_lea](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_15_lea.csv>)**. Unduplicated pupil count, academic year 2015, LEA Level
  * **[upc_15_school](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_15_school.csv>)**. Unduplicated pupil count, academic year 2015, School Level
  * **[upc_16_lea](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_16_lea.csv>)**. Unduplicated pupil count, academic year 2016, LEA Level
  * **[upc_16_school](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_16_school.csv>)**. Unduplicated pupil count, academic year 2016, School Level
  * **[upc_17_lea](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_17_lea.csv>)**. Unduplicated pupil count, academic year 2017, LEA Level
  * **[upc_17_school](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_17_school.csv>)**. Unduplicated pupil count, academic year 2017, School Level
  * **[upc_combined_lea](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_combined_lea.csv>)**. Combined LEA files, 2014 on
  * **[upc_combined_school](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_combined_school.csv>)**. Combined LEA files, 2014 on


## Documentation

Unduplicated Pupil Counts are the counts of pupils that are in one or more categories of eligibility for free or reduced price meals (FRMP), an important part of the Local Control Funding Formula.

### Documentation Links

  * [Source file overview](<https://www.cde.ca.gov/ds/sd/sd/filescupc1617.asp>) Additional details of the counting process
  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/index.html>)
  * [Dataset home page](<https://www.cde.ca.gov/ds/sd/sd/filescupc.asp>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

upc_13 | upc_14 | upc_combined   


### upc_13

Column Name| Data Type| Description  
---|---|---  
academic_year| string|   
county_code| integer|   
district_code| integer|   
school_code| integer|   
county_name| string|   
district_name| string|   
school_name| string|   
district_type| string|   
school_type| string|   
nslp_provision_2_or_3_school_y_n| string|   
charter_number| string|   
charter_funding_type| string|   
low_grade| string|   
high_grade| string|   
enrollment_k_12| integer|   
unduplicated_frpm_eligible_count_unadjusted| integer|   
english_learner_el_count| integer|   
cdss_foster_youth_count| integer|   
unduplicated_frpm_el_foster_count_unadjusted| integer|   
directly_certified_dec_feb_count| integer|   
unduplicated_frpm_el_foster_count_adjusted| integer|   
unduplicated_non_juvenile_hall_pupil_count| integer|   
unduplicated_juvenile_hall_pupil_count| integer|   
calpads_unduplicated_pupil_count_upc| integer|   
2013_14_calpads_fall_1_certification_status_y_n| string|   
  
### upc_14

Column Name| Data Type| Description  
---|---|---  
academic_year| string|   
county_code| integer|   
district_code| integer|   
school_code| integer|   
county_name| string|   
district_name| string|   
school_name| text|   
district_type| string|   
school_type| string|   
educational_option_type| string|   
nslp_provision_status| string|   
charter_school_y_n| string|   
charter_number| string|   
charter_funding_type| string|   
irc| string|   
low_grade| string|   
high_grade| string|   
total_enrollment| integer|   
free_reduced_meal_program| integer|   
foster| integer|   
homeless| integer|   
migrant_program| integer|   
direct_certification| integer|   
unduplicated_frpm_eligible_count| integer|   
english_learner_el| integer|   
calpads_unduplicated_pupil_count_upc| integer|   
calpads_fall_1_certification_status_y_n| string|   
  
### upc_combined

Column Name| Data Type| Description  
---|---|---  
file_year| integer|   
academic_year| string| The academic year corresponding to the annual Census Day from which official enrollment counts are determined using data submitted as part of the annual Fall 1 submission to the California Longitudinal Pupil Achievement Data System (CALPADS) by local educational agencies (LEAs), which includes school districts, charter schools, and county offices of education. Census Day or Information Day is always the first Wednesday in October.  
county_code| integer| A unique two-digit code corresponding to the county.  
district_code| integer| A unique five-digit code corresponding to the district.  
school_code| integer| A unique seven-digit code corresponding to the school.  
county_name| string| County Name  
district_name| string| District or Administrative Authority Name  
school_name| string| School Name  
district_type| string| District Ownership Type Description  
school_type| string| School Ownership Type Description  
educational_option_type| string| Educational Option Type Description  
nslp_provision_status| string| The values in this field indicate the school-level National School Lunch Program Provision Status for lunch and breakfast. Where no lunch or breakfast provision is specified, then the specified provision applies to both lunch and breakfast. Values are as follows: Community Eligibility Provision (CEP), Provision 1, Provision 2, Provision 3, Lunch Provision 1, Lunch Provision 2, Lunch Provision 3, Breakfast Provision 1, Breakfast Provision 2, Breakfast Provision 3, Multiple Provision Types, or N/A. This information is provided for informational purposes only. No special adjustments were made in the data for provision schools. For more information on NSLP provision status, please refer to the United States Department of Agriculture (USDA) School Meals Guidance and Resources Webpage.  
charter_school| string| A "Y" or "N" value indicating whether a school is a charter school in the current academic year.  
charter_number| string| A four character value (any combination of numbers and letters) assigned to a charter school. A blank value indicates the school is not a charter school.  
charter_funding_type| string| The values in this field indicate the charter school funding type. Values are as follows: Locally funded, Directly funded, Not in Charter School funding model, or Blank.  
irc| string| A "Y" or "N" value indicating whether a school is an independently reporting charter (IRC) school in the current academic year.  
low_grade| string| Lowest grade offered  
high_grade| string| Highest grade offered  
total_enrollment| integer| A total count of all K-12 students enrolled (primary or short-term) on Census Day. This count corresponds to the "Total Enrollment" count provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth - Count.  
frmp| integer| Of the Total Enrollment, a total count of students reported being eligible on Census Day for the National School Lunch Program (NSLP) based on Education Program records with an Education Program Membership Code 181 (Free) or 182 (Reduced). This count corresponds to the "Free & Reduced Meal Program 181/182" count provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth - Count.  
foster| integer| Of the Total Enrollment, a total count of students identified through the weekly CALPADS Foster Matching process or matched by the LEA through the CALPADS online match process as being in Foster Students on Census Day. This count corresponds to the "Foster" count provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth - Count.  
homeless| integer| Of the Total Enrollment, a total count of students reported as being homeless on Census Day based on Education Program record with an Education Program Membership Code 191 (Homeless). This count corresponds to the "Homeless" count provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth - Count.  
migrant_program| integer| Of the Total Enrollment, a total count of students eligible for the Migrant Education Program on Census Day based on and Education Program record with an Education Program Membership Code 135 (Migrant). This count corresponds to the "Migrant Program: 135" count provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth - Count.  
direct_certification| integer| Of the Total Enrollment, a total count of students identified as being "directly certified" through CALPADS as participating in California's food stamp or CalWORKs programs during July - November and who are therefore eligible for free meals. This count corresponds to the "Direct Certification" count provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth - Count.  
frpm_eligible| integer| Of the Total Enrollment, a total unduplicated count of students who meet household income or categorical eligibility criteria for free or reduced price meals (FRPM) based on applying for the National School Lunch Program (NSLP); submitting alternative household income forms; their foster, homeless, or migrant statuses in CALPADS; or being "directly certified" through CALPADS as participating in California's food stamp or CalWORKs programs during July - November. This count corresponds to the "Unduplicated Eligible Free/Reduced Meal Counts" provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth - Count. This count does NOT represent the "official" FRPM eligible count because early TK children have been removed (Kindergarten students who turn five years old after December 2).  
english_learnerl| integer| Of the Total Enrollment, a count of students identified in CALPADS as English learners (EL) on Census Day. This count corresponds to the "EL Funding Eligible" count provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth - Count.  
unduplicated_pupils| integer| Of the Total Enrollment, an unduplicated count of students who are FRPM eligible (including foster youth students) or EL eligible. This count corresponds to the "Total Unduplicated FRPM/EL Eligible Count" provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth - Count.  
certification_status| string| A "Y" or "N" value indicating whether data were submitted and certified in CALPADS. No data are provided where the certification status is "N".  
  
## Packages

  * **s3** s3://cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1.csv>
  * **source** <https://github.com/Metatab/metatab-packages.git>


### Accessing Data in Vanilla Pandas
```
import pandas as pd


upc_13_lea_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_13_lea.csv')
upc_13_school_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_13_school.csv')
upc_14_lea_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_14_lea.csv')
upc_14_school_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_14_school.csv')
upc_15_lea_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_15_lea.csv')
upc_15_school_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_15_school.csv')
upc_16_lea_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_16_lea.csv')
upc_16_school_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_16_school.csv')
upc_17_lea_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_17_lea.csv')
upc_17_school_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_17_school.csv')
upc_combined_lea_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_combined_lea.csv')
upc_combined_school_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1/data/upc_combined_school.csv')
```

### Accessing Package in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-calpads_upc-1.1.1.csv')

# Create Dataframes
upc_13_lea_df = pkg.resource('upc_13_lea').dataframe()
upc_13_school_df = pkg.resource('upc_13_school').dataframe()
upc_14_lea_df = pkg.resource('upc_14_lea').dataframe()
upc_14_school_df = pkg.resource('upc_14_school').dataframe()
upc_15_lea_df = pkg.resource('upc_15_lea').dataframe()
upc_15_school_df = pkg.resource('upc_15_school').dataframe()
upc_16_lea_df = pkg.resource('upc_16_lea').dataframe()
upc_16_school_df = pkg.resource('upc_16_school').dataframe()
upc_17_lea_df = pkg.resource('upc_17_lea').dataframe()
upc_17_school_df = pkg.resource('upc_17_school').dataframe()
upc_combined_lea_df = pkg.resource('upc_combined_lea').dataframe()
upc_combined_school_df = pkg.resource('upc_combined_school').dataframe()
```
