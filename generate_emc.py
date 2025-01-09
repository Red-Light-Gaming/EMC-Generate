import json

# Input file containing the log
log_file = "Missing EMC.txt"  # Change this if the log file has a different name

# Default EMC value
default_emc_value = 128  # Change this to set a different default EMC value for items

# List to store items with their EMC values
emc_data = []

# Read and process the log file
with open(log_file, 'r') as file:
    for line in file:
        if "[Render thread/INFO]:" in line:
            start_index = line.index("[Render thread/INFO]:") + len("[Render thread/INFO]:")
            item_data = line[start_index:].strip()
            item_name = item_data.split(" ")[0].split("{")[0].split("[")[0].strip()
            if item_name:  # Ensure valid item name
                emc_data.append({
                    "item": item_name,
                    "emc": default_emc_value
                })

# Save to JSON file in the new format
with open("custom_emc_formatted.json", "w") as json_file:  # Change this if a different output file name is desired
    json.dump(emc_data, json_file, indent=4)

print("custom_emc_formatted.json file created successfully!")
