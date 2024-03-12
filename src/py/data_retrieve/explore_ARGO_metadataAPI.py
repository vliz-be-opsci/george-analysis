## python script to query json API of ARGO, containing Argo floats data and metadata
import requests
import pandas as pd

#functions
def fetch_json_data(url):
    """
    Fetch JSON data from the specified URL.

    Args:
        url (str): The URL of the JSON API.

    Returns:
        dict: JSON data.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    
    else:
        print(f"Error: Unable to fetch data from {url}")
        return None


def save_to_csv(data: dict, filename: str):
    """
    Save data to a CSV file.

    Args:
        data (list): List of dictionaries where each dictionary represents a row of data.
        filename (str): The name of the CSV file to save.
    """
    if not data:
        print("No data to save.")
        return

    # Extract field names from the first dictionary
    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)


# Define the API endpoint
argo_url = "https://sextant.ifremer.fr/examind/WS/sts/coriolis/v1.1"

response = fetch_json_data(argo_url)

for item in response['value']:
    try:
        name = list(item.values())[0]
        url = list(item.values())[-1]
        response = fetch_json_data(url)
        save_to_csv(response['value'][0], f'data/json_api_data/{name}.csv')
    except:
        pass
