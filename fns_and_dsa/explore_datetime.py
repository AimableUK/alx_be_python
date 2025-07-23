from datetime import datetime, timedelta

current_date = datetime.now()


def display_current_datetime():
    print(f'Current Date: {current_date.strftime("%Y-%m-%d %H:%M:%S")}')


def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date:"))

    future_date = current_date + timedelta(days)
    print(future_date.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
