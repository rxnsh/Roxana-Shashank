# check_allowed_files.py

import sys
import glob

# Get list of patterns to check from arguments
patterns_to_check = sys.argv[1:]

# Initialize a list to keep track of found files
found_files = []

# Loop over each pattern and check if files exist
for pattern in patterns_to_check:
    found_files.extend(glob.glob(pattern))

# If no files are found for a pattern, exit with an error
if not found_files:
    print("Error: No allowed files found in the repository.")
    sys.exit(1)
else:
    print(f"Allowed files found: {found_files}")
