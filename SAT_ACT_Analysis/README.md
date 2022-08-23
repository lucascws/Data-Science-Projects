## Problem Statement

How do socio-economic indicators relate to state-level test scores?

## Executive Summary

There are growing concerns that the ACT and SAT are bias and affected by other socio-economic factors, making the test an unfair method to judge a student for college admissions. To investigate this concern, we are assisting the US Department of Education in conducting a preliminary analysis on how several socio-economic factors affect the ACT and SAT scores on a state level. From our findings, there is definitely an indication that the state average test scores for both ACT and SAT are affected by factors such as the state's racial diversity, population density and how developed a state is. These factors affect the state average test scores to a different level of magnitude. These findings do suggest that further analysis needs to be done on other factors and at an individual student level to determine how much each variable affects the student's ACT and SAT scores.

## Background

The SAT and ACT are standardized tests that many colleges and universities in the United States require for their admissions process. This score is used along with other materials such as grade point average (GPA) and essay responses to determine whether or not a potential student will be accepted to the university.

The SAT has two sections of the test: Evidence-Based Reading and Writing and Math ([*source*](https://www.princetonreview.com/college/sat-sections)). The ACT has 4 sections: English, Mathematics, Reading, and Science, with an additional optional writing section ([*source*](https://www.act.org/content/act/en/products-and-services/the-act/scores/understanding-your-scores.html)). 
* [SAT](https://collegereadiness.collegeboard.org/sat)
* [ACT](https://www.act.org/content/act/en.html)

In recent years, there are growing concerns that the SAT and ACT are not a fair measure of assessment for colleges and universities as they are bias towards various socio-economic factors. ([*source*](https://www.forbes.com/sites/kimelsesser/2019/12/11/lawsuit-claims-sat-and-act-are-biased-heres-what-research-says/?sh=9d693b63c429)) This includes racial and economic biasness in the test scores. For instance, research has indicated that SAT scores for family with an income of more than USD100,000 is significantly higher than family with an income of lower than USD50,000. White Students tend to perform better than African-American and Hispanic Students. ([*source*](https://www.forbes.com/sites/markkantrowitz/2021/05/21/how-admissions-tests-discriminate-against-low-income-and-minority-student-admissions-at-selective-colleges/?sh=77b5a88f3cc1))

In 2019, there was even a lawsuit raised against the University of California claiming they are "violating state civil rights laws by requiring applicants to take the SAT or ACT, standardized tests that unlawfully discriminate against disabled, low-income, multilingual and underrepresented minority students". ([*source*](https://www.latimes.com/california/story/2019-12-10/uc-violates-civil-rights-of-disadvantaged-students-by-requiring-sat-for-admission-lawsuit-alleges)) In light of the rising number of claims challenging the fairness of the ACT and SAT for college admissions, we are task to conduct an analysis for the US Department of Education to delve gain a better understanding of some of these issues.

As consultants to the US Department of Education, we are tasked with analysing if socio-economic factors do affect ACT and SAT test scores. In the analysis below, we will look further into three features of interest, the Human Development Index (HDI), Racial Diversity and Population Density, and look into how they affect the ACT and SAT Scores. Our Analysis is done at the State level, comparing the state average scores with the State's HDI, Racial Diversity and Population Density.


### Dataset

* [`act_2017.csv`](./data/act_2017.csv): 2017 ACT Scores by State
* [`act_2018.csv`](./data/act_2018.csv): 2018 ACT Scores by State
* [`act_2019.csv`](./data/act_2019.csv): 2019 ACT Scores by State
* [`sat_2017.csv`](./data/sat_2017.csv): 2017 SAT Scores by State
* [`sat_2018.csv`](./data/sat_2018.csv): 2018 SAT Scores by State
* [`sat_2019.csv`](./data/sat_2019.csv): 2019 SAT Scores by State
* [`race_perc_2019.csv`](./data/race_perc_2019.csv): Racial Composition of the Population by State
* [`hdi_2019.csv`](./data/hdi_2019.csv): HDI Index by State
* [`population_density_2020.csv`](./data/population_density_2020.csv): Population Density by State


### Further Research - Other Datasets

**Human Development Index (HDI)**

- The HDI serves as a metric to assess the development of a region. (Not just economic growth) The key measures that make up a HDI are:
    - Life Expectancy
    - Knowledge
    - Standard of Living
- The HDI ranges from 0 to 1
- A higher HDI incidates that the state is more developed
- We will be assessing if there is a difference in ACT/SAT scores between states with higher or lower HDI

* [HDI](https://hdr.undp.org/en/content/human-development-index-hdi)
* [Data Source](https://globaldatalab.org/shdi/shdi/USA/?levels=1%2B4&interpolation=1&extrapolation=0&nearest_real=0&years=2019)

**Racial Diversity**

- The Racial Diversity metric serves as an indicator of how racially diverse a state is. This is an indicator of how racially diverse a state is (we do not consider the racial composition of the state itself)
- To attain a metric for racial diversity of each state, we will be using an index called Herfindahl–Hirschman Index (HHI)
    - The range of the HHI is from 0 to 1
    - The HHI is calculated by squaring the proportion of each race in the state
    - A higher HHI indicates that the state is less racially diverse
- We will be assessing if there is a difference in ACT/SAT scores between states with higher or lower racial diversity

* [HHI](https://www.justice.gov/atr/herfindahl-hirschman-index)
* [Data Source](https://worldpopulationreview.com/states/states-by-race)  

**Population Density**

- The population density is a measure of how densely populated each states are
- We will be using a measure of the population per km^2 in each state
- We will be assessing if there is a difference in ACT/SAT scores between states with higher or lower population density

* [Data Source](https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population_density)    


### Data Dictionary - Dataset 1 (SAT and ACT scores by state for all three years)

|Feature|Type|Description|
|---|---|---|
|state|string|Name of the State (used as the label and key for the row)|
|score|float|The average test score - our main variable of concern|
|high_participation|bool|Whether the participation rate of the state is more than 90%|
|year|integer|The year where the average test score relates to|
|test|string|type of test - "ACT" or "SAT"|


### Data Dictionary for 2019 dataset

|Feature|Type|Description|Source|
|---|---|---|---|
|state|string|Name of the State (used as the label and key for the row)|act/sat|
|score|float|The average test score - our main variable of concern|act/sat|
|high_participation|bool|Whether the participation rate of the state is more than 90%|act/sat|
|year|integer|The year where the average test score relates to|act/sat|
|test|string|type of test - "ACT" or "SAT"|act/sat|
|hdi|float|The HDI index of the state in 2019|hdi_2019|
|diversity_metric|float|The HHI Diversity index of the state in 2019 (the closer the value to 1 - the lower the racial diversity of the state)|race_perc_2019|
|population_density|float|The population density of the state in 2020 (number of pax per km^2|population_density_2019|

## Summary of Findings

|Feature|Correlation with ACT|Correlation with SAT|Summary|
|---|---|---|---|
|Participation Rate|-0.86|-0.83|High negative correlation with Participation Rate for both ACT and SAT scores|
|HDI|0.61|0.036|High positive correlation with HDI for ACT but no correlation for SAT|
|Racial Diversity|0.17|0.22|Low positive correlation with Racial Diversity for both ACT and SAT scores|
|Population Density|0.55|-0.38|Moderate positive correlation with Population Density for ACT but moderate negative correlation for SAT|

**Participation Rate**

Our analysis indicates that both SAT and ACT scores tend to be lower as Participation rate of the state increases. 

**HDI**

States with higher HDI tend to have better ACT scores. However, there does not seem to be any relationship between HDI and the SAT scores based on the Pearson's correlation coefficient.

**Racial Diversity*

States that are more racially diverse tend to perform worse for both ACT and SAT. (Higher Racial Diversity Metric indicate a lower Racial Diversity in the state) However, the correlation coefficient is relatively low, which suggest that the relationship might not be strong.

**Population Density**

States which have a higher population density tend to perform better on the ACT. However, the opposite observation can been seen for SAT, where states with a higher population density tend to perform worse.


## Conclusions and Recommendations

**Conclusion**

From our analysis, socio-economic factors definitely does seem to affect ACT and SAT score. The ACT and SAT scores seem to be affected by the different socio-economic factors we have analysed to varying degrees. Some that are noteworthy are:

1. ACT scores are strongly positively correlated with HDI
2. Population Density affects ACT and SAT in opposite directions (Positive Correlation with ACT and Negative Correlation with SAT)

However, there is also a strong possibility that they are not independent of one another. Nevertheless, the evidence does indicate that the ACT and SAT are affected by external socio-economic factors.

**Recommendations**

Our prelimnary analysis indicates that ACT and SAT scores are affected by socio-economic factors on a state level. In order to tackle the issue of fairness of the ACT and SAT test, further analysis would be needed to explore out the magnitude of a socio-economic factor on an individual's ACT and SAT score. For instance, one further analysis that can can be done on how each race perform on the tests and whether the test are fair across the various race. 

1. Study other socio-economic features (such as Scores between Genders)
2. Analysis on individual student level instead of just state level
