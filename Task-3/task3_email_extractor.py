import re

# File names
input_file = "input.txt"
output_file = "extracted_emails.txt"

try:
    with open(input_file, 'r') as file:
        content = file.read()
        print("✅ input.txt found. Content loaded.")
except FileNotFoundError:
    print(f"❌ The file '{input_file}' was not found.")
    exit()

# Extract emails using regex
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
emails = sorted(set(emails))  # Remove duplicates & sort

if emails:
    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')
    print(f"✅ {len(emails)} email(s) extracted and saved to '{output_file}'")
    print("\n📧 Extracted Emails:")
    for e in emails:
        print("-", e)
else:
    print("⚠️ No emails found in the input file.")
