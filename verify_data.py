import pandas as pd
import json

def normalize_economic_data(data):
    """Normalize economic data by flattening the nested JSON structure."""
    normalized_data = []
    for _, item in data.iterrows():
        indicator = json.loads(item['indicator'].replace("'", "\""))
        country = json.loads(item['country'].replace("'", "\""))
        normalized_item = {
            'indicator_id': indicator.get('id'),
            'indicator_value': indicator.get('value'),
            'country_id': country.get('id'),
            'country_value': country.get('value'),
            'countryiso3code': item.get('countryiso3code'),
            'date': item.get('date'),
            'value': item.get('value'),
            'unit': item.get('unit'),
            'obs_status': item.get('obs_status'),
            'decimal': item.get('decimal')
        }
        normalized_data.append(normalized_item)
    return pd.DataFrame(normalized_data)

def main():
    try:
        economic_data = pd.read_csv('../data/economic_data_processed.csv')
        print("Economic Data Columns:\n", economic_data.columns)
        economic_data_df = normalize_economic_data(economic_data)
        print("Economic Data:\n", economic_data_df.head())
    except FileNotFoundError as e:
        print(f"Error: {e}. Please make sure the economic_data_processed.csv file exists in the data directory.")
    except pd.errors.EmptyDataError as e:
        print(f"Error: {e}. The file economic_data_processed.csv is empty or not properly formatted.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from economic_data_processed.csv: {e}")

    try:
        crop_yield_data = pd.read_csv('../data/crop_yield_data_processed.csv')
        print("Crop Yield Data Columns:\n", crop_yield_data.columns)
        print("Crop Yield Data:\n", crop_yield_data.head())
    except FileNotFoundError as e:
        print(f"Error: {e}. Please make sure the crop_yield_data_processed.csv file exists in the data directory.")
    except pd.errors.EmptyDataError as e:
        print(f"Error: {e}. The file crop_yield_data_processed.csv is empty or not properly formatted.")

if __name__ == "__main__":
    main()
