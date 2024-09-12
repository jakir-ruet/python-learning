# its introduce from python 3.10 version
def weekendFinder(user_activity):
    match user_activity:
        case 0:
            return "Saturday"
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case _:
            return "Invalid activity"


print(weekendFinder(0))
print(weekendFinder(3))
print(weekendFinder(7))
