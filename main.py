import logging
import yaml
from data_fetcher_api import fetch_data_from_api
from data_fetcher_html import fetch_data_from_html

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        with open('../config/config.yaml', 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            logging.info("Config file loaded successfully")
    except Exception as e:
        logging.error(f"Failed to load config file: {e}")
        return
    
    try:
        logging.info("Fetching economic data")
        economic_data = fetch_data_from_api(config['economic_data_api']['url'], config['economic_data_api']['params'])
        if economic_data is not None:
            economic_data.to_csv('../data/economic_data_processed.csv', index=False, encoding='utf-8')
            logging.info("Economic data fetched and saved successfully")
        else:
            logging.error(f"Failed to fetch and save economic data: {config['economic_data_api']['url']}")
    except Exception as e:
        logging.error(f"Error in fetching economic data: {e}")
    
    try:
        logging.info("Fetching crop yield data")
        crop_yield_data = fetch_data_from_html(config['crop_yield_data_html']['url'])
        if crop_yield_data is not None:
            crop_yield_data.to_csv('../data/crop_yield_data_processed.csv', index=False, encoding='utf-8')
            logging.info("Crop yield data fetched and saved successfully")
        else:
            logging.error(f"Failed to fetch and save crop yield data: {config['crop_yield_data_html']['url']}")
    except Exception as e:
        logging.error(f"Error in fetching crop yield data: {e}")

if __name__ == "__main__":
    main()
