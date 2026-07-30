# 🏥 Data Visualization Project: Hospital Patient Treatment Analysis

An end-to-end data visualization project that analyzes hospital patient treatment data to uncover trends in treatment cost, hospital stay duration, recovery outcomes, department performance, and doctor efficiency.  
The project includes data cleaning, exploratory data analysis (EDA), interactive visualizations, and two Streamlit dashboards.

---

## 📌 Project Overview

This project explores the *Hospital Patient Treatment Dataset* using Python and modern data visualization libraries.  
The objective is to extract meaningful insights from the dataset and present them through interactive charts and dashboards.

The project demonstrates a complete data analysis workflow:

- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature Engineering  
- Plotly Visualizations  
- Streamlit Dashboards  
- Canva Presentation  

---

## 📁 Files in This Repository

- **Hospital_Patient_Treatment_Analysis.ipynb** — Full Jupyter Notebook analysis  
- **hospital_patient_treatment_dataset.csv** — Dataset used  
- **app_main.py** — Main Streamlit dashboard  
- **app_doctors.py** — Doctor performance dashboard  
- **presentation.pdf** — Final project presentation  
- **screenshots/** — Dashboard and chart images  
- **README.md** — Project documentation  

---

## 📊 Dataset Description

The dataset contains:

- Department  
- Treatment Type  
- Doctor Name  
- Gender  
- Age  
- Treatment Cost  
- Hospital Stay (Days)  
- Recovery Score  

It includes both **categorical** and **numerical** attributes, making it ideal for visualization and analysis.

---

## 🔧 Tools & Technologies Used

- Python  
- Pandas  
- NumPy  
- Plotly  
- Streamlit  
- Jupyter Notebook  
- Canva  

---

## 📘 Notebook Contents

### ✔ Data Cleaning
- Handling missing values  
- Removing duplicates  
- Converting data types  

### ✔ Feature Engineering
- Cost Category  
- Age Group  
- Recovery Level  

### ✔ Exploratory Data Analysis
- Summary statistics  
- Distribution analysis  
- Correlation insights  

### ✔ Visualizations (10 Analytical Questions)
1. Average Treatment Cost by Department  
2. Average Treatment Cost by Treatment Type  
3. Average Hospital Stay by Department  
4. Treatment Cost vs Recovery Score  
5. Number of Patients per Doctor  
6. Average Treatment Cost by Gender  
7. Hospital Stay by Age Group  
8. Average Recovery Score by Department  
9. Average Recovery Score by Treatment Type  
10. Average Recovery Score by Doctor  

---

## 📊 Streamlit Dashboards

### **1️⃣ Main Dashboard — `app_main.py`**
Includes:

- Filters: Department, Treatment Type, Doctor  
- Key metrics: Avg Cost, Avg Stay, Avg Recovery  
- Visuals:
  - Cost by Department  
  - Recovery by Treatment Type  
  - Cost vs Recovery Scatter  

Run:

```bash
streamlit run app_main.py


