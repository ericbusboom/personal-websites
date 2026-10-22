---
title: "LA Homelessness Demographic Survey"
date: 2019-07-04T17:08:38+00:00
draft: false
categories: ["Dataset", "homelessness"]
tags: ["economicrt.org", "homelessness", "los_angeles"]
author: "metapack"
description: "Standardized Records from the Demographic Survey of Unsheltered Individuals"
---

_Standardized Records from the Demographic Survey of Unsheltered Individuals_

`economicrt.org-demographic_survey-1`

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[combined_survey](<https://library-metatab-org.s3.amazonaws.com/economicrt.org-demographic_survey-1/data/combined_survey.csv>)**. Combined survey data from 2011 to 2017, with all columns, naievely combined
  * **[multiyear_survey](<https://library-metatab-org.s3.amazonaws.com/economicrt.org-demographic_survey-1/data/multiyear_survey.csv>)**. Data from Demographic Surveys and HMIS Records 2011 to 2017, with a normalized subset of common columns


## Documentation

The Los Angeles Homeless Services Authority (LAHSA) conducts annual in-person surveys of the unsheltered homeless population in Los Angeles. This data package includes the standardized versions of the annual survey data for 2011 through 2017, combined into a single file (`combined_survey`) and another multi year file that was produced by UCLA, which includes only the common columns from the multi-year files. (`multiyear_survey`)

The `combined_survey` includes all of the columns from all of the years, although many columns only exist for one year. The result is that many of variables are null for one or more of the survey years.

The source for the `multiyear_survey` file was produced by UCLA and includes only a subset of the columns available in `combined_survey`, but the variables have many more non-null values.

The best way to compare these files is to look at the EDA notebooks for the files, and in particular, the Null map at the end of the notebook.

## Processing

Both files have some additional processing

  * 'NA' values are converted to blank cells
  * A new `sex` column which codes the genders Male as 'M', Female as 'F', and all others as 'U'
  * A new `raceeth` variable for census race and ethnicity categories with values for `black`, `white`, `asian`, `aian`, `aian`, `nhopi`, `hisp` and `other`, based on keywords in the `Race_Full` variable. 
  * Strip trailing spaces from `Race_Full`
  * A new `geoid` variable that holds the census tract variable converted to a format Census geoid. 
  * A new `year` variable that holds an integer version of the `Survey_Year`` variable


### Documentation Links

  * [2011 Codebook](</uploads/2018/08/2011_Unsheltered_Codebook.docx>)2011 Codebook for Standardized Records from the Demographic Survey of Unsheltered Individuals
  * [2011 Methodology White Paper](</uploads/2018/08/2011_Methodology.pdf>)
  * [2013 Codebook](</uploads/2018/08/2013_Unsheltered_Codebook.docx>)2013 Codebook for Standardized Records from the Demographic Survey of Unsheltered Individuals
  * [2013 Methodology White Paper](</uploads/2018/08/2013_Methodology.pdf>)
  * [2015 Codebook](</uploads/2018/08/2015_Unsheltered_Codebook.docx>)2015 Codebook for Standardized Records from the Demographic Survey of Unsheltered Individuals
  * [2015 Methodology White Paper](</uploads/2018/08/2015_Methodology.pdf>)
  * [2016 Codebook](</uploads/2018/08/2016-Unsheltered-Codebook.docx>)2016 Codebook for Standardized Records from the Demographic Survey of Unsheltered Individuals
  * [2016 Methodology White Paper](</uploads/2018/08/2016_Methodology.pdf>)
  * [2017 Codebook](</uploads/2018/08/2017_Sheltered_Codebook.docx>)2017 Codebook for Standardized HMIS Records of Sheltered Individuals
  * [2017 Methodology White Paper](</uploads/2018/08/2017_Methodology.pdf>)
  * [Codebook](</uploads/2018/08/Multi_Year_Codebook_2011_2017.docx>)Codebook for Multi-Year Data Set
  * [Download Page](<https://economicrt.org/publication/los-angeles-county-homeless-count-data-library/>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)

  * **Publisher**

[The Economic Roundtable](<https://economicrt.org/about/>)

  * **Creator**

[Los Angeles Homeless Services Authority](<https://www.lahsa.org/>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/economicrt.org-demographic_survey-1.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/economicrt.org-demographic_survey-1.csv>
  * **source** <https://github.com/metatab-packages/metatab-packages.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/economicrt.org-demographic_survey-1.zip')
    
    # Create Dataframes
    
    combined_survey_df = pkg.resource('combined_survey').dataframe()
    multiyear_survey_df = pkg.resource('multiyear_survey').dataframe()
[/code]

## Data Dictionary

combined_survey | multiyear_survey   


### combined_survey

Column Name| Data Type| Description  
---|---|---  
year| integer|   
gender| string|   
sex| string|   
raceeth| string|   
race_full| string|   
race_recode| string|   
ethnicity| string|   
age| integer|   
birth_year| integer|   
census_tract| string|   
census_tract_or_shelterid| string|   
spa| integer|   
adult_probation_involvement| integer|   
adult_with_child| integer|   
age_first_homeless| integer|   
alcohol_abuse_ever| integer|   
alcohol_abuse_past_year| integer|   
automobile_past_6mnths| integer|   
automobile_past_year| integer|   
car_past_6mnths| integer|   
car_past_year| integer|   
chronic| integer|   
chronic_condition| integer|   
chronic_time| integer|   
current_stint_duration| string|   
current_stint_duration_detailed| string|   
currently_access_dropin| integer|   
currently_alcohol_drug_counseling| integer|   
currently_case_management| integer|   
currently_emergency_shelter| integer|   
currently_housing_placement| integer|   
currently_job_training| integer|   
currently_legal_assistance| integer|   
currently_mental_health| integer|   
currently_pay_shelter| integer|   
currently_transitional_housing| integer|   
day_labor| integer|   
depression| integer|   
depression_past_year| integer|   
developmental_disability_ever| integer|   
drug_abuse_ever| integer|   
drug_abuse_past_year| integer|   
drug_alcohol_history| integer|   
encampment_past_year| integer|   
er_past_year| string|   
er_times_past_3mnths| string|   
foster_care_involvement| integer|   
full_time| integer|   
gov_assist_calworks| integer|   
gov_assist_capi| integer|   
gov_assist_child_support| integer|   
gov_assist_food_stamps| integer|   
gov_assist_general_relief| integer|   
gov_assist_medical| integer|   
gov_assist_medicare| integer|   
gov_assist_social_security| integer|   
gov_assist_ssi_ssd| integer|   
gov_assist_unemployment| integer|   
gov_assist_vet_disability_payment| integer|   
gov_assist_vet_other_benefit| integer|   
gov_assist_vet_pension| integer|   
gov_assist_women_infants_children| integer|   
hardship_from_substance_abuse| integer|   
have_child| integer|   
have_had_child| integer|   
hiv_positive| integer|   
hospital_times_past_year| string|   
indoor_majority_last_month| string|   
jail_prison_involvement| integer|   
justice_system_homeless| integer|   
justice_system_past_year| integer|   
juvenile_probation_involvement| integer|   
la_community_before_current_stint| string|   
la_county_years| number|   
location_before_current_stint| string|   
location_before_current_stint_raw| string|   
long_term_health_past_year| integer|   
mental_illness_ever| integer|   
mental_illness_past_year| integer|   
msshelter_past_6mnths| integer|   
new_to_homelessness| integer|   
observed_mental| integer|   
observed_physical| integer|   
observed_substance| integer|   
outside_la_county| integer|   
outside_majority_last_month| string|   
panhandling| integer|   
parole_involvement| integer|   
part_time| integer|   
performance| integer|   
physical_disability_ever| integer|   
physical_disability_past_year| integer|   
physical_illness_ever| integer|   
physical_sexual_abuse| integer|   
ptsd_ever| integer|   
reason_homeless_breakup| integer|   
reason_homeless_child_support| integer|   
reason_homeless_death_illness_fam| integer|   
reason_homeless_dv| integer|   
reason_homeless_eviction| integer|   
reason_homeless_family_hmls| integer|   
reason_homeless_foster_care| integer|   
reason_homeless_hh_conflict| integer|   
reason_homeless_immigration| integer|   
reason_homeless_jail_prison| integer|   
reason_homeless_job| integer|   
reason_homeless_medical| integer|   
reason_homeless_mental| integer|   
reason_homeless_no_fam| integer|   
reason_homeless_previous_housing_program| integer|   
reason_homeless_released_treatment| integer|   
reason_homeless_safety| integer|   
reason_homeless_sexual_orientation| integer|   
reason_homeless_subs_abuse| integer|   
reason_previous_housing_program| integer|   
reason_previous_uninhabitable_housing| integer|   
recycling| integer|   
retired| integer|   
rv_camper_past_6mnths| integer|   
rv_camper_past_year| integer|   
seasonal| integer|   
severe_depression_ever| integer|   
severe_depression_past_year| integer|   
sex_traffic| integer|   
sex_worker| integer|   
sexual_orientation| string|   
student_vocational| integer|   
temp_work| integer|   
tent_past_6mnths| integer|   
tent_past_year| integer|   
times_homeless_3yrs| string|   
times_homeless_past_year| string|   
tobacco_past_year| integer|   
total_time_homeless_life| string|   
traumatic_brain_injury_ever| integer|   
turned_away_age_requirement| integer|   
turned_away_criminal_record| integer|   
turned_away_drug_alcohol| integer|   
turned_away_ever| integer|   
turned_away_had_children| integer|   
turned_away_had_pets| integer|   
turned_away_immigration| integer|   
turned_away_lack_housing| integer|   
turned_away_last_month| integer|   
turned_away_mental| integer|   
turned_away_no_beds| integer|   
turned_away_noid| integer|   
turned_away_not_foster| integer|   
turned_away_partner| integer|   
turned_away_physical| integer|   
turned_away_pregnant| integer|   
turned_away_previous_stay| integer|   
turned_away_strictness| integer|   
unable_to_work_disability| integer|   
unemployed_looking| integer|   
unemployed_not_looking| integer|   
van_past_6mnths| integer|   
van_past_year| integer|   
veteran| integer|   
work_barrier_experience| integer|   
work_barrier_gaps| integer|   
work_barrier_lack_ed| integer|   
work_barrier_no_access| integer|   
work_barrier_no_interview| integer|   
work_barrier_turned_down| integer|   
weights| number|   
  
### multiyear_survey

Column Name| Data Type| Description  
---|---|---  
geoid| string|   
survey_year| string|   
survey_type| string|   
year| integer|   
birth_year| integer|   
age| number|   
gender| string|   
sex| string|   
ethnicity| string|   
race_full| string|   
race_recode| string|   
raceeth| string|   
veteran| integer|   
chronic_time| integer|   
chronic_condition| integer|   
chronic| integer|   
adult_with_child| integer|   
times_homeless_3yrs| string|   
times_homeless_past_year| string|   
current_stint_duration| string|   
spa| integer|   
census_tract| integer|   
physical_sexual_abuse| integer|   
physical_disability| integer|   
mental_illness| integer|   
alcohol_abuse| integer|   
drug_abuse| integer|   
drug_alcohol_history| integer|   
hiv_positive| integer|   
part_time| integer|   
full_time| integer|   
unemployed_looking| integer|   
unemployed_not_looking| integer|   
  
## References

Urls used in the creation of this data package.

  * **[demo_survey_2011](</uploads/2018/08/Demographic_Survey_2011_Final.csv>)**. 2011 Homeless Count Unsheltered Adult and Youth Demographic Survey - Individuals - Standardized Records
  * **[demo_survey_2013](</uploads/2018/08/Demographic_Survey_2013_Final.csv>)**. 2013 Homeless Count Unsheltered Adult and Youth Demographic Survey - Individuals - Standardized Records
  * **[demo_survey_2015](</uploads/2018/08/Demographic_Survey_2015_Final.csv>)**. 2015 Homeless Count Unsheltered Adult and Youth Demographic Survey - Individuals - Standardized Records
  * **[demo_survey_2016](</uploads/2018/08/Demographic_Survey_2016_Final.csv>)**. 2016 Homeless Count Unsheltered Adult and Youth Demographic Survey - Individuals - Standardized Records
  * **[demo_survey_2017](</uploads/2018/09/Demographic_Survey_2017_v3.csv>)**. 2017 Homeless Count Unsheltered Adults and Youth Demographic Survey - Individuals - Standardized Records
  * **[demo_survey_2011_2017](</uploads/2018/08/Homelessness_Multi_Year_2011_2017.csv>)**. Data from Demographic Surveys and HMIS Records 2011 to 2017


Last Modified 2019-07-17T00:48:21

## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/economicrt.org-demographic_survey-1.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/economicrt.org-demographic_survey-1.csv>
  * **source** <https://github.com/metatab-packages/metatab-packages.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/economicrt.org-demographic_survey-1.zip')
    
    # Create Dataframes
    
    combined_survey_df = pkg.resource('combined_survey').dataframe()
    multiyear_survey_df = pkg.resource('multiyear_survey').dataframe()
[/code]
