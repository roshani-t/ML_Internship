# Machine Learning Internship – Week 1

## Life Expectancy Data Cleaning and Analysis

This project is part of my Machine Learning Internship Week 1.

The project focuses on Python fundamentals, data cleaning, exploratory data analysis, visualization, and deployment using Streamlit.

---

## Project Objective

The main objective of this project is to clean and analyze the Life Expectancy dataset.

The project performs the following tasks:

* Loads the Life Expectancy dataset.
* Removes duplicate rows.
* Removes rows where the target column, `Life expectancy`, is missing.
* Handles missing numerical values using country-wise median imputation.
* Uses the overall median as a fallback when a country has no available value.
* Handles missing text values using the mode.
* Creates visualizations to understand the dataset.
* Provides a command-line data cleaning tool.
* Provides a Streamlit web application.
* Includes a Jupyter Notebook for data analysis.

---

## Dataset

The dataset contains information about countries, years, health indicators, economic factors, and life expectancy.

The dataset contains **2938 rows and 22 columns** before cleaning.

After removing the 10 rows with missing `Life expectancy`, the cleaned dataset contains **2928 rows and 22 columns**.

---

## Data Cleaning Method

### Country-wise Median Imputation

Missing numerical values are filled using the median value of the same country.

For example, if a country's GDP value is missing, the cleaning program first calculates the median GDP for that country and uses that value.

This is more realistic than using one global median for every country because countries have different economic and health conditions.

If a country has no available value for a particular numerical column, the overall dataset median is used as a fallback.

### Target Column

Missing values in `Life expectancy` are not imputed.

Since `Life expectancy` is the main column being analyzed and can be used as a future prediction target, rows with missing target values are removed instead of creating artificial values.

---

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
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requirements

### Prerequisites

* Python 3.10 or higher
* pip
* Jupyter Notebook
* Internet connection for installing Python packages

Python 3.12 is recommended for this project.

---

## Installation

### Windows

Open PowerShell and go to the project folder:

```powershell
cd "D:\internship folder\ML_Internship"
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required libraries:

```powershell
pip install -r requirements.txt
```

### macOS / Linux

Open Terminal and go to the project folder:

```bash
cd /path/to/ML_Internship
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Running the Data Cleaning CLI

### Windows

```powershell
python src\clean_data.py data\LifeExpectancyData.csv data\cleaned_life_expectancy.csv
```

### macOS / Linux

```bash
python src/clean_data.py data/LifeExpectancyData.csv data/cleaned_life_expectancy.csv
```

The program displays:

* Original dataset shape
* Number of duplicate rows removed
* Number of rows removed because `Life expectancy` was missing
* Cleaned dataset shape
* Missing values after cleaning
* Location of the saved cleaned CSV file

The program also provides a clear error message if the input file does not exist.

---

## Running the Jupyter Notebook

### Windows

```powershell
jupyter notebook notebooks/data_analysis.ipynb
```

### macOS / Linux

```bash
jupyter notebook notebooks/data_analysis.ipynb
```

The notebook contains data analysis and visualizations including:

* Missing values before cleaning
* Life Expectancy Distribution
* Life Expectancy by Status
* Average Life Expectancy Over Years
* Top 10 Countries by Average Life Expectancy

---

## Running the Streamlit Application

Run:

```bash
streamlit run app.py
```

The application displays:

* Dataset overview
* Number of rows and columns
* Cleaned dataset
* Life expectancy analysis
* Average life expectancy by year

---

## Live Demo

The deployed Streamlit application is available here:

https://mlinternship-ytv3ei8mguhdujtetvsrjx.streamlit.app/

---

## GitHub Repository

GitHub repository:

https://github.com/roshani-t/ML_Internship

---

## Libraries Used

The project uses the following Python libraries:

* Pandas – data loading and cleaning
* NumPy – numerical analysis
* Matplotlib – data visualization
* Seaborn – statistical visualization
* Streamlit – web application
* Jupyter – notebook-based analysis

---

## Learning Outcomes

Through this project, I learned:

* Python fundamentals for data analysis
* Pandas DataFrame operations
* Handling missing values
* Removing duplicate records
* Country-wise data imputation
* Data visualization
* Exploratory data analysis
* Creating a command-line data cleaning tool
* Creating a Streamlit application
* Using Git and GitHub
* Deploying a Streamlit application

---

## Author

**Roshani Thakrani**

Machine Learning Intern
