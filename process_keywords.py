#!/usr/bin/env python3
"""
Keyword Processor Script

This script processes keywords from a file, fetches data from the KWRDS API,
and saves the results in a structured way.
"""

import os
import argparse
from pathlib import Path
from kwrds_api import (
    fetch_keyword_volume_data, save_keyword_volume_data,
    fetch_paa_data, save_paa_data,
    read_keywords_from_file, create_readme
)

def process_keywords(keywords_file, output_folder="data", country="US", language="en"):
    """Process keywords from a file and fetch data from KWRDS API.
    
    Args:
        keywords_file (str): Path to the file containing keywords
        output_folder (str): Folder to save the data in
        country (str): Country code for the API requests
        language (str): Language code for the API requests
    """
    processed_keywords = []
    data_types = []
    
    # Read keywords from file
    keywords = read_keywords_from_file(keywords_file)
    print(f"Found {len(keywords)} keywords to process: {keywords}")
    
    # Process each keyword
    for keyword in keywords:
        print(f"\nProcessing keyword: {keyword}")
        keyword_processed = False
        
        # Fetch keyword volume data
        print("Fetching keyword volume data...")
        volume_data = fetch_keyword_volume_data(keyword, country=f"{language}-{country}")
        
        if volume_data:
            # Save volume data to file
            save_keyword_volume_data(keyword, volume_data, base_folder=output_folder)
            if "keyword_volume" not in data_types:
                data_types.append("keyword_volume")
            keyword_processed = True
        else:
            print(f"Failed to fetch volume data for keyword: {keyword}")
        
        # Fetch People Also Ask data
        print("Fetching People Also Ask data...")
        paa_data = fetch_paa_data(keyword, country=country, language=language)
        
        if paa_data:
            # Save PAA data to file
            save_paa_data(keyword, paa_data, base_folder=output_folder)
            if "people_also_ask" not in data_types:
                data_types.append("people_also_ask")
            keyword_processed = True
        else:
            print(f"Failed to fetch PAA data for keyword: {keyword}")
        
        if keyword_processed:
            processed_keywords.append(keyword)
    
    # Create README file
    if processed_keywords:
        create_readme(processed_keywords, data_types, base_folder=output_folder)
        print(f"\nProcessed {len(processed_keywords)} keywords successfully.")
    else:
        print("\nNo keywords were processed successfully.")

def main():
    """Main function to parse arguments and process keywords."""
    parser = argparse.ArgumentParser(description="Process keywords and fetch data from KWRDS API.")
    parser.add_argument("--keywords-file", default="keyword_to_process.txt",
                        help="Path to the file containing keywords (default: keyword_to_process.txt)")
    parser.add_argument("--output-folder", default="data",
                        help="Folder to save the data in (default: data)")
    parser.add_argument("--country", default="US",
                        help="Country code for the API requests (default: US)")
    parser.add_argument("--language", default="en",
                        help="Language code for the API requests (default: en)")
    
    args = parser.parse_args()
    
    process_keywords(args.keywords_file, args.output_folder, args.country, args.language)

if __name__ == "__main__":
    main() 