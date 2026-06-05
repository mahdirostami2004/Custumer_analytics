# Customer Analytics – RFM Segmentation

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-1.5%2B-blueviolet)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

This project performs **customer segmentation** using **RFM analysis** (Recency, Frequency, Monetary) on the UCI Online Retail dataset.  
It identifies valuable customer groups (Champions, Loyal, Potential, At Risk, Others) and visualizes their distribution.

## 📊 Key Visualizations

### RFM Metrics Distribution
![RFM Distribution](reports/rfm_distribution.png)

### Customer Segment Proportions
![Segments Pie](reports/segments_pie.png)

### Top 10 Customers by Monetary Value
![Top Customers](reports/top10_customers.png)

## 🔍 Business Insights
- **Champions** (8.5%): highest value, most frequent – reward them.
- **At Risk** (22.1%): haven't purchased recently – re-engagement campaigns.
- **Loyal & Potential** can be targeted for upselling.

## 🛠️ Technologies Used
- Python 3.8+
- Pandas, NumPy
- Matplotlib

## 📁 Project Structure

├── data/ # Raw and cleaned data (CSV)
├── reports/ # Generated charts (PNG)
├── scripts/ # Python scripts
│ ├── clean_data.py
│ ├── rfm_analysis.py
│ ├── visualize.py
│ └── run_all.py
├── requirements.txt
└── README.md



## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/mahdirostami2004/Custumer_analytics.git
   cd Custumer_analytics

Install dependencies
bash

pip install -r requirements.txt

Add the dataset
Download online_retail.csv from UCI and place it inside data/.

Run the pipeline
bash

python scripts/run_all.py

Or step by step:
bash

python scripts/clean_data.py
python scripts/rfm_analysis.py
python scripts/visualize.py

📈 Results

    Cleaned data saved as data/cleaned_data.csv

    RFM scores saved as data/rfm_scores.csv

    Charts saved in reports/ folder

📚 Dataset Source

UCI Online Retail – Transaction data from a UK online retailer (2010–2011).
