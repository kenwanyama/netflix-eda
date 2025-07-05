import pandas as pd


input_path = 'data/processed/netflix_final_clean.csv'
output_path = 'data/processed/netflix_final_clean_12cols.csv'

df = pd.read_csv(input_path)

df_first12 = df.iloc[:, :12]

# Save to a new CSV
df_first12.to_csv(output_path, index=False)

print(f"done, path: {output_path}")