import logging, os
from fake_headers import Headers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

downloads_path = os.path.join(os.getcwd(), 'downloads')

def get_driver():
    headers = Headers()
    random_headers = headers.generate()
    ua = random_headers['User-Agent']
    logging.info(f"user-agent: {ua}")
    # Set up Chrome options to avoid detection
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Uncomment to run headless Chrome
    chrome_options.add_argument("--no-sandbox") # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage") # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu") # Applicable to Windows OS only
    chrome_options.add_argument("--disable-features=NetworkService") # Overcome limited resource problems
    chrome_options.add_argument("--disable-extension") # Disable extensions
    chrome_options.add_argument("--disable-features=NetworkService") # Overcome limited resource problems
    chrome_options.add_argument("--disable-features=VizDisplayCompositor") # Overcome limited resource problems
    chrome_options.add_argument("--disable-block-site-notifications") # Disable site notifications
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") # Disable automation control
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")# Disable automation control
    chrome_options.add_argument(f"user-agent={ua}") # Set a random user agent
    chrome_options.add_experimental_option('useAutomationExtension', False) # Disable automation extension
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": downloads_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # Initialize the WebDriver with options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver