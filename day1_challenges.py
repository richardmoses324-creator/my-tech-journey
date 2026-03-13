# Day 1 CHALLENGES - Richard's Tech Journey
# Type your answers below each challenge. Run the file after eachone!

print("=== CHALLENGE 1 ===")
name ="Richard"
print(name + " - I will own a company in 2026!")

# challenge 2: ask the user their age
age = int(input("How old are you?"))
if age > 16:
    print("You can learn cybersecurity!")
else:
    print("You're young enough to become the best hacker in Malawi!")    


print("\n=== Challenge 3 ===")
# Create list of strong password and print the second one

passwords = ["MalawiSecure2026!", "RichardCyberBoss!", "BlantyreHackProof123"]
print(passwords[1]) # means the second one (computer start  counting at 0)

print("\n===Challenge 5===")
# use for loop

for i in range (1, 6):
    print(str(i) + " Secure!")


print("\n===Challenge 5===")
#create a function

def generate_greeting(name):
    return "Welcome to Cybersecurity, " + name +  "!"
print(generate_greeting("Richard"))











