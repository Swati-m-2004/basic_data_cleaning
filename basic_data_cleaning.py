import pandas as pd

# Task 25: Basic Data Cleaning
# Install: pip install pandas
# Run: python basic_data_cleaning.py

data = {
    "Student_ID": ["S101", "S102", "S103", "S104", "S102", "S105", "S106"],
    "Name": ["Asha", "Rahul", "Meera", "Arun", "Rahul", "Divya", "Kiran"],
    "Age": ["20", "21", "20", "twenty-two", "21", "19", "20"],
    "Department": ["CSE", "ECE", "CSE", "ISE", "ECE", "CSE", "ISE"],
    "Marks": ["85", "missing", "91", "76", "missing", "88", "79"],
    "Attendance": [92.0, 85.0, None, 78.0, 85.0, None, 89.0]
}

df = pd.DataFrame(data)

print("ORIGINAL DATA")
print(df)
print("\nOriginal shape:", df.shape)
print("\nOriginal data types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nExact duplicate rows:", df.duplicated().sum())

cleaned = df.copy()

# Convert numeric text to numeric values. Invalid text becomes missing.
cleaned["Age"] = pd.to_numeric(cleaned["Age"], errors="coerce").astype("Int64")
cleaned["Marks"] = pd.to_numeric(cleaned["Marks"], errors="coerce")

# Remove exact duplicate rows, keeping the first occurrence.
rows_before = len(cleaned)
cleaned = cleaned.drop_duplicates()
print("\nDuplicate rows removed:", rows_before - len(cleaned))

# Fill missing numerical values with their column medians for this example.
# Select an imputation method based on the real dataset and its context.
for column in ["Age", "Marks", "Attendance"]:
    if cleaned[column].isna().any():
        cleaned[column] = cleaned[column].fillna(cleaned[column].median())

print("\nCLEANED DATA")
print(cleaned)
print("\nCorrected data types:\n", cleaned.dtypes)
print("\nMissing values after treatment:\n", cleaned.isna().sum())
print("\nDuplicate rows after cleaning:", cleaned.duplicated().sum())
print("Rows before cleaning:", len(df))
print("Rows after cleaning:", len(cleaned))

df.to_csv("original_dataset.csv", index=False)
cleaned.to_csv("cleaned_dataset.csv", index=False)
print("\nSaved original_dataset.csv and cleaned_dataset.csv")
