---
title: "San Diego Point In Time Count 2018, Tracts"
date: 2019-07-12T17:08:59+00:00
draft: false
categories: ["Dataset", "homelessness"]
tags: ["homelessness", "rtfhsd.org", "san_diego"]
author: "metapack"
description: "Unsheltered counts per tract and sheltered counts per facility, for 2018 San"
---

_Unsheltered counts per tract and sheltered counts per facility, for 2018 San Diego Point in Time Count of homeless._

`rtfhsd.org-pitc-2018-4`


## Resources

  * **[unsheltered_2018](<https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2018-4/data/unsheltered_2018.csv>)**. Unsheltered count, by tract
  * **[sheltered_2018](<https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2018-4/data/sheltered_2018.csv>)**. Housing inventory and sheltered count


## Documentation

This dataset includes the sheltered and unsheltered homeless counts from the San Diego Continuum of Care, CA-601. 

## Caveats

The sheltered count, `sheltered_2018`, is based on a data extract from HUD, and is similar, although not exactly, the same as the 2018 records for CA-601 from the official HUD HIC dataset, which [has been packaged to combine multiple years. ](</dataset/hudexchange-info-hic-project/>). The `sheltered_2018` resource in this dataset differs from the HUD dataset in two rows ( 336790, 347741 ) which appear to have been removed in an update made after source file for `sheltered_2018` was extracted. However, the PITC beds for the removed rows appear to have been re-allocated, because both datasets have the same value for the sum of the `pit_count` variable. For many analytical uses, these datasets will be identical.

However, the [HUD HIC file](<//data.sandiegodata.org/dataset/hudexchange-info-hic-project/\)>) has many columns that the `sheltered_2018` file does not, including street addresses for the facilities

## Versions

  1. Initial Version
  2. Added descriptions to data dictionary


### Documentation Links

  * [WeAllCount 2018 Annual Report](<https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2018-4/docs/2018-WPoint-in-Time-Count-Annual-Report.pdf>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2018-4.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2018-4.csv>
  * **source** <https://github.com/sandiegodata-projects/homelessness.git>


### Accessing Packages in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2018-4.zip')

# Create Dataframes

unsheltered_2018_df = pkg.resource('unsheltered_2018').dataframe()
sheltered_2018_df = pkg.resource('sheltered_2018').dataframe()
```

## Data Dictionary

unsheltered_2018 | sheltered_2018   


### unsheltered_2018

Column Name| Data Type| Description  
---|---|---  
geoid| string| Tract Geoid  
tract| string| Tract number  
community| string| Community Name where tract is located  
count| number| Count of unsheltered homless  
  
### sheltered_2018

Column Name| Data Type| Description  
---|---|---  
row| integer| Row #  
year| integer| Year  
proj_type| string| Proj. Type  
organization_name| string| Organization Name  
project_name| string| Project Name  
geo_code| integer| Geo Code  
inventory_type| string| Inventory Type  
bed_type| string| Bed Type  
target_pop_a| string| Target Pop. A  
target_pop_b| string| Target Pop. B  
beds_hh_w_children| integer| Beds HH w/ Children  
units_hh_w_children| integer| Units HH w/ Children  
beds_hh_w_o_children| integer| Beds HH w/o Children  
beds_hh_w_only_children| integer| Beds HH w/ only Children  
veteran_beds_hh_w_children| integer| Veteran Beds HH w/ Children  
youth_beds_hh_w_children| integer| Youth Beds HH w/ Children  
ch_beds_hh_w_children| integer| CH Beds HH w/ Children  
veteran_beds_hh_w_o_children| integer| Veteran Beds HH w/o Children  
youth_beds_hh_w_o_children| integer| Youth Beds HH w/o Children  
ch_beds_hh_w_o_children| integer| CH Beds HH w/o Children  
ch_beds_hh_w_only_children| integer| CH Beds HH w/ only Children  
additional_federal_funding_hud_vash| string| Additional Federal Funding: HUD-VASH  
additional_federal_funding_ssvf| string| Additional Federal Funding: SSVF  
additional_federal_funding_gpd| string| Additional Federal Funding: GPD  
additional_federal_funding_gpd_bh| string| Additional Federal Funding: GPD-BH  
additional_federal_funding_gpd_ld| string| Additional Federal Funding: GPD-LD  
additional_federal_funding_gpd_hh| string| Additional Federal Funding: GPD-HH  
additional_federal_funding_gpd_ct| string| Additional Federal Funding: GPD-CT  
additional_federal_funding_gpd_sith| string| Additional Federal Funding: GPD-SITH  
additional_federal_funding_gpd_tp| unknown| Additional Federal Funding: GPD-TP  
additional_federal_funding_hchv| string| Additional Federal Funding: HCHV  
additional_federal_funding_hchv_crs| unknown| Additional Federal Funding: HCHV-CRS  
additional_federal_funding_hchv_sh| unknown| Additional Federal Funding: HCHV-SH  
additional_federal_funding_cwt_tr| string| Additional Federal Funding: CWT/TR  
additional_federal_funding_bcp| string| Additional Federal Funding: BCP  
additional_federal_funding_tlp| string| Additional Federal Funding: TLP  
additional_federal_funding_mgh| string| Additional Federal Funding: MGH  
additional_federal_funding_hopwa| string| Additional Federal Funding: HOPWA  
additional_federal_funding_hopwa_hmv| unknown| Additional Federal Funding: HOPWA-HMV  
additional_federal_funding_hopwa_ph| string| Additional Federal Funding: HOPWA-PH  
additional_federal_funding_hopwa_stsf| unknown| Additional Federal Funding: HOPWA-STSF  
additional_federal_funding_hopwa_th| string| Additional Federal Funding: HOPWA-TH  
additional_federal_funding_pih| string| Additional Federal Funding: PIH  
additional_federal_funding_other| string| Additional Federal Funding: Other  
housing_type| text| Housing Type  
mckinney_vento_esg| string| McKinney- Vento: Esg  
mckinney_vento_esges| string| McKinney- Vento: EsgEs  
mckinney_vento_esgrrh| string| McKinney- Vento: EsgRrh  
mckinney_vento_coc| string| McKinney- Vento: Coc  
mckinney_vento_cocsh| string| McKinney- Vento: CocSh  
mckinney_vento_cocth| string| McKinney- Vento: CocTh  
mckinney_vento_cocpsh| string| McKinney- Vento: CocPsh  
mckinney_vento_cocrrh| string| McKinney- Vento: CocRrh  
mckinney_vento_cocsro| string| McKinney- Vento: CocSro  
mckinney_vento_spc| string| McKinney- Vento: SpC  
mckinney_vento_s8| string| McKinney- Vento: S8  
mckinney_vento_shp| string| McKinney- Vento: Shp  
year_round_beds| integer| Year-Round Beds  
hmis_beds_hh_w_children| integer| HMIS Beds HH w/ Children  
hmis_beds_hh_w_o_children| integer| HMIS Beds HH w/o Children  
hmis_beds_hh_w_only_children| integer| HMIS Beds HH w/ only Children  
pct_of_hmis_beds_hh_with_children| integer| % of HMIS Beds HH with Children  
pct_of_hmis_beds_hh_without_children| integer| % of HMIS Beds HH without Children  
pct_of_hmis_beds_hh_w_only_children| integer| % of HMIS Beds HH w/ only Children  
total_seasonal_beds| integer| Total Seasonal Beds  
seasonal_beds_available_in_hmis| integer| Seasonal Beds Available in HMIS  
availability_start_date| integer| Availability Start Date  
availability_end_date| integer| Availability End Date  
overflow_beds| integer| Overflow Beds  
hmis_overflow_beds| integer| HMIS Overflow Beds  
pit_count| integer| PIT Count  
total_beds| integer| Total Beds  
utilization_rate| number| Utilization Rate  
last_update_on| number| Last Update On  
  
## References

Urls used in the creation of this data package.

  * **file:data/pitc-2018.csv# &encoding=ascii**. 
  * **pitc_2018_pdf (no longer available)**. PDF document from which pitc_2018_source data were scraped


Last Modified 2019-07-17T16:32:44

## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2018-4.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2018-4.csv>
  * **source** <https://github.com/sandiegodata-projects/homelessness.git>


### Accessing Packages in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/rtfhsd.org-pitc-2018-4.zip')

# Create Dataframes

unsheltered_2018_df = pkg.resource('unsheltered_2018').dataframe()
sheltered_2018_df = pkg.resource('sheltered_2018').dataframe()
```
