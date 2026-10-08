"""
RECORD CHECK  -  my version
===========================

Name  :  Manuel Cerqueira Cajrabille do Carmo Paquete
Lane  :  IT
Date  :  8/10/2026 (DD/MM/YY)

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"{'Value:':<18}{value:>10.2f}")
    print(f"{'Limit:':<18}{limit:>10.2f}")
    print(f"{'Difference:':<18}{difference:>10.2f}")
    print(f"{'Percentage:':<18}{percent:>9.2f}%")
    print(f"{'Status:':<18}{status:>10}")
    print("=" * 34)

while True:
    label = input("Enter a name, hostname or IP (or 'quit' to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter the value used: "))
    limit = float(input("Enter the total limit: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)