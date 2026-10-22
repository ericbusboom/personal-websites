---
title: "San Diego Homelessness Contract Annotations"
date: 2021-08-12T19:24:17+00:00
draft: false
categories: ["Dataset"]
tags: ["homlessness", "sdcta.org", "text_analysis"]
author: "metapack"
description: "Processed TagTog annotations for homelessness contracts collected by the"
---

_Processed TagTog annotations for homelessness contracts collected by the_

`sdcta.org-hl_contracts-1.1.1`. Modified 2021-08-12T19:25:41

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[annotations](<https://library-metatab-org.s3.amazonaws.com/sdcta.org-hl_contracts-1.1.1/data/annotations.csv>)**. Extracted and processed annotations.
  * **[contexts](<https://library-metatab-org.s3.amazonaws.com/sdcta.org-hl_contracts-1.1.1/data/contexts.csv>)**. Surrounding paragraphs for the annotations, linked by 'part'


## Documentation

Processed TagTog annotations for homelessness contracts collected by the San Diego County Taxpayers Association.

### Documentation Links

  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/sdcta.org-hl_contracts-1.1.1/index.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

annotations | contexts   


### annotations

Column Name| Data Type| Description  
---|---|---  
classid| string|   
part| string|   
offset_start| integer|   
text| text|   
coordinates| string|   
confidence| string|   
confidence_prob| number|   
fields| string|   
normalizations| string|   
who| string|   
file_name| string|   
html_file_name| string|   
coordinates_0_x| number|   
coordinates_0_y| number|   
coordinates_1_x| number|   
coordinates_1_y| number|   
value| integer|   
anno_type| string|   
  
### contexts

Column Name| Data Type| Description  
---|---|---  
part| string|   
context| text|   
  
## References

Urls used in the creation of this data package.

  * **data/homelessness-contracts-20210811.zip**. Zip file downloaded from TagTog with text and annotations, date 2021-08-11


## Packages

  * **zip** <https://library-metatab-org.s3.amazonaws.com/sdcta.org-hl_contracts-1.1.1.zip>
  * **s3** s3://library.metatab.org/sdcta.org-hl_contracts-1.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/sdcta.org-hl_contracts-1.1.1.csv>
  * **source** <https://github.com/metatab-packages/sdcta.org-hl_contracts.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    annotations_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sdcta.org-hl_contracts-1.1.1/data/annotations.csv')
    contexts_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/sdcta.org-hl_contracts-1.1.1/data/contexts.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/sdcta.org-hl_contracts-1.1.1.zip')
    
    # Create Dataframes
    annotations_df = pkg.resource('annotations').dataframe()
    contexts_df = pkg.resource('contexts').dataframe()
    
[/code]
