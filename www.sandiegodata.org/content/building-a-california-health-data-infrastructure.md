---
title: "Building A California Health Data Infrastructure"
date: 2014-06-10T09:39:57+00:00
draft: false
author: "qaadmin"
---

How long would it take you to create a chart of the rate of the teenage smoking over the last 20 years in your county, compared to similar counties? If the data is already on your computer, maybe a few minutes. But for most nonprofits, journalists or government staff, this simple question might take days to answer. The reason is that data acquisition and preparation is time consuming and difficult. Even when things are going well, 80% of a data project's effort can be consumed with acquisition and preparation. Because of this cost, there is a wide gap between what we are doing with data and what we could be doing with data. By solving the problems of data acquisition and preparation, we have a substantial opportunity to advance the pace of civic and social development. We propose to build a health data infrastructure for California, an effort that is guided by a simple vision: 

> Anyone with basic skills in Excel and the web should be able to ask a data question at lunch answer it in the afternoon.

To do this, we will need to collect a lot of data, from a lot of counties, clean it, store it, and redistribute it back to the same organizations we got it from. And we'll have to it quickly and inexpensively. But that Data Acquisition problem is one we've already solved. Here, we'll discuss that solution and how to run a pilot to demonstrate its full value.

## What Does a Solution Look Like?

The crux of the problem is data acquisition: getting data is too hard, expensive and time consuming. When the Data Acquisition problem is solved: 

  * Analysts of any experience level can easily find the data they need.
  * Analysts can get the data in formats they can use with familiar tools.
  * Documentation for the data is as easy to find as the data.
  * Excel users can do basic analysis and charts without additional help.
  * Managers can easily get inexpensive help for more difficult data analysis tasks.

A solution like this will require a way to collect and manage data from a wide variety of sources, primarily from state and county health departments. We'll have to organize the data, convert it to many other formats, and deliver it to the websites or file folders where users expect to find it. Our solution is based on an Open Source data management tool called Ambry, which can: 
  * Convert a broad range of datasets to a common format
  * Publish data and documentation to websites, databases and files, in the formats and locations that analysts can most easily find and use them

A complete solution will also will involve: 
  * Hiring a data librarian who can answer questions and help people find and use data
  * Recruiting a broad range of analysts to use the system, so the librarian can refer users to analysts who need more help

In operation, our system will allow data analysts to visit websites, databases or shared drives to find the data the need from any county in California. And, analysts will have access to people they can call to answer questions about what data to use and how to use it. 

## Getting and Using Data

The Ambry system employs a distributed collection of public datasets that are packaged in a common format. (The details of the packaging and distribution will be discussed later.) For the purposes of the next few section, suppose that there exists a large collection of standardized datasets that can be searched for and installed in a similar fashion to phone apps in an app store. How do analysts want to get data? 

  * From a site they know and trust, preferably one run by their own organization, with vetted data,
  * In the formats they already know how to use, 
    * Excel Jockeys want Excel or CSV;
    * Programmers want CSV, JSON or relational databases;
    * Statisticians and Epidemiologists want Stata or SAS;
    * Social scientists want SPSS;
  * With easy access to the documentation for the data, to know the meanings of the variables, how the data was collected, and other important information.

Our system addresses these issues by making it easy to publish data from a central repository of files to other locations. It's like an advertising network, where a company can submit an advertisement once and it shows up on websites, radio programs, television shows and billboards, all the places that consumers already view. In our case, we send datasets to the places that an organization's staff already go to get files for their work. The types of locations that Ambry can publish to include: 
  * Data file repositories such as CKAN, Socrata, DKAN and Junar.
  * Databases, both relational databases and NoSql databases.
  * Directories of files, for instance, a shared drive folder full of CSV files.
  * File sharing services such as Box, Dropbox or Google Drive.

The organization that publishes data does not need to be a government agency. It could be a nonprofit, a private organization, or a consortium. What's important is that the organization understands the needs of its users and can tailor how and where data is published to those needs, so users can find the data they need without being overwhelmed with a lot of data they will never be interested in. For file repositories, Ambry can convert file formats for the tools that analysts use most. 
  * Excel users can have CSV files in a shared drive.
  * Web programmer can have the same set of data in a MySql database.
  * Business analysts can have the data stores in Tableau Server.
  * Statisticians can download SPSS, SAS or Stata files from a website.

All of these separate repositories hold the same set of data, all managed from a single source. If the data is updated only once a month, a single site administrator could handle a dozen different data repositories in a few hours a month. If the agency prefers, all of the repositories could be managed by a contractor for a few hundred dollars per month. 

## Getting Help

At some point, most people need help. In the Ambry system, because datasets are all managed in a similar way, it is possible to create central places to collect and share knowledge about the dataset. Some of the ways of getting help can be: 

  * Documentation included in the Ambry data packages
  * A question and answer forum
  * A dedicated, human Librarian

Often, users will need more than answers, preferring to hire an analyst to do the work. Because Ambry uses a common format for all datasets, hired analysts can find the data they need for a job immediately. Analysts who are familiar with Ambry will also be attracted to answering questions on the form because building a reputation on forums is an excellent way to advertise services. 

## How Data Enters the System

The Ambry system is most useful when a lot of data is available through it, so it is designed to be very accessible to Data Wranglers, the people who build data packages. Ambry tools are Open Source, so they can be freely downloaded, installed and used with no charge. For simple files – most CSV and Excel files – importing can be done automatically, by configuring a URL or filename for the import file. This is particularly true when the organization that packages the data is also the one that publishes it originally. More complex files require programming, but only moderate skill, using Python, one of the most popular programming languages. 

### Automatic Importing

For simple files, particularly ones that don't have documentation or don't require it, users can email the file to an email address, or upload it to a file sharing system, either of which has been configured with a conversion program. This sort of conversion is guaranteed to fit in anyone's daily process, does not require any special skills, and doesn't require installing any extra software. Some of many ways that automatic importing can be configured are: 

  * The spreadsheet user emails the spreadsheet to a special address, once a month.
  * The spreadsheet user saves the file to a shared drive, and an external program copies the file into Ambry.
  * Users store their files in a file sharing service, such as, Box, Dropbox, Google Drive, and Ambry loads the file directly.
  * Users upload their files to a dedicated data repository, similar to the one we host at <http://data.sandiegodata.org>.

The goal of automatic importing is to ensure the process of contributing data does not require any changes to people's daily process. 

### Importing using the Web interface

Ambry supplies a web application for building packages, which, most of the time, involves nothing more than entering the location of a file, either on a shared drive on the web. When the file changes, Ambry can automatically create a new version of the package. Files that Ambry can import through the web interface include: 

  * Excel
  * CSV
  * Geographic shapefiles

Users can setup basic corrections to the data loaded through the automatic uploader, such as simplifying column headers and removing special characters from number columns. The web interface also allows package creators to document the package, providing links and text so others can better understand the data. 

### Importing with a Program

Sometimes, a dataset requires a lot of processing before it is useful, such as combining or splitting files or converting from arcane formats. For these datasets, Ambry provides a sophisticated framework for importing data. Ambry import programs can take data from databases, statistical tool formats, fixed-with files, or scrape websites. And, after the program is created, it can be run automatically to import data when the data are updates. 

## Distributing Data

After the packages are converted, Ambry will upload the packages to a public or private storage location, which can be any file sharing service like Box or Dropbox, Google drive or Amazon S3. The only requirement is that the service provides a URL that other people can access. Then, others can use the URL to that storage service – and a password if the repository is private – to get the files into their own Ambry library. Because people can create packages without a central authority, using free tools, and can distribute data on their own terms, it is much easier to get a lot of people to convert data, which means there is more data in the system for everyone. 

## The Whole Process

Since this document described the process in reverse to motivate why is was designed the way it is, let's describe the whole process from the start. 

  1. Staff in many counties and health oriented nonprofits upload files to websites or send them to email addresses for automatic conversion, or moderately skilled programmers take public data and convert them to Ambry packages.
  2. After conversion Ambry packages are sent to an online library, which can be any online file sharing system, like Dropbox or Google Drive.
  3. Organization's data administrators configure their Ambry systems to use the repository URLs of the other organizations and copy the data they want to their own site.
  4. Administrators select the data their users need, and publish it to CSV files, database, websites or file sharing services, wherever their users want to get the data.
  5. Data users use the file locations they are already familiar with to get they data they need. Data sets are sent to shared drive, Dropbox and other file sharing services, or data repository websites.

The result is that any analyst in a nonprofit or government agency can have, on their desktop, file sharing service or organization website any of the data published by other organizations or counties. 

## Paying For It

We estimate that running the data infrastructure with 50% of California counties participating is sustainable with a revenue of about $1,000 per county per month for the most basic level of collecting and converting data. This cost could be borne by the counties themselves, but it can also be shared with other revenue sources. The monthly revenue requirement includes the amortized cost of converting about 15 datasets per county and hosting a shared file store. Other potential customers for the system are: 

  * University researchers
  * Research firms
  * Nonprofit health organizations
  * Journalists and news organization

The number of organizations that would benefit from a robust health data library is much lager than the number of counties, particularly because a comprehensive data set would appeal to researchers nationwide, not just within California. By selling access to the system to others, we can amortize the costs across a large base, reducing the costs for everyone. 

## A Plan for A Pilot

We propose to run a pilot of the system with a few counties to test how users interact with the system, how to structure the business model, and what additional features users will require. This pilot would likely: 

  * Recruit 2 - 4 counties to participate.
  * Convert high-value health datasets from the counties, as well as datasets from the state, national health organizations and nonprofits. 
  * Publish datasets to a variety of locations and test how users interact with them.
  * Recruit university researchers to use the system and provide feedback.
  * Experiment with a revenue model for sustainability.


Building this system would ensure that a much wider array of data is available to the broadest range of users, and we believe the system can be deployed as a sustainable, revenue generating operation. For more information about Ambry and this project proposal, please contact Eric Busboom at 858 386 4134 or eric@sandiegodata.org.
