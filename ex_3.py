vowels = ["a","e","o","i","u"]
char = input("Enter a letter: ")
if char in vowels:
    print(f"{char} is vowel.")
elif char=="y":
    print(f"{char} is vowel and consonant.")
else:
    print(f"{char} is consonant.")
