---
title: "San Diego Beachwatch Data"
date: 2019-05-15T22:32:10+00:00
draft: false
categories: ["Dataset"]
tags: ["ceden.waterboards.ca.gov", "ckan", "natural-environment", "water-project"]
author: "metapack"
description: "Water quality data for San Diego county beaches."
---

_Water quality data for San Diego county beaches._

`ceden.waterboards.ca.gov-beachwatch-sandiego-2`


## Resources

  * **[beachwatch-sd](<https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-beachwatch-sandiego-2/data/beachwatch-sd.csv>)**. Beachwatch program for San Diego county


## Documentation

The Beachwatch data set has four bacteria measurements from 172 stations on the coast of San Diego county, from July 1998 to Decenber 2013. The four measurements are:

  * Coliform, Total 66992
  * Coliform, Fecal 65827
  * Enterococcus 65010
  * E. coli 4428


There are two units for the measurements: 

  * MPN/100 mL: "Most Probable Number"
  * cfu/100mL: "Colony forming units". Number of viable bacteria, excluding the dead ones. 


From [Cascade Analytical](<http://www.cascadeanalytical.com/resources-downloads/faqs>):
```
What does CFU and MPN mean? A: CFU stands for 'Colony Forming Units' and
refers to the number of viable bacterial cells in a sample per unit of
volume. For example: 50 CFU/100 mL means 50 Colony Forming Units per 100 mL
of sample. It is different from the direct microscopic counts that include
both dead and living cells.

MPN stands for 'Most Probable Number' and refers to a method that uses
dilution cultures and a probability calculation to determine the
approximate number of viable cells in a given volume of sample. It is
useful when samples contain too few organisms for agar plates to be used or
when organisms will not grow on agar. For example: 50 MPN/100 mL means that
the Most Probable Number of viable cells in 100 mL of sample is 50.
```

I haven't found traditional data dictionary documentation, [but there are controlled vocabulary lists](<http://ceden.org/CEDEN_checker/Checker/LookUpLists.php>) online for data submitters, which explain a lot of the columns.

### Documentation Links

  * [https://www.waterboards.ca.gov/water_issues/programs/beaches/beach_water_quality/beaches_program.html](<overview>)Project Overview Page
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

  * **csv** <https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-beachwatch-sandiego-2.csv>
  * **zip** <https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-beachwatch-sandiego-2.zip>
  * **source** <https://github.com/san-diego-water-quality/water-datasets.git>


### Accessing Packages in Metapack
```
import metapack as mp
# ZIP Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-beachwatch-sandiego-2.zip')
# CSV Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/ceden.waterboards.ca.gov-beachwatch-sandiego-2.csv') 

resource = pkg.resource('resource_name') # Get a resource
df = resource.dataframe() # Create a pandas Dataframe
gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
```

Last Modified 2018-08-09T14:59:01
