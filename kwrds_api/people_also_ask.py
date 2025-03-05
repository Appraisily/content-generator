import os
import json
import requests
from pathlib import Path

# API Configuration
API_KEY = "687f70ae-0590-4ede-8d4a-3d29e38b9e7b"
API_ENDPOINT = "https://paa.api.kwrds.ai/people-also-ask"

def fetch_paa_data(keyword, country="US", language="en"):
    """Fetch People Also Ask data from KWRDS API.
    
    Args:
        keyword (str): The keyword to search for
        country (str): The country code (e.g., US)
        language (str): The language code (e.g., en)
        
    Returns:
        dict: The API response data or None if the request failed
    """
    headers = {
        "X-API-KEY": API_KEY
    }
    
    params = {
        "keyword": keyword,
        "search_country": country,
        "search_language": language
    }
    
    try:
        response = requests.get(API_ENDPOINT, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching PAA data for keyword '{keyword}': {response.status_code}")
            print(response.text)
            
            # If the API key is invalid, create a mock response for demonstration purposes
            if response.status_code == 403 and "Invalid API key" in response.text:
                print("Creating mock PAA data for demonstration purposes...")
                return create_mock_paa_data(keyword)
            
            return None
    except Exception as e:
        print(f"Exception while fetching PAA data for keyword '{keyword}': {str(e)}")
        return None

def create_mock_paa_data(keyword):
    """Create mock PAA data for demonstration purposes.
    
    Args:
        keyword (str): The keyword
        
    Returns:
        dict: Mock PAA data
    """
    return {
        "results": [
            {
                "question": f"What is {keyword}?",
                "google_answer": f"This is a mock answer about {keyword}.",
                "google_answer_source_url": "https://example.com",
                "google_answer_source_title": "Example Source"
            },
            {
                "question": f"How to find {keyword} services?",
                "google_answer": f"You can find {keyword} services by searching online or asking for recommendations.",
                "google_answer_source_url": "https://example.com/services",
                "google_answer_source_title": "Finding Services"
            },
            {
                "question": f"How much does {keyword} cost?",
                "google_answer": f"The cost of {keyword} varies depending on various factors.",
                "google_answer_source_url": "https://example.com/cost",
                "google_answer_source_title": "Cost Information"
            }
        ],
        "mock_data": True
    }

def save_paa_data(keyword, data, base_folder="data"):
    """Save People Also Ask data to a JSON file in a folder named after the keyword.
    
    Args:
        keyword (str): The keyword
        data (dict): The API response data
        base_folder (str): The base folder to save the data in
        
    Returns:
        Path: The path to the saved file
    """
    # Create base folder if it doesn't exist
    base_path = Path(base_folder)
    base_path.mkdir(exist_ok=True)
    
    # Create folder for keyword (replace spaces with underscores for folder name)
    folder_name = keyword.replace(" ", "_")
    folder_path = base_path / folder_name
    folder_path.mkdir(exist_ok=True)
    
    # Save data to JSON file
    file_path = folder_path / "people_also_ask.json"
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    # Add a note if this is mock data
    if data.get("mock_data"):
        print(f"Mock PAA data for keyword '{keyword}' saved to {file_path}")
    else:
        print(f"PAA data for keyword '{keyword}' saved to {file_path}")
    
    return file_path 