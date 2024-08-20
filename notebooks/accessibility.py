import pandas as pd
import requests
from collections import defaultdict
import json

def check_endpoint(url, api_endpoint=None, headers=None):
    print(f"Checking endpoint: {url}")
    try:
        # Step 1: Check if online
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"Endpoint is online: {response.status_code}")
        else:
            print(f"Failed to access endpoint: {response.status_code}")
            return False
        
        # Step 2: Check content type
        content_type = response.headers.get('Content-Type', '')
        if 'json' in content_type or 'xml' in content_type or 'csv' in content_type:
            print(f"Content type suggests machine-readable data: {content_type}")
        else:
            print(f"Content type may not be machine-readable: {content_type}")
        
        # Step 3: Check for API endpoint
        if api_endpoint:
            api_response = requests.get(f"{url}/{api_endpoint}", headers=headers)
            if api_response.status_code == 200:
                print(f"API endpoint is accessible: {api_response.status_code}")
            else:
                print(f"Failed to access API endpoint: {api_response.status_code}")
                return False
        
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error accessing portal: {e}")
        return False
    


