---
title: "Distressed Housing Tracts"
date: 2020-05-26T20:14:50+00:00
draft: false
categories: ["Dataset"]
tags: ["ffeic.gov", "ffiec.gov"]
author: "metapack"
description: "An extract of a subset of columns from the FFIEC Census Flat File, including"
---

_An extract of a subset of columns from the FFIEC Census Flat File, including flags that indicate a tract is distressed._

`ffiec.gov-census-tract-1.5.2`. Modified 2020-06-24T21:57:54

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[ffiec_distressed](<https://library-metatab-org.s3.amazonaws.com/ffiec.gov-census-tract-1.5.2/data/ffiec_distressed.csv>)**. Distressed tracts


## Documentation

This dataset extracts the columns for distressed tracts from the FFIEC compilation of census data, for use in their FFIEC Census Windows Application. It includes only 25 columns, the first 17 columns of the file, which have geographic identifiers, median income, and three population totals. The reamaining 8 columns hold flags to indicate if a tract is distressed. 

  * 1205 Identifies Income Level Indicator 
  * 1206 Meets current year's poverty CRA distressed criterion? 
  * 1207 Meets current year's unemployment CRA distressed criterion? 
  * 1208 Meets current year's population CRA distressed criterion? 
  * 1209 Meets current year's remote rural (low density) CRA underserved criterion? 
  * 1210 Meets at least one of the previous year's CRA distressed criteria? 
  * 1211 Meets previous year's CRA underserved criterion? 
  * 1212 Meets at least one of current or previous year's CRA distressed/underserved tract criteria? 


## Caveats

The 2017 file, as distributed by FFIEC, is broken: it includes a ZIP file with in the ZIP file, which Metapack cannot read. This file has been manually extracted and stored in the source package.

### Documentation Links

  * [File information](<https://library-metatab-org.s3.amazonaws.com/ffiec.gov-census-tract-1.5.2/doc/cen2018.pdf>) Description of the 2018 census file, including all columns. Other years are similar
  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/ffiec.gov-census-tract-1.5.2/index.html>)
  * [homepage](<https://www.ffiec.gov/censusapp.htm>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

ffiec_distressed   


### ffiec_distressed

Column Name| Data Type| Description  
---|---|---  
geoid| string| ACS Geoid for tract  
year| integer| Key field. HMDA/CRA collection year  
msa_md_code| integer| Key field. MSA/MD Code  
state| integer| Key field. FIPS state code  
county| integer| Key field. FIPS county code  
tract| integer| Key field. Census tract. Implied decimal point.  
principal_city_flag| integer| Principal city flag. 0=not principal city 1=principal city  
small_county_flag| string| Small county flag. T=tract record S=small county I=Island Area  
split_tract_flag| string| Split tract flag. N=tract number occurs w/in one MA S=split between MAs  
demo_flag| string| Demographic data flag. X=Tot persons/population or median family income is 0 D=tot persons/population and median family income are not 0 I=Island Area  
urban_rural_flag| string| Urban/rural flag. U=urban R=rural M=mixed I=Island Area  
msa_family_income| integer| Median Family Income of MSA in which tract resides  
msa_household_income| integer| Median Household Income of MSA in which tract resides  
tract_household_income| integer| Median household income for tract.  
tract_family_income_pct| number| Tract median family income as a percentage of the MSA/MD median family income. Two decimal places, truncated.  
ffiec_median_income| integer| FFIEC Estimated MSA/MD Median Family Income  
population| integer| Total persons  
families| integer| Total families  
households| integer| Total households  
female| integer| Total female population  
male| integer| Total male population  
nonwhite| integer| Total population minus white alone population  
minority_percent| integer| Minority population as percent of tract population rounded to two decimal places  
income_level| integer| Identifies Income Level Indicator (low, mod, mid, upper income areas)  
poverty_distressed| string| Meets current year's poverty CRA distressed criterion? 'X' - Yes , ' ' (blank space) - No  
unemployment_distressed| string| Meets current year's unemployment CRA distressed criterion? 'X' - Yes , ' ' (blank space) - No  
population_distressed| string| Meets current year's population CRA distressed criterion? 'X' - Yes , ' ' (blank space) - No  
rural_underserved| string| Meets current year's remote rural (low density) CRA underserved criterion? 'X' -Yes, ' ' (blank space) - No  
last_year_distressed| string| Meets at least one of the previous year's CRA distressed criteria? 'X' - Yes , ' ' (blank space) - No  
last_year_underserved| string| Meets previous year's CRA underserved criterion? 'X' - Yes , ' ' (blank space) - No  
current_prior_distressed| string| Meets at least one of current or previous year's CRA distressed/underserved tract criteria? 'X' - Yes, ' ' (blank space) - No  
  
## References

Urls used in the creation of this data package.

  * **[ffiec_census_2013](<https://www.ffiec.gov/Census/Census_Flat_Files/Census2013.zip#*.csv>)**. 2013 Census Flat File
  * **[ffiec_census_2014](<https://www.ffiec.gov/Census/Census_Flat_Files/CENSUS2014.ZIP#*.csv>)**. 2014 Census Flat File
  * **[ffiec_census_2015](<https://www.ffiec.gov/Census/Census_Flat_Files/CENSUS2015.zip#*.csv>)**. 2015 Census Flat File
  * **[ffiec_census_2016](<https://www.ffiec.gov/Census/Census_Flat_Files/CENSUS2016.zip#*.csv>)**. 2016 Census Flat File
  * **data/Census2017.zip#*.csv**. 2017 Census Flat File
  * **[ffiec_census_2018](<https://www.ffiec.gov/Census/Census_Flat_Files/CENSUS2018.zip#*.csv>)**. 2018 Census Flat File
  * **[ffiec_census_2019](<https://www.ffiec.gov/Census/Census_Flat_Files/CENSUS2019.zip#*.csv>)**. 2019 Census Flat File


## Packages

  * **s3** s3://library.metatab.org/ffiec.gov-census-tract-1.5.2.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/ffiec.gov-census-tract-1.5.2.csv>
  * **source** <https://github.com/metatab-packages/ffiec.gov-census-tract.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    ffiec_distressed_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/ffiec.gov-census-tract-1.5.2/data/ffiec_distressed.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/ffiec.gov-census-tract-1.5.2.csv')
    
    # Create Dataframes
    ffiec_distressed_df = pkg.resource('ffiec_distressed').dataframe()
    
[/code]
