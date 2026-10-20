---
title: "San Diego Beachwatch Data, With Features"
date: 2019-05-15T22:33:42+00:00
draft: false
categories: ["Dataset"]
tags: ["ckan", "sandiegodata.org", "water-project"]
author: "metapack"
description: "Water quality data for San Diego county beaches from CEDEN, with added features"
---

_Water quality data for San Diego county beaches from CEDEN, with added features for log transformation, quantiles and group codes._

`sandiegodata.org-beachwatch-4`

Resources | Packages | Documentation| Contacts| References

## Resources

  * **[stations](<http://library.metatab.org/sandiegodata.org-beachwatch-4/data/stations.csv>)**. Measurement stations
  * **[measure_codes](<http://library.metatab.org/sandiegodata.org-beachwatch-4/data/measure_codes.csv>)**. Measurement group codes
  * **[beachwatch](<http://library.metatab.org/sandiegodata.org-beachwatch-4/data/beachwatch.csv>)**. Beachwatch data, with features added


## Documentation

This datasets rebuilds `ceden.waterboards.ca.gov-beachwatch-sandiego` with constant and null columns removed and many features added. It also breaks out station information into a seperate datasets, and enumerates the many difference combinations of methodname/analyte/unit, adding a code for each group to the dataset in `measure_code`. The measure code identifies sets of records that have compatible measurements.

The dataset adds counts, mean, median and quantiles for groups of station_code/measure_code. The dataset rows are grouped, for each station and measure code, and mean, median and quantiles computed for each group. The procedure is performed both for `result` and for `lresult`, the log of `results`. 

After computing the group summary statistics, the processing creates dichotomous features for the relationship of `result` and `lresult` to the summary value, including:

  * Greater than the median
  * Greater than the mean
  * Less than or equal to the 25th percentile
  * Greater than or equal to the 7th percentile


These variables are particularly useful for doing logistic regressions across the measure code groups or stations. 

# Elided Columns

This datasets excludes the const and empty columns from the source dataset. These columns and their values are:
[code] 
    program                      BeachWatch
    parentproject                BeachWatch_San Diego County
    project                      BeachWatch_San Diego County
    locationcode                 SurfZone
    collectiondepth              -88
    unitcollectiondepth          NR
    sampletypecode               Grab
    collectionreplicate          1
    resultsreplicate             1
    labsampleid                  Not Recorded
    matrixname                   samplewater
    mdl                          -88
    rl                           -88
    batchverification            NR
    compliancecode               NR
    eventcode                    WQ
    protocolcode                 Not Recorded
    collectionmethodname         Water_Grab
    collectiondevicedescription  Not Recorded
    calibrationdate              0000-00-00
    positionwatercolumn          Not Recorded
    preppreservationname         Not Recorded
    preppreservationdate         0000-00-00 00:00:00
    digestextractmethod          Not Recorded
    digestextractdate            0000-00-00
    analysisdate                 0000-00-00
    dilutionfactor               -88
    expectedvalue                0
    submissioncode               NR
    county                       San Diego
    county_fips                  73
    regional_board               San Diego
    rb_number                    9
    sampleid                     Not Recorded
    
[/code]

The dataset also excludes these Null columns:

  * observation
  * samplecomments
  * collectioncomments
  * resultscomments
  * batchcomments
  * groupsamples
  * occupationmethod
  * startingbank
  * distancefrombank
  * unitdistancefrombank
  * streamwidth
  * unitstreamwidth
  * stationwaterdepth
  * unitstationwaterdepth
  * hydromod
  * hydromodloc
  * locationdetailwqcomments
  * channelwidth
  * upstreamlength
  * downstreamlength
  * totalreach
  * locationdetailbacomments
  * huc8
  * huc8_number
  * huc10
  * huc10_number
  * huc12
  * huc12_number
  * waterbody_type


# Notes

The most prevalent measure code in this dataset is 24 for Enterococcus (analyte) meaured with Enterolert (methodname) in units of MPN/100 mL. This is probably because in 2004, the [EPA changed recomendations to use Enterococcus as a primary indicator bacteria in coastal waters:](<https://www.federalregister.gov/documents/2004/11/16/04-25303/water-quality-standards-for-coastal-and-great-lakes-recreation-waters>)
[code] 
    EPA subsequently recommended the use of E. coli or enterococci for fresh
    recreational waters and enterococci for marine recreational waters because
    levels of these organisms more accurately predict acute gastrointestinal
    illness than levels of fecal coliforms.
    
[/code]

### Documentation Links

  * [https://ceden.waterboards.ca.gov/AdvancedQueryTool](<source_page>)CEDEN advanced query tool page
  * [https://ceden.waterboards.ca.gov/Metadata/ControlledVocab.php](<controlled_vocab>)Controlled vocabulary search page
  * [https://ceden.waterboards.ca.gov/Metadata/get_lu_data.php?format=html&table=AnalyteLU&include_all=yes](<analyte_cv>)Analyte controlled vocabulary
  * [https://ceden.waterboards.ca.gov/Metadata/get_lu_data.php?format=html&table=MethodLU&include_all=yes](<method_cv>)Method controlled vocabulary
  * [https://ceden.waterboards.ca.gov/Metadata/get_lu_data.php?format=html&table=ResultQualityLU&include_all=yes](<result_qual_cv>)Result Qualifier controlled vocabulary
  * [https://ceden.waterboards.ca.gov/Metadata/get_lu_data.php?format=html&table=QA_LU&include_all=yes](<qa_cv>)QA controlled vocabulary


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **zip** <http://library.metatab.org/sandiegodata.org-beachwatch-4.zip>
  * **csv** <http://library.metatab.org/sandiegodata.org-beachwatch-3.csv>
  * **source** <https://github.com/san-diego-water-quality/water-datasets.git>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('http://library.metatab.org/sandiegodata.org-beachwatch-4.zip')
    # CSV Package
    pkg = mp.open_package('http://library.metatab.org/sandiegodata.org-beachwatch-3.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

## References

Urls used in the creation of this data package.

  * **index:ceden.waterboards.ca.gov-beachwatch-sandiego#beachwatch-sd**. Beachwatch source data


Last Modified 2018-08-10T22:40:33
