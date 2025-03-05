# Content Generator - AI Development Guide

## Project Overview
This project is a content generation pipeline that processes keywords and generates Hugo markdown posts. The current implementation focuses on fetching data from the KWRDS API.

## Current Implementation
- `process_keywords.py`: Main script that reads keywords from a file, fetches data from the KWRDS API, and saves the results in JSON format.
- `kwrds_api/`: Package containing KWRDS API functionality:
  - `keyword_volume.py`: Module for fetching keyword volume data
  - `people_also_ask.py`: Module for fetching People Also Ask data
  - `utils.py`: Utility functions for file operations
- The script creates a folder for each keyword (replacing spaces with underscores) and saves the API responses in JSON files within that folder.
- A README.md file is generated with information about processed keywords.

## API Details

### Keyword Volume API
- Endpoint: https://keywordresearch.api.kwrds.ai/keywords-with-volumes
- Method: POST
- API Key: 687f70ae-0590-4ede-8d4a-3d29e38b9e7b
- The API returns keyword metrics including search volume, CPC, search intent, and competition level.

#### Response Structure
The Keyword Volume API response includes:
- keyword: Object with indices as keys and keyword strings as values
- volume: Object with indices as keys and search volumes as values
- cpc: Object with indices as keys and cost-per-click values as values
- avg_monthly_searches: Object with indices as keys and monthly search volumes as values
- search-intent: Object with indices as keys and search intent categories as values
- competition_value: Object with indices as keys and competition levels as values

### People Also Ask API
- Endpoint: https://paa.api.kwrds.ai/people-also-ask
- Method: GET
- API Key: 687f70ae-0590-4ede-8d4a-3d29e38b9e7b
- The API returns a list of questions related to a keyword, along with metadata.

#### Response Structure
The People Also Ask API response includes:
- results: An array of questions related to the keyword.
  - Each item contains:
    - question: The question that users commonly ask.
    - google_answer (optional): The answer provided by Google, if available.
    - google_answer_source_url (optional): The source URL for the Google answer, if available.
    - google_answer_source_title (optional): The title of the source for the Google answer, if available.
- paa_search_count (optional): The usage count for the PAA search.

## Future Development
1. **Content Generation**:
   - Create a script to generate Hugo markdown posts based on the keyword data
   - Implement templates for different types of content
   - Use the keyword metrics to optimize the content for SEO

2. **Potential Enhancements**:
   - Add support for batch processing multiple keywords
   - Implement error handling and retries for API requests
   - Add logging for better debugging
   - Create a configuration file for customizable settings

## Notes for Implementation
- The avg_monthly_searches and competition_value fields might be undefined in case of Google downtime, so the content generation script should handle this gracefully.
- The content generation should focus on creating high-quality, SEO-optimized content based on the keyword metrics.
- The Hugo markdown files should follow the standard Hugo frontmatter format. 