import pandas as pd
import yaml

def load_and_standardize_data(file_path, config_mapping):
    """
    Standardize the dataframe columns using the {standard_name: user_name} mapping from YAML.
    """
    # 1. Load data based on the file extension
    if file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        df = pd.read_csv(file_path)
    
    # 2. Validate if the user-specified columns actually exist in the dataframe (typo prevention)
    for std_col, user_col in config_mapping.items():
        if user_col not in df.columns:
            raise ValueError(
                f"Error: The column '{user_col}' specified in the config was not found in the data. "
                f"(Please check the mapping for '{std_col}')"
            )

    # 3. Reverse the Key and Value for Pandas rename function (Dictionary Comprehension)
    # Resulting format: {'Origin': 'origin', 'Destin': 'destination', ...}
    rename_dict = {user_col: std_col for std_col, user_col in config_mapping.items()}
    
    # 4. Apply the column renaming
    df = df.rename(columns=rename_dict)
    
    return df

# === Execution Example ===
if __name__ == "__main__":
    # with open('config.yaml', 'r', encoding='utf-8') as f:
    #     config = yaml.safe_load(f)
    
    # user_od_df = load_and_standardize_data('user_od.xlsx', config['od_data']['column_name'])
    pass