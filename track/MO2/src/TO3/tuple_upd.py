# Read the course details
crs_name = input()
curr_wk = input()
crs_st = input()

# Create the original tuple
course_details = (crs_name, curr_wk, crs_st)

# Read the updated week
upd_wk = input()

# Create a new tuple using indexes from original tuple and assign back
course_details = (course_details[0], upd_wk, course_details[2])

# Display the updated tuple
print(course_details)