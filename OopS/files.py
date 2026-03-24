#1
with open("sample.txt", "r") as f:
    lines = f.readlines()

with open("sample.txt", "w") as f:
    for line in lines:
        if line.strip():         
            f.write(line)


print("Blank lines removed successfully!")

#2
with open("file1.txt", "r") as f1:
    data1 = f1.read()

with open("file2.txt", "r") as f2:
    data2 = f2.read()

with open("merged.txt", "w") as f:
    f.write(data1)
    f.write("\n")      
    f.write(data2)

print("Files merged successfully into merged.txt!")

#3
# Read words from file
with open("sample.txt", "r") as f:
    words = f.read().split()   

# Sort alphabetically (case-insensitive)
words.sort(key=str.lower)

# Write sorted words back to file
with open("sample.txt", "w") as f:
    for w in words:
        f.write(w + "\n")

print("Words sorted alphabetically!")

#4
import re
with open("data.txt", "r") as f:
    text = f.read()

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Find all emails
emails = re.findall(pattern, text)

print("Extracted Emails:")
for email in emails:
    print(email)

#5
from collections import Counter
import re

with open("sample.txt", "r") as f:
    text = f.read().lower()     # convert to lowercase for uniformity

words = re.findall(r"\b[a-zA-Z]+\b", text)

count = Counter(words)

word, freq = count.most_common(1)[0]

print(f"Most frequent word: '{word}' (appears {freq} times)")





