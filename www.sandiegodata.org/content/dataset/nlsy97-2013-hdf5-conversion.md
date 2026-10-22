---
title: "NLSY97 2013 HDF5 Conversion"
date: 2019-05-15T22:33:14+00:00
draft: false
categories: ["Dataset"]
tags: ["ckan", "nlsinfo.org"]
author: "metapack"
description: "The NLSY97 as an HDF5  file"
---

_The NLSY97 as an HDF5 file_

`nlsinfo.org-nlsy97-2013-1`


## Documentation

This datapackage links to a HDF5 conversion of the NLSY97, with responses to 2013. 

Because the HDF file is very large and complex to produce, this package links to the file on the web. The file was produces external to the package. 

This is much more complicated to use than other files. The `publicdata` python package must be installed to get the Nlsy classes that can read the HDF5 file. Typical useage is: 
```
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/nlsinfo.org-nlsy97-2013.csv')
nlsy = pkg.reference('nlsy97').resolved_url.get_resource().get_target().nlsy
homeless = nlsy.question_dataframe('YHEA-2600A',  replacena=True, rmeta=True)
homeless.head()
```

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Packages

  * **csv** <https://library-metatab-org.s3.amazonaws.com/nlsinfo.org-nlsy97-2013-1.csv>
  * **source** <https://github.com/SDRDLAnalysts/data-projects.git>


### Accessing Packages in Metapack
```
import metapack as mp

# CSV Package
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/nlsinfo.org-nlsy97-2013-1.csv') 

resource = pkg.resource('resource_name') # Get a resource
df = resource.dataframe() # Create a pandas Dataframe
gdf = resource.geoframe() # Create a GeoPandas GeoDataFrame
```

## References

Urls used in the creation of this data package.

  * **nlsy+https://library-metatab-org.s3.amazonaws.com/nlsinfo.org-nlsy97-2013/data/nlsy97_all_1997-2013.h5.zip**. NLSY 97 HDF5 file


Last Modified 2019-04-18T18:41:54
