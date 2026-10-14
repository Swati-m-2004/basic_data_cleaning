# Task 25: Basic Data Cleaning

**Track:** AI & ML  
**Tools:** Python, Pandas, Jupyter Notebook

## Overview
This project combines missing-value handling, duplicate removal, and data-type correction in one workflow. It uses a small synthetic student-performance dataset with intentional data-quality issues.

## Objectives
- Inspect the dataset before making changes.
- Identify missing values and exact duplicate rows.
- Convert numeric text columns to numeric types.
- Remove exact duplicate records.
- Fill missing numeric values using the median in this example.
- Save original and cleaned datasets.

## Install and Run
```bash
pip install pandas
python basic_data_cleaning.py
```
You can also paste the code into a Jupyter Notebook cell.

## Cleaning Steps

### 1. Inspect the data
```python
df.dtypes
df.isna().sum()
df.duplicated().sum()
```

### 2. Correct data types
```python
df["Age"] = pd.to_numeric(df["Age"], errors="coerce").astype("Int64")
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
```
Invalid strings become missing values so they can be reviewed.

### 3. Remove duplicates
```python
df = df.drop_duplicates(keep="first")
```

### 4. Handle missing numeric values
```python
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
```
The project uses median imputation as an example. For real datasets, choose a method based on the data and why values are missing.

### 5. Validate and save
The script prints data types, missing-value counts, duplicate counts, and row totals. It creates:
- `original_dataset.csv`
- `cleaned_dataset.csv`

## Dataset
Columns: `Student_ID`, `Name`, `Age`, `Department`, `Marks`, and `Attendance`. All records are synthetic and intended for practice.

## Conclusion
Data cleaning improves consistency and helps prevent missing, duplicated, or incorrectly typed values from affecting analysis.

## Interview Questions
**1. What is data cleaning?** Identifying and treating inaccurate, incomplete, duplicated, or inconsistent data.

**2. Why is data cleaning important before machine learning?** Poor-quality data can lead to misleading analysis and unreliable predictions.

**3. What problems can poor-quality data cause?** Incorrect summaries, biased results, and unreliable predictions.

**4. How do you check missing values in Pandas?** Use `df.isna().sum()`.

**5. How do you remove duplicates?** Use `df.drop_duplicates()`.

**6. How do you convert text to numeric?** Use `pd.to_numeric()` with appropriate error handling.
