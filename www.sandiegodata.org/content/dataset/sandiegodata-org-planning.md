---
title: "San Diego Planning Database"
date: 2019-06-12T21:55:10+00:00
draft: false
categories: ["build_environment", "Dataset", "planning"]
tags: ["build_environment", "planning", "sandiegodata.org"]
author: "metapack"
description: "<!-- wp:paragraph --> <p><em></em></p> <!-- /wp:paragraph -->  <!-- wp:paragraph --> <p><code>sandiegodata.org-planning-1</code></p> <!-- /wp:paragraph -->  <!-- wp:paragraph --> <p>&lt;a href=&quot;#"
---

__

`sandiegodata.org-planning-1`


## Resources

  * **[tracts](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1/data/tracts.csv>)**. Tract information
  * **[tract_communities](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1/data/tract_communities.csv>)**. Link tracts to communities and cities
  * **[tract_boundaries](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1/data/tract_boundaries.csv>)**. Geographic boundaries for tracts
  * **[community_boundaries](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1/data/community_boundaries.csv>)**. Geographic boundaries for communities and cities
  * **[tract_diabetes](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1/data/tract_diabetes.csv>)**. 
  * **[hpi](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1/data/hpi.csv>)**. Healthy places index
  * **[business_sites](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1/data/business_sites.csv>)**. Point locations for businesses
  * **[business_tract_counts](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1/data/business_tract_counts.csv>)**. Business counts linked to tracts
  * **[acs_pdb](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1/data/acs_pdb.csv>)**. Planning database for tracts in SD County, ACS columns
  * **[cen10_pdb](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1/data/cen10_pdb.csv>)**. Planning database for tracts in SD County, Census 2010 columns


## Documentation

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1.csv>
  * **source** <https://github.com/sandiegodata/planning-database.git>


### Accessing Packages in Metapack
```
import metapack as mp
# ZIP Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1.zip')
# CSV Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-1.csv') 

resource = pkg.resource('resource_name') # Get a resource
df = resource.dataframe() # Create a pandas Dataframe
gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
```

## Data Dictionary

tracts | tract_links | community_boundaries | tract_diabetes | hpi | tract_boundaries | acs_pdb | tract_communities | business_sites | business_tract_counts | cen10_pdb   


### tracts

Column Name| Data Type| Description  
---|---|---  
geoid| string| Tract geoid, ACS format  
statefp| integer| State FIPS code  
countyfp| integer| County FIPS code  
tractce| integer| Census tract code  
name| number| Census tract name, this is the census tract code converted to an integer or integer plus two-digit decimal if the last two characters of the code are not both zeros.  
namelsad| string| Translated legal/statistical area description and the census tract name  
mtfcc| string| MAF/TIGER feature class code (G5020)  
funcstat| string| Functional status  
aland| integer| Land area  
awater| integer| Water area  
intptlat| number| Latitude of the internal point  
intptlon| number| Longitude of the internal point  
  
### tract_links

Column Name| Data Type| Description  
---|---|---  
geoid| string| Tract Geoid  
city_name| string| Name of the city the tract is in.  
city_code| string| Code for the city the tract is in.  
community_name| string| Community name  
community_cpcode| integer| Community planning code  
community_code| string| Short community Mnemonic code.  
  
### community_boundaries

Column Name| Data Type| Description  
---|---|---  
type| string| Record type: city, sd_community, county_community, county  
name| string| Community name  
name_code| string| Short name code  
city| string| City the community is in, or the county.  
link_code| string| Unique code for linking records  
geometry| string| Boundary geometry, in WKT format.  
  
### tract_diabetes

Column Name| Data Type| Description  
---|---|---  
geoid| string|   
asian| number|   
black| string|   
hisp| number|   
nhwhite| number|   
other| number|   
total| number|   
  
### hpi

Column Name| Data Type| Description  
---|---|---  
geoid| string| ACS format geoid  
pop2010| integer| population  
pct2010gq| number| population in group quarters in 2010  
city| text| City associated with centroid of census tract  
zip| integer| 5-digit postal zip code  
county_fips| integer| 4-digit code of county  
county_name| string| Name of county  
urbantype| string| Census classification of urban type  
hpi2score| number| Total score of HPI  
hpi2_pctile_pos| number| Percentile ranking of HPI score (positive frame)  
hpi2_pctile_neg| number| Percentile ranking of HPI score (negative frame)  
hpi_top25pct| string| Top 25% most advantaged  
quintiles| integer| Quintile of HPI score  
quartiles| integer| Quartile of HPI score  
economic| number| Economic policy action area score, summed Z-scores of individual policy action area variables  
economic_pctile| number| Percentile ranking ranking of "economic" policy action area z score  
education| number| Education score, summed Z-scores of individual policy action area variables  
education_pctile| number| Percentile ranking of "education" policy action area z score  
housing| number| Housing policy action area score, summed Z-scores of individual policy action area variables  
houseing_pctile| number| Percentile ranking of "housing" policy action area z score  
healthcareaccess| number| Healthcare Access policy action area score, z-score of insurance variable  
healthcareaccess_pctile| number| Percentile ranking of "healthcare access" policy action area z score  
neighborhood| number| Neighborhood policy action area score, summed Z-scores of individual policy action area variables  
neighborhood_pctile| number| Percentile ranking of "neighborhood" policy action area z score  
pollution| number| Pollution ("Clean Environment") policy action area score, summed Z-scores of individual policy action area variables  
pollution_pctile| number| Percentile ranking of "pollution" policy action area z score  
transportation| number| Transportation policy action area score, summed Z-scores of individual policy action area variables  
transportation_pctile| number| Percentile ranking of "transportation" policy action area z score  
social| number| Social policy action area score, summed Z-scores of individual policy action area variables  
social_pctile| number| Percentile ranking of "social" policy action area z score  
insured| number| Percentage of adults aged 18 to 64 years currently insured  
insured_pctile| number| Percentile ranking of percentage of adults aged 18 to 64 years currently insured  
uncrowded| number| Percentage of households with less or equal to 1 occupant per room  
uncrowded_pctile| number| Percentile ranking of uncrowded households  
homeownership| number| Percentage of occupied housing units occupied by property owners  
homeownership_pctile| number| Percentile ranking of percentage of occupied housing units occupied by property owners  
automobile| number| Percentage of households with access to an automobile  
automobile_pctile| number| Percentile ranking of households with access to an automobile  
commute| number| Percentage of workers (16 years and older) who commute to work by transit, walking, or cycling  
commute_pctile| number| Percentile ranking of percentage of workers (16 years and older) who commute to work by transit, walking, or cycling  
inpreschool| number| Percentage of 3 and 4 year olds enrolled in school  
inpreschool_pctile| number| Percentile ranking of 3 and 4 year olds enrolled in school  
inhighschool| number| Percentage of 15-17 year olds enrolled in school  
inhighschool_pctile| number| Percentile ranking of 15-17 year olds enrolled in school  
bachelorsed| number| Percentage of population over age 25 with a bachelor's education or higher  
bachelorsed_pctile| number| Percentile ranking of percentage of population over age 25 with a bachelor's education or higher  
employed| number| Percentage of population aged 25-64 who are employed  
employed_pctile| number| Percentile ranking of population aged 25-64 who are employed  
abovepoverty| number| Percent of the population with an income exceeding 200% of federal poverty level  
abovepoverty_pctile| number| Percentile ranking of the population with an income exceeding 200% of federal poverty level  
income| integer| Median annual household income  
income_pctile| number| Percentile ranking of median annual household income  
retail| number| Gross retail, entertainment, and education employment density (jobs/acre) on unprotected land  
retail_pctile| number| Percentile ranking of employment density for retail, entertainment, and educational uses  
parkaccess| number| Percentage of the population living within a half-mile of a park, beach, or open space greater than 1 acre  
parkaccess_pctile| number| Percentile ranking of the population living within a half-mile of a park, beach, or open space greater than 1 acre  
treecanopy| number| Population-weighted percentage of the census tract area without tree canopy  
treecanopy_pctile| number| Percentile ranking of population-weighted percentage of the census tract area without tree canopy  
alcoffsale| number| Percent of Population beyond 1/4 Mile of Off-Sale Alcohol Outlets  
alcoffsale_pctile| number| Percentile ranking of the opulation within 1/4 Mile of Off-Sale Alcohol Outlets  
voting| number| Percentage of registered voters voting in the 2012 general election  
voting_pctile| number| Percentile ranking of registered voters voting in the 2012 general election  
ownsevere| number| Percent of low income owner households with housing costs exceeding 50% of income  
ownsevere_pctile| number| Percentile ranking of low income owner households with housing costs exceeding 50% of income  
rentsevere| number| Percent of low income renter households with housing costs exceeding 50% of income  
rentsevere_pctile| number| Percentile ranking of low income renter households with housing costs exceeding 50% of income  
houserepair| number| Percent of households with kitchen facilities and plumbing  
houserepair_pctile| number| Percentile ranking of the households with kitchen facilities and plumbing  
twoparents| number| Percentage of children in married-couple family households or one parent with unmarried partner family households  
twoparents_pctile| number| Percentile ranking of percentage of children in married-couple family households or one parent with unmarried partner family households  
supermkts| number| Percentage of the urban population residing less than 1/2 mile from a supermarket/large grocery store, or the percent of the rural population living less than 1 mile from a supermarket/large grocery store  
supermkts_pctile| number| Percentile ranking of percentage of the urban population residing less than 1/2 mile from a supermarket/large grocery store, or the percent of the rural population living less than 1 mile from a supermarket/large grocery store  
ozone| number| Mean of summer months (May-October) of the daily maximum 8-hour ozone concentration (ppm), averaged over three years (2012 to 2014).  
ozone_pctile| number| Percentile ranking of mean of summer months (May-October) of the daily maximum 8-hour ozone concentration (ppm), averaged over three years (2012 to 2014).  
pm25| number| Annual mean concentration of PM2.5 (average of quarterly means, μg/m3), over three years (2012 to 2014)  
pm25_pctile| number| Percentile ranking of annual mean PM 2.5 level  
dieselpm| number| Spatial distribution of gridded diesel PM emissions from on-road and non-road sources for a 2012 summer day in July (kg/day)  
dieselpm_pctile| number| Percentile ranking of spatial distribution of gridded diesel PM emissions from on-road and non-road sources for a 2012 summer day in July (kg/day)  
h20contam| number| Cal EnviroScreen 3.0 drinking water contaminant index for selected contaminants  
h20contam_pctile| number| Percentile ranking of Cal EnviroScreen 3.0 drinking water contaminant index for selected contaminants  
leb| number| Life Expectancy at Birth  
leb_pctile| number| Percentile ranking of life expectancy at birth  
white_pct| number| Percent of Whites in the total population  
black_pct| number| Percent of Blacks in the total population  
asian_pct| number| Percent of Asians in the total population  
latino_pct| number| Percent of Latinos in the total population  
multiple_pct| number| Percent of two or more races in the total population  
nativeam_pct| number| Percent of American Indian/Alaskan Natives in the total population  
pacificisl_pct| number| Percent of Native Hawaiians and other Pacific Islanders in the total population  
other_pct| integer| Percent of some other race in the total population  
version| string| Date file was created  
  
### tract_boundaries

Column Name| Data Type| Description  
---|---|---  
geoid| string| Tract geoid, ACS format  
geometry| string| Tract boundary geometry  
  
### acs_pdb

Column Name| Data Type| Description  
---|---|---  
geoid| string| Subdivision of a County or statistically equivalent entity (0 to over 25,000 people per Tract with an average size of 4,200)  
flag| string| If a tract contains only uninhabitable land, this variable is filled. Otherwise, this variable is blank.  
land_area| number| Land area of geographical entity in square miles  
aian_land| integer| The number of block groups in this tract that are located on any part of an American Indian, Alaska Native, or Native Hawaiian area  
tot_population| integer| U.S. resident population includes everyone who meets the ACS residence rules in the tract at the time of the ACS interview  
tot_population_m90| integer| Margin of Error for Total Population  
males| integer| Number of Males in ACS Total Population  
males_m90| integer| Margin of Error for Number of Males  
females| integer| Number of Females in ACS Total Population  
females_m90| integer| Margin of Error for Number of Females  
pop_under_5| integer| Number of persons under age 5 at the time of the ACS interview  
pop_under_5_m90| integer| Margin of Error for Persons less than age 5  
pop_5_17| integer| Number of persons ages 5 to 17 at the time of the ACS interview  
pop_5_17_m90| integer| Margin of Error for Persons ages 5 to 17  
pop_18_24| integer| Number of persons ages 18 to 24 at the time of the ACS interview  
pop_18_24_m90| integer| Margin of Error for Persons ages 18 to 24  
pop_25_44| integer| Number of persons ages 25 to 44 at the time of the ACS interview  
pop_25_44_m90| integer| Margin of Error for Persons ages 25 to 44  
pop_45_64| integer| Number of persons ages 45 to 64 at the time of the ACS interview  
pop_45_64_m90| integer| Margin of Error for Persons ages 45 to 64  
pop_65plus| integer| Number of persons age 65 and over at the time of the ACS interview  
pop_65plus_m90| integer| Margin of Error for Persons ages 65 and over  
hispanic| integer| Number of people who identify as "Mexican", "Puerto Rican", "Cuban", or "another Hispanic, Latino, or Spanish origin" in the ACS population  
hispanic_m90| integer| Margin of Error of Hispanic Origin Population  
nh_white_alone| integer| Number of people who indicate no Hispanic origin and their only race as "White" or report entries such as Irish, German, Italian, Lebanese, Arab, Moroccan, or Caucasian in the ACS population  
nh_white_alone_m90| integer| Margin of Error of Non-Hispanic White only  
nh_blk_alone| integer| Number of people who indicate no Hispanic origin and their only race as "Black, African Am., or Negro" or report entries such as African American, Kenyan, Nigerian, or Haitian in the ACS population  
nh_blk_alone_m90| integer| Margin of Error of Non-Hispanic Black or African-American only  
nh_aian_alone| integer| Number of people who indicate no Hispanic origin and their only race as "American Indian or Alaska Native" or report entries such as Navajo, Blackfeet, Inupiat, Yup'ik, or Central/South American Indian groups in the ACS population  
nh_aian_alone_m90| integer| Margin of Error of Non-Hispanic American Indian and Alaska Native only  
nh_asian_alone| integer| Number of people who indicate no Hispanic origin and their only race as "Asian Indian", "Chinese", "Filipino", "Korean", "Japanese", "Vietnamese", or "Other Asian" in the ACS population  
nh_asian_alone_m90| integer| Margin of Error of Non-Hispanic Asian only  
nh_nhopi_alone| integer| Number of people who indicate no Hispanic origin and their only race as "Native Hawaiian", "Guamanian or Chamorro", "Samoan", or "Other Pacific Islander" in the ACS population  
nh_nhopi_alone_m90| integer| Margin of Error of Non-Hispanic Native Hawaiian and Other Pacific Islander only  
nh_sor_alone| integer| Number of people who indicate no Hispanic origin and their race as other than "White", "Hispanic", "Black or African American", "American Indian or Alaska Native", "Asian", and "Native Hawaiian or Other Pacific Islander" in the ACS population  
nh_sor_alone_m90| integer| Margin of Error of Non-Hispanic Some other Race only  
pop_5yrs_over| integer| Number of people ages 5 years and over at time of interview in the ACS population  
pop_5yrs_over_m90| integer| Margin of Error of Population 5 years and over  
othr_lang| integer| Number of people ages 5 years and over at the time of interview that speak a language other than English at home in the ACS population, regardless of ability to speak English  
othr_lang_m90| integer| Margin of Error of Population 5 years and over that speak a language other than English at home, regardless of ability to speak English  
age5p_only_english| integer| Number of people ages 5 years and over at the time of the interview that speak only English at home in the ACS  
age5p_only_english_m90| integer| Margin of Error of Population 5 years and over that speak only English at home  
age5p_spanish| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Spanish or Spanish Creole at home in the ACS. Examples include Ladino and Pachuco.  
age5p_spanish_m90| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Spanish or Spanish Creole at home  
age5p_french| integer| Number of people ages 5 years and over who speak English less than "very well" and speak French at home in the ACS. Examples include Cajun and Patois.  
age5p_french_m90| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak French at home  
age5p_german| integer| Number of people ages 5 years and over who speak English less than "very well" and speak German at home in the ACS. Examples include Luxembourgian.  
age5p_german_m90| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak German at home  
age5p_russian| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Russian at home in the ACS  
age5p_russian_m90| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Russian at home  
age5p_otheuro| integer| Number of people ages 5 years and over who speak English less than "very well" and speak some other Indo-European language at home in the ACS. Examples include Albanian, Gaelic, Lithuanian, and Romanian.  
age5p_otheuro_m90| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak some other Indo-European language at home  
age5p_korean| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Korean at home in the ACS  
age5p_korean_m90| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Korean at home  
age5p_chinese| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Chinese at home in the ACS. Examples include Cantonese, Formosan, and Mandarin.  
age5p_chinese_m90| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Chinese at home  
age5p_vietnamese| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Vietnamese at home in the ACS  
age5p_vietnamese_m90| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Vietnamese at home  
age5p_tagalog| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Tagalog at home in the ACS  
age5p_tagalog_m90| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Tagalog at home  
age5p_othasian| integer| Number of people ages 5 years and over who speak English less than "very well" and speak some other Asian language at home in the ACS. Examples include Turkish or Dravidian languages such as Malayalam, Telugu, and Tamil.  
age5p_othasian_m90| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak some other Asian language at home  
age5p_arabic| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Arabic at home in the ACS  
age5p_arabic_m90| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Arabic at home  
age5p_othunsp| integer| Number of people ages 5 years and over who speak English less than "very well" and speak some other or unspecified language at home in the ACS. Examples include Syriac, Finnish, other languages of the Americas, or no reported language.  
age5p_othunsp_m90| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak some other or unspecified language at home  
pop_25yrs_over| integer| Number of people ages 25 years and over at time of interview in the ACS population  
pop_25yrs_over_m90| integer| Margin of Error of Number of people 25 years old and over  
not_hs_grad| integer| Number of people ages 25 years and over at time of interview who are not high school graduates and have not received a diploma or the equivalent in the ACS population  
not_hs_grad_m90| integer| Margin of Error of Number of people 25 years old and over who are not high school graduates  
college| integer| Number of people ages 25 years and over at the time of interview with a college degree or higher in the ACS population  
college_m90| integer| Margin of Error of Persons 25 and over with a college degree or higher  
pov_univ| integer| Number of people excluding institutionalized people, people in military group quarters, people in college dormitories, and unrelated individuals under 15 years old in the ACS  
pov_univ_m90| integer| Margin of Error for Population for whom poverty level is determined  
prs_blw_pov_lev| integer| Number of people classified as below the poverty level given their total family or household income within the last year, family size, and family composition in the ACS population  
prs_blw_pov_lev_m90| integer| Margin of Error of Number of people classified as below the poverty level  
one_health_ins| integer| Number of people who have one type of health insurance coverage, including public or private insurance, in the ACS population  
one_health_ins_m90| integer| Margin of Error of Number of people who have one type of health insurance coverage  
two_plus_health_ins| integer| Number of people who have two or more types of health insurance at the same time, in the ACS population  
two_plus_health_ins_m90| integer| Margin of Error of Number of people who have two or more types of health insurance coverage  
no_health_ins| integer| Number of people who have no health insurance coverage, public or private, in the ACS population  
no_health_ins_m90| integer| Margin of Error of Number of people who have no health insurance coverage  
civ_labor_16plus| integer| Number of civilians ages 16 years and over at the time of the interview that are in the labor force in the ACS  
civ_labor_16plus_m90| integer| Margin of Error of Number of civilians 16 and over that are in the labor force  
civ_emp_16plus| integer| Number of civilians ages 16 years and over at the time of the interview that are employed in the ACS  
civ_emp_16plus_m90| integer| Margin of Error of Number of civilians 16 and over that are employed  
civ_unemp_16plus| integer| Number of civilians ages 16 years and over at the time of the interview that are unemployed in the ACS  
civ_unemp_16plus_m90| integer| Margin of Error of Number of civilians 16 and over that are unemployed  
civ_labor_16_24| integer| Number of civilians between the ages of 16 and 24 at the time of the interview who are in the labor force in the ACS  
civ_labor_16_24_m90| integer| Margin of error of Number of civilians between the ages of 16 to 24 who are in the labor force  
civ_emp_16_24| integer| Number of civilians between the ages of 16 and 24 at the time of the interview who are employed in the ACS  
civ_emp_16_24_m90| integer| Margin of Error of Number of civilians aged 16 to 24 who are employed  
civ_unemp_16_24| integer| Number of civilians between the ages of 16 and 24 at the time of the interview who are unemployed in the ACS  
civ_unemp_16_24_m90| integer| Margin of Error of Number of civilians aged 16 to 24 who are unemployed  
civ_labor_25_44| integer| Number of civilians between the ages of 25 and 44 at the time of the interview who are in the labor force in the ACS  
civ_labor_25_44_m90| integer| Margin of Error of Number of civilians aged 25 to 44 who are in the labor force  
civ_emp_25_44| integer| Number of civilians between the ages of 25 and 44 at the time of the interview who are employed in the ACS  
civ_emp_25_44_m90| integer| Margin of Error of Number of civilians aged 25 to 44 who are employed  
civ_unemp_25_44| integer| Number of civilians between the ages of 25 and 44 at the time of the interview who are unemployed in the ACS  
civ_unemp_25_44_m90| integer| Margin of Error of Number of civilians aged 25 to 44 who are unemployed  
civ_labor_45_64| integer| Number of civilians between the ages of 45 and 64 at the time of the interview who are in the labor force in the ACS  
civ_labor_45_64_m90| integer| Margin of Error of Number of civilians aged 45 to 64 who are in the labor force  
civ_emp_45_64| integer| Number of civilians between the ages of 45 and 64 at the time of the interview who are employed in the ACS  
civ_emp_45_64_m90| integer| Margin of Error of Number of civilians aged 45 to 64 who are employed  
civ_unemp_45_64| integer| Number of civilians between the ages of 45 and 64 at the time of the interview who are unemployed in the ACS  
civ_unemp_45_64_m90| integer| Margin of Error of Number of civilians aged 45 to 64 who are unemployed  
civ_noninst_pop| integer| Total number of noninstitutionalized civilians in the population  
civ_noninst_pop_m90| integer| Margin of Error of total number of noninstitutionalized civilians in the population  
pop_disabled| integer| Number of persons who have one or more disabilities in the ACS population  
pop_disabled_m90| integer| Margin of Error of Number of persons who have one or more disabilities in the ACS population  
pop_1yr_over| integer| Number of people ages 1 year and over at time of interview in the ACS population  
pop_1yr_over_m90| integer| Margin of Error for Number of people 1 year old and over  
diff_hu_1yr_ago| integer| Number of people who moved from another residence in the U.S. or Puerto Rico within the last year in the ACS population  
diff_hu_1yr_ago_m90| integer| Margin of Error of Different house one year ago  
born_us| integer| Number of people who are citizens of the United States at birth in the ACS. This includes respondents who said that they were born in the United States, Puerto Rico, a US Island Area (such as Guam), or abroad of American (US citizen) parent or parents.  
born_us_m90| integer| Margin of Error of Number of people who are US citizens at birth  
born_foreign| integer| Number of people who were not a citizen of the United States at birth. This includes respondents who indicated that they were a US citizen by naturalization or not a US citizen.  
born_foreign_m90| integer| Margin of Error of Number of people who were not US citizens at birth  
us_cit_nat| integer| Number of people who are citizens of the United States through naturalization in the ACS  
us_cit_nat_m90| integer| Margin of Error of Number of people who are US citizens through naturalization  
non_us_cit| integer| Number of people who are not citizens of the United States in the ACS  
non_us_cit_m90| integer| Margin of Error of Number of people who are not US citizens  
eng_vw_span| integer| Number of ACS households where a Spanish or Spanish Creole language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
eng_vw_span_m90| integer| Margin of Error of Spanish-No one 14 and over speaks English only or speaks English "very well"  
eng_vw_indo_euro| integer| Number of ACS households where an Indo-European language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
eng_vw_indo_euro_m90| integer| Margin of Error of INDO EURO -No one 14 and over speaks English only or speaks English "very well"  
eng_vw_api| integer| Number of ACS households where an Asian and Pacific Island language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
eng_vw_api_m90| integer| Margin of Error of API-No one 14 and over speaks English only or speaks English "very well"  
eng_vw_other| integer| Number of ACS households where a language other than English, Spanish, Indo-Euro, or API was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
eng_vw_other_m90| integer| Margin of Error of OTH-No one 14 and over speaks English only or speaks English "very well"  
eng_vw| integer| Number of ACS households where no one ages 14 years and over speaks English only or speaks English "very well"  
eng_vw_m90| integer| Margin of Error of No one 14 and over speaks English only or speaks English "very well"  
rel_family_hhd| integer| Number of ACS households where at least 2 members are related by birth, marriage, or adoption; same-sex couple households with no relatives of the householder present are not included  
rel_family_hhd_m90| integer| Margin of Error of Related family households  
mrdcple_fmly_hhd| integer| Number of ACS households in which the householder and his or her spouse are listed as members of the same household; does not include same-sex married couples  
mrdcple_fmly_hhd_m90| integer| Margin of Error of Married-Couple Family  
not_mrdcple_hhd| integer| Number of ACS households with no spousal relationship present  
not_mrdcple_hhd_m90| integer| Margin of Error of Number of ACS households with no spousal relationship present  
female_no_hb| integer| Number of ACS households with a female householder and no husband of householder present  
female_no_hb_m90| integer| Margin of Error of Female householder, no husband present  
nonfamily_hhd| integer| Number of ACS households where a householder lives alone or with nonrelatives only; includes same-sex couples where no relatives of the householder are present  
nonfamily_hhd_m90| integer| Margin of Error of Nonfamily household: Unrelated households  
sngl_prns_hhd| integer| Number of ACS households where a householder lives alone  
sngl_prns_hhd_m90| integer| Margin of Error of Single person householder living alone  
hhd_ppl_und_18| integer| Number of ACS households where one or more people are ages 18 years or under  
hhd_ppl_und_18_m90| integer| Margin of Error of Households with one or more people under 18 years  
tot_prns_in_hhd| integer| All persons (household population) in ACS occupied housing unit. This is the numerator to calculate the average household size.  
tot_prns_in_hhd_m90| integer| Margin of Error of Total Persons in households  
rel_child_under_6| integer| Number of ACS families with related children under 6 years old  
rel_child_under_6_m90| integer| Margin of Error of Number of families with related children under 6 years old  
hhd_moved_in| integer| Number of ACS households where the householder moved into the current unit in the year 2010 or later  
hhd_moved_in_m90| integer| Margin of Error of Number of households where the householder moved into the current unit in the year 2010 or later  
pub_asst_inc| integer| Number of ACS households that receive public assistance income (general assistance and Temporary Assistance to Needy Families)  
pub_asst_inc_m90| integer| Margin of Error of With Public Assistance Income  
med_hhd_inc| integer| Median ACS household income for the tract  
med_hhd_inc_m90| integer| Margin of Error of Med household income for the tract  
aggregate_hh_inc| integer| Sum of all incomes in the household  
aggregate_hh_inc_m90| integer| Margin of Error for Aggregate household income  
tot_housing_units| integer| Number of ACS living quarters in which the occupant(s) live separately from any other individuals in the building and have direct access  
tot_housing_units_m90| integer| Margin of Error for Total Housing Units  
tot_occp_units| integer| Number of ACS housing units classified as usual place of residence of the individual or group living in it  
tot_occp_units_m90| integer| Margin of Error for Total Occupied Housing Units  
tot_vacant_units| integer| Number of ACS housing units where no one is living regularly at the time of interview; units occupied at the time of interview entirely by persons who are staying two months or less and who have a more permanent residence elsewhere are classified as vacant  
tot_vacant_units_m90| integer| Margin of Error for Total vacant housing units  
renter_occp_hu| integer| Number of ACS occupied housing units that are not owner occupied, whether they are rented or occupied without payment of rent  
renter_occp_hu_m90| integer| Margin of Error for Number of renter occupied units  
owner_occp_hu| integer| Number of ACS housing units where owner or co-owner lives in it  
owner_occp_hu_m90| integer| Margin of Error for Number of owner occuped units  
single_unit| integer| Number of ACS housing units in which the structure contains only that single unit  
single_unit_m90| integer| Margin of Error for Number of units in structures containing only 1 housing unit  
mlt_u2_9_strc| integer| Number of ACS housing units in which the structure contains two or more housing units  
mlt_u2_9_strc_m90| integer| Margin of Error for Number of units in structures containing two or more housing units  
mlt_u10p| integer| Number of ACS housing units in which the structure contains 10 or more housing units  
mlt_u10p_m90| integer| Margin of Error for Number of units in structures containing 10 or more housing units  
mobile_homes| integer| Number of ACS housing units that are considered mobile homes  
mobile_homes_m90| integer| Margin of Error for Mobile Homes  
crowd_occp_u| integer| Number of ACS occupied housing units with more than 1.01 persons per room  
crowd_occp_u_m90| integer| Margin of Error for Occupied units with more than 1.01 persons per room  
occp_u_no_ph_srvc| integer| Number of ACS housing units without a working telephone and available service  
occp_u_no_ph_srvc_m90| integer| Margin of Error for Number of units without a telephone  
no_plumb| integer| Number of ACS housing units lacking complete plumbing facilities  
no_plumb_m90| integer| Margin of Error for housing units lacking complete plumbing facilities  
recent_built_hu| integer| Number of both occupied and vacant ACS housing units whose building was constructed in 2010 or later  
recent_built_hu_m90| integer| Margin of Error for HUs built 2010 or later  
med_house_value| integer| Median of ACS respondents' house value estimates for the tract  
med_house_value_m90| integer| Margin of Error for Med House value for the tract  
aggr_house_value| integer| Sum of all value estimates for owner-occupied ACS housing units in an area  
aggr_house_value_m90| integer| Margin of Error for Aggregate value in dollars  
low_response_score| number| A score predicting that a block group will produce a low mail return rate. This score is negatively associated with Mail Return Rate CEN 2010.  
pct_males| number| The percentage of the ACS population that is male  
pct_males_m90| number| Margin of error of the percentage of the ACS population that is male  
pct_females| number| The percentage of the ACS population that is female  
pct_females_m90| number| Margin of error of the percentage of the ACS population that is female  
pct_pop_under_5| number| The percentage of the ACS population that is under five years old  
pct_pop_under_5_m90| number| Margin of error of the percentage of the ACS population that is under five years old  
pct_pop_5_17| number| The percentage of the ACS population that is between 5 and 17 years old  
pct_pop_5_17_m90| number| Margin of error of the percentage of the ACS population that is between 5 and 17 years old  
pct_pop_18_24| number| The percentage of the ACS population that is between 18 and 24 years old  
pct_pop_18_24_m90| number| Margin of error of the percentage of the ACS population that is between 18 and 24 years old  
pct_pop_25_44| number| The percentage of the ACS population that is between 25 and 44 years old  
pct_pop_25_44_m90| number| Margin of error of the percentage of the ACS population that is between 25 and 44 years old  
pct_pop_45_64| number| The percentage of the ACS population that is between 45 and 64 years old  
pct_pop_45_64_m90| number| Margin of error of the percentage of the ACS population that is between 45 and 64 years old  
pct_pop_65plus| number| The percentage of the ACS population that is 65 years old or over  
pct_pop_65plus_m90| number| Margin of error of the percentage of the ACS population that is 65 years old or over  
pct_hispanic| number| The percentage of the ACS population that identify as "Mexican", "Puerto Rican", "Cuban", or "another Hispanic, Latino, or Spanish origin"  
pct_hispanic_m90| number| Margin of error of the percentage of the ACS population that identify as "Mexican", "Puerto Rican", "Cuban", or "another Hispanic, Latino, or Spanish origin"  
pct_nh_white_alone| number| The percentage of the ACS population that indicate no Hispanic origin and their only race as "White" or report entries such as Irish, German, Italian, Lebanese, Arab, Moroccan, or Caucasian  
pct_nh_white_alone_m90| number| Margin of error of the percentage of the ACS population that indicate no Hispanic origin and their only race as "White" or report entries such as Irish, German, Italian, Lebanese, Arab, Moroccan, or Caucasian  
pct_nh_blk_alone| number| The percentage of the ACS population that indicate no Hispanic origin and their only race as "Black, African Am., or Negro" or report entries such as African American, Kenyan, Nigerian, or Haitian  
pct_nh_blk_alone_m90| number| Margin of error of the percentage of the ACS population that indicate no Hispanic origin and their only race as "Black, African Am., or Negro" or report entries such as African American, Kenyan, Nigerian, or Haitian  
pct_nh_aian_alone| number| The percentage of the ACS population that indicate no Hispanic origin and their only race as "American Indian or Alaska Native" or report entries such as Navajo, Blackfeet, Inupiat, Yup'ik, or Central/South American Indian groups  
pct_nh_aian_alone_m90| number| Margin of error of the percentage of the ACS population that indicate no Hispanic origin and their only race as "American Indian or Alaska Native" or report entries such as Navajo, Blackfeet, Inupiat, Yup'ik, or Central/South American Indian groups  
pct_nh_asian_alone| number| The percentage of the ACS population that indicate no Hispanic origin and their only race as "Asian Indian", "Chinese", "Filipino", "Korean", "Japanese", "Vietnamese", or "Other Asian"  
pct_nh_asian_alone_m90| number| Margin of error of the percentage of the ACS population that indicate no Hispanic origin and their only race as "Asian Indian", "Chinese", "Filipino", "Korean", "Japanese", "Vietnamese", or "Other Asian"  
pct_nh_nhopi_alone| number| The percentage of the ACS population that indicate no Hispanic origin and their only race as "Native Hawaiian", "Guamanian or Chamorro", "Samoan", or "Other Pacific Islander"  
pct_nh_nhopi_alone_m90| number| Margin of error of the percentage of the ACS population that indicate no Hispanic origin and their only race as "Native Hawaiian", "Guamanian or Chamorro", "Samoan", or "Other Pacific Islander"  
pct_nh_sor_alone| number| The percentage of the ACS population that indicate no Hispanic origin and their race as other than "White", "Hispanic", "Black or African American", "American Indian or Alaska Native", "Asian", and "Native Hawaiian or Other Pacific Islander"  
pct_nh_sor_alone_m90| number| Margin of error of the percentage of the ACS population that indicate no Hispanic origin and their race as other than "White", "Hispanic", "Black or African American", "American Indian or Alaska Native", "Asian", and "Native Hawaiian or Other Pacific Islander"  
pct_pop_5yrs_over| number| The percentage of the ACS population who are ages 5 years and over at time of interview  
pct_pop_5yrs_over_m90| number| Margin of error of the percentage of the ACS population who are ages 5 years and over at time of interview  
pct_othr_lang| number| The percentage of the ACS population aged 5 years and over that speaks a language other than English at home  
pct_othr_lang_m90| number| Margin of error of the percentage of the ACS population aged 5 years and over that speaks a language other than English at home  
pct_age5p_only_eng| number| The percentage of the ACS population ages 5 years and over at the time of the interview that speak only English at home  
pct_age5p_only_eng_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over that speak only English at home  
pct_age5p_spanish| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Spanish or Spanish Creole at home. Examples include Ladino and Pachuco.  
pct_age5p_spanish_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Spanish or Spanish Creole at home  
pct_age5p_french| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak French at home. Examples include Cajun and Patois.  
pct_age5p_french_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak French at home  
pct_age5p_german| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak German at home. Examples include Luxembourgian.  
pct_age5p_german_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak German at home  
pct_age5p_russian| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Russian at home  
pct_age5p_russian_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Russian at home  
pct_age5p_otheuro| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak some other Indo-European language at home. Examples include Albanian, Gaelic, Lithuanian, and Romanian.  
pct_age5p_otheuro_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak some other Indo-European language at home  
pct_age5p_korean| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Korean at home  
pct_age5p_korean_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Korean at home  
pct_age5p_chinese| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Chinese at home. Examples include Cantonese,  
pct_age5p_chinese_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Chinese at home  
pct_age5p_vietnames| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Vietnamese at home  
pct_age5p_vietnames_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Vietnamese at home  
pct_age5p_tagalog| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Tagalog at home  
pct_age5p_tagalog_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Tagalog at home  
pct_age5p_othasian| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak some other Asian language at home. Examples include Turkish or Dravidian languages such as Malayalam, Telugu, and Tamil.  
pct_age5p_othasian_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak some other Asian language at home  
pct_age5p_arabic| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Arabic at home  
pct_age5p_arabic_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Arabic at home  
pct_age5p_othunsp| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak some other or unspecified language at home. Examples include Syriac, Finnish, other languages of the Americas, or no reported language.  
pct_age5p_othunsp_m90| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak some other or unspecified language at home  
pct_pop_25yrs_over| number| The percentage of the ACS population who are ages 25 years and over at time of interview  
pct_pop_25yrs_over_m90| number| Margin of error of the percentage of the ACS population who are ages 25 years and over at time of interview  
pct_not_hs_grad| number| The percentage of the ACS population aged 25 years and over that are not high school graduates and have not received a diploma or the equivalent  
pct_not_hs_grad_m90| number| Margin of error of the percentage of the ACS population aged 25 years and over that are not high school graduates  
pct_college| number| The percentage of the ACS population aged 25 years and over that have a college degree or higher  
pct_college_m90| number| Margin of error of the percentage of the ACS population aged 25 years and over that have a college degree or higher  
pct_pov_univ| number| The percentage of the ACS population that are not institutionalized people, people in military group quarters, people in college dormitories, and unrelated individuals under 15 years old  
pct_pov_univ_m90| number| Margin of Error for the percentage of the ACS population that are not institutionalized people, people in military group quarters, people in college dormitories, and unrelated individuals under 15 years old  
pct_prs_blw_pov_lev| number| The percentage of the ACS eligible population that are classified as below the poverty level given their total family or household income within the last year, family size, and family composition  
pct_prs_blw_pov_lev_m90| number| Margin of Error of the percentage of the ACS eligible population that are classified as below the poverty level  
pct_one_health_ins| number| The percentage of the ACS population that have one type of health insurance coverage, including public or private  
pct_one_health_ins_m90| number| Margin of Error of the percentage of the ACS population that have one type of health insurance  
pct_twophealthins| number| The percentage of the ACS population that have two or more types of health insurance  
pct_twophealthins_m90| number| Margin of Error of the percentage of the ACS population that have two or more types of health insurance  
pct_no_health_ins| number| The percentage of the ACS population that have no health insurance, public or private  
pct_no_health_ins_m90| number| Margin of Error of the percentage of the ACS population that have no health insurance  
pct_civ_emp_16p| number| The percentage of ACS civilians ages 16 years and over in the labor force that are employed  
pct_civ_emp_16p_m90| number| Margin of error of the percentage of civilians ages 16 years and over in the labor force that are employed  
pct_civ_unemp_16p| number| The percentage of ACS civilians ages 16 years and over in the labor force that are unemployed  
pct_civ_unemp_16p_m90| number| Margin of error of the percentage of civilians ages 16 years and over in the labor force that are unemployed  
pct_civ_emp_16_24| number| The percentage of ACS civilians between the ages of 16 and 24 in the labor force that are employed  
pct_civ_emp_16_24_m90| number| Margin of error of the percentage of civilians between the ages of 16 and 24 in the labor force that are employed  
pct_civ_unemp_16_24| number| The percentage of ACS civilians between the ages of 16 and 24 in the labor force that are unemployed  
pct_civ_unemp_16_24_m90| number| Margin of error of the percentage of civilians between the ages of 16 and 24 in the labor force that are unemployed  
pct_civ_emp_25_44| number| The percentage of ACS civilians between the ages of 25 and 44 in the labor force that are employed  
pct_civ_emp_25_44_m90| number| Margin of error of the percentage of civilians between the ages of 25 and 44 in the labor force that are employed  
pct_civ_unemp_25_44| number| The percentage of ACS civilians between the ages of 25 and 44 in the labor force that are unemployed  
pct_civ_unemp_25_44_m90| number| Margin of error of the percentage of civilians between the ages of 25 and 44 in the labor force that are unemployed  
pct_civ_emp_45_64| number| The percentage of ACS civilians between the ages of 45 and 64 in the labor force that are employed  
pct_civ_emp_45_64_m90| number| Margin of error of the percentage of civilians between the ages of 45 and 64 in the labor force that are employed  
pct_civ_unemp_45_64| number| The percentage of ACS civilians between the ages of 45 and 64 in the labor force that are unemployed  
pct_civ_unemp_45_64_m90| number| Margin of error of the percentage of civilians between the ages of 45 and 64 in the labor force that are unemployed  
pct_pop_disabled| number| The percentage of the ACS population who have one or more disabilities.  
pct_pop_disabled_m90| number| Margin of error of the percentage of the ACS population who have one or more disabilities.  
pct_pop_1yr_over| number| The percentage of the ACS population who are ages 1 year and over at time of interview  
pct_pop_1yr_over_m90| number| Margin of error of the percentage of the ACS population who are ages 1 year and over at time of interview  
pct_diff_hu_1yr_ago| number| The percentage of the ACS population aged 1 year and over that moved from another residence in the U.S. or Puerto Rico within the last year  
pct_diff_hu_1yr_ago_m90| number| Margin of Error of the percentage of the ACS population aged 1 year and over that moved from another residence in the U.S. or Puerto Rico within the last year  
pct_born_us| number| The percentage of the ACS population who are citizens of the United States at birth in the ACS. This includes respondents who said that they were born in the United States, Puerto Rico, a US Island Area (such as Guam), or abroad of American (US citizen) parent or parents.  
pct_born_us_m90| number| Margin of error of the percentage of the population who are US citizens at birth  
pct_born_foreign| number| The percentage of the ACS population who were not a citizen of the United States at birth. This includes respondents who indicated that they were a US citizen by naturalization or not a US citizen.  
pct_born_foreign_m90| number| Margin of error of the percentage of the population who are not US citizens at birth  
pct_us_cit_nat| number| The percentage of the ACS population who are citizens of the United States through naturalization  
pct_us_cit_nat_m90| number| Margin of error of the percentage of the population who are US citizens through naturalization  
pct_non_us_cit| number| The percentage of the ACS population who are not citizens of the United States  
pct_non_us_cit_m90| number| Margin of error of the percentage of the population who are not US citizens  
pct_eng_vw_span| number| The percentage of all ACS occupied housing units where a Spanish or Spanish Creole language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_span_m90| number| Margin of error of the percentage of all ACS occupied housing units where a Spanish or Spanish Creole language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_indoeuro| number| The percentage of all ACS occupied housing units where an Indo-European language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_indoeuro_m90| number| Margin of error of the percentage of all ACS occupied housing units where an Indo-European language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_api| number| The percentage of all ACS occupied housing units where an Asian and Pacific Island language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_api_m90| number| Margin of error of the percentage of all ACS occupied housing units where an Asian and Pacific Island language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_other| number| The percentage of all ACS occupied housing units where a language other than English, Spanish, Indo-Euro, or API was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_other_m90| number| Margin of error of the percentage of all ACS occupied housing units where a language other than English, Spanish, Indo-Euro, or API was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw| number| The percentage of all ACS occupied housing units where no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_m90| number| Margin of error of the percentage of all ACS occupied housing units where no one ages 14 years and over speaks English only or speaks English "very well"  
pct_rel_family_hhd| number| The percentage of all ACS occupied housing units where at least 2 members are related by birth, marriage, or adoption; same-sex couple households with no relatives of the householder present are not included  
pct_rel_family_hhd_m90| number| Margin of error of the percentage of all ACS occupied housing units where at least 2 members are related by birth, marriage, or adoption  
pct_mrdcple_hhd| number| The percentage of all ACS occupied housing units where the householder and his or her spouse are listed as members of the same household; does not include same-sex married couples  
pct_mrdcple_hhd_m90| number| Margin of error of the percentage of all ACS occupied housing units where the householder and his or her spouse are listed as members of the same household  
pct_not_mrdcple_hhd| number| The percentage of all ACS occupied housing units with no spousal relationship present  
pct_not_mrdcple_hhd_m90| number| Margin of error of the percentage of all ACS occupied housing units with no spousal relationship present  
pct_female_no_hb| number| The percentage of all ACS occupied housing units with a female householder and no husband of householder present  
pct_female_no_hb_m90| number| Margin of error of the percentage of all ACS occupied housing units with a female householder and no husband of householder present  
pct_nonfamily_hhd| number| The percentage of all ACS occupied housing units where a householder lives alone or with nonrelatives only; includes same-sex couples where no relatives of the householder are present  
pct_nonfamily_hhd_m90| number| Margin of error of the percentage of all ACS occupied housing units where a householder lives alone or with nonrelatives only  
pct_sngl_prns_hhd| number| The percentage of all ACS occupied housing units where a householder lives alone  
pct_sngl_prns_hhd_m90| number| Margin of error of the percentage of all ACS occupied housing units where a householder lives alone  
pct_hhd_ppl_und_18| number| The percentage of all ACS occupied housing units where one or more people are ages 18 years or under  
pct_hhd_ppl_und_18_m90| number| Margin of error of the percentage of all ACS occupied housing units where one or more people are ages 18 years or under  
avg_tot_prns_in_hhd| number| The average number of persons per ACS occupied housing unit. This was calculated by dividing the total household population in the ACS by the total number of occupied housing units in the ACS.  
avg_tot_prns_in_hhd_m90| number| Margin of error of the average number of persons per ACS occupied housing unit  
pct_rel_under_6| number| The percentage of 2010 ACS family-occupied housing units with a related child under 6 years old; same-sex couple households with no relatives of the householder present are not included in the denominator  
pct_rel_under_6_m90| number| Margin of error of the percentage of 2010 ACS family-occupied housing units with a related child under 6 years old  
pct_hhd_moved_in| number| The percentage of all ACS occupied housing units where the householder moved into the current unit in the year 2010 or later  
pct_hhd_moved_in_m90| number| Margin of error of the percentage of all ACS occupied housing units where the householder moved into the current unit in the year 2010 or later  
pct_pub_asst_inc| number| The percentage of all ACS occupied housing units that receive public assistance income (general assistance and Temporary Assistance to Needy Families)  
pct_pub_asst_inc_m90| number| Margin of error of percentage of all ACS occupied housing units that receive public assistance income  
avg_agg_hh_inc| integer| The average aggregated household income of all ACS occupied housing units.  
avg_agg_hh_inc_m90| integer| Margin of error for the average aggregated household income of all ACS occupied housing units.  
pct_tot_occp_units| number| The percentage of all ACS housing units that are classified as the usual place of residence of the individual or group living in it  
pct_tot_occp_units_m90| number| Margin of error for the percentage of all ACS housing units that are classified as the usual place of residence of the individual or group living in it  
pct_vacant_units| number| The percentage of all ACS housing units where no one is living regularly at the time of interview; units occupied at the time of interview entirely by persons who are staying two months or less and who have a more permanent residence elsewhere are classified as vacant  
pct_vacant_units_m90| number| Margin of error for the percentage of all ACS housing units where no one is living regularly at the time of interview  
pct_renter_occp_hu| number| The percentage of ACS occupied housing units that are not owner occupied, whether they are rented or occupied without payment of rent  
pct_renter_occp_hu_m90| number| Margin of error for the percentage of ACS occupied housing units that are not owner occupied  
pct_owner_occp_hu| number| The percentage of ACS occupied housing units with an owner or co-owner living in it  
pct_owner_occp_hu_m90| number| Margin of error for the ACS occupied housing units with an owner or co-owner living in it  
pct_single_unit| number| The percentage of all ACS housing units that are in a structure that contains only that single unit  
pct_single_unit_m90| number| Margin of error for the percentage of all ACS housing units that are in a structure that contains only that single unit  
pct_mlt_u2_9_strc| number| The percentage of all ACS housing units that are in a structure that contains two to nine housing units  
pct_mlt_u2_9_strc_m90| number| Margin of error for the percentage of all ACS housing units that are in a structure that contains two to nine housing units  
pct_mlt_u10p| number| The percentage of all ACS housing units that are in a structure that contains 10 or more housing units  
pct_mlt_u10p_m90| number| Margin of error for the percentage of all ACS housing units that are in a structure that contains 10 or more housing units  
pct_mobile_homes| number| The percentage of all ACS housing units that are considered mobile homes  
pct_mobile_homes_m90| number| Margin of error for the percentage of all ACS housing units that are considered mobile homes  
pct_crowd_occp_u| number| The percentage of ACS occupied housing units that have more than 1.01 persons per room  
pct_crowd_occp_u_m90| number| Margin of error for the percentage of ACS occupied housing units that have more than 1.01 persons per room  
pct_no_ph_srvc| number| The percentage of ACS occupied housing units that do not have a working telephone and available service  
pct_no_ph_srvc_m90| number| Margin of error for the percentage of ACS occupied housing units that do not have a working telephone and available service  
pct_no_plumb| number| The percentage of all ACS housing units that do not have complete plumbing facilities  
pct_no_plumb_m90| number| Margin of error for the percentage of all ACS housing units that do not have complete plumbing facilities  
pct_recent_built_hu| number| The percentage of all ACS housing units that are in a building that was constructed in 2010 or later  
pct_recent_built_hu_m90| number| Margin of error for all ACS housing units that are in a building that was constructed in 2010 or later  
avg_agg_house_value| integer| Average aggregated value in dollars for ACS occupied housing units.  
avg_agg_house_value_m90| integer| Margin of error for average aggregated value in dollars for ACS occupied housing units.  
  
### tract_communities

Column Name| Data Type| Description  
---|---|---  
geoid| string| Tract Geoid  
city_name| string| Name of the city the tract is in.  
city_code| string| Code for the city the tract is in.  
community_name| string| Community name  
community_cpcode| integer| Community planning code  
community_code| string| Short community Mnemonic code.  
  
### business_sites

Column Name| Data Type| Description  
---|---|---  
id| integer|   
apn| integer|   
bcccode| integer|   
ownnam1| string|   
ownnam2| string|   
ownnam3| string|   
careof| string|   
strnum| integer|   
strfra| string|   
strdir| string|   
strnam| string|   
strtyp| string|   
strsrm| string|   
city| string|   
state| string|   
contry| string|   
zipcd1| integer|   
zipcd2| integer|   
loccod| string|   
locnum| integer|   
locfra| string|   
locdir| string|   
locnam| string|   
loctyp| string|   
locsrm| string|   
loccit| string|   
bustype| string|   
point_x| number|   
point_y| number|   
geometry| string|   
  
### business_tract_counts

Column Name| Data Type| Description  
---|---|---  
geoid| string|   
bcccode| integer|   
bustype| string|   
count| integer|   
  
### cen10_pdb

Column Name| Data Type| Description  
---|---|---  
geoid| string|   
flag| number|   
land_area| number|   
aian_land| integer|   
urbanized_area_pop| integer|   
urban_cluster_pop| integer|   
rural_pop| integer|   
tot_population| integer|   
males| integer|   
females| integer|   
pop_under_5| integer|   
pop_5_17| integer|   
pop_18_24| integer|   
pop_25_44| integer|   
pop_45_64| integer|   
pop_65plus| integer|   
tot_gq| integer|   
inst_gq| integer|   
non_inst_gq| integer|   
hispanic| integer|   
nh_white_alone| integer|   
nh_blk_alone| integer|   
nh_aian_alone| integer|   
nh_asian_alone| integer|   
nh_nhopi_alone| integer|   
nh_sor_alone| integer|   
rel_family_hhd| integer|   
mrdcple_fmly_hhd| integer|   
not_mrdcple_hhd| integer|   
female_no_hb| integer|   
nonfamily_hhd| integer|   
sngl_prns_hhd| integer|   
hhd_ppl_und_18| integer|   
tot_prns_in_hhd| integer|   
rel_child_under_6| integer|   
tot_housing_units| integer|   
tot_occp_units| integer|   
tot_vacant_units| integer|   
renter_occp_hu| integer|   
owner_occp_hu| integer|   
mailback_area_count| number|   
tea_mail_out_mail_back| number|   
tea_update_leave| number|   
census_mail_returns| number|   
vacants| number|   
deletes| number|   
census_uaa| number|   
valid_mailback_count| number|   
frst_frms| number|   
rplcmnt_frms| number|   
bilq_mailout_count| number|   
bilq_frms| number|   
mail_return_rate| number|   
low_response_score| number|   
pct_urbanized_area_pop| number|   
pct_urban_cluster_pop| number|   
pct_rural_pop| number|   
pct_males| number|   
pct_females| number|   
pct_pop_under_5| number|   
pct_pop_5_17| number|   
pct_pop_18_24| number|   
pct_pop_25_44| number|   
pct_pop_45_64| number|   
pct_pop_65plus| number|   
pct_tot_gq| number|   
pct_inst_gq| number|   
pct_non_inst_gq| number|   
pct_hispanic| number|   
pct_nh_white_alone| number|   
pct_nh_blk_alone| number|   
pct_nh_aian_alone| number|   
pct_nh_asian_alone| number|   
pct_nh_nhopi_alone| number|   
pct_nh_sor_alone| number|   
pct_rel_family_hhd| number|   
pct_mrdcple_hhd| number|   
pct_not_mrdcple_hhd| number|   
pct_female_no_hb| number|   
pct_nonfamily_hhd| number|   
pct_sngl_prns_hhd| number|   
pct_hhd_ppl_und_18| number|   
avg_tot_prns_in_hhd| number|   
pct_rel_under_6| number|   
pct_tot_occp_units| number|   
pct_vacant_units| number|   
pct_renter_occp_hu| number|   
pct_owner_occp_hu| number|   
pct_tea_mailoutmailback| number|   
pct_tea_update_leave| number|   
pct_census_mail_returns| number|   
pct_vacants| number|   
pct_deletes| number|   
pct_census_uaa| number|   
pct_mailback_count| number|   
pct_frst_frms| number|   
pct_rplcmnt_frms| number|   
pct_bilq_mailout_count| number|   
  
## References

Urls used in the creation of this data package.

  * **index:sandiegodata.org-planning-tracts#planning_db_sd**. San Diego county planning database tracts


Last Modified 2019-01-03T22:57:07
