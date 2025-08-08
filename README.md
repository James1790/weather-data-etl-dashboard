# Weather Data ETL & Tableau Dashboard Project

## 📌 Overview
This project is an **end-to-end data engineering and analytics pipeline** that collects, stores, cleans, and visualizes **five years of historical monthly weather data** for multiple U.S. cities.  
The workflow demonstrates **ETL (Extract, Transform, Load)** processes using Python and SQLite, followed by **data analysis and dashboard creation in Tableau** to uncover trends and insights.

The goal was to create a **fully automated data pipeline** capable of:
1. **Extracting** data from an API.
2. **Storing** it in a relational database.
3. **Cleaning and preparing** it for visualization.
4. **Presenting interactive insights** in a professional dashboard.

---

## 🛠 Tools & Technologies
- **Programming Language:** Python (Requests, Pandas, Dateutil, Dotenv, SQLite3)
- **Database:** SQLite (Relational Database)
- **Data Source:** [Visual Crossing Weather API](https://www.visualcrossing.com/weather-data)
- **Visualization:** Tableau (Interactive Dashboard)
- **Version Control:** Git & GitHub

---

## 🔄 Project Workflow

### 1. **Data Extraction (API Integration)**
- Used the **Visual Crossing Weather API** to request monthly historical weather data for:
  - Chicago, IL
  - Minneapolis, MN
  - Des Moines, IA
  - Indianapolis, IN
  - St. Louis, MO
- Implemented **dynamic date generation** using Python’s `datetime` and `dateutil.relativedelta` to pull data for the last 5 years automatically.
- Parameters included **average temperature**, **minimum temperature**, **maximum temperature**, **precipitation**, and **weather conditions**.

**Skills Demonstrated:**  
`API Integration`, `Data Acquisition`, `REST API`, `Python Automation`

---

### 2. **Data Storage (SQLite Database)**
- Designed and created a **SQLite database (`weather.db`)** to store extracted weather data.
- Created an **ETL pipeline**:
  - **Extract:** API call
  - **Transform:** Extracted relevant JSON fields & clean Data
  - **Load:** Inserted into SQLite
- Added **error handling** to ensure robustness during API failures or network issues.

**Skills Demonstrated:**  
`SQL`, `Database Management`, `ETL Pipelines`, `Data Modeling`

---

### 3. **Data Cleaning & Preparation**
- Exported data from SQLite and loaded into **Pandas** for cleaning.
- Standardized:
  - Date formats
  - City name consistency
  - Weather condition categories
- Handled missing/null values appropriately.
- Saved cleaned dataset to `cleaned_weather.csv` for Tableau integration.

**Skills Demonstrated:**  
`Data Wrangling`, `Data Cleaning`, `Pandas`, `Data Quality Assurance`

---

### 4. **Data Analysis & Visualization (Tableau)**
- Built an **interactive Tableau dashboard** to display:
  - **Average Temperature Trends** (Line Charts)
  - **Precipitation Levels** (Bar Charts)
  - **Weather Condition Frequency** (Pie/Bar Charts)
  - **KPI/BAN Cards** for:
    - Highest recorded temperature (84.6°F)
    - Lowest recorded temperature (-6.6°F)
- Added **city and year filters** for interactivity.
- Used **color encoding** to highlight highest and lowest temperature cities.
- Included **insight callouts** such as:
  > "Indianapolis & St. Louis had the highest average annual temperatures (58°F), while Minneapolis recorded the lowest (46°F)."

**Skills Demonstrated:**  
`Data Visualization`, `Business Intelligence`, `Tableau`, `Storytelling with Data`, `KPI Dashboards`

---

## 📊 Key Insights
- **Temperature Extremes:**  
  - Max recorded temp: **84.6°F**
  - Min recorded temp: **-6.6°F**
- **Warmest Cities:** Indianapolis & St. Louis (avg annual temp: ~58°F)
- **Coldest City:** Minneapolis (avg annual temp: ~46°F)
- **Precipitation Trends:** Precipitation distribution varied significantly between cities, with notable seasonal peaks.

---

## 📂 Repository Contents
- `weather_etl.py` → Python ETL script for API calls and database insertion.
- `cleaned_weather.csv` → Cleaned dataset ready for analysis.
- `weather.db` → SQLite database containing raw extracted weather data.
- `weather_query_notebook.ipynb` → Jupyter Notebook with SQL queries and exploratory analysis.
- `Weather_Dashboard.twbx` → Packaged Tableau dashboard.
- `README.md` → Project documentation (this file).
