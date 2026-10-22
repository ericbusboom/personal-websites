---
title: "California Schools and Districts"
date: 2019-06-16T17:49:56+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "education"]
author: "metapack"
description: "California public schools, private schools and  districts."
---

_California public schools, private schools and districts._

`cde.ca.gov-schools-2.1.1`. Modified 2022-06-17T15:44:42


## Resources

  * **[public_schools](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-schools-2.1.1/data/public_schools.csv>)**. 
  * **[school_districts](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-schools-2.1.1/data/school_districts.csv>)**. 
  * **[private_schools](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-schools-2.1.1/data/private_schools.csv>)**. 


## Documentation

## License

The source data, from the California Department of Education, does not explicitly reference a license, but since the top-level website for California indicates that data published on the State of California website [is generally in the public domain](<https://www.ca.gov/use/>), we assume it is in the public domain. Derived data included in this package is also in the public domain. Metadata in this package ( contained in the `metadata.csv` file ) is derived from metadata for the source package, and is also in the public domain. 

Programs used for data transformation (contained in the `notebooks` directory), are Copyright 2021 Civic Knowledge, and are relased under the [Creative Commons Attribution-ShareAlike 4.0 International License.](<https://creativecommons.org/licenses/by-sa/4.0/>)

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-schools-2.1.1/index.html>)
  * [Public Schools Download Page](<https://www.cde.ca.gov/ds/si/ds/pubschls.asp>)
  * [Private Schools Download Page](<https://www.cde.ca.gov/ds/si/ps/index.asp>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

public_schools | school_districts | private_schools   


### public_schools

Column Name| Data Type| Description  
---|---|---  
cdscode| integer| This 14-digit code is the official, unique identification of a school within California. The first two digits identify the county, the next five digits identify the school district, and the last seven digits identify the school. Please note that a CDS code ending in '0000000' indicates a district record not a school.  
ncesdist| string| This field represents the 7-digit National Center for Educational Statistics (NCES) school district identification number. The first 2 digits identify the state and the last 5 digits identify the school district. Combined, they make a unique 7-digit ID for each school district.  
ncesschool| string| This field represents the 5-digit NCES school identification number. The NCESSchool combined with the NCESDist form a unique 12-digit ID for each school.  
statustype| string| This field identifies the status of the district. Definitions of the valid status types are listed below: \- *Active:* The district is in operation and providing instructional services. \- *Closed:* The district is not in operation and no longer providing instructional services. \- *Merged:* The district has combined with another district or districts. \- *Pending:* The district has not opened for operation and instructional services yet, but plans to open within the next 9–12 months.  
county| string| County name.  
district| string| District or Administrative Authority name.  
school| text| School name.  
street| string| The unabbreviated street (physical) address of this school, district, or administrative authority. Note: Some entities (primarily closed or retired schools) may not have data in this field.  
streetabr| string| The abbreviated street address of the school, district, or administrative authority’s physical location. Note: Some records (primarily records of closed or retired schools) may not have data in this field.  
city| string| The city where the school, district, or administrative authority is physically located. Note: Some records (primarily records of closed or retired schools) may not have data in this field.  
zip| string| The zip code associated with the street address of the school, district, or administrative authority’s physical location. Note: Some records (primarily records of closed or retired schools) may not have data in this field.  
state| string| The state in which the school, district, or administrative authority is located.  
mailstreet| string| The unabbreviated mailing address of the school, district, or administrative authority (i.e., P.O. Box). Note: 1) Some entities (primarily closed or retired schools) may not have data in this field; 2) Many active entities have not provided a mailing street address. For your convenience we have filled the unpopulated MailStreet cells with Street data.  
mailstrabr| string| The abbreviated mailing street address of the school, district, or administrative authority (i.e., P.O. Box).Note: Many active entities have not provided a mailing street address. For your convenience we have filled the unpopulated MailStrAbr cells with StreetAbr data.  
mailcity| string| The city associated with the mailing address of the school, district, or administrative authority. Note: Many entities have not provided a mailing address city. For your convenience we have filled the unpopulated MailCity cells with City data.  
mailzip| string| The zip code associated with the mailing address of the school, district, or administrative authority. Note: Many entities have not provided a mailing address zip code. For your convenience we have filled the unpopulated MailZip cells with Zip data.  
mailstate| string| The state within the mailing address. For your convenience we have filled the unpopulated MailState cells with State data.  
phone| string| The area code and phone number of the school, district, or administrative authority.  
ext| string| The phone number extension of the school, district, or administrative authority.  
faxnumber| string|   
email| string|   
website| string| The website address of the school, district, or administrative authority.  
opendate| string| The date the school opened.  
closeddate| string| The date the school closed.  
charter| string| This field identifies a charter school. The field is coded as follows: \- Y = The school is a charter \- N = The school is not a charter  
charternum| string| The charter school number, which is a 4-digit number assigned to a charter school.  
fundingtype| string| Indicates the charter school funding type. Values are as follows: \- Not in CS funding model \- Locally funded \- Directly funded  
doc| integer| The District Ownership Code (DOC) is the numeric code used to identify the category of the Administrative Authority. \- 00 – County Office of Education \- 02 – State Board of Education \- 03 – Statewide Benefit Charter \- 31 – State Special Schools \- 34 – Non-school Location* \- 52 – Elementary School District \- 54 – Unified School District \- 56 – High School District \- 98 – Regional Occupational Center/Program (ROC/P) *Only the California Education Authority has been included in the non-school location category.  
doctype| string| The District Ownership Code Type is the text description of the DOC category. (See text values in DOC field description above)  
soc| string| The School Ownership Code is a numeric code used to identify the type of school. \- 08 – Preschool \- 09 – Special Education Schools (Public) \- 10 – County Community \- 11 – Youth Authority Facilities (CEA) \- 13 – Opportunity Schools \- 14 – Juvenile Court Schools \- 15 – Other County or District Programs \- 31 – State Special Schools \- 60 – Elementary School (Public) \- 61 – Elementary School in 1 School District (Public) \- 62 – Intermediate/Middle Schools (Public) \- 63 – Alternative Schools of Choice \- 64 – Junior High Schools (Public) \- 65 – K-12 Schools (Public) \- 66 – High Schools (Public) \- 67 – High Schools in 1 School District (Public) \- 68 – Continuation High Schools \- 69 – District Community Day Schools \- 70 – Adult Education Centers \- 98 – Regional Occupational Center/Program (ROC/P)  
soctype| string| The School Ownership Code Type is the text description of the type of school. (See text values in SOC field description above)  
edopscode| string| The Education Option Code is a short text description of the type of education offered. \- ALTSOC – Alternative School of Choice \- COMM – County Community School \- COMMDAY – Community Day School \- CON – Continuation School \- JUV – Juvenile Court School \- OPP – Opportunity School \- YTH – Youth Authority School \- SSS – State Special School \- SPEC – Special Education School \- TRAD – Traditional \- ROP – Regional Occupational Program \- HOMHOS – Home and Hospital \- SPECON – District Consortia Special Education School  
edopsname| string| The Educational Option Name is the long text description of the type of education being offered. (See text values in EdOPsCode field description above)  
eilcode| string| The Educational Instruction Level Code is a short text description of the institution's type relative to the grade range served. \- A – Adult \- ELEM – Elementary \- ELEMHIGH – Elementary-High Combination \- HS – High School \- INTMIDJR – Intermediate/Middle/Junior High \- PS – Preschool \- UG – Ungraded  
eilname| string| The Educational Instruction Level Name is the long text description of the institution’s type relative to the grade range served. (See text values in EILCode field description above)  
gsoffered| string| The grade span offered is the lowest grade and the highest grade offered or supported by the school, district, or administrative authority. This field might differ from the grade span served as reported in the most recent certified California Longitudinal Pupil Achievement (CALPADS) Fall 1 data collection. For example XYZ School might display the following data: GSoffered = P–Adult GSserved = K–12  
gsserved| string| This field represents the grade span served. It is the lowest grade and the highest grade of student enrollment as reported in the most recent certified CALPADS Fall 1 data collection. Only K–12 enrollment is reported through CALPADS. This field may differ from the grade span offered. Note: Special programs at independent study, alternative education, and special education schools will often exceed the typical grade span for schools of that type (i.e., a high school might serve grades three through twelve).  
virtual| string| This field identifies the type of virtual instruction offered by the school. Virtual instruction is instruction in which students and teachers are separated by time and/or location, and interaction occurs via computers and/or telecommunications technologies. The field is coded as follows: \- F = Exclusively Virtual – The school has no physical building where students meet with each other or with teachers, all instruction is virtual. \- V = Primarily Virtual – The school focuses on a systematic program of virtual instruction but includes some physical meetings among students or with teachers. \- C = Primarily Classroom – The school offers virtual courses but virtual instruction is not the primary means of instruction. \- N = Not Virtual – The school does not offer any virtual instruction. \- P = Partial Virtual – The school offers some, but not all, instruction through virtual instruction. Note: This value was retired and replaced with the Primarily Virtual and Primarily Classroom values beginning with the 2016–17 school year.  
magnet| string| This field identifies whether a school is a magnet school and/or provides a magnet program. Additional information on magnet schools may be obtained from the CDE Magnets web page. The field is coded as follows: \- Y = Magnet - The school is a magnet school and/or offers a magnet program. \- N = Not Magnet - The school is not a magnet school and/or does not offer a magnet program. Note: Preschools and adult education centers do not contain a magnet school indicator.  
yearroundyn| string| This field indicates if the school is operating on a year round calendar. More information about year-round education can be found by visiting the CDE Year-Round Education Program Guide web page.  
federaldfcdistrictid| string| This field represents the 7-digit National Center for Educational Statistics (NCES) school district identification number for direct funded charter schools. Beginning in February 2019, direct funded charter schools were issued their own federal district ID and should no longer use the federal district ID associated with their authorizing agency.  
latitude| string| The angular distance (expressed in degrees) between the location of the school, district, or administrative authority and the equator measured north to south.  
longitude| string| The angular distance (expressed in degrees) between the location of the school, district, or administrative authority and the prime meridian (Greenwich, England) measured from west to east.  
admfname| string|   
admlname| text|   
admemail| string|   
lastupdate| date| The date the record was last updated.  
  
### school_districts

Column Name| Data Type| Description  
---|---|---  
cd_code| integer|   
county| string| County  
district| string| District  
street| string| Street  
city| string| City  
zip| string| Zip  
state| string| State  
mailstreet| string| MailStreet  
mailcity| string| MailCity  
mailzip| string| MailZip  
mailstate| string| MailState  
phone| string| Phone  
ext| string| Ext  
faxnumber| string|   
email| string|   
admfname| text| AdmFName  
admlname| text| AdmLName  
admemail| string| AdmEmail  
latitude| number| Latitude  
longitude| number| Longitude  
doc| integer| DOC  
doctype| string| DOCType  
statustype| string| StatusType  
lastupdate| date| LastUpDate  
  
### private_schools

Column Name| Data Type| Description  
---|---|---  
year| integer|   
affidavit_id| integer|   
cds_code| integer|   
county| string|   
district| string|   
school| text|   
school_type| string|   
school_accommodations| string|   
religious_denomination| string|   
religious_classification| string|   
low_grade| string|   
high_grade| string|   
grade_k_enroll| integer|   
grade_1_enroll| integer|   
grade_2_enroll| integer|   
grade_3_enroll| integer|   
grade_4_enroll| integer|   
grade_5_enroll| integer|   
grade_6_enroll| integer|   
grade_7_enroll| integer|   
grade_8_enroll| integer|   
grade_9_enroll| integer|   
grade_10_enroll| integer|   
grade_11_enroll| integer|   
grade_12_enroll| integer|   
ungraded_elem_enroll| integer|   
ungraded_sec_enroll| integer|   
total_enroll| integer|   
graduates_2017_18| integer|   
previous_year_grads| integer|   
diploma_offered| string|   
full_time_teachers| integer|   
part_time_teachers| number|   
administrators| number|   
other_staff| integer|   
street| string|   
city| text|   
state| string|   
zip| integer|   
mail_street| string|   
mail_city| string|   
mail_state| string|   
mail_zip| string|   
school_phone_number| string|   
area_code| integer|   
phone_prefix| integer|   
phone_suffix| integer|   
email| string|   
email2| string|   
administrator_salutation| string|   
administrator_first_name| text|   
administrator_last_name| text|   
administrator_title| string|   
administrator_email| string|   
director_salutation| string|   
director_first_name| text|   
director_last_name| text|   
director_title| string|   
director_email| text|   
custodian_of_records_salutation| string|   
custodian_of_records_first_name| text|   
custodian_of_records_last_name| text|   
custodian_of_records_email| text|   
tax_exempt_501| string|   
tax_exempt_23701| string|   
tax_exempt_27301| string|   
tax_exempt_214| string|   
tax_exempt| string|   
  
## References

Urls used in the creation of this data package.

  * **[private_schools_2018](<https://www.cde.ca.gov/ds/si/ps/documents/privateschools1819.xlsx#headers=2&start=3>)**. 
  * **[private_schools_2019](<https://www.cde.ca.gov/ds/si/ps/documents/privateschools1920.xlsx#headers=2&start=3>)**. 
  * **[private_schools_2020](<https://www.cde.ca.gov/ds/si/ps/documents/privateschools2021.xlsx#headers=2&start=3>)**. 
  * **[private_schools_2021](<https://www.cde.ca.gov/ds/si/ps/documents/privateschools2122.xlsx#headers=2&start=3>)**. 


## Packages

  * **s3** s3://library.metatab.org/cde.ca.gov-schools-2.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-schools-2.1.1.csv>
  * **source** <https://github.com/metatab-packages/cde.ca.gov.git>


### Accessing Data in Vanilla Pandas
```
import pandas as pd


public_schools_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-schools-2.1.1/data/public_schools.csv')
school_districts_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-schools-2.1.1/data/school_districts.csv')
private_schools_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-schools-2.1.1/data/private_schools.csv')
```

### Accessing Package in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-schools-2.1.1.csv')

# Create Dataframes
public_schools_df = pkg.resource('public_schools').dataframe()
school_districts_df = pkg.resource('school_districts').dataframe()
private_schools_df = pkg.resource('private_schools').dataframe()
```
