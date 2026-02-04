
import os

file_path = 'index.html'

with open(file_path, 'rb') as f:
    content = f.read()

# Check for BOM at start
if content.startswith(b'\xef\xbb\xbf'):
    print("Found BOM at start. Removing...")
    content = content[3:]
else:
    print("No BOM at start.")

# Check for other BOMs inside?
# The review said "stray BOM characters scattered".
# BOM in UTF-8 is \xef\xbb\xbf
count = content.count(b'\xef\xbb\xbf')
if count > 0:
    print(f"Found {count} other BOM sequences. Removing all...")
    content = content.replace(b'\xef\xbb\xbf', b'')

with open(file_path, 'wb') as f:
    f.write(content)

print("BOM cleanup complete.")
