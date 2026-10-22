---
title: "Population Density Maps"
date: 2013-04-22T10:00:41+00:00
draft: false
categories: ["Analysis", "New Data", "Projects"]
author: "qaadmin"
---

Here is some eye candy, a population density map of Pacific Beach and surrounding neighborhoods. 

[![population-density-map](/uploads/7/2013/04/population-density-map-1024x931.jpg)](</uploads/7/2013/04/population-density-map.jpg>)

This map was created with a lot of Python code, using the 2010 census shapefiles for census blocks, setting a value for each block as the population of the block divided by the area of the block, and rasterizing all of the blocks to an image. Red indicates areas of higher population density. You can clearly pick out the areas in Pacific Beach that are zoned for apartments vs single family homes, the UTC high-rise apartment area, and many other variations in land use.

This map is a test of code I'm creating to allow any census variable to be mapped, but I'm not really happy with the result. The problem is that human brains like to see smooth variations in density, and the jaring discontinuities in this map are confusing. Some of the time, the abrupt changes in density is connected to changes in land use, since census boundaries tend to follow streets, but most of the time what map users are really more interested in is how people respond to density, and in those cases, human movements and behaviors don't follow sharp boundaries.

To address this issue, I will be converting these maps into the same grid structure that we use for crime maps and smoothing across the grid cells to remove the discontinuities. These modified maps won't show the population density with the same accuracy, but they will be easier for people to interpret in ways that are relevant to their real interests in population density.
