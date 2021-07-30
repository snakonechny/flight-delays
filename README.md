# Flight Delays Project
Project brewing for a long time; revived again in Jul 2021

## Intro

Predicting flight delays is a common task for beginner's machine learning projects. It's a straightforward real world example of how one can take [readily available data](https://www.transtats.bts.gov/DL_SelectFields.asp?gnoyr_VQ=FGK&QO_fu146_anzr=b0-gvzr), run some rudimentary analyses on it, and produce a relatively good classifier for delay/no delay outcome.

The issue with most of these projects is how they conceptualize a delay. The unit of analysis is generally correct - it's a particular flight that will experience a delay/no delay outcome, not a plane or an airline. However, the explanatory variables that can be used to make a prediction go beyond just attributes of a plane or a flight. In fact, there are endless factors that can cause both a particular departure to be delayed, many of which are *systemic* (those belonging to the system in which a particular flight is operated) and not to the _physical airplane_ that's doing the flying.

In this pet project, I will model the universe of flights with respect to the system in which they are operated. Stated as series of assumptions:

(1) a flight can be delayed because of some [fat tail](https://en.wikipedia.org/wiki/Fat-tailed_distribution), low probability/high impact event. It's [futile](https://arxiv.org/abs/2001.10488) to model these. For example, [a catering truck gets a jammed gas pedal, hits the plane and causes massive delays](https://www.youtube.com/watch?v=RtVKF1feKHg). No model can predict a discrete event like that

(2) a flight can be delayed because of a trail of prior delays during preceding segments

(3) the cause of (2) may be (1), but it also may be some features of the airport, the operating environment, the air traffic control, etc. that triggered things to go amiss

(4) *if (1) is eliminated/discounted from a predictive model and the system in which a flight is operated can be represented with rich and useful attributes, we can build a model that predicts the likelihood of a delay given the systemic factors around it*

## Data used

[BTS's delays data](https://www.transtats.bts.gov/DL_SelectFields.asp?gnoyr_VQ=FGK&QO_fu146_anzr=b0-gvzr). Mercifully, there's years of clean flight-level data available for free. Sadly, a row in that dataset is a flight, which means we have to compute airport- and system-level stats ourselves.

## Plan of action

(0) do some exploratory work on tiny slice of this dataset

(1) write a heuristic for predicting a delayed flight. Doesn't have to be a probabilistic one - just come up with a rule of thumb for saying that a flight will be delayed or not; test it out on a bigger slice of data

(2) expand (1) to a probabilistic model with a handful of features