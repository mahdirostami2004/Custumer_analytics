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


#🚀 How to Run

1. Clone the repository
'git clone https://github.com/mahdirostami2004/Custumer_analytics.git
cd Custumer_analytics

3. Install dependencies
'pip install -r requirements.txt

5. Add the dataset
Download online_retail.csv from UCI and place it inside the data/ folder.

7. Run the pipeline
To run all scripts at once:
'python3 scripts/run_all.py
Or run step by step:
'''python scripts/clean_data.py
python scripts/rfm_analysis.py
python scripts/visualize.py

##📈 Results
Cleaned data: Saved as data/cleaned_data.csv
RFM scores: Saved as data/rfm_scores.csv
Charts: Saved in the reports/ folder

##📚 Dataset Source
UCI Online Retail — Transaction data from a UK online retailer (2010–2011).
