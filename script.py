import requests
import json

with open("config/openrouter_config.json") as f:
    config = json.load(f)

url = "https://openrouter.ai/api/v1/endpoint"
headers = {"Authorization": f"Bearer {config['api_key']}"}
payload = {"data": "test"}

print(f"Sending POST request to {url}")
print(f"Headers: {headers}")
print(f"Payload: {payload}")

response = requests.post(url, headers=headers, json=payload)

try:
    response.raise_for_status()  # Raise an error for bad status codes
    print("Connection successful!")
    print(f"Response status code: {response.status_code}")
    print(f"Response headers: {response.headers}")
    
    if 'application/json' in response.headers.get('Content-Type', ''):
        print(f"Response content (truncated): {response.json()[:200]}...")  # Print only the first 200 characters of JSON
    else:
        print("Unexpected content type. Response content (truncated):")
        print(response.text[:1000])  # Print the first 1000 characters of HTML
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
    print(f"Response status code: {response.status_code}")
    print(f"Response headers: {response.headers}")
    print(f"Response content (truncated): {response.text[:1000]}...")
except json.decoder.JSONDecodeError as json_err:
    print(f"JSON decode error: {json_err}")
    print(f"Response status code: {response.status_code}")
    print(f"Response headers: {response.headers}")
    print(f"Response content (truncated): {response.text[:1000]}...")