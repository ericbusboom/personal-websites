---
title: "California OpenJustice Datasets"
date: 2020-06-18T00:07:45+00:00
draft: false
categories: ["Dataset", "Police Data"]
tags: ["crime", "law_enforcement", "openjustice.doj.ca.gov", "police", "police_data_collection"]
author: "metapack"
description: "Collection of mulltiple, simpler datasets from OpenJustice that don't require"
---

_Collection of mulltiple, simpler datasets from OpenJustice that don't require special processing_

`openjustice.doj.ca.gov-datasets-1.1.1`. Modified 2020-06-18T00:07:36

Resources | Packages | Documentation| Contacts| Data Dictionary

## Resources

  * **[arrests](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-datasets-1.1.1/data/arrests.csv>)**. Arrests counts aggregated to year, race, agency and other factors
  * **[arrest_dispositions](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-datasets-1.1.1/data/arrest_dispositions.csv>)**. Arrests counts aggregated to year, race, agency and other factors, but disaggregated on disposition.
  * **[complaints](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-datasets-1.1.1/data/complaints.csv>)**. Summary of civilian complaints by agency
  * **[crimes_clearances](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-datasets-1.1.1/data/crimes_clearances.csv>)**. Counts of reported cimes and clearances, by year and agency
  * **[ripa_stop](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-datasets-1.1.1/data/ripa_stop.csv>)**. RIPA Stop Data
  * **[lea_cjp](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-datasets-1.1.1/data/lea_cjp.csv>)**. Law Enforcement and Criminal Justice Personnel
  * **[leap](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-datasets-1.1.1/data/leap.csv>)**. Law Enforcement Personnel
  * **[leoka](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-datasets-1.1.1/data/leoka.csv>)**. Law Enforcement Officers Killed or Assaulted


## Documentation

### Documentation Links

  * [Open Justice Homepage](<https://openjustice.doj.ca.gov/>) A transparency initiative led by the California Department of Justice that publishes criminal justice data so we can understand how we are doing, hold ourselves accountable, and improve public policy to make California safer.


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

arrests | arrest_dispositions | complaints | crimes_clearances | ripa_stop | lea_cjp | leap | leoka   


### arrests

Column Name| Data Type| Description  
---|---|---  
year| integer|   
gender| string|   
race| string|   
age_group| string|   
county| string|   
violent| integer|   
property| integer|   
f_drugoff| integer|   
f_sexoff| integer|   
f_allother| integer|   
f_total| integer|   
m_total| integer|   
s_total| integer|   
  
### arrest_dispositions

Column Name| Data Type| Description  
---|---|---  
year| integer|   
county| string|   
gender| string|   
race| string|   
arrest_disp_code| string|   
age_group| string|   
f_total| integer|   
violent| integer|   
property| integer|   
f_drugoff| integer|   
f_sexoff| integer|   
f_allother| integer|   
m_total| integer|   
s_total| integer|   
  
### complaints

Column Name| Data Type| Description  
---|---|---  
ncic| integer|   
agencyname| string|   
complaintyear| integer|   
totalcomplaintsreported| integer|   
noncriminalreported| integer|   
misdemeanorreported| integer|   
felonyreported| integer|   
totalcomplaintsindetentionreported| integer|   
noncriminalindetentionreported| integer|   
misdemeanorindetentionreported| integer|   
felonyindetentionreported| integer|   
totalracialprofilingcomplaintsreported| integer|   
raceethnicityreported| integer|   
nationalityreported| integer|   
genderreported| integer|   
agereported| integer|   
religionreported| integer|   
genderidentityexpressionreported| integer|   
sexualorientationreported| integer|   
mentaldisabilityreported| integer|   
physicaldisabilityreported| integer|   
totalcomplaintssustained| integer|   
noncriminalsustained| integer|   
misdemeanorsustained| integer|   
felonysustained| integer|   
totalcomplaintsindetentionsustained| integer|   
noncriminalindetentionsustained| integer|   
misdemeanorindetentionsustained| integer|   
felonyindetentionsustained| integer|   
totalracialprofilingcomplaintssustained| integer|   
raceethnicitysustained| integer|   
nationalitysustained| integer|   
gendersustained| integer|   
agesustained| integer|   
religionsustained| integer|   
genderidentityexpressionsustained| integer|   
sexualorientationsustained| integer|   
mentaldisabilitysustained| integer|   
physicaldisabilitysustained| integer|   
totalcomplaintsexonerated| integer|   
noncriminalexonerated| integer|   
misdemeanorexonerated| integer|   
felonyexonerated| integer|   
totalcomplaintsindetentionexonerated| integer|   
noncriminalindetentionexonerated| integer|   
misdemeanorindetentionexonerated| integer|   
felonyindetentionexonerated| integer|   
totalracialprofilingcomplaintsexonerated| integer|   
raceethnicityexonerated| integer|   
nationalityexonerated| integer|   
genderexonerated| integer|   
ageexonerated| integer|   
religionexonerated| integer|   
genderidentityexpressionexonerated| integer|   
sexualorientationexonerated| integer|   
mentaldisabilityexonerated| integer|   
physicaldisabilityexonerated| integer|   
totalcomplaintsnotsustained| integer|   
noncriminalnotsustained| integer|   
misdemeanornotsustained| integer|   
felonynotsustained| integer|   
totalcomplaintsindetentionnotsustained| integer|   
noncriminalindetentionnotsustained| integer|   
misdemeanorindetentionnotsustained| integer|   
felonyindetentionnotsustained| integer|   
totalracialprofilingcomplaintsnotsustained| integer|   
raceethnicitynotsustained| integer|   
nationalitynotsustained| integer|   
gendernotsustained| integer|   
agenotsustained| integer|   
religionnotsustained| integer|   
genderidentityexpressionnotsustained| integer|   
sexualorientationnotsustained| integer|   
mentaldisabilitynotsustained| integer|   
physicaldisabilitynotsustained| integer|   
totalcomplaintsunfounded| integer|   
noncriminalunfounded| integer|   
misdemeanorunfounded| integer|   
felonyunfounded| integer|   
totalcomplaintsindetentionunfounded| integer|   
noncriminalindetentionunfounded| integer|   
misdemeanorindetentionunfounded| integer|   
felonyindetentionunfounded| integer|   
totalracialprofilingcomplaintsunfounded| integer|   
raceethnicityunfounded| integer|   
nationalityunfounded| integer|   
genderunfounded| integer|   
ageunfounded| integer|   
religionunfounded| integer|   
genderidentityexpressionunfounded| integer|   
sexualorientationunfounded| integer|   
mentaldisabilityunfounded| integer|   
physicaldisabilityunfounded| integer|   
totalcomplaintspending| integer|   
noncriminalpending| integer|   
misdemeanorpending| integer|   
felonypending| integer|   
totalcomplaintsindetentionpending| integer|   
noncriminalindetentionpending| integer|   
misdemeanorindetentionpending| integer|   
felonyindetentionpending| integer|   
totalracialprofilingcomplaintspending| integer|   
raceethnicitypending| integer|   
nationalitypending| integer|   
genderpending| integer|   
agepending| integer|   
religionpending| integer|   
genderidentityexpressionpending| integer|   
sexualorientationpending| integer|   
mentaldisabilitypending| integer|   
physicaldisabilitypending| integer|   
nocomplaintsfiled| integer|   
  
### crimes_clearances

Column Name| Data Type| Description  
---|---|---  
year| integer|   
county| string|   
nciccode| string|   
violent_sum| integer|   
homicide_sum| integer|   
forrape_sum| integer|   
robbery_sum| integer|   
aggassault_sum| integer|   
property_sum| integer|   
burglary_sum| integer|   
vehicletheft_sum| integer|   
lttotal_sum| integer|   
violentclr_sum| integer|   
homicideclr_sum| integer|   
forrapeclr_sum| integer|   
robberyclr_sum| integer|   
aggassaultclr_sum| integer|   
propertyclr_sum| integer|   
burglaryclr_sum| integer|   
vehicletheftclr_sum| integer|   
lttotalclr_sum| integer|   
totalstructural_sum| string|   
totalmobile_sum| string|   
totalother_sum| string|   
grandtotal_sum| string|   
grandtotclr_sum| string|   
rapact_sum| integer|   
arapact_sum| integer|   
frobact_sum| integer|   
krobact_sum| integer|   
orobact_sum| integer|   
srobact_sum| integer|   
hrobnao_sum| integer|   
chrobnao_sum| integer|   
grobnao_sum| integer|   
crobnao_sum| integer|   
rrobnao_sum| integer|   
brobnao_sum| integer|   
mrobnao_sum| integer|   
fassact_sum| integer|   
kassact_sum| integer|   
oassact_sum| integer|   
hassact_sum| integer|   
feburact_sum| integer|   
uburact_sum| integer|   
resdbur_sum| integer|   
rnburnao_sum| integer|   
rdburnao_sum| integer|   
ruburnao_sum| integer|   
nresbur_sum| integer|   
nnburnao_sum| integer|   
ndburnao_sum| integer|   
nuburnao_sum| integer|   
mvtact_sum| integer|   
tmvtact_sum| integer|   
omvtact_sum| integer|   
pplarnao_sum| integer|   
pslarnao_sum| integer|   
sllarnao_sum| integer|   
mvlarnao_sum| integer|   
mvplarnao_sum| integer|   
bilarnao_sum| integer|   
fblarnao_sum| integer|   
comlarnao_sum| integer|   
aolarnao_sum| integer|   
lt400nao_sum| integer|   
lt200400nao_sum| integer|   
lt50200nao_sum| integer|   
lt50nao_sum| integer|   
  
### ripa_stop

Column Name| Data Type| Description  
---|---|---  
_doj_record_id| string|   
person_number| integer|   
agency_ori| string|   
agency_ori_2| integer|   
agency_name| string|   
time_of_stop| integer|   
date_of_stop| datetime|   
stop_duration| integer|   
closest_city| string|   
school_code| string|   
school_name| string|   
stop_student| integer|   
k12_school_grounds| integer|   
rae_full| integer|   
rae_asian| integer|   
rae_black_african_american| integer|   
rae_hispanic_latino| integer|   
rae_middle_eastern_south_asian| integer|   
rae_native_american| integer|   
rae_pacific_islander| integer|   
rae_white| integer|   
rae_multiracial| integer|   
g_full| integer|   
g_male| integer|   
g_female| integer|   
g_transgender_man| integer|   
g_transgender_woman| integer|   
g_gender_nonconforming| integer|   
g_multigender| integer|   
lgbt| integer|   
age| integer|   
age_group| integer|   
limited_english_fluency| integer|   
pd_full| integer|   
pd_deafness_hearing| integer|   
pd_speech_impair| integer|   
pd_blind| integer|   
pd_mental_health| integer|   
pd_devel_disab| integer|   
pd_hyperactivity_disability| integer|   
pd_other| integer|   
pd_none_disability| integer|   
pd_disab_multi| integer|   
reason_for_stop| integer|   
rfs_traffic_violation_type| string|   
rfs_traffic_violation_code| string|   
rfs_rs_code| string|   
rfs_rs_off_witness| string|   
rfs_rs_match_suspect| string|   
rfs_rs_witness_id| string|   
rfs_rs_carry_sus_object| string|   
rfs_rs_actions_indicative| string|   
rfs_rs_suspect_look| string|   
rfs_rs_drug_trans| string|   
rfs_rs_violent_crime| string|   
rfs_rs_reason_susp| string|   
rfs_ec_discipline_code| string|   
rfs_ec_discipline| string|   
call_for_service| integer|   
ads_removed_vehicle_order| integer|   
ads_removed_vehicle_phycontact| integer|   
ads_sobriety_test| integer|   
ads_curb_detent| integer|   
ads_handcuffed| integer|   
ads_patcar_detent| integer|   
ads_canine_search| integer|   
ads_firearm_point| integer|   
ads_firearm_discharge| integer|   
ads_elect_device| integer|   
ads_impact_discharge| integer|   
ads_canine_bite| integer|   
ads_baton| integer|   
ads_chem_spray| integer|   
ads_other_contact| integer|   
ads_photo| integer|   
ads_asked_search_per| integer|   
ads_search_person| integer|   
ads_asked_search_prop| integer|   
ads_search_property| integer|   
ads_prop_seize| integer|   
ads_vehicle_impound| integer|   
ads_written_statement| integer|   
ads_no_actions| integer|   
ads_search_pers_consen| string|   
ads_search_prop_consen| string|   
bfs_consent_given| string|   
bfs_officer_safety| string|   
bfs_search_warrant| string|   
bfs_parole| string|   
bfs_suspect_weapon| string|   
bfs_visible_contraband| string|   
bfs_odor_contraband| string|   
bfs_canine_detect| string|   
bfs_evidence| string|   
bfs_incident| string|   
bfs_exigent_circum| string|   
bfs_vehicle_invent| string|   
bfs_school_policy| string|   
ced_none_contraband| integer|   
ced_firearm| integer|   
ced_ammunition| integer|   
ced_weapon| integer|   
ced_drugs| integer|   
ced_alcohol| integer|   
ced_money| integer|   
ced_drug_paraphernalia| integer|   
ced_stolen_prop| integer|   
ced_elect_device| integer|   
ced_other_contraband| integer|   
bps_safekeeping| string|   
bps_contraband| string|   
bps_evidence| string|   
bps_impound_vehicle| string|   
bps_abandon_prop| string|   
bps_violate_school| string|   
tps_firearm| string|   
tps_ammunition| string|   
tps_weapon| string|   
tps_drugs| string|   
tps_alcohol| string|   
tps_money| string|   
tps_drug_paraphernalia| string|   
tps_stolen_prop| string|   
tps_cellphone| string|   
tps_vehicle| string|   
tps_contraband| string|   
ros_no_action| integer|   
ros_warning| integer|   
ros_citation| integer|   
ros_in_field_cite_release| integer|   
ros_custodial_warrant| integer|   
ros_custodial_without_warrant| integer|   
ros_field_interview_card| integer|   
ros_noncriminal_transport| integer|   
ros_contact_legal_guardian| integer|   
ros_psych_hold| integer|   
ros_us_homeland| integer|   
ros_referral_school_admin| integer|   
ros_referral_school_counselor| integer|   
ros_warning_cds| string|   
ros_citation_cds| string|   
ros_in_field_cite_release_cds| string|   
ros_custodial_wout_warrant_cds| string|   
  
### lea_cjp

Column Name| Data Type| Description  
---|---|---  
year| integer|   
county| string|   
st_total| integer|   
st_le_total| integer|   
st_le_sworn| integer|   
st_le_nonsworn| integer|   
st_oth_funded_total| string|   
st_oth_funded_sworn| string|   
st_oth_funded_nonsworn| string|   
cnty_total| integer|   
cnty_le_total| integer|   
cnty_le_sworn| integer|   
cnty_le_nonsworn| integer|   
cnty_oth_funded_total| string|   
cnty_oth_funded_sworn| string|   
cnty_oth_funded_nonsworn| string|   
so_funded_total| integer|   
so_funded_sworn| integer|   
so_funded_nonsworn| integer|   
pd_funded_total| string|   
pd_funded_sworn| string|   
pd_funded_nonsworn| string|   
chp_funded_total| string|   
chp_funded_sworn| string|   
chp_funded_nonsworn| string|   
prosecution| integer|   
da_attorneys| integer|   
da_investigators| integer|   
da_clerical| integer|   
da_other| integer|   
publicdefense| string|   
pd_attorneys| string|   
pd_investigators| string|   
pd_clerical| string|   
pd_other| string|   
probationdept| integer|   
probationofficers| integer|   
prob_other| integer|   
  
### leap

Column Name| Data Type| Description  
---|---|---  
year| integer|   
ncic_agency| integer|   
funded_non_jail_sworn_male| integer|   
funded_non_jail_sworn_female| integer|   
funded_non_jail_sworn_total| integer|   
funded_non_jail_civil_male| integer|   
funded_non_jail_civil_female| integer|   
funded_non_jail_civil_total| integer|   
funded_jail_sworn_male| integer|   
funded_jail_sworn_female| integer|   
funded_jail_sworn_total| integer|   
funded_jail_civil_male| integer|   
funded_jail_civil_female| integer|   
funded_jail_civil_total| integer|   
  
### leoka

Column Name| Data Type| Description  
---|---|---  
county| string|   
agency_name| string|   
ncic_agency_code| integer|   
month| integer|   
year| integer|   
officers_killed_felony| integer|   
officers_killed_accident| integer|   
c1_a| integer|   
c1_b| integer|   
c1_c| integer|   
c1_d| integer|   
c1_e| integer|   
c1_f| integer|   
c1_g| integer|   
c1_h| integer|   
c1_i| integer|   
c1_j| integer|   
c1_k| integer|   
c1_l| integer|   
c1_m| integer|   
c2_a| integer|   
c2_b| integer|   
c2_c| integer|   
c2_d| integer|   
c2_e| integer|   
c2_f| integer|   
c2_g| integer|   
c2_h| integer|   
c2_i| integer|   
c2_j| integer|   
c2_k| integer|   
c2_l| integer|   
c2_m| integer|   
c3_a| integer|   
c3_b| integer|   
c3_c| integer|   
c3_d| integer|   
c3_e| integer|   
c3_f| integer|   
c3_g| integer|   
c3_h| integer|   
c3_i| integer|   
c3_j| integer|   
c3_k| integer|   
c3_l| integer|   
c3_m| integer|   
c4_a| integer|   
c4_b| integer|   
c4_c| integer|   
c4_d| integer|   
c4_e| integer|   
c4_f| integer|   
c4_g| integer|   
c4_h| integer|   
c4_i| integer|   
c4_j| integer|   
c4_k| integer|   
c4_l| integer|   
c4_m| integer|   
c5_a| integer|   
c5_b| integer|   
c5_c| integer|   
c5_d| integer|   
c5_e| integer|   
c5_f| integer|   
c5_g| integer|   
c5_h| integer|   
c5_i| integer|   
c5_j| integer|   
c5_k| integer|   
c5_l| integer|   
c5_m| integer|   
c6_a| integer|   
c6_b| integer|   
c6_c| integer|   
c6_d| integer|   
c6_e| integer|   
c6_f| integer|   
c6_g| integer|   
c6_h| integer|   
c6_i| integer|   
c6_j| integer|   
c6_k| integer|   
c6_l| integer|   
c6_m| integer|   
c7_a| integer|   
c7_b| integer|   
c7_c| integer|   
c7_d| integer|   
c7_e| integer|   
c7_f| integer|   
c7_g| integer|   
c7_h| integer|   
c7_i| integer|   
c7_j| integer|   
c7_k| integer|   
c7_l| integer|   
c7_m| integer|   
c8_a| integer|   
c8_b| integer|   
c8_c| integer|   
c8_d| integer|   
c8_e| integer|   
c8_f| integer|   
c8_g| integer|   
c8_h| integer|   
c8_i| integer|   
c8_j| integer|   
c8_k| integer|   
c8_l| integer|   
c8_m| integer|   
c9_a| integer|   
c9_b| integer|   
c9_c| integer|   
c9_d| integer|   
c9_e| integer|   
c9_f| integer|   
c9_g| integer|   
c9_h| integer|   
c9_i| integer|   
c9_j| integer|   
c9_k| integer|   
c9_l| integer|   
c9_m| integer|   
c10_a| integer|   
c10_b| integer|   
c10_c| integer|   
c10_d| integer|   
c10_e| integer|   
c10_f| integer|   
c10_g| integer|   
c10_h| integer|   
c10_i| integer|   
c10_j| integer|   
c10_k| integer|   
c10_l| integer|   
c10_m| integer|   
c11_a| integer|   
c11_b| integer|   
c11_c| integer|   
c11_d| integer|   
c11_e| integer|   
c11_f| integer|   
c11_g| integer|   
c11_h| integer|   
c11_i| integer|   
c11_j| integer|   
c11_k| integer|   
c11_l| integer|   
c11_m| integer|   
c12_a| integer|   
c12_b| integer|   
c12_c| integer|   
c12_d| integer|   
c12_e| integer|   
c12_f| integer|   
c12_g| integer|   
c12_h| integer|   
c12_i| integer|   
c12_j| integer|   
c12_k| integer|   
c12_l| integer|   
c12_m| integer|   
c13_a| integer|   
c13_b| integer|   
c13_c| integer|   
c13_d| integer|   
c13_e| integer|   
c14_a| integer|   
c14_b| integer|   
c14_c| integer|   
c14_d| integer|   
c14_e| integer|   
c15am_a| integer|   
c15am_b| integer|   
c15am_c| integer|   
c15am_d| integer|   
c15am_e| integer|   
c15am_f| integer|   
c15pm_a| integer|   
c15pm_b| integer|   
c15pm_c| integer|   
c15pm_d| integer|   
c15pm_e| integer|   
c15pm_f| integer|   
  
## Packages

  * **s3** s3://library.metatab.org/openjustice.doj.ca.gov-datasets-1.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-datasets-1.1.1.csv>
  * **source** <https://github.com/metatab-packages/policedata-collection.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-datasets-1.1.1.csv')
    
    # Create Dataframes
    arrests_df = pkg.resource('arrests').dataframe()
    arrest_dispositions_df = pkg.resource('arrest_dispositions').dataframe()
    complaints_df = pkg.resource('complaints').dataframe()
    crimes_clearances_df = pkg.resource('crimes_clearances').dataframe()
    ripa_stop_df = pkg.resource('ripa_stop').dataframe()
    lea_cjp_df = pkg.resource('lea_cjp').dataframe()
    leap_df = pkg.resource('leap').dataframe()
    leoka_df = pkg.resource('leoka').dataframe()
    
[/code]
