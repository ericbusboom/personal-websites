---
title: "Homelessness Risk Tutorial"
date: 2019-07-05T20:28:13+00:00
draft: false
categories: ["Dataset", "homelessness"]
tags: ["arcgis.com", "homelessness", "los_angeles"]
author: "metapack"
description: "Data related to homelessness from an ArcGIS tutorial"
---

_Data related to homelessness from an ArcGIS tutorial_

`arcgis.com-risk-3`

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[resources](<https://library-metatab-org.s3.amazonaws.com/arcgis.com-risk-3/data/resources.csv>)**. Homeless population, crime, and 311 calls by tract and community.
  * **[county_outline](<https://library-metatab-org.s3.amazonaws.com/arcgis.com-risk-3/data/county_outline.csv>)**. County bountry outline
  * **[shelters_services](<https://library-metatab-org.s3.amazonaws.com/arcgis.com-risk-3/data/shelters_services.csv>)**. Locations and basic information for shelters and other services
  * **[homeless_population](<https://library-metatab-org.s3.amazonaws.com/arcgis.com-risk-3/data/homeless_population.csv>)**. Detailed homeless population data per tract.
  * **[risk_factors](<https://library-metatab-org.s3.amazonaws.com/arcgis.com-risk-3/data/risk_factors.csv>)**. Tract level neighborhood risk factors, probably from teh American Community Survey


## Documentation

ESRI [publishes a tutorial for creating maps for analyzing homelesness](<http://desktop.arcgis.com/en/analytics/case-studies/la-county-homel
essness-2-pro-workflow.htm>), with a link to the data used. Many of the data are from lahsa.org and economicrt.org, but the package also includes many other columns. The data download includes a .gdb file, which includes no documentation, although there may be documentation in the HomelessnessPkg.ppkx file.

For this data package, the files from the .gdb database have been converted to GeoJSON, to be imported into the package.

The files are interesting, but poorly documented and of unknown provenance, so probably should only be used for tutorials and demonstrations. Some information about the dataset can be inferred from an [ESRI Homelessness Story Map](<https://eath.maps.arcgis.com/apps/Cascade/index.html?appid=0c56e846dacb4663926cdbc8570ea4f6>), which appears to use these datasets.

### Documentation Links

  * [Tutorial](<http://desktop.arcgis.com/en/analytics/case-studies/la-county-homelessness-2-pro-workflow.htm>)Tutorial web page
  * [Combating Homelessness in Los Angeles County](<https://eath.maps.arcgis.com/apps/Cascade/index.html?appid=0c56e846dacb4663926cdbc8570ea4f6>)Homelessness story map


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/arcgis.com-risk-3.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/arcgis.com-risk-3.csv>
  * **source** <https://github.com/SDRDLAnalysts/data-projects.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/arcgis.com-risk-3.zip')
    
    # Create Dataframes
    resources_gdf = pkg.resource('resources').geoframe()
    county_outline_gdf = pkg.resource('county_outline').geoframe()
    shelters_services_gdf = pkg.resource('shelters_services').geoframe()
    homeless_population_gdf = pkg.resource('homeless_population').geoframe()
    risk_factors_gdf = pkg.resource('risk_factors').geoframe()
    
[/code]

## Data Dictionary

resources | county_outline | shelters_services | homeless_population | risk_factors   


### resources

Column Name| Data Type| Description  
---|---|---  
id| integer|   
objectid| integer|   
tract| integer|   
uniqid| integer|   
totpop_cy| integer|   
totunsheltpeople| number|   
totsheltpeople| integer|   
totpeople| number|   
community| text|   
victimcount| integer|   
callcnt311| integer|   
chronic| integer|   
shape_length| number|   
shape_area| number|   
geometry| string|   
  
### county_outline

Column Name| Data Type| Description  
---|---|---  
id| integer|   
objectid| integer|   
shape_length| number|   
shape_area| number|   
geometry| string|   
  
### shelters_services

Column Name| Data Type| Description  
---|---|---  
id| integer|   
objectid| integer|   
source| integer|   
cat1| string|   
cat2| string|   
org_name| string|   
name| string|   
addrln1| string|   
addrln2| string|   
city| string|   
state| string|   
hours| string|   
phones| string|   
url| string|   
post_id| integer|   
description| text|   
zip| integer|   
link| string|   
use_type| string|   
latitude| number|   
longitude| number|   
date_updated| datetime|   
point_x| number|   
point_y| number|   
geometry| string|   
  
### homeless_population

Column Name| Data Type| Description  
---|---|---  
id| integer|   
objectid| integer|   
tract| integer|   
uniqid| integer|   
totpop_cy| integer|   
totunsheltpeople| integer|   
totsheltpeople| integer|   
totpeople| integer|   
poly_area| number|   
popdensity| number|   
homelesspopdensity| number|   
unsheltereddensity| number|   
sheltereddensity| number|   
community| text|   
indfamcvc| integer|   
pindfamcvc| number|   
indfamte| integer|   
pindfamte| number|   
onstreet| integer|   
ponstreet| number|   
indfamesthsh| integer|   
pindfamesthsh| number|   
vets| integer|   
chronic| integer|   
addicted| number|   
braininjury| number|   
smi| number|   
hivaids| number|   
devdis| number|   
phydis| number|   
domviol| number|   
under18| number|   
over62| number|   
amerind| number|   
asian| number|   
black| number|   
hispanic| number|   
pacislalaskan| number|   
white| number|   
male| number|   
female| number|   
transgender| number|   
shape_length| number|   
shape_area| number|   
geometry| string|   
  
### risk_factors

Column Name| Data Type| Description  
---|---|---  
id| integer|   
objectid| integer|   
tract| integer|   
uniqid| integer|   
acshhbpov| integer|   
pacshhbpov| number|   
changehhinpoverty| integer|   
acspubai| integer|   
ppublicassistanceinc| number|   
changehhpubassist| integer|   
acshhdis| integer|   
pdisabilities| number|   
acsgrnti50| integer|   
p50hhinc4rent| number|   
changehhs50pinc4rent| integer|   
unemp_cy| integer|   
unemprt_cy| number|   
changeunemprate| number|   
nohealthins| integer|   
pnohealthins| number|   
est_veteran_ptsd| number|   
ptsdvets| integer|   
estsmi| integer|   
pestsmi| number|   
subabuse| integer|   
psubabuse| number|   
domviol| integer|   
pdomviolrate| number|   
totpop_cy| integer|   
shape_length| number|   
shape_area| number|   
geometry| string|   
  
## References

Urls used in the creation of this data package.

  * **[Data package](<http://www.arcgis.com/sharing/rest/content/items/21fca68ca0564ba6b344ee36c594025b/data>)**. Data package included in the tutorial.


Last Modified 2019-07-17T00:49:01

## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/arcgis.com-risk-3.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/arcgis.com-risk-3.csv>
  * **source** <https://github.com/SDRDLAnalysts/data-projects.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/arcgis.com-risk-3.zip')
    
    # Create Dataframes
    resources_gdf = pkg.resource('resources').geoframe()
    county_outline_gdf = pkg.resource('county_outline').geoframe()
    shelters_services_gdf = pkg.resource('shelters_services').geoframe()
    homeless_population_gdf = pkg.resource('homeless_population').geoframe()
    risk_factors_gdf = pkg.resource('risk_factors').geoframe()
    
[/code]
