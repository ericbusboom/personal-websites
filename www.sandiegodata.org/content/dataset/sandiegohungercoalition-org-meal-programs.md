---
title: "SDHC Meal Programs Data Collection"
date: 2019-05-23T04:15:51+00:00
draft: false
categories: ["Dataset"]
tags: ["sandiegohungercoalition.org"]
author: "metapack"
description: "A collection of files from other data packages, from the California Department"
---

_A collection of files from other data packages, from the California Department of Education, for the San Diego Hunger Coalition’s Hunger Free Kids program_

`sandiegohungercoalition.org-meal_programs-1`

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[cacfpreimburse](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/cacfpreimburse.csv>)**. Child and Adult Care Food Program
  * **[nslpreimburse](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/nslpreimburse.csv>)**. National School Lunch Program
  * **[sbpreimburse](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/sbpreimburse.csv>)**. School Breakfast Program
  * **[snackreimburse](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/snackreimburse.csv>)**. Meal Supplements (After-School Snacks) in the National School Lunch Program
  * **[summerreimburse](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/summerreimburse.csv>)**. Summer Food Service Program
  * **[subgroup_ids](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/subgroup_ids.csv>)**. CAASPP aggreation groups
  * **[test_ids](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/test_ids.csv>)**. CAASPP test id numbers
  * **[subgroups](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/subgroups.csv>)**. CAASPP scores, aggregated by subgroup
  * **[entities](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/entities.csv>)**. CAASPP schools and districts
  * **[chronic_absenteeism](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/chronic_absenteeism.csv>)**. Chronic Absenteeism 2016-2017a
  * **[frpm](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/frpm.csv>)**. Free and Reduced Price Meals 2004 – 2018
  * **[upc_lea](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/upc_lea.csv>)**. Unduplicated pupil counts by LEA, 2013 to 2017
  * **[upc_school](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/upc_school.csv>)**. Unduplicated pupil counts by school, 2013 to 2017
  * **[current_expense](<http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1/data/current_expense.csv>)**. Current Expense file, 1998 to 2017


## Documentation

### Documentation Links

  * [http://data.sandiegodata.org/dataset/cde-ca-gov-reimbursements](<Reimbursements data  package>)
  * [http://data.sandiegodata.org/dataset/cde-ca-gov-caaspp-2015e](<CAASPP Test Results data package>)
  * [http://data.sandiegodata.org/dataset/cde-ca-gov-absenteeism](<Absenteeism data package>)
  * [http://data.sandiegodata.org/dataset/cde-ca-gov-frpm](<Student Poverty FRPM data package>)
  * [http://data.sandiegodata.org/dataset/cde-ca-gov-calpads_upc](<Unduplicated Pupil Counts data package>)
  * [http://data.sandiegodata.org/dataset/cde-ca-gov-current-expense-source/](<Current Expense data package>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1.zip>
  * **csv** <http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1.csv>
  * **source** <https://github.com/sandiegodata-projects/sandiegohungercoalition.org.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1.zip')
    # CSV Package
    pkg = mp.open_package('http://library.metatab.org/sandiegohungercoalition.org-meal_programs-1.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

## Data Dictionary

cacfpreimburse | nslpreimburse | sbpreimburse | snackreimburse | summerreimburse | subgroup_ids | test_ids | subgroups | entities | chronic_absenteeism | frpm | upc_lea | upc_school | current_expense   


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
  
### subgroup_ids

Column Name| Data Type| Description  
---|---|---  
code| integer|   
label| string|   
group| string|   
  
### test_ids

Column Name| Data Type| Description  
---|---|---  
test_id| integer|   
test_num| integer|   
test_name| string|   
  
### subgroups

Column Name| Data Type| Description  
---|---|---  
year| integer| Source File Year  
county_code| integer| County Code  
district_code| integer| District Code  
school_code| integer| School Code  
filler| string| Filler  
test_year| integer| Test Year  
subgroup_id| integer| Subgroup ID  
test_type| string| Test Type  
total_caaspp_enrollment| integer| Total CAASPP Enrollment  
total_tested_at_entity_level| integer| Total Tested At Entity Level  
total_tested_with_scores| unknown| Total Tested with Scores  
total_tested_at_subgroup_level| integer| Total Tested at Subgroup Level  
grade| integer| Grade  
test_id| integer| Test Id  
caaspp_reported_enrollment| integer| CAASPP Reported Enrollment  
students_tested| integer| Students Tested  
mean_scale_score| string| Mean Scale Score  
percentage_standard_exceeded| string| Percentage Standard Exceeded  
percentage_standard_met| string| Percentage Standard Met  
percentage_standard_met_and_above| string| Percentage Standard Met and Above  
percentage_standard_nearly_met| string| Percentage Standard Nearly Met  
percentage_standard_not_met| string| Percentage Standard Not Met  
students_with_scores| integer| Students with Scores  
area_1_percentage_above_standard| float| Area 1 Percentage Above Standard  
area_1_percentage_near_standard| float| Area 1 Percentage Near Standard  
area_1_percentage_below_standard| float| Area 1 Percentage Below Standard  
area_1_percentage_at_or_near_standard| float| Area 1 Percentage At or Near Standard  
area_2_percentage_above_standard| float| Area 2 Percentage Above Standard  
area_2_percentage_near_standard| float| Area 2 Percentage Near Standard  
area_2_percentage_below_standard| float| Area 2 Percentage Below Standard  
area_2_percentage_at_or_near_standard| float| Area 2 Percentage At or Near Standard  
area_3_percentage_above_standard| float| Area 3 Percentage Above Standard  
area_3_percentage_near_standard| float| Area 3 Percentage Near Standard  
area_3_percentage_at_or_near_standard| float| Area 3 Percentage At or Near Standard  
area_3_percentage_below_standard| float| Area 3 Percentage Below Standard  
area_4_percentage_above_standard| float| Area 4 Percentage Above Standard  
area_4_percentage_near_standard| float| Area 4 Percentage Near Standard  
area_4_percentage_at_or_near_standard| float| Area 4 Percentage At or Near Standard  
area_4_percentage_below_standard| float| Area 4 Percentage Below Standard  
  
### entities

Column Name| Data Type| Description  
---|---|---  
year| integer| Source File Year  
county_code| integer| County Code  
district_code| integer| District Code  
school_code| integer| School Code  
filler| string| Filler  
test_year| integer| Test Year  
type_id| integer| Type Id  
county_name| string| County Name  
district_name| string| District Name  
school_name| string| School Name  
zip_code| string| Zip Code  
  
### chronic_absenteeism

Column Name| Data Type| Description  
---|---|---  
year| integer| Year taken from the source dataset name.  
academic_year| string| The academic year (July 1 – June 30) corresponding to the time period during which the data were collected.  
aggregate_level| string| T = State C = County D1 = District (All Schools) D2 = District (Non-Charter Schools) S = School  
county_code| integer| A unique two-digit code corresponding to the county.  
district_code| integer| A unique five-digit code corresponding to the district.  
school_code| integer| A unique seven-digit code corresponding to the school.  
county_name| string| County Name  
district_name| string| District or Administrative Authority Name  
school_name| string| School Name  
is_charter| string| A "Y" or "N" value indicating whether a school is a charter school in the current academic year.  
reporting_category| string| RB = African American RI = American Indian or Alaska Native RA = Asian RF = Filipino RH = Hispanic or Latino RD = Did not Report RP = Pacific Islander RT = Two or More Races RW = White GM = Male GF = Female SE = English Learners SD = Students with Disabilities SS = Socioeconomically Disadvantaged SM = Migrant SF = Foster SH = Homeless GRK = Kindergarten GR13 = Grades 1–3 GR46 = Grades 4–6 GR78 = Grades 7–8 GRK8 = Grades K–8 GR912 = Grades 9–12 GRUG = Ungraded Elementary and Secondary TA = Total  
cumulative_enrollment| integer| Cumulative enrollment consists of the total number of unduplicated primary and short-term enrollments within the academic year (July 1 to June 30), regardless of whether the student is enrolled multiple times within a school or district.  
chronic_absenteeism_count| integer| Total count of ALL chronically absent students at the selected entity for the selected population using the available filters. Students are determined to be chronically absent if they were enrolled for a combined total of 30 days or more at the selected reporting level during the academic year and they were absent for 10% or more of the days they were expected to attend.  
cumulative_eligible_enrollment| integer| This count uses the Cumulative Enrollment of the selected entity as the baseline and removes students that were not eligible to be considered chronically absent at that entity. Students that are enrolled less than 31 instructional days at the selected entity are not eligible to be considered chronically absent at that entity. This is calculated by looking at the number of "expected days to attend" that LEAs submit for each student in CALPADS. Students with exempt status are also removed from Chronic Absenteeism eligibility. Students are considered to be exempt if they are enrolled in a Non-Public School (NPS), receive instruction through a home or hospital instructional setting or are attending community college full-time.  
chronic_absenteeism_rate| number| The unduplicated count of students determined to be chronically absent (Chronic Absenteeism Count) divided by the Chronic Absenteeism Enrollment at the selected entity for the selected population using the available filters.  
  
### frpm

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
  
### upc_lea

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
  
### upc_school

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
  
### current_expense

Column Name| Data Type| Description  
---|---|---  
year| integer| Year of the original source file  
county| integer| County FIPS number  
district| string| District name  
lea_id| integer| District code, the ‘D’ part of the CDS code  
expenditures| number| Total district expenditures (EDP 365), in current dollars.  
ada| number| Average Daily attendance used for the cost per ada calculation  
cost_per_ada| number| Cost per average daily attendance  
lea_type| string| Type of district: High school Elementary or Unified  
  
## References

Urls used in the creation of this data package.

  * **metapack+http://library.metatab.org/cde.ca.gov-reimbursements-1.csv**. Reimbursements package
  * **metapack+http://library.metatab.org/cde.ca.gov-caaspp-2015e-1.csv**. CAASPP Test Scores package
  * **metapack+http://library.metatab.org/cde.ca.gov-absenteeism-1.csv**. Absenteeism package
  * **metapack+http://library.metatab.org/cde.ca.gov-frpm-1.csv**. Free/Reduced Price Meals package
  * **metapack+http://library.metatab.org/cde.ca.gov-calpads_upc-1.csv**. Unduplicated pupil counts
  * **metapack+http://library.metatab.org/cde.ca.gov-current_expense-1.csv**. Current expenses


Last Modified 2019-05-23T04:15:19
