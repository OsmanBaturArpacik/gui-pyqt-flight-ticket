# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#
hafta = 9
soru_sayisi = 6

import os
os.makedirs(f"haftalar/hafta{hafta}", exist_ok=True)

for i in range(1, soru_sayisi+1):
    with open(f"haftalar/hafta{hafta}/soru{hafta}_{i}.py", "a") as f:
        f.write("if __name__ == '__main__':\n\tpass\n")
