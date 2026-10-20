---
title: "Annual Survey of School System Finances"
date: 2022-07-17T12:51:36+00:00
draft: false
categories: ["cde.ca.gov", "Dataset"]
tags: ["cde.ca.gov", "census.gov", "education"]
author: "metapack"
description: "Education finance data include revenues, expenditures, debt, and assets (cash"
---

_Education finance data include revenues, expenditures, debt, and assets (cash and security holdings) of elementary and secondary public school systems. Statistics cover school systems in all states, and include the District of Columbia._

`census.gov-school_finance-1.1.3`. Modified 2022-07-17T13:01:02

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[school_finance](<http://library.metatab.org/census.gov-school_finance-1.1.3/data/school_finance.csv>)**. Combined school finance


## Documentation

### Documentation Links

  * [Annual Survey of School System Finances Tables](<https://www.census.gov/programs-surveys/school-finances/data/tables.html>) Program homepage
  * [Documentation, 2020](<https://www2.census.gov/programs-surveys/school-finances/technical-documentation/complete-technical-documentation/2020/school20doc.doc>) Dataset documentation, including data dictionary
  * [Documentation Page](<http://library.metatab.org/census.gov-school_finance-1.1.3/index.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

school_finance   


### school_finance

Column Name| Data Type| Description  
---|---|---  
state| integer| State Identification Number  
idcensus| integer| School System Identification Number1  
name| string| School System Name  
conum| integer| ANSI State and County Code1  
csa| string| Consolidated Statistical Area1  
cbsa| string| Core-Based Statistical Area1  
schlev| integer| School Level Code1  
ncesid| integer| NCES ID Code1  
yrdata| integer| Year of Data  
v33| integer| Fall Membership  
totalrev| integer| TOTAL ELEMENTARY-SECONDARY REVENUE  
tfedrev| integer| Total Revenue from Federal Sources  
c14| integer| Federal revenue through the state - Title I  
c15| integer| Federal revenue through the state - IDEA, Part B, Sections 611 and 619 - Special Education Grants to States and Preschool Grants  
c19| integer| Federal revenue through the state - Career and technical education  
c22| integer| Federal revenue through the state - Title II, Part A - Supporting Effective Instruction  
c23| integer| Federal revenue through the state - Title IV, Part A, Subpart 1, Section 4105 - Student Support and Academic Enrichment Grants  
c26| integer| Federal revenue through the state - Title IV, Part B - 21st Century Community Learning Centers  
c27| integer| Federal revenue through the state - Title V, Part B, Subpart 2 - Rural and Low-Income School Program  
b11| integer| Federal revenue through the state - Title III, Part A - English Language Acquisition State Grants  
c20| integer| Federal revenue through the state - All other  
c25| integer| Federal revenue through the state - School meal programs - Child Nutrition Act  
c36| integer| Federal revenue - Nonspecified  
b10| integer| Direct federal revenue - Title VII - Impact Aid  
b12| integer| Direct federal revenue - Title VI - Indian, Native Hawaiian, and Alaska Native Education  
b14| integer| Direct federal revenue - Title V, Part B, Subpart 1 - Small, Rural School Achievement Program  
b13| integer| Direct federal revenue - All other  
tstrev| integer| Total Revenue from State Sources  
c01| integer| General formula assistance  
c04| integer| Staff improvement programs  
c05| integer| Special education programs  
c06| integer| Compensatory and basic skills attainment programs  
c07| integer| Bilingual education programs  
c08| integer| Gifted and talented programs  
c09| integer| Career and technical education programs  
c10| integer| School meal programs  
c11| integer| Capital outlay and debt service programs  
c12| integer| Transportation programs  
c13| integer| All other revenues from state sources  
c24| integer| Census state, NCES local revenue  
c35| integer| State revenue - Nonspecified  
c38| integer| State payments on behalf - Benefits  
c39| integer| State payments on behalf - Nonbenefits  
tlocrev| integer| Total Revenue from Local Sources  
t02| integer| Parent government contributions  
t06| integer| Property taxes  
t09| integer| General sales or gross receipts taxes  
t15| integer| Public utility taxes  
t40| integer| Individual and corporate income taxes  
t99| integer| All other taxes  
d11| integer| Revenue from other school systems  
d23| integer| Revenue from cities and counties  
a07| integer| Tuition fees from pupils, parents, and other private sources  
a08| integer| Transportation fees from pupils, parents, and other private sources  
a09| integer| School lunch revenues  
a11| integer| Textbook sales and rentals  
a13| integer| District activity receipts  
a15| integer| Student fees, nonspecified  
a20| integer| Other sales and service revenues  
a40| integer| Rents and royalties  
u11| integer| Sale of property  
u22| integer| Interest earnings  
u30| integer| Fines and forfeits  
u50| integer| Private contributions  
u97| integer| Miscellaneous other local revenues  
totalexp| integer|   
tcurelsc| integer| TOTAL CURRENT SPENDING FOR ELEMENTARY-SECONDARY PROGRAMS  
tcurinst| integer| TOTAL CURRENT SPENDING FOR INSTRUCTION  
e13| integer| Current operation expenditure - Instruction  
j13| integer| State payments on behalf - Instruction benefits  
j12| integer| Own retirement system transfer - Instruction  
j14| integer| State payments on behalf - Instruction nonbenefits  
v91| integer| Exhibit - Payments to private schools  
v92| integer| Exhibit - Payments to charter schools  
tcurssvc| integer| TOTAL CURRENT SPENDING FOR SUPPORT SERVICES  
e17| integer| Current operation expenditure - Pupil support  
e07| integer| Current operation expenditure - Instructional staff support  
e08| integer| Current operation expenditure - General administration  
e09| integer| Current operation expenditure - School administration  
v40| integer| Current operation expenditure - Operation and maintenance of plant  
v45| integer| Current operation expenditure - Student transportation  
v90| integer| Current operation expenditure - Business/central/other support services  
v85| integer| Current operation expenditure - Nonspecified support services  
j17| integer| State payments on behalf - Pupil support benefits  
j07| integer| State payments on behalf - Instructional staff support benefits  
j08| integer| State payments on behalf - General administration benefits  
j09| integer| State payments on behalf - School administration benefits  
j40| integer| State payments on behalf - Operation and maintenance of plant benefits  
j45| integer| State payments on behalf - Student transportation benefits  
j90| integer| State payments on behalf - Business/central/other support services benefits  
j11| integer| Own retirement system transfer - Support services  
j96| integer| State payments on behalf - Support services, nonbenefits  
tcuroth| integer| TOTAL CURRENT SPENDING FOR OTHER ELEMENTARY-SECONDARY PROGRAMS  
e11| integer| Current operation expenditure - Food services  
v60| integer| Current operation expenditure - Enterprise operations  
v65| integer| Current operation expenditure - Other elementary-secondary programs  
j10| integer| State payments on behalf - Other benefits  
j97| integer| State payments on behalf - Noninstructional and nonbenefits  
nonelsec| integer| TOTAL CURRENT SPENDING FOR NONELEMENTARY-SECONDARY PROGRAMS  
v70| integer| Current operation expenditure - Community services  
v75| integer| Current operation expenditure - Adult education  
v80| integer| Current operation expenditure - Other nonelementary-secondary programs  
j98| integer| State payments on behalf - Nonelementary-secondary programs  
tcapout| integer| TOTAL CAPITAL OUTLAY EXPENDITURE  
f12| integer| Construction  
g15| integer| Purchase of land and existing structures  
k09| integer| Instructional equipment  
k10| integer| Other equipment  
k11| integer| Nonspecified equipment  
j99| integer| State payments on behalf - Capital outlay  
l12| integer| Payments to state governments  
m12| integer| Payments to local governments  
q11| integer| Payments to other school systems  
i86| integer| Interest on school system debt  
z32| integer| Total salaries and wages  
z33| integer| Total salaries and wages - Instruction  
v11| integer| Total salaries and wages - Pupil support  
v13| integer| Total salaries and wages - Instructional staff support  
v15| integer| Total salaries and wages - General administration  
v17| integer| Total salaries and wages - School administration  
v21| integer| Total salaries and wages - Operation and maintenance of plant  
v23| integer| Total salaries and wages - Student transportation  
v37| integer| Total salaries and wages - Business/central/other support services  
v29| integer| Total salaries and wages - Food services  
z34| integer| Total employee benefit payments  
v10| integer| Total employee benefit payments - Instruction  
v12| integer| Total employee benefit payments - Pupil support  
v14| integer| Total employee benefit payments - Instructional staff  
v16| integer| Total employee benefit payments - General administration  
v18| integer| Total employee benefit payments - School administration  
v22| integer| Total employee benefit payments - Operation and maintenance of plant  
v24| integer| Total employee benefit payments - Student transportation  
v38| integer| Total employee benefit payments - Business/central/other support services  
v30| integer| Total employee benefit payments - Food services  
v32| integer| Total employee benefit payments - Enterprise operations  
_19h| integer| Long-term debt outstanding at beginning of the fiscal year  
_21f| integer| Long-term debt issued during the fiscal year  
_31f| integer| Long-term debt retired during the fiscal year  
_41f| integer| Long-term debt outstanding at end of fiscal year  
_61v| integer| Short-term debt outstanding at beginning of the fiscal year  
_66v| integer| Short-term debt outstanding at end of the fiscal year  
w01| integer| Cash and deposits, held at end of fiscal year - Debt service funds  
w31| integer| Cash and deposits, held at end of fiscal year - Bond funds  
w61| integer| Cash and deposits, held at end of fiscal year - Other funds  
ar1| integer| CARES Act Funds - Revenue - Elementary and Secondary School Emergency Relief (ESSER) Fund  
ar2| integer| CARES Act Funds - Revenue - Governor’s Emergency Education Relief (GEER) Fund  
ar3| integer| CARES Act Funds - Revenue - Education Stabilization Fund - Reimagine Workforce Preparation (ESF-RWP) Discretionary Grant  
ar4| integer| CARES Act Funds - Revenue - Education Stabilization Fund - Rethink K-12 Education Models (ESF-REM) Discretionary Grant  
ar5| integer| CARES Act Funds - Revenue - Project School Emergency Response to Violence (Project SERV)  
ar6| integer| CARES Act Funds - Revenue - Coronavirus Relief Fund (CRF)  
ae1| integer| CARES Act Funds - Expenditure - Current spending  
ae2| integer| CARES Act Funds - Expenditure - Instructional  
ae3| integer| CARES Act Funds - Expenditure - Support services  
ae4| integer| CARES Act Funds - Expenditure - Capital outlay  
ae5| integer| CARES Act Funds - Expenditure - Technology-related supplies and purchased services  
ae6| integer| CARES Act Funds - Expenditure - Technology-related equipment  
c17| integer|   
c16| integer|   
  
## References

Urls used in the creation of this data package.

  * **[sch_finance_20](<https://www2.census.gov/programs-surveys/school-finances/tables/2020/secondary-education-finance/elsec20.xls>)**. All Data items, 2020
  * **[sch_finance_19](<https://www2.census.gov/programs-surveys/school-finances/tables/2019/secondary-education-finance/elsec19.xls>)**. All Data items, 2019
  * **[sch_finance_18](<https://www2.census.gov/programs-surveys/school-finances/tables/2018/secondary-education-finance/elsec18.xls>)**. All Data items, 2018
  * **[sch_finance_17](<https://www2.census.gov/programs-surveys/school-finances/tables/2017/secondary-education-finance/elsec17.xls>)**. All Data items, 2017


## Packages

  * **s3** s3://library.metatab.org/census.gov-school_finance-1.1.3.csv
  * **csv** <http://library.metatab.org/census.gov-school_finance-1.1.3.csv>
  * **source** <https://github.com/metatab-packages/cde.ca.gov-collection.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    school_finance_df =  pd.read_csv('http://library.metatab.org/census.gov-school_finance-1.1.3/data/school_finance.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('http://library.metatab.org/census.gov-school_finance-1.1.3.csv')
    
    # Create Dataframes
    school_finance_df = pkg.resource('school_finance').dataframe()
    
[/code]
