# 🛒 Active Product Sales Analysis

This project analyzes a product transaction dataset to uncover valuable insights into customer behavior, purchasing trends, and product performance. Using Python and libraries like **Pandas** and **Matplotlib**, the primary focus is to identify the peak purchasing hours of the day, which is crucial information for e-commerce businesses to optimize their marketing and operational strategies.

---

## 📊 Analysis Overview

This project performs several analyses to extract meaningful insights from the transaction data:

* **Purchase Time Analysis ⏰:** Identifies peak hours when customers make the most purchases and analyzes patterns by day or week to optimize marketing campaigns.
* **Product Analysis 📦:** Determines the most popular products based on purchase frequency and analyzes which products are often bought together.
* **Customer Analysis 👤:** Identifies top customers by the number of purchases or repeat buying behavior to spot high-value customers.
* **Purchase Frequency Analysis 🔁:** Counts how often each customer makes a purchase and analyzes the time between purchases to predict future behavior.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas:** For handling and analyzing tabular data.
* **NumPy:** For handling numerical operations.
* **Matplotlib & Seaborn:** For data visualization and creating plots.
* **Dateparser:** For parsing datetime strings.
* **Jupyter Notebook:** For interactive analysis and presentation.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone [https://your-repository-link.git](https://your-repository-link.git)
    cd your-repository-directory
    ```

2.  **Install necessary libraries:**
    ```bash
    pip install pandas numpy dateparser matplotlib seaborn
    ```

3.  **Run the Jupyter Notebook:**
    Open and run the `Product Sales Analysis.ipynb` file in your Jupyter environment to see the analysis workflow and visualizations.

---

## 💾 Dataset

The analysis is performed on an order details dataset. This dataset contains the following columns: `Name`, `Email`, `Product`, and `Transaction Date`.

The key findings from the notebook indicate:
- **Peak Purchase Hours:** The highest transaction volumes occur around **12:00 PM** and during the evening from **7:00 PM to 11:00 PM**.
- **Customer Behavior:** Most customers make only 1-2 transactions.

These insights suggest that marketing efforts and customer support should be intensified during these peak hours to maximize sales and customer satisfaction.

---

## 📈 Key Visualization

A key output of this analysis is a visualization of the **cumulative number of purchases by the hour of the day**, which clearly identifies the busiest hours.
