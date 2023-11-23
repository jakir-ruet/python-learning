# its introduce from python 3.10 version
def weekendFinder(n):
    match n:
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
            return "Invalid Number"
    print(weekendFinder(3))
