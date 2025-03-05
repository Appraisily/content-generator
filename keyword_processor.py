import os
import json
import requests
from pathlib import Path

# API Configuration
API_KEY = "687f70ae-0590-4ede-8d4a-3d29e38b9e7b"
API_ENDPOINT = "https://keywordresearch.api.kwrds.ai/keywords-with-volumes"

def read_keywords_from_file(file_path):
    """Read keywords from a text file."""
    with open(file_path, 'r') as file:
        keywords = [line.strip() for line in file.readlines() if line.strip()]
    return keywords

def fetch_keyword_data(keyword, country="en-US"):
    """Fetch keyword data from KWRDS API."""
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
        print(f"Error fetching data for keyword '{keyword}': {response.status_code}")
        print(response.text)
        return None

def save_keyword_data(keyword, data):
    """Save keyword data to a JSON file in a folder named after the keyword."""
    # Create folder for keyword (replace spaces with underscores for folder name)
    folder_name = keyword.replace(" ", "_")
    folder_path = Path(folder_name)
    folder_path.mkdir(exist_ok=True)
    
    # Save data to JSON file
    file_path = folder_path / "keyword_data.json"
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Data for keyword '{keyword}' saved to {file_path}")

def create_readme(processed_keywords):
    """Create a README file with information about processed keywords."""
    readme_content = "# Keyword Processing Results\n\n"
    readme_content += "This file contains information about the keywords that have been processed.\n\n"
    readme_content += "## Processed Keywords\n\n"
    
    for keyword in processed_keywords:
        folder_name = keyword.replace(" ", "_")
        readme_content += f"- {keyword}: Data saved in `{folder_name}/keyword_data.json`\n"
    
    with open("README.md", 'w') as file:
        file.write(readme_content)
    
    print("README.md file created with information about processed keywords.")

def main():
    """Main function to process keywords."""
    keywords_file = "keyword_to_process.txt"
    processed_keywords = []
    
    # Read keywords from file
    keywords = read_keywords_from_file(keywords_file)
    print(f"Found {len(keywords)} keywords to process: {keywords}")
    
    # Process each keyword
    for keyword in keywords:
        print(f"Processing keyword: {keyword}")
        
        # Fetch data from KWRDS API
        keyword_data = fetch_keyword_data(keyword)
        
        if keyword_data:
            # Save data to file
            save_keyword_data(keyword, keyword_data)
            processed_keywords.append(keyword)
        else:
            print(f"Failed to process keyword: {keyword}")
    
    # Create README file
    create_readme(processed_keywords)

if __name__ == "__main__":
    main() 