# Data-pipeline-development

*COMPANY*:CODTECH IT SOLUTIONS

*NAME*: SATHYA MURTHY E

*INTERN ID:CT08DK896

*DURATION*: 8 WEEKS

*MENTOR*: NEELAM SANTHOSH


##1. Introduction
In modern data-driven applications, raw datasets often contain inconsistencies such as missing values,
varying formats, and unstructured data. Effective preprocessing is crucial to ensure that machine
learning models can interpret and learn from data efficiently. This project, as part of the CODTECH
Internship Task 1, focuses on developing an automated ETL (Extract, Transform, Load) pipeline using
Python libraries like pandas and scikit-learn . The pipeline addresses data cleaning,
transformation, and encoding in a streamlined and reproducible manner.


2. Objective
The objective of this task is to develop a data preprocessing pipeline that automates the Extract,
Transform, and Load (ETL) process. This project utilizes the pandas library for data manipulation and
scikit-learn for preprocessing workflows. The pipeline is designed to handle missing values, scale
numerical features, and encode categorical variables in a clean and reusable structure.


4. Dataset Description
For demonstration purposes, a synthetic dataset is created with structure similar to the Titanic dataset.
The dataset includes both numerical and categorical variables, and contains missing values to simulate
real-world scenarios.

import pandas as pd
data = pd.DataFrame({
'Age': [22, 38, None, 35],
'Fare': [7.25, 71.83, 8.05, None],
'Sex': ['male', 'female', 'female', 'male'],
'Embarked': ['S', 'C', 'S', None]
})

5.Features:
Age : Numerical (with missing values)
Fare : Numerical (with missing values)
Sex : Categorical
Embarked : Categorical (with missing values)


4. Pipeline Design
a. Numerical Pipeline
This sub-pipeline handles numerical features. Missing values are imputed with the column mean, and
the values are then standardized using z-score normalization.

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
num_pipeline = Pipeline([
('imputer', SimpleImputer(strategy='mean')),
('scaler', StandardScaler())
])

b. Categorical Pipeline
This sub-pipeline manages categorical features. Missing values are imputed using the most frequent
value (mode), and the features are encoded using One-Hot Encoding.

from sklearn.preprocessing import OneHotEncoder
cat_pipeline = Pipeline([
('imputer', SimpleImputer(strategy='most_frequent')),
('encoder', OneHotEncoder(handle_unknown='ignore'))
])

c. Combining Pipelines with ColumnTransformer
A ColumnTransformer is used to apply the numerical and categorical pipelines to their respective
columns.

from sklearn.compose import ColumnTransformer
num_cols = ['Age', 'Fare']
cat_cols = ['Sex', 'Embarked']
preprocessor = ColumnTransformer([
('num', num_pipeline, num_cols),
('cat', cat_pipeline, cat_cols)
])
