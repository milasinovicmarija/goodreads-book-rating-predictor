import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.

    file_path (str): The file path to the CSV file containing the book ratings data based on my account.
    (This will not be shared due to privacy concerns. If anyone wishes to test the code, they should use their own data file path.)

    Returns:
    pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        raise