marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 90:
    print("Grade: A")
    print("Result: Pass")

elif marks >= 75:
    print("Grade: B")
    print("Result: Pass")

elif marks >= 50:
    print("Grade: C")
    print("Result: Pass")

else:
    print("Grade: Fail")
    print("Result: Fail")