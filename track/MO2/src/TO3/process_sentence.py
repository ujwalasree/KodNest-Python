sentence = input()

# Process the sentence according to the required steps
cleaned = sentence.strip()
normalized = cleaned.lower().replace(".", "")
words = normalized.split()
slug = "-".join(words)
uppercase = normalized.upper()
python_pos = normalized.find("python")

# Display the required output formats
print(f"Cleaned: {cleaned}")
print(f"Normalized: {normalized}")
print(f"Words: {words}")
print(f"Slug: {slug}")
print(f"Uppercase: {uppercase}")
print(f"Python Position: {python_pos}")