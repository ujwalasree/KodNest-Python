skills = []

# Read and store five skills
for i in range(5):
    skills.append(input())

# Convert the list into a tuple
skill_record = tuple(skills)

# Display required results using f-strings for exact formatting
print(f"Skill Record: {skill_record}")
print(f"First Three: {skill_record[:3]}")
print(f"Last Two: {skill_record[-2:]}")
print(f"Alternate Skills: {skill_record[::2]}")
print(f"Reversed Skills: {skill_record[::-1]}")