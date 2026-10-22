---
title: "SANGIS Census Regions"
date: 2019-05-15T22:34:21+00:00
draft: false
categories: ["Dataset"]
tags: ["age-friendly-communities", "built_environment", "ckan"]
author: "metapack"
description: "San Diego county Tracts, MSAs and SRAs, based on 2010 Census boundaries, as extracted by SANGIS."
---

_San Diego county Tracts, MSAs and SRAs, based on 2010 Census boundaries, as extracted by SANGIS._

`OrderedDict([('dataset', 'census-regions'), ('time', '2010'), ('version', '4'), ('space', 'sandiego'), ('origin', 'sangis.org'), ('@value', 'sangis.org-census_regions-2010-sandiego-4')])`

Resources | Packages | Documentation| Contacts

## Resources

  * **[tracts](<https://library-metatab-org.s3.amazonaws.com/sangis.org-census_regions-2010-sandiego-4/data/tracts.csv>)**. 2010 Census Tract boundaries
  * **[msa](<https://library-metatab-org.s3.amazonaws.com/sangis.org-census_regions-2010-sandiego-4/data/msa.csv>)**. 2010 Metro Statistical Area boundaries
  * **[sra](<https://library-metatab-org.s3.amazonaws.com/sangis.org-census_regions-2010-sandiego-4/data/sra.csv>)**. San Diego County Sub-Regional Areas boundaries
  * **[zip](<https://library-metatab-org.s3.amazonaws.com/sangis.org-census_regions-2010-sandiego-4/data/zip.csv>)**. ZIP Code boundaries
  * **[tract-sra-msa-xwalk](<https://library-metatab-org.s3.amazonaws.com/sangis.org-census_regions-2010-sandiego-4/data/tract-sra-msa-xwalk.csv>)**. Crosswalk between crosswalks, tracts, zip codes and SRAs.


## Documentation

### Documentation Links

  * [docs/tracts-sras-and-msaa](<Tracts, SRAs and MSAa>)Overview of how SRAs are composed of tracts and related to MSAs.


## Contacts

  * **Origin**

[SANGIS](<sangis.org>)

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **xlsx** <https://library-metatab-org.s3.amazonaws.com/sangis.org-census_regions-2010-sandiego-4.xlsx>
  * **zip** <https://library-metatab-org.s3.amazonaws.com/sangis.org-census_regions-2010-sandiego-4.zip>
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sangis.org-census_regions-2010-sandiego-4.csv>


### Accessing Packages in Metapack
[code] 
    import metapack as mp
    # ZIP Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sangis.org-census_regions-2010-sandiego-4.zip')
    # CSV Package
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sangis.org-census_regions-2010-sandiego-4.csv') 
    
    resource = pkg.resource('resource_name') # Get a resource
    df = resource.dataframe() # Create a pandas Dataframe
    gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
    
[/code]

Last Modified 2017-04-03T20:16:31
