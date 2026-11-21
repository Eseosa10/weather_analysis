# Weather Analysis Germany

## Project Overview

This project analyzes historical temperature data from the German Weather Service (DWD).

The goal is to build a reproducible data pipeline that processes raw weather data, performs data quality checks, transforms the data into an analysis-friendly structure, and prepares it for further analysis using Python and SQL.

The project focuses on real-world data handling rather than machine learning and demonstrates practical data engineering and analytics skills.

---

## Research Question

How have temperatures in Germany changed over time and what data quality issues can be identified in the available weather records?

---

## Dataset

Source: Deutscher Wetterdienst (DWD)

The dataset contains historical monthly temperature averages for Germany and individual federal states.

Data characteristics:

- Historical records from 1881 onwards
- Monthly observations
- Measurements for Germany and multiple federal states
- Real-world data with quality issues such as empty columns

---

## Technologies

- Python
- Pandas
- Git & GitHub
- PostgreSQL (next project phase)
- Jupyter Notebook
- VS Code

---

## Project Structure

```text
weather_analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── data_loader.py
│   ├── data_quality.py
│   └── analysis.py
│
├── main.py
│
├── README.md
│
└── requirements.txt
```

---

## Data Pipeline

The project follows the following workflow:

1. Load raw DWD weather files
2. Perform data quality checks
3. Detect missing values
4. Detect duplicates
5. Detect empty columns
6. Clean the dataset
7. Transform data from wide format to long format
8. Export a cleaned dataset

---

## Data Quality Checks

Implemented quality checks:

- Missing value detection
- Duplicate detection
- Empty column detection
- Data type validation
- Temperature range validation

---

## Data Transformation

The original DWD files contain temperature data in wide format.

Example:

| Year | Month | Bayern | Nordrhein-Westfalen |
|--------|--------|--------|--------|
| 1881 | 1 | -6.51 | -4.21 |

The pipeline converts the data into long format:

| Year | Month | State | Temperature |
|--------|--------|--------|--------|
| 1881 | 1 | Bayern | -6.51 |
| 1881 | 1 | Nordrhein-Westfalen | -4.21 |

This format is better suited for SQL analysis and future visualizations.

---

## Results

Final processed dataset:

- 29,750 observations
- 4 columns:
  - Jahr
  - Monat
  - Bundesländer
  - Temperatur

The processed dataset is stored in:

```text
data/processed/weather_long.csv
```

---

## Key Findings

- January temperatures after 1950 are higher on average than before 1950.
- Bayern shows lower January temperatures compared to Nordrhein-Westfalen.
- Quality checks identified and removed an empty column in the raw dataset.
- A reproducible data pipeline was implemented to automate preprocessing.

---

## How To Run

Install requirements:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python main.py
```

Output:

```text
data/processed/weather_long.csv
```

---

## Skills Demonstrated

This project demonstrates:

- Data Cleaning
- Data Quality Assessment
- Exploratory Data Analysis (EDA)
- Pandas
- Modular Python Development
- Data Transformation
- Git Version Control
- Reproducible Data Pipelines
```
