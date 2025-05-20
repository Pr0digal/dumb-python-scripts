import os
import random

# This is the folder where your other folders are located
# "." means the current folder where this script is running
path = os.path.abspath(".")

# A list of silly dad jokes to rename folders with
dad_jokes = [
    "folder? I hardly know her!",
    "I'm reading a book on anti-gravity. It's impossible to put down.",
    "I would avoid this folder... it’s too edgy.",
    "Why don’t scientists trust atoms? Because they make up everything.",
    "She looked surprised.",
    "Outstanding in its field—like a scarecrow.",
    "Renamed by my dad. Sorry.",
    "Don't trust stairs... they're always up to something.",
    "Not all heroes wear capes. Some write Python.",
    "Backup your backup of the backup."
]

# Get a list of all items in the folder
items = os.listdir(path)

# Filter only the folders
folders = []
for item in items:
    if os.path.isdir(os.path.join(path, item)):
        folders.append(item)

# Shuffle the dad jokes so each run is different
random.shuffle(dad_jokes)

# Rename each folder using a dad joke
for index, folder in enumerate(folders):
    # Get a joke (repeat from start if more folders than jokes)
    joke = dad_jokes[index % len(dad_jokes)]
    
    # Clean the joke to make it a valid folder name
    new_name = joke.replace(" ", "_").replace("?", "").replace(".", "")
    
    # Get full paths
    old_path = os.path.join(path, folder)
    new_path = os.path.join(path, new_name)

    try:
        # Rename the folder
        os.rename(old_path, new_path)
        print(f"Renamed '{folder}' → '{new_name}'")
    except Exception as error:
        print(f"Error renaming '{folder}': {error}")

print("\nAll folders have been given a dad joke. You're welcome.")
