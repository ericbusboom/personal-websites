---
title: "San Diego County Parcel Rasters"
date: 2019-05-15T22:27:36+00:00
draft: false
categories: ["Dataset"]
tags: ["autogen", "sangis.org"]
author: "metapack"
description: "Raster maps of Assessor's tax zone, from the azr_zone field of the original"
---

_Raster maps of Assessor's tax zone, from the azr_zone field of the original dataset, rasterized to 10m cells._

`sangis.org-parcels-1`


## Resources

  * **[images.zip](<https://s3.amazonaws.com/s3.sandiegodata.org/repo/clarinova.com/parcels-casd-7ba4-r1/images.zip>)**. Raster maps of Assessor's tax zone, from the azr_zone field of the original dataset, rasterized to 10m cells.


## Documentation

Parcels, linked to communities and groups by land use. (more...)

San Diego County parcels, from the SANGIS.org shape files, with improved data structure. 

# Images

The Images zip file includes raster maps, two for each incorporated city, with the Assessor's tax zone -- from the asr_zone field in the original SANGIS files -- assigned to 10m square cells. Since there are no parcels for roads and other areas, there are two versions of each image. The '-base' version is rasterized directly from the parcels, and has no data over roads and other areas that have an asr_zone of 0. The '-infill' version fills in cells that have a value of 0 in the '-base' version with the value of the nearest non-zero cell. These files are particularly useful for use with point data that is assigned to streets, where there otherwise would be no values. 

# City, District and Community Codes

In the source datasets ( not included in the repository, but available in the the databundle library ) Four of the fields use custom codes to identify geographic regions: 

  * neighborhood/nbrhood
  * community
  * council
  * city


These fields use [Clarinova Place Codes](<https://sandiegodata.atlassian.net/wiki/display/SDD/Clarinova+Place+Codes>), 6 character codes that are designed to be memorable and unambiguous. See the [place codes Google spreadsheet](<https://docs.google.com/a/clarinova.com/spreadsheet/ccc?key=0AhnSJoCKXnSUdE1SMXVDYzBGYjVXX3kwUkRBUi1NaHc#gid=0>) for a list all of the codes. 

# Citation

_Name of file_ , extracted from clarinova.com-parcels-casd-7ba4. San Diego Regional Data Library. 2013-07-18 /

# Terms

This data is released under the following terms and conditions. [See the SDRDL Disclaimers and Limitations web page for complete details.](</get-data/data-disclaimers-and-limitations/>)

This data is based on data from SANGIS, which is subject to its own terms and conditions. See the [SANGIS Legal Notice for details](<http://www.sangis.org/Legal_Notice.htm>). 

This data is based on data from SANDAG, which is subject to its own terms and conditions. See the [SANDAG Legal Notice for details](<http://rdw.sandag.org/m>).

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@sandiegodata.org>), [San Diego Regional Data Library](</>)


## Packages

  * **source** <https://github.com/metatab-packages/sdrdl-data-repo.git>


Last Modified 2019-05-15T21:58:22
