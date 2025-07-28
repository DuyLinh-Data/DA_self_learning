# 🦠 COVID-19 Data Analysis

This project provides an in-depth analysis of the global COVID-19 pandemic using real-world data. The analysis focuses on identifying trends over time and comparing the pandemic's impact across countries. Insights are extracted to understand the peak of the outbreak, fatality and recovery rates, and provide visual summaries of key metrics.

---

## 📊 Analysis Overview

### 1. 📅 Time Series Analysis
- Trends of confirmed cases, deaths, and recoveries by day and month.
- Identifies peak dates and months using visualizations.

### 2. 🌍 Country Comparison
- Compares total confirmed, deaths, and recoveries by country.
- Computes death and recovery rates.
- Visualizes top 10 countries by case count, death rate, and recovery rate.

---

## 🛠️ Technologies Used
- **Python**
- **Pandas** & **NumPy** for data manipulation.
- **Matplotlib** & **Seaborn** for visualizations.
- **Jupyter Notebook** for interactive analysis.

---

## 📁 Dataset
The dataset includes fields such as:
- `Date`, `Country/Region`, `Confirmed`, `Deaths`, `Recovered`, `Active`, `New cases`, `New deaths`, `New recovered`, `WHO Region`, `iso_alpha`.

The data is cleaned by removing negative values and converting appropriate columns to numerical or datetime formats.

---

## 📌 Key Insights
- 🕐 **Peak Hours**: Most new cases occurred around mid-2020.
- 🌍 **Top Countries**: Countries with the highest cases include the US, India, and Brazil.
- ⚠️ **Death Rate**: Some countries show alarming death rates; others excel in recovery.

---

## 📷 Sample Visualizations

<table>
  <tr>
    <td width="50%">
      <img src="https://raw.githubusercontent.com/DuyLinh-Data/DA_self_learning/main/Stats_covid19/figs/covid_trend_month.png" alt="Monthly COVID Trend" width="100%">
    </td>
    <td width="50%">
      <img src="https://raw.githubusercontent.com/DuyLinh-Data/DA_self_learning/main/Stats_covid19/figs/country_compare.png" alt="Country Comparison" width="100%">
    </td>
  </tr>
</table>

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/DuyLinh-Data/DA_self_learning.git
cd DA_self_learning/Stats_covid19
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the notebook:
```bash
jupyter notebook Stats_covid19.ipynb
```

---

## 📎 Summary

This analysis reveals crucial patterns of the COVID-19 pandemic, enabling better understanding of its progression and global impact. The visualizations and metrics provide a foundation for further epidemiological or public health studies.