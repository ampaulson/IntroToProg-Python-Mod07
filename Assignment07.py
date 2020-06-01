# ------------------------------------ #
# Title: Assignment07 - Bug Explorer
# Description: Demo of error handling and pickling
# ChangeLog: (Who, When, What)
# APaulson, 3/30/2020, Created Script
# APaulson, 3/30/2020, Added file inputs
# APaulson, 3/30/2020, Changed file name to bugList
# ------------------------------------ #

# -- Data -- #
import pickle
import sys

bugList = ['spider', 'mosquito']  # inputs for list file


# -- Processing -- #
def write_to_file(listToWrite):
    with open('bugList.pkl', 'wb') as bugpickle:
        print(listToWrite)
        pickle.dump(listToWrite, bugpickle)


def read_file():
    with open('bugList.pkl', 'rb') as bugpickle:
        readOut = pickle.load(bugpickle)
        print(readOut)
        return readOut


def get_user_input():
    bugItem = input('Enter a type of bug: ')
    if len(bugItem) == 0:
        raise ValueError('Error: You didn\'t input anything')  # first error
    return bugItem


# -- Main Script -- #
try:
    fileData = read_file()
except FileNotFoundError as e:  # second error
    print('\nWelcome to the bug explorer. \n'
          'There is no data to read to you yet -\n')
    fileData = bugList
except pickle.UnpicklingError as e:  # third error
    print('There were invalid edits to the bugList.pkl file.')
    sys.exit(1)

try:
    fileData.append(get_user_input())
    write_to_file(fileData)
except ValueError as e:
    print(e)
