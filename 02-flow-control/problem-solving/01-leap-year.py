year = int(input('Enter the year '))

# if year % 400 == 0 and year % 100 == 0:
#     print(year, 'is leap year')
#
# elif year % 4 == 0 and year % 100 != 0:
#     print(year, 'is leap year')
#
# else:
#     print(year, 'is not lear year')


def checking_year():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if checking_year():
    print(year, 'is leap year')
else:
    print(year, 'is not leap year')
