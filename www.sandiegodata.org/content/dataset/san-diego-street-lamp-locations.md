---
title: "San Diego Street Lamp Locations"
date: 2019-05-15T22:27:46+00:00
draft: false
categories: ["Dataset"]
tags: ["autogen", "sandiegodata.org"]
author: "metapack"
description: "Maps and geo data for the locations of San Diego streetlamps"
---

_Maps and geo data for the locations of San Diego streetlamps_

`sandiegodata.org-street_lamps-1`


## Resources

  * **[sandiego-light-distance.tiff](<https://s3.amazonaws.com/s3.sandiegodata.org/repo/clarinova.com/street_lights-casnd-429e-r1/sandiego-light-distance.tiff>)**. A GeoTIFF map of distances from a street lamp, in centimeters. The map is top coded, with the highest value being 12,000, or 120m.
  * **[street_lights.csv](<https://s3.amazonaws.com/s3.sandiegodata.org/repo/clarinova.com/street_lights-casnd-429e-r1/street_lights.csv>)**. Streetlight locations in CSV format.
  * **[styles.zip](<https://s3.amazonaws.com/s3.sandiegodata.org/repo/clarinova.com/street_lights-casnd-429e-r1/styles.zip>)**. QGIS colormap, spefically tuned for the GeoTIFF file


## Documentation

# San Diego Street Lamps

Street lamp locations, derived from SANGIS data. Note that the source file was [last updated](<http://rdw.sandag.org/file_store/Miscellaneous/Street_Light.pdf>) in June 2008, and there have been a few Street lamp-related projects since then. In particular, most of the lamps in the City of San Diego were converted to Induction in 2013, and there was a project in Kensington to add street lamps in 2012. 

So, this data should be used as a rough-guide to the locations of lamps, rather than definitive data. 

# Terms

This data is released under the following terms and conditions. 

Clarinova and the San Diego Regional Data Library disclaim any warranty for this data shall not be liable for loss or harm. [See the SDRDL Disclaimers and Limitations web page for complete details.](</get-data/data-disclaimers-and-limitations/>)

This data is based on data from SANGIS, which is subject to its own terms and conditions. See the [SANGIS Legal Notice for details](<http://www.sangis.org/Legal_Notice.htm>).

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@sandiegodata.org>), [San Diego Regional Data Library](</>)


## Packages

  * **source** <https://github.com/metatab-packages/sdrdl-data-repo.git>


Last Modified 2019-05-15T21:58:22
