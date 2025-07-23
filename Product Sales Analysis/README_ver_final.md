
# 🛒 Active Product Sales Analysis

This project explores a real-world product transaction dataset to uncover insights into customer behavior, purchasing trends, and product performance.  
Using Python with **Pandas**, **Matplotlib**, and **Seaborn**, the analysis focuses on **peak purchase hours** and customer patterns — crucial for optimizing marketing and operations.

---

## 🔍 Project Highlights

| Feature                          | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| ⏰ **Peak Purchase Hours**       | Identify the busiest hours and days for customer purchases                 |
| 📦 **Product Trend Analysis**    | Discover most frequently purchased items and item bundling patterns        |
| 👤 **Customer Insights**         | Find top buyers and loyal customers for potential retention strategies     |
| 🔁 **Purchase Frequency**        | Analyze time between repeat purchases to predict future behavior           |

---

## 💼 Business Impact

> 📈 This analysis enables data-driven decisions for:
> - Targeted ads during peak times
> - Smart inventory planning
> - Personalized offers for high-value customers

---

## 🛠️ Tech Stack

- **Python**
- **Pandas** for data manipulation  
- **NumPy** for numerical analysis  
- **Matplotlib & Seaborn** for visualizations  
- **Dateparser** for flexible time parsing  
- **Jupyter Notebook** for development

---

## 💾 Dataset Overview

The dataset includes the following fields:
- `Name`: Customer name  
- `Email`: Customer email  
- `Product`: Purchased item  
- `Transaction Date`: Purchase timestamp

> 🗂 Each record represents one transaction. We process time, group behavior, and product combinations to extract insights.

---

## 📊 Key Visualizations

<table>
  <tr>
    <td width="50%">
      <img src="https://raw.githubusercontent.com/DuyLinh-Data/DA_self_learning/main/Product%20Sales%20Analysis/pur_hour.png" alt="Purchase by Hour" width="100%">
    </td>
    <td width="50%">
      <img src="https://raw.githubusercontent.com/DuyLinh-Data/DA_self_learning/main/Product%20Sales%20Analysis/top10product.png" alt="Top Products" width="100%">
    </td>
  </tr>
</table>

> *Peak activity occurs around **12 PM** and between **7 PM – 11 PM**, providing ideal windows for marketing.*

---

### 🚀 How to Run This Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/DuyLinh-Data/Product-Sales-Analysis.git
   cd Product-Sales-Analysis
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Jupyter Notebook**
   ```bash
   jupyter notebook "Product Sales Analysis.ipynb"
   ```

---

### 📌 Summary or Takeaways

- ⏰ **Peak Purchase Hours**: Most transactions happen during **lunch (12 PM)** and **evening (7 PM–11 PM)** — ideal for targeted promotions.
- 📦 **Top-Selling Products**: A few products dominate sales, suggesting the potential for bundling or priority display.
- 👤 **Customer Frequency**: Majority of users are one-time buyers — indicating a need for re-engagement strategies.
