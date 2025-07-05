with open('data/processed/netflix_final_clean_12cols.csv', 'rb') as f:
    for i, line in enumerate(f, 1):
        if 6 <= i <= 10:
            print(i, line)