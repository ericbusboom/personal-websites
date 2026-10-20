---
title: "COVID-19 Disaster Depends on the Difference of One Day"
date: 2020-04-27T08:09:33+00:00
draft: false
categories: ["News"]
tags: ["covid-19"]
author: "eric"
---

One of the [simplest models of infection is the SIR model](<https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology>), a set of differential equations that describes how people in a population infect each other and eventually recover, transitioning between three compartments, from Susceptible to Infected to Recovered, although, because the model uses "Recovered" as the category for people who have died, some people refer to the R as "Removed." It is a very simplistic model that assumes that every person in the population is equally likely to run to anyone else, so it is much more suitable for the State Fair or Chochella than it is for a real society, but it does offer an easy way to explore how infections work, in the abstract. 

Below are a series of plots of an SIR simulation for a group of 1M people with a disease of $R_0$ of 4, showing the number of people in each state. The Recovered group is the people who have every had the disease and are now immune and the Infected group is those who have it at a particular point in time. The first plot is for a constant $R_0$ value of 4, but the following ones show what happens when $R$ changes, as it would because of a social distancing policy. 

![](https://i2.wp.com/www.sandiegodata.org/uploads/7/2020/04/SIR-SIM-Change-R.png?fit=1024%2C854&ssl=1)

In the first case, the infection tears through the entire 1M population in less than 1 month from the first infection. Note that it looks like nothing is happening until about day 12, then the number of infections explodes. 

In the next plot, the population implements a social distancing policy on day 5, after which the $R$ value decreases, over the next seven days, to 1.05, just slightly above the point where the infection will naturally burn itself out. This change in policy reduces the number of total infections at day 60 by more than 50%! But, for COVID-19, this 50% infection rate was one of the worst case scenarios for the US, so it isn't really a success. 

The third plot shows what happens when the social distancing policy is implemented one day earlier, another 50% reduction, and just as importantly, the curve is spread out, so the hospitals are much less likely to be overwhelmed. 

While the social distancing policies are effective in this simulation, they had to be implemented very early. On day 5, the model has only 100 infections, and since COVID-19 has such a large rate of asymptotic infections, it is very unlikely that the public health system would even know there were any infections on day 5, so it would be impossible to implement social distancing. So, while this analysis indicates that it's important to implement social distance policies early, the policy must be implemented earlier than is actually possible. 

So, what happens if our model society implements social distancing later, on day 14, compared to implementing a day earlier, on Day 13? In this image, the first plot is the same as the previous image, the second is implementing social distancing on day 14, and the third is implementing social distancing on day 13. 

![](https://i0.wp.com/www.sandiegodata.org/uploads/7/2020/04/SIR-too-late.png?fit=1024%2C661&ssl=1)

Almost nothing. A one day difference is only significant if the policy is implemented very early. 

Even though this model predicts disaster for late action, and it has been at least 50 days since San Diego's first infection, our county has far fewer infections and hospitalizations than this model would suggest. We are either doing something right, or the COVID-19 is behaving much differently than simple models would suggest. There is still a lot of work to be done to determine the actual $R_0$ values for COVID-19 — there is more than one, and they vary by both place and time — and modeling a real society required more sophistication than this SIR model, but this analysis can encourage some hunches.   
  
One of my hunches is that the curves we are seeing now, with hospitalization and death rates far below initial predictions, are not entirely the result of social policy. The curves are bending down, but I suspect that social distancing is only part of the reason, and that there are other features of the disease itself that contribute to us avoiding the dire fate of the earliest predictions. This analysis supports that hunch, because I think it is unlikely that San Diego County, despite being an early leader in social distancing, implemented the policy early enough to have a dominant effect. But that is just a hunch, and it will probably take years before there is enough data and research to either confirm or disprove it. 

Because models like this are simplistic, they cannot provide numerically precise predictions or estimates for the unknowably complex systems of real life. However, they can provide informed input to policy changes or illuminate promising paths for additional research. I think the lesson from this analysis is that regardless of what the parameters of an epidemic are, what you do at the start of the epidemic is really important, and delaying by a few days can have enormous consequences.
