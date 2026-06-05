import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_rfm(filepath="data/rfm_scores.csv"):
    return pd.read_csv(filepath)

def plot_rfm_distribution(rfm, save_dir="reports"):
    os.makedirs(save_dir, exist_ok=True)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    sns.histplot(rfm['Recency'], bins=30, kde=True, ax=axes[0])
    axes[0].set_title('Recency Distribution (days since last purchase)')
    
    sns.histplot(rfm['Frequency'], bins=30, kde=True, ax=axes[1])
    axes[1].set_title('Frequency Distribution (number of orders)')
    
    sns.histplot(rfm['Monetary'], bins=30, kde=True, ax=axes[2])
    axes[2].set_title('Monetary Distribution (total spend)')
    
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
    sns.barplot(data=top10, x='CustomerID', y='Monetary', palette='viridis')
    plt.title('Top 10 Customers by Monetary Value')
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
    