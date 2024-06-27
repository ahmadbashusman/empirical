import json
import os
from collections import Counter

# Function to load JSON file
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to extract impact metrics
def extract_impact_metrics(cve_data):
    impacts = []
    for item in cve_data.get('impact', {}).get('cvss', []):
        confidentiality_impact = item.get('confidentialityImpact')
        integrity_impact = item.get('integrityImpact')
        availability_impact = item.get('availabilityImpact')
        if confidentiality_impact or integrity_impact or availability_impact:
            impacts.append({
                "confidentialityImpact": confidentiality_impact,
                "integrityImpact": integrity_impact,
                "availabilityImpact": availability_impact
            })
    return impacts

# List of JSON files to read in the dataset folder
json_files = ['CVE-2023-1083.json', 'CVE-2023-47166.json']
dataset_folder = 'dataset'

# Initialize counters to accumulate impact counts
total_confidentiality_counter = Counter()
total_integrity_counter = Counter()
total_availability_counter = Counter()

# Process each JSON file and accumulate impact counts
for file_name in json_files:
    file_path = os.path.join(dataset_folder, file_name)
    cve_json = load_json_file(file_path)
    impact_metrics = extract_impact_metrics(cve_json)
    
    # Initialize counters for current file
    confidentiality_counter = Counter()
    integrity_counter = Counter()
    availability_counter = Counter()

    # Count impact metrics for current file
    for impact in impact_metrics:
        if impact['confidentialityImpact']:
            confidentiality_counter[impact['confidentialityImpact']] += 1
        if impact['integrityImpact']:
            integrity_counter[impact['integrityImpact']] += 1
        if impact['availabilityImpact']:
            availability_counter[impact['availabilityImpact']] += 1

    # Accumulate counts to total counters
    total_confidentiality_counter += confidentiality_counter
    total_integrity_counter += integrity_counter
    total_availability_counter += availability_counter

# Print the total frequency of each impact type
print("Total Confidentiality Impact Frequency:")
for impact, count in total_confidentiality_counter.items():
    print(f"{impact}: {count}")

print("\nTotal Integrity Impact Frequency:")
for impact, count in total_integrity_counter.items():
    print(f"{impact}: {count}")

print("\nTotal Availability Impact Frequency:")
for impact, count in total_availability_counter.items():
    print(f"{impact}: {count}")
