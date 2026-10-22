---
title: "Chronic Absenteeism"
date: 2019-05-23T03:37:07+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "education"]
author: "metapack"
description: "Student absenteeism data by ethnicity, gender, program subgroup, and grade span."
---

_Student absenteeism data by ethnicity, gender, program subgroup, and grade span. Chronic absenteeism counts, cumulative enrollment, and chronic absenteeism rate data are provided._

`cde.ca.gov-absenteeism-2`


## Resources

  * **[chronic_absenteeism](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-absenteeism-2/data/chronic_absenteeism.csv>)**. Combined Chronic Absenteeism files


## Documentation

### Documentation Links

  * [https://www.cde.ca.gov/ds/sd/sd/filesabd.asp](<Dataset Homepage>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-absenteeism-2.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-absenteeism-2.csv>
  * **source** <https://github.com/Metatab/metatab-packages.git>


### Accessing Packages in Metapack
```
import metapack as mp
# ZIP Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-absenteeism-2.zip')
# CSV Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-absenteeism-2.csv') 

resource = pkg.resource('resource_name') # Get a resource
df = resource.dataframe() # Create a pandas Dataframe
gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
```

## Data Dictionary

chab17 | chab16 | chronic_absenteeism   


### chab17

Column Name| Data Type| Description  
---|---|---  
academic_year| string|   
aggregate_level| string|   
county_code| integer|   
district_code| string|   
school_code| string|   
county_name| string|   
district_name| string|   
school_name| string|   
is_charter| string|   
reporting_category| string|   
cumulative_enrollment| string|   
cumulative_eligible_enrollment| string|   
chronic_absenteeism_count| string|   
chronic_absenteeism_rate| string|   
  
### chab16

Column Name| Data Type| Description  
---|---|---  
academic_year| string|   
aggregate_level| string|   
county_code| integer|   
district_code| string|   
school_code| string|   
county_name| string|   
district_name| string|   
school_name| string|   
is_charter| string|   
reporting_category| string|   
cumulative_enrollment| string|   
chronic_absenteeism_count| string|   
chronic_absenteeism_rate| string|   
  
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
  
## References

Urls used in the creation of this data package.

  * **ftp://ftp.cde.ca.gov/demo/attendance/ChrAbsRate1718.txt#target_format=tsv**. Chronic Absenteeism 2017-2018
  * **ftp://ftp.cde.ca.gov/demo/attendance/ChrAbsRate1617.txt#target_format=tsv**. Chronic Absenteeism 2016-2017


Last Modified 2019-05-22T19:15:44
