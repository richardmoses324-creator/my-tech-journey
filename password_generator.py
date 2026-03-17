# PASSWORD GENERATOR v2 - Richard's Cybersecurity Tool
# Now saves passwords to a file (secure local storage - Day 3 upgrade!)

import random
import string
from datetime import datetime

print("=== RICHARD'S STRONG PASSWORD GENERATOR v2 ===")
print("Now with secure file saving!\n")

length = int(input("How many characters? (12-16 recommended) "))

characters = string.ascii_letters + string.digits + string.punctuation

print("\nHere are 5 strong passwords:\n")
passwords = []
for i in range(5):
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Password {i+1}: {password}")
    passwords.append(password)

# NEW FEATURE: Save to file
filename = "my_secure_passwords.txt"
with open(filename, "a") as file:  # "a" = append (adds without deleting old ones)
    file.write(f"\n=== Passwords generated on {datetime.now().strftime('%Y-%m-%d %H:%M')} ===\n")
    for pwd in passwords:
        file.write(pwd + "\n")

print(f"\n✅ Saved to {filename} in your folder!")
print("Tip from future CEO: Never share this file. We'll add encryption next week!")
