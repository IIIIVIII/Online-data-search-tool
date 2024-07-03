import requests
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_data_from_api(url, params=None):
    """
    Fetch data from an API and return it as a DataFrame.
    
    :param url: API endpoint URL
    :param params: Dictionary of query parameters
    :return: DataFrame containing the API data
    """
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()[1]  # Assuming the API returns JSON data and we're interested in the second element
        df = pd.DataFrame(data)
        logging.info(f"Successfully fetched data from API: {url}")
        return df
    except Exception as e:
        logging.error(f"Failed to fetch data from API: {url}: {e}")
        return None
