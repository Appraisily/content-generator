import os
from pathlib import Path

def read_keywords_from_file(file_path):
    """Read keywords from a text file.
    
    Args:
        file_path (str): Path to the file containing keywords
        
    Returns:
        list: List of keywords
    """
    with open(file_path, 'r') as file:
        keywords = [line.strip() for line in file.readlines() if line.strip()]
    return keywords

def create_readme(processed_keywords, data_types, base_folder="data"):
    """Create a README file with information about processed keywords.
    
    Args:
        processed_keywords (list): List of processed keywords
        data_types (list): List of data types that were processed
        base_folder (str): Base folder where data is stored
    """
    readme_content = "# Keyword Processing Results\n\n"
    readme_content += "This file contains information about the keywords that have been processed.\n\n"
    readme_content += "## Processed Keywords\n\n"
    
    for keyword in processed_keywords:
        folder_name = keyword.replace(" ", "_")
        readme_content += f"### {keyword}\n\n"
        
        for data_type in data_types:
            file_name = f"{data_type}.json"
            file_path = Path(base_folder) / folder_name / file_name
            if file_path.exists():
                readme_content += f"- {data_type.replace('_', ' ').title()}: `{file_path}`\n"
        
        readme_content += "\n"
    
    with open(Path(base_folder) / "README.md", 'w') as file:
        file.write(readme_content)
    
    print(f"README.md file created in {base_folder} with information about processed keywords.") 