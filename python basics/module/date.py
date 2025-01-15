import datetime

# 1. Get Current Date and Time
current_datetime = datetime.datetime.now()
print(f"Current Date and Time: {current_datetime}")

# 2. Get Specific Information from Date (Year and Day of the Week)
year = current_datetime.year
day_of_week = current_datetime.strftime('%A')  # Full weekday name
print(f"Year: {year}")
print(f"Day of the Week: {day_of_week}")

# 3. Creating a Specific Date Object (Year, Month, Day)
specific_date = datetime.datetime(2020, 5, 17)
print(f"Specific Date: {specific_date}")

# 4. Formatting Date Using strftime() (Month Name)
formatted_month = specific_date.strftime("%B")
print(f"Month Name: {formatted_month}")

# 5. Working with Time and Time Zones (Creating a Date Object with Time)
specific_datetime = datetime.datetime(2025, 1, 15, 14, 30, 0)  # January 15, 2025, 14:30:00
print(f"Specific Date and Time: {specific_datetime}")

# 6. Formatting Date and Time (Using Multiple Format Codes)
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted Date and Time (YYYY-MM-DD HH:MM:SS): {formatted_datetime}")
