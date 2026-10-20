---
title: "HUD Housing Inventory Count"
date: 2019-07-12T05:00:29+00:00
draft: false
categories: ["Dataset", "homelessness"]
tags: ["homelessness", "hudexchange.info"]
author: "metapack"
description: "Project-level housing inventory for 2012 to 2018."
---

_Project-level housing inventory for 2012 to 2018._

`hudexchange.info-hic-project-1`

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[hic](<http://library.metatab.org/hudexchange.info-hic-project-1/data/hic.csv>)**. Combined HIC, 2012 to 2018


## Documentation

DUring the annual Point in Time Count, HUD also collects information about sheltered homeless, with detailed information about housing projects, including number of beds, occupancy, funding, and many other variables.

There is no formal data dictionary, so the dataset is lighly documented; the meaning of the fields is probably part of the HDX web application.

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)

  * **Publisher**

[US Department of Housing and Urban Development](<https://www.hud.gov/>)


## Packages

  * **zip** <http://library.metatab.org/hudexchange.info-hic-project-1.zip>
  * **csv** <http://library.metatab.org/hudexchange.info-hic-project-1.csv>
  * **source** <https://github.com/sandiegodata-projects/homelessness.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/hudexchange.info-hic-project-1.zip')
    
    # Create Dataframes
    
    hic_df = pkg.resource('hic').dataframe()
[/code]

## Data Dictionary

hic   


### hic

Column Name| Data Type| Description  
---|---|---  
year| integer|   
row| integer|   
cocstate| string|   
coc| string|   
coc_id| integer|   
hudnum| string|   
status| string|   
year| integer|   
organization_id| integer|   
organization_name| text|   
address1| text|   
address2| text|   
city| text|   
state| string|   
zip| string|   
project_id| integer|   
project_name| text|   
project_type| string|   
bed_type| string|   
geo_code| integer|   
inventory_type| string|   
begin_op_within_year| string|   
target_population_a| string|   
target_population_b| string|   
mc_kinney_vento| integer|   
mckinneyventoesg| integer|   
mckinneyventoesges| string|   
mckinneyventoesgrrh| string|   
mckinneyventococ| integer|   
mckinneyventococsh| string|   
mckinneyventococth| string|   
mckinneyventococpsh| string|   
mckinneyventococrrh| string|   
mckinneyventococsro| string|   
mckinneyventospc| integer|   
mckinneyventos8| integer|   
mckinneyventoshp| integer|   
federalfunding| integer|   
federalfundingvash| integer|   
federalfundingssvf| integer|   
federalfundinggpd| integer|   
federalfundinggpdbh| string|   
federalfundinggpdld| string|   
federalfundinggpdhh| string|   
federalfundinggpdct| string|   
federalfundinggpdsith| string|   
federalfundinggpdtp| string|   
federalfundinghchv| integer|   
federalfundinghchvcrs| string|   
federalfundinghchvsh| string|   
federalfundingcwt| integer|   
federalfundingbcp| integer|   
federalfundingtlp| integer|   
federalfundingmgh| integer|   
federalfundingrhydp| integer|   
federalfundinghopwa| integer|   
federalfundinghopwahmv| string|   
federalfundinghopwaph| string|   
federalfundinghopwastsf| string|   
federalfundinghopwath| string|   
federalfundingpih| integer|   
federalfundingother| integer|   
federalfundingotherspecify| string|   
housingtype| text|   
victim_service_provider| integer|   
beds_hh_w_children| string|   
units_hh_w_children| string|   
hmis_beds_hh_w_children| string|   
veteran_beds_hh_w_children| string|   
youth_beds_hh_w_children| string|   
ch_beds_hh_w_children| string|   
beds_hh_w_o_children| string|   
hmis_beds_hh_w_o_children| string|   
veteran_beds_hh_w_o_children| string|   
youth_beds_hh_w_o_children| string|   
ch_beds_hh_w_o_children| string|   
beds_hh_w_only_children| string|   
hmis_beds_hh_w_only_children| string|   
ch_beds_hh_w_only_children| string|   
year_round_beds| integer|   
dv_beds| string|   
total_seasonal_beds| string|   
seasonal_beds_available_in_hmis| string|   
availability_start_date| string|   
availability_end_date| string|   
o_v_beds| string|   
hmis_o_v_beds| string|   
pit_count| integer|   
total_beds| integer|   
updated_on| number|   
mergeddefunctyear| string|   
questionusesdescriptorelements| integer|   
questiondesirestousedescriptorelements| string|   
projectnotes| text|   
sandyrelated| string|   
sandyrelatednote| string|   
mckinneyventococsso| integer|   
projectstate| string|   
th_unit_type| string|   
scattered_sites| integer|   
ch_beds| string|   
yearveteranbedcount| integer|   
yearyouthbedcount| integer|   
youthagegroup| integer|   
program_name| string|   
program_type| string|   
usesrrhmodel| integer|   
notes| text|   
col108| unknown|   
  
## References

Urls used in the creation of this data package.

  * **[hic_2018](<https://www.hudexchange.info/resources/documents/2018-Housing-Inventory-Count-Raw-File.xlsx>)**. 2018 HIC (Raw File)
  * **[hic_2017](<https://www.hudexchange.info/resources/documents/2017-Housing-Inventory-Count-Raw-File.xlsx>)**. 2017 HIC (Raw File)
  * **[hic_2016](<https://www.hudexchange.info/resources/documents/2016-Housing-Inventory-Count-Raw-File.xlsx>)**. 2016 HIC (Raw File)
  * **[hic_2015](<https://www.hudexchange.info/resources/documents/2015-Housing-Inventory-Count-Raw-File.xlsx>)**. 2015 HIC (Raw File)
  * **[hic_2014](<https://www.hudexchange.info/resources/documents/2014-Housing-Inventory-Count-Raw-File.xlsx>)**. 2014 HIC (Raw File)
  * **[hic_2013](<https://www.hudexchange.info/resources/documents/2013-Housing-Inventory-Count-Raw-File.xlsx>)**. 2013 HIC (Raw File)
  * **[hic_2012](<https://www.hudexchange.info/resources/documents/2012HIC_RawData.xlsx#1>)**. 2012 HIC (Raw File)


Last Modified 2019-07-12T05:03:50

## Packages

  * **zip** <http://library.metatab.org/hudexchange.info-hic-project-1.zip>
  * **csv** <http://library.metatab.org/hudexchange.info-hic-project-1.csv>
  * **source** <https://github.com/sandiegodata-projects/homelessness.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/hudexchange.info-hic-project-1.zip')
    
    # Create Dataframes
    
    hic_df = pkg.resource('hic').dataframe()
[/code]
