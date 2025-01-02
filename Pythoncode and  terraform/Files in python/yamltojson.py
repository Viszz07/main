import yaml
import json

# Load the YAML file
with open('file.yaml', 'r') as yaml_file:
   yaml_content = yaml.safe_load(yaml_file)

# Convert YAML content to JSON
json_content = json.dumps(yaml_content, indent=4)

# Save the JSON content to a file
with open('file.json', 'w') as json_file:
    json_file.write(json_content)

print("YAML content has been converted to JSON and saved to 'file.json'")
