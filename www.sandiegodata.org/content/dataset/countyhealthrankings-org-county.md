---
title: "County Health Rankings"
date: 2020-05-13T17:55:21+00:00
draft: false
categories: ["covid19", "Dataset", "Health"]
tags: ["county", "countyhealthrankings.org", "covid19", "health", "national", "national-p"]
author: "metapack"
description: "The CHR&amp;R program provides data, evidence, guidance, and examples to build"
---

_The CHR &R program provides data, evidence, guidance, and examples to build awareness of the multiple factors that influence health and support community leaders working to improve health and increase health equity. The Rankings are unique in their ability to measure the health of nearly every county in all 50 states,and are complemented by guidance, tools, and resources designed to accelerate community learning and action._

`countyhealthrankings.org-county-1.1.3`. Modified 2020-08-12T17:00:43

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[county_health_rankings](<https://library-metatab-org.s3.amazonaws.com/countyhealthrankings.org-county-1.1.3/data/county_health_rankings.csv>)**. Complete datafile with all measures and supporting values. Over 800 columns.


## Documentation

### Documentation Links

  * [documentation](<https://www.countyhealthrankings.org/sites/default/files/media/document/2020%20Analytic%20Documentation_0.pdf>) Primary documentation
  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/countyhealthrankings.org-county-1.1.3/index.html>)
  * [homepage](<https://www.countyhealthrankings.org/>) Project homepage
  * [data_download](<https://www.countyhealthrankings.org/explore-health-rankings/rankings-data-documentation>) Page with links to data files and documentation


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

county_health_rankings   


### county_health_rankings

Column Name| Data Type| Description  
---|---|---  
geoid| string| ACS Geoid for County  
statecode| integer| State FIPS Code  
countycode| integer| County FIPS Code  
fipscode| integer| 5-digit FIPS Code  
state| string| State Abbreviation  
county| string| Name  
year| integer| Release Year  
county_ranked| integer| County Ranked (Yes=1/No=0)  
v001_rawvalue| number| Premature death raw value  
v001_numerator| integer| Premature death numerator  
v001_denominator| integer| Premature death denominator  
v001_cilow| number| Premature death CI low  
v001_cihigh| number| Premature death CI high  
v001_flag| integer| Premature death flag (0 = No Flag/1=Unreliable/2=Suppressed)  
v001_race_aian| number| Premature death (AIAN)  
v001_race_aian_cilow| number| Premature death CI low (AIAN)  
v001_race_aian_cihigh| number| Premature death CI high (AIAN)  
v001_race_aian_flag| integer| Premature death flag (AIAN) (. = No Flag/1=Unreliable/2=Suppressed)  
v001_race_asian| number| Premature death (Asian/Pacific Islander)  
v001_race_asian_cilow| number| Premature death CI low (Asian/Pacific Islander)  
v001_race_asian_cihigh| number| Premature death CI high (Asian/Pacific Islander)  
v001_race_asian_flag| integer| Premature death flag (Asian/Pacific Islander) (. = No Flag/1=Unreliable/2=Suppressed)  
v001_race_black| number| Premature death (Black)  
v001_race_black_cilow| number| Premature death CI low (Black)  
v001_race_black_cihigh| number| Premature death CI high (Black)  
v001_race_black_flag| integer| Premature death flag (Black) (. = No Flag/1=Unreliable/2=Suppressed)  
v001_race_hispanic| number| Premature death (Hispanic)  
v001_race_hispanic_cilow| number| Premature death CI low (Hispanic)  
v001_race_hispanic_cihigh| number| Premature death CI high (Hispanic)  
v001_race_hispanic_flag| integer| Premature death flag (Hispanic) (. = No Flag/1=Unreliable/2=Suppressed)  
v001_race_white| number| Premature death (White)  
v001_race_white_cilow| number| Premature death CI low (White)  
v001_race_white_cihigh| number| Premature death CI high (White)  
v001_race_white_flag| integer| Premature death flag (White) (. = No Flag/1=Unreliable/2=Suppressed)  
v002_rawvalue| number| Poor or fair health raw value  
v002_numerator| unknown| Poor or fair health numerator  
v002_denominator| unknown| Poor or fair health denominator  
v002_cilow| number| Poor or fair health CI low  
v002_cihigh| number| Poor or fair health CI high  
v036_rawvalue| number| Poor physical health days raw value  
v036_numerator| unknown| Poor physical health days numerator  
v036_denominator| unknown| Poor physical health days denominator  
v036_cilow| number| Poor physical health days CI low  
v036_cihigh| number| Poor physical health days CI high  
v042_rawvalue| number| Poor mental health days raw value  
v042_numerator| unknown| Poor mental health days numerator  
v042_denominator| unknown| Poor mental health days denominator  
v042_cilow| number| Poor mental health days CI low  
v042_cihigh| number| Poor mental health days CI high  
v037_rawvalue| number| Low birthweight raw value  
v037_numerator| integer| Low birthweight numerator  
v037_denominator| integer| Low birthweight denominator  
v037_cilow| number| Low birthweight CI low  
v037_cihigh| number| Low birthweight CI high  
v037_flag| integer| LBW unreliable indicator (Unreliable = Numerator 20%)  
v037_race_aian| number| Low birthweight (AIAN)  
v037_race_aian_cilow| number| Low birthweight CI low (AIAN)  
v037_race_aian_cihigh| number| Low birthweight CI high (AIAN)  
v037_race_asian| number| Low birthweight (Asian/Pacific Islander)  
v037_race_asian_cilow| number| Low birthweight CI low (Asian/Pacific Islander)  
v037_race_asian_cihigh| number| Low birthweight CI high (Asian/Pacific Islander)  
v037_race_black| number| Low birthweight (Black)  
v037_race_black_cilow| number| Low birthweight CI low (Black)  
v037_race_black_cihigh| number| Low birthweight CI high (Black)  
v037_race_hispanic| number| Low birthweight (Hispanic)  
v037_race_hispanic_cilow| number| Low birthweight CI low (Hispanic)  
v037_race_hispanic_cihigh| number| Low birthweight CI high (Hispanic)  
v037_race_white| number| Low birthweight (White)  
v037_race_white_cilow| number| Low birthweight CI low (White)  
v037_race_white_cihigh| number| Low birthweight CI high (White)  
v009_rawvalue| number| Adult smoking raw value  
v009_numerator| unknown| Adult smoking numerator  
v009_denominator| unknown| Adult smoking denominator  
v009_cilow| number| Adult smoking CI low  
v009_cihigh| number| Adult smoking CI high  
v011_rawvalue| number| Adult obesity raw value  
v011_numerator| integer| Adult obesity numerator  
v011_denominator| unknown| Adult obesity denominator  
v011_cilow| number| Adult obesity CI low  
v011_cihigh| number| Adult obesity CI high  
v133_rawvalue| number| Food environment index raw value  
v133_numerator| number| Food environment index numerator  
v133_denominator| number| Food environment index denominator  
v133_cilow| unknown| Food environment index CI low  
v133_cihigh| unknown| Food environment index CI high  
v070_rawvalue| number| Physical inactivity raw value  
v070_numerator| integer| Physical inactivity numerator  
v070_denominator| unknown| Physical inactivity denominator  
v070_cilow| number| Physical inactivity CI low  
v070_cihigh| number| Physical inactivity CI high  
v132_rawvalue| number| Access to exercise opportunities raw value  
v132_numerator| integer| Access to exercise opportunities numerator  
v132_denominator| integer| Access to exercise opportunities denominator  
v132_cilow| unknown| Access to exercise opportunities CI low  
v132_cihigh| unknown| Access to exercise opportunities CI high  
v049_rawvalue| number| Excessive drinking raw value  
v049_numerator| unknown| Excessive drinking numerator  
v049_denominator| unknown| Excessive drinking denominator  
v049_cilow| number| Excessive drinking CI low  
v049_cihigh| number| Excessive drinking CI high  
v134_rawvalue| number| Alcohol-impaired driving deaths raw value  
v134_numerator| integer| Alcohol-impaired driving deaths numerator  
v134_denominator| integer| Alcohol-impaired driving deaths denominator  
v134_cilow| number| Alcohol-impaired driving deaths CI low  
v134_cihigh| number| Alcohol-impaired driving deaths CI high  
v045_rawvalue| number| Sexually transmitted infections raw value  
v045_numerator| integer| Sexually transmitted infections numerator  
v045_denominator| integer| Sexually transmitted infections denominator  
v045_cilow| unknown| Sexually transmitted infections CI low  
v045_cihigh| unknown| Sexually transmitted infections CI high  
v014_rawvalue| number| Teen births raw value  
v014_numerator| integer| Teen births numerator  
v014_denominator| integer| Teen births denominator  
v014_cilow| number| Teen births CI low  
v014_cihigh| number| Teen births CI high  
v014_race_aian| number| Teen births (AIAN)  
v014_race_aian_cilow| number| Teen births CI low (AIAN)  
v014_race_aian_cihigh| number| Teen births CI high (AIAN)  
v014_race_asian| number| Teen births (Asian/Pacific Islander)  
v014_race_asian_cilow| number| Teen births CI low (Asian/Pacific Islander)  
v014_race_asian_cihigh| number| Teen births CI high (Asian/Pacific Islander)  
v014_race_black| number| Teen births (Black)  
v014_race_black_cilow| number| Teen births CI low (Black)  
v014_race_black_cihigh| number| Teen births CI high (Black)  
v014_race_hispanic| number| Teen births (Hispanic)  
v014_race_hispanic_cilow| number| Teen births CI low (Hispanic)  
v014_race_hispanic_cihigh| number| Teen births CI high (Hispanic)  
v014_race_white| number| Teen births (White)  
v014_race_white_cilow| number| Teen births CI low (White)  
v014_race_white_cihigh| number| Teen births CI high (White)  
v085_rawvalue| number| Uninsured raw value  
v085_numerator| integer| Uninsured numerator  
v085_denominator| integer| Uninsured denominator  
v085_cilow| number| Uninsured CI low  
v085_cihigh| number| Uninsured CI high  
v004_rawvalue| number| Primary care physicians raw value  
v004_numerator| integer| Primary care physicians numerator  
v004_denominator| integer| Primary care physicians denominator  
v004_cilow| unknown| Primary care physicians CI low  
v004_cihigh| unknown| Primary care physicians CI high  
v004_other_data_1| number| Ratio of population to primary care physicians.  
v088_rawvalue| number| Dentists raw value  
v088_numerator| integer| Dentists numerator  
v088_denominator| integer| Dentists denominator  
v088_cilow| unknown| Dentists CI low  
v088_cihigh| unknown| Dentists CI high  
v088_other_data_1| number| Ratio of population to dentists.  
v062_rawvalue| number| Mental health providers raw value  
v062_numerator| integer| Mental health providers numerator  
v062_denominator| integer| Mental health providers denominator  
v062_cilow| unknown| Mental health providers CI low  
v062_cihigh| unknown| Mental health providers CI high  
v062_other_data_1| number| Ratio of population to mental health providers.  
v005_rawvalue| integer| Preventable hospital stays raw value  
v005_numerator| unknown| Preventable hospital stays numerator  
v005_denominator| unknown| Preventable hospital stays denominator  
v005_cilow| unknown| Preventable hospital stays CI low  
v005_cihigh| unknown| Preventable hospital stays CI high  
v005_race_aian| integer| Preventable hospital stays (AIAN)  
v005_race_asian| integer| Preventable hospital stays (Asian/Pacific Islander)  
v005_race_black| integer| Preventable hospital stays (Black)  
v005_race_hispanic| integer| Preventable hospital stays (Hispanic)  
v005_race_white| integer| Preventable hospital stays (White)  
v050_rawvalue| number| Mammography screening raw value  
v050_numerator| unknown| Mammography screening numerator  
v050_denominator| unknown| Mammography screening denominator  
v050_cilow| unknown| Mammography screening CI low  
v050_cihigh| unknown| Mammography screening CI high  
v050_race_aian| number| Mammography screening (AIAN)  
v050_race_asian| number| Mammography screening (Asian/Pacific Islander)  
v050_race_black| number| Mammography screening (Black)  
v050_race_hispanic| number| Mammography screening (Hispanic)  
v050_race_white| number| Mammography screening (White)  
v155_rawvalue| number| Flu vaccinations raw value  
v155_numerator| unknown| Flu vaccinations numerator  
v155_denominator| unknown| Flu vaccinations denominator  
v155_cilow| unknown| Flu vaccinations CI low  
v155_cihigh| unknown| Flu vaccinations CI high  
v155_race_aian| number| Flu vaccinations (AIAN)  
v155_race_asian| number| Flu vaccinations (Asian/Pacific Islander)  
v155_race_black| number| Flu vaccinations (Black)  
v155_race_hispanic| number| Flu vaccinations (Hispanic)  
v155_race_white| number| Flu vaccinations (White)  
v021_rawvalue| number| High school graduation raw value  
v021_numerator| number| High school graduation numerator  
v021_denominator| number| High school graduation denominator  
v021_cilow| unknown| High school graduation CI low  
v021_cihigh| unknown| High school graduation CI high  
v069_rawvalue| number| Some college raw value  
v069_numerator| integer| Some college numerator  
v069_denominator| integer| Some college denominator  
v069_cilow| number| Some college CI low  
v069_cihigh| number| Some college CI high  
v023_rawvalue| number| Unemployment raw value  
v023_numerator| integer| Unemployment numerator  
v023_denominator| integer| Unemployment denominator  
v023_cilow| unknown| Unemployment CI low  
v023_cihigh| unknown| Unemployment CI high  
v024_rawvalue| number| Children in poverty raw value  
v024_numerator| integer| Children in poverty numerator  
v024_denominator| unknown| Children in poverty denominator  
v024_cilow| number| Children in poverty CI low  
v024_cihigh| number| Children in poverty CI high  
v024_race_aian| number| Children in poverty (AIAN)  
v024_race_aian_cilow| number| Children in poverty CI low (AIAN)  
v024_race_aian_cihigh| number| Children in poverty CI high (AIAN)  
v024_race_asian| number| Children in poverty (Asian/Pacific Islander)  
v024_race_asian_cilow| number| Children in poverty CI low (Asian/Pacific Islander)  
v024_race_asian_cihigh| number| Children in poverty CI high (Asian/Pacific Islander)  
v024_race_black| number| Children in poverty (Black)  
v024_race_black_cilow| number| Children in poverty CI low (Black)  
v024_race_black_cihigh| number| Children in poverty CI high (Black)  
v024_race_hispanic| number| Children in poverty (Hispanic)  
v024_race_hispanic_cilow| number| Children in poverty CI low (Hispanic)  
v024_race_hispanic_cihigh| number| Children in poverty CI high (Hispanic)  
v024_race_white| number| Children in poverty (White)  
v024_race_white_cilow| number| Children in poverty CI low (White)  
v024_race_white_cihigh| number| Children in poverty CI high (White)  
v044_rawvalue| number| Income inequality raw value  
v044_numerator| integer| Income inequality numerator  
v044_denominator| integer| Income inequality denominator  
v044_cilow| number| Income inequality CI low  
v044_cihigh| number| Income inequality CI high  
v082_rawvalue| number| Children in single-parent households raw value  
v082_numerator| integer| Children in single-parent households numerator  
v082_denominator| integer| Children in single-parent households denominator  
v082_cilow| number| Children in single-parent households CI low  
v082_cihigh| number| Children in single-parent households CI high  
v140_rawvalue| number| Social associations raw value  
v140_numerator| integer| Social associations numerator  
v140_denominator| integer| Social associations denominator  
v140_cilow| unknown| Social associations CI low  
v140_cihigh| unknown| Social associations CI high  
v043_rawvalue| number| Violent crime raw value  
v043_numerator| number| Violent crime numerator  
v043_denominator| number| Violent crime denominator  
v043_cilow| unknown| Violent crime CI low  
v043_cihigh| unknown| Violent crime CI high  
v135_rawvalue| number| Injury deaths raw value  
v135_numerator| integer| Injury deaths numerator  
v135_denominator| integer| Injury deaths denominator  
v135_cilow| number| Injury deaths CI low  
v135_cihigh| number| Injury deaths CI high  
v135_race_aian| number| Injury deaths (AIAN)  
v135_race_aian_cilow| number| Injury deaths CI low (AIAN)  
v135_race_aian_cihigh| number| Injury deaths CI high (AIAN)  
v135_race_asian| number| Injury deaths (Asian/Pacific Islander)  
v135_race_asian_cilow| number| Injury deaths CI low (Asian/Pacific Islander)  
v135_race_asian_cihigh| number| Injury deaths CI high (Asian/Pacific Islander)  
v135_race_black| number| Injury deaths (Black)  
v135_race_black_cilow| number| Injury deaths CI low (Black)  
v135_race_black_cihigh| number| Injury deaths CI high (Black)  
v135_race_hispanic| number| Injury deaths (Hispanic)  
v135_race_hispanic_cilow| number| Injury deaths CI low (Hispanic)  
v135_race_hispanic_cihigh| number| Injury deaths CI high (Hispanic)  
v135_race_white| number| Injury deaths (White)  
v135_race_white_cilow| number| Injury deaths CI low (White)  
v135_race_white_cihigh| number| Injury deaths CI high (White)  
v125_rawvalue| number| Air pollution - particulate matter raw value  
v125_numerator| unknown| Air pollution - particulate matter numerator  
v125_denominator| unknown| Air pollution - particulate matter denominator  
v125_cilow| unknown| Air pollution - particulate matter CI low  
v125_cihigh| unknown| Air pollution - particulate matter CI high  
v124_rawvalue| number| Drinking water violations raw value  
v124_numerator| unknown| Drinking water violations numerator  
v124_denominator| unknown| Drinking water violations denominator  
v124_cilow| unknown| Drinking water violations CI low  
v124_cihigh| unknown| Drinking water violations CI high  
v136_rawvalue| number| Severe housing problems raw value  
v136_numerator| integer| Severe housing problems numerator  
v136_denominator| integer| Severe housing problems denominator  
v136_cilow| number| Severe housing problems CI low  
v136_cihigh| number| Severe housing problems CI high  
v136_other_data_1| number| Percentage of households with high housing costs  
v136_other_data_1_cilow| number| Percentage of households with high housing costs CI low  
v136_other_data_1_cihigh| number| Percentage of households with high housing costs CI high  
v136_other_data_2| number| Percentage of households with overcrowding  
v136_other_data_2_cilow| number| Percentage of households with overcrowding CI low  
v136_other_data_2_cihigh| number| Percentage of households with overcrowding CI high  
v136_other_data_3| number| Percentage of households with lack of kitchen or plumbing facilities  
v136_other_data_3_cilow| number| Percentage of households with lack of kitchen or plumbing facilities CI low  
v136_other_data_3_cihigh| number| Percentage of households with lack of kitchen or plumbing facilities CI high  
v067_rawvalue| number| Driving alone to work raw value  
v067_numerator| integer| Driving alone to work numerator  
v067_denominator| integer| Driving alone to work denominator  
v067_cilow| number| Driving alone to work CI low  
v067_cihigh| number| Driving alone to work CI high  
v067_race_aian| number| Driving alone to work (AIAN)  
v067_race_aian_cilow| number| Driving alone to work CI low (AIAN)  
v067_race_aian_cihigh| number| Driving alone to work CI high (AIAN)  
v067_race_asian| number| Driving alone to work (Asian/Pacific Islander)  
v067_race_asian_cilow| number| Driving alone to work CI low (Asian/Pacific Islander)  
v067_race_asian_cihigh| number| Driving alone to work CI high (Asian/Pacific Islander)  
v067_race_black| number| Driving alone to work (Black)  
v067_race_black_cilow| number| Driving alone to work CI low (Black)  
v067_race_black_cihigh| number| Driving alone to work CI high (Black)  
v067_race_hispanic| number| Driving alone to work (Hispanic)  
v067_race_hispanic_cilow| number| Driving alone to work CI low (Hispanic)  
v067_race_hispanic_cihigh| number| Driving alone to work CI high (Hispanic)  
v067_race_white| number| Driving alone to work (White)  
v067_race_white_cilow| number| Driving alone to work CI low (White)  
v067_race_white_cihigh| number| Driving alone to work CI high (White)  
v137_rawvalue| number| Long commute - driving alone raw value  
v137_numerator| unknown| Long commute - driving alone numerator  
v137_denominator| integer| Long commute - driving alone denominator  
v137_cilow| number| Long commute - driving alone CI low  
v137_cihigh| number| Long commute - driving alone CI high  
v147_rawvalue| number| Life expectancy raw value  
v147_numerator| unknown| Life expectancy numerator  
v147_denominator| unknown| Life expectancy denominator  
v147_cilow| number| Life expectancy CI low  
v147_cihigh| number| Life expectancy CI high  
v147_race_aian| number| Life expectancy (AIAN)  
v147_race_aian_cilow| number| Life expectancy CI low (AIAN)  
v147_race_aian_cihigh| number| Life expectancy CI high (AIAN)  
v147_race_asian| number| Life expectancy (Asian/Pacific Islander)  
v147_race_asian_cilow| number| Life expectancy CI low (Asian/Pacific Islander)  
v147_race_asian_cihigh| number| Life expectancy CI high (Asian/Pacific Islander)  
v147_race_black| number| Life expectancy (Black)  
v147_race_black_cilow| number| Life expectancy CI low (Black)  
v147_race_black_cihigh| number| Life expectancy CI high (Black)  
v147_race_hispanic| number| Life expectancy (Hispanic)  
v147_race_hispanic_cilow| number| Life expectancy CI low (Hispanic)  
v147_race_hispanic_cihigh| number| Life expectancy CI high (Hispanic)  
v147_race_white| number| Life expectancy (White)  
v147_race_white_cilow| number| Life expectancy CI low (White)  
v147_race_white_cihigh| number| Life expectancy CI high (White)  
v127_rawvalue| number| Premature age-adjusted mortality raw value  
v127_numerator| integer| Premature age-adjusted mortality numerator  
v127_denominator| integer| Premature age-adjusted mortality denominator  
v127_cilow| number| Premature age-adjusted mortality CI low  
v127_cihigh| number| Premature age-adjusted mortality CI high  
v127_race_aian| number| Premature age-adjusted mortality (AIAN)  
v127_race_aian_cilow| number| Premature age-adjusted mortality CI low (AIAN)  
v127_race_aian_cihigh| number| Premature age-adjusted mortality CI high (AIAN)  
v127_race_asian| number| Premature age-adjusted mortality (Asian/Pacific Islander)  
v127_race_asian_cilow| number| Premature age-adjusted mortality CI low (Asian/Pacific Islander)  
v127_race_asian_cihigh| number| Premature age-adjusted mortality CI high (Asian/Pacific Islander)  
v127_race_black| number| Premature age-adjusted mortality (Black)  
v127_race_black_cilow| number| Premature age-adjusted mortality CI low (Black)  
v127_race_black_cihigh| number| Premature age-adjusted mortality CI high (Black)  
v127_race_hispanic| number| Premature age-adjusted mortality (Hispanic)  
v127_race_hispanic_cilow| number| Premature age-adjusted mortality CI low (Hispanic)  
v127_race_hispanic_cihigh| number| Premature age-adjusted mortality CI high (Hispanic)  
v127_race_white| number| Premature age-adjusted mortality (White)  
v127_race_white_cilow| number| Premature age-adjusted mortality CI low (White)  
v127_race_white_cihigh| number| Premature age-adjusted mortality CI high (White)  
v128_rawvalue| number| Child mortality raw value  
v128_numerator| integer| Child mortality numerator  
v128_denominator| integer| Child mortality denominator  
v128_cilow| number| Child mortality CI low  
v128_cihigh| number| Child mortality CI high  
v128_race_aian| number| Child mortality (AIAN)  
v128_race_aian_cilow| number| Child mortality CI low (AIAN)  
v128_race_aian_cihigh| number| Child mortality CI high (AIAN)  
v128_race_asian| number| Child mortality (Asian/Pacific Islander)  
v128_race_asian_cilow| number| Child mortality CI low (Asian/Pacific Islander)  
v128_race_asian_cihigh| number| Child mortality CI high (Asian/Pacific Islander)  
v128_race_black| number| Child mortality (Black)  
v128_race_black_cilow| number| Child mortality CI low (Black)  
v128_race_black_cihigh| number| Child mortality CI high (Black)  
v128_race_hispanic| number| Child mortality (Hispanic)  
v128_race_hispanic_cilow| number| Child mortality CI low (Hispanic)  
v128_race_hispanic_cihigh| number| Child mortality CI high (Hispanic)  
v128_race_white| number| Child mortality (White)  
v128_race_white_cilow| number| Child mortality CI low (White)  
v128_race_white_cihigh| number| Child mortality CI high (White)  
v129_rawvalue| number| Infant mortality raw value  
v129_numerator| integer| Infant mortality numerator  
v129_denominator| integer| Infant mortality denominator  
v129_cilow| number| Infant mortality CI low  
v129_cihigh| number| Infant mortality CI high  
v129_race_aian| number| Infant mortality (AIAN)  
v129_race_aian_cilow| number| Infant mortality CI low (AIAN)  
v129_race_aian_cihigh| number| Infant mortality CI high (AIAN)  
v129_race_asian| number| Infant mortality (Asian/Pacific Islander)  
v129_race_asian_cilow| number| Infant mortality CI low (Asian/Pacific Islander)  
v129_race_asian_cihigh| number| Infant mortality CI high (Asian/Pacific Islander)  
v129_race_black| number| Infant mortality (Black)  
v129_race_black_cilow| number| Infant mortality CI low (Black)  
v129_race_black_cihigh| number| Infant mortality CI high (Black)  
v129_race_hispanic| number| Infant mortality (Hispanic)  
v129_race_hispanic_cilow| number| Infant mortality CI low (Hispanic)  
v129_race_hispanic_cihigh| number| Infant mortality CI high (Hispanic)  
v129_race_white| number| Infant mortality (White)  
v129_race_white_cilow| number| Infant mortality CI low (White)  
v129_race_white_cihigh| number| Infant mortality CI high (White)  
v144_rawvalue| number| Frequent physical distress raw value  
v144_numerator| unknown| Frequent physical distress numerator  
v144_denominator| unknown| Frequent physical distress denominator  
v144_cilow| number| Frequent physical distress CI low  
v144_cihigh| number| Frequent physical distress CI high  
v145_rawvalue| number| Frequent mental distress raw value  
v145_numerator| unknown| Frequent mental distress numerator  
v145_denominator| unknown| Frequent mental distress denominator  
v145_cilow| number| Frequent mental distress CI low  
v145_cihigh| number| Frequent mental distress CI high  
v060_rawvalue| number| Diabetes prevalence raw value  
v060_numerator| integer| Diabetes prevalence numerator  
v060_denominator| unknown| Diabetes prevalence denominator  
v060_cilow| number| Diabetes prevalence CI low  
v060_cihigh| number| Diabetes prevalence CI high  
v061_rawvalue| number| HIV prevalence raw value  
v061_numerator| integer| HIV prevalence numerator  
v061_denominator| integer| HIV prevalence denominator  
v061_cilow| unknown| HIV prevalence CI low  
v061_cihigh| unknown| HIV prevalence CI high  
v139_rawvalue| number| Food insecurity raw value  
v139_numerator| integer| Food insecurity numerator  
v139_denominator| unknown| Food insecurity denominator  
v139_cilow| unknown| Food insecurity CI low  
v139_cihigh| unknown| Food insecurity CI high  
v083_rawvalue| number| Limited access to healthy foods raw value  
v083_numerator| number| Limited access to healthy foods numerator  
v083_denominator| integer| Limited access to healthy foods denominator  
v083_cilow| unknown| Limited access to healthy foods CI low  
v083_cihigh| unknown| Limited access to healthy foods CI high  
v138_rawvalue| number| Drug overdose deaths raw value  
v138_numerator| integer| Drug overdose deaths numerator  
v138_denominator| integer| Drug overdose deaths denominator  
v138_cilow| number| Drug overdose deaths CI low  
v138_cihigh| number| Drug overdose deaths CI high  
v138_race_aian| number| Drug overdose deaths (AIAN)  
v138_race_aian_cilow| number| Drug overdose deaths CI low (AIAN)  
v138_race_aian_cihigh| number| Drug overdose deaths CI high (AIAN)  
v138_race_asian| number| Drug overdose deaths (Asian/Pacific Islander)  
v138_race_asian_cilow| number| Drug overdose deaths CI low (Asian/Pacific Islander)  
v138_race_asian_cihigh| number| Drug overdose deaths CI high (Asian/Pacific Islander)  
v138_race_black| number| Drug overdose deaths (Black)  
v138_race_black_cilow| number| Drug overdose deaths CI low (Black)  
v138_race_black_cihigh| number| Drug overdose deaths CI high (Black)  
v138_race_hispanic| number| Drug overdose deaths (Hispanic)  
v138_race_hispanic_cilow| number| Drug overdose deaths CI low (Hispanic)  
v138_race_hispanic_cihigh| number| Drug overdose deaths CI high (Hispanic)  
v138_race_white| number| Drug overdose deaths (White)  
v138_race_white_cilow| number| Drug overdose deaths CI low (White)  
v138_race_white_cihigh| number| Drug overdose deaths CI high (White)  
v039_rawvalue| number| Motor vehicle crash deaths raw value  
v039_numerator| integer| Motor vehicle crash deaths numerator  
v039_denominator| integer| Motor vehicle crash deaths denominator  
v039_cilow| number| Motor vehicle crash deaths CI low  
v039_cihigh| number| Motor vehicle crash deaths CI high  
v039_race_aian| number| Motor vehicle crash deaths (AIAN)  
v039_race_aian_cilow| number| Motor vehicle crash deaths CI low (AIAN)  
v039_race_aian_cihigh| number| Motor vehicle crash deaths CI high (AIAN)  
v039_race_asian| number| Motor vehicle crash deaths (Asian/Pacific Islander)  
v039_race_asian_cilow| number| Motor vehicle crash deaths CI low (Asian/Pacific Islander)  
v039_race_asian_cihigh| number| Motor vehicle crash deaths CI high (Asian/Pacific Islander)  
v039_race_black| number| Motor vehicle crash deaths (Black)  
v039_race_black_cilow| number| Motor vehicle crash deaths CI low (Black)  
v039_race_black_cihigh| number| Motor vehicle crash deaths CI high (Black)  
v039_race_hispanic| number| Motor vehicle crash deaths (Hispanic)  
v039_race_hispanic_cilow| number| Motor vehicle crash deaths CI low (Hispanic)  
v039_race_hispanic_cihigh| number| Motor vehicle crash deaths CI high (Hispanic)  
v039_race_white| number| Motor vehicle crash deaths (White)  
v039_race_white_cilow| number| Motor vehicle crash deaths CI low (White)  
v039_race_white_cihigh| number| Motor vehicle crash deaths CI high (White)  
v143_rawvalue| number| Insufficient sleep raw value  
v143_numerator| unknown| Insufficient sleep numerator  
v143_denominator| unknown| Insufficient sleep denominator  
v143_cilow| number| Insufficient sleep CI low  
v143_cihigh| number| Insufficient sleep CI high  
v003_rawvalue| number| Uninsured adults raw value  
v003_numerator| integer| Uninsured adults numerator  
v003_denominator| integer| Uninsured adults denominator  
v003_cilow| number| Uninsured adults CI low  
v003_cihigh| number| Uninsured adults CI high  
v122_rawvalue| number| Uninsured children raw value  
v122_numerator| integer| Uninsured children numerator  
v122_denominator| integer| Uninsured children denominator  
v122_cilow| number| Uninsured children CI low  
v122_cihigh| number| Uninsured children CI high  
v131_rawvalue| number| Other primary care providers raw value  
v131_numerator| integer| Other primary care providers numerator  
v131_denominator| integer| Other primary care providers denominator  
v131_cilow| unknown| Other primary care providers CI low  
v131_cihigh| unknown| Other primary care providers CI high  
v131_other_data_1| number| Ratio of population to primary care providers other than physicians.  
v149_rawvalue| number| Disconnected youth raw value  
v149_numerator| integer| Disconnected youth numerator  
v149_denominator| integer| Disconnected youth denominator  
v149_cilow| number| Disconnected youth CI low  
v149_cihigh| number| Disconnected youth CI high  
v159_rawvalue| number| Reading scores raw value  
v159_numerator| unknown| Reading scores numerator  
v159_denominator| unknown| Reading scores denominator  
v159_cilow| unknown| Reading scores CI low  
v159_cihigh| unknown| Reading scores CI high  
v159_race_aian| unknown| Reading scores (AIAN)  
v159_race_asian| number| Reading scores (Asian/Pacific Islander)  
v159_race_black| number| Reading scores (Black)  
v159_race_hispanic| number| Reading scores (Hispanic)  
v159_race_white| number| Reading scores (White)  
v160_rawvalue| number| Math scores raw value  
v160_numerator| unknown| Math scores numerator  
v160_denominator| unknown| Math scores denominator  
v160_cilow| unknown| Math scores CI low  
v160_cihigh| unknown| Math scores CI high  
v160_race_aian| unknown| Math scores (AIAN)  
v160_race_asian| number| Math scores (Asian/Pacific Islander)  
v160_race_black| number| Math scores (Black)  
v160_race_hispanic| number| Math scores (Hispanic)  
v160_race_white| number| Math scores (White)  
v063_rawvalue| integer| Median household income raw value  
v063_numerator| unknown| Median household income numerator  
v063_denominator| unknown| Median household income denominator  
v063_cilow| number| Median household income CI low  
v063_cihigh| number| Median household income CI high  
v063_race_aian| integer| Median household income (AIAN)  
v063_race_aian_cilow| number| Median household income CI low (AIAN)  
v063_race_aian_cihigh| number| Median household income CI high (AIAN)  
v063_race_asian| integer| Median household income (Asian)  
v063_race_asian_cilow| number| Median household income CI low (Asian)  
v063_race_asian_cihigh| number| Median household income CI high (Asian)  
v063_race_black| integer| Median household income (Black)  
v063_race_black_cilow| number| Median household income CI low (Black)  
v063_race_black_cihigh| number| Median household income CI high (Black)  
v063_race_hispanic| integer| Median household income (Hispanic)  
v063_race_hispanic_cilow| number| Median household income CI low (Hispanic)  
v063_race_hispanic_cihigh| number| Median household income CI high (Hispanic)  
v063_race_white| integer| Median household income (White)  
v063_race_white_cilow| number| Median household income CI low (White)  
v063_race_white_cihigh| number| Median household income CI high (White)  
v065_rawvalue| number| Children eligible for free or reduced price lunch raw value  
v065_numerator| integer| Children eligible for free or reduced price lunch numerator  
v065_denominator| integer| Children eligible for free or reduced price lunch denominator  
v065_cilow| unknown| Children eligible for free or reduced price lunch CI low  
v065_cihigh| unknown| Children eligible for free or reduced price lunch CI high  
v141_rawvalue| number| Residential segregation - Black/White raw value  
v141_numerator| unknown| Residential segregation - Black/White numerator  
v141_denominator| unknown| Residential segregation - Black/White denominator  
v141_cilow| unknown| Residential segregation - Black/White CI low  
v141_cihigh| unknown| Residential segregation - Black/White CI high  
v142_rawvalue| number| Residential segregation - non-White/White raw value  
v142_numerator| unknown| Residential segregation - non-White/White numerator  
v142_denominator| unknown| Residential segregation - non-White/White denominator  
v142_cilow| unknown| Residential segregation - non-White/White CI low  
v142_cihigh| unknown| Residential segregation - non-White/White CI high  
v015_rawvalue| number| Homicides raw value  
v015_numerator| integer| Homicides numerator  
v015_denominator| integer| Homicides denominator  
v015_cilow| number| Homicides CI low  
v015_cihigh| number| Homicides CI high  
v015_race_aian| number| Homicides (AIAN)  
v015_race_aian_cilow| number| Homicides CI low (AIAN)  
v015_race_aian_cihigh| number| Homicides CI high (AIAN)  
v015_race_asian| number| Homicides (Asian/Pacific Islander)  
v015_race_asian_cilow| number| Homicides CI low (Asian/Pacific Islander)  
v015_race_asian_cihigh| number| Homicides CI high (Asian/Pacific Islander)  
v015_race_black| number| Homicides (Black)  
v015_race_black_cilow| number| Homicides CI low (Black)  
v015_race_black_cihigh| number| Homicides CI high (Black)  
v015_race_hispanic| number| Homicides (Hispanic)  
v015_race_hispanic_cilow| number| Homicides CI low (Hispanic)  
v015_race_hispanic_cihigh| number| Homicides CI high (Hispanic)  
v015_race_white| number| Homicides (White)  
v015_race_white_cilow| number| Homicides CI low (White)  
v015_race_white_cihigh| number| Homicides CI high (White)  
v161_rawvalue| number| Suicides raw value  
v161_numerator| integer| Suicides numerator  
v161_denominator| integer| Suicides denominator  
v161_cilow| number| Suicides CI low  
v161_cihigh| number| Suicides CI high  
v161_other_data_1| number| Crude suicide rate  
v161_race_aian| number| Suicides (AIAN)  
v161_race_aian_cilow| number| Suicides CI low (AIAN)  
v161_race_aian_cihigh| number| Suicides CI high (AIAN)  
v161_race_asian| number| Suicides (Asian/Pacific Islander)  
v161_race_asian_cilow| number| Suicides CI low (Asian/Pacific Islander)  
v161_race_asian_cihigh| number| Suicides CI high (Asian/Pacific Islander)  
v161_race_black| number| Suicides (Black)  
v161_race_black_cilow| number| Suicides CI low (Black)  
v161_race_black_cihigh| number| Suicides CI high (Black)  
v161_race_hispanic| number| Suicides (Hispanic)  
v161_race_hispanic_cilow| number| Suicides CI low (Hispanic)  
v161_race_hispanic_cihigh| number| Suicides CI high (Hispanic)  
v161_race_white| number| Suicides (White)  
v161_race_white_cilow| number| Suicides CI low (White)  
v161_race_white_cihigh| number| Suicides CI high (White)  
v148_rawvalue| number| Firearm fatalities raw value  
v148_numerator| integer| Firearm fatalities numerator  
v148_denominator| integer| Firearm fatalities denominator  
v148_cilow| number| Firearm fatalities CI low  
v148_cihigh| number| Firearm fatalities CI high  
v148_race_aian| number| Firearm fatalities (AIAN)  
v148_race_aian_cilow| number| Firearm fatalities CI low (AIAN)  
v148_race_aian_cihigh| number| Firearm fatalities CI high (AIAN)  
v148_race_asian| number| Firearm fatalities (Asian/Pacific Islander)  
v148_race_asian_cilow| number| Firearm fatalities CI low (Asian/Pacific Islander)  
v148_race_asian_cihigh| number| Firearm fatalities CI high (Asian/Pacific Islander)  
v148_race_black| number| Firearm fatalities (Black)  
v148_race_black_cilow| number| Firearm fatalities CI low (Black)  
v148_race_black_cihigh| number| Firearm fatalities CI high (Black)  
v148_race_hispanic| number| Firearm fatalities (Hispanic)  
v148_race_hispanic_cilow| number| Firearm fatalities CI low (Hispanic)  
v148_race_hispanic_cihigh| number| Firearm fatalities CI high (Hispanic)  
v148_race_white| number| Firearm fatalities (White)  
v148_race_white_cilow| number| Firearm fatalities CI low (White)  
v148_race_white_cihigh| number| Firearm fatalities CI high (White)  
v158_rawvalue| number| Juvenile arrests raw value  
v158_numerator| unknown| Juvenile arrests numerator  
v158_denominator| integer| Juvenile arrests denominator  
v158_cilow| unknown| Juvenile arrests CI low  
v158_cihigh| unknown| Juvenile arrests CI high  
v158_other_data_1| integer| Number of juvenile delinquency cases formally processed by a juvenile court  
v158_other_data_2| integer| Number of informally handled juvenile delinquency cases  
v156_rawvalue| number| Traffic volume raw value  
v156_numerator| unknown| Traffic volume numerator  
v156_denominator| unknown| Traffic volume denominator  
v156_cilow| unknown| Traffic volume CI low  
v156_cihigh| unknown| Traffic volume CI high  
v153_rawvalue| number| Homeownership raw value  
v153_numerator| integer| Homeownership numerator  
v153_denominator| integer| Homeownership denominator  
v153_cilow| number| Homeownership CI low  
v153_cihigh| number| Homeownership CI high  
v154_rawvalue| number| Severe housing cost burden raw value  
v154_numerator| integer| Severe housing cost burden numerator  
v154_denominator| integer| Severe housing cost burden denominator  
v154_cilow| number| Severe housing cost burden CI low  
v154_cihigh| number| Severe housing cost burden CI high  
v051_rawvalue| integer| Population raw value  
v051_numerator| unknown| Population numerator  
v051_denominator| unknown| Population denominator  
v051_cilow| unknown| Population CI low  
v051_cihigh| unknown| Population CI high  
v052_rawvalue| number| % below 18 years of age raw value  
v052_numerator| integer| % below 18 years of age numerator  
v052_denominator| integer| % below 18 years of age denominator  
v052_cilow| unknown| % below 18 years of age CI low  
v052_cihigh| unknown| % below 18 years of age CI high  
v053_rawvalue| number| % 65 and older raw value  
v053_numerator| integer| % 65 and older numerator  
v053_denominator| integer| % 65 and older denominator  
v053_cilow| unknown| % 65 and older CI low  
v053_cihigh| unknown| % 65 and older CI high  
v054_rawvalue| number| % Non-Hispanic Black raw value  
v054_numerator| integer| % Non-Hispanic Black numerator  
v054_denominator| integer| % Non-Hispanic Black denominator  
v054_cilow| unknown| % Non-Hispanic Black CI low  
v054_cihigh| unknown| % Non-Hispanic Black CI high  
v055_rawvalue| number| % American Indian & Alaska Native raw value  
v055_numerator| integer| % American Indian & Alaska Native numerator  
v055_denominator| integer| % American Indian & Alaska Native denominator  
v055_cilow| unknown| % American Indian & Alaska Native CI low  
v055_cihigh| unknown| % American Indian & Alaska Native CI high  
v081_rawvalue| number| % Asian raw value  
v081_numerator| integer| % Asian numerator  
v081_denominator| integer| % Asian denominator  
v081_cilow| unknown| % Asian CI low  
v081_cihigh| unknown| % Asian CI high  
v080_rawvalue| number| % Native Hawaiian/Other Pacific Islander raw value  
v080_numerator| integer| % Native Hawaiian/Other Pacific Islander numerator  
v080_denominator| integer| % Native Hawaiian/Other Pacific Islander denominator  
v080_cilow| unknown| % Native Hawaiian/Other Pacific Islander CI low  
v080_cihigh| unknown| % Native Hawaiian/Other Pacific Islander CI high  
v056_rawvalue| number| % Hispanic raw value  
v056_numerator| integer| % Hispanic numerator  
v056_denominator| integer| % Hispanic denominator  
v056_cilow| unknown| % Hispanic CI low  
v056_cihigh| unknown| % Hispanic CI high  
v126_rawvalue| number| % Non-Hispanic White raw value  
v126_numerator| integer| % Non-Hispanic White numerator  
v126_denominator| integer| % Non-Hispanic White denominator  
v126_cilow| unknown| % Non-Hispanic White CI low  
v126_cihigh| unknown| % Non-Hispanic White CI high  
v059_rawvalue| number| % not proficient in English raw value  
v059_numerator| integer| % not proficient in English numerator  
v059_denominator| integer| % not proficient in English denominator  
v059_cilow| number| % not proficient in English CI low  
v059_cihigh| number| % not proficient in English CI high  
v057_rawvalue| number| % Females raw value  
v057_numerator| integer| % Females numerator  
v057_denominator| integer| % Females denominator  
v057_cilow| unknown| % Females CI low  
v057_cihigh| unknown| % Females CI high  
v058_rawvalue| number| % Rural raw value  
v058_numerator| integer| % Rural numerator  
v058_denominator| integer| % Rural denominator  
v058_cilow| unknown| % Rural CI low  
v058_cihigh| unknown| % Rural CI high  
v104_rawvalue| number| Communicable disease raw value  
v104_numerator| integer| Communicable disease numerator  
v104_denominator| integer| Communicable disease denominator  
v104_cilow| unknown| Communicable disease CI low  
v104_cihigh| unknown| Communicable disease CI high  
v099_rawvalue| number| Cancer incidence raw value  
v099_numerator| integer| Cancer incidence numerator  
v099_denominator| integer| Cancer incidence denominator  
v099_cilow| number| Cancer incidence CI low  
v099_cihigh| number| Cancer incidence CI high  
v100_rawvalue| number| Coronary heart disease hospitalizations raw value  
v100_numerator| integer| Coronary heart disease hospitalizations numerator  
v100_denominator| unknown| Coronary heart disease hospitalizations denominator  
v100_cilow| unknown| Coronary heart disease hospitalizations CI low  
v100_cihigh| unknown| Coronary heart disease hospitalizations CI high  
v101_rawvalue| number| Cerebrovascular disease hospitalizations raw value  
v101_numerator| integer| Cerebrovascular disease hospitalizations numerator  
v101_denominator| unknown| Cerebrovascular disease hospitalizations denominator  
v101_cilow| unknown| Cerebrovascular disease hospitalizations CI low  
v101_cihigh| unknown| Cerebrovascular disease hospitalizations CI high  
v010_rawvalue| number| Smoking during pregnancy raw value  
v010_numerator| integer| Smoking during pregnancy numerator  
v010_denominator| integer| Smoking during pregnancy denominator  
v010_cilow| unknown| Smoking during pregnancy CI low  
v010_cihigh| unknown| Smoking during pregnancy CI high  
v150_rawvalue| number| Opioid hospital visits raw value  
v150_numerator| integer| Opioid hospital visits numerator  
v150_denominator| integer| Opioid hospital visits denominator  
v150_cilow| number| Opioid hospital visits CI low  
v150_cihigh| number| Opioid hospital visits CI high  
v109_rawvalue| number| Alcohol-related hospitalizations raw value  
v109_numerator| integer| Alcohol-related hospitalizations numerator  
v109_denominator| unknown| Alcohol-related hospitalizations denominator  
v109_cilow| unknown| Alcohol-related hospitalizations CI low  
v109_cihigh| unknown| Alcohol-related hospitalizations CI high  
v018_rawvalue| number| Motor vehicle crash occupancy rate raw value  
v018_numerator| integer| Motor vehicle crash occupancy rate numerator  
v018_denominator| integer| Motor vehicle crash occupancy rate denominator  
v018_cilow| unknown| Motor vehicle crash occupancy rate CI low  
v018_cihigh| unknown| Motor vehicle crash occupancy rate CI high  
v019_rawvalue| number| On-road motor vehicle crash-related ER visits raw value  
v019_numerator| integer| On-road motor vehicle crash-related ER visits numerator  
v019_denominator| integer| On-road motor vehicle crash-related ER visits denominator  
v019_cilow| number| On-road motor vehicle crash-related ER visits CI low  
v019_cihigh| number| On-road motor vehicle crash-related ER visits CI high  
v103_rawvalue| number| Childhood immunizations raw value  
v103_numerator| unknown| Childhood immunizations numerator  
v103_denominator| unknown| Childhood immunizations denominator  
v103_cilow| unknown| Childhood immunizations CI low  
v103_cihigh| unknown| Childhood immunizations CI high  
v116_rawvalue| number| Reading proficiency raw value  
v116_numerator| integer| Reading proficiency numerator  
v116_denominator| integer| Reading proficiency denominator  
v116_cilow| unknown| Reading proficiency CI low  
v116_cihigh| unknown| Reading proficiency CI high  
v117_rawvalue| integer| W-2 enrollment raw value  
v117_numerator| unknown| W-2 enrollment numerator  
v117_denominator| unknown| W-2 enrollment denominator  
v117_cilow| unknown| W-2 enrollment CI low  
v117_cihigh| unknown| W-2 enrollment CI high  
v118_rawvalue| number| Poverty raw value  
v118_numerator| integer| Poverty numerator  
v118_denominator| unknown| Poverty denominator  
v118_cilow| number| Poverty CI low  
v118_cihigh| number| Poverty CI high  
v120_rawvalue| number| Older adults living alone raw value  
v120_numerator| integer| Older adults living alone numerator  
v120_denominator| integer| Older adults living alone denominator  
v120_cilow| unknown| Older adults living alone CI low  
v120_cihigh| unknown| Older adults living alone CI high  
v119_rawvalue| number| Child abuse raw value  
v119_numerator| integer| Child abuse numerator  
v119_denominator| integer| Child abuse denominator  
v119_cilow| unknown| Child abuse CI low  
v119_cihigh| unknown| Child abuse CI high  
v106_rawvalue| number| Injury hospitalizations raw value  
v106_numerator| integer| Injury hospitalizations numerator  
v106_denominator| integer| Injury hospitalizations denominator  
v106_cilow| number| Injury hospitalizations CI low  
v106_cihigh| number| Injury hospitalizations CI high  
v105_rawvalue| number| Self-inflicted injury hospitalizations raw value  
v105_numerator| integer| Self-inflicted injury hospitalizations numerator  
v105_denominator| integer| Self-inflicted injury hospitalizations denominator  
v105_cilow| number| Self-inflicted injury hospitalizations CI low  
v105_cihigh| number| Self-inflicted injury hospitalizations CI high  
v107_rawvalue| number| Fall fatalities 65+ raw value  
v107_numerator| integer| Fall fatalities 65+ numerator  
v107_denominator| integer| Fall fatalities 65+ denominator  
v107_cilow| number| Fall fatalities 65+ CI low  
v107_cihigh| number| Fall fatalities 65+ CI high  
v123_rawvalue| number| Year structure built raw value  
v123_numerator| integer| Year structure built numerator  
v123_denominator| integer| Year structure built denominator  
v123_cilow| unknown| Year structure built CI low  
v123_cihigh| unknown| Year structure built CI high  
v008_rawvalue| integer| Male population 0-17 raw value  
v013_rawvalue| integer| Male population 18-44 raw value  
v016_rawvalue| integer| Male population 45-64 raw value  
v017_rawvalue| integer| Male population 65+ raw value  
v025_rawvalue| integer| Total male population raw value  
v026_rawvalue| integer| Female population 0-17 raw value  
v027_rawvalue| integer| Female population 18-44 raw value  
v031_rawvalue| integer| Female population 45-64 raw value  
v032_rawvalue| integer| Female population 65+ raw value  
v035_rawvalue| integer| Total female population raw value  
v097_rawvalue| number| Population growth raw value  
  
## References

Urls used in the creation of this data package.

  * **[source](<https://www.countyhealthrankings.org/sites/default/files/media/document/analytic_data2020.csv>)**. County-level statistics for a variety of health measures
  * **metapack+https://library-metatab-org.s3.amazonaws.com/census.gov-boundaries-2018.csv#county_20m**. County grographic boundary shapes.


## Packages

  * **s3** s3://library.metatab.org/countyhealthrankings.org-county-1.1.3.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/countyhealthrankings.org-county-1.1.3.csv>
  * **source** <https://github.com/CivicKnowledge/tablecloth.io.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    county_health_rankings_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/countyhealthrankings.org-county-1.1.3/data/county_health_rankings.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/countyhealthrankings.org-county-1.1.3.csv')
    
    # Create Dataframes
    county_health_rankings_df = pkg.resource('county_health_rankings').dataframe()
    
[/code]
