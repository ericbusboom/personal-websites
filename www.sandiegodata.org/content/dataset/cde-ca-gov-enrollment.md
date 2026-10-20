---
title: "Enrollment by school"
date: 2019-08-12T19:45:10+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "education"]
author: "metapack"
description: "School-level enrollment by racial/ethnic designation, gender, and grade."
---

_School-level enrollment by racial/ethnic designation, gender, and grade._

`cde.ca.gov-enrollment-1.2.2`. Modified 2022-06-17T17:38:10

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[enrollment](<http://library.metatab.org/cde.ca.gov-enrollment-1.2.2/data/enrollment.csv>)**. School enrollment, 2007 to 2021
  * **[race_eth](<http://library.metatab.org/cde.ca.gov-enrollment-1.2.2/data/race_eth.csv>)**. Simplified structure for race/ethnicity


## Documentation

Enrollment by school and demographic group for the years 2007 to 2018. The upstream dataset has enrollment data files for yearlier years, as early as 1981, but these files have a different structure.

## Caveats

The download page includes this note: 
[code] 
    Note these data files contain enrollment data for primary enrollments only. 
    It does not include short-term enrollments. For data on short-term enrollments, 
    please refer to the Primary and Short-term Enrollment by School data files.
    
[/code]

Some of the annual files have a Race/Ethincity code of '8', which corresponds to "Multiple or No Response" in he 1998 to 2006 file structure, but is not defined for this set of files. 

## Versions

  1. Initial Version


## License

The source data, from the California Department of Education, does not explicitly reference a license, but since the top-level website for California indicates that data published on the State of California website [is generally in the public domain](<https://www.ca.gov/use/>), we assume it is in the public domain. Derived data included in this package is also in the public domain. Metadata in this package ( contained in the `metadata.csv` file ) is derived from metadata for the source package, and is also in the public domain. 

Programs used for data transformation (contained in the `notebooks` directory), are Copyright 2021 Civic Knowledge, and are relased under the [Creative Commons Attribution-ShareAlike 4.0 International License.](<https://creativecommons.org/licenses/by-sa/4.0/>)

### Documentation Links

  * [data_dictionary](<https://www.cde.ca.gov/ds/ad/fsenr.asp>) Table columns and descriptions.
  * [Documentation Page](<http://library.metatab.org/cde.ca.gov-enrollment-1.2.2/index.html>)
  * [download_page](<https://www.cde.ca.gov/ds/ad/enrolldowndata.asp>) Enrollment by School download page


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

enrollment | race_eth_07_18 | race_eth   


### enrollment

Column Name| Data Type| Description  
---|---|---  
year| integer| File year of source data  
cdscode| integer| This 14-digit code is the official, unique identification of a school within California. The first two digits identify the county, the next five digits identify the school district, and the last seven digits identify the school.  
county| string| County name.  
district| string| District name.  
school| text| School name.  
ethnic| integer| Racial/ethnic designation. This field is coded as follows: \- Code 0 = Not reported \- Code 1 = American Indian or Alaska Native, Not Hispanic \- Code 2 = Asian, Not Hispanic \- Code 3 = Pacific Islander, Not Hispanic \- Code 4 = Filipino, Not Hispanic \- Code 5 = Hispanic or Latino \- Code 6 = African American, not Hispanic \- Code 7 = White, not Hispanic \- Code 9 = Two or More Races, Not Hispanic (See Glossary for complete definitions of the ethnic groups.)  
gender| string| Gender. This field is a coded as follows: \- M = Male \- F = Female  
kdgn| integer| Students enrolled in kindergarten.  
gr_1| integer| Students enrolled in grade one.  
gr_2| integer| Students enrolled in grade two.  
gr_3| integer| Students enrolled in grade three.  
gr_4| integer| Students enrolled in grade four.  
gr_5| integer| Students enrolled in grade five.  
gr_6| integer| Students enrolled in grade six.  
gr_7| integer| Students enrolled in grade seven.  
gr_8| integer| Students enrolled in grade eight.  
ungr_elm| integer| Students enrolled in ungraded elementary classes in grades kindergarten through grade eight.  
gr_9| integer| Students enrolled in grade nine.  
gr_10| integer| Students enrolled in grade ten.  
gr_11| integer| Students enrolled in grade eleven.  
gr_12| integer| Students enrolled in grade twelve.  
ungr_sec| integer| Students enrolled in ungraded secondary classes in grades nine through twelve.  
enr_total| integer| Total school enrollment for fields Kindergarten (KDGN) through grade twelve (GR_12) plus ungraded elementary (UNGR_ELM) and ungraded secondary classes (UNGR_SEC). Adults in kindergarten through grade twelve programs are not included.  
adult| integer| Adults enrolled in kindergarten through grade twelve programs. This data does not include adults in independent study.  
  
### race_eth_07_18

Column Name| Data Type| Description  
---|---|---  
cdscode| integer| 14 digit CDS code, which uniquely identifies schools  
year| integer| Year of enrollment data  
na| number| Race/Ethnicity not known.  
aian| number| American Indian or Alaska Native, Not Hispanic  
asian| number| Asian, Not Hispanic  
pi| number| Pacific Islander, Not Hispanic  
filipino| number| Filipino, Not Hispanic  
hisp| number| Hispanic or Latino  
black| number| African American, not Hispanic  
nh_white| number| White, not Hispanic  
unk| number| Unknown code 8;Code 8 is "Multiple or No Response" in the 1998-2006 file structure, but is not defined for the post 2006 file structure.  
two_more| number| Two or More Races, Not Hispanic  
total| number| Sum of all other columns  
  
### race_eth

Column Name| Data Type| Description  
---|---|---  
cdscode| integer|   
year| integer|   
na| integer|   
aian| integer|   
asian| integer|   
pi| integer|   
filipino| integer|   
hisp| integer|   
black| integer|   
nh_white| integer|   
unk| integer|   
two_more| integer|   
total| integer|   
  
## References

Urls used in the creation of this data package.

  * **[enrollment_2021](<https://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2021-22&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2020](<https://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2020-21&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2019](<https://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2019-20&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2018](<http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2018-19&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2017](<http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2017-18&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2016](<http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2016-17&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2015](<http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2015-16&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2014](<http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2014-15&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2013](<http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2013-14&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2012](<http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2012-13&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2011](<http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2011-12&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2010](<http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2010-11&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2009](<http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2009-10&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2008](<http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2008-09&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 
  * **[enrollment_2007](<http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2007-08&cCat=Enrollment&cPage=filesenr.asp#target_format=tsv>)**. 


## Packages

  * **s3** s3://library.metatab.org/cde.ca.gov-enrollment-1.2.2.csv
  * **csv** <http://library.metatab.org/cde.ca.gov-enrollment-1.2.2.csv>
  * **source** <https://github.com/metatab-packages/cde.ca.gov-enrollment.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    enrollment_df =  pd.read_csv('http://library.metatab.org/cde.ca.gov-enrollment-1.2.2/data/enrollment.csv')
    race_eth_df =  pd.read_csv('http://library.metatab.org/cde.ca.gov-enrollment-1.2.2/data/race_eth.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/cde.ca.gov-enrollment-1.2.2.csv')
    
    # Create Dataframes
    enrollment_df = pkg.resource('enrollment').dataframe()
    race_eth_df = pkg.resource('race_eth').dataframe()
    
[/code]
