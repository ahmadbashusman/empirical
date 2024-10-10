import json
from collections import Counter
import os

# Function to load JSON file
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Function to extract CWE identifiers
def extract_cwes(cve_data):
    cwes = []

    # Check if problemtype data is present
    problemtype_data = cve_data.get('cve', {}).get('problemtype', {}).get('problemtype_data', [])
    print(problemtype_data)
    for problemtype in problemtype_data:
        descriptions = problemtype.get('description', [])
        for description in descriptions:
            cwe = description.get('value')
            if cwe:
                cwes.append(cwe)
    
    return cwes

# Path to dataset folder
dataset_folder = './dataset_sw'

# Get list of JSON files in the dataset folder
json_files = [file for file in os.listdir(dataset_folder) if file.endswith('.json')]

# Initialize counter to accumulate CWE counts
total_cwe_counter = Counter()


# Process each JSON file and accumulate CWE counts
for file_name in json_files:
    file_path = os.path.join(dataset_folder, file_name)
    cve_json = load_json_file(file_path)
    # Initialize counter for current file
    cwe_counter = Counter()
    # Skip files that couldn't be loaded
    if cve_json is None:
        print("None here")
        cwe_counter["None"] += 1
        # Accumulate counts to total counter
        total_cwe_counter += cwe_counter
        continue

    cwes = extract_cwes(cve_json)
    print(file_name,len(cwes))
    # Count CWE identifiers for current file
    for cwe in cwes:
        print(file_name, cwe)
        cwe_counter[cwe] += 1

        # Accumulate counts to total counter
    total_cwe_counter += cwe_counter

# Print the total frequency of each CWE identifier sorted by frequency
print("Total CWE Frequency:")
for cwe, count in total_cwe_counter.most_common():
    print(f"{cwe}: {count}")
print("Total CVE analyz: ",len(json_files))

#$print("Accumulated ", total_cwe_counter )