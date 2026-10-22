---
title: "California Academic Performance Index, 1999 - 2012"
date: 2019-05-15T22:27:28+00:00
draft: false
categories: ["Dataset"]
tags: ["autogen", "cde.ca.gov"]
author: "metapack"
description: "API scores for California schools"
---

_API scores for California schools_

`cde.ca.gov-api_scores-1`

Resources | Packages | Documentation| Contacts

## Resources

  * **[columns_by_year_growth.csv](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandiegodata.org/cde.ca.gov-api-combined-429e/cal-api-growth-99-13.csv>)**. Report of the column names and descriptions in all growth files, and what year of file each column and description appears in.
  * **[documentation.html](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandiegodata.org/cde.ca.gov-api-combined-429e/California%20Academic%20Performance%20Index%2C%201999%20-%202012.htm>)**. Dataset documentation
  * **[cal-api-base-99-12.csv](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandiegodata.org/cde.ca.gov-api-combined-429e/cal-api-base-99-12.csv>)**. API Base in CSV Format
  * **[cal-api-growth-99-13.csv](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandiegodata.org/cde.ca.gov-api-combined-429e/cal-api-growth-99-13.csv>)**. API Growth in CSV Format
  * **[columns_by_year_base.csv](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandiegodata.org/cde.ca.gov-api-combined-429e/columns_by_year_base.csv>)**. Report of the column names and descriptions in all base files, and what year of file each column and description appears in.
  * **[schema.csv](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandiegodata.org/cde.ca.gov-api-combined-429e/schema.csv>)**. The schema for all tables, as a CSV file.


## Documentation

Compilation of multiple years of California Academic Performance Index scores into single files. 

This dataset includes two files that combine multiple years of the [California Academic Performance Index](<http://www.cde.ca.gov/ta/ac/ap/>) into single CSV files. These files have a few advantages over the oroginal data releases from The California Department of Education:

  * Multiple years of records are combined into a single file
  * Files are converted to CSV format to be useful with a wider range of software tools
  * Column names are normalized to be consistent across years
  * Data is presented in a consistent schema, with some erroneous values removed


If you do not need to analyze multiple years and can work with fixed with text or DBF files, the original, single-year source files may be more appropriate. 

**This data is a beta release, and has not been fully verified for fidelity with the upstream source. Use with caution.**

This file and the attached **schema.csv** and **documentation.html** files describe the changes made to the original files in this compilation. See the [California Department of Education website](<http://www.cde.ca.gov/ta/ac/ap/>) for complete documentation on the data in these datasets.

## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@sandiegodata.org>), [San Diego Regional Data Library](<http://www.sandiegodata.org>)


## Packages

  * **source** <https://github.com/metatab-packages/sdrdl-data-repo.git>


Last Modified 2019-05-15T21:58:21
