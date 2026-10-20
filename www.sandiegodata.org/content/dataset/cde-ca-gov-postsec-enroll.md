---
title: "Post-Secondary Enrollment"
date: 2022-06-10T16:02:05+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "education"]
author: "metapack"
description: "Downloadable data about the College-Going Rate (CGR) for California high school"
---

_Downloadable data about the College-Going Rate (CGR) for California high school completers disaggregated by race/ethnicity, student group, and academic year._

`cde.ca.gov-postsec_enroll-1.2.3`. Modified 2022-06-17T17:07:51

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[cgr](<http://library.metatab.org/cde.ca.gov-postsec_enroll-1.2.3/data/cgr.csv>)**. College Going Rate


## Documentation

College-Going Rate (CGR) for California high school completers 12 months and 16 months after high school completion reported by race/ethnicity, student group, and academic year.

## License

The source data, from the California Department of Education, does not explicitly reference a license, but since the top-level website for California indicates that data published on the State of California website [is generally in the public domain](<https://www.ca.gov/use/>), we assume it is in the public domain. Derived data included in this package is also in the public domain. Metadata in this package ( contained in the `metadata.csv` file ) is derived from metadata for the source package, and is also in the public domain. 

Programs used for data transformation (contained in the `notebooks` directory), are Copyright 2021 Civic Knowledge, and are relased under the [Creative Commons Attribution-ShareAlike 4.0 International License.](<https://creativecommons.org/licenses/by-sa/4.0/>)

### Documentation Links

  * [College-Going Rate](<https://www.cde.ca.gov/ds/ad/cgrinfo.asp>) High-level overview of the CGR data sources, DataQuest reports, downloadable files, definitions, and rules helpful to understanding the CGR data reports and downloadable data files.
  * [Using the CGR Data File](<https://www.cde.ca.gov/ds/ad/usingcgr.asp>) This page explains how to effectively use the sub-setting variables included in this CGR data file to obtain the desired counts.
  * [Documentation Page](<http://library.metatab.org/cde.ca.gov-postsec_enroll-1.2.3/index.html>)
  * [Home Page](<https://www.cde.ca.gov/ds/ad/pse.asp>)
  * [Data Dictionary](<https://www.cde.ca.gov/ds/ad/fscgr16.asp>) Field descriptions for the 16 month file


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)

  * **Origin**

[Data Reporting Office](<mailto:dro@cde.ca.gov>), [California Department of Education](<https://www.cde.ca.gov>)


## Data Dictionary

cgr   


### cgr

Column Name| Data Type| Description  
---|---|---  
academicyear| string| The academic year corresponding to year of high school graduation or completion.  
aggregatelevel| string| C=County S=School, D=District T=State  
countycode| number| A unique two-digit code corresponding to the county.  
districtcode| number| A unique five-digit code corresponding to the district.  
schoolcode| number| A unique seven-digit code corresponding to the school.  
countyname| string| County name.  
districtname| string| District or Administrative Authority Name.  
schoolname| string| School name.  
charterschool| string| An indicator of whether data for all schools, only charter schools, or only non-charter schools are included. NOTE: One of these values must be chosen to obtain an unduplicated count at the selected level. All = Includes data for all schools regardless of charter status. For Aggregate Level=S, all schools are included. For Aggregate Levels T, C, and D, data for all schools are included in the aggregate. Y = Includes only data for charter schools. For Aggregate Level=S, only charter schools are included. For Aggregate Levels T, C, and D, only data for charter schools are included in the aggregate. N = Includes only data for non-charter schools. For Aggregate Level=S, only non-charter schools are included. For Aggregate Levels T, C, and D, only data for non-charter schools are included in the aggregate.  
asas| string| An indicator of whether data for all schools, only schools participating in the Dashboard Alternative School Status Program (DASS) or previously the Alternative School Accountability Model (ASAM), or only non-DASS or non-ASAM schools are included. NOTE: One of these values must be chosen to obtain an unduplicated count at the selected level. All = Includes data for all schools regardless of ASAS status. For Aggregate Level=S, all schools are included. For Aggregate Levels T, C, and D, data for all schools are included in the aggregate. Y = Includes only data for schools participating in ASAS. For Aggregate Level=S, only ASAS schools are included. For Aggregate Levels T, C, and D, only data for ASAS schools are included in the aggregate. N = Includes only data for non-ASAS schools. For Aggregate Level=S, only data for non-ASAS schools are included. For Aggregate Levels T, C, and D, only data for non-ASAS schools are included in the aggregate.  
reportingcategory| string| An indicator of the student group reporting category (race/ethnicity, gender, or program subgroup) disaggregation or subset. NOTE: Select Reporting Category = TA for aggregate totals without consideration of a Reporting Category student group. RB = African American RI = American Indian or Alaska Native RA = Asian RF = Filipino RH = Hispanic or Latino RD = Not Reported RP = Pacific Islander RT = Two or More Races RW = White GM = Male GF = Female SE = English Learners SD = Students with Disabilities SS = Socioeconomically Disadvantaged SM = Migrant SF = Foster SH = Homeless TA = Total (all high school completers).  
completertype| string| AGY = Count of graduates meeting a-g requirements for admission into a University of California (UC) or California State University (CSU) school. AGN = Count of graduates not meeting a-g requirements for admission into a UC or CSU school. NGC = Count of non-graduate completers not meeting a-g requirements for admission into a UC or CSU school. TA = Total (all high school completers).  
high_school_completers| number| The number of students who graduated from a California public high school with a regular high school diploma or who otherwise successfully finished high school as a non-graduate completer during the reporting period for the associated academic year (8/16/Year 1 to 8/15/Year 2), including summer graduates and non-graduate completers, regardless of when the students first entered grade 9. For the purpose of calculating the College-Going Rate (CGR), the following types graduates and non-graduate completers are included: regular high school diploma graduates, California High School Proficiency Exam (CHSPE) completers, General Education Development (GED) completers, and adult education high school diploma graduates. Please note, for the purposes of calculating the CGR, students who received a Special Education Certificate of Completion during the reporting period are not included.  
in_college_total_12m| number| The total number of California public high school completers who enrolled in any postsecondary institution within 16 months of completing high school. Postsecondary institutions include 2-year and 4-year, public and private postsecondary institutions, both in-state and out-of-state as determined through student-level data matches with the National Student Clearinghouse, which receives postsecondary enrollment and completion information from colleges and universities.  
cgr_12m| number| The total percentage of California public high school completers who enrolled in any public or private postsecondary institution (in-state or out-of-state) within 16 months of completing high school.  
in_12m| number| The number of California public high school completers who enrolled in a public or private postsecondary institution inside California within 16 months of completing high school.  
out_12m| number| The number of California public high school completers who enrolled in a public or private postsecondary institution outside California within 16 months of completing high school.  
not_enr_12m| number| The number of California public high school completers (1) who did not enroll in a public or private postsecondary institution inside or outside California within 12 or 16 months of completing high school or (2) whose postsecondary educational directory information records were blocked from being shared by the student or institution pursuant to privacy rights outlined in the Family Educational Rights and Privacy Act (FERPA). Analysis conducted by the National Student Clearinghouse (NSC) shows that California’s average block rate was 11 percent over 2012–13, 2014–15, and 2016–17. Additional information about directory information blocks and block rates by institution and state can be found on the NSC website at Working With Our Data under the "FERPA Implications for Researchers" section.  
uc_12m| number| The number of California public high school completers who enrolled in the University of California system within 16 months completing high school.  
csu_12m| number| The number California public high school completers who enrolled in the California State University system within 16 months of completing high school.  
ccc_12m| number| The number California public high school completers who enrolled in the California Community College (CCC) system within 16 months of completing high school.  
in_private_24y_12m| number| The number of California public high school completers who enrolled in a private California 2- or 4-year institution within 16 months of completing high school.  
out_4ypp_12m| number| The number of California public high school completers who enrolled in an out-of-state (public/private) 4-year postsecondary institution within 16 months completing high school.  
out_2ypp_12m| number| The number California public high school completers who enrolled in an out-of-state (public/private) 2-year postsecondary institution within 16 months completing high school.  
in_college_total_16m| number| The total number of California public high school completers who enrolled in any postsecondary institution within 16 months of completing high school. Postsecondary institutions include 2-year and 4-year, public and private postsecondary institutions, both in-state and out-of-state as determined through student-level data matches with the National Student Clearinghouse, which receives postsecondary enrollment and completion information from colleges and universities.  
cgr_16m| number| The total percentage of California public high school completers who enrolled in any public or private postsecondary institution (in-state or out-of-state) within 16 months of completing high school.  
in_16m| number| The number of California public high school completers who enrolled in a public or private postsecondary institution inside California within 16 months of completing high school.  
out_16m| number| The number of California public high school completers who enrolled in a public or private postsecondary institution outside California within 16 months of completing high school.  
not_enr_16m| number| The number of California public high school completers (1) who did not enroll in a public or private postsecondary institution inside or outside California within 12 or 16 months of completing high school or (2) whose postsecondary educational directory information records were blocked from being shared by the student or institution pursuant to privacy rights outlined in the Family Educational Rights and Privacy Act (FERPA). Analysis conducted by the National Student Clearinghouse (NSC) shows that California’s average block rate was 11 percent over 2012–13, 2014–15, and 2016–17. Additional information about directory information blocks and block rates by institution and state can be found on the NSC website at Working With Our Data under the "FERPA Implications for Researchers" section.  
uc_16m| number| The number of California public high school completers who enrolled in the University of California system within 16 months completing high school.  
csu_16m| number| The number California public high school completers who enrolled in the California State University system within 16 months of completing high school.  
ccc_16m| number| The number California public high school completers who enrolled in the California Community College (CCC) system within 16 months of completing high school.  
in_private_24y_16m| number| The number of California public high school completers who enrolled in a private California 2- or 4-year institution within 16 months of completing high school.  
out_4ypp_16m| number| The number of California public high school completers who enrolled in an out-of-state (public/private) 4-year postsecondary institution within 16 months completing high school.  
out_2ypp_16m| number| The number California public high school completers who enrolled in an out-of-state (public/private) 2-year postsecondary institution within 16 months completing high school.  
  
## References

Urls used in the creation of this data package.

  * **[cgr12mo18](<https://www3.cde.ca.gov/demo-downloads/cgr/cgr12mo18.txt#target_format=tsv>)**. 12 Month CGR 2018
  * **[cgr12mo17](<https://www3.cde.ca.gov/demo-downloads/cgr/cgr12mo17.txt#target_format=tsv>)**. 12 Month CGR 2017
  * **[cgr12mo16](<https://www3.cde.ca.gov/demo-downloads/cgr/cgr12mo16.txt#target_format=tsv>)**. 12 Month CGR 2016
  * **[cgr12mo15](<https://www3.cde.ca.gov/demo-downloads/cgr/cgr12mo15.txt#target_format=tsv>)**. 12 Month CGR 2015
  * **[cgr16mo17](<https://www3.cde.ca.gov/demo-downloads/cgr/cgr16mo17.txt#target_format=tsv>)**. 16 Month CGR 2017
  * **[cgr16mo16](<https://www3.cde.ca.gov/demo-downloads/cgr/cgr16mo16.txt#target_format=tsv>)**. 16 Month CGR 2016
  * **[cgr16mo15](<https://www3.cde.ca.gov/demo-downloads/cgr/cgr16mo15.txt#target_format=tsv>)**. 16 Month CGR 2015


## Packages

  * **s3** s3://library.metatab.org/cde.ca.gov-postsec_enroll-1.2.3.csv
  * **csv** <http://library.metatab.org/cde.ca.gov-postsec_enroll-1.2.3.csv>
  * **source** <https://github.com/metatab-packages/cde.ca.gov-collection.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    cgr_df =  pd.read_csv('http://library.metatab.org/cde.ca.gov-postsec_enroll-1.2.3/data/cgr.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/cde.ca.gov-postsec_enroll-1.2.3.csv')
    
    # Create Dataframes
    cgr_df = pkg.resource('cgr').dataframe()
    
[/code]
