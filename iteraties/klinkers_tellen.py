# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/1095693228

def count_vowels(text):
    # Initialize a dictionary to store the counts of each vowel
    vowel_counts = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    
    # Iterate through each character in the text and check if it is a vowel
    for ch in text:
        ch = ch.upper()  # Convert the character to upper case to ignore case
        if ch in vowel_counts:
            vowel_counts[ch] += 1  # Increment the count for the vowel
    
    # Print the counts for each vowel
    for vowel, count in vowel_counts.items():
        print(f"{vowel}: {count}")

# Test the function with a sample text
text = input("Geef een text in: ")
count_vowels(text)
