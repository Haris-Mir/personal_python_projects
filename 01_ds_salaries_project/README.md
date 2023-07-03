# AI, ML, Data Salaries Project


## Table of Contents

1. [Introduction](#1.-Introduction)
    1.1 [Data Source](#1.1-Data-Source)
    1.2 [Feature Description](#1.2-Feature-Description)
    1.3 [Problem Statement](#1.3-Problem-Statement)
2. [Project Organization](#2.-Project-Organization)


## 1. Introduction

* I worked on this dataset in the first semester of my postgradute degree in Master of Data Science. I think it is intuitive to understand the end result of one's study goals and give it a clear and concise model. There is no better way to do it but to analyze the salaries of people working in AL, ML, and Data fields along with their job titles, job experience, and location etc. I will use CRISP-DM phyilosophy to execute this project. 

* "Salary for AI, ML Data jobs" is one of the fascinating practical topics, currently receiving great attention from the community of people studying and working in the field of Data Science.

* Helping those interested in the field of Data Science:
    - Get an overview of the changes in this field from 2020 to the present.
    - Capture the trend of working and salary between industries going on in the world.
    - Provide a lot of useful information to give directions on future work.

### 1.1 Data Source

The dataset is taken from kaggle.com website. To see the link of page please click [_here_](https://www.kaggle.com/datasets/nguyenthicamlai/ai-ml-data-salaries). 

* The data source is available with a worldwide contribution size, being collected and updated continuously from 2020 to the present time (usually on a weekly basis). The dataset is published in the public domain, users can access and download the dataset easily.
* This dataset was extracted from Kaggle on __1st July 2023__.

### 1.2 Feature Description

* __work_year__: The year the salary was paid.
* __experience_level__: The experience level in the job during the year with the following possible values
    - EN Entry-level
    - MI Junior Mid-level
    - SE Intermediate Senior-level
    - EX Expert Executive-level / Director
* __employment_type__: The type of employment for the role
    - PT Part-time
    - FT Full-time
    - CT Contract
    - FL Freelance
* __job_title__: The role worked in during the year.
* __salary__: The total gross salary amount paid.
* __salary_currency__: The currency of the salary paid as an ISO 4217 currency code.
* __salary_in_usd__: The salary in USD (FX rate divided by avg. USD rate for the respective year via fxdata.foorilla.com.
* __employee_residence__: Employee's primary country of residence in during the work year as an ISO 3166 country code.
* __remote_ratio__: The overall amount of work done remotely, possible values are as follows
    - 0 No remote work (less than 20%)
    - 50 Partially remote
    - 100 Fully remote (more than 80%)
* __company_location__: The country of the employer's main office or contracting branch as an ISO 3166 country code.
* __company_size__: The average number of people that worked for the company during the year
    - S less than 50 employees (small)
    - M 50 to 250 employees (medium)
    - L more than 250 employees (large)
    
### 1.3 Problem Statement

We can extract many valuable insights from this dataset. As this datset provides three years salary data (dependent variable) of three major fields (AI, ML, and Data), we can address some of the following questions from the thorough analysis of the dataset:

#### Exploratory Data Analysis (EDA)

* How have salaries in the AI, ML, and Data fields changed from 2020 to 2023?
* What are the most common job titles and employment types in the AI, ML, and Data fields?
* How does experience level and employment type affect salary in the AI, ML, and Data fields?
* Are there any significant differences in salary trends between different industries or company sizes?
* What is the impact of remote work on salary in the AI, ML, and Data fields?

#### RFS and Heirarchical clustering

* Can we group similar types of jobs based on their salaries and other features using clustering techniques?
* What are the most important features in predicting salaries in the AI, ML, and Data fields?

#### Machine Learning (ML)

* Can we predict salaries in the AI, ML, and Data fields based on certain features such as job title, experience level, or company size?
* What is the best model or technique for predicting salaries in the AI, ML, and Data fields based on our evaluation criteria?

## 2. Project Organization

Project organization is loosly based on Cookiecutter's Data Science Template. As this project is not too complex, therefore, I have reduced some of the elements from the template to make it more readable. To know about the template please click [_here_](https://drivendata.github.io/cookiecutter-data-science/). 


    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.

