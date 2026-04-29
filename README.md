# Data Cleaning Automation Tool

# Overview

This project is a Python-based tool designed to clean and preprocess raw datasets. It automates common data cleaning tasks such as removing duplicate records and handling missing values.

# Features

-Removes duplicate rows
- Handles missing values using mean imputation
- Maintains proper data types (e.g., integer formatting for age)
- Supports command-line input and output

# Technologies Used

- Python
- Pandas

# How to Run

Run the script from the terminal:

```bash
python clean_data.py data/raw_data.csv data/cleaned_data.csv
```

# Input Data

The input dataset includes:

- Name
- Age
- Salary

# Output

The tool generates a cleaned dataset:

- No duplicate records
- Missing values handled
- Proper formatting applied

# Project Structure
```
data-cleaning-tool/
├── clean_data.py
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
```
# Learning Outcome

This project demonstrates:

- Data preprocessing using Python
- Automation of repetitive data tasks
- Building reusable command-line tools

## Author

Ayman Shehzadi
Master’s in Artificial Intelligence
