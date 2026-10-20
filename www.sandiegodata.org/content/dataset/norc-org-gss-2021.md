---
title: "General Social Survey"
date: 2023-03-03T21:47:58+00:00
draft: false
categories: ["Dataset", "Uncategorized"]
tags: ["norc.org"]
author: "metapack"
description: "General Social Survey collects information and keeps a historical record of the"
---

_General Social Survey collects information and keeps a historical record of the concerns, experiences, attitudes, and practices of residents of the United States._

`norc.org-gss-2021-1.1.1`. Modified 2023-03-04T17:10:58

Resources | Packages | Documentation| Contacts| References| Data Dictionary

## Resources

  * **[gss_2021](<https://library.metatab.org/norc.org-gss-2021-1.1.1/data/gss_2021.csv>)**. General Social Survey 2021


## Documentation

## Caveats

This package is an extract meant for a specific workflow. For general analysis, you should almost certainly use an extract generated from the [GSS website](<https://gss.norc.org/>). 

## Using the Data Files

The variables in this package are almost entirely categorical, but the data is stored with codes, with the categorical labels stored seperately in the `_labels` reference. When opening the file with Metapack, the `convert_categorical` argument ( which defaults to `True` ) controls converting the codes to labels. 
[code] 
    pkg.resource('gss_2021').dataframe(convert_categorical=True)
    
[/code]

Because the default is `True` this should happen automatically when using `.dataframe`, but it is good to know what is happening behind the scenes.

### Documentation Links

  * [Documentation Page](<https://library.metatab.org/norc.org-gss-2021-1.1.1/index.html>)
  * [General Social Survey](<https://gss.norc.org/>) GSS Homepage at NORC
  * [Download page](<https://gss.norc.org/get-the-data/stata>)


## Contacts

  * **Wrangler**

[Eric Busboom](<mailto:eric@civicknowledge.com>), [Civic Knowledge](<http://civicknowledge.com>)


## Data Dictionary

gss_2021   


### gss_2021

Column Name| Data Type| Description  
---|---|---  
year| integer|   
id| integer|   
wrkslf| integer| (Are/Were) you self employed or (do/did) you work for someone else?  
wrkgovt| integer|   
occ10| integer| RESPONDENT'S OCCUPATION  
prestg10| integer| PRESTIGE OF RESPONDENT'S OCCUPATION  
indus10| integer| RESPONDENT'S INDUSTRY  
marital| integer| Are you currently married, widowed, divorced, separated, or have you never been married?  
martype| integer| CODE TYPE OF MARRIAGE  
divorce| integer| IF CURRENTLY MARRIED OR WIDOWED: Have you ever been divorced or legally separated?  
widowed| integer| IF CURRENTLY MARRIED, SEPARATED, OR DIVORCED: Have you ever been widowed?  
spwrksta| integer| Last week was your (wife/husband) working full time, part time, going to school, keeping house, or what?  
sphrs1| integer| (Last week was your (wife/husband) working full time, part time, going to school, keeping house, or what?...) IF WORKING, FULL OR PART TIME: How many hours did (he/she) work last week, at all jobs?  
sphrs2| integer| IF WITH A JOB, BUT NOT AT WORK: How many hours a week does your spouse usually work, at all jobs?  
spevwork| integer| IF RETIRED, IN SCHOOL, KEEPING HOUSE, OR OTHER: Did your spouse ever work for as long as one year?  
cowrksta| integer| Last week was your partner working full time, part time, going to school, keeping house, or what?  
coevwork| integer| IF RETIRED, IN SCHOOL, KEEPING HOUSE, OR OTHER: Did your partner ever work for as long as one year?  
cohrs1| integer| IF WORKING, FULL OR PART TIME: How many hours did your partner work last week, at all jobs?  
cohrs2| integer| IF WITH A JOB, BUT NOT AT WORK: How many hours a week does your partner usually work, at all jobs?  
spocc10| integer| RESPONDENT'S SPOUSE'S OCCUPATION  
sppres10| integer| PRESTIGE OF RESPONDENT'S SPOUSE'S OCCUPATION  
spind10| integer| RESPONDENT'S SPOUSE'S INDUSTRY  
coocc10| integer| RESPONDENT'S PARTNER'S OCCUPATION  
coind10| integer| RESPONDENT'S PARTNER'S INDUSTRY  
pawrkslf| integer| Was your [father/stepfather/male relative you were living with when you were 16] an employee, self-employed without employees, or self-employed with employees?  
paocc10| integer| FATHER'S OCCUPATION  
papres10| integer| PRESTIGE OF RESPONDENT'S FATHER'S OCCUPATION  
paind10| integer| FATHER'S INDUSTRY  
mawrkslf| integer| At this job, was [mother/stepmother/female realtive you were living with when you were 16] an employee, self-employed without employees, or self-employed with employees?  
maocc10| integer| MOTHER'S OCCUPATION  
mapres10| integer| PRESTIGE OF RESPONDENT'S MOTHER'S OCCUPATION  
maind10| integer| MOTHER'S INDUSTRY CODE  
sibs| integer| How many brothers and sisters did you have? Please count those born alive, but no longer living, as well as those alive now. Also include stepbrothers and stepsisters, and children adopted by your parents.  
childs| integer| How many children have you ever had? Please count all that were born alive at any time (including any you had from a previous marriage).  
age| integer| RESPONDENT'S AGE  
agekdbrn| integer| How old were you when your first child was born?  
educ| integer| RESPONDENT'S EDUCATION  
paeduc| integer| What is the highest grade in elementary school or high school that your father finished and got credit for?  
maeduc| integer| What is the highest grade in elementary school or high school that your mother finished and got credit for?  
degree| integer| RESPONDENT'S DEGREE  
dipged| integer|   
sex| integer| CODE RESPONDENT'S SEX  
race| integer| What race do you consider yourself? RECORD VERBATIM AND CODE. CODE WITHOUT ASKING ONLY IF THERE IS NO DOUBT IN YOUR MIND.  
res16| integer| Which of these categories comes closest to the type of place you were living in when you were 16 years old?  
reg16| integer| In what state or foreign country were you living when you were 16 years old?  
mobile16| integer| IF STATE NAMED IS SAME STATE R. LIVES IN NOW, ASK MOBILE16: When you were 16 years old, were you living in this same (city/town/county)?  
famdif16| integer| IF NOT LIVING WITH BOTH OWN MOTHER AND FATHER: What happened?  
mawrkgrw| integer| Did your mother ever work for pay for as long as a year, while you were growing up?  
incom16| integer| Thinking about the time when you were 16 years old, compared with American families in general then, would you say your family income was: far below average, below average, average, above average, or far above average? (PROBE: Just your best guess.)  
born| integer| Were you born in this country?  
granborn| integer| (Were all of your four grandparents born in this country?...) IF NO: How many were born outside the United States?  
preteen| integer| NUMBER OF MEMBERS 6 TO 12 YEARS. 6-12 YEARS  
earnrs| integer| Just thinking about your family now--those people in the household who are related to you . . . How many persons in the family (including yourself) earned any money in (2019/2020) from any job or employment?  
income| integer| In which of these groups did your total family income, from all sources, fall last year before taxes, that is?  
income16| integer| In which of these groups did your total family income, from all sources, fall last year? That is, before taxes.  
rincom16| integer| In which of these groups did your earnings from (OCC), from all sources for (2019/2020) fall? That is, before taxes or other deductions.  
region| integer| REGION OF INTERVIEW  
partyid| integer| Generally speaking, do you usually think of yourself as a Republican, Democrat, Independent, or what?  
vote16| integer| In 2016, you remember that Hillary Clinton ran for President on the Democratic ticket against Donald Trump for the Republicans. Do you remember for sure whether or not you voted in that election?  
pres16| integer| Did you vote for Hillary Clinton or Donald Trump?  
if16who| integer| Who would you have voted for, for president, if you had voted?  
polviews| integer| We hear a lot of talk these days about liberals and conservatives. I'm going to show you a seven-point scale on which the political views that people might hold are arranged from extremely liberal--point 1--to extremely conservative--point 7. Where would you place yourself on this scale?  
natspac| integer| (Letâs begin with some things people think about today. We are faced with many problems in this country, none of which can be solved easily or inexpensively. I'm going to name some of these problems, and for each one I'd like you to tell me whether you think we're spending too much money on it, too little money, or about the right amount.) Space exploration program  
natenvir| integer| (... are we spending too much, too little, or about the right amount on) Improving and protecting the environment  
natheal| integer| (... are we spending too much, too little, or about the right amount on) Improving and protecting the nation's health  
natcity| integer| (... are we spending too much, too little, or about the right amount on) Solving the problems of big cities  
natcrime| integer| (... are we spending too much, too little, or about the right amount on) Halting the rising crime rate  
natdrug| integer| (... are we spending too much, too little, or about the right amount on) Dealing with drug addiction  
nateduc| integer| (... are we spending too much, too little, or about the right amount on) Improving the nation's education system  
natrace| integer| (... are we spending too much, too little, or about the right amount on) Improving the conditions of Blacks  
natarms| integer| (... are we spending too much, too little, or about the right amount on) The military, armaments, and defense  
nataid| integer| (... are we spending too much, too little, or about the right amount on) Foreign aid  
natfare| integer| (... are we spending too much, too little, or about the right amount on) Welfare  
natroad| integer| (... are we spending too much, too little, or about the right amount on) Highways and bridges  
natsoc| integer| (... are we spending too much, too little, or about the right amount on) Social Security  
natmass| integer| (... are we spending too much, too little, or about the right amount on) Mass Transportation  
natpark| integer| (... are we spending too much, too little, or about the right amount on) Parks and recreation  
natchld| integer| (... are we spending too much, too little, or about the right amount on) Assistance for childcare  
natsci| integer| (... are we spending too much, too little, or about the right amount on) Supporting scientific research  
natenrgy| integer| (... are we spending too much, too little, or about the right amount on) Developing alternative energy sources  
natspacy| integer| (... are we spending too much, too little, or about the right amount on) Space exploration  
natenviy| integer| Improving and protecting the environment  
nathealy| integer| (... are we spending too much, too little, or about the right amount on) Health  
natcityy| integer| (... are we spending too much, too little, or about the right amount on) Assistance to big cities  
natcrimy| integer| (... are we spending too much, too little, or about the right amount on) Law enforcement  
natdrugy| integer| (... are we spending too much, too little, or about the right amount on) Drug rehabilitation  
nateducy| integer| (... are we spending too much, too little, or about the right amount on) Education  
natracey| integer| (... are we spending too much, too little, or about the right amount on) Assistance to Blacks  
natarmsy| integer| (... are we spending too much, too little, or about the right amount on) National defense  
nataidy| integer| (... are we spending too much, too little, or about the right amount on) Assistance to other countries  
natfarey| integer| (... are we spending too much, too little, or about the right amount on) Assistance to the poor  
eqwlth| integer| Some people think that the government in Washington ought to reduce the income differences between the rich and the poor, perhaps by raising the taxes of wealthy families or by giving income assistance to the poor. Others think that the government should not concern itself with reducing this income difference between the rich and the poor. Here is a scale from 1 to 7. Think of a score of 1 as meaning that the government ought to reduce the income differences between rich and poor, and a score of 7 meaning that the government should not concern itself with reducing income differences. What score between 1 and 7 comes closest to the way you feel?  
tax| integer| Do you consider the amount of federal income tax which you have to pay as too high, about right, or too low?  
spkath| integer| There are always some people whose ideas are considered bad or dangerous by other people. For instance, somebody who is against all churches and religion . . . If such a person wanted to make a speech in your (city/town/community) against churches and religion, should he be allowed to speak, or not?  
colath| integer| (There are always some people whose ideas are considered bad or dangerous by other people. For instance, somebody who is against all churches and religionâ¦) Should such a person be allowed to teach in a college or university, or not?  
libath| integer| (There are always some people whose ideas are considered bad or dangerous by other people. For instance, somebody who is against all churches and religionâ¦) If some people in your community suggested that a book he wrote against churches and religion should be taken out of your public library, would you favor removing this book, or not?  
spkrac| integer| Or consider a person who believes that Blacks are genetically inferior. If such a person wanted to make a speech in your community claiming that Blacks are inferior, should he be allowed to speak, or not?  
colrac| integer| (Or consider a person who believes that Blacks are genetically inferiorâ¦) Should such a person be allowed to teach in a college or university, or not?  
librac| integer| (Or consider a person who believes that Blacks are genetically inferiorâ¦) If some people in your community suggested that a book he wrote which said Blacks are inferior should be taken out of your public library, would you favor removing this book, or not?  
spkcom| integer| Now,we would like to ask you some questions about a man who admits he is a Communist. Suppose this admitted Communist wanted to make a speech in your community. Should he be allowed to speak, or not?  
colcom| integer| (Now,we would like to ask you some questions about a man who admits he is a Communistâ¦) Suppose he is teaching in a college. Should he be fired, or not?  
libcom| integer| (Now,we would like to ask you some questions about a man who admits he is a Communistâ¦) Suppose he wrote a book which is in your public library. Somebody in your community suggests that the book should be removed from the library. Would you favor removing it, or not?  
spkmil| integer| Consider a person who advocates doing away with elections and letting the military run the country. If such a person wanted to make a speech in your community, should he be allowed to speak, or not?  
colmil| integer| (Consider a person who advocates doing away with elections and letting the military run the countryâ¦) Should such a person be allowed to teach in a college or university, or not?  
libmil| integer| Suppose he wrote a book advocating doing away with elections and letting the military run the country. Somebody in your community suggests that the book be removed from the public library. Would you favor removing it, or not?  
spkhomo| integer| And what about a man who admits that he is homosexualâ¦ Suppose this admitted homosexual wanted to make a speech in your community. Should he be allowed to speak, or not?  
colhomo| integer| Should such a person be allowed to teach in a college or university, or not?  
libhomo| integer| (And what about a man who admits that he is homosexualâ¦) If some people in your community suggested that a book he wrote in favor of homosexuality should be taken out of your public library, would you favor removing this book, or not?  
spkmslm| integer| Now consider a Muslim clergyman who preaches hatred of the United States. If such a person wanted to make a speech in your community preaching hatred of the United States, should he be allowed to speak, or not?  
colmslm| integer| Should such a person be allowed to teach in a college or university, or not?  
libmslm| integer| (Now consider a Muslim clergyman who preaches hatred of the United Statesâ¦) If some people in your community suggested that a book he wrote which preaches hatred of the United States should be taken out of your public library, would you favor removing this book, or not?  
cappun| integer| Do you favor or oppose the death penalty for persons convicted of murder?  
gunlaw| integer| Would you favor or oppose a law which would require a person to obtain a police permit before he or she could buy a gun?  
relig| integer| What is your religious preference? Is it Protestant, Catholic, Jewish, some other religion, or no religion?  
denom| integer| (PROBE FOR EXACT DENOMINATION)  
other| integer| if any?(PROBE FOR EXACT DENOMINATION)  
jew| integer| Conservative, Reform or none of these? (PROBE FOR EXACT DENOMINATION)  
fund| integer| Fundamentalism/Liberalism of Respondent's Religion  
attend| integer| How often do you attend religious services? (USE CATEGORIES AS PROBES, IF NECESSARY.)  
pray| integer| About how often do you pray? (USE CATEGORIES AS PROBES.)  
popespks| integer| We are interested in what American Catholics think about religious matters. Please select the answer that comes closest to your own personal opinion about the following statement: Under certain conditions,the pope is infallible when he speaks on matters of faith and morals.  
relig16| integer| In what religion were you raised?  
denom16| integer| (PROBE FOR EXACT DENOMINATION)  
oth16| integer| (PROBE FOR EXACT DENOMINATION)  
jew16| integer| Reform, or none of these? (PROBE FOR EXACT DENOMINATION)  
fund16| integer| IF JEWISH: Fundamentalism/Liberalism of Religion Respondent Raised In  
sprel| integer| IF R CURRENTLY MARRIED, ASK Q. 120 and 121 (OTHERS, SKIP SPREL and SPREL16) What is your (SPOUSE'S) religious preference? Is it Protestant, Catholic, Jewish, some other religion, or no religion?  
spden| integer| (What is your(SPOUSE'S) religious preference? Is it Protestant, Catholic, Jewish, some other religion, or no religion?...) What specific denomination is that, if any? (PROBE FOR EXACT DENOMINATION)  
spother| integer| Please specify denomination:  
spjew| integer| (What is your(SPOUSE'S) religious preference? Is it Protestant, Catholic, Jewish, some other religion, or no religion?...) Does (s/he) consider (her/himself) Orthodox, Conservative, Reform or none of these? (PROBE FOR EXACT DENOMINATION)  
spfund| integer| (What is your(SPOUSE'S) religious preference? Is it Protestant, Catholic, Jewish, some other religion, or no religion?...) Fundamentalism/Liberalism of Religion of Spouse  
corel| integer| What is your partner's religious preference? Is it Protestant, Catholic, Jewish, some other religion, or no religion? (PROBE FOR EXACT DENOMINATION)  
coden| integer| (What is your partner's religious preference? Is it Protestant, Catholic, Jewish, some other religion, or no religion?...) What specific denomination is that, if any? (PROBE FOR EXACT DENOMINATION)  
coother| integer| (What is your partner's religious preference? Is it Protestant, Catholic, Jewish, some other religion, or no religion?...) What specific denomination is that, if any? (PROBE FOR EXACT DENOMINATION)  
cojew| integer| IF JEWISH: Doeyour partner considehis/herself Orthodox, Conservative, Reform or none of these? (PROBE FOR EXACT DENOMINATION)  
raclive| integer| Are there any (âwhitesâ for black respondents, âblacksâ for non-black respondents) living in this neighborhood now?  
affrmact| integer| Some people say that because of past discrimination, Blacks should be given preference in hiring and promotion. Others say that such preference in hiring and promotion of Blacks is wrong because it discriminates against Whites. What about your opinion? Are you for or against preferential hiring and promotion of Blacks? IF FAVORS: Do you favor preference in hiring and promotion strongly or not strongly? IF OPPOSES: Do you oppose preference in hiring and promotion strongly or not strongly?  
wrkwayup| integer| Do you agree strongly, agree somewhat, neither agree nor disagree, disagree somewhat, or disagree strongly with the following statement: Irish, Italians, Jewish and many other minorities overcame prejudice and worked their way up. Blacks should do the same without special favors.  
happy| integer| Taken all together, how would you say things are these days--would you say that you are very happy, pretty happy, or not too happy?  
hapmar| integer| (IF CURRENTLY MARRIED, ASK HAPMAR) Taking things all together, how would you describe your marriage? Would you say that your marriage is very happy, pretty happy, or not too happy?  
hapcohab| integer| (IF CURRENTLY UNMARRIED OR ANSWERED PUNCHES 1 OR 2 FOR POSSLQ OR POSSLQY, ASK HAPCOHAB) Taking things all together, would you say that your relationship with your partner is very happy, pretty happy, or not too happy?  
health| integer| Would you say your own health, in general, is excellent, good, fair, or poor?  
life| integer| In general, do you find life exciting, pretty routine, or dull?  
confinan| integer| (I am going to name some institutions in this country. As far as the people running this institution are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Banks and financial institutions  
conbus| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Major companies  
conclerg| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Organized religion  
coneduc| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Education  
confed| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Executive branch of the federal government  
conlabor| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Organized labor  
conpress| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Press  
conmedic| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Medicine  
contv| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) TV  
conjudge| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) U.S. Supreme Court  
consci| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Scientific Community  
conlegis| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Congress  
conarmy| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Military  
obey| integer| (If you had to choose, which thing on this list would you pick as the most important for a child to learn to prepare him or her for life? Which comes next in importance? Which comes third? Which comes fourth?) To obey  
popular| integer| (If you had to choose, which thing on this list would you pick as the most important for a child to learn to prepare him or her for life? Which comes next in importance? Which comes third? Which comes fourth?) To be well-liked or popular  
thnkself| integer| (If you had to choose, which thing on this list would you pick as the most important for a child to learn to prepare him or her for life? Which comes next in importance? Which comes third? Which comes fourth?) To think for himself or herself  
workhard| integer| (If you had to choose, which thing on this list would you pick as the most important for a child to learn to prepare him or her for life? Which comes next in importance? Which comes third? Which comes fourth?) To work hard  
helpoth| integer| (If you had to choose, which thing on this list would you pick as the most important for a child to learn to prepare him or her for life? Which comes next in importance? Which comes third? Which comes fourth?) To help others when they need help.  
socrel| integer| (For each of the next four questions, please select the answer that comes closest to how often you do the following thingsâ¦) How often do you spend a social evening with relatives?  
socommun| integer| (For each of the next four questions, please select the answer that comes closest to how often you do the following thingsâ¦) How often do you spend a social evening with someone who lives in your neighborhood?  
socfrend| integer| (For each of the next four questions, please select the answer that comes closest to how often you do the following thingsâ¦) Spend a social evening with friends who live outside the neighborhood?  
socbar| integer| (For each of the next four questions, please select the answer that comes closest to how often you do the following thingsâ¦) Go to a bar or tavern?  
joblose| integer| Thinking about the next 12 months, how likely do you think it is that you will lose your job or be laid off--very likely, fairly likely, not too likely, or not at all likely?  
jobfind| integer| About how easy would it be for you to find a job with another employer with approximately the same income and fringe benefits you now have? Would you say very easy, somewhat easy, or not easy at all?  
satjob| integer| On the whole, how satisfied are you with the work you do -would you say you are very satisfied, moderately satisfied, a little dissatisfied, or very dissatisfied?  
richwork| integer| (IF CURRENTLY WORKING OR TEMPORARILY NOT AT WORK, ASK RICHWORK.) If you were to get enough money to live as comfortably as you would like for the rest of your life, would you continue to work or would you stop working?  
class| integer| If you were asked to use one of four names for your social class, which would you say you belong in: the lower class, the working class, the middle class, or the upper class?  
rank| integer| (In our society there are groups which tend to be towards the top and those that are towards the bottom. Here we have a scale that runs from top to bottomâ¦) Where would you put yourself on this scale?  
satfin| integer| We are interested in how people are getting along financially these days. So far as you and your family are concerned, would you say that you are pretty well satisfied with your present financial situation, more or less satisfied, or not satisfied at all?  
finalter| integer| During the last few years, has your financial situation been getting better, worse, or has it stayed the same?  
finrela| integer| Compared with American families in general, would you say your family income is far below average, below average, average, above average, or far above average? (PROBE: Just your best guess.)  
wksub| integer| We have some more questions about [your/your spouse's] job. At work, [do you/does your spouse] have a supervisor to whom [you/he or she] are directly responsible?  
wksubs| integer| IF YES: Does that supervisor have a supervisor to whom he or she is directly responsible?  
wksub1| integer| Do you (does your (SPOUSE or PARTNER) have a supervisor on (your/his/her) job to whom you are (he/she/is) directly responsible?  
wksubs1| integer| IF YES: Does that person have a supervisor on the job to whom he is directly responsible?  
wksup| integer| At work, [do you/does your spouse] supervise anyone who is directly responsible to [you/your spouse]?  
wksups| integer| Is anyone that [you supervise/your spouse supervises] the direct supervisor of somebody else?  
wksup1| integer| In your (SPOUSE or PARTNER'S) job, (do you/does he/she) supervise anyone who is directly responsible to (you/him/her)?  
wksups1| integer| IF YES: Do any of those persons supervise anyone else?  
union| integer|   
union1| integer| Do you (or your spouse or partner) belong to a labor union? (Who?)  
parsol| integer| Compared to your parents when they were the age you are now, do you think your own standard of living now is much better, somewhat better, about the same, somewhat worse, or much worse than theirs was?  
abdefect| integer| (Please tell me whether or not you think it should be possible for a pregnant woman to obtain a legal abortion if. . .) If there is a strong chance of serious defect in the baby?  
abnomore| integer| If she is married and does not want any more children?  
abhlth| integer| If the woman's own health is seriously endangered by the pregnancy?  
abpoor| integer| If the family has a very low income and cannot afford any more children?  
abrape| integer| If she becomes pregnant as a result of rape?  
absingle| integer| If she is not married and does not want to marry the man?  
abany| integer| If the woman wants it for any reason?  
chldidel| integer| What do you think is the ideal number of children for a family to have?  
pillok| integer| Do you strongly agree, agree, disagree, or strongly disagree that methods of birth control should be available to teenagers between the ages of 14 and 16 if their parents do not approve?  
sexeduc| integer| Would you be for or against sex education in the public schools?  
premarsx| integer| There's been a lot of discussion about the way morals and attitudes about sex are changing in this country. If a man and a woman have sexual relations before marriage, do you think it is always wrong, almost always wrong, wrong only sometimes, or not wrong at all?  
teensex| integer| What if they are in their early teens, say 14 to 16 years old? In that case, do you think sex relations before marriage are always wrong, almost always wrong, wrong only sometimes, or not wrong at all?  
xmarsex| integer| What is your opinion about a married person having sexual relations with someone other than the marriage partner--is it always wrong, almost always wrong, wrong only sometimes, or not wrong at all?  
homosex| integer| What about sexual relations between two adults of the same sex--do you think it is always wrong, almost always wrong, wrong only sometimes, or not wrong at all?  
pornlaw| integer| Which of these statements comes closest to your feelings about pornography laws?  
xmovie| integer| Have you seen an X-rated movie in the last year?  
spanking| integer| Do you strongly agree, agree, disagree, or strongly disagree that it is sometimes necessary to discipline a child with a good, hard spanking?  
letdie1| integer| When a person has a disease that cannot be cured, do you think doctors should be allowed by law to end the patient's life by some painless means if the patient and his family request it?  
suicide1| integer| (Do you think a person has the right to end his or her own life if this person . . .) Has an incurable disease?  
suicide2| integer| (Do you think a person has the right to end his or her own life if this person . . .) Has gone bankrupt?  
suicide3| integer| (Do you think a person has the right to end his or her own life if this person . . .) Has dishonored his or her family?  
suicide4| integer| (Do you think a person has the right to end his or her own life if this person . . .) Is tired of living and ready to die?  
polhitok| integer| Are there any situations you can imagine in which you would approve of a policeman striking an adult male citizen?  
polabuse| integer| (Would you approve of a policeman striking a citizen who...) Had said vulgar and obscene things to the policeman?  
polmurdr| integer| (Would you approve of a policeman striking a citizen whoâ¦) Was being questioned as a suspect in a murder case?  
polescap| integer| Was attempting to escape from custody?  
polattak| integer| Was attacking the policeman with his fists?  
fear| integer| Is there any area right around here--that is, within a mile--where you would be afraid to walk alone at night?  
owngun| integer| Do you happen to have in your home (IF HOUSE: or garage) any guns or revolvers?  
pistol| integer| Is it a pistol, shotgun, rifle, or what? CODE ALL THAT APPLY. [Coded if Pistol]  
shotgun| integer|   
rifle| integer|   
rowngun| integer| Do any of these guns personally belong to you?  
hunt| integer| And now a question on a different topic. [(Do you/Do you or does your spouse] go hunting?  
hunt1| integer|   
news| integer| How often do you read the newspaper--every day, a few times a week, once a week, less than once a week, or never?  
tvhours| integer| On the average day, about how many hours do you personally watch television?  
phone| integer| Thank you very much for your time and help. Do you have a telephone? May I have your name and (one of your) telephone number(s) just in case I have left something out in this interview?  
coop| integer| (FOR INTERVIEWERS) In general, what was the respondent's attitude toward the interview?  
comprend| integer| (FOR INTERVIEWERS) Was respondent's understanding of the questionsâ¦  
form| integer| FORM OF SPLIT QUESTIONNAIRE ASKED  
fechld| integer| Please read the following statements and indicate whether you strongly agree, agree, disagree, or strongly disagree with each statement. For example, here is the statement: A working mother can establish just as warm and secure a relationship with her children as a mother who does not work.  
fepresch| integer| (Please read the following statements and indicate whether you strongly agree, agree, disagree, or strongly disagree with each statementâ¦) A preschool child is likely to suffer if his or her mother works.  
fefam| integer| (Please read the following statements and indicate whether you strongly agree, agree, disagree, or strongly disagree with each statementâ¦) It is much better for everyone involved if the man is the achiever outside the home and the woman takes care of the home and family.  
racdif1| integer| On the average (Negroes/Blacks/African-Americans) have worse jobs, income, and housing than white people. Do you think these differences are . . . Mainly due to discrimination?  
racdif2| integer| (On the average (Negroes/Blacks/African-Americans) have worse jobs, income, and housing than white people. Do you think these differences are . . .) Because most (Negroes/Blacks/African-Americans) have less in-born ability to learn?  
racdif3| integer| (On the average (Negroes/Blacks/African-Americans) have worse jobs, income, and housing than white people. Do you think these differences are . . .) Because most (Negroes/Blacks/African-Americans) don't have the chance for education that it takes to rise out of poverty?  
racdif4| integer| (On the average (Negroes/Blacks/African-Americans) have worse jobs, income, and housing than white people. Do you think these differences are . . .) Because most (Negroes/Blacks/African-Americans) just don't have the motivation or willpower to pull themselves up out of poverty?  
helppoor| integer| Next, here are issues that some people tell us are important. Some people think that the government in Washington should do everything possible to improve the standard of living of all poor Americans, they are at Point 1 on the scale below. Other people think it is not the governmentâs responsibility, and that each person should take care of himself, they are at Point 5. Where would you place yourself on this scale, or haven't you made up your mind on this?  
helpnot| integer| Some people think that the government in Washington is trying to do too many things that should be left to individuals and private businesses. Others disagree and think that the government should do even more to solve our country's problems. Still others have opinions somewhere in between. Where would you place yourself on this scale, or haven't you made up your mind on this?  
helpsick| integer| In general, some people think that it is the responsibility of the government in Washington to see to it that people have help in paying for doctors and hospital bills. Others think that these matters are not the responsibility of the federal government and that people should take care of these things themselves. Where would you place yourself on this scale, or haven't you made up your mind on this?  
helpblk| integer| Some people think that Blacks have been discriminated against for so long that the government has a special obligation to help improve their living standards. Others believe that the government should not be giving special treatment to Blacks. Where would you place yourself on this scale, or haven't you made up your mind on this?  
god| integer| Which of the statements comes closest to expressing what you believe about God  
reborn| integer| Would you say you have been born again or have had a born again experience -- that is, a turning point in your life when you committed yourself to Christ?  
savesoul| integer| Have you ever tried to encourage someone to believe in Jesus Christ or to accept Jesus Christ as his or her savior?  
wlthwhts| integer|   
wlthblks| integer|   
wlthhsps| integer| (Do people in this group tend to be rich or poor?) Hispanic Americans?  
workwhts| integer|   
workblks| integer|   
workhsps| integer| (Do people in this group tend to be hardworking or lazy?) Hispanic-Americans?  
intlwhts| integer|   
intlblks| integer|   
intlhsps| integer| (Do people in this group tend to be unintelligent or tend to be intelligent?) Hispanic, Latinos?  
liveblks| integer| Now we are going to ask you about different types of contact with various groups of people. For the following situation, please indicate whether you would be very much in favor of it happening, somewhat in favor, neither in favor nor opposed to it happening, somewhat opposed, or very much opposed to it happening. Living in a neighborhood where half of your neighbors were blacks?  
marblk| integer| What about having a close relative marry a Black person?  
marasian| integer| How about having a close relative marry an Asian American person?  
marhisp| integer| How about having a close relative marry a Hispanic or Latino person?  
marwht| integer| What about having a close relative marry a White person? Would you be very in favor of it happening, somewhat in favor, neither in favor nor opposed to it happening, somewhat opposed, or very opposed to it happening?  
racwork| integer| IF EMPLOYED: Are the people who work where you work all white, mostly white, about half and half, mostly black, or all black?  
discaff| integer| What do you think the chances are these days that a white person won't get a job or promotion while an equally or less qualified black person gets one instead? Is this very likely, somewhat likely, or not very likely to happen these days?  
yousup| integer|   
spwksup| integer|   
fejobaff| integer| Some people say that because of past discrimination, women should be given preference in hiring and promotion. Others say that such preference in hiring and promotion of women is wrong because it discriminates against men. What about your opinion -are you for or against preferential hiring and promotion of women? IF FOR: Do you favor prefence in hiring and promotion strongly or not strongly? IF AGAINST: Do you oppose the preference in hiring and promotion strongly or not strongly?  
discaffm| integer| What do you think the chances are these days that a man won't get a job or promotion while an equally or less qualified woman gets one instead. Is this very likely, somewhat likely, somewhat unlikely, or very unlikely these days?  
fehire| integer| Now I'm going to read several statements. As I read each one, please tell me whether you strongly agree, agree, neither agree nor disagree, Because of past discrimination, employers should make special efforts to hire and promote qualified women.  
relpersn| integer| To what extent do you consider yourself a religious person? Are you very religious, moderately religious, slightly religious, or not religious at all?  
sprtprsn| integer| To what extent do you consider yourself a spiritual person? Are you very spiritual, moderately spiritual, slightly spiritual, or not spiritual at all?  
othlang| integer| Can you speak a language other than English [Spanish]?  
othlang1| integer| What other language(s) do you speak? First response.  
othlang2| integer| What other language(s) do you speak? Second response.  
spklang| integer| How well do you speak that language? [IF SPEAKS 2 OR MORE, ASK ONLY OF THE MOST FLUENT LANGUAGE] READ CATEGORIES  
betrlang| integer| Which language do you speak more fluently?  
compuse| integer| Do you personally ever use a computer at home, at work, or at some other location?  
webmob| integer| Do you have access to the Internet in your home through an Internet-enabled mobile device like a smart phone or tablet?  
emailmin| integer| About how many minutes or hours per week do you spend sending and answering electronic mail or e-mail?  
emailhr| integer| About how many minutes or hours per week do you spend sending and answering electronic mail or e-mail?  
usewww| integer| Other than for e-mail, do you ever use the Internet or World Wide Web? [INTERVIEWER: TREAT THESE AS THE SAME]  
wwwhr| integer| Not counting e-mail, about how many minutes or hours per week do you use the Web? (Include time you spend visiting regular web sites and time spent using interactive Internet services like social media, streaming services, chat rooms, online conferencing services, discussion boards or forums, and the like.)  
wwwmin| integer| Minutes per week?  
disrspct| integer| (In your day-to-day life how often have any of the following things happened to you?) You are treated with less courtesy or respect than other people.  
poorserv| integer| (In your day-to-day life how often have any of the following things happened to you?) You receive poorer service than other people at restaurants or stores.  
notsmart| integer| (In your day-to-day life how often have any of the following things happened to you?) People act as if they think you are not smart.  
afraidof| integer| (In your day-to-day life how often have any of the following things happened to you?) People act as if they are afraid of you.  
threaten| integer| (In your day-to-day life how often have any of the following things happened to you?) You are threatened or harassed.  
quallife| integer| In general, would you say your quality of life isâ¦  
hlthphys| integer| In general, how would you rate your physical health?  
hlthmntl| integer| In general, how would you rate your mental health, including your mood and your ability to think?  
satsoc| integer| In general, how would you rate your satisfaction with your social activities and relationships?  
actssoc| integer| In general, please rate how well you carry out your usual social activities and roles. (This includes activities at home, at work and in your community, and responsibilities as a parent, child, spouse, employee, friend, etc.)  
physacts| integer| To what extent are you able to carry out your everyday physical activities such as walking, climbing stairs, carrying groceries, or moving a chair?  
emoprobs| integer| In the past seven days, how often have you been bothered by emotional problems such as feeling anxious, depressed or irritable?  
fatigue| integer| In the past seven days, how would you rate your fatigue on average?  
wrkslffam| integer| (Do/did) you work in your own family business or farm?  
nextgen| integer| For each statement, please tell me if you strongly agree, agree, disagree, or strongly disagree. Because of science and technology, there will be more opportunities for the next generation.  
toofast| integer| Science makes our way of life change too fast. (Do you strongly agree, agree, disagree, or strongly disagree?)  
advfront| integer| Even if it brings no immediate benefits, scientific research that advances the frontiers of knowledge is necessary and should be supported by the federal government. (Do you strongly agree, agree, disagree, or strongly disagree?)  
balpos| integer| Would you say that the balance has been strongly in favor of the benefits, or only slightly?  
balneg| integer| Would you say that the balance has been strongly in favor of the harmful results, or only slightly?  
viruses| integer| Antibiotics kill viruses as well as bacteria. (Is that true or false?)  
inteduc| integer| Local school issues. (Are you very interested, moderately interested, or not at all interested?)  
intsci| integer| Issues about new scientific discoveries. (Are you very interested, moderately interested, or not at all interested?)  
intecon| integer| Economic issues and business conditions. (Are you very interested, moderately interested, or not at all interested?)  
inttech| integer| Issues about the use of new inventions and technologies. (Are you very interested, moderately interested, or not at all interested?)  
scientgo| integer| Scientific researchers are dedicated people who work for the good of humanity. Do you strongly agree, agree, disagree, or strongly disagree?  
scienthe| integer| Scientists are helping to solve challenging problems. (Do you strongly agree, agree, disagree, or strongly disagree?)  
scientbe| integer| Most scientists want to work on things that will make life better for the average person. (Do you strongly agree, agree, disagree, or strongly disagree?)  
posslq| integer| Which of these statements applies to you?  
posslqy| integer| Which of these statements applies to you? CODE ONE ONLY.  
marcohab| integer|   
endsmeet| integer| Thinking of your household's total income, including all the sources of income of all the members who contribute to it, how difficult or easy is it currently for your household to make ends meet?  
opwlth| integer| (For each of these, please tell me how important you think it is for getting ahead in life . . .) How important is coming from a wealthy family?  
oppared| integer| (For each of these, please tell me how important you think it is for getting ahead in life . . .) How important is having well-educated parents?  
opeduc| integer| (For each of these, please tell me how important you think it is for getting ahead in life . . .) How important is having a good education yourself?  
ophrdwrk| integer| (For each of these, please tell me how important you think it is for getting ahead in life . . .) How important is hard work?  
opknow| integer| (For each of these, please tell me how important you think it is for getting ahead in life . . .) How important is knowing the right people?  
opclout| integer| (For each of these, please tell me how important you think it is for getting ahead in life . . .) How important is having political connections?  
oprace| integer| (For each of these, please tell me how important you think it is for getting ahead in life . . .) How important is a personâs race?  
oprelig| integer| (For each of these, please tell me how important you think it is for getting ahead in life . . .) How important is a personâs religion?  
opsex| integer| (For each of these, please tell me how important you think it is for getting ahead in life . . .) How important is being born a man or a woman?  
goodlife| integer| (Please tell me/Please indicate) whether you strongly agree, agree, neither agree nor disagree, disagree, or strongly disagree with the following statement: The way things are in America, people like me and my family have a good chance of improving our standard of living-- do you agree or disagree?  
inequal5| integer| (To what extent do you agree or disagree with the following statements?) Large differences in income are necessary for America's prosperity.  
inequal6| integer| (To what extent do you agree or disagree with the following statements?) Allowing business to make good profits is the best way to improve everyoneâs standard of living.  
paydoc| integer| About how much do you think a doctor in general practice earns?  
payclerk| integer| How much do you think a salesclerk earns?  
payexec| integer| How much do you think a chairman of a large national corporation earns?  
payunskl| integer| How much do you think an unskilled worker in a factory earns?  
paycabnt| integer| How much do you think a cabinet minister in the federal government earns?  
givdoc| integer| About how much do you think a doctor in general practice should earn?  
givclerk| integer| How much do you think a salesclerk should earn?  
givexec| integer| How much do you think a chairman of a large national corporation should earn?  
givunskl| integer| How much do you think an unskilled worker in a factory should earn?  
givcabnt| integer| How much do you think a cabinet minister in the federal government should earn?  
incgap| integer| To what extent do you agree or disagree with the following statements? Differences in income in America are too large.  
goveqinc| integer| It is the responsibility of the government to reduce the differences in income between people with high incomes and those with low incomes.  
govunemp| integer| The government should provide a decent standard of living for the unemployed.  
taxrich| integer| Generally, how would you describe taxes in America today for those with high incomes? Taxes are . . .  
taxshare| integer| Do you think people with high incomes should pay a larger share of their income in taxes than those with low incomes, the same share, or a smaller share?  
conwlth| integer| (In all countries, there are differences or even conflicts between different social groups. In your opinion, in America how much conflict is there between . . .) Poor people and rich people?  
conclass| integer| (In all countries, there are differences or even conflicts between different social groups. In your opinion, in America how much conflict is there between . . .) The working class and the middle class?  
conunion| integer| (In all countries, there are differences or even conflicts between different social groups. In your opinion, in America how much conflict is there between . . .) Management and workers?  
conage| integer| (In all countries, there are differences or even conflicts between different social groups. In your opinion, in America how much conflict is there between . . .) Young people and older people?  
ldcgap| integer| (Turning to international differences, to what extent do you agree or disagree with the following statements?) Present economic differences between rich and poor countries are too large.  
ldctax| integer| (Turning to international differences, to what extent do you agree or disagree with the following statements?) People in wealthy countries should make an additional tax contribution to help people in poor countries.  
richhlth| integer| Is it just or unjust â right or wrong â that people with higher incomes can buy better health care than people with lower incomes?  
richeduc| integer| Is it just or unjust â right or wrong â that people with higher incomes can buy better education for their children than people with lower incomes?  
payresp| integer| (In deciding how much people ought to earn, how important should each of these things be, in your opinion . . .) How much responsibility goes with the job â how important do you think that ought to be in deciding pay?  
payedtrn| integer| (In deciding how much people ought to earn, how important should each of these things be, in your opinion . . .) The number of years spent in education and training?  
paychild| integer| (In deciding how much people ought to earn, how important should each of these things be, in your opinion . . .) Whether the person has children to support?  
paydowel| integer| (In deciding how much people ought to earn, how important should each of these things be, in your opinion . . .) How well he or she does the job?  
soctype1| integer| (These five diagrams show different types of society. Please read the descriptions and look at the diagrams and decide which you think best describes America . . .) First, what type of society is America today â which diagram comes closest?  
soctype2| integer| What do you think America ought to be like â which would you prefer?  
marhomo| integer| (Do you agree or disagree?) Homosexual couples should have the right to marry one another.  
meovrwrk| integer| Family life often suffers because men concentrate too much on their work.  
relactiv| integer|   
cantrust| integer| Generally speaking, would you say that people can be trusted or that you can't be too careful in dealing with people?  
religinf| integer| (Please indicate to what extent you agree or disagree with each of the following statements.) The U.S. would be a better country if religion had less influence.  
privent| integer| (How much do you agree or disagree with each of these statements) Private enterprise is the best way to solve Americaâs economic problems.  
postmat1| integer| Please tell us the one thing you think should be America's highest priority, the most important thing it should do.  
postmat2| integer| And which one do you think should be Americaâs next highest priority, the second most important thing it should do?  
scigrn| integer| (How much do you agree or disagree with each of these statements)? Modern science will solve our environmental problems with little change to our way of life.  
grnecon| integer| (How much do you agree or disagree with each of these statements?) We worry too much about the future of the environment and not enough about prices and jobs today  
harmsgrn| integer| (How much do you agree or disagree with each of these statements?) Almost everything we do in modern life harms the environment.  
grnprog| integer| (How much do you agree or disagree with each of these statements?) People worry too much about human progress harming the environment.  
grwthelp| integer| (And please tell me for each of these statements, how much you agree or disagree with it.) In order to protect the environment America needs economic growth.  
grwtharm| integer| (And please tell me for each of these statements, how much you agree or disagree with it.) Economic growth always harms the environment.  
grnprice| integer| How willing would you be to pay much higher prices in order to protect the environment?  
grntaxes| integer| And how willing would you be to pay much higher taxes in order to protect the environment?  
grnsol| integer| And how willing would you be to accept cuts in your standard of living in order to protect the environment?  
toodifme| integer| How much do you agree or disagree with each of these statements? It is just too difficult for someone like me to do much about the environment.  
ihlpgrn| integer| (How much do you agree or disagree with each of these statements?) I do what is right for the environment, even when it costs more money or takes more time.  
carsgen| integer| In general, do you think that air pollution caused by cars is . . .  
recycle| integer| How often do you make a special effort to sort glass or cans or plastic or newspapers and so on for recycling?  
grngroup| integer| Are you a member of any group whose main aim is to preserve or protect the environment?  
grnsign| integer| In the last five years, have you signed a petition about an environmental issue?  
grnmoney| integer| In the last five years , have you given money to an environmental group?  
grndemo| integer| In the last five years, have you taken part in a protest or demonstration about an environmental issue?  
impgrn| integer| (How much do you agree or disagree with each of these statements?) There are more important things to do in life than protect the environment.  
othssame| integer| (How much do you agree or disagree with each of these statements?) There is no point in doing what I can for the environment unless others do the same.  
grnexagg| integer| (How much do you agree or disagree with each of these statements?) Many of the claims about environmental threats are exaggerated.  
topprob1| integer| Which of these issues is the most important for America today?  
topprob2| integer| Which is the next most important?  
trust5| integer| Generally speaking, would you say that most people can be trusted, or that you canât be too careful in dealing with people? Please tell me what you think, where 1 means you canât be too careful and 5 means most people can be trusted.  
grncon| integer| Generally speaking, how concerned are you about environmental issues? Please tell me what you think, where 1 means you are not at all concerned and 5 means you are very concerned.  
enprbus| integer| Here is a list of some different environmental problems. Which problem, if any, do you think is the most important for America as a whole?  
helpharm| integer| (How much do you agree or disagree with each of these statements?) I find it hard to know whether the way I live is helpful or harmful to the environment.  
grneffme| integer| (How much do you agree or disagree with each of these statements?) Environmental problems have a direct effect on my everyday life.  
tempgen1| integer| In general, do you think that a rise in the worldâs temperature caused by climate change is . . .  
busgrn| integer| Which of these approaches do you think would be the best way of getting business and industry in America to protect the environment?  
peopgrn| integer| Which of these approaches do you think would be the best way of getting people and their families in America to protect the environment?  
nobuygrn| integer| And how often do you avoid buying certain products for environmental reasons?  
imports| integer| America should limit the import of foreign products in order to protect its national economy.  
powrorgs| integer| International organizations are taking away too much power from the American government.  
letin1a| integer| Do you think the number of immigrants to America nowadays should be  
partners| integer| How many sex partners have you had in the last 12 months?  
matesex| integer| Was one of the partners your husband or wife or regular sexual partner?  
frndsex| integer| (If you had other partners, does this describe any of them?...) Close personal friend  
acqntsex| integer| (If you had other partners, does this describe any of them?...) Neighbor, co-worker, or long-term acquaintance  
pikupsex| integer| (If you had other partners, does this describe any of them?...) Casual date or pick-up  
paidsex| integer| (If you had other partners, does this describe any of them?) Person you paid or paid you for sex  
othersex| integer| (If you had other partners, does this describe any of them?...) Other  
sexsex| integer| Have your sex partners in the last 12 months beenâ¦  
sexfreq| integer| About how often did you have sex during the last 12 months?  
numwomen| integer| Now thinking about the time since your 18th birthday (including the past 12 months), how many female partners have you had sex with?  
nummen| integer| Now thinking about the time since your 18th birthday (including the past 12 months), how many male partners have you had sex with?  
partnrs5| integer| Now thinking about the past five years--the time since February/March 2015, and including the past 12 months, how many sex partners have you had in that five year period?  
sexsex5| integer| (Now thinking about the past five years--the time since February/March 2015, and including the past 12 month), have your sex partners in the last five years beenâ¦  
evpaidsx| integer| Thinking about the time since your 18th birthday, have you ever had sex with a person you paid or who paid you for sex?  
evstray| integer| Have you ever had sex with someone other than your husband or wife while you were married?  
condom| integer| The last time you had sex, was a condom used? By 'sex' we mean vaginal, oral, or anal sex.  
relatsex| integer| The last time you had sex, was it with someone you were in an on-going relationship with, or was it with someone else? Remember that by 'sex' we mean only vaginal, oral, or anal sex.  
evidu| integer| Have you ever, even once, taken any drugs by injection with a needle (like heroin, cocaine, amphetamines, or steroids)? DO NOT include anything you took under a doctorâs orders.  
idu30| integer| How long has it been since you last used a needle to inject drugs?  
evcrack| integer| Have you ever, even once, used 'crack' cocaine in chunk or rock form?  
crack30| integer| How long has it been since you last used 'crack' cocaine in chunk or rock form?  
hivtest| integer| Have you ever been tested for HIV? Do not count tests you may have had as part of a blood donation. Include oral test (where they take a swab from your mouth).  
hivtest1| integer| Not including blood donations, in what month and year was your last HIV test?  
hivtest2| integer| Where did you have your last HIV test - at a private doctor or HMO office, at a counseling and testing site, at an emergency room, as an inpatient at a hospital, at a clinic, in a jail or prison, at a drug treatment facility, at home, or somewhere else?  
sexornt| integer| Which of the following best describes you?  
realinc| integer| Family income in 1972-2006 surveys in constant dollars (base=1986)  
coninc| integer| Inflation-adjusted family income.  
ethnic| integer| (From what countries or part of the world did your ancestors come?) IF MORE THAN ONE COUNTRY NAMED: Which one of these countries do you feel closer to?  
hispanic| integer| Are you Spanish, Hispanic, or Latino/Latina? IF YES: Which group are you from?  
racecen1| integer| (What is your race? Indicate one or more races that you consider yourself to be.) First mention  
racecen2| integer| (What is your race? Indicate one or more races that you consider yourself to be.) Second mention  
racecen3| integer| (What is your race? Indicate one or more races that you consider yourself to be.) Third mention  
vetyears| integer| Have you ever been on active duty for military training or service for two consecutive months or more? IF YES: What was your total time on active duty?  
dwelown| integer| (Do you/Does your family) own your (home/apartment), pay rent, or what?  
dwelown16| integer| When you were 16 years old, did your family own your own home, pay rent, or something else?  
dateintv| integer| Date of interview.  
sei10| integer| R's SOCIOECONOMIC INDEX (2010)  
spsei10| integer| R'S SPOUSE'S SOCIOECONOMIC INDEX (2010)  
cosei10| integer| R'S PARTNER'S SOCIOECONOMIC INDEX (2010)  
copres10| integer| PRESTIGE OF RESPONDENT'S PARTNER'S OCCUPATION  
cohort| integer| Birth cohort of respondent.  
marcohrt| integer|   
zodiac| integer| ASTROLOGICAL SIGN OF RESPONDENT  
mode| integer| Interview done in-person, over the phone, a combination of in-person and over the phone, or web  
consent| integer| PARTICIPATION/RECORDING CONSENT  
adminconsent| integer| May we try to link government records with your survey answers?  
letdie1y| integer|   
ballot| integer| Ballot Administered.  
version| integer|   
issp| integer| Status on International Social Survey Program Self-Completion Supplement.  
formwt| integer| Weight for form variables.  
oversamp| integer| Weight for Black oversamples.  
spanself| integer| If this interview had only been available in English, would you...  
spanint| integer|   
spaneng| integer| Interviews Conducted in Spanish or English  
vstrat| integer|   
vpsu| integer|   
famdif16y| integer| Which of the following best describes your situation?  
pawrkslf2| integer| Was he self-employed or did he work for someone else?  
mawrkslf2| integer| At this job, was (your mother/your stepmother/the female relative you were living with when you were 16) an employee, self-employed without employees, or self-employed with employees?  
ethworld1| integer| From what part of the world did your ancestors come? Europe  
ethworld2| integer| From what part of the world did your ancestors come? Africa  
ethworld3| integer| From what part of the world did your ancestors come? Asia  
ethworld4| integer| From what part of the world did your ancestors come? Middle East  
ethworld5| integer| From what part of the world did your ancestors come? South America  
ethworld6| integer| From what part of the world did your ancestors come? Central America  
ethworld7| integer| From what part of the world did your ancestors come? North America  
ethworld8| integer| From what part of the world did your ancestors come? Caribbean  
ethworld9| integer| From what part of the world did your ancestors come? Oceania  
ethregion1| integer| From what country or countries did your ancestors come? Austria  
ethregion2| integer| From what country or countries did your ancestors come? Belgium  
ethregion3| integer| From what country or countries did your ancestors come? Czechoslovakia  
ethregion4| integer| From what country or countries did your ancestors come? Denmark  
ethregion5| integer| From what country or countries did your ancestors come? England and Wales  
ethregion6| integer| From what country or countries did your ancestors come? Finland  
ethregion7| integer| From what country or countries did your ancestors come? France  
ethregion8| integer| From what country or countries did your ancestors come? Germany  
ethregion9| integer| From what country or countries did your ancestors come? Greece  
ethregion10| integer| From what country or countries did your ancestors come? Hungary  
ethregion11| integer| From what country or countries did your ancestors come? Ireland  
ethregion12| integer| From what country or countries did your ancestors come? Italy  
ethregion13| integer| From what country or countries did your ancestors come? Lithuania  
ethregion14| integer| From what country or countries did your ancestors come? Netherlands (Dutch/Holland)  
ethregion15| integer| From what country or countries did your ancestors come? Norway  
ethregion16| integer| From what country or countries did your ancestors come? Poland  
ethregion17| integer| From what country or countries did your ancestors come? Portugal  
ethregion18| integer| From what country or countries did your ancestors come? Romania  
ethregion19| integer| From what country or countries did your ancestors come? Russia (USSR)  
ethregion20| integer| From what country or countries did your ancestors come? Scotland  
ethregion21| integer| From what country or countries did your ancestors come? Spain  
ethregion22| integer| From what country or countries did your ancestors come? Sweden  
ethregion23| integer| From what country or countries did your ancestors come? Switzerland  
ethregion24| integer| From what country or countries did your ancestors come? Turkey  
ethregion25| integer| From what country or countries did your ancestors come? Yugoslavia  
ethregion26| integer| From what country or countries did your ancestors come? Other (Europe)  
ethregion27| integer| From what country or countries did your ancestors come? Algeria  
ethregion28| integer| From what country or countries did your ancestors come? Democratic Republic of the Congo  
ethregion29| integer| From what country or countries did your ancestors come? Egypt  
ethregion30| integer| From what country or countries did your ancestors come? Ethiopia  
ethregion31| integer| From what country or countries did your ancestors come? Kenya  
ethregion32| integer| From what country or countries did your ancestors come? Nigeria  
ethregion33| integer| From what country or countries did your ancestors come? South Africa  
ethregion34| integer| From what country or countries did your ancestors come? Sudan  
ethregion35| integer| From what country or countries did your ancestors come? Tanzania  
ethregion36| integer| From what country or countries did your ancestors come? Uganda  
ethregion37| integer| From what country or countries did your ancestors come? Other (Africa)  
ethregion38| integer| From what country or countries did your ancestors come? Bangladesh  
ethregion39| integer| From what country or countries did your ancestors come? China  
ethregion40| integer| From what country or countries did your ancestors come? India  
ethregion41| integer| From what country or countries did your ancestors come? Indonesia  
ethregion42| integer| From what country or countries did your ancestors come? Japan  
ethregion43| integer| From what country or countries did your ancestors come? Pakistan  
ethregion44| integer| From what country or countries did your ancestors come? Philippines  
ethregion45| integer| From what country or countries did your ancestors come? South Korea  
ethregion46| integer| From what country or countries did your ancestors come? Thailand  
ethregion47| integer| From what country or countries did your ancestors come? Vietnam  
ethregion48| integer| From what country or countries did your ancestors come? Other (Asia)  
ethregion49| integer| From what country or countries did your ancestors come? Iran  
ethregion50| integer| From what country or countries did your ancestors come? Iraq  
ethregion51| integer| From what country or countries did your ancestors come? Israel  
ethregion52| integer| From what country or countries did your ancestors come? Jordan  
ethregion53| integer| From what country or countries did your ancestors come? Saudi Arabia  
ethregion54| integer| From what country or countries did your ancestors come? Syria  
ethregion55| integer| From what country or countries did your ancestors come? United Arab Emirates  
ethregion56| integer| From what country or countries did your ancestors come? Yemen  
ethregion57| integer| From what country or countries did your ancestors come? Other (Middle East)  
ethregion58| integer| From what country or countries did your ancestors come? Argentina  
ethregion59| integer| From what country or countries did your ancestors come? Bolivia  
ethregion60| integer| From what country or countries did your ancestors come? Brazil  
ethregion61| integer| From what country or countries did your ancestors come? Chile  
ethregion62| integer| From what country or countries did your ancestors come? Colombia  
ethregion63| integer| From what country or countries did your ancestors come? Ecuador  
ethregion64| integer| From what country or countries did your ancestors come? French Guiana  
ethregion65| integer| From what country or countries did your ancestors come? Guyana  
ethregion66| integer| From what country or countries did your ancestors come? Paraguay  
ethregion67| integer| From what country or countries did your ancestors come? Peru  
ethregion68| integer| From what country or countries did your ancestors come? Suriname  
ethregion69| integer| From what country or countries did your ancestors come? Uruguay  
ethregion70| integer| From what country or countries did your ancestors come? Venezuela  
ethregion71| integer| From what country or countries did your ancestors come? Other (South America)  
ethregion72| integer| From what country or countries did your ancestors come? Belize  
ethregion73| integer| From what country or countries did your ancestors come? Costa Rica  
ethregion74| integer| From what country or countries did your ancestors come? El Salvador  
ethregion75| integer| From what country or countries did your ancestors come? Guatemala  
ethregion76| integer| From what country or countries did your ancestors come? Honduras  
ethregion77| integer| From what country or countries did your ancestors come? Mexico  
ethregion78| integer| From what country or countries did your ancestors come? Nicaragua  
ethregion79| integer| From what country or countries did your ancestors come? Panama  
ethregion80| integer| From what country or countries did your ancestors come? Other (Central America)  
ethregion81| integer| From what country or countries did your ancestors come? American Indian  
ethregion82| integer| From what country or countries did your ancestors come? Canada  
ethregion83| integer| From what country or countries did your ancestors come? Canada (French)  
ethregion84| integer| From what country or countries did your ancestors come? Puerto Rico  
ethregion85| integer| From what country or countries did your ancestors come? Other (North America)  
ethregion86| integer| From what country or countries did your ancestors come? Cuba  
ethregion87| integer| From what country or countries did your ancestors come? Haiti  
ethregion88| integer| From what country or countries did your ancestors come? Dominican Republic  
ethregion89| integer| From what country or countries did your ancestors come? Jamaica  
ethregion90| integer| From what country or countries did your ancestors come? Other (Caribbean)  
ethregion91| integer| From what country or countries did your ancestors come? Australia  
ethregion92| integer| From what country or countries did your ancestors come? Papua New Guinea  
ethregion93| integer| From what country or countries did your ancestors come? New Zealand  
ethregion94| integer| From what country or countries did your ancestors come? Samoa  
ethregion95| integer| From what country or countries did your ancestors come? Jamaica  
ethregion96| integer| From what country or countries did your ancestors come? Other (Oceania)  
wrkgovt1| integer| (Are/Were) you employed by the government? (Please consider federal, state, or local government.)  
wrkgovt2| integer| (Are/Were) you employed by a private employer (including non-profit organizations)?  
spkathy| integer| (There are always some people whose ideas are considered bad or dangerous by other people. For instance, somebody who is against all churches and religionâ¦) If such a person wanted to make a speech in your community against churches and religion, should this person be allowed to speak, or not?  
libathy| integer| (There are always some people whose ideas are considered bad or dangerous by other people. For instance, somebody who is against all churches and religionâ¦) If some people in your community suggested that a book this person wrote against churches and religion should be taken out of your public library, would you favor removing this book, or not?  
spkracy| integer| Or consider a person who believes that Blacks are genetically inferiorâ¦ If such a person wanted to make a speech in your community claiming that Blacks are inferior, should this person be allowed to speak, or not?  
libracy| integer| (Or consider a person who believes that Blacks are genetically inferiorâ¦) If some people in your community suggested that a book this person wrote which said Blacks are inferior should be taken out of your public library, would you favor removing this book, or not?  
spkcomy| integer| Now,we would like to ask you some questions about a self-identified Communist. Suppose this admitted Communist wanted to make a speech in your community. Should this person be allowed to speak, or not?  
colcomy| integer| (Now,we would like to ask you some questions about a self-identified Communist...) Suppose this person is teaching in a college. Should this person be fired, or not?  
libcomy| integer| (Now,we would like to ask you some questions about a self-identified Communistâ¦) Suppose this person wrote a book which is in your public library. Somebody in your community suggests that the book should be removed from the library. Would you favor removing it, or not?  
spkmily| integer| Consider a person who advocates doing away with elections and letting the military run the country. If such a person wanted to make a speech in your community, should this person be allowed to speak, or not?  
libmily| integer| Suppose this person wrote a book advocating doing away with elections and letting the military run the country. Somebody in your community suggests that the book be removed from the public library. Would you favor removing it, or not?  
spkhomoy| integer| And what about a gay person? Suppose this gay person wanted to make a speech in your community. Should this person be allowed to speak, or not?  
libhomoy| integer| If somebody in your community suggests that a book the gay person wrote in favor of homosexuality should be taken out of your public library, would you favor removing it, or not?  
spkmslmy| integer| Now consider a Islamic religious leader who preaches hatred of the United States. If such a person wanted to make a speech in your community preaching hatred of the United States, should this person be allowed to speak, or not?  
libmslmy| integer| (Now consider a Islamic religious leader who preaches hatred of the United Statesâ¦) If some people in your community suggested that a book this person wrote which preaches hatred of the United States should be taken out of your public library, would you favor removing this book, or not?  
polhitoky| integer| Are there any situations you can imagine in which you would approve of a police officer striking an adult male citizen?  
polabusey| integer| (Would you approve of a policeman striking a citizen who...) Had said vulgar and obscene things to the police officer?  
polattaky| integer| Would you approve if the citizen was attacking the police officer with his fists?  
raceacs1| integer| What is your race? White  
raceacs2| integer| Black or African American  
raceacs3| integer| American Indian or Alaska Native  
raceacs4| integer| Asian Indian  
raceacs5| integer| Chinese  
raceacs6| integer| Filipino  
raceacs7| integer| Japanese  
raceacs8| integer| Korean  
raceacs9| integer| Vietnamese  
raceacs10| integer| Other Asian  
raceacs11| integer| Native Hawaiian  
raceacs12| integer| Guamanian or Chamorro  
raceacs13| integer| Samoan  
raceacs14| integer| Other Pacific Islander  
raceacs15| integer| Some other race  
raceacs16| integer| Hispanic  
abdefectg| integer| (Please tell me whether or not you think it should be possible for a pregnant woman to obtain a legal abortion if. . .) If there is a strong chance of serious defect in the baby?  
abnomoreg| integer| If she is married and does not want any more children?  
abhlthg| integer| If the woman's own health is seriously endangered by the pregnancy?  
abpoorg| integer| If the family has a very low income and cannot afford any more children?  
abrapeg| integer| If she becomes pregnant as a result of rape?  
absingleg| integer| If she is not married and does not want to marry the man?  
suicide1g| integer| (Do you think a person has the right to end his or her own life if this person . . .) Has an incurable disease?  
suicide2g| integer| (Do you think a person has the right to end his or her own life if this person . . .) Has gone bankrupt?  
suicide3g| integer| (Do you think a person has the right to end his or her own life if this person . . .) Has dishonored his or her family?  
suicide4g| integer| (Do you think a person has the right to end his or her own life if this person . . .) Is tired of living and ready to die?  
maborn| integer| Was(your mother/ your stepmother/ the female relative you were living with at 16) born in this country?  
paborn| integer| Was(your father/ your stepfather/ the male relative you were living with at 16) born in this country?  
sexbirth1| integer| Was your sex recorded as male or female at birth?  
sexnow1| integer| Do you describe yourself as male, female, or transgender?  
goveqinc1| integer| It is the responsibility of the government to reduce the differences in income between people with high incomes and those with low incomes.  
immlimit| integer| America should limit immigration in order to protect our national way of life.  
trresrch| integer| (On a scale of 0 to 10, how much do you personally trust each of the following institutions? 0 means you do not trust an institution at all, and 10 means you trust it completely.) University research centers  
trmedia| integer| (On a scale of 0 to 10, how much do you personally trust each of the following institutions? 0 means you do not trust an institution at all, and 10 means you trust it completely.) The news media  
trbusind| integer| (On a scale of 0 to 10, how much do you personally trust each of the following institutions? 0 means you do not trust an institution at all, and 10 means you trust it completely.) Business and industry  
trlegis| integer| (On a scale of 0 to 10, how much do you personally trust each of the following institutions? 0 means you do not trust an institution at all, and 10 means you trust it completely.) The U.S. Congress  
clmtcaus| integer| There has been a lot of discussion about the worldâs climate and the idea it has been changing in recent decades. Which of the following statements comes closest to your opinion?  
clmtwrld| integer| On a scale from 0 to 10, how bad or good do you think the impacts of climate change will be for the world as a whole? 0 means extremely bad, 10 means extremely good.  
clmtusa| integer| On a scale from 0 to 10, how bad or good do you think the impacts of climate change will be for America? 0 means extremely bad, 10 means extremely good.  
naturdev| integer| How willing would you be to accept a reduction in the size of Americaâs protected nature areas, in order to open them up for economic development?  
indusgen1| integer| In general, do you think that air pollution caused by industry is . . .  
chemgen1| integer| And do you think that pesticides and chemicals used in farming are . . .  
watergen1| integer| And do you think that pollution of Americaâs rivers, lakes and streams is . . .  
genegen1| integer|   
nukegen1| integer| And do you think that nuclear power stations are . . .  
enjoynat| integer|   
activnat| integer| In the last twelve months how often, if at all, have you engaged in any leisure activities outside in nature, such as hiking, bird watching, swimming, skiing, other outdoor activities or just relaxing?  
planetrp| integer| In the last twelve months, how many trips did you make by plane? Count outward and return journeys, including transfers, as one trip.  
carhr| integer| In a typical week, about how many hours do you spend in a car or another motor vehicle, including motorcycles, trucks, and vans, but not counting public transport? Do not include shared rides in buses, collective taxis, or carpooling services.  
eatmeat| integer| In a typical week, on how many days do you eat beef, lamb, or products that contain them?  
numrooms| integer| How many rooms are there in your home (apartment or house)? Do not count any separate kitchens, bathrooms, garages, balconies, hallways or cupboards.  
airpollu| integer| (Thinking about your neighborhood, to what extent, if at all, was it affected by the following things over the last twelve months?) Air pollution  
wtrpollu| integer| (Thinking about your neighborhood, to what extent, if at all, was it affected by the following things over the last twelve months?) Water pollution  
exweathr| integer| (Thinking about your neighborhood, to what extent, if at all, was it affected by the following things over the last twelve months?) Extreme weather events (such as severe storms, droughts, floods, heat waves, cold snaps, etc.)  
opbribes| integer| (For each of these, please tell me how important you think it is for getting ahead in life . . .) How important is giving bribes?  
mkt1| integer| It is the responsibility of private companies to reduce the differences in pay between their employees with high pay and those with low pay.  
respineq| integer| From the following list, who do you think should have the greatest responsibility for reducing differences in income between people with high incomes and people with low incomes?  
govineq1| integer| To what extent do you agree or disagree with the following statement: Most politicians in America do not care about reducing the differences in income between people with high incomes and people with low incomes.  
govineq2| integer| How successful do you think the government in America is nowadays in reducing the differences in income between people with high incomes and people with low incomes?  
ineqmad| integer| Some people feel angry about differences in wealth between the rich and the poor, while others do not. How do you feel when you think about differences in wealth between the rich and the poor in America? Please place yourself on a scale of 0 to 10, where 0 means not angry at all and 10 means extremely angry.  
migrpoor| integer| (Turning to international differences, to what extent do you agree or disagree with the following statements?) People from poor countries should be allowed to work in wealthy countries.  
conimm| integer| (In all countries, there are differences or even conflicts between different social groups. In your opinion, in America how much conflict is there between . . .) People born in America and people from other countries who have come to live in America?  
rank1| integer| In our society there are groups which tend to be towards the top and groups which tend to be towards the bottom. Below is a scale that runs from top to bottom. Where would you put yourself now on this scale?  
rank16| integer| If you think about the family that you grew up in, where did they fit in then?  
rank10fut| integer| (In our society there are groups which tend to be towards the top and groups which tend to be towards the bottom. On the diagram is a scale that runs from top to bottom.) And thinking ahead 10 years from now, where do you think you will be on a scale of 1 to 10, where 1 is the top and 10 the bottom?  
fairdist| integer| How fair or unfair do you think the income distribution is in America?  
contpoor| integer| How often do you have any contact with people who are a lot poorer than you when you are out and about? This might be in the street, on public transport, in shops, in your neighborhood, or at your workplace.  
contrich| integer| How often do you have any contact with people who are a lot richer than you when you are out and about? This might be in the street, on public transport, in shops, in your neighborhood, or at your workplace.  
endsme12| integer| And during the next 12 months, how difficult or easy do you think it will be for your household to make ends meet?  
skipmeal| integer| How often do you or other members of your household skip a meal because there is not enough money for food?  
class1| integer| Most people see themselves as belonging to a particular class. Please tell me which social class you would say you belong to?  
ratepain1| integer| On a scale from 0 to 10, with 0 meaning no pain and 10 being the worst imaginable pain, how would you rate your pain on average?  
norelgsp| integer| Do you consider yourself to be atheist, agnostic, something else, or nothing in particular?  
evangclx| integer| Would you describe yourself as a 'born again' or evangelical Christian, or not?  
evangcly| integer| Would you describe yourself as an evangelical Christian, or not?  
religimp| integer| How important is religion in your life â very important, somewhat important, not too important, or not at all important?  
relidimp| integer| When thinking about religion, how important is being (a Christian/a Catholic/a Jew/a Buddhist/a Hindu/a Muslim/an Atheist/an Agnostic/someone who does not identify with a religion/ a member of your religion) to you?  
relidesc| integer| How well does the term (Christian/Catholic/Jew/Buddhist/Hindu/Muslim/Atheist/Agnostic/non-religious/N/A) describe you?  
relidwe| integer| When talking about (Christians/Catholics/Jews/Buddhists/Hindus/Muslims/Atheists/Agnostics/people who do not identify with a religion/your religion), how often do you say 'we' instead of 'they'?  
relidins| integer| If someone criticized (Christians/Catholics/Jews/Buddhists/Hindus/Muslims/Atheists/Agnostics/people who do not identify with a religion/your religion), to what extent would it feel like a personal insult?  
biblauth| integer| The Bible is the highest authority for what I believe.  
evngelze| integer| It is very important for me personally to encourage non-Christians to accept Jesus Christ as their Savior.  
sinsacri| integer| Jesus Christâs death on the cross is the only sacrifice that could remove the penalty of my sin.  
chrstsav| integer| Only those who accept Jesus Christ alone as their Savior can achieve eternal salvation.  
sprtconnct| integer| (Some people say they have experiences of being personally moved, touched, or inspired, while others say they do not have these experiences at all. How often, if at all, do you experience each of the following?) Felt particularly connected to the world around you.  
sprtlrgr| integer| (Some people say they have experiences of being personally moved, touched, or inspired, while others say they do not have these experiences at all. How often, if at all, do you experience each of the following?) Felt like you were part of something much larger than yourself.  
sprtpurp| integer| (Some people say they have experiences of being personally moved, touched, or inspired, while others say they do not have these experiences at all. How often, if at all, do you experience each of the following?) Felt a sense of a larger meaning or purpose in life.  
mditate1| integer| How often do you meditate?  
grtwrks| integer| (Please indicate to what extent you agree or disagree with each of the following statements.) The great works of philosophy and science are the best source of truth, wisdom, and ethics.  
freemind| integer| (Please indicate to what extent you agree or disagree with each of the following statements.) To understand the world, we must free our minds from old traditions and beliefs.  
decevidc| integer| (Please indicate to what extent you agree or disagree with each of the following statements.) When I make important decisions in my life, I rely mostly on reason and evidence.  
advfmsci| integer| (Please indicate to what extent you agree or disagree with each of the following statements.) All of the greatest advances for humanity have come from science and technology.  
prochoic| integer| (We hear a lot of talk these days about abortion. Please indicate to what extent you agree or disagree with each of the following statements.) I consider myself pro-choice.  
prolife| integer| (We hear a lot of talk these days about abortion. Please indicate to what extent you agree or disagree with each of the following statements.) I consider myself pro-life.  
godusa| integer| (Please indicate to what extent you agree or disagree with each of the following statements.) The success of the United States is part of Godâs plan.  
govchrst| integer| (Please indicate to what extent you agree or disagree with each of the following statements.) The federal government should advocate Christian values.  
buseqinc| integer| Some people think that major companies ought to reduce the pay differences between employees with high pay and those with low pay, perhaps by reducing the pay of executives or by increasing the pay of unskilled workers. Others think that major companies should not concern themselves with reducing this pay difference between employees with high pay and those with low pay. Think of a score of 1 as meaning that major companies ought to reduce the pay differences between employees with high pay and those with low pay, and a score of 7 meaning that major companies should not concern themselves with reducing pay differences. What score between 1 and 7 comes closest to the way you feel?  
trdunio1| integer| To what extent do you agree or disagree with the following statements? Workers need strong trade unions to protect their interests.  
boardrep| integer| (To what extent do you agree or disagree with the following statements?) Workers should be represented on the board of directors at major companies.  
upwages| integer| (To what extent do you agree or disagree with the following statements?) The government should ensure that the wages of low-paying jobs increase as the economy grows.  
limitpay| integer| (To what extent do you agree or disagree with the following statements?) The government should take steps to limit the pay of executives at major companies.  
govfnanc| integer| (To what extent do you agree or disagree with the following statements?) The government should finance projects to create new jobs, even if it might require a tax increase to pay for it.  
dclindus| integer| (To what extent do you agree or disagree with the following statements?) The government should support declining industries to protect jobs, even if it might require a tax increase to pay for it.  
govfnaid| integer| (To what extent do you agree or disagree with the following statements?) The government should give financial assistance to college students from low-income families, even if it might require a tax increase to pay for it.  
hivafraid| integer| Please indicate how much you agree or disagree with each of the following comments. I would be afraid to be around a person with HIV because I would be worried I could get infected.  
hivimmrl| integer| (Please indicate how much you agree or disagree with each of the following comments.) People who have HIV have participated in immoral activities  
hivdscrm| integer| (Please indicate how much you agree or disagree with each of the following comments.) There is a lot of discrimination against people with HIV in this country today.  
ptnrornt| integer| To the best of your knowledge, which of the following best describes how your most recent sexual partner thinks of themselves?  
ptnrsxbrth| integer| To the best of your knowledge, was your most recent sexual partnerâs sex recorded as male or female at birth?  
ptnrsxnow| integer| To the best of your knowledge, does your most recent sexual partner describe themselves as male, female, or transgender?  
poltrtblk| integer| The following questions are about police and law enforcement. In general, do the police (treat Whites better than Blacks, treat them both the same, or treat Blacks better than Whites/treat Blacks better than Whites, treat them both the same, or treat Whites better than Blacks)?  
poltrthsp| integer| In general, do the police (treat Whites better than Latinos, treat them both the same, or treat Latinos better than Whites/treat Latinos better than Whites, treat them both the same, or treat Whites better than Latinos)?  
defund| integer| Do you favor or oppose reducing funding for police departments, and moving those funds to mental health, housing, and other social services?  
strvbias| integer| Which do you think should be the bigger priority for the U.S. criminal justice system today?  
strvbiasy| integer|   
racesurv17| integer| How much, if at all, do you think the legacy of slavery affects the position of black people in American society today?  
conpharvac| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Pharmaceutical companies  
conpharvacy| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) Pharmaceutical companies  
confedvac| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) The federal government ensuring the safety of vaccines to protect the public against serious diseases.  
confedvacy| integer| (I am going to name some institutions in this country. As far as the people running these institutions are concerned, would you say you have a great deal of confidence, only some confidence, or hardly any confidence at all in them?) The federal government ensuring the safety of vaccines to protect the public against COVID-19.  
wtssps| integer|   
wtssnrps| integer|   
uswaryv| integer| Do you expect the United States to fight in another world war within the next ten years?  
prayerv| integer| The United States Supreme Court has ruled that no state or local government may require the reading of the Lord's Prayer or Bible verses in public schools. What are your views on this--do you approve or disapprove of the court ruling?  
courtsv| integer| In general, do you think the courts in this area deal too harshly or not harshly enough with criminals?  
discaffwv| integer| What do you think the chances are these days that a woman won't get a job or promotion while an equally or less qualified man gets one instead. Is this very likely, somewhat likely, somewhat unlikely, or very unlikely these days?  
racopenv| integer| Suppose there is a community-wide vote on the general housing issue. There are two possible laws to vote on: One law says that a homeowner can decide whom to sell their house to, even if that homeowner prefers not to sell to someone because of their race or color. The second law says that a homeowner cannot refuse to sell to someone because of their race or color. Which law would you vote for?  
getaheadv| integer| Some people say that people get ahead by their own hard work; others say that lucky breaks or help from other people are more important. Which do you think is most important?  
divlawv| integer| Should divorce in this country be easier or more difficult to obtain than it is now?  
helpfulv| integer| Would you say that most of the time people try to be helpful, or that they are mostly just looking out for themselves?  
fairv| integer| Do you think most people would try to take advantage of you if they got a chance, or would they try to be fair?  
trustv| integer| Generally speaking, would you say that most people can be trusted or that you can't be too careful in dealing with people?  
agedv| integer| As you know, many older people share a home with their grown children. Do you think this is generally a good idea or a bad idea?  
grassv| integer| Do you think the use of marijuana should be made legal or not?  
relitenv| integer| (ASK EVERYONE WITH ANY RELIGIOUS PREFERENCE NAMED IN RELIG) Would you call yourself a strong (PREFERENCE NAMED IN RELIG) or a not very strong (PREFERENCE NAMED IN RELIG)?  
biblev| integer| Which of these statements comes closest to describing your feelings about the Bible? A.) The Bible is the actual word of God and is to be taken literally, word for word. B.)The Bible is the inspired word of God but not everything in it should be taken literally, word for word. C.)The Bible is an ancient book of fables, legends, history, and moral precepts recorded by man.  
postlifev| integer| Do you believe there is a life after death?  
kidssolv| integer| When your children are at the age you are now, do you think their standard of living will be much better, somewhat better, about the same, somewhat worse, or much worse than yours is now?  
uscitznv| integer| Now we would like to ask you about U.S. citizenship. Are youâ¦  
fucitznv| integer| Are youâ¦  
fepolv| integer| Tell me if you agree or disagree with this statement: Most men are better suited emotionally for politics than are most women.  
uswarynv| integer| Do you expect the United States to fight in another world war within the next ten years?  
prayernv| integer| The United States Supreme Court has ruled that no state or local government may require the reading of the Lord's Prayer or Bible verses in public schools. What are your views on this--do you approve or disapprove of the court ruling?  
courtsnv| integer| In general, do you think the courts in this area deal too harshly or not harshly enough with criminals?  
discaffwnv| integer| What do you think the chances are these days that a woman won't get a job or promotion while an equally or less qualified man gets one instead. Is this very likely, somewhat likely, somewhat unlikely, or very unlikely these days?  
racopennv| integer| Suppose there is a community-wide vote on the general housing issue. There are two possible laws to vote on: One law says that a homeowner can decide whom to sell their house to, even if that homeowner prefers not to sell to someone because of their race or color. The second law says that a homeowner cannot refuse to sell to someone because of their race or color. Which law would you vote for?  
getaheadnv| integer| Some people say that people get ahead by their own hard work: others say that lucky breaks or help from other people are more important. Which do you think is most important?  
divlawnv| integer| Should divorce in this country be easier or more difficult to obtain than it is now?  
helpfulnv| integer| Would you say that most of the time people try to be helpful, or that they are mostly just looking out for themselves?  
fairnv| integer| Do you think most people would try to take advantage of you if they got a chance, or would they try to be fair?  
trustnv| integer| Generally speaking, would you say that most people can be trusted or that you can't be too careful in dealing with people?  
agednv| integer| As you know, many older people share a home with their grown children. Do you think this is generally a good idea or a bad idea?  
grassnv| integer| Do you think the use of marijuana should be made legal or not?  
relitennv| integer| (ASK EVERYONE WITH ANY RELIGIOUS PREFERENCE NAMED IN RELIG) Would you call yourself a strong (PREFERENCE NAMED IN RELIG) or a not very strong (PREFERENCE NAMED IN RELIG)?  
biblenv| integer| Which of these statements comes closest to describing your feelings about the Bible? A.) The Bible is the actual word of God and is to be taken literally, word for word. B.)The Bible is the inspired word of God but not everything in it should be taken literally, word for word. C.)The Bible is an ancient book of fables, legends, history, and moral precepts recorded by man.  
postlifenv| integer| Do you believe there is a life after death?  
kidssolnv| integer| When your children are at the age you are now, do you think their standard of living will be much better, somewhat better, about the same, somewhat worse, or much worse than yours is now?  
uscitznnv| integer| Now we would like to ask you about U.S. citizenship. Are youâ¦  
fucitznnv| integer| Are youâ¦  
fepolnv| integer| Tell me if you agree or disagree with this statement: Most men are better suited emotionally for politics than are most women.  
scibnftsv| integer| Would you say that, on balance, the benefits of scientific research have outweighed the harmful results, or have the harmful results of scientific research been greater than its benefits?  
abanyg| integer| If the woman wants it for any reason?  
fileversion| integer|   
  
## References

Urls used in the creation of this data package.

  * **[gss_2021_src](<https://gss.norc.org/Documents/stata/2021_stata.zip#GSS2021.dta>)**. GSS 2021 Source archive
  * **[gss_2021_codes](<https://gss.norc.org/Documents/stata/2021_stata.zip#GSS 2021 Codebook.pdf>)**. GSS 2021 Codebook
  * **data/variables.csv**. Variable names and descriptions
  * **data/labels.csv**. Variable value labels


## Packages

  * **s3** s3://library.metatab.org/norc.org-gss-2021-1.1.1.csv
  * **csv** <https://library.metatab.org/norc.org-gss-2021-1.1.1.csv>


### Accessing Data in Vanilla Pandas
[code] 
    import pandas as pd
    
    
    gss_2021_df =  pd.read_csv('https://library.metatab.org/norc.org-gss-2021-1.1.1/data/gss_2021.csv')
[/code]

### Accessing Package in Metapack
[code] 
    import metapack as mp
    pkg = mp.open_package('https://library.metatab.org/norc.org-gss-2021-1.1.1.csv')
    
    # Create Dataframes
    gss_2021_df = pkg.resource('gss_2021').dataframe()
    
[/code]
