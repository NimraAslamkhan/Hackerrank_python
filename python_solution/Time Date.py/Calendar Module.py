import datetime

# Read input
month, day, year = map(int, input().split())

# Create a date object
date_obj = datetime.date(year, month, day)

# List of days corresponding to weekday numbers
days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

# Get the day of the week as an integer (0 = Monday, 6 = Sunday)
day_of_week = date_obj.weekday()

# Output the day in capital letters
print(days[day_of_week])
