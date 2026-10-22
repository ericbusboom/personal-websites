---
title: "Homicides in California"
date: 2020-06-18T00:08:23+00:00
draft: false
categories: ["Dataset", "Police Data"]
tags: ["crime", "homicide", "law_enforcement", "openjustice.doj.ca.gov", "police", "police_data_collection"]
author: "metapack"
description: "Homicides reported to the California DOJ by local law enforcement."
---

_Homicides reported to the California DOJ by local law enforcement._

`openjustice.doj.ca.gov-homicide-1.1.1`. Modified 2020-06-18T00:08:12


## Resources

  * **[homicides](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-homicide-1.1.1/data/homicides.csv>)**. California homicides
  * **[homicide_justifiable](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-homicide-1.1.1/data/homicide_justifiable.csv>)**. California justifiable homicides
  * **[homicide_manslaughter](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-homicide-1.1.1/data/homicide_manslaughter.csv>)**. California manslaughter homicides
  * **[precipitating_event_labels](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-homicide-1.1.1/data/precipitating_event_labels.csv>)**. Value labels for the Precipitating Event column
  * **[means_of_death_labels](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-homicide-1.1.1/data/means_of_death_labels.csv>)**. Value labels for the means_of_death column
  * **[location_labels](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-homicide-1.1.1/data/location_labels.csv>)**. Value labels for the location column
  * **[gender_labels](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-homicide-1.1.1/data/gender_labels.csv>)**. Value labels for the gender column
  * **[relationship_labels](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-homicide-1.1.1/data/relationship_labels.csv>)**. Value labels for the relationship column
  * **[race_ethnicity_labels](<https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-homicide-1.1.1/data/race_ethnicity_labels.csv>)**. Value labels for the race_ethnicity column


## Documentation

The Homicides in California file is publilshed by the California Department of Justices's [Open Justice](<https://openjustice.doj.ca.gov>) site. It collects reports from local law enformcement. From the website: 

> Information on homicides in California are reported by various LEAs as part of the reporting requirements for the Federal Uniform Crime Reporting (UCR) Program. These data provide detailed information about the circumstances of each homicide in addition to personal characteristics of the victim.

## Processing

The value label files were manually extracted from the data dictionary PDF. These files can be merged with the main homicide files to add human readable labels to the values for these columns: 

  * precipitating_event
  * means_of_death
  * location
  * gender
  * relationship
  * race_ethnicity


The `race_ethnicity` column has two codes that map to the same race label for many race labels. For instance, both '1' and 'W' are codes for the label 'White'. These duplicate numeric codes have been replaced with the associated alpha code.

### Documentation Links

  * [Data documentation](<https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2019-07/Homicide%20Context_062419.pdf>) Data documentation and data dictionary
  * [Homicide in California in 2019](<https://data-openjustice.doj.ca.gov/sites/default/files/2019-07/Homicide%20In%20CA%2020190701.pdf>) Report based on this dataset.
  * [Data download page](<https://openjustice.doj.ca.gov/data>)
  * [Open Justice Home Page](<https://openjustice.doj.ca.gov/>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

homicides | precipitating_event_labels | means_of_death_labels | location_labels | gender_labels | relationship_labels | race_ethnicity_labels   


### homicides

Column Name| Data Type| Description  
---|---|---  
county| integer| County  
jurisdiction_ncic| string| Jurisdiction (NCIC)  
bcs_number| integer| BCS number  
victim_number| integer| Victim Number  
month_of_report| integer| Month of Report  
year_of_report| integer| Year of Report  
total_victim| integer| Total Victim  
total_suspects| integer| Total Suspects  
gender| integer| Gender  
race_ethnicity| string| Race/Ethnicity  
age| integer| Age  
crime_status| integer| Crime Status  
victim_offender_relationship_1| integer| Victim/Offender Relationship #2  
victim_offender_relationship_2| integer| Victim/Offender Relationship #3  
victim_offender_relationship_3| integer| Victim/Offender Relationship #4  
victim_offender_relationship_4| integer| Victim/Offender Relationship #4  
month_of_incident| integer| Month of Incident  
day_of_month_of_incident| integer| Day of month of Incident  
year_of_incident| integer| Year of Incident  
day_of_week| integer| Day of week  
year_of_death| integer| Year of death  
means_of_death| integer| Means of death  
location| integer| Location where Assault Occured  
precipitating_event| integer| Precipitating Event  
special_circumstance| integer| Special Circumstance/ Potential Death Penalty.  
  
### precipitating_event_labels

Column Name| Data Type| Description  
---|---|---  
precipitating_event| integer|   
precipitating_event_label| text|   
subject_heading| string|   
  
### means_of_death_labels

Column Name| Data Type| Description  
---|---|---  
means_of_death| integer|   
means_of_death_label| string|   
  
### location_labels

Column Name| Data Type| Description  
---|---|---  
location| integer|   
location_label| string|   
  
### gender_labels

Column Name| Data Type| Description  
---|---|---  
gender| integer|   
gender_label| string|   
  
### relationship_labels

Column Name| Data Type| Description  
---|---|---  
relationship| integer|   
relationship_label| string|   
  
### race_ethnicity_labels

Column Name| Data Type| Description  
---|---|---  
race_ethnicity| string|   
race_ethnicity_label| string|   
  
## References

Urls used in the creation of this data package.

  * **data/value_labels.csv**. Data dictionary, extracted from the data ditionary pdf
  * **[homicides_s](<https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2019-06/Homicide%20_Actuals_1987-2018.csv>)**. California homicides
  * **[homicide_justifiable_s](<https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2019-06/Homicide_Justifiable_1987-2018.csv>)**. California justifiable homicides
  * **[homicide_manslaughter_s](<https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2019-06/Homicide_Manslaughter_1987-2018.csv>)**. California manslaughter homicides


## Packages

  * **s3** s3://library.metatab.org/openjustice.doj.ca.gov-homicide-1.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-homicide-1.1.1.csv>
  * **source** <https://github.com/metatab-packages/policedata-collection.git>


### Accessing Packages in Metapack
```
import metapack as mp
pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/openjustice.doj.ca.gov-homicide-1.1.1.csv')

# Create Dataframes
homicides_df = pkg.resource('homicides').dataframe()
homicide_justifiable_df = pkg.resource('homicide_justifiable').dataframe()
homicide_manslaughter_df = pkg.resource('homicide_manslaughter').dataframe()
precipitating_event_labels_df = pkg.resource('precipitating_event_labels').dataframe()
means_of_death_labels_df = pkg.resource('means_of_death_labels').dataframe()
location_labels_df = pkg.resource('location_labels').dataframe()
gender_labels_df = pkg.resource('gender_labels').dataframe()
relationship_labels_df = pkg.resource('relationship_labels').dataframe()
race_ethnicity_labels_df = pkg.resource('race_ethnicity_labels').dataframe()
```
