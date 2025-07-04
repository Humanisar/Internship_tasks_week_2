birth_year=input("Enter your year of birth")
birth_year=int(birth_year)
current_year=2025
age=current_year-birth_year
print(f"You are(age)years old.")

if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")