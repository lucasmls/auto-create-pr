from datetime import datetime

# Get the current timestamp
current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Define the file path
file_path = 'timestamp.txt'

# Write the current timestamp to the file
with open(file_path, 'w') as file:
    file.write(f"Current Timestamp: {current_timestamp}\n")

print(f"Timestamp written to {file_path}")
