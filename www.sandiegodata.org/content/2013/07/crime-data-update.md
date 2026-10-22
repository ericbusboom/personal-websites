---
title: "Crime Data Update"
date: 2013-07-24T09:41:47+00:00
draft: false
categories: ["New Data"]
author: "qaadmin"
---

We've released an update to the crime dataset today. This update is based on reprocessed data from SANDAG and includes some new fields. 

[San Diego Crime Incidents, Revision 3](</dataset/>)

This update is based on a new extract of the data we got recently from SANDAG. They didn't tell me what had changed, just that they found some problems and re-ran the extract. If you want to compare the inputs, we have both the [first revision](</dataset/>) and [second revision ](</dataset/>)of the SANDAG input data in the data repository. This release includes several new fields in the CSV and Shapefiles, including 

  * is_night: 1 means that the incident time is at night, between dusk and dawn, accounting for changing seasons and daylight savings time.
  * asr_zone: The assessor's code for land use. It differentiates commercial, residential and industrial lands
  * lampdist: distance to the nearest streetlamp, in centimeters.

This release also groups all of the individual CSV and Shapefiles into single Zip archives, to make it easier to download all of the files in a set at once. If you are using this data, or would like to see additional fields in the dataset, let me know: eric@sandiegodata.org.
