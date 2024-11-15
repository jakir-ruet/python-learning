marks = 90

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C")


# nested conditional statement
age = 20
isStudent = True

if age >= 18:
    if isStudent:
        print("discount applied")
    else:
        print("discount not applied")
else:
    print("not adult")