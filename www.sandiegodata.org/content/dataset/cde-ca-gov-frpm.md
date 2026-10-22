---
title: "Student Poverty FRPM Data"
date: 2019-05-23T03:37:38+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "education"]
author: "metapack"
description: "Data files pertaining to students eligible for Free or Reduced Price Meals"
---

_Data files pertaining to students eligible for Free or Reduced Price Meals (FRPM)._

`cde.ca.gov-frpm-1.2.1`. Modified 2021-03-11T00:51:02


## Resources

  * **[frp_meals](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-frpm-1.2.1/data/frp_meals.csv>)**. Combined data, 2004 to 2018


## Documentation

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-frpm-1.2.1/index.html>)
  * [Homepage](<https://www.cde.ca.gov/ds/sd/sd/filessp.asp>) Dataset home page


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

combined | frp_meals   


### combined

Column Name| Data Type| Description  
---|---|---  
year| integer|   
academic_year| string| The academic year corresponding to the annual Census Day from which official enrollment counts are determined using data submitted to the California Longitudinal Pupil Achievement Data System (CALPADS) by districts and charter schools. Census Day or Information Day is always the first Wednesday in October.  
county_code| integer| A unique two-digit code corresponding to the county.  
county_name| string|   
district_code| integer| A unique five-digit code corresponding to the district.  
district_name| string| District or Administrative Authority Name  
district_type| string|   
school_code| integer| A unique seven-digit code corresponding to the school.  
school_name| text|   
school_type| string|   
lea_name| string| Local educational agency (LEA) name.  
charter_funding_type| string| Indicates the charter school funding type. Values are as follows: Locally funded, Directly funded, Not in Charter School funding model, or Blank.  
charter_school_number| string| A four character value (any combination of numbers and letters) assigned to a charter school. A blank value indicates the school is not a charter school.  
charter_school_y_n| string| A "Y" or "N" value indicating whether a school is a charter school in the current academic year.  
direct_funded_charter_school_number| string|   
low_grade| string|   
high_grade| string|   
educational_option_type| string|   
irc| string|   
fund_type| string|   
nslp_provision_2_or_3_school| string| A Y or N value to indicate whether a school is on a National School Lunch Program (NSLP) provision 2 or 3 status. "Y" indicates the school is on a provisional status; "N" indicates the school is not. For more information on provision status, please refer to the United States Department of Agriculture (USDA) Food Nutrition Service Web page External link opens in new window or tab..  
nslp_provision_status| string|   
provision_2_or_3_school_y_n| string|   
calpads_enrollment| integer| A total count of students ages 5-17 enrolled (primary or short-term) on Census Day (the first Wednesday in October). These data were submitted to CALPADS as part of the annual Fall 1 submission.  
calpads_enrollment_k_12| integer|   
enrollment| integer| A total count of students ages 5-17 enrolled (primary or short-term) on Census Day (the first Wednesday in October). These data were submitted to CALPADS as part of the annual Fall 1 submission.  
enrollment_k_12| integer| A total count of K-12 students enrolled (primary or short-term) on Census Day (the first Wednesday in October). These data were submitted to CALPADS as part of the annual Fall 1 submission.  
calpads_fall_1_certification_status| string| A Y or N value to indicate whether data were submitted and certified in CALPADS. No data are provided where the certification status is "N".  
free_meal_count| string|   
free_meal_count_k_12| integer| Of the Enrollment (K-12), a total unduplicated count of students who meet household income or categorical eligibility criteria for free meals based on one or more of the following reasons: (1) applying for the National School Lunch Program (NSLP); (2) submitting alternative household income forms; (3) student homeless or migrant statuses in CALPADS; (4) being "directly certified" through CALPADS as participating in California's food stamp or CalWORKs programs during July - November; or (5) being identified through the weekly CALPADS Foster Matching process or matched by the LEA through the CALPADS online match process as being in Foster Placement or Foster Family Maintenance on Census day. The Free Meal Count (K-12) is not displayed on any CALPADS report; however, this count represents the official Free Meal Count (K-12) for the academic year.  
frpm_count| integer| Of the Enrollment (Ages 5-17), a total unduplicated count of students who meet household income or categorical eligibility criteria for free or reduced meals (FRPM) based on one or more of the following reasons: (1) applying for the National School Lunch Program (NSLP); (2) submitting alternative household income forms; (3) student homeless or migrant statuses in CALPADS; (4) being "directly certified" through CALPADS as participating in California's food stamp or CalWORKs programs during July - November; or (5) being identified through the weekly CALPADS Foster Matching process or matched by the LEA through the CALPADS online match process as being in Foster Placement or Foster Family Maintenance on Census day. The FRPM Count (Ages 5-17) generally corresponds to the "Total Unduplicated Eligible Free/Reduced Meal Counts" provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth – Count with the 5-17 Year Olds filter applied; however, this count has been augmented to also included students identified as being in Foster Family Maintenance on Census Day, as these students have been determined to be categorically eligible for free meals. This adjustment was made outside of CALPADS and is not included in the "Total Unduplicated Eligible Free/Reduced Meal Counts" provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth – Count; however, this count represents the official FRPM Count (Ages 5-17) for the academic year.  
frpm_count_k_12| integer| Of the Enrollment (K-12), a total unduplicated count of students who meet household income or categorical eligibility criteria for free or reduced meals (FRPM) based on one or more of the following reasons: (1) applying for the National School Lunch Program (NSLP); (2) submitting alternative household income forms; (3) student homeless or migrant statuses in CALPADS; (4) being "directly certified" through CALPADS as participating in California's food stamp or CalWORKs programs during July - November; or (5) being identified through the weekly CALPADS Foster Matching process or matched by the LEA through the CALPADS online match process as being in Foster Placement or Foster Family Maintenance on Census day. The FRPM Count (K-12) generally corresponds to the "Total Unduplicated Eligible Free/Reduced Meal Counts" provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth – Count; however, this count has been augmented to also included students identified as being in Foster Family Maintenance on Census Day, as these students have been determined to be categorically eligible for free meals. This adjustment was made outside of CALPADS and is not included in the "Total Unduplicated Eligible Free/Reduced Meal Counts" provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth – Count; however, this count represents the official FRPM Count (K-12) for the academic year.  
frpm_total_unduplicated_count| string| Of the students (Ages 5–17) enrolled in the school, the total unduplicated count of students who are eligible to receive free or reduced price meals (FRPM). Students may be eligible for free meals based on applying for the National School Lunch Program (NSLP), or who are determined to meet the same income eligibility criteria as the NSLP, through their local schools, their homeless, migrant, or foster status, or participation in California's food stamp program. There are no counts provided for Provision 2 and 3 schools because only percentages were collected for these schools; as a result, a value of "NULL" is displayed instead of counts of students eligible.  
frpm_total_unduplicated_count_k_12| string| Of the students (K–12) enrolled in the school, the total unduplicated count of who are eligible to receive free or reduced price meals (FRPM). Students may be eligible for free meals based on applying for the National School Lunch Program (NSLP), or who are determined to meet the same income eligibility criteria as the NSLP, through their local schools, their homeless, migrant, or foster status, or participation in California’s food stamp program. There are no counts provided for Provision 2 and 3 schools because only percentages were collected for these schools; as a result, a value of "NULL" is displayed instead of counts of students eligible.  
percent_eligible_free| number| The percent of students eligible for free meals. [Free Meal Count (Ages 5-17) divided by Enrollment (Ages 5-17)].  
percent_eligible_free_k_12| number| The percent of students eligible for free meals. [Free Meal Count (K-12) divided by Enrollment (K-12)].  
percent_eligible_frpm| number| The percent of students eligible for free or reduced price meals (FRPM). [FRPM Count (Ages 5-17) divided by Enrollment (Ages 5-17)].  
percent_eligible_frpm_k_12| number| The percent of students eligible for free or reduced price meals (FRPM). [FRPM Count (K-12) divided by Enrollment (K-12)].  
percent_frpm| number|   
reduced_price_meals| integer|   
total_frpm| integer|   
unadjusted_free_meal_count| integer|   
unadjusted_free_meal_count_k_12| integer|   
unadjusted_frpm_count| integer| Of the Enrollment (K-12) count, a total unduplicated count of students who are eligible to receive free meals. Students may be eligible for free meals based on applying for the National School Lunch Program (NSLP), or who are determined to meet the same income eligibility criteria as the NSLP through their local schools, or their homeless, migrant, or foster status in CALPADS, or those students "directly certified" as participating in California's food stamp program during July - November 2013. This count corresponds to the "Free Meal Count" provided in the CALPADS certification report 5.1a: Free or Reduced Price Meal Eligibility – Count.  
unadjusted_frpm_count_k_12| integer| Of the Enrollment (K-12) count, a total unduplicated count of students who are eligible to receive free or reduced price meals (FRPM). Students may be eligible for free or reduced price meals based on applying for the National School Lunch Program (NSLP), or who are determined to meet the same income eligibility criteria as the NSLP through their local schools, or their homeless, migrant, or foster status in CALPADS, or those students "directly certified" as participating in California's food stamp program during July - November 2013. This count corresponds to the "Free & Reduced Meal Count" provided in the CALPADS certification report 5.1a: Free or Reduced Price Meal Eligibility - Count.  
data_source_for_frpm| string|   
data_source_for_provision_2_or_3_school| string| This indicates the data source for Provision 2 or 3 school data. "NSD" indicates that the data are sourced from October 2012 claim data submitted to the CDE's Nutrition Services Division (NSD); "CARS" indicates that the data are sourced from base percentages that LEAs certified in the Consolidated Application and Reporting System (CARS) in 2011–12. Since only percentages were collected for Provision 2 and 3 schools, a value of "NULL" is displayed instead of counts of students eligible for these schools.  
  
### frp_meals

Column Name| Data Type| Description  
---|---|---  
county_code| integer| A unique two-digit code corresponding to the county.  
district_code| integer| A unique five-digit code corresponding to the district.  
school_code| integer| A unique seven-digit code corresponding to the school.  
charter_school_number| integer| A four character value (any combination of numbers and letters) assigned to a charter school. A blank value indicates the school is not a charter school.  
charter_funding_type| string| Indicates the charter school funding type. Values are as follows: Locally funded, Directly funded, Not in Charter School funding model, or Blank.  
lea_name| string| Local educational agency (LEA) name.  
school_name| text|   
low_grade| string|   
high_grade| integer|   
enrollment| integer| A total count of students ages 5-17 enrolled (primary or short-term) on Census Day (the first Wednesday in October). These data were submitted to CALPADS as part of the annual Fall 1 submission.  
free_meal_count| integer|   
reduced_price_meals| integer|   
total_frpm| integer|   
percent_frpm| number|   
county_name| string|   
data_source_for_frpm| string|   
academic_year| string| The academic year corresponding to the annual Census Day from which official enrollment counts are determined using data submitted to the California Longitudinal Pupil Achievement Data System (CALPADS) by districts and charter schools. Census Day or Information Day is always the first Wednesday in October.  
provision_2_or_3_school_y_n| string|   
data_source_for_provision_2_or_3_school| string| This indicates the data source for Provision 2 or 3 school data. "NSD" indicates that the data are sourced from October 2012 claim data submitted to the CDE's Nutrition Services Division (NSD); "CARS" indicates that the data are sourced from base percentages that LEAs certified in the Consolidated Application and Reporting System (CARS) in 2011–12. Since only percentages were collected for Provision 2 and 3 schools, a value of "NULL" is displayed instead of counts of students eligible for these schools.  
free_meal_count_k_12| integer| Of the Enrollment (K-12), a total unduplicated count of students who meet household income or categorical eligibility criteria for free meals based on one or more of the following reasons: (1) applying for the National School Lunch Program (NSLP); (2) submitting alternative household income forms; (3) student homeless or migrant statuses in CALPADS; (4) being "directly certified" through CALPADS as participating in California's food stamp or CalWORKs programs during July - November; or (5) being identified through the weekly CALPADS Foster Matching process or matched by the LEA through the CALPADS online match process as being in Foster Placement or Foster Family Maintenance on Census day. The Free Meal Count (K-12) is not displayed on any CALPADS report; however, this count represents the official Free Meal Count (K-12) for the academic year.  
percent_eligible_free_k_12| number| The percent of students eligible for free meals. [Free Meal Count (K-12) divided by Enrollment (K-12)].  
frpm_total_unduplicated_count_k_12| string| Of the students (K–12) enrolled in the school, the total unduplicated count of who are eligible to receive free or reduced price meals (FRPM). Students may be eligible for free meals based on applying for the National School Lunch Program (NSLP), or who are determined to meet the same income eligibility criteria as the NSLP, through their local schools, their homeless, migrant, or foster status, or participation in California’s food stamp program. There are no counts provided for Provision 2 and 3 schools because only percentages were collected for these schools; as a result, a value of "NULL" is displayed instead of counts of students eligible.  
percent_eligible_frpm_k_12| number| The percent of students eligible for free or reduced price meals (FRPM). [FRPM Count (K-12) divided by Enrollment (K-12)].  
calpads_enrollment| integer| A total count of students ages 5-17 enrolled (primary or short-term) on Census Day (the first Wednesday in October). These data were submitted to CALPADS as part of the annual Fall 1 submission.  
percent_eligible_free| number| The percent of students eligible for free meals. [Free Meal Count (Ages 5-17) divided by Enrollment (Ages 5-17)].  
nslp_provision_2_or_3_school| string| A Y or N value to indicate whether a school is on a National School Lunch Program (NSLP) provision 2 or 3 status. "Y" indicates the school is on a provisional status; "N" indicates the school is not. For more information on provision status, please refer to the United States Department of Agriculture (USDA) Food Nutrition Service Web page External link opens in new window or tab..  
unadjusted_free_meal_count_k_12| integer|   
unadjusted_frpm_count_k_12| integer| Of the Enrollment (K-12) count, a total unduplicated count of students who are eligible to receive free or reduced price meals (FRPM). Students may be eligible for free or reduced price meals based on applying for the National School Lunch Program (NSLP), or who are determined to meet the same income eligibility criteria as the NSLP through their local schools, or their homeless, migrant, or foster status in CALPADS, or those students "directly certified" as participating in California's food stamp program during July - November 2013. This count corresponds to the "Free & Reduced Meal Count" provided in the CALPADS certification report 5.1a: Free or Reduced Price Meal Eligibility - Count.  
frpm_count_k_12| integer| Of the Enrollment (K-12), a total unduplicated count of students who meet household income or categorical eligibility criteria for free or reduced meals (FRPM) based on one or more of the following reasons: (1) applying for the National School Lunch Program (NSLP); (2) submitting alternative household income forms; (3) student homeless or migrant statuses in CALPADS; (4) being "directly certified" through CALPADS as participating in California's food stamp or CalWORKs programs during July - November; or (5) being identified through the weekly CALPADS Foster Matching process or matched by the LEA through the CALPADS online match process as being in Foster Placement or Foster Family Maintenance on Census day. The FRPM Count (K-12) generally corresponds to the "Total Unduplicated Eligible Free/Reduced Meal Counts" provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth – Count; however, this count has been augmented to also included students identified as being in Foster Family Maintenance on Census Day, as these students have been determined to be categorically eligible for free meals. This adjustment was made outside of CALPADS and is not included in the "Total Unduplicated Eligible Free/Reduced Meal Counts" provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth – Count; however, this count represents the official FRPM Count (K-12) for the academic year.  
unadjusted_free_meal_count| integer|   
unadjusted_frpm_count| integer| Of the Enrollment (K-12) count, a total unduplicated count of students who are eligible to receive free meals. Students may be eligible for free meals based on applying for the National School Lunch Program (NSLP), or who are determined to meet the same income eligibility criteria as the NSLP through their local schools, or their homeless, migrant, or foster status in CALPADS, or those students "directly certified" as participating in California's food stamp program during July - November 2013. This count corresponds to the "Free Meal Count" provided in the CALPADS certification report 5.1a: Free or Reduced Price Meal Eligibility – Count.  
frpm_count| integer| Of the Enrollment (Ages 5-17), a total unduplicated count of students who meet household income or categorical eligibility criteria for free or reduced meals (FRPM) based on one or more of the following reasons: (1) applying for the National School Lunch Program (NSLP); (2) submitting alternative household income forms; (3) student homeless or migrant statuses in CALPADS; (4) being "directly certified" through CALPADS as participating in California's food stamp or CalWORKs programs during July - November; or (5) being identified through the weekly CALPADS Foster Matching process or matched by the LEA through the CALPADS online match process as being in Foster Placement or Foster Family Maintenance on Census day. The FRPM Count (Ages 5-17) generally corresponds to the "Total Unduplicated Eligible Free/Reduced Meal Counts" provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth – Count with the 5-17 Year Olds filter applied; however, this count has been augmented to also included students identified as being in Foster Family Maintenance on Census Day, as these students have been determined to be categorically eligible for free meals. This adjustment was made outside of CALPADS and is not included in the "Total Unduplicated Eligible Free/Reduced Meal Counts" provided in CALPADS certification report 1.17: FRPM/English Learner/Foster Youth – Count; however, this count represents the official FRPM Count (Ages 5-17) for the academic year.  
calpads_fall_1_certification_status| string| A Y or N value to indicate whether data were submitted and certified in CALPADS. No data are provided where the certification status is "N".  
district_type| string|   
school_type| string|   
educational_option_type| string|   
nslp_provision_status| string|   
charter_school_y_n| string| A "Y" or "N" value indicating whether a school is a charter school in the current academic year.  
irc| string|   
  
## References

Urls used in the creation of this data package.

  * **index:cde.ca.gov-frpm-source**. 
  * **data/column-map.csv**. 


## Packages

  * **s3** s3://cde.metatab.org/cde.ca.gov-frpm-1.2.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-frpm-1.2.1.csv>
  * **source** <https://github.com/Metatab/metatab-packages.git>


### Accessing Data in Vanilla Pandas
```
import pandas as pd


frp_meals_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-frpm-1.2.1/data/frp_meals.csv')
```

### Accessing Package in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/cde.metatab.org/cde.ca.gov-frpm-1.2.1.csv')

# Create Dataframes
frp_meals_df = pkg.resource('frp_meals').dataframe()
```
