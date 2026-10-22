---
title: "Child and Adult Care Food Program (CACFP) Sites, 2020"
date: 2019-06-16T17:49:46+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "education"]
author: "metapack"
description: "The Child and Adult Care Food Program (CACFP) provides federal funding to"
---

_The Child and Adult Care Food Program (CACFP) provides federal funding to participating child care and adult day care centers, allowing the centers to serve nutritious meals to enrolled participants_

`cde.ca.gov-cacfp_sites-1.2.1`. Modified 2022-06-15T17:58:35

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[cacfp_sites](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-cacfp_sites-1.2.1/data/cacfp_sites.csv>)**. CACFP sites, with location geocode and program type dummy variables


## Documentation

California Department of Education CACFP sites file, with extra features, include:

  * Sites geocoded to Lat/Lon and Census tract
  * The `program_types` field is broken out into dummy variables
  * CDS codes are matched from the CDE schools list. 


## CDS Code Matching

There are 5 different methods for matching sites to schools in the schools file, each with its own code:

  * `fhs`: Fuzzy hash string, a has string based n the address. 
  * `fhs_nz`: The fuzzy hash strin, but without the zip code, which occasionally is wrong or changes. 
  * `name_city`: A lightly normalized ( alpha only, lowercase, combination of the site name and the site city
  * `name_county`: A lightly normalized combination of the site name and county
  * `mp_name`: The site name and county, with each word converted to it's metaphone. 


The matching method code is included in the `match_type` columns. For many of the matching types there can be more than one CDS code associated with the matching string, particularly the strings based on addresses. The `match_qc` value is the inverse of the number of values with the same matching code, so if the algorithm selected the first of 5 CDS codes, the `match_qc` value is .2

Only about of the 35% of the 5076 sites are matched. The number matched for each type of matching tecchnique is: 
[code] 
    Not Matched    3292
    fhs            1602
    name_city       161
    name_county      19
    mp_name           1
    fhs_nz            1
    
[/code]

## Versions

  1. Initial version
  2. Add faked CDS codes for sites that are not schools


## License

The source data, from the California Department of Education, does not explicitly reference a license, but since the top-level website for California indicates that data published on the State of California website [is generally in the public domain](<https://www.ca.gov/use/>), we assume it is in the public domain. Derived data included in this package is also in the public domain. Metadata in this package ( contained in the `metadata.csv` file ) is derived from metadata for the source package, and is also in the public domain. 

Programs used for data transformation (contained in the `notebooks` directory), are Copyright 2021 Civic Knowledge, and are relased under the [Creative Commons Attribution-ShareAlike 4.0 International License.](<https://creativecommons.org/licenses/by-sa/4.0/>)

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-cacfp_sites-1.2.1/index.html>)
  * [Program home page](<https://www.cde.ca.gov/ls/nu/cc/index.asp>)
  * [Download page](<https://www.cde.ca.gov/ds/sh/sn/cacfpcentermap.asp>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

cacfp_sites   


### cacfp_sites

Column Name| Data Type| Description  
---|---|---  
name| text|   
county| string|   
address| text|   
city| text|   
state| string|   
zip| string|   
geoid| string| Geoid of the Census tract that contains the site  
lat| number| Latitude of the site  
lon| number| Longitude of the site  
sponsor_name| string|   
contact| text| Site contact person name  
phone_number| string| Phone number for site or site contact person.  
program_type| string| Comma separated collection of site type strings.  
adc| integer| 1 if the program_type includes 'ADULT DAY CARE (ADC)', 0 otherwise  
adh| integer| 1 if the program_type includes 'ADULT DAY HEALTH (ADH)', 0 otherwise  
atr| integer| 1 if the program_type includes 'AT RISK SITE (ATR)', 0 otherwise  
hom| integer| 1 if the program_type includes 'EMERGENCY SHELTER (HOM)', 0 otherwise  
hsc| integer| 1 if the program_type includes 'HEAD START CENTER (HSC)', 0 otherwise  
itc| integer| 1 if the program_type includes 'INFANT/TODDLER (ITC)', 0 otherwise  
other| integer| 1 if the program_type includes 'OTHER', 0 otherwise  
ccc| integer| 1 if the program_type includes 'PRESCHOOL AGE CENTER (CCC)', 0 otherwise  
sac| integer| 1 if the program_type includes 'SCHOOL AGE CENTER (SAC)', 0 otherwise  
sps| integer| 1 if the program_type includes 'STATE PRE SCHOOL CENTER (SPS)', 0 otherwise  
cdscode| string| Matched CDS code  
match_type| string| Way the CDS code way matched: fhs, name_city, name_county, fhs_nz, mp_name  
match_qc| float| The inverse of the number of records that matched. Higher values are more definite matches  
  
## References

Urls used in the creation of this data package.

  * **data/geocodes.csv**. Externally geocoded site locations. Geocoded with Geocodio.io
  * **[cacfp_sites_source](<https://www.cde.ca.gov/ds/sh/sn/documents/apcacfpcentersites2020.xlsx#&headers=5&start=6>)**. List of Child and Adult Care Food Program (CACFP) sites
  * **metapack+https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-schools-1.csv#public_schools**. California schools and districts
  * **metapack+https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-county_codes-ca-1.csv#ca_county_codes**. California government codes for counties, used in CDS codes


## Packages

  * **s3** s3://library.metatab.org/cde.ca.gov-cacfp_sites-1.2.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-cacfp_sites-1.2.1.csv>
  * **source** <https://github.com/metatab-packages/cde.ca.gov.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    cacfp_sites_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-cacfp_sites-1.2.1/data/cacfp_sites.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/cde.ca.gov-cacfp_sites-1.2.1.csv')
    
    # Create Dataframes
    cacfp_sites_df = pkg.resource('cacfp_sites').dataframe()
    
[/code]
