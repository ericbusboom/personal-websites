---
title: "Day/Time Crime Heatmaps"
date: 2013-12-21T11:23:02+00:00
draft: false
categories: ["Analysis"]
author: "qaadmin"
---

Here is an interactive data application that explores how crime incidents vary over the day of week and time of day. In the checkbox below, select one or more crime types, and the heatmap will show the relative intensity of those crime types over day of week and time of day.  There many interesting patterns here, some you would expect, some you might not: Things you might expect: 

  * DUI and Drugs violations are primarily committed in the evening and early mornings on weekends.
  * Assaults are most frequent in the late evenings and early mornings on weekends.
  * Vehicle theft and break-ins are committed in the dark.
  * Burglary is committed during the day, while people are at work.

There are also a few interesting surprises: 
  * Sex crimes, which are mostly prostitution, peak on Thursday evenings.
  * Homicides are spread throughout the week. Rather than being tied to nightlife.
  * Fraud occurs almost entirely at noon or midnight. This is almost certainly a data-collection issue, not the actual time the crimes occurred.
  * Weapons violations, however, are primarily in the middle of the week.

This sort of heatmap is a really powerful way to visualize complex relationships quickly, although it also hides a lot of other interesting features. For instance, crime varies considerably by location, so a valuable extension of this analysis would be to include checkboxes for selecting neighborhoods. This application was built using R and Shiny. If you'd like to learn to develop this sort of application for your own site, the Library is considering running a training class. [If you are interested, let us know.](</about/contact/> "Contact")
