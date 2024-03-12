import requests

# Define the API endpoint
url = "https://data-argo.ifremer.fr/"

# Make the GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.text)
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)