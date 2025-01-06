# Project Title

This project processes CSV files containing EPA EIS Filings and performs automated searches on the EPA website using Selenium.


## Files Description

- **csv/**: Directory containing the CSV files to be processed.
- **downloads/**: Directory where downloaded files will be saved.
- **driver.py**: Contains the function `get_driver` to initialize the Selenium WebDriver.
- **main.py**: Main script to execute the processing pipeline.
- **process.py**: Contains the `do_process` function to perform automated searches and handle CAPTCHA.

## How to Run

1. Ensure you have the required dependencies installed:
    ```sh
    pip install -r requirements.txt
    ```

2. Execute the main script:
    ```sh
    python main.py
    ```

## Functions

### main.py

- **get_csv_files(folder_path)**: Returns a list of CSV files in the specified folder.
- **extract_titles_from_csv(file_path)**: Extracts the 'Title' column from a CSV file and returns it as a list.
- **main()**: Main function to process CSV files and perform searches.

### process.py

- **do_process(search_key)**: Automates the search process on the EPA website using Selenium.
- **log_failed_search_key(search_key, file_path='failed_search_keys.csv')**: Logs failed search keys to a CSV file.

## Notes

- Ensure the WebDriver is correctly set up and the path is configured in `driver.py`.
- Adjust the sleep times in `process.py` based on your internet speed and system performance.