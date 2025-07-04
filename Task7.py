#Marks of 5 subjects
sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))
sub4 = int(input("Enter marks for Subject 4: "))
sub5 = int(input("Enter marks for Subject 5: "))

# Calculate
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total/ 5

#Result
print("Total Marks=",total)
print(f"Percentage=",percentage)

# Grades
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")