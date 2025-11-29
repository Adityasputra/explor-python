"""Display calendar for a specific month or entire year."""

import calendar


def display_monthly_calendar():
    """Display calendar for a specific month."""
    print("\n=== Monthly Calendar ===")
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    
    month_cal = calendar.month(year, month)
    print(month_cal)


def display_yearly_calendar():
    """Display calendar for an entire year."""
    print("\n=== Yearly Calendar ===")
    year = int(input("Enter year: "))
    
    # Parameters: year, w=2 (width), l=1 (lines), c=8 (spacing), m=3 (months per row)
    yearly_cal = calendar.calendar(year, w=2, l=1, c=8, m=3)
    print(yearly_cal)


def main():
    """Main function to run calendar display."""
    print("Calendar Display Program")
    print("1. Monthly Calendar")
    print("2. Yearly Calendar")
    
    choice = input("\nChoose an option (1 or 2): ")
    
    if choice == "1":
        display_monthly_calendar()
    elif choice == "2":
        display_yearly_calendar()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()