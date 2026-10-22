---
title: "San Diego Crime Incidents with Victim Descriptions"
date: 2020-09-29T15:08:12+00:00
draft: false
categories: ["Dataset"]
tags: ["arjis.org", "crime", "law_enforcement", "police", "police_data_collection", "sandiegodata.org"]
author: "metapack"
description: "Crime Victims in San Diego, from 2016 though July 2020, with UCR codes for the"
---

_Crime Victims in San Diego, from 2016 though July 2020, with UCR codes for the crime and the age, race and sex of the victim._

`arjis.org-crime_victims-pra-1.1.1`. Modified 2020-09-30T16:40:33

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[sdcrime_16_20_allyears](<https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/data/sdcrime_16_20_allyears.csv>)**. San Diego crime suspects and victims, 2016 though July 2020,all records
  * **[sdcrime_16_20_nosusp](<https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/data/sdcrime_16_20_nosusp.csv>)**. San Diego crime victims, 2016 though July 2020, no suspects
  * **[sdcrime_16_20_uniquecase](<https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/data/sdcrime_16_20_uniquecase.csv>)**. San Diego crime victims, 2016 though July 2020, unique case numbers
  * **[ucrcodes](<https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/data/ucrcodes.csv>)**. UCR codes and detailed descriptions


## Documentation

There are important national conversations going on about criminal justice reform, aligning resources towards prevention and community support rather than primarily for policing, and calls to Defund or Abolish the Police. These are all valuable discussions about the communities in which we want to live. An important voice in that conversation is the voice of victims of crime. The data below is a complete data set for victims of violent crime from ARJIS (Automated Regional Justice Information System) for San Diego County, the nation's fifth largest County, from 2016 through 2020. The complete data set, a cleaned version of the data, a data dictionary, the Public Records Act request on which the data was based and several maps are provided for review. A full conversation requires diverse voices and will help ensure that resources are realigned in a way that furthers the dual aims of equity and safety in our communities. 

The file has multiple rows per incident, one for each suspect or victim. The primary key `pk` links records together into a single crime incident. 

This package provides the datasets as CSV files. You can also get the Excel source files for these CSVs, and the Excel file originally returned by ARJIS:

  * [Processed Dataset](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandag.org/OPCrimeVictims/Omar%20Passons%20-%20SDCounty_CrimeData_Jan16_Jul20.xlsx>). Excel. This is the dataset used to generate this data package
  * [Original Source Dataset](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandag.org/OPCrimeVictims/Omar%20Passons%20-%20second_DataExtract_Omar_Passons.xlsx>). Excel. Original, unprocessed dataset, ARJIS’ response to the PRA. This dataset is an Excel file with one tab per year.


## Processing

The resources in this pacakage have been converted from Excel format to CSV, and the mixed-case column names are all lowercased. For the Excel file source, as it was recieved by the San Diego Regional Data Library, see the References Section.

  * dates are converted to ISO format
  * Created "year" field
  * Deleted MACRStatus from years 2017-2020
  * Combined years into 1 file
  * Deleted partial August cases to have complete month
  * Deleted 2 ARJIS and 1 DA as AGENCY records
  * Deleted incident type (all were crime case), highcharge (all were 1) and role (all were incident)
  * ALLYRS_NOSUSP includes only victims, victim/witnesses and blank (property?) in the person role
  * UNIQUECASE includes unique case numbers (no matter how many victims)


ALLYEARS data has 676,244 records/ ALLYRS_NOSUSP has 402,397 records with 312,089 unique cases

Of the 312,089 cases, 5% (16,765) don't have a block number and 2% (5,025) don't have a ZIP (with another 1-2% with a ZIP not in SD County).

### Documentation Links

  * [PRA Request](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandag.org/OPCrimeVictims/PRA%20Request%20-%20Crime%20Victims%20San%20Diego%20County.pdf>) PRA request issued for the data.
  * [Data Dictionary](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandag.org/OPCrimeVictims/Omar%20Passons%20-%20Data%20Dictionary%20for%20Omar%20Passons%20Request%209.4.20.docx>) Original data dictionary provided with the response, describing the original, unmodified dataset.
  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/index.html>)


## Images

  * [![](https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/doc/Figure1_HomicideVictimsFinal.png)](<https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/doc/Figure1_HomicideVictimsFinal.png> "Figure 1") Homicide Victims by Race, San Diego County
  * [![](https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/doc/Figure2_VictimsbyRaceFinal.jpg)](<https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/doc/Figure2_VictimsbyRaceFinal.jpg> "Figure 2") Violent Crime Victims, Jan 2016 to July 2020, South Central San Diego County. Neighborhoods with large proportions of Black/Latino crime victims.
  * [![](https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/doc/Figure3_VictimsbyAreaFinal.jpg)](<https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/doc/Figure3_VictimsbyAreaFinal.jpg> "Figure 3") Violent Crime Victims, Jan 2016 to July 2020, South Central San Diego County. Higher and lower crime rate neighborhoods


## Contacts

  * **Analyst**

[Julie Wartell](<mailto:julie.wartell@att.net>), Problem Analysis Group

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)

  * **Origin**

[ARJIS](<http://www.arjis.org>)


## Data Dictionary

ucrcodes | sdcrime_16_20_allyears | sdcrime_16_20_nosusp | sdcrime_16_20_uniquecase   


### ucrcodes

Column Name| Data Type| Description  
---|---|---  
index| integer|   
ucr_code| string|   
description| string|   
  
### sdcrime_16_20_allyears

Column Name| Data Type| Description  
---|---|---  
pk| integer| Pk – this is an auto number generated by our SQL database when a new unique record comes into ARJIS. Note: Use this as your unique identifier.  
activitynumber| string| activityNumber - the case number for each activity/incident/crime case (these all mean the same thing), this can be used as a unique identifier when combined with the agency name  
activitydate| datetime| ActivityDate – The date/time the crime case occurred  
year| integer| Year of source file  
agency| string| Agency - the agency reporting the crime case  
violationsection| string| ViolationSection – the highest charge number recorded on the arrest ( i.e. most serious charge connected to the arrest, arrests may have up to ten charges)  
violationtype| string| ViolationType – the municipal, penal or other code section which is attached to the highest recorded Violation section on the arrest  
chargedescription| string| ChargeDescription – A brief text definition of the type of crime type noted in the violation section  
chargelevel| string| ChargeLevel – whether the highest charge is a felony, misdemeanor or infraction (there should only be felonies and misdemeanors in this file)  
codeucr| string| CodeUCR – a more specific code to define the exact crime type per Uniform Crime Reporting Standards, see defining table on last tab of excel. If you really want to get specific with crime categories this is your tool!  
crimecategory| string| CrimeCategory – This is the category of the offense type based on the UCR program definitions and corresponds to the categories used on the Crime Statistics portal, with the exception that additional crime categories are included such as arson, simple assault, Part II crimes, and recovered vehicles.  
personrole| string| PersonRole – the role of the person on this particular record (victim, suspect, victim/witness or blank) please note that the same crime case may have multiple suspects or victims and some crime cases may not have any suspect or victim information listed depending on what the agency provided to ARJIS.  
race| string| Race – the ethnicity of the person listed in the person role field which can include numerous fields. Note: ARJIS agencies may apply race codes differently across the region.  
age| integer| Age – the age of the person listed in the person role field Note: some cases may have no age listed which is a data entry error or unknown by the agency  
sex| string| Sex – the gender of the person listed in the person role field which can include Male, Female, Non-Binary or Unknown. Note: some cases may have no sex listed which is a data entry error or unknown by the agency  
zipcode| integer| ZipCode – The zip code where the incident/crime case occurred  
censusblock| string| Census Block/Tract – the census block/tract where the incident/crime case occurred  
censustract| string| Census Block/Tract – the census block/tract where the incident/crime case occurred  
city| string| City – The city where the incident/crime case occurred  
  
### sdcrime_16_20_nosusp

Column Name| Data Type| Description  
---|---|---  
pk| integer| Pk – this is an auto number generated by our SQL database when a new unique record comes into ARJIS. Note: Use this as your unique identifier.  
activitynumber| string| activityNumber - the case number for each activity/incident/crime case (these all mean the same thing), this can be used as a unique identifier when combined with the agency name  
activitydate| datetime| ActivityDate – The date/time the crime case occurred  
year| integer| Year of source file  
agency| string| Agency - the agency reporting the crime case  
violationsection| string| ViolationSection – the highest charge number recorded on the arrest ( i.e. most serious charge connected to the arrest, arrests may have up to ten charges)  
violationtype| string| ViolationType – the municipal, penal or other code section which is attached to the highest recorded Violation section on the arrest  
chargedescription| string| ChargeDescription – A brief text definition of the type of crime type noted in the violation section  
chargelevel| string| ChargeLevel – whether the highest charge is a felony, misdemeanor or infraction (there should only be felonies and misdemeanors in this file)  
codeucr| string| CodeUCR – a more specific code to define the exact crime type per Uniform Crime Reporting Standards, see defining table on last tab of excel. If you really want to get specific with crime categories this is your tool!  
crimecategory| string| CrimeCategory – This is the category of the offense type based on the UCR program definitions and corresponds to the categories used on the Crime Statistics portal, with the exception that additional crime categories are included such as arson, simple assault, Part II crimes, and recovered vehicles.  
personrole| string| PersonRole – the role of the person on this particular record (victim, suspect, victim/witness or blank) please note that the same crime case may have multiple suspects or victims and some crime cases may not have any suspect or victim information listed depending on what the agency provided to ARJIS.  
race| string| Race – the ethnicity of the person listed in the person role field which can include numerous fields. Note: ARJIS agencies may apply race codes differently across the region.  
age| integer| Age – the age of the person listed in the person role field Note: some cases may have no age listed which is a data entry error or unknown by the agency  
sex| string| Sex – the gender of the person listed in the person role field which can include Male, Female, Non-Binary or Unknown. Note: some cases may have no sex listed which is a data entry error or unknown by the agency  
zipcode| integer| ZipCode – The zip code where the incident/crime case occurred  
censusblock| string| Census Block/Tract – the census block/tract where the incident/crime case occurred  
censustract| string| Census Block/Tract – the census block/tract where the incident/crime case occurred  
city| string| City – The city where the incident/crime case occurred  
  
### sdcrime_16_20_uniquecase

Column Name| Data Type| Description  
---|---|---  
activitynumber| string| activityNumber - the case number for each activity/incident/crime case (these all mean the same thing), this can be used as a unique identifier when combined with the agency name  
activitydate| datetime| ActivityDate – The date/time the crime case occurred  
year| integer| Year of source file  
agency| string| Agency - the agency reporting the crime case  
violationsection| string| ViolationSection – the highest charge number recorded on the arrest ( i.e. most serious charge connected to the arrest, arrests may have up to ten charges)  
violationtype| string| ViolationType – the municipal, penal or other code section which is attached to the highest recorded Violation section on the arrest  
chargedescription| string| ChargeDescription – A brief text definition of the type of crime type noted in the violation section  
chargelevel| string| ChargeLevel – whether the highest charge is a felony, misdemeanor or infraction (there should only be felonies and misdemeanors in this file)  
codeucr| string| CodeUCR – a more specific code to define the exact crime type per Uniform Crime Reporting Standards, see defining table on last tab of excel. If you really want to get specific with crime categories this is your tool!  
crimecategory| string| CrimeCategory – This is the category of the offense type based on the UCR program definitions and corresponds to the categories used on the Crime Statistics portal, with the exception that additional crime categories are included such as arson, simple assault, Part II crimes, and recovered vehicles.  
personrole| string| PersonRole – the role of the person on this particular record (victim, suspect, victim/witness or blank) please note that the same crime case may have multiple suspects or victims and some crime cases may not have any suspect or victim information listed depending on what the agency provided to ARJIS.  
race| string| Race – the ethnicity of the person listed in the person role field which can include numerous fields. Note: ARJIS agencies may apply race codes differently across the region.  
age| integer| Age – the age of the person listed in the person role field Note: some cases may have no age listed which is a data entry error or unknown by the agency  
sex| string| Sex – the gender of the person listed in the person role field which can include Male, Female, Non-Binary or Unknown. Note: some cases may have no sex listed which is a data entry error or unknown by the agency  
zipcode| integer| ZipCode – The zip code where the incident/crime case occurred  
censusblock| string| Census Block/Tract – the census block/tract where the incident/crime case occurred  
censustract| string| Census Block/Tract – the census block/tract where the incident/crime case occurred  
city| string| City – The city where the incident/crime case occurred  
city| string|   
  
## References

Urls used in the creation of this data package.

  * **[Processed Source Dataset](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandag.org/OPCrimeVictims/Omar%20Passons%20-%20SDCounty_CrimeData_Jan16_Jul20.xlsx>)**. Source dataset, as received by SDRDL, and processed by Julie Wartell. This is the dataset used to generate this data package
  * **[Original Source Dataset](<https://library-metatab-org.s3.amazonaws.com/ds.civicknowledge.org/sandag.org/OPCrimeVictims/Omar%20Passons%20-%20second_DataExtract_Omar_Passons.xlsx>)**. Original, unprocessed dataset, ARJIS' response to the PRA. This dataset is an Excel file with one tab per year.


## Packages

  * **s3** s3://library.metatab.org/arjis.org-crime_victims-pra-1.1.1.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1.csv>
  * **source** <https://github.com/metatab-packages/arjis.org-crime_victims-pra.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    sdcrime_16_20_allyears_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/data/sdcrime_16_20_allyears.csv')
    sdcrime_16_20_nosusp_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/data/sdcrime_16_20_nosusp.csv')
    sdcrime_16_20_uniquecase_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/data/sdcrime_16_20_uniquecase.csv')
    ucrcodes_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1/data/ucrcodes.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/arjis.org-crime_victims-pra-1.1.1.csv')
    
    # Create Dataframes
    sdcrime_16_20_allyears_df = pkg.resource('sdcrime_16_20_allyears').dataframe()
    sdcrime_16_20_nosusp_df = pkg.resource('sdcrime_16_20_nosusp').dataframe()
    sdcrime_16_20_uniquecase_df = pkg.resource('sdcrime_16_20_uniquecase').dataframe()
    ucrcodes_df = pkg.resource('ucrcodes').dataframe()
    
[/code]
