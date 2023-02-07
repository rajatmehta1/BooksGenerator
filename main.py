# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import test.ReadFile

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    rf = open('./conf/python/python_interview_questions.txt','r')
    lines = rf.readlines()
    for line in lines:
        print(line)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
