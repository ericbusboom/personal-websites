---
title: "Crime Data Heatmaps"
date: 2013-01-01T14:12:03+00:00
draft: false
categories: ["Uncategorized"]
author: "qaadmin"
---

A heat map is a way of presenting data that makes it much easier to understand the density of a variable. Rather than just plotting each pont on a map, a point on a heatmap adds a bit of 'temperature' to a location, so a lot of points close together make an area "hotter". There are several ways of constructing heatmaps, but they all generally represent the areal density of a variable, and when the viewer is most concerned with density, they are the best representation. For instance, here is a typical crime map, showing an icon for each crime incident: [![Crime map from Crimedata.com](/uploads/12/2013/01/Screen-Shot-2013-01-01-at-1.53.59-PM-300x189.png)](<http://www.sandiegodata.org/2013/01/crime-data-heatmaps/screen-shot-2013-01-01-at-1-53-59-pm/>) Crime map from Crimedata.com While this map is useful for determining what crime incidents may have been recorded near a particular address, the size of the icons obscures the variation in incident density. Here is a map of the same area, from the [Trulia Crime Maps](<http://www.trulia.com/crime/#!san-diego-ca/14/32.79498,-117.23851/Pacific_Beach,CA,Mission_Beach/> "Trulia Crime Maps") website, presented as a heat map: [![Heat map of Pacific Beach, from Trulia.com](/uploads/12/2013/01/Screen-Shot-2013-01-01-at-1.57.49-PM-300x193.png)](<http://www.sandiegodata.org/2013/01/crime-data-heatmaps/screen-shot-2013-01-01-at-1-57-49-pm/>) Heat map of Pacific Beach, from Trulia.com The heat map isn't useful for getting information about a particular incident, but it is a much better representation of where crime is happening, in this case, clustered around bars and the beach, while few incident are occurring in the residential areas. This [crime heat map of London](<http://oobrien.com/vis/crime/>) allows you to adjust the radius that each crime incident contributed to the map, as well of intensity of the event, so you can get a sense for how those parameters work. If you'd like to generate your own heat maps, many GIS programs can create them, and heat maps are increasingly common in web-based mapping services. Here are a few online services you might try: 

  * [HeatCanvas](<https://github.com/openplans/heatcanvas>), heatmap library for HTML5 canvas
  * [gheat](<http://code.google.com/p/gheat/>), an open source program that works with google maps.
  * [PyHeat](<https://github.com/amccollum/pyheat>), a similar program for the Python language.
  * [Open Heat Maps](<http://www.openheatmap.com/>), a free web service.
  * [Heat Map Too](<http://www.heatmaptool.com/>)l, a commercial web service.
  * [Heat Map Api](<http://www.heatmapapi.com/>), a commercial service, although it has a free tier.
