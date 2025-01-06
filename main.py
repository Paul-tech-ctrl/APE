import os
import json
import pandas as pd
from driver import get_driver
from process import do_process
from concurrent.futures import ThreadPoolExecutor


def get_csv_files(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
def extract_titles_from_csv(file_path):
    df = pd.read_csv(file_path)
    titles = df['Title'].tolist() 
    return titles 
    
def get_downloaded_search_keys(file_path='downloaded_search_keys.json'):
    file_exists = os.path.isfile(file_path)
    
    if file_exists:
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        data = []
        
    return data
    
def main():
    files = get_csv_files('csv')
    titles = []
    
    for file in files:
        titles.extend(extract_titles_from_csv(f"csv/{file}"))
        
    downloaded_search_keys = get_downloaded_search_keys()
    titles = [title for title in titles if title not in downloaded_search_keys] # Exclude already downloaded search keys
        
    # Use ThreadPoolExecutor to run Selenium browser instances concurrently with 5( can add more workers ) workers in this case
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(do_process, titles)

    
if __name__ == "__main__":
    main()