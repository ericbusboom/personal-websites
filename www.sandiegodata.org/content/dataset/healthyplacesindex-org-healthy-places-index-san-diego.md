---
title: "California Healthy Places Index"
date: 2019-06-12T22:09:47+00:00
draft: false
categories: ["build_environment", "Dataset", "planning", "planning-collection"]
tags: ["build_environment", "healthyplacesindex.org", "planning", "planning-collection", "planning-project"]
author: "metapack"
description: "The HPI provides overall scores and more detailed data on specific policy action"
---

_The HPI provides overall scores and more detailed data on specific policy action areas that shape health, like housing, transportation, education and more._

`healthyplacesindex.org-healthy_places_index-san_diego-4`


## Resources

  * **[hpi](<https://library-metatab-org.s3.amazonaws.com/healthyplacesindex.org-healthy_places_index-san_diego-4/data/hpi.csv>)**. Healthy Places Index master file


## Documentation

The Healthy Places Index is a collection of indicators produced by the Public Health Alliance of Southern California from a wide variety of data sources to study social determinants of health. It offers index values for many topics -- about 80 columns -- as well as a weighted aggreate index value, all at the tract level.

This version of the HPI presents the original file with only one modification: the Tiger format Geoid for tracts has been converted to ACS format.

### Documentation Links

  * Main Documentation. <https://library-metatab-org.s3.amazonaws.com/healthyplacesindex.org-healthy_places_index-san_diego-4/docs/HPI2Documentation2018-07-08-FINAL.pdf>Full technical documentation.
  * Project homepage. <https://healthyplacesindex.org/>Website for the HPI project


## Contacts

  * **Creator**

[Public Health Alliance of Southern California](<https://healthyplacesindex.org/>), [PHASoCal@PHI.org](<mailto:PHASoCal@PHI.org>)

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/healthyplacesindex.org-healthy_places_index-san_diego-4.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/healthyplacesindex.org-healthy_places_index-san_diego-4.csv>
  * **source** <https://github.com/sandiegodata/planning-database.git>


### Accessing Packages in Metapack
```
import metapack as mp
# ZIP Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/healthyplacesindex.org-healthy_places_index-san_diego-4.zip')
# CSV Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/healthyplacesindex.org-healthy_places_index-san_diego-4.csv') 

resource = pkg.resource('resource_name') # Get a resource
df = resource.dataframe() # Create a pandas Dataframe
gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
```

## Data Dictionary

hpi   


### hpi

Column Name| Data Type| Description  
---|---|---  
geoid| string| ACS format geoid  
pop2010| integer| total population of census tract in 2010  
pct2010gq| number| population in group quarters in 2010  
city| string| City associated with centroid of census tract  
zip| integer| 5-digit postal zip code  
county_fips| integer| 4-digit code of county  
county_name| string| Name of county  
urbantype| string| Census classification of urban type  
hpi2score| number| Total score of HPI  
hpi2_pctile_pos| number| Percentile ranking of HPI score (positive frame)  
hpi2_pctile_neg| number| Percentile ranking of HPI score (negative frame)  
hpi_top25pct| string| Top 25% most advantaged  
quintiles| integer| Quintile of HPI score  
quartiles| integer| Quartile of HPI score  
economic| number| Economic policy action area score, summed Z-scores of individual policy action area variables  
economic_pctile| number| Percentile ranking ranking of "economic" policy action area z score  
education| number| Education score, summed Z-scores of individual policy action area variables  
education_pctile| number| Percentile ranking of "education" policy action area z score  
housing| number| Housing policy action area score, summed Z-scores of individual policy action area variables  
houseing_pctile| number| Percentile ranking of "housing" policy action area z score  
healthcareaccess| number| Healthcare Access policy action area score, z-score of insurance variable  
healthcareaccess_pctile| number| Percentile ranking of "healthcare access" policy action area z score  
neighborhood| number| Neighborhood policy action area score, summed Z-scores of individual policy action area variables  
neighborhood_pctile| number| Percentile ranking of "neighborhood" policy action area z score  
pollution| number| Pollution ("Clean Environment") policy action area score, summed Z-scores of individual policy action area variables  
pollution_pctile| number| Percentile ranking of "pollution" policy action area z score  
transportation| number| Transportation policy action area score, summed Z-scores of individual policy action area variables  
transportation_pctile| number| Percentile ranking of "transportation" policy action area z score  
social| number| Social policy action area score, summed Z-scores of individual policy action area variables  
social_pctile| number| Percentile ranking of "social" policy action area z score  
insured| number| Percentage of adults aged 18 to 64 years currently insured  
insured_pctile| number| Percentile ranking of percentage of adults aged 18 to 64 years currently insured  
uncrowded| number| Percentage of households with less or equal to 1 occupant per room  
uncrowded_pctile| number| Percentile ranking of uncrowded households  
homeownership| number| Percentage of occupied housing units occupied by property owners  
homeownership_pctile| number| Percentile ranking of percentage of occupied housing units occupied by property owners  
automobile| number| Percentage of households with access to an automobile  
automobile_pctile| number| Percentile ranking of households with access to an automobile  
commute| number| Percentage of workers (16 years and older) who commute to work by transit, walking, or cycling  
commute_pctile| number| Percentile ranking of percentage of workers (16 years and older) who commute to work by transit, walking, or cycling  
inpreschool| number| Percentage of 3 and 4 year olds enrolled in school  
inpreschool_pctile| number| Percentile ranking of 3 and 4 year olds enrolled in school  
inhighschool| number| Percentage of 15-17 year olds enrolled in school  
inhighschool_pctile| number| Percentile ranking of 15-17 year olds enrolled in school  
bachelorsed| number| Percentage of population over age 25 with a bachelor's education or higher  
bachelorsed_pctile| number| Percentile ranking of percentage of population over age 25 with a bachelor's education or higher  
employed| number| Percentage of population aged 25-64 who are employed  
employed_pctile| number| Percentile ranking of population aged 25-64 who are employed  
abovepoverty| number| Percent of the population with an income exceeding 200% of federal poverty level  
abovepoverty_pctile| number| Percentile ranking of the population with an income exceeding 200% of federal poverty level  
income| integer| Median annual household income  
income_pctile| number| Percentile ranking of median annual household income  
retail| number| Gross retail, entertainment, and education employment density (jobs/acre) on unprotected land  
retail_pctile| number| Percentile ranking of employment density for retail, entertainment, and educational uses  
parkaccess| number| Percentage of the population living within a half-mile of a park, beach, or open space greater than 1 acre  
parkaccess_pctile| number| Percentile ranking of the population living within a half-mile of a park, beach, or open space greater than 1 acre  
treecanopy| number| Population-weighted percentage of the census tract area without tree canopy  
treecanopy_pctile| number| Percentile ranking of population-weighted percentage of the census tract area without tree canopy  
alcoffsale| number| Percent of Population beyond 1/4 Mile of Off-Sale Alcohol Outlets  
alcoffsale_pctile| number| Percentile ranking of the opulation within 1/4 Mile of Off-Sale Alcohol Outlets  
voting| number| Percentage of registered voters voting in the 2012 general election  
voting_pctile| number| Percentile ranking of registered voters voting in the 2012 general election  
ownsevere| number| Percent of low income owner households with housing costs exceeding 50% of income  
ownsevere_pctile| number| Percentile ranking of low income owner households with housing costs exceeding 50% of income  
rentsevere| number| Percent of low income renter households with housing costs exceeding 50% of income  
rentsevere_pctile| number| Percentile ranking of low income renter households with housing costs exceeding 50% of income  
houserepair| number| Percent of households with kitchen facilities and plumbing  
houserepair_pctile| number| Percentile ranking of the households with kitchen facilities and plumbing  
twoparents| number| Percentage of children in married-couple family households or one parent with unmarried partner family households  
twoparents_pctile| number| Percentile ranking of percentage of children in married-couple family households or one parent with unmarried partner family households  
supermkts| number| Percentage of the urban population residing less than 1/2 mile from a supermarket/large grocery store, or the percent of the rural population living less than 1 mile from a supermarket/large grocery store  
supermkts_pctile| number| Percentile ranking of percentage of the urban population residing less than 1/2 mile from a supermarket/large grocery store, or the percent of the rural population living less than 1 mile from a supermarket/large grocery store  
ozone| number| Mean of summer months (May-October) of the daily maximum 8-hour ozone concentration (ppm), averaged over three years (2012 to 2014).  
ozone_pctile| number| Percentile ranking of mean of summer months (May-October) of the daily maximum 8-hour ozone concentration (ppm), averaged over three years (2012 to 2014).  
pm25| number| Annual mean concentration of PM2.5 (average of quarterly means, μg/m3), over three years (2012 to 2014)  
pm25_pctile| number| Percentile ranking of annual mean PM 2.5 level  
dieselpm| number| Spatial distribution of gridded diesel PM emissions from on-road and non-road sources for a 2012 summer day in July (kg/day)  
dieselpm_pctile| number| Percentile ranking of spatial distribution of gridded diesel PM emissions from on-road and non-road sources for a 2012 summer day in July (kg/day)  
h20contam| number| Cal EnviroScreen 3.0 drinking water contaminant index for selected contaminants  
h20contam_pctile| number| Percentile ranking of Cal EnviroScreen 3.0 drinking water contaminant index for selected contaminants  
leb| number| Life Expectancy at Birth  
leb_pctile| number| Percentile ranking of life expectancy at birth  
white_pct| number| Percent of Whites in the total population  
black_pct| number| Percent of Blacks in the total population  
asian_pct| number| Percent of Asians in the total population  
latino_pct| number| Percent of Latinos in the total population  
multiple_pct| number| Percent of two or more races in the total population  
nativeam_pct| number| Percent of American Indian/Alaskan Natives in the total population  
pacificisl_pct| number| Percent of Native Hawaiians and other Pacific Islanders in the total population  
other_pct| integer| Percent of some other race in the total population  
version| string| Date file was created  
  
Last Modified 2019-01-03T22:49:49
