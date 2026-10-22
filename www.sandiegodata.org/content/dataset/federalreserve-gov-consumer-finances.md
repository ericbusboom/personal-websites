---
title: "Survey of Consumer Finances"
date: 2020-07-27T22:33:49+00:00
draft: false
categories: ["Dataset"]
tags: ["federalreserve.gov"]
author: "metapack"
description: "References to the Survey of Consumer Finances"
---

_References to the Survey of Consumer Finances_

`federalreserve.gov-consumer_finances-1.2.4`. Modified 2020-12-22T22:08:50


## Documentation

The data package provides references to the main SCF files. The package does not contain data. 

  * [How Does Intergenerational Wealth Transmission Affect Wealth Concentration? ](<https://www.federalreserve.gov/econres/notes/feds-notes/how-does-intergenerational-wealth-transmission-affect-wealth-concentration-20180601.htm>)
  * [The Dynamics of the Racial Wealth Gap](<http://www.people.virginia.edu/~ey2d/aliprantis_carroll_young_2019b.pdf>)


Feiveson and Sabelhaus calculate that 26% of welath is due to transfers, because they assume that all of the transfer is invested at 3%. THis is clearly nonsense0

### Documentation Links

  * [2019 Codebook](<https://www.federalreserve.gov/econres/files/codebk2019.txt>)
  * [2016 Codebook](<https://www.federalreserve.gov/econres/files/codebk2016.txt>)
  * [2016 Extract SAS Macro](<https://www.federalreserve.gov/econres/files/bulletin.macro.txt>)
  * [2013 Codebook](<https://www.federalreserve.gov/econres/files/codebk2013.txt>)
  * [2013 Extract SAS Macro](<https://www.federalreserve.gov/econres/files/bulletin.macro.txt>)
  * [2010 Codebook](<https://www.federalreserve.gov/econres/files/codebk2010.txt>)
  * [2010 Extract SAS Macro](<https://www.federalreserve.gov/econres/files/bulletin.macro.txt>)
  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances-1.2.4/index.html>)
  * [Homepage](<https://www.federalreserve.gov/econres/scfindex.htm>)
  * [2016 Homepage](<https://www.federalreserve.gov/econres/scf_2016.htm>)
  * [2013 Home Page](<https://www.federalreserve.gov/econres/scf_2013.htm>)
  * [2010 Home Page](<https://www.federalreserve.gov/econres/scf_2010.htm>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

  


## References

Urls used in the creation of this data package.

  * **[scf_public_19](<https://www.federalreserve.gov/econres/files/scf2019s.zip#p19i6.dta>)**. Survey of consumer finances, full public dataset, 2019
  * **[scf_extract_19](<https://www.federalreserve.gov/econres/files/scfp2019s.zip#rscfp2019.dta>)**. Survey of consumer finances, public extract, 2019
  * **[scf_weights_19](<https://www.federalreserve.gov/econres/files/scf2019rw1s.zip#p19_rw1.dta>)**. Survey of consumer finances, replicate weights, 2019
  * **[scf_public_16](<https://www.federalreserve.gov/econres/files/scf2016s.zip#p16i6.dta>)**. Survey of consumer finances, full public dataset, 2016
  * **[scf_extract_16](<https://www.federalreserve.gov/econres/files/scfp2016s.zip#rscfp2016.dta>)**. Survey of consumer finances, public extract, 2016
  * **[scf_weights_16](<https://www.federalreserve.gov/econres/files/scf2016rw1s.zip#p16_rw1.dta>)**. Survey of consumer finances, replicate weights, 2016
  * **[scf_public_13](<https://www.federalreserve.gov/econres/files/scf2013s.zip#p13i6.dta>)**. Survey of consumer finances, full public dataset, 2013
  * **[scf_extract_13](<https://www.federalreserve.gov/econres/files/scfp2013s.zip#rscfp2013.dta>)**. Survey of consumer finances, public extract, 2013
  * **[scf_weights_13](<https://www.federalreserve.gov/econres/files/scf2013rw1s.zip#p13_rw1.dta>)**. Survey of consumer finances, replicate weights, 2013
  * **[scf_public_10](<https://www.federalreserve.gov/econres/files/scf2010s.zip#p10i6.dta>)**. Survey of consumer finances, full public dataset, 2010
  * **[scf_extract_10](<https://www.federalreserve.gov/econres/files/scfp2010.zip#scfp2010&target_format=dta>)**. Survey of consumer finances, public extract, 2010
  * **[scf_weights_10](<https://www.federalreserve.gov/econres/files/scf2010rw1s.zip#p10_rw1.dta>)**. Survey of consumer finances, replicate weights, 2010


## Packages

  * **s3** s3://library.metatab.org/federalreserve.gov-consumer_finances-1.2.4.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances-1.2.4.csv>
  * **source** <https://github.com/CivicKnowledge/insights.civicknowledge.com.git>


### Accessing Data in Vanilla Pandas
```
import pandas as pd
```

### Accessing Package in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/federalreserve.gov-consumer_finances-1.2.4.csv')

# Create Dataframes
```
