import time, os, random, logging, json
from driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to scroll the page with random coordinates
def selenium_scroll(driver):
    driver.execute_script(f"window.scrollTo({random.randint(0, 1000)}, {random.randint(0, 1000)});")
    time.sleep(1)

def random_trigger(driver):
    num_triggers = random.randint(10, 20)
    for _ in range(num_triggers):
        selenium_scroll(driver)

# Function to mimic human behavior with random delays
def human_delay(driver, min_delay=5, max_delay=10):
    time.sleep(random.uniform(min_delay, max_delay))
    random_trigger(driver)
    
def do_process(search_key):
    driver = get_driver()
    try:
        time.sleep(5)
        # Navigate to the URL
        url = "https://cdxapps.epa.gov/cdx-enepa-II/public/action/eis/search"
        driver.get(url)
        human_delay(driver)
        
        # Locate the search bar by ID and input search_key
        search_bar = driver.find_element(By.ID, "title")
        search_bar.send_keys(search_key)
        human_delay(driver)
        
        # Locate the search button by ID and click it
        search_button = driver.find_element(By.ID, "searchButtonLink")
        search_button.click()
        logging.info("Search button clicked")
        human_delay(driver)
        
        time.sleep(15)

        # Wait for the results to load and locate the element by its text
        wait = WebDriverWait(driver, 30)
        element = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{search_key}')]")))
        human_delay(driver)
        element.click()
        human_delay(driver)
        
        time.sleep(20)

        # Wait for the reCAPTCHA iframe to be present
        recaptcha_iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]")))
        human_delay(driver)
        
        # Switch to the reCAPTCHA iframe
        driver.switch_to.frame(recaptcha_iframe)
        human_delay(driver)
        
        # Move the mouse to the document link before clicking
        captcha_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox-border")))
        human_delay(driver)
        
        actions = ActionChains(driver)
        actions.move_to_element(captcha_element).perform()
        human_delay(driver)
        
        # Click the document link
        captcha_element.click()

        time.sleep(10)

        # Switch back to the default content
        driver.switch_to.default_content()
        human_delay(driver)
        
        # Move the mouse to the document link before clicking
        eis_document_element = driver.find_element(By.XPATH, "//a[@href='javascript:void(0);']")
        actions = ActionChains(driver)
        actions.move_to_element(eis_document_element).perform()
        human_delay(driver)
        
        # Click the document link
        eis_document_element.click()

        # Wait for the download to complete (you might need to adjust the wait time)
        time.sleep(30)  # Adjust this time based on your download speed
        logging.info("Download complete")
        log_download_complete(search_key)
        
        # Close the WebDriver
        driver.quit()
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
            
    finally:
        # Close the WebDriver
        driver.quit()
        
def log_download_complete(search_key, file_path='downloaded_search_keys.json'):
    file_exists = os.path.isfile(file_path)
    
    if file_exists:
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        data = []

    data.append(search_key)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        