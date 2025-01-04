import os
import pandas as pd
from driver import get_driver
from process import do_process

def get_csv_files(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
def extract_titles_from_csv(file_path):
    df = pd.read_csv(file_path)
    titles = df['Title'].tolist() 
    return titles 
    
def main():
    files = get_csv_files('csv')
    titles = []
    
    for file in files:
        titles.extend(extract_titles_from_csv(f"csv/{file}"))
    
    for item in titles:
        do_process(item)
    
if __name__ == "__main__":
    main()