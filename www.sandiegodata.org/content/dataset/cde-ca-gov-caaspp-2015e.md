---
title: "CAASPP Test Results"
date: 2019-05-23T03:37:41+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "education"]
author: "metapack"
description: "California Assessment of Student Performance and Progress"
---

_California Assessment of Student Performance and Progress_

`cde.ca.gov-caaspp-2015e-2.1.1`. Modified 2022-08-09T20:25:49

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[subgroup_ids](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-caaspp-2015e-2.1.1/data/subgroup_ids.csv>)**. Subgroup codes and names
  * **[test_ids](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-caaspp-2015e-2.1.1/data/test_ids.csv>)**. Test codes and names
  * **[subgroups](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-caaspp-2015e-2.1.1/data/subgroups.csv>)**. Combined subgroups file
  * **[entities](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-caaspp-2015e-2.1.1/data/entities.csv>)**. Combined entities file


## Documentation

This dataset is a simple combination of multiple years of California Assessment of Student Performance and Progress (CAASPP) results, for the years 2015 on. The CAASPP was conducted in 2014, but the 2014 file has a different structure from other years ( it's a "pp" file, see below) so it is excluded from this package.

## Download Structure

The `Base Download` documentation link points to an FTP-like web directory of files, which contain the downloadable files. The other download pages have links to the files in these directories. These directories, as well as the dataset webpages are a bit complex. There seems to be a few different sorts of test result files, but there isn't a clear distinction between them. These fiels include:

  * "Paper Based" results , for 2014 and 2015
  * Tests in Spanish, marked "STS" for 2016 and 2017
  * Files with code 'pp'. Some 'pp' files have additional codes 'p2' or 'p3'
  * Files with 'sb', often also with 'p2' or 'p3'


I think 'sb' means 'Smarter-Balanced'. 

The main page for accessing test results, https://caaspp.cde.ca.gov/, has an inconsistent set of links to result pages for each year. For some years, the links are to "STS" results, others are to "Paper-Based" and for 2018, the links are to the "STS" and "Smarter Balanced" results.

## Versions

  1. Initial version
  2. `total_tested_with_scores` datatype changed from 'unknown' to 'integer' with 'robust_int' transform


## License

The source data, from the California Department of Education, does not explicitly reference a license, but since the top-level website for California indicates that data published on the State of California website [is generally in the public domain](<https://www.ca.gov/use/>), we assume it is in the public domain. Derived data included in this package is also in the public domain. Metadata in this package ( contained in the `metadata.csv` file ) is derived from metadata for the source package, and is also in the public domain. 

Programs used for data transformation (contained in the `notebooks` directory), are Copyright 2021 Civic Knowledge, and are relased under the [Creative Commons Attribution-ShareAlike 4.0 International License.](<https://creativecommons.org/licenses/by-sa/4.0/>)

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-caaspp-2015e-2.1.1/index.html>)
  * [CAASPP Homepage](<https://caaspp.cde.ca.gov/>)
  * [CAASPP Download page, 2015](<https://caaspp.cde.ca.gov/sb2017/ResearchFileList?ps=true&lstTestType=B&lstCounty=00&lstCntyNam=Select%20County...&lstTestYear=2015>) Dataset page for 2015
  * [CAASPP Download page, 2016](<https://caaspp.cde.ca.gov/sb2017/ResearchFileList?ps=true&lstTestType=B&lstCounty=00&lstCntyNam=Select%20County...&lstTestYear=2016>) Dataset page for 2016
  * [CAASPP Download page, 2017](<https://caaspp.cde.ca.gov/sb2017/ResearchFileList?ps=true&lstTestType=B&lstCounty=00&lstCntyNam=Select%20County...&lstTestYear=2017>) Dataset page for 2017
  * [Base Download](<http://www3.cde.ca.gov/caasppresearchfiles/>) Web directory of downloadable files.


## Contacts

  * **Creator**

[California Department of Education, Assessment Development and Administration Division](<mailto:caaspp@cde.ca.gov>), [California Department of Education](<https://caaspp.cde.ca.gov/>)

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

subgroup_ids | test_ids | entities | subgroups   


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
  
### entities

Column Name| Data Type| Description  
---|---|---  
county_code| integer|   
district_code| integer|   
school_code| integer|   
filler| unknown|   
test_year| integer|   
type_id| integer|   
county_name| string|   
district_name| string|   
school_name| string|   
zip_code| string|   
type_id| integer|   
  
### subgroups

Column Name| Data Type| Description  
---|---|---  
county_code| integer|   
district_code| integer|   
school_code| integer|   
filler| unknown|   
test_year| integer|   
subgroup_id| integer|   
test_type| string|   
total_caaspp_enrollment| integer|   
total_tested_at_entity_level| integer|   
total_tested_at_subgroup_level| integer|   
grade| integer|   
test_id| integer|   
caaspp_reported_enrollment| integer|   
students_tested| integer|   
mean_scale_score| string|   
percentage_standard_exceeded| string|   
percentage_standard_met| string|   
percentage_standard_met_and_above| string|   
percentage_standard_nearly_met| string|   
percentage_standard_not_met| string|   
students_with_scores| integer|   
area_1_percentage_above_standard| string|   
area_1_percentage_at_or_near_standard| string|   
area_1_percentage_below_standard| string|   
area_2_percentage_above_standard| string|   
area_2_percentage_at_or_near_standard| string|   
area_2_percentage_below_standard| string|   
area_3_percentage_above_standard| string|   
area_3_percentage_at_or_near_standard| string|   
area_3_percentage_below_standard| string|   
area_4_percentage_above_standard| string|   
area_4_percentage_at_or_near_standard| string|   
area_4_percentage_below_standard| string|   
total_tested_with_scores| unknown|   
area_1_percentage_near_standard| unknown|   
area_2_percentage_near_standard| unknown|   
area_3_percentage_near_standard| unknown|   
area_4_percentage_near_standard| unknown|   
total_tested_at_reporting_level| unknown|   
total_tested_with_scores_at_reporting_level| unknown|   
students_enrolled| unknown|   
type_id| unknown|   
  
## References

Urls used in the creation of this data package.

  * **[entities15](<http://www3.cde.ca.gov/caasppresearchfiles/2017/sb/sb_ca2015_all_csv_v3.zip#sb_ca2015entities_csv.txt&target_format=csv>)**. Entities, 2015
  * **[entities16](<http://www3.cde.ca.gov/caasppresearchfiles/2017/sb/sb_ca2016_all_csv_v3.zip#sb_ca2016entities_csv.txt&target_format=csv&encoding=latin1>)**. Entities, 2016
  * **[entities17](<http://www3.cde.ca.gov/caasppresearchfiles/2017/sb/sb_ca2017_all_csv_v2.zip#sb_ca2017entities_csv.txt&target_format=csv&encoding=latin1>)**. Entities, 2017
  * **[entities18](<http://www3.cde.ca.gov/caasppresearchfiles/2018/sb/sb_ca2018_all_csv_v3.zip#sb_ca2018entities_csv.txt&target_format=csv&encoding=latin1>)**. Entities, 2018
  * **[entities20](<https://caaspp-elpac.cde.ca.gov/caaspp/researchfiles/sb_ca2021_all_csv_v2.zip#sb_ca2021entities_csv.txt&target_format=csv>)**. Entities, 2020
  * **[subgroups15](<http://www3.cde.ca.gov/caasppresearchfiles/2017/sb/sb_ca2015_all_csv_v3.zip#sb_ca2015_all_csv_v3.txt&target_format=csv>)**. Subgroups 2015
  * **[subgroups16](<http://www3.cde.ca.gov/caasppresearchfiles/2017/sb/sb_ca2016_all_csv_v3.zip#sb_ca2016_all_csv_v3.txt&target_format=csv>)**. Subgroups 2016
  * **[subgroups17](<http://www3.cde.ca.gov/caasppresearchfiles/2017/sb/sb_ca2017_all_csv_v2.zip#sb_ca2017_all_csv_v2.txt&target_format=csv>)**. Subgroups 2017
  * **[subgroups18](<http://www3.cde.ca.gov/caasppresearchfiles/2018/sb/sb_ca2018_all_csv_v3.zip#sb_ca2018_all_csv_v3.txt&target_format=csv>)**. Subgroups 2018
  * **[subgroups20](<https://caaspp-elpac.cde.ca.gov/caaspp/researchfiles/sb_ca2021_all_csv_v2.zip#sb_ca2021_all_csv_v2.txt&target_format=csv>)**. Subgroups2020


## Packages

  * **s3** s3://library.metatab.org/cde.ca.gov-caaspp-2015e-2.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-caaspp-2015e-2.1.1.csv>
  * **source** <https://github.com/metatab-packages/cde.ca.gov-caaspp-2015e.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    subgroup_ids_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-caaspp-2015e-2.1.1/data/subgroup_ids.csv')
    test_ids_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-caaspp-2015e-2.1.1/data/test_ids.csv')
    subgroups_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-caaspp-2015e-2.1.1/data/subgroups.csv')
    entities_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-caaspp-2015e-2.1.1/data/entities.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-caaspp-2015e-2.1.1.csv')
    
    # Create Dataframes
    subgroup_ids_df = pkg.resource('subgroup_ids').dataframe()
    test_ids_df = pkg.resource('test_ids').dataframe()
    subgroups_df = pkg.resource('subgroups').dataframe()
    entities_df = pkg.resource('entities').dataframe()
    
[/code]
