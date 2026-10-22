---
title: "International Administrative Boundaries"
date: 2021-07-12T20:12:44+00:00
draft: false
categories: ["Dataset", "sez"]
tags: ["berkeley.edu/", "sez", "special_economic_zones"]
author: "metapack"
description: "Geographic boundaries of second-level administrative regions for countries that"
---

_Geographic boundaries of second-level administrative regions for countries that have a lot of special economic zones._

`berkeley.edu-administrative_boundaries-1.1.1`. Modified 2021-07-12T20:47:26


## Resources

  * **[vietnam_political](<https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/vietnam_political.csv>)**. Adminstrative boundaries of Vietnam, 2007
  * **[china_city](<https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/china_city.csv>)**. City Boundaries of China, 2012
  * **[skorea_admin2](<https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/skorea_admin2.csv>)**. Second-level Administrative Divisions, South Korea, 2015
  * **[china_admin2](<https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/china_admin2.csv>)**. Second-level Administrative Divisions, China, 2015
  * **[vietnam_admin2](<https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/vietnam_admin2.csv>)**. Second-level Administrative Divisions, Vietnam, 2015
  * **[turkey_admin2](<https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/turkey_admin2.csv>)**. Second-level Administrative Divisions, Turkey, 2015
  * **[philippines_admin2](<https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/philippines_admin2.csv>)**. Second-level Administrative Divisions, Philippines, 2015
  * **[indonesia_admin2](<https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/indonesia_admin2.csv>)**. Second-level Administrative Divisions, Indonesia, 2015
  * **[colombia_admin2](<https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/colombia_admin2.csv>)**. Second-level Administrative Divisions, Colombia, 2015


## Documentation

A collection of second level administrative boundaries, by country, for a select group of countries ( the countries that have the most special exconomic zones. ) 

The China city boundaries file was loaded into QGis from Berkeley's Web Feature Service, then saved as CSV with WKT geometries, but the rest are direct links to Berkeley's geographic file store.

# Licenses and Descriptions

Many of the dataset included in this package have use restrictions that are described on the download page on Berkeley's repository. 

## City Boundaries, China, 2012

Author(s): All China Marketing Research Co., Ltd. Description: This polygon dataset represents city boundaries in China from 2012. The attribute table includes the GB codes and names in Chinese and English (Pinyin). All data is copyrighted by China Data Center and/or its suppliers. Derived works that include the source data must be merged with other value-added data in such a way that the derived work cannot be converted back to the original source data format. This data is licensed by UC Berkeley for research, educational, and other non-commercial use by authorized users, which include persons affiliated with UC Berkeley and walk-in users who must access the data in person at the library.The data sources for the layers in the collection "Administrative Boundary Maps of China, 1949-2014" include the following primary sources: “The Historical Changes of Administrative Regions of China, 1949-1983” (three volumes); 《中华人民共和国县级以上行政区沿革》（三册，1949-1983年）“The Atlas of Changes of Administrative Regions of China”;《中华人民共和国行政区划沿革地图集》The yearly publications of “The Administrative Regions”, 1985-2014; 每年的出版行政区划简册（1985-2014年）The web site for administrative regions: www.xzqh.org; 行政区划网www.xzqh.org

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/index.html>)
  * [China city Boundaries](<https://geodata.lib.berkeley.edu/catalog/berkeley-s7b12n>) Data repository page for China Boundaries, 2012
  * [Vietnam Political Boundaries](<https://geodata.lib.berkeley.edu/catalog/sde-columbia-iscgm_vietnam_2007_polbndl>) Data repository page for Vietnam Boundaries, 2008
  * [Vietnam administrative divisions](<https://geodata.lib.berkeley.edu/catalog/stanford-zq121fy4008>) Second-level Administrative Divisions, Vietnam, 2015
  * [China Administrative Divisions](<https://geodata.lib.berkeley.edu/catalog/stanford-nt024fn0432>) Second-level Administrative Divisions, China, 2015
  * [South Korea administrative boundaries](<https://geodata.lib.berkeley.edu/catalog/stanford-dp437fd4983>) Data repository page for Second-level Administrative Divisions, South Korea, 2015
  * [Turkey administrative divisions](<https://geodata.lib.berkeley.edu/catalog/stanford-nj696zj1674>) Second-level Administrative Divisions, Turkey, 2015
  * [Philipines administrative divisions](<https://geodata.lib.berkeley.edu/catalog/stanford-mw379pp5559>) Second-level Administrative Divisions, Philippines, 2015
  * [Indonesia administrative divisions](<https://geodata.lib.berkeley.edu/catalog/stanford-hq794hx9239>) Second-level Administrative Divisions, Indonesia, 2015


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

vietnam_political | china_city | skorea_admin2 | china_admin2 | vietnam_admin2 | turkey_admin2 | philippines_admin2 | indonesia_admin2 | colombia_admin2   


### vietnam_political

Column Name| Data Type| Description  
---|---|---  
id| integer|   
f_code| string|   
f_code_des| string|   
acc| integer|   
acc_descri| string|   
use| integer|   
use_descri| string|   
soc| string|   
tile_id| integer|   
edg_id| integer|   
geometry| string|   
  
### china_city

Column Name| Data Type| Description  
---|---|---  
geometry| string|   
dcode| integer|   
city_ch| text|   
city_en| text|   
pcode| integer|   
prov_ch| text|   
prov_en| string|   
  
### skorea_admin2

Column Name| Data Type| Description  
---|---|---  
id| integer|   
id_0| integer|   
iso| string|   
name_0| string|   
id_1| integer|   
name_1| string|   
id_2| integer|   
name_2| string|   
hasc_2| unknown|   
ccn_2| integer|   
cca_2| unknown|   
type_2| string|   
engtype_2| string|   
nl_name_2| text|   
varname_2| string|   
geometry| string|   
  
### china_admin2

Column Name| Data Type| Description  
---|---|---  
id| integer|   
id_0| integer|   
iso| string|   
name_0| string|   
id_1| integer|   
name_1| string|   
id_2| integer|   
name_2| text|   
hasc_2| unknown|   
ccn_2| integer|   
cca_2| unknown|   
type_2| text|   
engtype_2| string|   
nl_name_2| text|   
varname_2| text|   
geometry| string|   
  
### vietnam_admin2

Column Name| Data Type| Description  
---|---|---  
id| integer|   
id_0| integer|   
iso| string|   
name_0| string|   
id_1| integer|   
name_1| text|   
id_2| integer|   
name_2| text|   
hasc_2| string|   
ccn_2| integer|   
cca_2| unknown|   
type_2| text|   
engtype_2| string|   
nl_name_2| unknown|   
varname_2| text|   
geometry| string|   
  
### turkey_admin2

Column Name| Data Type| Description  
---|---|---  
id| integer|   
id_0| integer|   
iso| string|   
name_0| string|   
id_1| integer|   
name_1| text|   
id_2| integer|   
name_2| text|   
hasc_2| string|   
ccn_2| integer|   
cca_2| unknown|   
type_2| string|   
engtype_2| string|   
nl_name_2| unknown|   
varname_2| text|   
geometry| string|   
  
### philippines_admin2

Column Name| Data Type| Description  
---|---|---  
id| integer|   
id_0| integer|   
iso| string|   
name_0| string|   
id_1| integer|   
name_1| string|   
id_2| integer|   
name_2| text|   
hasc_2| string|   
ccn_2| integer|   
cca_2| integer|   
type_2| string|   
engtype_2| string|   
nl_name_2| unknown|   
varname_2| text|   
geometry| string|   
  
### indonesia_admin2

Column Name| Data Type| Description  
---|---|---  
id| integer|   
id_0| integer|   
iso| string|   
name_0| string|   
id_1| integer|   
name_1| string|   
id_2| integer|   
name_2| string|   
hasc_2| string|   
ccn_2| integer|   
cca_2| unknown|   
type_2| string|   
engtype_2| string|   
nl_name_2| unknown|   
varname_2| string|   
geometry| string|   
  
### colombia_admin2

Column Name| Data Type| Description  
---|---|---  
id| integer|   
id_0| integer|   
iso| string|   
name_0| string|   
id_1| integer|   
name_1| text|   
id_2| integer|   
name_2| text|   
hasc_2| string|   
ccn_2| integer|   
cca_2| unknown|   
type_2| string|   
engtype_2| string|   
nl_name_2| unknown|   
varname_2| text|   
geometry| string|   
  
## Packages

  * **s3** s3://library.metatab.org/berkeley.edu-administrative_boundaries-1.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1.csv>
  * **source** <https://github.com/sandiegodata-projects/chartercitiesinstitute.org-sez>


### Accessing Data in Vanilla Pandas
```
import pandas as pd


vietnam_political_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/vietnam_political.csv')
china_city_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/china_city.csv')
skorea_admin2_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/skorea_admin2.csv')
china_admin2_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/china_admin2.csv')
vietnam_admin2_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/vietnam_admin2.csv')
turkey_admin2_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/turkey_admin2.csv')
philippines_admin2_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/philippines_admin2.csv')
indonesia_admin2_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/indonesia_admin2.csv')
colombia_admin2_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1/data/colombia_admin2.csv')
```

### Accessing Package in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/berkeley.edu-administrative_boundaries-1.1.1.csv')

# Create Dataframes
vietnam_political_gdf = pkg.resource('vietnam_political').geoframe()
china_city_gdf = pkg.resource('china_city').geoframe()
skorea_admin2_gdf = pkg.resource('skorea_admin2').geoframe()
china_admin2_gdf = pkg.resource('china_admin2').geoframe()
vietnam_admin2_gdf = pkg.resource('vietnam_admin2').geoframe()
turkey_admin2_gdf = pkg.resource('turkey_admin2').geoframe()
philippines_admin2_gdf = pkg.resource('philippines_admin2').geoframe()
indonesia_admin2_gdf = pkg.resource('indonesia_admin2').geoframe()
colombia_admin2_gdf = pkg.resource('colombia_admin2').geoframe()
```
