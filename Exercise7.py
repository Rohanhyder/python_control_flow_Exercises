
# Get the user numeric_score.

numeric_score = int(input("Enter your score "))

# check the grade is either (A,B,C,D or F).

if numeric_score >= 80:
    print("Grade A")
elif numeric_score >= 70:
    print("Grade B")
elif numeric_score >= 60:
    print("Grade C")
elif numeric_score >= 50:
    print("Grade D")
else:
     print("Grade F")