import pandas as pd

def save_data(data, file_path):
    try:
        data.to_csv(file_path, index=False, encoding='utf-8')
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Failed to save data to {file_path}: {e}")

if __name__ == "__main__":
    data = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': ['A', 'B', 'C']
    })
    save_data(data, '../data/example_data.csv')
