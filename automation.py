#move images in one folder to another folder
import os
import shutil

def move_images(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder, exist_ok=True)

    moved = False

    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith((".jpg", ".jpeg", ".png")):  # check for multiple formats
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)

            shutil.move(source_path, destination_path)
            print(f"Moved: {file_name}")
            moved = True

    if not moved:
        print("No .jpg/.jpeg/.png files found in the source folder.")
        
source = r"C:\Users\iprav\OneDrive\Pictures\Screenshots"
destination = r"C:\Users\iprav\OneDrive\Pictures\moved_images"

move_images(source, destination)

#extracting emails from the given data file
import os
import re

def extract_emails(input_file, output_file):
    with open(input_file, "r") as f:
        text = f.read()
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Regular expression to find email addresses
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)

    # Write emails to output file
    with open(output_file, "w") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"Extracted {len(emails)} emails and saved to {output_file}")

data=r"C:\Users\iprav\OneDrive\Pictures\data.txt"
emails=r"C:\Users\iprav\OneDrive\Pictures\emails.txt"
# Example usage
extract_emails(data, emails)
