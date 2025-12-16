# Credit Risk Modeling
A machine learning project that predicts a borrower’s likelihood of loan default for data science and finance applications.

## Business Problem
Financial institutions need to assess the likelihood of loan applicants defaulting to minimize losses and make informed lending decisions. This project builds a machine learning model that predicts whether a borrower is a good or bad credit risk, helping banks make data-driven lending decisions and reduce credit risk.

## Data Preprocessing
#### Handling Missing Values
Checked the dataset for missing values and removed rows with missing data to ensure a clean dataset for modeling.

## Data Visualization
#### Distributions of Sex, Job, Housing, Saving accounts, Checking account, Purpose
![image alt](https://github.com/SundeepChaluvadi/Credit-Risk-Modeling/blob/3de66133cbd6d3d83bfab5818abbab8d051a586b/images/Distributions.png)

#### High Correlation between Credit Amount and Duration
![image alt](https://github.com/SundeepChaluvadi/Credit-Risk-Modeling/blob/6a13e2a2c1fd0df6b6b188ea8a4676e5ff6196ae/images/Correlation.png)

#### Most of the credit is centered aroung young age with low credit amount <br> As the credit amount is increasing, larger dots implying more duration
![image alt](https://github.com/SundeepChaluvadi/Credit-Risk-Modeling/blob/816ce753b88c3b98cc5c27218dd3f70f0ee95800/images/Credit_Amt_By_Sex_and_Duration.png)

#### "Credit amount" and "Duration" affect "Risk" highly
![image alt](https://github.com/SundeepChaluvadi/Credit-Risk-Modeling/blob/816ce753b88c3b98cc5c27218dd3f70f0ee95800/images/Credit_amt_and_Duration_Risk.png)

## Dependencies
```bash
  pip install -r requirements.txt
```

## Installation
Clone the repository:

```bash
  git clone https://github.com/SundeepChaluvadi/Credit-Risk-Modeling.git
  cd credit-risk-modeling
```

## Sources
https://www.kaggle.com/datasets/kabure/german-credit-data-with-risk
