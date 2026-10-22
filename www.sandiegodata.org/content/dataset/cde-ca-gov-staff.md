---
title: "Staff Demographic Data"
date: 2022-06-27T23:03:14+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "education"]
author: "metapack"
description: "Data files pertaining to staff demographics, credentials and teaching load."
---

_Data files pertaining to staff demographics, credentials and teaching load._

`cde.ca.gov-staff-1.1.2`. Modified 2022-06-27T23:03:03


## Resources

  * **[staff_cred](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-staff-1.1.2/data/staff_cred.csv>)**. Staff credentials
  * **[staff_demo](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-staff-1.1.2/data/staff_demo.csv>)**. Staff Demographics
  * **[staff_fte](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-staff-1.1.2/data/staff_fte.csv>)**. Staff FTE teaching load 100=full time.


## Documentation

## License

The upstream data, from the California Department of Education, does not explicitly reference a license, so we assume it is in the public domain. 

## License

The source data, from the California Department of Education, does not explicitly reference a license, but since the top-level website for California indicates that data published on the State of California website [is generally in the public domain](<https://www.ca.gov/use/>), we assume it is in the public domain. Derived data included in this package is also in the public domain. Metadata in this package ( contained in the `metadata.csv` file ) is derived from metadata for the source package, and is also in the public domain. 

Programs used for data transformation (contained in the `notebooks` directory), are Copyright 2021 Civic Knowledge, and are relased under the [Creative Commons Attribution-ShareAlike 4.0 International License.](<https://creativecommons.org/licenses/by-sa/4.0/>)

### Documentation Links

  * [StaffData-EntityRelationshipDiagram](<https://www.cde.ca.gov/ds/ad/documents/StaffData-EntityRelationshipDiagram.pdf>) ERD diagram for the relationships within the data files.
  * [Staff Demographics 2015-16 to Current](<https://www.cde.ca.gov/ds/ad/fsstaffdemo15.asp>) File structure for the staff demographics record, which includes demographic and full-time equivalent (FTE) data for K-12 public education certificated teachers, administrators, and pupil services personnel reported as employed on Information Day.
  * [Staff Credentials 2012–13 to Current](<https://www.cde.ca.gov/ds/ad/fsstaffcred12.asp>) File structure for staff credential data, including associated authorizations, for staff employed on Information Day.
  * [Staff School FTE 2012–13 to Current](<https://www.cde.ca.gov/ds/ad/fsstaffschoolfte.asp>) This table contains the structure for the staff school FTE record.
  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-staff-1.1.2/index.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

staff_cred | staff_demo | staff_fte   


### staff_cred

Column Name| Data Type| Description  
---|---|---  
academicyear| integer|   
recid| integer|   
credentialtype| integer|   
authorizationtype| integer|   
filecreated| date|   
  
### staff_demo

Column Name| Data Type| Description  
---|---|---  
academicyear| integer|   
recid| integer|   
districtcode| integer|   
countyname| string|   
districtname| string|   
gendercode| string|   
educationlevel| string|   
ethnicgroup| integer|   
yearsteaching| integer|   
yearsindistrict| integer|   
employmentstatuscode| string|   
fte_teaching| number|   
fte_administrative| number|   
fte_pupilservices| number|   
filecreated| date|   
age| number|   
  
### staff_fte

Column Name| Data Type| Description  
---|---|---  
academicyear| integer|   
recid| integer|   
districtcode| integer|   
schoolcode| integer|   
countyname| string|   
districtname| string|   
schoolname| string|   
jobclassification| integer|   
stafftype| string|   
fte| number|   
filecreated| date|   
  
## References

Urls used in the creation of this data package.

  * **[StaffCred12](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffCred12.txt#target_format=tsv>)**. 
  * **[StaffCred13](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffCred13.txt#target_format=tsv>)**. 
  * **[StaffCred14](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffCred14.txt#target_format=tsv>)**. 
  * **[StaffCred15](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffCred15.txt#target_format=tsv>)**. 
  * **[StaffCred16](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffCred16.txt#target_format=tsv>)**. 
  * **[StaffCred17](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffCred17.txt#target_format=tsv>)**. 
  * **[StaffCred18](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffCred18.txt#target_format=tsv>)**. 
  * **[StaffDemo12](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffDemo12.txt#target_format=tsv>)**. 
  * **[StaffDemo13](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffDemo13.txt#target_format=tsv>)**. 
  * **[StaffDemo14](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffDemo14.txt#target_format=tsv>)**. 
  * **[StaffDemo15](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffDemo15.txt#target_format=tsv>)**. 
  * **[StaffDemo16](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffDemo16.txt#target_format=tsv>)**. 
  * **[StaffDemo17](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffDemo17.txt#target_format=tsv>)**. 
  * **[StaffDemo18](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffDemo18.txt#target_format=tsv>)**. 
  * **[StaffSchoolFTE12](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffSchoolFTE12.txt#target_format=tsv&encoding=latin1>)**. 
  * **[StaffSchoolFTE13](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffSchoolFTE13.txt#target_format=tsv&encoding=latin1>)**. 
  * **[StaffSchoolFTE14](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffSchoolFTE14.txt#target_format=tsv&encoding=latin1>)**. 
  * **[StaffSchoolFTE15](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffSchoolFTE15.txt#target_format=tsv&encoding=latin1>)**. 
  * **[StaffSchoolFTE16](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffSchoolFTE16.txt#target_format=tsv&encoding=latin1>)**. 
  * **[StaffSchoolFTE17](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffSchoolFTE17.txt#target_format=tsv&encoding=latin1>)**. 
  * **[StaffSchoolFTE18](<https://www3.cde.ca.gov/demo-downloads/staffclass/StaffSchoolFTE18.txt#target_format=tsv&encoding=latin1>)**. 


## Packages

  * **s3** s3://library.metatab.org/cde.ca.gov-staff-1.1.2.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-staff-1.1.2.csv>
  * **source** <https://github.com/metatab-packages/cde.ca.gov-collection.git>


### Accessing Data in Vanilla Pandas
```
import pandas as pd


staff_cred_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-staff-1.1.2/data/staff_cred.csv')
staff_demo_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-staff-1.1.2/data/staff_demo.csv')
staff_fte_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-staff-1.1.2/data/staff_fte.csv')
```

### Accessing Package in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-staff-1.1.2.csv')

# Create Dataframes
staff_cred_df = pkg.resource('staff_cred').dataframe()
staff_demo_df = pkg.resource('staff_demo').dataframe()
staff_fte_df = pkg.resource('staff_fte').dataframe()
```
