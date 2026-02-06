# Data Cleaning Guide with Pandas

This guide demonstrates basic data cleaning techniques using Pandas, based on the `sample_data.csv` file.

## Prerequisites

Ensure you have Pandas installed and the virtual environment activated.

## Loading Data

```python
import pandas as pd

# Load the CSV file
df = pd.read_csv('data/sample_data.csv')
print("Data loaded:")
print(df.head())
```

## Exploring Data

```python
# Basic info
print(df.info())

# Summary statistics
print(df.describe())

# Check for missing values
print("Missing values:")
print(df.isnull().sum())
```

## Handling Missing Values

```python
# Example: Fill missing salaries with mean
if df['salary'].isnull().any():
    df['salary'].fillna(df['salary'].mean(), inplace=True)
    print("Filled missing salaries with mean.")
```

## Data Type Conversions

```python
# Ensure age is integer
df['age'] = df['age'].astype(int)

# Check data types
print("Data types:")
print(df.dtypes)
```

## Filtering and Cleaning

```python
# Remove duplicates
df.drop_duplicates(inplace=True)

# Filter valid ages
df = df[df['age'] > 0]
```

## Saving Cleaned Data

```python
# Save to new CSV
df.to_csv('data/cleaned_sample_data.csv', index=False)
print("Cleaned data saved.")
```

## Next Steps

Experiment with more advanced cleaning: outlier removal, string processing, etc. Refer to Pandas documentation for more.