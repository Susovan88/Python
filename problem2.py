import os

# 🔧 Change this to the directory you want to explore
directory = r"C:\Users\susov\OneDrive\Desktop\YatraX\backend"

# Check if the path exists
if os.path.exists(directory):
    print(f"Listing contents of: {directory}\n")

    # List all items in the directory
    items = os.listdir(directory)

    for item in items:
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path):
            print(f"[FILE]   {item}")
        elif os.path.isdir(full_path):
            print(f"[FOLDER] {item}")
        else:
            print(f"[OTHER]  {item}")
else:
    print("The specified directory does not exist.")
