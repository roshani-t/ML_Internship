# Machine Learning Internship – Week 1

## Project: Python Data Cleaning CLI Tool

This project was completed as part of Week 1 of the Machine Learning Internship.

The main goal of the project is to load a local dataset, inspect the data, clean missing values and duplicate records, and save the cleaned dataset using Python and Pandas.

## Dataset

The project uses the **Life Expectancy dataset**.

The dataset contains information about countries, years, health indicators, economic factors, and life expectancy.

### Dataset Size

* Rows: 2,938
* Columns: 22

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

## Project Structure

```text
ML_Internship/
│
├── data/
│   ├── LifeExpectancyData.csv
│   └── cleaned_life_expectancy.csv
│
├── notebooks/
│   └── data_analysis.ipynb
│
├── src/
│   └── clean_data.py
│
└── README.md
```

## Data Cleaning

The cleaning script performs the following operations:

1. Loads the CSV dataset.
2. Removes unnecessary spaces from column names.
3. Detects and removes duplicate rows.
4. Identifies numerical columns.
5. Fills missing numerical values using the median.
6. Identifies text columns.
7. Fills missing text values using the most common value.
8. Saves the cleaned dataset as a new CSV file.

After cleaning, the dataset contains **0 missing values**.

## How to Run the CLI Tool

Open a terminal in the project folder:

```bash
cd ML_Internship
```

Run the cleaning tool using:

```bash
python src\clean_data.py data\LifeExpectancyData.csv data\cleaned_life_expectancy.csv
```

The command follows this format:

```bash
python src\clean_data.py <input_file> <output_file>
```

### Example

```bash
python src\clean_data.py data\LifeExpectancyData.csv data\cleaned_life_expectancy.csv
```

The cleaned dataset will be saved inside the `data` folder.

## Data Analysis

A Jupyter Notebook is included in the `notebooks` folder.

The notebook contains visualizations for:

* Distribution of Life Expectancy
* Life Expectancy by Country Status
* Average Life Expectancy Over the Years
* Top 10 Countries by Average Life Expectancy

The visualizations were created using Matplotlib and Seaborn.

## Project Outcome

This project demonstrates basic skills in:

* Python programming
* Pandas data processing
* Missing-value imputation
* Duplicate detection
* Data cleaning
* Command Line Interface (CLI) usage
* Data visualization
* Jupyter Notebook analysis

## Author

Machine Learning Internship – Week 1
