#Extract IDs

from collections import OrderedDict

# Initialize an ordered dictionary to store the extracted user IDs - if not, the ids will be shuffled while extracting
new_user_ids = OrderedDict()

# Open Grass-Reg-Full2.txt and read it line by line
print("Extracting user IDs from Grass-Reg-Full2.txt...")
with open("Grass-Reg-Full2.txt", "r") as input_file:
    for line in input_file:
        # Check if the line contains "User ID: "
        if "User ID: " in line:
            # Extract the user ID and append it to the ordered dictionary
            user_id = line.split("User ID: ")[1].split(",")[0].strip()
            new_user_ids[user_id] = None

print("Finished extracting user IDs.")

# Read existing user IDs from user_ids.txt
existing_user_ids = OrderedDict()
try:
    with open("user_ids.txt", "r") as user_ids_file:
        for user_id in user_ids_file:
            existing_user_ids[user_id.strip()] = None
except FileNotFoundError:
    print("user_ids.txt not found. Starting with an empty list of existing user IDs.")

# Combine existing user IDs with new user IDs and remove duplicates while maintaining order - cus some of you might run the code multiple times
all_user_ids = list(existing_user_ids.keys()) + list(new_user_ids.keys())
all_user_ids = list(OrderedDict.fromkeys(all_user_ids))

# Write the user IDs to the output file without overwriting
print("Writing user IDs to user_ids.txt...")
with open("user_ids.txt", "w") as output_file:
    # Write each user ID to a new line
    output_file.write("\n".join(all_user_ids))

print("Finished writing user IDs.")