---
title: "Current Population Survey, 2023"
date: 2023-03-02T17:49:06+00:00
draft: false
categories: ["Dataset", "Uncategorized"]
tags: ["census.gov"]
author: "metapack"
description: "The Current Population Survey (CPS) is the primary source of labor force"
---

_The Current Population Survey (CPS) is the primary source of labor force statistics for the population of the United States._

`census.gov-cps-2023-basic_monthly-1.1.2`. Modified 2023-03-02T18:24:15

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[variable_descriptions](<https://library-metatab-org.s3.amazonaws.com/census.gov-cps-2023-basic_monthly-1.1.2/data/variable_descriptions.csv>)**. All of the variables and their cleaned text descriptions
  * **[variable_values](<https://library-metatab-org.s3.amazonaws.com/census.gov-cps-2023-basic_monthly-1.1.2/data/variable_values.csv>)**. Text descriptions of the integer values of categorical variables.
  * **[cps202301](<https://library-metatab-org.s3.amazonaws.com/census.gov-cps-2023-basic_monthly-1.1.2/data/cps202301.csv>)**. 


## Documentation

### Documentation Links

  * [Subject Definitions](<https://www.census.gov/programs-surveys/cps/technical-documentation/subject-definitions.html>) Descriptions of major concepts.
  * [User Notes](<https://www.census.gov/programs-surveys/cps/technical-documentation/user-notes.html>) Various technical documentation.
  * [Documentation Page](<https://library-metatab-org.s3.amazonaws.com/census.gov-cps-2023-basic_monthly-1.1.2/index.html>)
  * [Homepage](<https://www.census.gov/programs-surveys/cps.html>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

cps202301 | variable_descriptions | variable_values   


### cps202301

Column Name| Data Type| Description  
---|---|---  
hrhhid2| integer| Household Identifier (Part 2).  
hufinal| integer| Final Outcome Code Outcome codes between 001 and 020 are for CATI. All other outcome codes are for CAPI.  
occurnum| integer| Unique person identifier. Valid only within any specific month.  
huinttyp| integer| Type of interview  
hurespli| integer| Line Number of the Current Respondent  
huprscnt| integer| Number of actual and attempted personal contacts.  
hutypea| integer| Type A noninterview reason  
hutypb| integer| Type B non-interview reason  
hutypc| integer| Type C non-interview reason  
hubus| integer| Does anyone in this household have a business or a farm?  
hubusl1| integer| Enter line number for HUBUS = 1.  
hubusl2| integer| See BUSL1.  
hubusl3| integer| See BUSL1.  
hubusl4| integer| See BUSL1.  
hrmis| integer| Month-in-sample  
hrmonth| integer| Month of Interview  
hryear4| integer| Year of Interview  
hrlonglk| integer|   
qstnum| integer| Unique household identifier. Valid only within any specific month.  
gereg| integer| Region.  
gestfips| integer| Federal Information Processing Standards (FIPS) State Code.  
gediv| integer| Division.  
hehousut| integer| Type of housing unit  
hxhousut| integer| Allocation flag.  
hephoneo| integer| Is a telephone interview acceptable?  
hxphoneo| integer| Allocation flag.  
hetelavl| integer| Is there a telephone elsewhere on which people in this household can be contacted?  
hxtelavl| integer| Allocation flag.  
hetelhhd| integer| Is there a telephone in this house/apartment?  
hxtelhhd| integer| Allocation flag.  
hrhtype| integer| Household type  
hrintsta| integer| Interview status  
hrnumhou| integer| Total number of persons living in the household (household members)  
hefaminc| integer| Family income (combined income of all family members during the last 12 months. Includes money from jobs, net income from business, farm or rent, pensions, dividends, interest, social security payments and any other money income received by family members who are 15 years of age or older.) Note: Caution should be used when using this variable since it has an allocation rate of approximately 20 percent.  
hxfaminc| integer| Allocation flag  
hwhhwgt| integer| Household weight (4 implied decimal places) used for tallying household characteristics  
hwhhwtln| integer| Line number (PULINENO) of the person whose PWSSWGT was donated as HWHHWGT for the household.  
pulineno| integer| Person's line number.  
puchinhh| integer| Change in household composition.  
puwk| integer| Last week, did you do any work for (either) pay (or profit)?  
pubus1| integer| Last week, did you do any unpaid work in the family business or farm?  
pudis| integer| Disability status (last month you were reported to have a disability.) Does your disability continue to prevent you from doing any kind of work for the next 6 months?  
pulay| integer| Last week, were you on layoff from a job?  
puhroff1| integer| Last week, did you lose or take off any hours from your job, for any reason such as illness, slack work, vacation, or holiday?  
puhroff2| integer| How many hours did you take off?  
puhrot1| integer| Last week, did you work any overtime or extra hours (at your main job) that you do not usually work?  
puhrot2| integer| How many additional hours did you work?  
puabsot| integer| Last week did you have a job either full or part-time?  
pubusck1| integer| Check Item 1 filter for questions on unpaid work  
pubusck2| integer| Check Item 2 skips owners of family businesses who did not work last week  
pubusck3| integer| Check Item 3  
pubusck4| integer| Check Item 4  
puretot| integer| Retirement status (last month you were reported to be retired, are you still retired this month?)  
puhrck1| integer| Check item 1 (HRACTT)  
puhrck2| integer| Check Item 2 skips persons responding yes to HRFTPT out of PT series.  
puhrck3| integer| Check Item 3.  
puhrck4| integer| Check Item 4.  
puhrck5| integer| Check Item 5.  
puhrck6| integer| Check Item 6.  
puhrck7| integer| Check Item 7.  
puhrck12| integer| Check Item 12.  
pulaydt| integer| Has your employer given you a date to return to work?  
pulay6m| integer| Have you been given any indication that you will be recalled to work within the next 6 months?  
pulayavr| integer| Why is that?  
pulk| integer| Have you been doing anything to find work during the last 4 weeks?  
pulkavr| integer| Why is that?  
pulayck1| integer| Check Item 1.  
pulayck2| integer| Check Item 2 screen for dependent layoff.  
pulayck3| integer| Check Item 3 filter for dependent I & O.  
pudwck1| integer|   
pudwck2| integer| Screen for disabled  
pudwck3| integer| Filter for retired  
pudwck4| integer| Filter for passive job seekers  
pudwck5| integer| Filter for passive job seekers  
pujhck1| integer| Filter for outgoing rotations  
pujhck2| integer| Filter for persons going through the I and O series  
pujhdp1o| integer| Did you do any of this work in the last 4 weeks?  
pujhck3| integer| Job history check item.  
pujhck4| integer| Screen for dependent NILF.  
pujhck5| integer| Screen for dependent NILF.  
pulkm2| integer| Anything else? (Second method).  
pulkm3| integer| Same as PULKM2 (Third Method).  
pulkm4| integer| Same as PULKM2 (Fourth Method).  
pulkm5| integer| Same as PULKM2 (Fifth Method).  
pulkm6| integer| Same as PULKM2 (Sixth Method).  
pulkdk1| integer| You said you have been trying to find work. How did you go about looking? (First Method).  
pulkdk2| integer|   
pulkdk3| integer| Same as PULKDK2 (Third Method).  
pulkdk4| integer| Same as PULKDK2 (Fourth Method).  
pulkdk5| integer| Same as PULKDK2 (Fifth Method).  
pulkdk6| integer| Same as PULKDK2 (Sixth Method).  
pulkps1| integer| Can you tell me more about what you did to search for work? (First Method).  
pulkps2| integer| Anything else? (Second Method).  
pulkps3| integer| Same as PULKPS2 (Third Method).  
pulkps4| integer| Same as PULKPS2 (Fourth Method).  
pulkps5| integer| Same as PULKPS2 (Fifth Method).  
pulkps6| integer| Same as PULKPS2 (Sixth Method).  
puiock1| integer| I & O Check Item 1 screen for dependent I and O  
puiock2| integer| I & O Check Item 2 screen for previous months I and O cases  
puiock3| integer| I & O Check Item 3  
puiodp1| integer| Last month, it was reported that you worked for (Employer's name). Do you still work for (Employer's name) (at your main job)?  
puiodp2| integer| Have the usual activities and duties of your job changed since last month?  
puiodp3| integer| Last month you were reported as (a/an) (Occupation) and your usual activities were (description). Is this an accurate description of your current job?  
puio1mfg| integer| Is this business or organization mainly manufacturing, retail trade, wholesale trade, or something else?  
puio2mfg| integer| Is this business or organization mainly manufacturing, retail trade, wholesale trade, or something else?  
punlfck1| integer| Not in labor force check item - 1.  
punlfck2| integer| Not in labor force check item - 2.  
puslfprx| integer| Labor force information collected by self or proxy response  
pudis1| integer| Does your disability prevent you from accepting any kind of work during the next six months?  
pudis2| integer| Do you have a disability that prevents you from accepting any kind of work during the next six months?  
pubus2ot| integer| Do you receive any payments or profits from the business?  
perrp| integer| Relationship to Reference Person.  
pxrrp| integer| Allocation flag.  
pxage| integer| Allocation flag.  
peafnow| integer| Are you now in the Armed Forces?  
pxafnow| integer| Allocation flag  
pesex| integer| Sex.  
pxsex| integer| Allocation flag.  
pemaritl| integer| Marital status.  
pxmaritl| integer| Allocation flag.  
pxrace1| integer| Allocation flag  
pehspnon| integer| Hispanic or non-Hispanic.  
pxhspnon| integer| Allocation flag  
peeduca| integer| Highest level of school completed or degree received.  
pxeduca| integer| Allocation flag  
peafever| integer| Did you ever serve on active duty in the U.S. Armed Forces?  
pxafever| integer| Allocation flag.  
peafwhn1| integer| When did you serve?  
pxafwhn1| integer| Allocation flag.  
peafwhn2| integer| When did you serve?  
peafwhn3| integer| When did you serve?  
peafwhn4| integer| When did you serve?  
pespouse| integer| Line number of spouse.  
pxspouse| integer| Allocation flag.  
penatvty| integer| Country of birth.  
pxnatvty| integer| Allocation flag  
pemntvty| integer| Mother's country of birth.  
pxmntvty| integer| Allocation flag  
pefntvty| integer| Father's country of birth.  
pxfntvty| integer| Allocation flag  
pxinusyr| integer| Allocation flag.  
pedipged| integer| How did (they/he/she) get (their/his/her) high school diploma?  
pxdipged| integer|   
pehgcomp| integer| What was the highest grade of regular school (they/he/she) completed before receiving (their/his/her) GED?  
pxhgcomp| integer| Allocation Flag.  
pecyc| integer| How many years of college credit has (they/he/she) completed?  
pxcyc| integer| Allocation Flag Filler 6 840 to 845.  
pepar1| integer| Line number of second parent (always the mother, if present. Will be a male if the parents are same sex).  
pxpar1| integer| Allocation flag.  
pepar2| integer| Line number of first parent (always the father, if present. Will be a female if the parents are same sex).  
pxpar2| integer| Allocation flag.  
pepar1typ| integer| Type of PEPAR1 edited universe: All - 1 No PEPAR2 present.  
pxpar1typ| integer| Allocation flag.  
pepar2typ| integer| Type of PEPAR2 edited universe: All - 1 No PEPAR1 present.  
pxpar2typ| integer| Allocation flag.  
prdasian| integer| Detailed Asian race recode  
prmarsta| integer| Marital status based on Armed Forces participation.  
ptdtrace| integer| Race.  
prdthsp| integer| Detailed Hispanic origin group, revised January 2014.  
prpertyp| integer| Type of person record recode.  
prfamnum| integer| Family number recode.  
prfamtyp| integer| Family type recode.  
prfamrel| integer| Family relationship recode.  
prnmchld| integer| Number of own children < 18 years of age.  
prchld| integer| Presence of own children < 18 years of age by selected age group.  
prcitflg| integer| Citizenship allocation flag  
prcitshp| integer| Citizenship status  
prinuyer| integer|   
prtage| integer| Person's age. Note: This variable was labeled as PEAGE in prior versions of this documentation even though it contained the public use version of age that was top-coded and underwent further masking steps to protect the confidentiality of individuals in the sample.  
prtfage| integer| Top code flag for age.  
pecohab| integer| Line number of cohabiting partner.  
pxcohab| integer| Allocation flag  
peabspdo| integer| Are you being paid by your employer for any of the time off last week?  
peabsrsn| integer| What is the main reason you were absent from work last week?  
pedwavl| integer| Last week, could you have started a job if one had been offered?  
pedwavr| integer| Why is that?  
pedwlko| integer| Did you look for work at any time in the last 12 months?  
pedwlkwk| integer| Since you left that job or business have you looked for work?  
pedwrsn| integer| What is the main reason you were not looking for work during the last 4 weeks?  
pedwwk| integer| Did you actually work at a job or business during the last 12 months?  
pedwwnto| integer| Do you currently want a job, either full or part time?  
pedw4wk| integer| Did you do any of this work during the last 4 weeks?  
pehractt| integer| Sum of PEHRACT1 and PEHRACT2.  
pehract1| integer| Last week, how many hours did you actually work at your job?  
pehract2| integer| Last week, how many hours did you actually work at your other job(s)?  
pehravl| integer| Last week, could you have worked full-time if the hours had been available?  
pehrftpt| integer| Do you usually work 35 hours or more per week?  
pehrrsn1| integer| What is your main reason for working part-time?  
pehrrsn2| integer| What is the main reason you do not want to work full-time?  
pehrrsn3| integer| What is the main reason you worked less than 35 hours last week?  
pehruslt| integer| Sum of HRUSL1 and HRUSL2.  
pehrusl1| integer| How many hours per week do you usually work at your main job?  
pehrusl2| integer| How many hours per week do you usually work at your other job(s)?  
pehrwant| integer| Do you want to work a full-time work week of 35 hours or more per week?  
pejhrsn| integer| What is the main reason you left your last job?  
pejhwant| integer| Do you intend to look for work during the next 12 months?  
pejhwko| integer| Have you worked at a job or business at any time during the past 12 months?  
pelayavl| integer| Could you have returned to work last week if you had been recalled?  
pelaydur| integer| Duration of layoff.  
pelayfto| integer| FT/PT status of job from which sample person was on layoff from.  
pelaylk| integer| Even though you are to be called back to work, have you been looking for work during the last 4 weeks?  
pelkavl| integer| Last week, could you have started a job if one had been offered?  
pelkdur| integer| Duration of job seeking  
pelkfto| integer| FT/PT status of jobseeker  
pelkll1o| integer| Before you started looking for work, what were you doing: working, going to school, or something else?  
pelkll2o| integer| Did you lose or quit that job, or was it a temporary job that ended?  
pelklwo| integer| When last worked?  
pelkm1| integer| What are all of the things you have done to find work during the last 4 weeks? (First method).  
pemjnum| integer| Altogether, how many jobs do you have?  
pemjot| integer| Do you have more than one job?  
pemlr| integer| Monthly labor force recode  
penlfact| integer| What best describes your situation at this time? For example, are you disabled, ill, in school, taking care of house or family, or something else?  
penlfjh| integer| When did you last work at a job or business?  
penlfret| integer|   
peret1| integer| Do you currently want a job, either full or part-time?  
pxabspdo| integer| Allocation flag  
pxabsrsn| integer| Allocation flag  
pxdwavl| integer| Allocation Flag  
pxdwavr| integer| Allocation Flag  
pxdwlko| integer| Allocation flag.  
pxdwlkwk| integer| Allocation Flag  
pxdwrsn| integer| Allocation flag.  
pxdwwk| integer| Allocation Flag  
pxdwwnto| integer| Allocation flag.  
pxdw4wk| integer| Allocation Flag  
pxhractt| integer| Allocation flag.  
pxhract1| integer| Allocation flag.  
pxhract2| integer| Allocation flag.  
pxhravl| integer| Allocation flag.  
pxhrftpt| integer| Allocation flag  
pxhrrsn1| integer| Allocation flag  
pxhrrsn2| integer| Allocation flag.  
pxhrrsn3| integer| Allocation flag.  
pxhruslt| integer| Allocation flag  
pxhrusl1| integer| Allocation flag  
pxhrusl2| integer| Allocation flag  
pxhrwant| integer| Allocation flag  
pxjhrsn| integer| Allocation Flag  
pxjhwant| integer| Allocation Flag  
pxjhwko| integer| Allocation Flag  
pxlayavl| integer| Allocation flag.  
pxlaydur| integer| Allocation flag.  
pxlayfto| integer| Allocation flag.  
pxlaylk| integer| Allocation flag.  
pxlkavl| integer| Allocation flag.  
pxlkdur| integer| Allocation flag.  
pxlkfto| integer| Allocation flag.  
pxlkll1o| integer| Allocation flag.  
pxlkll2o| integer| Allocation flag.  
pxlklwo| integer| Allocation flag.  
pxlkm1| integer| Allocation flag.  
pxmjnum| integer| Allocation flag  
pxmjot| integer| Allocation flag  
pxmlr| integer| Allocation flag  
pxnlfact| integer| Allocation Flag.  
pxnlfjh| integer| Allocation Flag.  
pxnlfret| integer| Allocation Flag.  
pxret1| integer| Allocation flag  
prabsrea| integer| Reason not at work and pay status.  
prcivlf| integer| Civilian labor force.  
prdisc| integer| Discouraged worker recode.  
premphrs| integer| Reason not at work or hours at work.  
prempnot| integer| MLR - Employed, unemployed, or NILF.  
prexplf| integer| Experienced labor force employment.  
prftlf| integer| Full time labor force.  
prhrusl| integer| Usual hours worked weekly.  
prjobsea| integer| Job search recode.  
prpthrs| integer| At work 1 - 34 by hours at work.  
prptrea| integer| Detailed reason for part-time.  
prunedur| integer| Duration of unemployment for layoff and looking records.  
pruntype| integer| Reason for unemployment.  
prwksch| integer| Labor force by time worked or lost.  
prwkstat| integer| Full/part-time work status.  
prwntjob| integer| NILF recode - Want a job or other NILF.  
peio1icd| integer| Industry code for primary job.  
peio2icd| integer| Industry code for second job.  
peio1cow| integer| Individual class of worker code on first job. Note: A PEIO1COW code can be assigned even if an individual is not currently employed.  
peio2cow| integer| Individual class of worker on second job. Note: For those self-employed unincorporated on their first job, this should have a response every month. For all others, this should only have a value in out-going rotations.  
pepdemp1| integer| Does this person usually have any paid employees? See location 637 - 638 for the allocation flag.  
pepdemp2| integer| Does this person usually have any paid employees? See location 787 - 788 for the allocation flag.  
pxio1icd| integer| Allocation Flag  
pxio2icd| integer| Allocation Flag  
pxio1ocd| integer| Allocation Flag  
pxio2ocd| integer| Allocation Flag  
pxio1cow| integer| Allocation Flag  
pxio2cow| integer| Allocation Flag  
pxpdemp1| integer| Allocation flag.  
pxpdemp2| integer| Allocation Flag  
pxnmemp1| integer| Allocation flag  
pxnmemp2| integer| Allocation Flag PXERNWKP 2 Allocation Flag 791 to 792.  
prioelg| integer| Industry and Occupation Eligibility Flag  
premp| integer| Employed persons (non-farm and non-private household) recode  
prcow1| integer| Class of Worker Recode - Job 1  
prcow2| integer| Class of Worker Recode - Job 2  
prnagws| integer| Non-Agriculture Wage and Salary Workers Recode  
prnagpws| integer| Non-Agriculture, Private Wage and Salary Workers Recode  
prdtcow1| integer| Detailed Class of Worker Recode - Job 1  
prdtcow2| integer| Detailed Class of Worker Recode - Job 2  
prmjind1| integer| Major Industry Recode - Job 1  
prmjind2| integer| Major Industry Recode - Job 2  
primind1| integer| Intermediate industry recode (Job 1).  
primind2| integer| Intermediate industry recode (Job 2).  
prmjocc1| integer| Major Occupation Recode - Job 1  
prmjocc2| integer| Major Occupation Recode - Job 2  
prdtind1| integer| Detailed Industry Recode - Job 1  
prdtind2| integer| Detailed Industry Recode - Job 2  
prdtocc1| integer| Detailed Occupation Recode - Job 1  
prdtocc2| integer| Detailed Occupation Recode  
pragna| integer| Agriculture / Non-Agriculture Industry  
prsjmj| integer|   
prcowpg| integer| COW - Private or Government  
prmjocgr| integer| Major Occupation Categories  
peernper| integer| Periodicity  
peernhry| integer| Hourly/Nonhourly Status  
peernuot| integer| Do you usually receive overtime pay, tips, or commissions at your job?  
peernwkp| integer| How many weeks a year do you get paid for?  
peernrt| integer| Even though you told me it is easier to report your earnings (periodicity); are you paid at an hourly rate on your (main/this) job?  
peernhro| integer| Usual hours.  
peernlab| integer| On this job, are you a member of a labor union or of an employee association similar to a union?  
peerncov| integer| On this job, are you covered by a union or employee association contract?  
pxernper| integer| Allocation Flag  
pxernhry| integer| Allocation Flag.  
pxernuot| integer| Allocation Flag  
pxernwkp| integer|   
pxernrt| integer| Allocation Flag.  
pxernh2| integer| Allocation Flag.  
pxernh1o| integer| Allocation Flag  
pxernhro| integer| Allocation Flag  
pxern| integer| Allocation Flag  
pxernlab| integer| Allocation Flag.  
pxerncov| integer| Allocation Flag.  
prerelg| integer| Earnings Eligibility Flag  
prwernal| integer| Allocation flag weekly earnings recode (PTERNWA) allocation flag.  
prhernal| integer| Allocation flag hourly earnings recode (PTERNHLY) allocation flag.  
peschlvl| integer| Would that be high school, college, or university?  
peschenr| integer| Last week, were you enrolled in a high school, college, or university?  
peschft| integer| Are you enrolled in school as a full-time or part-time student?  
pxschlvl| integer| Allocation Flag.  
pxschenr| integer| Allocation Flag.  
pxschft| integer| Allocation Flag.  
prnlfsch| integer| NLF activity - in school or not in school.  
pedisear| integer| Is this person deaf or does he/she have serious difficulty hearing?  
pediseye| integer| Is this person blind or does he/she have serious difficulty seeing even when wearing glasses?  
pedisrem| integer| Because of a physical, mental, or emotional condition, does he/she have serious difficulty concentrating, remembering, or making decisions?  
pedisphy| integer| Does he/she have serious difficulty walking or climbing stairs?  
pedisdrs| integer| Does he/she have difficulty dressing or bathing?  
pedisout| integer| Because of a physical, mental, or emotional condition, does he/she have difficulty doing errands alone such as visiting a doctor's office or shopping?  
pxdisear| integer| Allocation flag  
pxdiseye| integer| Allocation flag  
pxdisrem| integer| Allocation flag  
pxdisphy| integer| Allocation flag  
pxdisdrs| integer| Allocation flag  
pxdisout| integer| Allocation flag  
prdisflg| integer| Does this person have any of these disability conditions?  
pecert1| integer|   
pecert2| integer|   
pecert3| integer|   
pxcert1| integer|   
pxcert2| integer|   
pxcert3| integer|   
pwsswgt| integer| Final weight (4 implied decimal places) used for most tabulations, controlled to independent estimates for 1) states; 2) origin, sex, and age; and 3) age, race, and sex.  
pwlgwgt| integer| Longitudinal weight (4 implied decimals) only found on adult records matched from month to month (used for gross flows analysis).  
pwvetwgt| integer| Veterans weight (4 implied decimals) used for tallying veteran's data only, controlled to estimates of veterans supplied by VA.  
pworwgt| integer| Outgoing rotation weight (4 implied decimals) used for tallying information collected only in outgoing rotations (i.e., earnings, 2nd job I & O, detailed NILF).  
pwfmwgt| integer| Family weight (4 implied decimals) only used for tallying family characteristics.  
pwcmpwgt| integer| Composited Final Weight. Used to create BLS's published labor force statistics (4 implied decimal places).  
prernmin| integer|   
pternhly| integer| Recode for hourly rate  
pternh1o| integer| Out variable for hourly rate of pay (2 implied decimals)  
pternh2| integer| (Excluding overtime pay, tips and commissions) What is your hourly rate of pay on your (main/this) job? Dollar amount – 2 implied decimals  
pternh1c| integer| What is your hourly rate of pay on this job, excluding overtime pay, tips or commission? Dollar amount – 2 implied decimals  
pternwa| integer| Weekly earnings recode.  
ptern| integer| Calculated weekly overtime amount.  
ptern2| integer| Calculated weekly overtime amount.  
ptio1ocd| integer| Occupation code for primary job.  
ptio2ocd| integer| Occupation code for second job.  
pthr| integer| Hourly Pay - Top Code  
ptwk| integer| Weekly earnings - top code.  
ptot| integer| Weekly overtime amount - top code.  
ptnmemp1| integer| Excluding all owners, how many paid employees does this person usually have? See location 681 - 682 for the allocation flag.  
ptnmemp2| integer| Excluding all owners, how many paid employees does this person usually have? See location 789 - 790 for the allocation flag.  
hrhhid| integer| Household Identifier (Part 1)  
gtcbsa| integer| Specific Metropolitan CBSA Code (see Geographic Attachment).  
gtco| integer| FIPS County Code.  
gtcbsast| integer| Principal City/Balance Status.  
gtcbsasz| integer| Metropolitan Area (CBSA) Size.  
gtcsa| integer| Consolidated Statistical Area (CSA) FIPS Code (see Geographic Attachment).  
gtmetsta| integer| Metropolitan Status.  
gtindvpc| integer| Individual Principal City.  
  
### variable_descriptions

Column Name| Data Type| Description  
---|---|---  
column| string|   
desc| text|   
  
### variable_values

Column Name| Data Type| Description  
---|---|---  
column| string|   
var_val| integer|   
desc| text|   
  
## References

Urls used in the creation of this data package.

  * **[jan23](<https://www2.census.gov/programs-surveys/cps/datasets/2023/basic/jan23pub.csv>)**. January 2023
  * **[data_dictionary_text](<https://www2.census.gov/programs-surveys/cps/datasets/2023/basic/2023_Basic_CPS_Public_Use_Record_Layout_plus_IO_Code_list.txt>)**. Original text of the data dictionary
  * **[cps202301_source](<https://www2.census.gov/programs-surveys/cps/datasets/2023/basic/jan23pub.csv>)**. 


## Packages

  * **s3** s3://library.metatab.org/census.gov-cps-2023-basic_monthly-1.1.2.csv
  * **csv** <https://library-metatab-org.s3.amazonaws.com/census.gov-cps-2023-basic_monthly-1.1.2.csv>
  * **source** <https://github.com/metatab-packages/census.gov-cps-2023-basic_monthly.git>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    variable_descriptions_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-cps-2023-basic_monthly-1.1.2/data/variable_descriptions.csv')
    variable_values_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-cps-2023-basic_monthly-1.1.2/data/variable_values.csv')
    cps202301_df =  pd.read_csv('https://library-metatab-org.s3.amazonaws.com/census.gov-cps-2023-basic_monthly-1.1.2/data/cps202301.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library-metatab-org.s3.amazonaws.com/census.gov-cps-2023-basic_monthly-1.1.2.csv')
    
    # Create Dataframes
    variable_descriptions_df = pkg.resource('variable_descriptions').dataframe()
    variable_values_df = pkg.resource('variable_values').dataframe()
    cps202301_df = pkg.resource('cps202301').dataframe()
    
[/code]
