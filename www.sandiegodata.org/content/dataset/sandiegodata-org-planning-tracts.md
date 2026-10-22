---
title: "County Planning Database"
date: 2019-06-12T20:09:48+00:00
draft: false
categories: ["build_environment", "Dataset", "planning", "planning-collection"]
tags: ["build_environment", "planning", "planning-collection", "planning-project", "sandiegodata.org"]
author: "metapack"
description: "A collection of data for demographics and housing from the Census planning"
---

_A collection of data for demographics and housing from the Census planning database. Files are broken into counties, for San Diego and Los Angeles_

`sandiegodata.org-planning-tracts-9`


## Resources

  * **[planning_db_sd](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-tracts-9/data/planning_db_sd.csv>)**. San Diego county planning database tracts
  * **[planning_db_la](<https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-tracts-9/data/planning_db_la.csv>)**. Los Angeles county planning database tracts


## Documentation

The Planing Database is a Census product that combines a range of data from the American Community Survey and 2010 Decenial Census into a single file, with one row per census tract. This version of the file includes only tracts in San Diego County. The file is linked to ACS format geoids to identify tracts, so it can be easily linked to other tracts data. This data package includes links to two such files, one for San Diego communities, and one for tract geographics.

The planning database has about 450 columns. For full definitions of the columns, refer to the [upstream documentation for the source file](<https://www.census.gov/research/data/planning_database/2018/docs/2018_Tract_PDB_Documentation_V4.pdf>). In general, the column names in the documentation must be lowercased for use with the file in this data package. 

## Use patterns

In Python, use metapack to open the data package. 
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-tracts-2.zip')
```

To display a simple map, link in the tract boundaries from the communities dataset and use the Geopandas .plot() function. The `column` argument names the column to use for coloring regions. Note that the column name is copied from the documentation with mixed case, then lowercased to index the dataset.
```
tracts = pkg.reference('communities').geoframe().set_index('geoid').fillna('')
df = tracts.join(cpdb)

fig, ax = plt.subplots(1, figsize=(15,10))
df.plot(ax=ax, column='pct_MLT_U10p_ACS_12_16'.lower())
```

After linking in the communities, you can also use the [community id columns](</dataset/>) to group by city or community: 
```
seniors = dfg.df.groupby('city_name').pop_65plus_acs_12_16.sum()
```

# Versions

  1. First Release
  2. Clean more currency columns
  3. Extended schema metadata. 
  4. Added 'group' to metadata.


### Documentation Links

  * Tract PDB Documentation. <https://www.census.gov/research/data/planning_database/2018/docs/2018_Tract_PDB_Documentation_V4.pdf>Primary documentation and data dictionary
  * Home page. <https://www.census.gov/research/data/planning_database/>


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-tracts-9.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-tracts-9.csv>
  * **source** <https://github.com/sandiegodata/planning-database.git>


### Accessing Packages in Metapack
```
import metapack as mp
# ZIP Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-tracts-9.zip')
# CSV Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-planning-tracts-9.csv') 

resource = pkg.resource('resource_name') # Get a resource
df = resource.dataframe() # Create a pandas Dataframe
gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
```

## Data Dictionary

planning_db   


### planning_db

Column Name| Data Type| Description  
---|---|---  
geoid| string| Subdivision of a County or statistically equivalent entity (0 to over 25,000 people per Tract with an average size of 4,200)  
flag| string| If a tract contains only uninhabitable land, this variable is filled. Otherwise, this variable is blank.  
land_area| number| Land area of geographical entity in square miles  
aian_land| integer| The number of block groups in this tract that are located on any part of an American Indian, Alaska Native, or Native Hawaiian area  
urbanized_area_pop_cen_2010| integer| Population living in a densely settled area containing 50,000 or more people  
urban_cluster_pop_cen_2010| integer| Population living in a densely settled area containing 2,500 to 49,999 people  
rural_pop_cen_2010| integer| Population living outside of an Urbanized Area or Urban Cluster  
tot_population_cen_2010| integer| U.S. resident population includes everyone whose usual place of residence was in the tract at the time of the 2010 Census  
tot_population_acs_12_16| integer| U.S. resident population includes everyone who meets the ACS residence rules in the tract at the time of the ACS interview  
tot_population_acsmoe_12_16| integer| Margin of Error for Total Population  
males_cen_2010| integer| Number of Males in 2010 Census Total Population  
males_acs_12_16| integer| Number of Males in ACS Total Population  
males_acsmoe_12_16| integer| Margin of Error for Number of Males  
females_cen_2010| integer| Number of Females in 2010 Census Total Population  
females_acs_12_16| integer| Number of Females in ACS Total Population  
females_acsmoe_12_16| integer| Margin of Error for Number of Females  
pop_under_5_cen_2010| integer| Number of persons under age 5 as of April 1, 2010  
pop_under_5_acs_12_16| integer| Number of persons under age 5 at the time of the ACS interview  
pop_under_5_acsmoe_12_16| integer| Margin of Error for Persons less than age 5  
pop_5_17_cen_2010| integer| Number of persons ages 5 to 17 as of April 1, 2010  
pop_5_17_acs_12_16| integer| Number of persons ages 5 to 17 at the time of the ACS interview  
pop_5_17_acsmoe_12_16| integer| Margin of Error for Persons ages 5 to 17  
pop_18_24_cen_2010| integer| Number of persons ages 18 to 24 as of April 1, 2010  
pop_18_24_acs_12_16| integer| Number of persons ages 18 to 24 at the time of the ACS interview  
pop_18_24_acsmoe_12_16| integer| Margin of Error for Persons ages 18 to 24  
pop_25_44_cen_2010| integer| Number of persons ages 25 to 44 as of April 1, 2010  
pop_25_44_acs_12_16| integer| Number of persons ages 25 to 44 at the time of the ACS interview  
pop_25_44_acsmoe_12_16| integer| Margin of Error for Persons ages 25 to 44  
pop_45_64_cen_2010| integer| Number of persons ages 45 to 64 as of April 1, 2010  
pop_45_64_acs_12_16| integer| Number of persons ages 45 to 64 at the time of the ACS interview  
pop_45_64_acsmoe_12_16| integer| Margin of Error for Persons ages 45 to 64  
pop_65plus_cen_2010| integer| Number of persons age 65 and over as of April 1, 2010  
pop_65plus_acs_12_16| integer| Number of persons age 65 and over at the time of the ACS interview  
pop_65plus_acsmoe_12_16| integer| Margin of Error for Persons ages 65 and over  
tot_gq_cen_2010| integer| Number of people living or staying in a group living arrangement owned by an entity providing housing to residents, who are usually unrelated, as of April 1, 2010  
inst_gq_cen_2010| integer| Number of those in group quarters primarily ineligible, unable, or unlikely to participate in labor force while residents. Institutional group quarters include correctional facilities for adults, juvenile facilities, nursing facilities, and other institutional facilities.  
non_inst_gq_cen_2010| integer| Number of those in group quarters primarily eligible, able, or likely to participate in labor force while residents. Noninstitutional group quarters include college/university student housing, military quarters, and other noninstitutional facilities.  
hispanic_cen_2010| integer| Number of people who identify as "Mexican", "Puerto Rican", "Cuban", or "another Hispanic, Latino, or Spanish origin" in the 2010 Census population  
hispanic_acs_12_16| integer| Number of people who identify as "Mexican", "Puerto Rican", "Cuban", or "another Hispanic, Latino, or Spanish origin" in the ACS population  
hispanic_acsmoe_12_16| integer| Margin of Error of Hispanic Origin Population  
nh_white_alone_cen_2010| integer| Number of people who indicate no Hispanic origin and their only race as "White" or report entries such as Irish, German, Italian, Lebanese, Arab, Moroccan, or Caucasian in the 2010 Census population  
nh_white_alone_acs_12_16| integer| Number of people who indicate no Hispanic origin and their only race as "White" or report entries such as Irish, German, Italian, Lebanese, Arab, Moroccan, or Caucasian in the ACS population  
nh_white_alone_acsmoe_12_16| integer| Margin of Error of Non-Hispanic White only  
nh_blk_alone_cen_2010| integer| Number of people who indicate no Hispanic origin and their only race as "Black, African Am., or Negro" or report entries such as African American, Kenyan, Nigerian, or Haitian in the 2010 Census population  
nh_blk_alone_acs_12_16| integer| Number of people who indicate no Hispanic origin and their only race as "Black, African Am., or Negro" or report entries such as African American, Kenyan, Nigerian, or Haitian in the ACS population  
nh_blk_alone_acsmoe_12_16| integer| Margin of Error of Non-Hispanic Black or African-American only  
nh_aian_alone_cen_2010| integer| Number of people who indicate no Hispanic origin and their only race as "American Indian or Alaska Native" or report entries such as Navajo, Blackfeet, Inupiat, Yup'ik, or Central/South American Indian groups in the 2010 Census population  
nh_aian_alone_acs_12_16| integer| Number of people who indicate no Hispanic origin and their only race as "American Indian or Alaska Native" or report entries such as Navajo, Blackfeet, Inupiat, Yup'ik, or Central/South American Indian groups in the ACS population  
nh_aian_alone_acsmoe_12_16| integer| Margin of Error of Non-Hispanic American Indian and Alaska Native only  
nh_asian_alone_cen_2010| integer| Number of people who indicate no Hispanic origin and their only race as "Asian Indian", "Chinese", "Filipino", "Korean", "Japanese", "Vietnamese", or "Other Asian" in the 2010 Census population  
nh_asian_alone_acs_12_16| integer| Number of people who indicate no Hispanic origin and their only race as "Asian Indian", "Chinese", "Filipino", "Korean", "Japanese", "Vietnamese", or "Other Asian" in the ACS population  
nh_asian_alone_acsmoe_12_16| integer| Margin of Error of Non-Hispanic Asian only  
nh_nhopi_alone_cen_2010| integer| Number of people who indicate no Hispanic origin and their only race as "Native Hawaiian", "Guamanian or Chamorro", "Samoan", or "Other Pacific Islander" in the 2010 Census population  
nh_nhopi_alone_acs_12_16| integer| Number of people who indicate no Hispanic origin and their only race as "Native Hawaiian", "Guamanian or Chamorro", "Samoan", or "Other Pacific Islander" in the ACS population  
nh_nhopi_alone_acsmoe_12_16| integer| Margin of Error of Non-Hispanic Native Hawaiian and Other Pacific Islander only  
nh_sor_alone_cen_2010| integer| Number of people who indicate no Hispanic origin and their race as other than "White", "Hispanic", "Black or African American", "American Indian or Alaska Native", "Asian", and "Native Hawaiian or Other Pacific Islander" in the 2010 Census population  
nh_sor_alone_acs_12_16| integer| Number of people who indicate no Hispanic origin and their race as other than "White", "Hispanic", "Black or African American", "American Indian or Alaska Native", "Asian", and "Native Hawaiian or Other Pacific Islander" in the ACS population  
nh_sor_alone_acsmoe_12_16| integer| Margin of Error of Non-Hispanic Some other Race only  
pop_5yrs_over_acs_12_16| integer| Number of people ages 5 years and over at time of interview in the ACS population  
pop_5yrs_over_acsmoe_12_16| integer| Margin of Error of Population 5 years and over  
othr_lang_acs_12_16| integer| Number of people ages 5 years and over at the time of interview that speak a language other than English at home in the ACS population, regardless of ability to speak English  
othr_lang_acsmoe_12_16| integer| Margin of Error of Population 5 years and over that speak a language other than English at home, regardless of ability to speak English  
age5p_only_english_acs_12_16| integer| Number of people ages 5 years and over at the time of the interview that speak only English at home in the ACS  
age5p_only_english_acsmoe_12_16| integer| Margin of Error of Population 5 years and over that speak only English at home  
age5p_spanish_acs_12_16| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Spanish or Spanish Creole at home in the ACS. Examples include Ladino and Pachuco.  
age5p_spanish_acsmoe_12_16| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Spanish or Spanish Creole at home  
age5p_french_acs_12_16| integer| Number of people ages 5 years and over who speak English less than "very well" and speak French at home in the ACS. Examples include Cajun and Patois.  
age5p_french_acsmoe_12_16| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak French at home  
age5p_german_acs_12_16| integer| Number of people ages 5 years and over who speak English less than "very well" and speak German at home in the ACS. Examples include Luxembourgian.  
age5p_german_acsmoe_12_16| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak German at home  
age5p_russian_acs_12_16| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Russian at home in the ACS  
age5p_russian_acsmoe_12_16| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Russian at home  
age5p_otheuro_acs_12_16| integer| Number of people ages 5 years and over who speak English less than "very well" and speak some other Indo-European language at home in the ACS. Examples include Albanian, Gaelic, Lithuanian, and Romanian.  
age5p_otheuro_acsmoe_12_16| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak some other Indo-European language at home  
age5p_korean_acs_12_16| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Korean at home in the ACS  
age5p_korean_acsmoe_12_16| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Korean at home  
age5p_chinese_acs_12_16| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Chinese at home in the ACS. Examples include Cantonese, Formosan, and Mandarin.  
age5p_chinese_acsmoe_12_16| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Chinese at home  
age5p_vietnamese_acs_12_16| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Vietnamese at home in the ACS  
age5p_vietnamese_acsmoe_12_16| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Vietnamese at home  
age5p_tagalog_acs_12_16| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Tagalog at home in the ACS  
age5p_tagalog_acsmoe_12_16| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Tagalog at home  
age5p_othasian_acs_12_16| integer| Number of people ages 5 years and over who speak English less than "very well" and speak some other Asian language at home in the ACS. Examples include Turkish or Dravidian languages such as Malayalam, Telugu, and Tamil.  
age5p_othasian_acsmoe_12_16| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak some other Asian language at home  
age5p_arabic_acs_12_16| integer| Number of people ages 5 years and over who speak English less than "very well" and speak Arabic at home in the ACS  
age5p_arabic_acsmoe_12_16| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak Arabic at home  
age5p_othunsp_acs_12_16| integer| Number of people ages 5 years and over who speak English less than "very well" and speak some other or unspecified language at home in the ACS. Examples include Syriac, Finnish, other languages of the Americas, or no reported language.  
age5p_othunsp_acsmoe_12_16| integer| Margin of Error of Number of people 5 years and over who speak English less than "very well" and speak some other or unspecified language at home  
pop_25yrs_over_acs_12_16| integer| Number of people ages 25 years and over at time of interview in the ACS population  
pop_25yrs_over_acsmoe_12_16| integer| Margin of Error of Number of people 25 years old and over  
not_hs_grad_acs_12_16| integer| Number of people ages 25 years and over at time of interview who are not high school graduates and have not received a diploma or the equivalent in the ACS population  
not_hs_grad_acsmoe_12_16| integer| Margin of Error of Number of people 25 years old and over who are not high school graduates  
college_acs_12_16| integer| Number of people ages 25 years and over at the time of interview with a college degree or higher in the ACS population  
college_acsmoe_12_16| integer| Margin of Error of Persons 25 and over with a college degree or higher  
pov_univ_acs_12_16| integer| Number of people excluding institutionalized people, people in military group quarters, people in college dormitories, and unrelated individuals under 15 years old in the ACS  
pov_univ_acsmoe_12_16| integer| Margin of Error for Population for whom poverty level is determined  
prs_blw_pov_lev_acs_12_16| integer| Number of people classified as below the poverty level given their total family or household income within the last year, family size, and family composition in the ACS population  
prs_blw_pov_lev_acsmoe_12_16| integer| Margin of Error of Number of people classified as below the poverty level  
one_health_ins_acs_12_16| integer| Number of people who have one type of health insurance coverage, including public or private insurance, in the ACS population  
one_health_ins_acsmoe_12_16| integer| Margin of Error of Number of people who have one type of health insurance coverage  
two_plus_health_ins_acs_12_16| integer| Number of people who have two or more types of health insurance at the same time, in the ACS population  
two_plus_health_ins_acsmoe_12_16| integer| Margin of Error of Number of people who have two or more types of health insurance coverage  
no_health_ins_acs_12_16| integer| Number of people who have no health insurance coverage, public or private, in the ACS population  
no_health_ins_acsmoe_12_16| integer| Margin of Error of Number of people who have no health insurance coverage  
civ_labor_16plus_acs_12_16| integer| Number of civilians ages 16 years and over at the time of the interview that are in the labor force in the ACS  
civ_labor_16plus_acsmoe_12_16| integer| Margin of Error of Number of civilians 16 and over that are in the labor force  
civ_emp_16plus_acs_12_16| integer| Number of civilians ages 16 years and over at the time of the interview that are employed in the ACS  
civ_emp_16plus_acsmoe_12_16| integer| Margin of Error of Number of civilians 16 and over that are employed  
civ_unemp_16plus_acs_12_16| integer| Number of civilians ages 16 years and over at the time of the interview that are unemployed in the ACS  
civ_unemp_16plus_acsmoe_12_16| integer| Margin of Error of Number of civilians 16 and over that are unemployed  
civ_labor_16_24_acs_12_16| integer| Number of civilians between the ages of 16 and 24 at the time of the interview who are in the labor force in the ACS  
civ_labor_16_24_acsmoe_12_16| integer| Margin of error of Number of civilians between the ages of 16 to 24 who are in the labor force  
civ_emp_16_24_acs_12_16| integer| Number of civilians between the ages of 16 and 24 at the time of the interview who are employed in the ACS  
civ_emp_16_24_acsmoe_12_16| integer| Margin of Error of Number of civilians aged 16 to 24 who are employed  
civ_unemp_16_24_acs_12_16| integer| Number of civilians between the ages of 16 and 24 at the time of the interview who are unemployed in the ACS  
civ_unemp_16_24_acsmoe_12_16| integer| Margin of Error of Number of civilians aged 16 to 24 who are unemployed  
civ_labor_25_44_acs_12_16| integer| Number of civilians between the ages of 25 and 44 at the time of the interview who are in the labor force in the ACS  
civ_labor_25_44_acsmoe_12_16| integer| Margin of Error of Number of civilians aged 25 to 44 who are in the labor force  
civ_emp_25_44_acs_12_16| integer| Number of civilians between the ages of 25 and 44 at the time of the interview who are employed in the ACS  
civ_emp_25_44_acsmoe_12_16| integer| Margin of Error of Number of civilians aged 25 to 44 who are employed  
civ_unemp_25_44_acs_12_16| integer| Number of civilians between the ages of 25 and 44 at the time of the interview who are unemployed in the ACS  
civ_unemp_25_44_acsmoe_12_16| integer| Margin of Error of Number of civilians aged 25 to 44 who are unemployed  
civ_labor_45_64_acs_12_16| integer| Number of civilians between the ages of 45 and 64 at the time of the interview who are in the labor force in the ACS  
civ_labor_45_64_acsmoe_12_16| integer| Margin of Error of Number of civilians aged 45 to 64 who are in the labor force  
civ_emp_45_64_acs_12_16| integer| Number of civilians between the ages of 45 and 64 at the time of the interview who are employed in the ACS  
civ_emp_45_64_acsmoe_12_16| integer| Margin of Error of Number of civilians aged 45 to 64 who are employed  
civ_unemp_45_64_acs_12_16| integer| Number of civilians between the ages of 45 and 64 at the time of the interview who are unemployed in the ACS  
civ_unemp_45_64_acsmoe_12_16| integer| Margin of Error of Number of civilians aged 45 to 64 who are unemployed  
civ_noninst_pop_acs_12_16| integer| Total number of noninstitutionalized civilians in the population  
civ_noninst_pop_acsmoe_12_16| integer| Margin of Error of total number of noninstitutionalized civilians in the population  
pop_disabled_acs_12_16| integer| Number of persons who have one or more disabilities in the ACS population  
pop_disabled_acsmoe_12_16| integer| Margin of Error of Number of persons who have one or more disabilities in the ACS population  
pop_1yr_over_acs_12_16| integer| Number of people ages 1 year and over at time of interview in the ACS population  
pop_1yr_over_acsmoe_12_16| integer| Margin of Error for Number of people 1 year old and over  
diff_hu_1yr_ago_acs_12_16| integer| Number of people who moved from another residence in the U.S. or Puerto Rico within the last year in the ACS population  
diff_hu_1yr_ago_acsmoe_12_16| integer| Margin of Error of Different house one year ago  
born_us_acs_12_16| integer| Number of people who are citizens of the United States at birth in the ACS. This includes respondents who said that they were born in the United States, Puerto Rico, a US Island Area (such as Guam), or abroad of American (US citizen) parent or parents.  
born_us_acsmoe_12_16| integer| Margin of Error of Number of people who are US citizens at birth  
born_foreign_acs_12_16| integer| Number of people who were not a citizen of the United States at birth. This includes respondents who indicated that they were a US citizen by naturalization or not a US citizen.  
born_foreign_acsmoe_12_16| integer| Margin of Error of Number of people who were not US citizens at birth  
us_cit_nat_acs_12_16| integer| Number of people who are citizens of the United States through naturalization in the ACS  
us_cit_nat_acsmoe_12_16| integer| Margin of Error of Number of people who are US citizens through naturalization  
non_us_cit_acs_12_16| integer| Number of people who are not citizens of the United States in the ACS  
non_us_cit_acsmoe_12_16| integer| Margin of Error of Number of people who are not US citizens  
eng_vw_span_acs_12_16| integer| Number of ACS households where a Spanish or Spanish Creole language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
eng_vw_span_acsmoe_12_16| integer| Margin of Error of Spanish-No one 14 and over speaks English only or speaks English "very well"  
eng_vw_indo_euro_acs_12_16| integer| Number of ACS households where an Indo-European language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
eng_vw_indo_euro_acsmoe_12_16| integer| Margin of Error of INDO EURO -No one 14 and over speaks English only or speaks English "very well"  
eng_vw_api_acs_12_16| integer| Number of ACS households where an Asian and Pacific Island language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
eng_vw_api_acsmoe_12_16| integer| Margin of Error of API-No one 14 and over speaks English only or speaks English "very well"  
eng_vw_other_acs_12_16| integer| Number of ACS households where a language other than English, Spanish, Indo-Euro, or API was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
eng_vw_other_acsmoe_12_16| integer| Margin of Error of OTH-No one 14 and over speaks English only or speaks English "very well"  
eng_vw_acs_12_16| integer| Number of ACS households where no one ages 14 years and over speaks English only or speaks English "very well"  
eng_vw_acsmoe_12_16| integer| Margin of Error of No one 14 and over speaks English only or speaks English "very well"  
rel_family_hhd_cen_2010| integer| Number of 2010 Census households where at least 2 members are related by birth, marriage, or adoption; same-sex couple households with no relatives of the householder present are not included  
rel_family_hhd_acs_12_16| integer| Number of ACS households where at least 2 members are related by birth, marriage, or adoption; same-sex couple households with no relatives of the householder present are not included  
rel_family_hhd_acsmoe_12_16| integer| Margin of Error of Related family households  
mrdcple_fmly_hhd_cen_2010| integer| Number of 2010 Census households in which the householder and his or her spouse are listed as members of the same household; does not include same-sex married couples  
mrdcple_fmly_hhd_acs_12_16| integer| Number of ACS households in which the householder and his or her spouse are listed as members of the same household; does not include same-sex married couples  
mrdcple_fmly_hhd_acsmoe_12_16| integer| Margin of Error of Married-Couple Family  
not_mrdcple_hhd_cen_2010| integer| Number of 2010 Census households with no spousal relationship present  
not_mrdcple_hhd_acs_12_16| integer| Number of ACS households with no spousal relationship present  
not_mrdcple_hhd_acsmoe_12_16| integer| Margin of Error of Number of ACS households with no spousal relationship present  
female_no_hb_cen_2010| integer| Number of 2010 Census households with a female householder and no husband of householder present  
female_no_hb_acs_12_16| integer| Number of ACS households with a female householder and no husband of householder present  
female_no_hb_acsmoe_12_16| integer| Margin of Error of Female householder, no husband present  
nonfamily_hhd_cen_2010| integer| Number of 2010 Census households where a householder lives alone or with nonrelatives only; includes same-sex couples where no relatives of the householder are present  
nonfamily_hhd_acs_12_16| integer| Number of ACS households where a householder lives alone or with nonrelatives only; includes same-sex couples where no relatives of the householder are present  
nonfamily_hhd_acsmoe_12_16| integer| Margin of Error of Nonfamily household: Unrelated households  
sngl_prns_hhd_cen_2010| integer| Number of 2010 Census households where a householder lives alone  
sngl_prns_hhd_acs_12_16| integer| Number of ACS households where a householder lives alone  
sngl_prns_hhd_acsmoe_12_16| integer| Margin of Error of Single person householder living alone  
hhd_ppl_und_18_cen_2010| integer| Number of 2010 Census households where one or more people are ages 18 years or under  
hhd_ppl_und_18_acs_12_16| integer| Number of ACS households where one or more people are ages 18 years or under  
hhd_ppl_und_18_acsmoe_12_16| integer| Margin of Error of Households with one or more people under 18 years  
tot_prns_in_hhd_cen_2010| integer| All persons (household population) in 2010 Census occupied housing unit. This is the numerator to calculate the average household size.  
tot_prns_in_hhd_acs_12_16| integer| All persons (household population) in ACS occupied housing unit. This is the numerator to calculate the average household size.  
tot_prns_in_hhd_acsmoe_12_16| integer| Margin of Error of Total Persons in households  
rel_child_under_6_cen_2010| integer| Number of 2010 Census families with related children under 6 years old  
rel_child_under_6_acs_12_16| integer| Number of ACS families with related children under 6 years old  
rel_child_under_6_acsmoe_12_16| integer| Margin of Error of Number of families with related children under 6 years old  
hhd_moved_in_acs_12_16| integer| Number of ACS households where the householder moved into the current unit in the year 2010 or later  
hhd_moved_in_acsmoe_12_16| integer| Margin of Error of Number of households where the householder moved into the current unit in the year 2010 or later  
pub_asst_inc_acs_12_16| integer| Number of ACS households that receive public assistance income (general assistance and Temporary Assistance to Needy Families)  
pub_asst_inc_acsmoe_12_16| integer| Margin of Error of With Public Assistance Income  
med_hhd_inc_acs_12_16| integer| Median ACS household income for the tract  
med_hhd_inc_acsmoe_12_16| integer| Margin of Error of Med household income for the tract  
aggregate_hh_inc_acs_12_16| integer| Sum of all incomes in the household  
aggregate_hh_inc_acsmoe_12_16| integer| Margin of Error for Aggregate household income  
tot_housing_units_cen_2010| integer| Number of 2010 Census living quarters in which the occupant(s) live separately from any other individuals in the building and have direct access  
tot_housing_units_acs_12_16| integer| Number of ACS living quarters in which the occupant(s) live separately from any other individuals in the building and have direct access  
tot_housing_units_acsmoe_12_16| integer| Margin of Error for Total Housing Units  
tot_occp_units_cen_2010| integer| Number of 2010 Census housing units classified as usual place of residence of the individual or group living in it  
tot_occp_units_acs_12_16| integer| Number of ACS housing units classified as usual place of residence of the individual or group living in it  
tot_occp_units_acsmoe_12_16| integer| Margin of Error for Total Occupied Housing Units  
tot_vacant_units_cen_2010| integer| Number of 2010 Census housing units with no regular occupants on Census Day; housing units with its usual occupants temporarily away (such as on vacation, a business trip, or in the hospital) are not considered vacant, but housing units temporarily occupied on Census Day by people who have a usual residence elsewhere are considered vacant  
tot_vacant_units_acs_12_16| integer| Number of ACS housing units where no one is living regularly at the time of interview; units occupied at the time of interview entirely by persons who are staying two months or less and who have a more permanent residence elsewhere are classified as vacant  
tot_vacant_units_acsmoe_12_16| integer| Margin of Error for Total vacant housing units  
renter_occp_hu_cen_2010| integer| Number of 2010 Census occupied housing units that are not owner occupied, whether they are rented or occupied without payment of rent  
renter_occp_hu_acs_12_16| integer| Number of ACS occupied housing units that are not owner occupied, whether they are rented or occupied without payment of rent  
renter_occp_hu_acsmoe_12_16| integer| Margin of Error for Number of renter occupied units  
owner_occp_hu_cen_2010| integer| Number of 2010 Census housing units where owner or co-owner lives in it  
owner_occp_hu_acs_12_16| integer| Number of ACS housing units where owner or co-owner lives in it  
owner_occp_hu_acsmoe_12_16| integer| Margin of Error for Number of owner occuped units  
single_unit_acs_12_16| integer| Number of ACS housing units in which the structure contains only that single unit  
single_unit_acsmoe_12_16| integer| Margin of Error for Number of units in structures containing only 1 housing unit  
mlt_u2_9_strc_acs_12_16| integer| Number of ACS housing units in which the structure contains two or more housing units  
mlt_u2_9_strc_acsmoe_12_16| integer| Margin of Error for Number of units in structures containing two or more housing units  
mlt_u10p_acs_12_16| integer| Number of ACS housing units in which the structure contains 10 or more housing units  
mlt_u10p_acsmoe_12_16| integer| Margin of Error for Number of units in structures containing 10 or more housing units  
mobile_homes_acs_12_16| integer| Number of ACS housing units that are considered mobile homes  
mobile_homes_acsmoe_12_16| integer| Margin of Error for Mobile Homes  
crowd_occp_u_acs_12_16| integer| Number of ACS occupied housing units with more than 1.01 persons per room  
crowd_occp_u_acsmoe_12_16| integer| Margin of Error for Occupied units with more than 1.01 persons per room  
occp_u_no_ph_srvc_acs_12_16| integer| Number of ACS housing units without a working telephone and available service  
occp_u_no_ph_srvc_acsmoe_12_16| integer| Margin of Error for Number of units without a telephone  
no_plumb_acs_12_16| integer| Number of ACS housing units lacking complete plumbing facilities  
no_plumb_acsmoe_12_16| integer| Margin of Error for housing units lacking complete plumbing facilities  
recent_built_hu_acs_12_16| integer| Number of both occupied and vacant ACS housing units whose building was constructed in 2010 or later  
recent_built_hu_acsmoe_12_16| integer| Margin of Error for HUs built 2010 or later  
med_house_value_acs_12_16| integer| Median of ACS respondents' house value estimates for the tract  
med_house_value_acsmoe_12_16| integer| Margin of Error for Med House value for the tract  
aggr_house_value_acs_12_16| integer| Sum of all value estimates for owner-occupied ACS housing units in an area  
aggr_house_value_acsmoe_12_16| integer| Margin of Error for Aggregate value in dollars  
mailback_area_count_cen_2010| integer| Total number of addresses at the start of 2010 Census operations where a Census form was expected to be delivered for mail return to Census. These include addresses in Mailout/Mailback areas (street address available for postal delivery) and addresses in Update/Leave enumeration areas (areas without mailboxes for individual address units). Note: Some of the addresses included in this variable's count were removed from the 2010 Census Universe as a result of actions in subsequent Census operations. For example, an address may have been deleted because it was determined to not correspond to a valid housing unit, or an address may have been added through the BeCounted program. Therefore, this variable represents the universe of addresses at the start of the 2010 Census, and may not be equal to the number of addresses in the final census count.  
tea_mail_out_mail_back_cen_2010| integer| Number of addresses in a Mailout/Mailback type of enumeration area in the 2010 Census. These are addresses that received a census form in the mail and occupants were instructed to complete and mail it back.  
tea_update_leave_cen_2010| string| Number of addresses in an Update/Leave type of enumeration area in the 2010 Census. These are addresses where a census form was hand-delivered and occupants were instructed to complete and mail it back.  
census_mail_returns_cen_2010| integer| Number of completed 2010 Census mail forms received from addresses in a mailback type of enumeration area (Mailout/Mailback and Update/Leave areas)  
vacants_cen_2010| integer| Number of addresses in a 2010 Census mailback area that were confirmed as vacant housing units (Mailout/Mailback and Update/Leave areas)  
deletes_cen_2010| integer| Number of addresses in a 2010 Census mailback area deleted because it was determined to not correspond to a valid housing unit (Mailout/Mailback and Update/Leave areas)  
census_uaa_cen_2010| integer| Number of addresses in a 2010 Census Mailout/Mailback area where the initial mail form was returned to the Census with the postal code "Undeliverable as Addressed"  
valid_mailback_count_cen_2010| integer| Total number of addresses at the start of 2010 Census operations where a Census form was expected to be delivered for mail return to Census minus the number of vacant addresses, the number of deleted addresses, and the number of addresses where the initial mail form was returned to the Census with the postal code "Undeliverable as Addressed." Denominator for the mail return rate.  
frst_frms_cen_2010| integer| Number of addresses in a 2010 Census Mailout/Mailback area where the first form mailed was completed and returned  
rplcmnt_frms_cen_2010| integer| Number of addresses in a 2010 Census Mailout/Mailback area where the replacement form was completed and returned  
bilq_mailout_count_cen_2010| string| Number of addresses that received the 2010 Census English/Spanish bilingual Mailout/Mailback form  
bilq_frms_cen_2010| string| Number of addresses that completed and returned the 2010 Census English/Spanish bilingual Mailout/Mailback form  
mail_return_rate_cen_2010| number| The number of mail returns received out of the total number of valid occupied housing units (HUs) in the Mailout/Mailback universe which excludes deleted, vacant, or units identified as undeliverable as addressed. Therefore, variable 294 can be less than variable 287 because of these exclusions. A small number of tracts contain only HUs that do not meet the requirement to be considered a valid, occupied HU. This variable will have a missing value for these tracts.  
low_response_score| number| A score predicting that a block group will produce a low mail return rate. This score is negatively associated with Mail Return Rate CEN 2010.  
pct_urbanized_area_pop_cen_2010| number| The percentage of the 2010 Census total population that lives in a densely settled area containing 50,000 or more people  
pct_urban_cluster_pop_cen_2010| integer| The percentage of the 2010 Census total population that lives in a densely settled area containing 2,500 to 49,999 people  
pct_rural_pop_cen_2010| number| The percentage of the 2010 Census total population that lives outside of an Urbanized Area or Urban Cluster  
pct_males_cen_2010| number| The percentage of the 2010 Census total population that is male  
pct_males_acs_12_16| number| The percentage of the ACS population that is male  
pct_males_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that is male  
pct_females_cen_2010| number| The percentage of the 2010 Census total population that is female  
pct_females_acs_12_16| number| The percentage of the ACS population that is female  
pct_females_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that is female  
pct_pop_under_5_cen_2010| number| The percentage of the 2010 Census total population that is under five years old  
pct_pop_under_5_acs_12_16| number| The percentage of the ACS population that is under five years old  
pct_pop_under_5_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that is under five years old  
pct_pop_5_17_cen_2010| number| The percentage of the 2010 Census total population that is between 5 and 17 years old  
pct_pop_5_17_acs_12_16| number| The percentage of the ACS population that is between 5 and 17 years old  
pct_pop_5_17_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that is between 5 and 17 years old  
pct_pop_18_24_cen_2010| number| The percentage of the 2010 Census total population that is between 18 and 24 years old  
pct_pop_18_24_acs_12_16| number| The percentage of the ACS population that is between 18 and 24 years old  
pct_pop_18_24_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that is between 18 and 24 years old  
pct_pop_25_44_cen_2010| number| The percentage of the 2010 Census total population that is between 25 and 44 years old  
pct_pop_25_44_acs_12_16| number| The percentage of the ACS population that is between 25 and 44 years old  
pct_pop_25_44_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that is between 25 and 44 years old  
pct_pop_45_64_cen_2010| number| The percentage of the 2010 Census total population that is between 45 and 64 years old  
pct_pop_45_64_acs_12_16| number| The percentage of the ACS population that is between 45 and 64 years old  
pct_pop_45_64_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that is between 45 and 64 years old  
pct_pop_65plus_cen_2010| number| The percentage of the 2010 Census total population that is 65 years old or over  
pct_pop_65plus_acs_12_16| number| The percentage of the ACS population that is 65 years old or over  
pct_pop_65plus_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that is 65 years old or over  
pct_tot_gq_cen_2010| number| The percentage of the 2010 Census population living or staying in a group living arrangement owned by an entity providing housing to residents, who are usually unrelated, as of April 1, 2010  
pct_inst_gq_cen_2010| number| The percentage of the 2010 Census population who live in group quarters and are primarily ineligible, unable, or unlikely to participate in labor force while residents. Institutional group quarters include correctional facilities for adults, juvenile facilities, nursing facilities, and other institutional facilities.  
pct_non_inst_gq_cen_2010| number| The percentage of the 2010 Census population who live in group quarters and are primarily eligible, able, or likely to participate in labor force while residents. Noninstitutional group quarters include college/university student housing, military quarters, and other noninstitutional facilities.  
pct_hispanic_cen_2010| number| The percentage of the 2010 Census total population that identify as "Mexican", "Puerto Rican", "Cuban", or "another Hispanic, Latino, or Spanish origin"  
pct_hispanic_acs_12_16| number| The percentage of the ACS population that identify as "Mexican", "Puerto Rican", "Cuban", or "another Hispanic, Latino, or Spanish origin"  
pct_hispanic_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that identify as "Mexican", "Puerto Rican", "Cuban", or "another Hispanic, Latino, or Spanish origin"  
pct_nh_white_alone_cen_2010| number| The percentage of the 2010 Census total population that indicate no Hispanic origin and their only race as "White" or report entries such as Irish, German, Italian, Lebanese, Arab, Moroccan, or Caucasian  
pct_nh_white_alone_acs_12_16| number| The percentage of the ACS population that indicate no Hispanic origin and their only race as "White" or report entries such as Irish, German, Italian, Lebanese, Arab, Moroccan, or Caucasian  
pct_nh_white_alone_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that indicate no Hispanic origin and their only race as "White" or report entries such as Irish, German, Italian, Lebanese, Arab, Moroccan, or Caucasian  
pct_nh_blk_alone_cen_2010| number| The percentage of the 2010 Census total population that indicate no Hispanic origin and their only race as "Black, African Am., or Negro" or report entries such as African American, Kenyan, Nigerian, or Haitian  
pct_nh_blk_alone_acs_12_16| number| The percentage of the ACS population that indicate no Hispanic origin and their only race as "Black, African Am., or Negro" or report entries such as African American, Kenyan, Nigerian, or Haitian  
pct_nh_blk_alone_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that indicate no Hispanic origin and their only race as "Black, African Am., or Negro" or report entries such as African American, Kenyan, Nigerian, or Haitian  
pct_nh_aian_alone_cen_2010| number| The percentage of the 2010 Census total population that indicate no Hispanic origin and their only race as "American Indian or Alaska Native" or report entries such as Navajo, Blackfeet, Inupiat, Yup'ik, or Central/South American Indian groups  
pct_nh_aian_alone_acs_12_16| number| The percentage of the ACS population that indicate no Hispanic origin and their only race as "American Indian or Alaska Native" or report entries such as Navajo, Blackfeet, Inupiat, Yup'ik, or Central/South American Indian groups  
pct_nh_aian_alone_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that indicate no Hispanic origin and their only race as "American Indian or Alaska Native" or report entries such as Navajo, Blackfeet, Inupiat, Yup'ik, or Central/South American Indian groups  
pct_nh_asian_alone_cen_2010| number| The percentage of the 2010 Census total population that indicate no Hispanic origin and their only race as "Asian Indian", "Chinese", "Filipino", "Korean", "Japanese", "Vietnamese", or "Other Asian"  
pct_nh_asian_alone_acs_12_16| number| The percentage of the ACS population that indicate no Hispanic origin and their only race as "Asian Indian", "Chinese", "Filipino", "Korean", "Japanese", "Vietnamese", or "Other Asian"  
pct_nh_asian_alone_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that indicate no Hispanic origin and their only race as "Asian Indian", "Chinese", "Filipino", "Korean", "Japanese", "Vietnamese", or "Other Asian"  
pct_nh_nhopi_alone_cen_2010| number| The percentage of the 2010 Census total population that indicate no Hispanic origin and their only race as "Native Hawaiian", "Guamanian or Chamorro", "Samoan", or "Other Pacific Islander"  
pct_nh_nhopi_alone_acs_12_16| number| The percentage of the ACS population that indicate no Hispanic origin and their only race as "Native Hawaiian", "Guamanian or Chamorro", "Samoan", or "Other Pacific Islander"  
pct_nh_nhopi_alone_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that indicate no Hispanic origin and their only race as "Native Hawaiian", "Guamanian or Chamorro", "Samoan", or "Other Pacific Islander"  
pct_nh_sor_alone_cen_2010| number| The percentage of the 2010 Census total population that indicate no Hispanic origin and their race as other than "White", "Hispanic", "Black or African American", "American Indian or Alaska Native", "Asian", and "Native Hawaiian or Other Pacific Islander"  
pct_nh_sor_alone_acs_12_16| number| The percentage of the ACS population that indicate no Hispanic origin and their race as other than "White", "Hispanic", "Black or African American", "American Indian or Alaska Native", "Asian", and "Native Hawaiian or Other Pacific Islander"  
pct_nh_sor_alone_acsmoe_12_16| number| Margin of error of the percentage of the ACS population that indicate no Hispanic origin and their race as other than "White", "Hispanic", "Black or African American", "American Indian or Alaska Native", "Asian", and "Native Hawaiian or Other Pacific Islander"  
pct_pop_5yrs_over_acs_12_16| number| The percentage of the ACS population who are ages 5 years and over at time of interview  
pct_pop_5yrs_over_acsmoe_12_16| number| Margin of error of the percentage of the ACS population who are ages 5 years and over at time of interview  
pct_othr_lang_acs_12_16| number| The percentage of the ACS population aged 5 years and over that speaks a language other than English at home  
pct_othr_lang_acsmoe_12_16| number| Margin of error of the percentage of the ACS population aged 5 years and over that speaks a language other than English at home  
pct_age5p_only_eng_acs_12_16| number| The percentage of the ACS population ages 5 years and over at the time of the interview that speak only English at home  
pct_age5p_only_eng_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over that speak only English at home  
pct_age5p_spanish_acs_12_16| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Spanish or Spanish Creole at home. Examples include Ladino and Pachuco.  
pct_age5p_spanish_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Spanish or Spanish Creole at home  
pct_age5p_french_acs_12_16| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak French at home. Examples include Cajun and Patois.  
pct_age5p_french_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak French at home  
pct_age5p_german_acs_12_16| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak German at home. Examples include Luxembourgian.  
pct_age5p_german_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak German at home  
pct_age5p_russian_acs_12_16| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Russian at home  
pct_age5p_russian_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Russian at home  
pct_age5p_otheuro_acs_12_16| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak some other Indo-European language at home. Examples include Albanian, Gaelic, Lithuanian, and Romanian.  
pct_age5p_otheuro_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak some other Indo-European language at home  
pct_age5p_korean_acs_12_16| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Korean at home  
pct_age5p_korean_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Korean at home  
pct_age5p_chinese_acs_12_16| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Chinese at home. Examples include Cantonese,  
pct_age5p_chinese_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Chinese at home  
pct_age5p_vietnames_acs_12_16| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Vietnamese at home  
pct_age5p_vietnames_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Vietnamese at home  
pct_age5p_tagalog_acs_12_16| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Tagalog at home  
pct_age5p_tagalog_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Tagalog at home  
pct_age5p_othasian_acs_12_16| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak some other Asian language at home. Examples include Turkish or Dravidian languages such as Malayalam, Telugu, and Tamil.  
pct_age5p_othasian_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak some other Asian language at home  
pct_age5p_arabic_acs_12_16| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Arabic at home  
pct_age5p_arabic_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak Arabic at home  
pct_age5p_othunsp_acs_12_16| number| The percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak some other or unspecified language at home. Examples include Syriac, Finnish, other languages of the Americas, or no reported language.  
pct_age5p_othunsp_acsmoe_12_16| number| Margin of error of the percentage of the ACS population ages 5 years and over who speak English less than "very well" and speak some other or unspecified language at home  
pct_pop_25yrs_over_acs_12_16| number| The percentage of the ACS population who are ages 25 years and over at time of interview  
pct_pop_25yrs_over_acsmoe_12_16| number| Margin of error of the percentage of the ACS population who are ages 25 years and over at time of interview  
pct_not_hs_grad_acs_12_16| number| The percentage of the ACS population aged 25 years and over that are not high school graduates and have not received a diploma or the equivalent  
pct_not_hs_grad_acsmoe_12_16| number| Margin of error of the percentage of the ACS population aged 25 years and over that are not high school graduates  
pct_college_acs_12_16| number| The percentage of the ACS population aged 25 years and over that have a college degree or higher  
pct_college_acsmoe_12_16| number| Margin of error of the percentage of the ACS population aged 25 years and over that have a college degree or higher  
pct_pov_univ_acs_12_16| number| The percentage of the ACS population that are not institutionalized people, people in military group quarters, people in college dormitories, and unrelated individuals under 15 years old  
pct_pov_univ_acsmoe_12_16| number| Margin of Error for the percentage of the ACS population that are not institutionalized people, people in military group quarters, people in college dormitories, and unrelated individuals under 15 years old  
pct_prs_blw_pov_lev_acs_12_16| number| The percentage of the ACS eligible population that are classified as below the poverty level given their total family or household income within the last year, family size, and family composition  
pct_prs_blw_pov_lev_acsmoe_12_16| number| Margin of Error of the percentage of the ACS eligible population that are classified as below the poverty level  
pct_one_health_ins_acs_12_16| number| The percentage of the ACS population that have one type of health insurance coverage, including public or private  
pct_one_health_ins_acsmoe_12_16| number| Margin of Error of the percentage of the ACS population that have one type of health insurance  
pct_twophealthins_acs_12_16| number| The percentage of the ACS population that have two or more types of health insurance  
pct_twophealthins_acsmoe_12_16| number| Margin of Error of the percentage of the ACS population that have two or more types of health insurance  
pct_no_health_ins_acs_12_16| number| The percentage of the ACS population that have no health insurance, public or private  
pct_no_health_ins_acsmoe_12_16| number| Margin of Error of the percentage of the ACS population that have no health insurance  
pct_civ_emp_16p_acs_12_16| number| The percentage of ACS civilians ages 16 years and over in the labor force that are employed  
pct_civ_emp_16p_acsmoe_12_16| number| Margin of error of the percentage of civilians ages 16 years and over in the labor force that are employed  
pct_civ_unemp_16p_acs_12_16| number| The percentage of ACS civilians ages 16 years and over in the labor force that are unemployed  
pct_civ_unemp_16p_acsmoe_12_16| number| Margin of error of the percentage of civilians ages 16 years and over in the labor force that are unemployed  
pct_civ_emp_16_24_acs_12_16| number| The percentage of ACS civilians between the ages of 16 and 24 in the labor force that are employed  
pct_civ_emp_16_24_acsmoe_12_16| number| Margin of error of the percentage of civilians between the ages of 16 and 24 in the labor force that are employed  
pct_civ_unemp_16_24_acs_12_16| number| The percentage of ACS civilians between the ages of 16 and 24 in the labor force that are unemployed  
pct_civ_unemp_16_24_acsmoe_12_16| number| Margin of error of the percentage of civilians between the ages of 16 and 24 in the labor force that are unemployed  
pct_civ_emp_25_44_acs_12_16| number| The percentage of ACS civilians between the ages of 25 and 44 in the labor force that are employed  
pct_civ_emp_25_44_acsmoe_12_16| number| Margin of error of the percentage of civilians between the ages of 25 and 44 in the labor force that are employed  
pct_civ_unemp_25_44_acs_12_16| number| The percentage of ACS civilians between the ages of 25 and 44 in the labor force that are unemployed  
pct_civ_unemp_25_44_acsmoe_12_16| number| Margin of error of the percentage of civilians between the ages of 25 and 44 in the labor force that are unemployed  
pct_civ_emp_45_64_acs_12_16| number| The percentage of ACS civilians between the ages of 45 and 64 in the labor force that are employed  
pct_civ_emp_45_64_acsmoe_12_16| number| Margin of error of the percentage of civilians between the ages of 45 and 64 in the labor force that are employed  
pct_civ_unemp_45_64_acs_12_16| number| The percentage of ACS civilians between the ages of 45 and 64 in the labor force that are unemployed  
pct_civ_unemp_45_64_acsmoe_12_16| number| Margin of error of the percentage of civilians between the ages of 45 and 64 in the labor force that are unemployed  
pct_pop_disabled_acs_12_16| number| The percentage of the ACS population who have one or more disabilities.  
pct_pop_disabled_acsmoe_12_16| number| Margin of error of the percentage of the ACS population who have one or more disabilities.  
pct_pop_1yr_over_acs_12_16| number| The percentage of the ACS population who are ages 1 year and over at time of interview  
pct_pop_1yr_over_acsmoe_12_16| number| Margin of error of the percentage of the ACS population who are ages 1 year and over at time of interview  
pct_diff_hu_1yr_ago_acs_12_16| number| The percentage of the ACS population aged 1 year and over that moved from another residence in the U.S. or Puerto Rico within the last year  
pct_diff_hu_1yr_ago_acsmoe_12_16| number| Margin of Error of the percentage of the ACS population aged 1 year and over that moved from another residence in the U.S. or Puerto Rico within the last year  
pct_born_us_acs_12_16| number| The percentage of the ACS population who are citizens of the United States at birth in the ACS. This includes respondents who said that they were born in the United States, Puerto Rico, a US Island Area (such as Guam), or abroad of American (US citizen) parent or parents.  
pct_born_us_acsmoe_12_16| number| Margin of error of the percentage of the population who are US citizens at birth  
pct_born_foreign_acs_12_16| number| The percentage of the ACS population who were not a citizen of the United States at birth. This includes respondents who indicated that they were a US citizen by naturalization or not a US citizen.  
pct_born_foreign_acsmoe_12_16| number| Margin of error of the percentage of the population who are not US citizens at birth  
pct_us_cit_nat_acs_12_16| number| The percentage of the ACS population who are citizens of the United States through naturalization  
pct_us_cit_nat_acsmoe_12_16| number| Margin of error of the percentage of the population who are US citizens through naturalization  
pct_non_us_cit_acs_12_16| number| The percentage of the ACS population who are not citizens of the United States  
pct_non_us_cit_acsmoe_12_16| number| Margin of error of the percentage of the population who are not US citizens  
pct_eng_vw_span_acs_12_16| number| The percentage of all ACS occupied housing units where a Spanish or Spanish Creole language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_span_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units where a Spanish or Spanish Creole language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_indoeuro_acs_12_16| number| The percentage of all ACS occupied housing units where an Indo-European language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_indoeuro_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units where an Indo-European language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_api_acs_12_16| number| The percentage of all ACS occupied housing units where an Asian and Pacific Island language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_api_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units where an Asian and Pacific Island language was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_other_acs_12_16| number| The percentage of all ACS occupied housing units where a language other than English, Spanish, Indo-Euro, or API was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_other_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units where a language other than English, Spanish, Indo-Euro, or API was assigned as the household language and no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_acs_12_16| number| The percentage of all ACS occupied housing units where no one ages 14 years and over speaks English only or speaks English "very well"  
pct_eng_vw_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units where no one ages 14 years and over speaks English only or speaks English "very well"  
pct_rel_family_hhd_cen_2010| number| The percentage of all 2010 Census occupied housing units where at least 2 members are related by birth, marriage, or adoption; same-sex couple households with no relatives of the householder present are not included  
pct_rel_family_hhd_acs_12_16| number| The percentage of all ACS occupied housing units where at least 2 members are related by birth, marriage, or adoption; same-sex couple households with no relatives of the householder present are not included  
pct_rel_family_hhd_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units where at least 2 members are related by birth, marriage, or adoption  
pct_mrdcple_hhd_cen_2010| number| The percentage of all 2010 Census occupied housing units where the householder and his or her spouse are listed as members of the same household; does not include same-sex married couples  
pct_mrdcple_hhd_acs_12_16| number| The percentage of all ACS occupied housing units where the householder and his or her spouse are listed as members of the same household; does not include same-sex married couples  
pct_mrdcple_hhd_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units where the householder and his or her spouse are listed as members of the same household  
pct_not_mrdcple_hhd_cen_2010| number| The percentage of all 2010 Census occupied housing units where no spousal relationship is present  
pct_not_mrdcple_hhd_acs_12_16| number| The percentage of all ACS occupied housing units with no spousal relationship present  
pct_not_mrdcple_hhd_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units with no spousal relationship present  
pct_female_no_hb_cen_2010| number| The percentage of all 2010 Census occupied housing units with a female householder and no husband of householder present  
pct_female_no_hb_acs_12_16| number| The percentage of all ACS occupied housing units with a female householder and no husband of householder present  
pct_female_no_hb_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units with a female householder and no husband of householder present  
pct_nonfamily_hhd_cen_2010| number| The percentage of all 2010 Census occupied housing units where a householder lives alone or with nonrelatives only; includes same-sex couples where no relatives of the householder are present  
pct_nonfamily_hhd_acs_12_16| number| The percentage of all ACS occupied housing units where a householder lives alone or with nonrelatives only; includes same-sex couples where no relatives of the householder are present  
pct_nonfamily_hhd_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units where a householder lives alone or with nonrelatives only  
pct_sngl_prns_hhd_cen_2010| number| The percentage of all 2010 Census occupied housing units where a householder lives alone  
pct_sngl_prns_hhd_acs_12_16| number| The percentage of all ACS occupied housing units where a householder lives alone  
pct_sngl_prns_hhd_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units where a householder lives alone  
pct_hhd_ppl_und_18_cen_2010| number| The percentage of all 2010 Census occupied housing units where one or more people are ages 18 years or under  
pct_hhd_ppl_und_18_acs_12_16| number| The percentage of all ACS occupied housing units where one or more people are ages 18 years or under  
pct_hhd_ppl_und_18_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units where one or more people are ages 18 years or under  
avg_tot_prns_in_hhd_cen_2010| number| The average number of persons per 2010 Census occupied housing unit. This was calculated by dividing the total household population in the 2010 Census by the total number of occupied housing units in the 2010 Census.  
avg_tot_prns_in_hhd_acs_12_16| number| The average number of persons per ACS occupied housing unit. This was calculated by dividing the total household population in the ACS by the total number of occupied housing units in the ACS.  
avg_tot_prns_in_hhd_acsmoe_12_16| number| Margin of error of the average number of persons per ACS occupied housing unit  
pct_rel_under_6_cen_2010| number| The percentage of 2010 Census family-occupied housing units with a related child under 6 years old; same-sex couple households with no relatives of the householder present are not included in the denominator  
pct_rel_under_6_acs_12_16| number| The percentage of 2010 ACS family-occupied housing units with a related child under 6 years old; same-sex couple households with no relatives of the householder present are not included in the denominator  
pct_rel_under_6_acsmoe_12_16| number| Margin of error of the percentage of 2010 ACS family-occupied housing units with a related child under 6 years old  
pct_hhd_moved_in_acs_12_16| number| The percentage of all ACS occupied housing units where the householder moved into the current unit in the year 2010 or later  
pct_hhd_moved_in_acsmoe_12_16| number| Margin of error of the percentage of all ACS occupied housing units where the householder moved into the current unit in the year 2010 or later  
pct_pub_asst_inc_acs_12_16| number| The percentage of all ACS occupied housing units that receive public assistance income (general assistance and Temporary Assistance to Needy Families)  
pct_pub_asst_inc_acsmoe_12_16| number| Margin of error of percentage of all ACS occupied housing units that receive public assistance income  
avg_agg_hh_inc_acs_12_16| integer| The average aggregated household income of all ACS occupied housing units.  
avg_agg_hh_inc_acsmoe_12_16| integer| Margin of error for the average aggregated household income of all ACS occupied housing units.  
pct_tot_occp_units_cen_2010| number| The percentage of all 2010 Census housing units that are classified as the usual place of residence of the individual or group living in it  
pct_tot_occp_units_acs_12_16| number| The percentage of all ACS housing units that are classified as the usual place of residence of the individual or group living in it  
pct_tot_occp_units_acsmoe_12_16| number| Margin of error for the percentage of all ACS housing units that are classified as the usual place of residence of the individual or group living in it  
pct_vacant_units_cen_2010| number| The percentage of all 2010 Census housing units that have no regular occupants on Census Day; housing units with its usual occupants temporarily away (such as on vacation, a business trip, or in the hospital) are not considered vacant, but housing units temporarily occupied on Census Day by people who have a usual residence elsewhere are considered vacant  
pct_vacant_units_acs_12_16| number| The percentage of all ACS housing units where no one is living regularly at the time of interview; units occupied at the time of interview entirely by persons who are staying two months or less and who have a more permanent residence elsewhere are classified as vacant  
pct_vacant_units_acsmoe_12_16| number| Margin of error for the percentage of all ACS housing units where no one is living regularly at the time of interview  
pct_renter_occp_hu_cen_2010| number| The percentage of 2010 Census occupied housing units that are not owner occupied, whether they are rented or occupied without payment of rent  
pct_renter_occp_hu_acs_12_16| number| The percentage of ACS occupied housing units that are not owner occupied, whether they are rented or occupied without payment of rent  
pct_renter_occp_hu_acsmoe_12_16| number| Margin of error for the percentage of ACS occupied housing units that are not owner occupied  
pct_owner_occp_hu_cen_2010| number| The percentage of 2010 Census occupied housing units with an owner or co-owner living in it  
pct_owner_occp_hu_acs_12_16| number| The percentage of ACS occupied housing units with an owner or co-owner living in it  
pct_owner_occp_hu_acsmoe_12_16| number| Margin of error for the ACS occupied housing units with an owner or co-owner living in it  
pct_single_unit_acs_12_16| number| The percentage of all ACS housing units that are in a structure that contains only that single unit  
pct_single_unit_acsmoe_12_16| number| Margin of error for the percentage of all ACS housing units that are in a structure that contains only that single unit  
pct_mlt_u2_9_strc_acs_12_16| number| The percentage of all ACS housing units that are in a structure that contains two to nine housing units  
pct_mlt_u2_9_strc_acsmoe_12_16| number| Margin of error for the percentage of all ACS housing units that are in a structure that contains two to nine housing units  
pct_mlt_u10p_acs_12_16| number| The percentage of all ACS housing units that are in a structure that contains 10 or more housing units  
pct_mlt_u10p_acsmoe_12_16| number| Margin of error for the percentage of all ACS housing units that are in a structure that contains 10 or more housing units  
pct_mobile_homes_acs_12_16| number| The percentage of all ACS housing units that are considered mobile homes  
pct_mobile_homes_acsmoe_12_16| number| Margin of error for the percentage of all ACS housing units that are considered mobile homes  
pct_crowd_occp_u_acs_12_16| number| The percentage of ACS occupied housing units that have more than 1.01 persons per room  
pct_crowd_occp_u_acsmoe_12_16| number| Margin of error for the percentage of ACS occupied housing units that have more than 1.01 persons per room  
pct_no_ph_srvc_acs_12_16| number| The percentage of ACS occupied housing units that do not have a working telephone and available service  
pct_no_ph_srvc_acsmoe_12_16| number| Margin of error for the percentage of ACS occupied housing units that do not have a working telephone and available service  
pct_no_plumb_acs_12_16| number| The percentage of all ACS housing units that do not have complete plumbing facilities  
pct_no_plumb_acsmoe_12_16| number| Margin of error for the percentage of all ACS housing units that do not have complete plumbing facilities  
pct_recent_built_hu_acs_12_16| number| The percentage of all ACS housing units that are in a building that was constructed in 2010 or later  
pct_recent_built_hu_acsmoe_12_16| number| Margin of error for all ACS housing units that are in a building that was constructed in 2010 or later  
avg_agg_house_value_acs_12_16| integer| Average aggregated value in dollars for ACS occupied housing units.  
avg_agg_house_value_acsmoe_12_16| integer| Margin of error for average aggregated value in dollars for ACS occupied housing units.  
pct_tea_mailoutmailback_cen_2010| number| The percentage of addresses from which a Census form was expected to be delivered for mail return that were in a Mailout/Mailback type of enumeration area in the 2010 Census. These are addresses that received a census form in the mail and occupants were instructed to complete and mail it back.  
pct_tea_update_leave_cen_2010| string| The percentage of addresses from which a Census form was expected to be delivered for mail return that were in an Update/Leave type of enumeration area in the 2010 Census. These are addresses where a census form was hand-delivered and occupants were instructed to complete and mail it back.  
pct_census_mail_returns_cen_2010| number| The completed 2010 Census mail forms received from addresses in a mailback type of enumeration area (Mailout/Mailback and Update/Leave areas) out of all addresses from which a Census form was expected to be delivered for mail return  
pct_vacants_cen_2010| number| The percentage of addresses in a 2010 Census mailback area that were confirmed as vacant housing units (Mailout/Mailback and Update/Leave areas)  
pct_deletes_cen_2010| number| The percentage of addresses in a 2010 Census mailback area deleted because it was determined to not correspond to a valid housing unit (Mailout/Mailback and Update/Leave areas)  
pct_census_uaa_cen_2010| number| The percentage of addresses in a 2010 Census Mailout/Mailback area where the initial mail form was returned to the Census with the postal code "Undeliverable as Addressed"  
pct_mailback_count_cen_2010| number| The total number of addresses at the start of 2010 Census operations where a Census form was expected to be delivered for mail return to Census minus the number of vacant addresses, the number of deleted addresses, and the number of addresses where the initial mail form was returned to the Census with the postal code "Undeliverable as Addressed," all divided by the number of addresses in a 2010 Census mailback area  
pct_frst_frms_cen_2010| number| The percentage of all addresses in a 2010 Census mailback area for which the first Mailout/Mailback form mailed was completed and returned  
pct_rplcmnt_frms_cen_2010| number| The percentage of all addresses in a 2010 Census mailback area for which the replacement Mailout/Mailback form mailed was completed and returned  
pct_bilq_mailout_count_cen_2010| string| The percentage of all addresses in a 2010 Census mailback area that received the 2010 Census English/Spanish bilingual Mailout/Mailback form  
  
## References

Urls used in the creation of this data package.

  * **[census_planning_database](<https://www.census.gov/research/data/planning_database/2018/docs/pdb2018trv4_us.zip#encoding=latin1>)**. Source file for the planning database.
  * **metapack+https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-geography-2018.csv#tract_links**. Links communities to tracts
  * **metapack+https://library-metatab-org.s3.amazonaws.com/sandiegodata.org-geography-2018.csv#tracts**. TRACT BOUNDARIES


Last Modified 2019-01-03T22:48:33
