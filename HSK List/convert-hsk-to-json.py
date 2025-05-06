import json

# Dictionary to hold all HSK words by level
hsk_data = {}

# Read each HSK level file and add to the dictionary
# Choose range(1,7) for hsk1-6, and range(1-8) for hsk1-9
for level in range(1, 7):
    filename = f"HSK{level}.txt"
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Read all lines, strip whitespace, and filter out empty lines
            words = [line.strip() for line in file if line.strip()]
            hsk_data[str(level)] = words
    except FileNotFoundError:
        print(f"Warning: File {filename} not found. Skipping...")

# Convert to JSON
json_output = json.dumps(hsk_data, ensure_ascii=False, indent=2)

# Save to file
with open('hsk_combined.json', 'w', encoding='utf-8') as outfile:
    outfile.write(json_output)

print("JSON file created successfully: hsk_combined.json")