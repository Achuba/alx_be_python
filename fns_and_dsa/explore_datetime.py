import datetime
from datetime import timedelta

def display_current_datetime():
    current_datetime = datetime.datetime.now()
    formatted = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted)


def calculate_future_date(days):
    current_datetime = datetime.datetime.now()
    future_date = current_datetime + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

if __name__ == "__main__":
    display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)
    
    