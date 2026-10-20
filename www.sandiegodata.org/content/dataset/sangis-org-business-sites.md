---
title: "San Diego County Business Sites"
date: 2019-06-13T04:41:46+00:00
draft: false
categories: ["build_environment", "Dataset", "planning", "planning-collection"]
tags: ["build_environment", "Business", "planning", "planning-collection", "planning-project", "sangis.org"]
author: "metapack"
description: "Point locations of businesses and tract aggregations of counts of businesses by"
---

_Point locations of businesses and tract aggregations of counts of businesses by type._

`sangis.org-business_sites-2`

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[business_sites](<http://library.metatab.org/sangis.org-business_sites-2/data/business_sites.csv>)**. Business sites, geographic file
  * **[tract_counts_rows](<http://library.metatab.org/sangis.org-business_sites-2/data/tract_counts_rows.csv>)**. Business counts per tract, by type of business, oriented by rows
  * **[tract_counts_columns](<http://library.metatab.org/sangis.org-business_sites-2/data/tract_counts_columns.csv>)**. Business counts per tract, by type of business, oriented by columns


## Documentation

This dataset is based on the SANGIS BUSINESS_SITES data file, which is compiled from the Assessors Business Property Account Master file. This file is different from the City of San Diego's business list, in that it includes records for the whole county, it categorizes businesses differently ( not using NAICS codes ) and for some categories, it does not appear to be very accurate. 

This package includes two additional files, which link counts of businesses by categories to tracts. 

  * `tract_counts_rows` presents the counts of businesses as rows. There is one row for each combination of type of business and census tract. 
  * `tract_counts_columns` presents the counts of businesses as columns. There is one row per tract, and one column for each type of business. 


The row oriented file is easier to use in tools that have good support for filtering, such as Pandas and Tableau. The column oriented form is easier to use in tools where selecting a column is easier than filtering, such as QGIS. 

## Caveats

The upstream documentation warns:

Data should be used with caution as not all addresses and/or APN numbers are correct, and certain business sites do not have precise addresses so that locations are approximate. Certain business sites could not be located but remain in the dataset.

### Documentation Links

  * [Primary Documentation](<http://library.metatab.org/sangis.org-business_sites-2/doc/BUSINESS_SITES.pdf>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <http://library.metatab.org/sangis.org-business_sites-2.zip>
  * **csv** <http://library.metatab.org/sangis.org-business_sites-2.csv>
  * **source** <https://github.com/sandiegodata/planning-database.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('http://library.metatab.org/sangis.org-business_sites-2.zip')
    # CSV Package
    pkg = mp.open_package('http://library.metatab.org/sangis.org-business_sites-2.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

## Data Dictionary

business_sites | tract_counts_rows | tract_counts_columns   


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
strnum| number|   
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
  
### tract_counts_rows

Column Name| Data Type| Description  
---|---|---  
geoid| string|   
bcccode| integer|   
bustype| string|   
count| integer|   
  
### tract_counts_columns

Column Name| Data Type| Description  
---|---|---  
geoid| string|   
geometry| string|   
total| integer|   
1_hour_film_processi| integer|   
1_way_paging_equip| integer|   
accountant| integer|   
advertising| integer|   
aerospace_airframe| integer|   
airlines_non_fleet| integer|   
airport_x| integer|   
airport_operator| integer|   
ambulance| integer|   
amusement_center| integer|   
antique| integer|   
apartments| integer|   
appliance_furniture| integer|   
appliance_repair_ser| integer|   
appliances_retail| integer|   
appliances_wholesale| integer|   
architect_engineer| integer|   
art_dealers| integer|   
attorney| integer|   
auctioneer| integer|   
auto_agency| integer|   
auto_body_fender| integer|   
auto_parking| integer|   
auto_parts_retail| integer|   
auto_parts_wholesale| integer|   
auto_rental| integer|   
auto_repair_shop| integer|   
auto_tires| integer|   
auto_wash_self_serv| integer|   
auto_washer| integer|   
bail_bonds| integer|   
bakery| integer|   
bakery_baker| integer|   
bakery_confectioners| integer|   
ballroom| integer|   
banks| integer|   
bar| integer|   
barber_beauty_shop_s| integer|   
barber_shop| integer|   
beauty_barber_supply| integer|   
beauty_shop| integer|   
beverage_beer_wine| integer|   
beverage_soft_drink| integer|   
bicycle_stores| integer|   
billboards| integer|   
billiard_bowl_card| integer|   
bio_med_r_d| integer|   
bio_tech_industry| integer|   
blueprints_maps| integer|   
boat_mfg| integer|   
boat_repair| integer|   
boat_suppliers| integer|   
body_culture_massage| integer|   
book_store| integer|   
bottled_water_compan| integer|   
brake_alignment| integer|   
brick_cement| integer|   
brick_products_retl| integer|   
brick_tile_mfg| integer|   
building_supplies_ge| integer|   
business_miscellaneo| integer|   
business_school| integer|   
cafe| integer|   
cafe_fast_food| integer|   
candy_stores| integer|   
canneries| integer|   
cargo_container| integer|   
carpet_draperies| integer|   
carpet_rug_movable| integer|   
cars_used| integer|   
caterer| integer|   
cell_tower| integer|   
cement_manufacturer| integer|   
check_cashing_money| integer|   
chemicals| integer|   
chemicals_fertilizer| integer|   
circuit_board_manufa| integer|   
clothing| integer|   
clothing_mfg| integer|   
clubs_social_servi| integer|   
cold_storage| integer|   
collection| integer|   
comm_laund_dry_cln| integer|   
commercial| integer|   
commercial_airline| integer|   
commercial_storage| integer|   
computer_center| integer|   
contrctr_rntal_const| integer|   
copy_shop_printer| integer|   
costume_jewelry_stor| integer|   
credit_union_exempt| integer|   
credit_union_non_ex| integer|   
dairy_product_stores| integer|   
dairy_wholesale_only| integer|   
dance| integer|   
data_center| integer|   
delicatessen| integer|   
dental_laboratory| integer|   
dentist| integer|   
department_store| integer|   
dirt_sand_gravel| integer|   
doctor_osteopa_chiro| integer|   
drug_stores| integer|   
drugs_wholesale| integer|   
electrical| integer|   
electrical_supp_ret| integer|   
electricity_generati| integer|   
electronic_assembly| integer|   
electronic_manufactu| integer|   
electronic_recording| integer|   
electronics| integer|   
employment| integer|   
escrow_company| integer|   
exempt_lessor| integer|   
exterminator| integer|   
farm_equip_farming| integer|   
farm_heavy_equip_ret| integer|   
farming_nurseries| integer|   
feed_store| integer|   
fish_poultry_market| integer|   
fitness_center| integer|   
floors_blinds_bldg| integer|   
florist_shop| integer|   
florist_wholesale| integer|   
food_brokers| integer|   
food_drink_cart| integer|   
foods| integer|   
fractional_aircraft| integer|   
frosty_stand| integer|   
frozen_food_locker| integer|   
fuel_tank_farm| integer|   
furniture| integer|   
furniture_outdoor| integer|   
furniture_used| integer|   
furniture_unfinished| integer|   
gas_oil_plants| integer|   
gas_recovery| integer|   
general_building| integer|   
glass_paints_retail| integer|   
golf_carts| integer|   
golf_course| integer|   
grading_earth_moving| integer|   
grocery_stores| integer|   
hangars_portable| integer|   
hardware_retail| integer|   
hardware_electrical| integer|   
heating_air_conditio| integer|   
heavy_construction| integer|   
heavy_farm_equipment| integer|   
horse_571k| integer|   
horse_stables| integer|   
hospital| integer|   
hotel_furnishings| integer|   
ice_vending_boxes| integer|   
illuminated_signs| integer|   
institutional_exempt| integer|   
insurance_broker| integer|   
interior_decorating| integer|   
janitorial| integer|   
jewelers| integer|   
jewelry_mfg| integer|   
jewelry_store| integer|   
kennels| integer|   
laundry| integer|   
laundry_hand| integer|   
leased_equip_true_le| integer|   
linen_sup_pick_up_st| integer|   
liquor_store| integer|   
liquor_wholesale_dis| integer|   
lithographer| integer|   
loan_mortgage| integer|   
locksmith| integer|   
lodges| integer|   
low_income_housing| integer|   
lumber_building_supp| integer|   
lumber_retail| integer|   
machine_shop| integer|   
mailbox_center| integer|   
mailing_shipping_ser| integer|   
meat_department| integer|   
meat_wholesale_dist| integer|   
medical_hospital| integer|   
medical_laboratory| integer|   
metal_gas_cylinder| integer|   
metal_heavy_mfg| integer|   
metal_light_mfg| integer|   
mfg_heavy| integer|   
mfg_light| integer|   
milling_companies| integer|   
misc_technical_lab| integer|   
misc_amusement| integer|   
misc_broker| integer|   
misc_contractor| integer|   
misc_food_store| integer|   
misc_professional| integer|   
misc_school| integer|   
miscellaneous_agency| integer|   
miscellaneous_assoc| integer|   
mobile_home_park| integer|   
mobile_home_sales| integer|   
mobile_homes| integer|   
model_homes| integer|   
mortuary| integer|   
motel_furnishings| integer|   
motorcycle| integer|   
mower_welding_sml_re| integer|   
music| integer|   
music_recordings| integer|   
nail_shop| integer|   
new_furniture| integer|   
news_stand_cigar_sta| integer|   
non_race_horses| integer|   
nurseries_retail| integer|   
office_equipment| integer|   
offset| integer|   
optometrist| integer|   
packing_houses| integer|   
paper_products| integer|   
pawn_broker| integer|   
pay_phone_private| integer|   
pet_food_stores| integer|   
pet_store| integer|   
pharmacy| integer|   
photo_finishing| integer|   
photo_wholesale_dist| integer|   
plastering| integer|   
plastics_mfg| integer|   
plumbing| integer|   
plumbing_retail| integer|   
plumbing_wholesale_d| integer|   
pool_supplies| integer|   
portable_toilets| integer|   
pre_school_childcare| integer|   
printers_graphics| integer|   
printshops| integer|   
private_storage_reta| integer|   
propane_tnks_hq_supp| integer|   
public_agency| integer|   
public_storage| integer|   
publisher_news_magaz| integer|   
publisher_offices| integer|   
radio_station| integer|   
radio_tv_computers| integer|   
radio_tv_repair| integer|   
radiology_laboratory| integer|   
real_estate_develope| integer|   
recycler_collection| integer|   
religious_organizati| integer|   
rental_linens| integer|   
rest_home| integer|   
restaurant| integer|   
retail_warehouse| integer|   
roofing| integer|   
rug_cleaners| integer|   
scaffolding| integer|   
see_312| integer|   
see_501| integer|   
see_528| integer|   
self_serv_composite| integer|   
service| integer|   
service_station_mkts| integer|   
shoe_repair| integer|   
signs| integer|   
silk_screening| integer|   
smog_station| integer|   
software| integer|   
special_eq_plates| integer|   
specialty_hard_goods| integer|   
specialty_store_soft| integer|   
stationery| integer|   
stock_bond_broker| integer|   
supermarket| integer|   
supplies_stationery| integer|   
tailor| integer|   
television_rental| integer|   
television_stations| integer|   
theatre| integer|   
theme_parks| integer|   
ticket_travel| integer|   
tire_recapping| integer|   
tires_general_merch| integer|   
title_insurance_co| integer|   
trailer_camper| integer|   
trash_company| integer|   
truck_terminals| integer|   
tv_cable_company| integer|   
tv_radio_wholesale_d| integer|   
tv_station_digital| integer|   
typesetting| integer|   
union| integer|   
upholstery| integer|   
vending| integer|   
vet_animal_hosp| integer|   
veterinarian| integer|   
video_rentals| integer|   
watch_repair| integer|   
water_co_wells| integer|   
water_softener_co| integer|   
water_softener_serv| integer|   
winery| integer|   
wood_products_mfg| integer|   
woodwork_repair_shop| integer|   
wreckers| integer|   
  
## References

Urls used in the creation of this data package.

  * **[business_sites_source](<http://rdw.sandag.org/Account/GetFSFile.aspx?dir=Business&Name=BUSINESS_SITES.zip>)**. Source URL for BUSINESS_SITES file. You must be logged into Sangis to download it.
  * **metapack+http://library.metatab.org/sandiegodata.org-geography-2018-1.csv#tract_communities**. San Diego tracts
  * **metapack+http://library.metatab.org/sandiegodata.org-geography-2018-1.csv#tract_boundaries**. Tracts linked to community names


Last Modified 2019-06-13T04:38:22
