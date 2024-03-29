#!/usr/bin/env python3

from datetime import date, datetime, timedelta

def get_invoice_date():
    while True:
        try:
            invoice_date_str = input("Enter the invoice date (MM/DD/YY): ")    
            invoice_datetime = datetime.strptime(invoice_date_str, "%m/%d/%y")
            invoice_date = date(invoice_datetime.year, invoice_datetime.month, invoice_datetime.day)

            if invoice_date > date.today():
                print("test")
                raise OSError("Date must be today or in the past.")
            
            break

        except OSError as e:
            print(e)
        except:
            print("Date must be in format MM/DD/YY")

    return invoice_date

def main():
    print("The Invoice Due Date program")
    print()

    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today()
        days_overdue = current_date.day - due_date.day

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")      

if __name__ == "__main__":
    main()
