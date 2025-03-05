# Content Generator

This application processes keywords from a text file, fetches data from the KWRDS API, and saves the results in a structured way. The data will later be used to generate Hugo markdown posts.

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Make sure you have the KWRDS API key (already included in the scripts).

## Usage

1. Add keywords to the `keyword_to_process.txt` file, one keyword per line.

2. Run the keyword processor script:
   ```
   python process_keywords.py
   ```

   Optional arguments:
   - `--keywords-file`: Path to the file containing keywords (default: keyword_to_process.txt)
   - `--output-folder`: Folder to save the data in (default: data)
   - `--country`: Country code for the API requests (default: US)
   - `--language`: Language code for the API requests (default: en)

3. The script will:
   - Read keywords from the file
   - Fetch data from the KWRDS API for each keyword (both keyword volume and People Also Ask data)
   - Save the results in a folder named after the keyword (with spaces replaced by underscores)
   - Create a README.md file with information about processed keywords

## Project Structure

- `process_keywords.py`: Main script for processing keywords
- `kwrds_api/`: Package containing KWRDS API functionality
  - `keyword_volume.py`: Module for fetching keyword volume data
  - `people_also_ask.py`: Module for fetching People Also Ask data
  - `utils.py`: Utility functions for file operations
- `keyword_to_process.txt`: File containing keywords to process
- `requirements.txt`: Python dependencies
- `data/`: Directory where processed data is stored
  - `README.md`: Auto-generated file with information about processed keywords
- `PROJECT_README.md`: This file, with instructions for humans

## API Endpoints

### Keyword Volume API
- Endpoint: `https://keywordresearch.api.kwrds.ai/keywords-with-volumes`
- Method: POST
- Returns keyword metrics including search volume, CPC, search intent, and competition level.

### People Also Ask API
- Endpoint: `https://paa.api.kwrds.ai/people-also-ask`
- Method: GET
- Returns a list of questions related to a keyword, along with metadata.

## Next Steps

The next phase will involve generating Hugo markdown posts based on the keyword data. 