import requests
import pandas as pd
from bs4 import BeautifulSoup
import gzip

# Endpoint
base_url = "https://data-argo.ifremer.fr/"

# Table from endpoint html 
dfs = pd.read_html(base_url) 
df = dfs[0]

def collect_urls(base_url):
    urls = []
    
    # Send a GET request to the base URL
    try: 
        df = pd.read_html(base_url)[0]
        
        # Check if the request was successful (status code 200)
        data_urls = df['Name']
        
        # Iterate through the items in the response
        for name in df['Name']:
            print(name)
            # Check if the item is a folder
            if isinstance(name,str) and name.endswith('/'):
                # Recursively collect URLs from this folder
                folder_url = base_url + name
                urls.extend(collect_urls(folder_url))

            elif isinstance(name,str) and not name.endswith('Parent Directory'):
                # If the item is a file, add its URL to the list
                urls.append(base_url + name)
    
    
    except Exception as e:
        urls.append(e)
    
    url_df = pd.DataFrame({'URL': urls})
    url_df.to_csv(f'./data/URL_list_of_ARGO_ifremer', index=False)
    return urls

results = collect_urls(base_url)
print(len(results))

# file links
txt_file_urls = [base_url+name for name in df['Name'] if isinstance(name,str) and name.endswith('.txt')]
txtgz_file_urls = [base_url+name for name in df['Name'] if isinstance(name,str) and name.endswith('.txt.gz')]


# explore txt file
txt_url = txt_file_urls[0]
txt_df = pd.read_csv(txt_url) 
#print(txt_df.head())


# unpack & explore txt.gz file
url_gz = txtgz_file_urls[0]
#df_gz = pd.read_csv(url_gz, compression='gzip', header=None)
#print(df_gz)