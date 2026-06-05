import pandas as pd
import os

def load_data(filepath="data/online_retail.csv"):
    df = pd.read_csv(filepath, encoding='latin1')
    return df

def clean_data(df):
    df = df.dropna(subset=['CustomerID'])
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    return df

def save_clean_data(df, output_path="data/cleaned_data.csv"):
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}. Records: {len(df)}")

if __name__ == "__main__":
    if not os.path.exists("data/online_retail.csv"):
        raise FileNotFoundError("Please place online_retail.csv in the data/ folder.")
    
    df_raw = load_data()
    df_clean = clean_data(df_raw)
    save_clean_data(df_clean)
    print("Cleaning finished.")