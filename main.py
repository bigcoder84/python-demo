#!/usr/bin/env python3
# This is a sample Python script.

# Press Alt+Shift+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# press the green button in the gutter to run the script.
if __name__ == '__main__':
    value = input("input value:")
    if int(value) > 100:
        print("input value more than 100")
    elif int(value) > 10:
        print("input value more than 10")
    else:
        print(f"input value: {value}")


def hello():
    pass