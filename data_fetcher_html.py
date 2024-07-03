from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_data_from_html(url):
    """
    Fetch data from an HTML page and return it as a DataFrame.
    
    :param url: URL of the web page to fetch data from
    :return: DataFrame containing the HTML table data
    """
    try:
        # Set up Selenium and ChromeDriver
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # Run in headless mode (commented out to run in normal mode)
        service = Service('/Users/mingfanxie/Desktop/data ass/chromedriver')  # Update this with the path to your chromedriver
        driver = webdriver.Chrome(service=service, options=options)
        
        driver.get(url)
        logging.info("Successfully opened the web page with Selenium")
        
        # Increase wait time and wait for a specific element to be present
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
        
        # Get page source after JavaScript has executed
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Output full page source for debugging
        logging.info("Full page source: " + driver.page_source[:1000])  # Only print first 1000 characters to avoid large output
        
        driver.quit()  # Close the browser
        
        table = soup.find('table')
        if not table:
            logging.error("No table found in HTML content")
            return None
        
        rows = table.find_all('tr')
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append(cols)
        
        df = pd.DataFrame(data)
        logging.info(f"Successfully fetched data from HTML: {url}")
        
        logging.info("Fetched data: " + df.head().to_string())
        return df
    except Exception as e:
        logging.error(f"Failed to fetch data from HTML: {url}: {e}")
        return None
