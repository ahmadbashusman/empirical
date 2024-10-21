import json
import os

# Function to load JSON file
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Function to extract base scores (considering only CVSS V3 if present, else CVSS V2)
def extract_base_score(cve_data):
    cve_id = cve_data.get('cve', {}).get('CVE_data_meta', {}).get('ID')
    scores = []

    # Check if impact data is a dictionary
    impact_data = cve_data.get('impact', {})
    if isinstance(impact_data, dict):
        # Extract CVSS V3 base score
        cvss_v3 = impact_data.get('baseMetricV3', {}).get('cvssV3', {})
        if cvss_v3:
            base_score = cvss_v3.get('baseScore')
            if base_score is not None:
                scores.append(base_score)
        else:
            # Extract CVSS V2 base score if CVSS V3 is not present
            cvss_v2 = impact_data.get('baseMetricV2', {}).get('cvssV2', {})
            if cvss_v2:
                base_score = cvss_v2.get('baseScore')
                if base_score is not None:
                    scores.append(base_score)
    
    return cve_id, scores

# Path to dataset folder
dataset_folder = './dataset_w'

# Get list of JSON files in the dataset folder
json_files = [file for file in os.listdir(dataset_folder) if file.endswith('.json')]

# Dictionary to accumulate base scores
base_scores = {}

# Process each JSON file and accumulate base scores
for file_name in json_files:
    file_path = os.path.join(dataset_folder, file_name)
    cve_json = load_json_file(file_path)

    # Skip files that couldn't be loaded
    if cve_json is None:
        continue

    # Check if the impact field is a list and skip if so
    if isinstance(cve_json.get('impact'), list):
        #print(f"Skipping file {file_name} as its 'impact' field is a list")
        continue

    cve_id, scores = extract_base_score(cve_json)
    
    # Add the scores to the dictionary
    if cve_id and scores:
        base_scores[cve_id] = scores

# Print the CVE IDs with their base scores
print("CVE Base Scores:")
for cve_id, scores in base_scores.items():
    for score in scores:
        print(f"{cve_id}: {score}")
