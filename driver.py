import logging, os
from fake_useragent import UserAgent
from fake_headers import Headers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



def get_driver():
    downloads_path = os.path.join(os.getcwd(), 'downloads')
    headers = Headers(browser="chrome")
    random_headers = headers.generate()
    ua = random_headers['User-Agent']
    logging.info(f"user-agent: {ua}")  

    # Set up Chrome options to avoid detection
    chrome_options = Options()
    
    # chrome_options.add_argument("--headless")  # Uncomment to run headless Chrome
    chrome_options.add_argument("--no-sandbox") # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage") # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu") # Applicable to Windows OS only
    chrome_options.add_argument("--disable-features=NetworkService") # Overcome limited resource problems
    chrome_options.add_argument("--disable-extension") # Disable extensions
    chrome_options.add_argument("--disable-features=NetworkService") # Overcome limited resource problems
    chrome_options.add_argument("--disable-features=VizDisplayCompositor") # Overcome limited resource problems
    chrome_options.add_argument("--disable-block-site-notifications") # Disable site notifications
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") # Disable automation control
    chrome_options.add_argument(f"user-agent={ua}") # Set a random user agent
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": downloads_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    chrome_options.add_experimental_option('useAutomationExtension', False) # Disable automation extension
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) # Exclude enable-automation switch
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    # Initialize the WebDriver with options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.delete_all_cookies()
    driver.maximize_window()

    stealth(driver,
       user_agent = ua,
       languages=["en-US", "en"],
       vendor="Google Inc.",
       platform="Win32",
       webgl_vendor="Intel Inc.",
       renderer="Intel Iris OpenGL Engine",
       fix_hairline=True,
       Host="cdxapps.epa.gov",
       Referer="https://cdxapps.epa.gov/cdx-enepa-II/public/action/eis/search/search"
       )
    
    return driver