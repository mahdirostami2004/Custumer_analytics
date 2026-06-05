# Customer Analytics – RFM Segmentation

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-1.5%2B-blueviolet)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

This project performs **customer segmentation** using **RFM analysis** (Recency, Frequency, Monetary) on the UCI Online Retail dataset.  
It identifies valuable customer groups such as **Champions**, **Loyal**, **Potential**, **At Risk**, and **Others**, and visualizes their distribution.

## 📊 Key Visualizations

### RFM Metrics Distribution
![RFM Distribution](reports/rfm_distribution.png)

### Customer Segment Proportions
![Segments Pie](reports/segments_pie.png)

### Top 10 Customers by Monetary Value
![Top Customers](reports/top10_customers.png)

## 🔍 Business Insights

- **Champions** (8.5%): highest value and most frequent customers — reward and retain them.
- **At Risk** (22.1%): customers who have not purchased recently — target with re-engagement campaigns.
- **Loyal** and **Potential** customers can be targeted for upselling and retention strategies.

## 🛠️ Technologies Used

- Python 3.8+
- Pandas
- NumPy
- Matplotlib

## 📁 Project Structure
```text
.
├── data/           # Raw and cleaned data (CSV)
├── reports/        # Generated charts (PNG)
├── scripts/        # Python scripts
│   ├── clean_data.py
│   ├── rfm_analysis.py
│   ├── visualize.py
│   └── run_all.py
├── requirements.txt
└── README.md
'''

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/mahdirostami2004/Custumer_analytics.git
cd Custumer_analytics
