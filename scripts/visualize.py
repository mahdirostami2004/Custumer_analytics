import pandas as pd
import matplotlib.pyplot as plt
import os

def load_rfm(filepath="data/rfm_scores.csv"):
    return pd.read_csv(filepath)

def plot_rfm_distribution(rfm, save_dir="reports"):
    os.makedirs(save_dir, exist_ok=True)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    axes[0].hist(rfm['Recency'], bins=30, edgecolor='black')
    axes[0].set_title('Recency Distribution (days since last purchase)')
    axes[0].set_xlabel('Days')
    axes[0].set_ylabel('Frequency')
    
    axes[1].hist(rfm['Frequency'], bins=30, edgecolor='black')
    axes[1].set_title('Frequency Distribution (number of orders)')
    axes[1].set_xlabel('Orders')
    axes[1].set_ylabel('Frequency')
    
    axes[2].hist(rfm['Monetary'], bins=30, edgecolor='black')
    axes[2].set_title('Monetary Distribution (total spend)')
    axes[2].set_xlabel('Revenue')
    axes[2].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.savefig(f"{save_dir}/rfm_distribution.png", dpi=150)
    plt.close()
    print(f"RFM distribution chart saved to {save_dir}/rfm_distribution.png")

def plot_segments_pie(rfm, save_dir="reports"):
    segment_counts = rfm['Segment'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Customer Segment Proportions')
    plt.savefig(f"{save_dir}/segments_pie.png", dpi=150)
    plt.close()
    print(f"Pie chart saved to {save_dir}/segments_pie.png")

def plot_top_customers(rfm, save_dir="reports"):
    top10 = rfm.nlargest(10, 'Monetary')[['CustomerID', 'Monetary', 'Frequency', 'Segment']]
    plt.figure(figsize=(12, 6))
    plt.bar(top10['CustomerID'].astype(str), top10['Monetary'], color='teal')
    plt.title('Top 10 Customers by Monetary Value')
    plt.xlabel('Customer ID')
    plt.ylabel('Total Spend')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{save_dir}/top10_customers.png", dpi=150)
    plt.close()
    print(f"Top customers chart saved to {save_dir}/top10_customers.png")

if __name__ == "__main__":
    if not os.path.exists("data/rfm_scores.csv"):
        raise FileNotFoundError("Please run rfm_analysis.py first.")
    
    rfm = load_rfm()
    plot_rfm_distribution(rfm)
    plot_segments_pie(rfm)
    plot_top_customers(rfm)
    print("All charts created successfully.")
