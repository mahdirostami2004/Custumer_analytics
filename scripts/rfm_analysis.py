import pandas as pd
import os

def load_clean_data(filepath="data/cleaned_data.csv"):
    return pd.read_csv(filepath, parse_dates=['InvoiceDate'])

def compute_rfm(df):
    snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
    
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'Revenue': 'sum'
    }).rename(columns={
        'InvoiceDate': 'Recency',
        'InvoiceNo': 'Frequency',
        'Revenue': 'Monetary'
    }).reset_index()
    
    return rfm

def assign_scores(rfm):
    rfm['R_score'] = pd.qcut(rfm['Recency'], 4, labels=['4','3','2','1'])
    rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=['1','2','3','4'])
    rfm['M_score'] = pd.qcut(rfm['Monetary'], 4, labels=['1','2','3','4'])
    rfm['RFM_score'] = rfm['R_score'].astype(str) + rfm['F_score'].astype(str) + rfm['M_score'].astype(str)
    return rfm

def segment_customers(rfm):
    conditions = [
        (rfm['R_score'] == '1') & (rfm['F_score'] == '4') & (rfm['M_score'] == '4'),
        (rfm['R_score'] == '1') & (rfm['F_score'] >= '3') & (rfm['M_score'] >= '3'),
        (rfm['R_score'].isin(['2','3'])) & (rfm['F_score'].isin(['2','3'])),
        (rfm['R_score'] == '4') | (rfm['F_score'] == '1') | (rfm['M_score'] == '1')
    ]
    choices = ['Champions', 'Loyal', 'Potential', 'At Risk']
    rfm['Segment'] = pd.Series(index=rfm.index)
    for cond, choice in zip(conditions, choices):
        rfm.loc[cond, 'Segment'] = choice
    rfm['Segment'].fillna('Others', inplace=True)
    return rfm

def save_rfm(rfm, output_path="data/rfm_scores.csv"):
    rfm.to_csv(output_path, index=False)
    print(f"RFM file saved to {output_path}")

if __name__ == "__main__":
    if not os.path.exists("data/cleaned_data.csv"):
        raise FileNotFoundError("Please run clean_data.py first.")
    
    df = load_clean_data()
    rfm = compute_rfm(df)
    rfm = assign_scores(rfm)
    rfm = segment_customers(rfm)
    save_rfm(rfm)
    
    print("\n--- Quick stats ---")
    print(f"Total customers: {len(rfm)}")
    print(rfm['Segment'].value_counts())