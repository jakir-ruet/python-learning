year = int(input('Enter year = '))


if (year % 400 == 0) and (year % 100 == 0) and (year % 4 == 0) or (year % 100 != 0):
    print('{0} is leap year'.format(year))
else:
    print('{0} is not a leap year'.format(year))
