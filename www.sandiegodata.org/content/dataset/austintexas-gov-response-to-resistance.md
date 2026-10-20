---
title: "Response to Resistance"
date: 2020-06-10T18:30:05+00:00
draft: false
categories: ["Dataset", "Police Data"]
tags: ["austintexas.gov", "crime", "law_enforcement", "police", "police_data_collection"]
author: "metapack"
description: "Austin Police Department response to police resistance incidents."
---

_Austin Police Department response to police resistance incidents._

`austintexas.gov-response_to_resistance-1.1.4`. Modified 2020-06-17T23:53:20

Resources | Packages | Documentation| Contacts| Data Dictionary

## Resources

  * **[r2r_2015](<http://library.metatab.org/austintexas.gov-response_to_resistance-1.1.4/data/r2r_2015.csv>)**. Response to Resistance, 2015
  * **[r2r_2016](<http://library.metatab.org/austintexas.gov-response_to_resistance-1.1.4/data/r2r_2016.csv>)**. Response to Resistance, 2016
  * **[r2r_2017](<http://library.metatab.org/austintexas.gov-response_to_resistance-1.1.4/data/r2r_2017.csv>)**. Response to Resistance, 2017
  * **[r2r_2018](<http://library.metatab.org/austintexas.gov-response_to_resistance-1.1.4/data/r2r_2018.csv>)**. Response to Resistance, 2018
  * **[r2r_2015_2018](<http://library.metatab.org/austintexas.gov-response_to_resistance-1.1.4/data/r2r_2015_2018.csv>)**. Combined R2R files, 2015 to 2018


## Documentation

This data package collects multiple years of the Response to Resistance dataset from the Austin, TX Police department. It includes each of the four source files and a fifth file that combines the four source files.

## Processing & Caveats

The source files, one year of data per file, have slightly different columns, so in the combined file there are some columns which will not have data across all years. These columns are:

  * census_tract
  * county
  * location_1
  * zip
  * county_description


The combined file also has a set of dummy variables for each of the values of the `subject_resistance` variable. The categories for `subject_resistance` change from year to year, and some codes from earlier years are "expired" in later years. The expiration tags have been removed, so the dummy variables mix expired and unexpired codes. This is because there are many `subject_resistance` values that only have expired codes in them. The original values etained in `subject_resistance`

It appears that the earlier two years used a wide range of detailed codes, such as "firearm" or "edged weapon" which the later years have collapsed into "agressive_resistance", "defensive resistance" and "passive resistance", with out a definite cutoffdate for the transition. The image below shows True values for the dummy variables in yellow. 

![](http://library.metatab.org/austintexas.gov-response_to_resistance-1.1.2/docs/sr_dummy_coverage.png)

## Police Data Collection

This package is part of the [San Diego Data Library's Police Data Collection](<https://github.com/metatab-packages/policedata-collection>)

### Documentation Links

  * [Data Dictionary](<https://data.austintexas.gov/Public-Safety/GUIDE-2017-R2R/27tg-e4dt/data>) A spreadsheet with field definitions, for 2017
  * [R2R Datasets](<https://data.austintexas.gov/browse?q=Response+To+Resistence&sortBy=relevance&page=1>) A search on the Austin open data site for R2R datasets.


## Images

  * [![](http://library.metatab.org/austintexas.gov-response_to_resistance-1.1.4/docs/sr_dummy_coverage.png)](<http://library.metatab.org/austintexas.gov-response_to_resistance-1.1.4/docs/sr_dummy_coverage.png> "Dummy Variable Coverage") True Values for Subject Resistance Dummy Variables by Date


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

r2r_2017 | r2r_2018 | r2r_2015 | r2r_2016 | r2r_2015_2018   


### r2r_2017

Column Name| Data Type| Description  
---|---|---  
rin| integer|   
primary_key| integer|   
date_occurred| datetime|   
time_occurred| integer|   
location| string|   
area_command| string|   
nature_of_contact| string|   
reason_desc| string|   
r2r_level| integer|   
master_subject_id| string|   
subject_sex| string|   
subject_race| string|   
subject_ethnicity| string|   
subject_conduct_desc| string|   
subject_resistance| string|   
weapon_used_1| string|   
weapon_used_2| string|   
weapon_used_3| string|   
weapon_used_4| string|   
weapon_used_5| string|   
number_shots| integer|   
subject_effects| string|   
effect_on_officer| string|   
officer_organization_desc| string|   
officer_commission_date| datetime|   
officer_yrs_of_service| integer|   
x_coordinate| integer|   
y_coordinate| integer|   
council_district| integer|   
census_tract| number|   
county| string|   
location_1| string|   
  
### r2r_2018

Column Name| Data Type| Description  
---|---|---  
rin| integer|   
primary_key| integer|   
date_occurred| datetime|   
time_occurred| integer|   
location| string|   
area_command| string|   
nature_of_contact| string|   
reason_desc| string|   
r2r_level| integer|   
master_subject_id| string|   
subject_sex| string|   
subject_race| string|   
subject_ethnicity| string|   
subject_conduct_desc| string|   
subject_resistance| string|   
weapon_used_1| string|   
weapon_used_2| string|   
weapon_used_3| string|   
weapon_used_4| string|   
weapon_used_5| unknown|   
number_shots| integer|   
effect_on_officer| string|   
officer_organization_desc| string|   
officer_commission_date| date|   
officer_yrs_of_service| integer|   
x_coordinate| integer|   
y_coordinate| integer|   
council_district| integer|   
census_tract| string|   
zip| integer|   
county| integer|   
county_description| string|   
  
### r2r_2015

Column Name| Data Type| Description  
---|---|---  
rin| integer|   
primary_key| integer|   
date_occurred| datetime|   
time_occurred| string|   
location| string|   
area_command| string|   
nature_of_contact| string|   
reason_desc| string|   
r2r_level| integer|   
master_subject_id| string|   
subject_sex| string|   
subject_race| string|   
subject_ethnicity| string|   
subject_conduct_desc| string|   
subject_resistance| string|   
weapon_used_1| string|   
weapon_used_2| string|   
weapon_used_3| string|   
weapon_used_4| string|   
weapon_used_5| unknown|   
number_shots| integer|   
subject_effects| string|   
effect_on_officer| string|   
officer_organization_desc| string|   
officer_commission_date| datetime|   
officer_yrs_of_service| integer|   
x_coordinate| integer|   
y_coordinate| integer|   
council_district| integer|   
  
### r2r_2016

Column Name| Data Type| Description  
---|---|---  
rin| integer|   
primary_key| integer|   
date_occurred| date|   
time_occurred| integer|   
location| string|   
area_command| string|   
nature_of_contact| string|   
reason_desc| string|   
r2r_level| integer|   
master_subject_id| string|   
subject_sex| string|   
subject_race| string|   
subject_ethnicity| string|   
subject_conduct_desc| string|   
subject_resistance| string|   
weapon_used_1| string|   
weapon_used_2| string|   
weapon_used_3| string|   
weapon_used_4| string|   
weapon_used_5| unknown|   
number_shots| integer|   
subject_effects| string|   
effect_on_officer| string|   
officer_organization_desc| string|   
officer_commission_date| date|   
officer_yrs_of_service| integer|   
x_coordinate| integer|   
y_coordinate| integer|   
council_district| integer|   
  
### r2r_2015_2018

Column Name| Data Type| Description  
---|---|---  
rin| integer|   
primary_key| integer|   
date_occurred| datetime|   
time_occurred| string|   
location| string|   
area_command| string|   
nature_of_contact| string|   
reason_desc| string|   
r2r_level| integer|   
master_subject_id| string|   
subject_sex| string|   
subject_race| string|   
subject_ethnicity| string|   
subject_conduct_desc| string|   
subject_resistance| string|   
weapon_used_1| string|   
weapon_used_2| string|   
weapon_used_3| string|   
weapon_used_4| string|   
weapon_used_5| string|   
number_shots| integer|   
subject_effects| string|   
effect_on_officer| string|   
officer_organization_desc| string|   
officer_commission_date| datetime|   
officer_yrs_of_service| integer|   
x_coordinate| integer|   
y_coordinate| integer|   
council_district| integer|   
census_tract| number|   
county| string|   
location_1| string|   
zip| integer|   
county_description| string|   
sr_not_resistant| string|   
sr_edged_weapon| string|   
sr_preparatory_resistance| string|   
sr_aggressive_resistance| string|   
sr_firearm| string|   
sr_defensive_resistance| string|   
sr_evading_fleeing_motor_vehicle| string|   
sr_empty_hand_defensive_resistance| string|   
sr_passive_resistance| string|   
sr_deadly_resistance| string|   
sr_verbal_resistance_aggression| string|   
sr_other| string|   
sr_none| string|   
sr_empty_hand_active_aggression| string|   
  
## Packages

  * **s3** s3://library.metatab.org/austintexas.gov-response_to_resistance-1.1.4.csv
  * **csv** <http://library.metatab.org/austintexas.gov-response_to_resistance-1.1.4.csv>
  * **source** <https://github.com/metatab-packages/policedata-collection.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/austintexas.gov-response_to_resistance-1.1.4.csv')
    
    # Create Dataframes
    r2r_2015_df = pkg.resource('r2r_2015').dataframe()
    r2r_2016_df = pkg.resource('r2r_2016').dataframe()
    r2r_2017_df = pkg.resource('r2r_2017').dataframe()
    r2r_2018_df = pkg.resource('r2r_2018').dataframe()
    r2r_2015_2018_df = pkg.resource('r2r_2015_2018').dataframe()
    
[/code]
