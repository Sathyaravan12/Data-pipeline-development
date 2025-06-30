import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

data = pd.DataFrame({
    'Age': [22, 38, None, 35],
    'Fare': [7.25, 71.83, 8.05, None],
    'Sex': ['male', 'female', 'female', 'male'],
    'Embarked': ['S', 'C', 'S', None]
})


num_cols = ['Age', 'Fare']
cat_cols = ['Sex', 'Embarked']

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', num_pipeline, num_cols),
    ('cat', cat_pipeline, cat_cols)
])

processed_data = preprocessor.fit_transform(data)


print(processed_data.toarray() if hasattr(processed_data, "toarray") else processed_data)
