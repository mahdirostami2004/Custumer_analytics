# Customer Analytics – RFM Segmentation

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-1.5%2B-blueviolet)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

This project performs **customer segmentation** using **RFM analysis** (Recency, Frequency, Monetary) on the UCI Online Retail dataset.  
It identifies valuable customer groups (Champions, Loyal, Potential, At Risk, Others) and visualizes their distribution.

## 📊 Key Visualizations

### RFM Metrics Distribution
![RFM Distribution](reports/rfm_distribution.png)

### Customer Segment Proportions & Top 10 Customers
<div style="display: flex; gap: 10px; justify-content: space-between;">
  <img src="reports/segments_pie.png" alt="Segments Pie" style="width: 49%;" />
  <img src="reports/top10_customers.png" alt="Top Customers" style="width: 49%;" />
</div>

## 🔍 Business Insights
- **Champions** (8.5%): highest value, most frequent – reward them.
- **At Risk** (22.1%): haven't purchased recently – re-engagement campaigns.
- **Loyal & Potential** can be targeted for upselling.

## 🛠️ Technologies Used
- Python 3.8+
- Pandas, NumPy
- Matplotlib

## 📁 Project Structure
