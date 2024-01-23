from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Extract the date from the datetime object
current_date = current_datetime.date()

# Print the current date
print("Current Date:", type(current_date))
