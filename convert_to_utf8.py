input_path = 'data/processed/netflix_final_clean_12cols.csv'
output_path = 'data/processed/netflix_final_clean_12cols_utf8.csv'

with open(input_path, 'r', encoding='cp1252', errors='ignore') as fin:
    with open(output_path, 'w', encoding='utf-8') as fout:
        for line in fin:
            fout.write(line)

print("Conversion complete! Saved as:", output_path)