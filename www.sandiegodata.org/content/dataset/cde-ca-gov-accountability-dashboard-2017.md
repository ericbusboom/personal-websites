---
title: "California Accountability Model & School Dashboard"
date: 2021-03-09T00:25:27+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "education"]
author: "metapack"
description: "Datasets for the California school dashboard at"
---

_Datasets for the California school dashboard at https://www.caschooldashboard.org_

`cde.ca.gov-accountability_dashboard-2017-1.2.1`. Modified 2021-03-11T00:52:26

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[ela38](<http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/ela38.csv>)**. English Language Arts, Grades 3-8
  * **[ela11](<http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/ela11.csv>)**. English Language Arts, Grade 11
  * **[math38](<http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/math38.csv>)**. Math, Grades 3-8
  * **[math11](<http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/math11.csv>)**. Math, Grade 11
  * **[collegecareer](<http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/collegecareer.csv>)**. College / Career Indicators
  * **[susprate](<http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/susprate.csv>)**. Suspension Rate
  * **[elaprog](<http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/elaprog.csv>)**. English Language Arts Progress Indicators
  * **[gradrate](<http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/gradrate.csv>)**. 


## Documentation

### Documentation Links

  * [California Accountability Model & School Dashboard](<http://www.cde.ca.gov/ta/ac/cm/>) Program page for the dashboard, datasets and reports.
  * [California School Dashboard](<https://www.caschooldashboard.org>) The California School Dashboard website.
  * [Documentation Page](<http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/index.html>)


## Contacts

  * **Origin**

[California Department of Education](<http://www.cde.ca.gov/>)

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://www.civicknowledge.com>)


## Data Dictionary

ela38 | ela11 | math38 | math11 | collegecareer | gradrate | susprate | elaprog | pubschools   


### ela38

Column Name| Data Type| Description  
---|---|---  
cds| integer| CDS Code  
rtype| text| Record Type  
studentgroup| text| Student Group  
currdenom| integer| Current year number of valid students  
priordenom| integer| CURRENT STATUS - Average distance from level 3  
currstatus| text| Prior year number of valid students  
priorstatus| text| PRIOR STATUS - Average distance from level 3  
change| text| CHANGE - Difference between current status and prior status  
statuslevel| integer| Status Level  
changelevel| integer| Change Level  
color| integer| Color  
box| integer| If a color was assigned, this value represents the specific 5x5 grid location  
  
### ela11

Column Name| Data Type| Description  
---|---|---  
cds| integer| CDS Code  
rtype| text| Record Type  
studentgroup| text| Student Group  
currdenom| integer| Current year number of valid students  
currstatus| text| CURRENT STATUS - Average distance from level 3  
priordenom| integer| Prior year number of valid students  
priorstatus| text| PRIOR STATUS - Average distance from level 3  
change| text| CHANGE - Difference between current status and prior status  
  
### math38

Column Name| Data Type| Description  
---|---|---  
cds| integer| CDS Code  
rtype| text| Record Type  
studentgroup| text| Student Group  
currdenom| integer| Current year number of valid students  
priordenom| integer| CURRENT STATUS - Average distance from level 3  
currstatus| text| Prior year number of valid students  
priorstatus| text| PRIOR STATUS - Average distance from level 3  
change| text| CHANGE - Difference between current status and prior status  
statuslevel| integer| Status Level  
changelevel| integer| Change Level  
color| integer| Color  
box| integer| If a color was assigned, this value represents the specific 5x5 grid location  
  
### math11

Column Name| Data Type| Description  
---|---|---  
cds| integer| CDS Code  
rtype| text| Record Type  
studentgroup| text| Student Group  
currdenom| integer| Current year number of valid students  
currstatus| text| CURRENT STATUS - Average distance from level 3  
priordenom| integer| Prior year number of valid students  
priorstatus| text| PRIOR STATUS - Average distance from level 3  
change| text| CHANGE - Difference between current status and prior status  
  
### collegecareer

Column Name| Data Type| Description  
---|---|---  
cds| integer| County-District-School Code  
rtype| text| Record Type  
studentgroup| text| Student Group  
num_cohort| integer| Number of students in the 2013-14 Four-Year Grad Cohort  
num_prep| text| Number of students in the 2013-14 Four-Year Grad Cohort who earned PREPARED on the CCI  
num_aprep| text| Number of students in the 2013-14 Four-Year Grad Cohort who earned APPROACHING PREPARED on the CCI  
num_nprep| text| Number of students in the 2013-14 Four-Year Grad Cohort who earned NOT PREPARED on the CCI  
pct_prep| text| Percent of students in field:NUM_COHORT who earned PREPARED on the CCI  
pct_aprep| text| Percent of students in field:NUM_COHORT who earned APPROACHING PREPARED on the CCI  
pct_nprep| text| Percent of students in field:NUM_COHORT who earned NOT PREPARED on the CCI  
  
### gradrate

Column Name| Data Type| Description  
---|---|---  
cds| integer| CDS Code  
rtype| text| Record Type  
studentgroup| text| Student Group  
currnumer| text| Number of 2014-15 cohort graduates  
currdenom| integer| Total number of 2014-15 cohort students  
currstatus| text| CURRENT STATUS - 2014-15 Graduation Rate  
priornumer| text| Number of students who graduated in prior 3 years  
priordenom| integer| Total number of students in prior 3 years  
priorstatus| text| PRIOR STATUS - 3-year graduation rate average  
change| text| CHANGE - Difference between 2014-15 graduation rate and prior 3-year average  
prioryear1_numer| text| Number of 2013-14 cohort graduates  
prioryear1_denom| integer| Total number of 2013-14 cohort students  
prioryear1_status| text| 2013-14 Graduation Rate  
prioryear2_numer| text| Number of 2012-13 cohort graduates  
prioryear2_denom| integer| Total number of 2012-13 cohort students  
prioryear2_status| text| 2012-13 Graduation Rate  
prioryear3_numer| text| Number of 2011-12 cohort graduates  
prioryear3_denom| integer| Total number of 2011-12 cohort students  
prioryear3_status| text| 2011-12 Graduation Rate  
statuslevel| integer| Status level  
changelevel| integer| Change level  
color| integer| Color  
box| integer| If a color was assigned, this value represents the specific 5x5 grid location  
  
### susprate

Column Name| Data Type| Description  
---|---|---  
cds| integer| CDS Code  
rtype| text| Record Type  
type| text| School or District Type  
studentgroup| text| Student Group  
currnumer| text| Number of Students Suspended in 2014-15  
currdenom| text| Cummulative Number of Students Enrolled in 2014-15  
currstatus| text| CURRENT STATUS - 2014-15 Suspension Rate  
priornumer| text| Number of Students Suspended in 2013-14  
priordenom| text| Cummulative Number of Students Enrolled in 2013-14  
priorstatus| number| PRIOR STATUS - 2013-14 Suspension Rate (rounded)  
change| text| CHANGE - Difference between 2014-15 Suspension Rate and 2013-14 Suspension Rate  
statuslevel| integer| Status level  
changelevel| integer| Change level  
color| integer| Color  
box| integer| If a color was assigned, this value represents the specific 5x5 grid location  
certifyflag| text| Non-certified data flag. Districts and schools that did not certify their suspension (or discipline) data in the California Longitudinal Pupil Achievement Data System (CALPADS) in the current year or prior year automatically are assigned an orange performance level (box 180) if their earned color was orginally blue, green, or yellow.  
  
### elaprog

Column Name| Data Type| Description  
---|---|---  
cds| integer| CDS Code  
rtype| text| Record Type  
currtesters| integer| Number of annual CELDT testers in 2014-15 with a prior CELDT score  
currrfeps| integer| Number of EL students who reclassified between July 1, 2013 and June 30, 2014  
currnumer| text| Number of ELs who moved up at least one performance level in CELDT from 2014 to 2015 or who maintained Early Advanced/Advanced Proficient plus ELs who were reclassified between July 1, 2013 to June 30, 2014  
currdenom| integer| Current year number of testers and RFEP students  
currstatus| text| CURRENT STATUS Percent of ELs who moved up at least one performance level in CELDT from 2014 to 2015 or who maintained Early Advanced/Advanced Proficient plus ELs who were reclassified between July 1, 2013 to June 30, 2014  
priortesters| integer| Number of annual CELDT testers in 2013-14 with a prior CELDT score  
priorrfeps| integer| Number of EL students who reclassified between July 1, 2012 and June 30, 2013  
priornumer| text| Number of ELs who moved up at least one performance level in CELDT from 2013 to 2014 or who maintained Early Advanced/Advanced Proficient plus ELs who were reclassified between July 1, 2012 to June 30, 2013  
priordenom| integer| Prior year number of testers and RFEP students  
priorstatus| text| PRIOR STATUS Percent of ELs who moved up at least one performance level in CELDT from 2013 to 2014 or who maintained Early Advanced/Advanced Proficient plus ELs who were reclassified between July 1, 2012 to June 30, 2013  
change| text| CHANGE Difference between current status and prior status  
statuslevel| integer| Status level  
changelevel| integer| Change level  
color| integer| Color  
box| integer| If a color was assigned, this value represents the specific 5x5 grid location  
flag50pct| text| Tested less than 50% of EL population flag. Districts and schools that did not test at least 50 percent of their English learner population on the California English Language Development Test (CELDT) in grades 3 through 8 and 11 are assigned an orange performance level (box 180). The 50 percent determination is based on the number of English learners (i.e., does not include reclassified students) who took the 2015 Smarter Balanced Summative Assessments in mathematics in grades 3 through 8 and 11.  
  
### pubschools

Column Name| Data Type| Description  
---|---|---  
cdscode| text| This 14-digit code is the official, unique identification of a school within California. The first two digits identify the county, the next five digits identify the school district, and the last seven digits identify the school. Please note that a CDS code ending in '0000000' indicates a district record not a school.  
ncesdist| text| This field represents the 7-digit National Center for Educational Statistics (NCES) school district identification number. The first 2 digits identify the state and the last 5 digits identify the school district. Combined, they make a unique 7-digit ID for each school district.  
ncesschool| text| This field represents the 5-digit NCES school identification number. The NCESSchool combined with the NCESDist form a unique 12-digit ID for each school.  
statustype| text| This field identifies the status of the district. Definitions of the valid status types are listed below: Active: The district is in operation and providing instructional services. Closed: The district is not in operation and no longer providing instructional services. Merged: The district has combined with another district or districts. Pending: The district has not opened for operation and instructional services yet, but plans to open within the next 9–12 months.  
county| text| County name.  
district| text| District or Administrative Authority name.  
school| text| School name.  
street| text| The unabbreviated street (physical) address of this school, district, or administrative authority. Note: Some entities (primarily closed or retired schools) may not have data in this field.  
streetabr| text| The abbreviated street address of the school, district, or administrative authority’s physical location. Note: Some records (primarily records of closed or retired schools) may not have data in this field.  
city| text| The city where the school, district, or administrative authority is physically located. Note: Some records (primarily records of closed or retired schools) may not have data in this field.  
zip| text| The zip code associated with the street address of the school, district, or administrative authority’s physical location. Note: Some records (primarily records of closed or retired schools) may not have data in this field.  
state| text| The state in which the school, district, or administrative authority is located.  
mailstreet| text| The unabbreviated mailing address of the school, district, or administrative authority (i.e., P.O. Box). Note: 1) Some entities (primarily closed or retired schools) may not have data in this field; 2) Many active entities have not provided a mailing street address. For your convenience we have filled the unpopulated MailStreet cells with Street data.  
mailstrabr| text| The abbreviated mailing street address of the school, district, or administrative authority (i.e., P.O. Box).Note: Many active entities have not provided a mailing street address. For your convenience we have filled the unpopulated MailStrAbr cells with StreetAbr data.  
mailcity| text| The city associated with the mailing address of the school, district, or administrative authority. Note: Many entities have not provided a mailing address city. For your convenience we have filled the unpopulated MailCity cells with City data.  
mailzip| text| The zip code associated with the mailing address of the school, district, or administrative authority. Note: Many entities have not provided a mailing address zip code. For your convenience we have filled the unpopulated MailZip cells with Zip data.  
mailstate| text| The state within the mailing address. For your convenience we have filled the unpopulated MailState cells with State data.  
phone| text| The area code and phone number of the school, district, or administrative authority.  
ext| text| The phone number extension of the school, district, or administrative authority.  
website| text| The website address of the school, district, or administrative authority.  
opendate| text| The date the school opened. A blank cell indicates the record is for a district or county office.  
closeddate| text| The date the school closed. An empty cell indicates that the entity is not closed.  
charter| text| This field identifies a charter school. The field is coded as follows: Y = The school is a charter N = The school is not a charter  
charternum| text| The charter school number. A 4-digit number assigned to a charter school. A blank value indicates the school is not a charter school.  
fundingtype| text| Indicates the charter school funding type. Values are as follows: Not in CS funding model Locally funded Directly funded Blank  
doc| text| The District Ownership Code (DOC) is the numeric code used to identify the category of the Administrative Authority. 00 – County Office of Education 02 – State Board of Education 03 – Statewide Benefit Charter 31 – State Special Schools 34 – Non-school Location* 52 – Elementary School District 54 – Unified School District 56 – High School District 98 – Regional Occupational Center/Program (ROC/P) *Only the California Education Authority has been included in the non-school location category.  
doctype| text| The District Ownership Code Type is the text description of the DOC category. (See text values in DOC field description above)  
soc| text| The School Ownership Code is a numeric code used to identify the type of school. 08 – Preschool 09 – Special Education Schools (Public) 10 – County Community 11 – Youth Authority Facilities (CEA) 13 – Opportunity Schools 14 – Juvenile Court Schools 15 – Other County or District Programs 31 – State Special Schools 60 – Elementary School (Public) 61 – Elementary School in 1 School District (Public) 62 – Intermediate/Middle Schools (Public) 63 – Alternative Schools of Choice 64 – Junior High Schools (Public) 65 – K-12 Schools (Public) 66 – High Schools (Public) 67 – High Schools in 1 School District (Public) 68 – Continuation High Schools 69 – District Community Day Schools 70 – Adult Education Centers 98 – Regional Occupational Center/Program (ROC/P)  
soctype| text| The School Ownership Code Type is the text description of the type of school. (See text values in SOC field description above)  
edopscode| text| The Education Option Code is a short text description of the type of education offered. ALTSOC – Alternative School of Choice COMM – County Community School COMMDAY – Community Day School CON – Continuation School JUV – Juvenile Court School OPP – Opportunity School YTH – Youth Authority School SSS – State Special School SPEC – Special Education School TRAD – Tradtional ROP – Regional Occupational Program HOMHOS – Home and Hospital SPECON – District Consortia Special Education School  
edopsname| text| The Educational Option Name is the long text description of the type of education being offered. (See text values in EdOPsCode field description above)  
eilcode| text| The Educational Instruction Level Code is a short text description of the institution's type relative to the grade range served. A – Adult ELEM – Elementary ELEMHIGH – Elementray-High Combination HS – High School INTMIDJR – Intermediate/Middle/Junior High PS – Preschool UG – Ungraded  
eilname| text| The Educational Instruction Level Name is the long text description of the institution’s type relative to the grade range served. (See text values in EILCode field description above)  
gsoffered| text| The grade span offered is the lowest grade and the highest grade offered or supported by the school, district, or administrative authority. This field might differ from the grade span served as reported in the most recent certified California Longitudinal Pupil Achievement (CALPADS) Fall 1 data collection. For example XYZ School might display the following data: GSoffered = P–Adult GSserved = K–12  
gsserved| text| This field represents the grade span served. It is the lowest grade and the highest grade of student enrollment as reported in the most recent certified CALPADS Fall 1 data collection. Only K–12 enrollment is reported through CALPADS. This field may differ from the grade span offered. Note: Special programs at independent study, alternative education, and special education schools will often exceed the typical grade span for schools of that type (i.e., a high school might serve grades three through twelve).  
virtual| text| This field identifies the type of virtual instruction offered by the school. Virtual instruction is instruction in which students and teachers are separated by time and/or location, and interaction occurs via computers and/or telecommunications technologies. The field is coded as follows: F = Exclusively Virtual – The school has no physical building where students meet with each other or with teachers, all instruction is virtual. V = Primarily Virtual – The school focuses on a systematic program of virtual instruction but includes some physical meetings among students or with teachers. C = Primarily Classroom – The school offers virtual courses but virtual instruction is not the primary means of instruction. N = Not Virtual – The school does not offer any virtual instruction. Blank = The type of virtual instruction offered by the school is not known, or the record is for a district or county office. Data are only available at the school level, however not all schools in this file are required to provide this information.  
magnet| text| This field identifies whether a school is a magnet school and/or provides a magnet program. Additional information on magnet schools may be obtained from the CDE Magnets Web page. The field is coded as follows: Y = Magnet - The school is a magnet school and/or offers a magnet program. N = Not Magnet - The school is not a magnet school and/or does not offer a magnet program. Note: Preschools and adult education centers do not contain a magnet school indicator.  
latitude| text| The angular distance (expressed in degrees) between the location of the school, district, or administrative authority and the equator measured north to south.  
longitude| text| The angular distance (expressed in degrees) between the location of the school, district, or administrative authority and the prime meridian (Greenwich, England) measured from west to east.  
admfname1| text| The superintendent’s or principal’s first name. Only active and pending districts and schools will display administrator information, if applicable.  
admlname1| text| The superintendent’s or principal’s last name. Only active and pending districts and schools will display administrator information, if applicable.  
admemail1| text| The superintendent’s or principal’s e-mail address. Only active and pending districts and schools will display administrator information, if applicable.  
admfname2| text| The second principal’s first name (optional). Only active and pending school records will display principal information, if applicable.  
admlname2| text| The second principal’s last name (optional). Only active and pending school records will display principal information, if applicable.  
admemail2| text| The second principal’s e-mail address (optional). Only active and pending school records will display principal information, if applicable.  
admfname3| text| The third principal’s first name (optional). Only active and pending school records will display principal information, if applicable.  
admlname3| text| The third principal’s last name (optional). Only active and pending school records will display principal information, if applicable.  
admemail3| text| The third principal’s e-mail address (optional). Only active and pending school records will display principal information, if applicable.  
lastupdate| date| The date the record was last updated.  
  
## References

Urls used in the creation of this data package.

  * **[gradrate_source](<http://www3.cde.ca.gov/researchfiles/cadashboard/graddownload2017s.txt>)**. 


## Packages

  * **s3** s3://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1.csv
  * **csv** <http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1.csv>
  * **source** <https://github.com/metatab-packages/cde.ca.gov.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    ela38_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/ela38.csv')
    ela11_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/ela11.csv')
    math38_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/math38.csv')
    math11_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/math11.csv')
    collegecareer_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/collegecareer.csv')
    susprate_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/susprate.csv')
    elaprog_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/elaprog.csv')
    gradrate_df =  pd.read_csv('http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1/data/gradrate.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://cde.metatab.org/cde.ca.gov-accountability_dashboard-2017-1.2.1.csv')
    
    # Create Dataframes
    ela38_df = pkg.resource('ela38').dataframe()
    ela11_df = pkg.resource('ela11').dataframe()
    math38_df = pkg.resource('math38').dataframe()
    math11_df = pkg.resource('math11').dataframe()
    collegecareer_df = pkg.resource('collegecareer').dataframe()
    susprate_df = pkg.resource('susprate').dataframe()
    elaprog_df = pkg.resource('elaprog').dataframe()
    gradrate_df = pkg.resource('gradrate').dataframe()
    
[/code]
