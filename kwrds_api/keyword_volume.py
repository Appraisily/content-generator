import os
import json
import requests
from pathlib import Path

# API Configuration
API_KEY = "687f70ae-0590-4ede-8d4a-3d29e38b9e7b"
API_ENDPOINT = "https://keywordresearch.api.kwrds.ai/keywords-with-volumes"

def fetch_keyword_volume_data(keyword, country="en-US"):
    """Fetch keyword volume data from KWRDS API."""
    headers = {
        "X-API-KEY": API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "search_question": keyword,
        "search_country": country
    }
    
    response = requests.post(API_ENDPOINT, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching volume data for keyword '{keyword}': {response.status_code}")
        print(response.text)
        return None

def save_keyword_volume_data(keyword, data, base_folder="data"):
    """Save keyword volume data to a JSON file in a folder named after the keyword."""
    # Create base folder if it doesn't exist
    base_path = Path(base_folder)
    base_path.mkdir(exist_ok=True)
    
    # Create folder for keyword (replace spaces with underscores for folder name)
    folder_name = keyword.replace(" ", "_")
    folder_path = base_path / folder_name
    folder_path.mkdir(exist_ok=True)
    
    # Save data to JSON file
    file_path = folder_path / "keyword_volume.json"
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Volume data for keyword '{keyword}' saved to {file_path}")
    
    return file_path 