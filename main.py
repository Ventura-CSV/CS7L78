def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """


def insertOne(numbers):
    """
    ########################################
    Code Your Program here
    Do not use 'sort' keyword
    ########################################
    """
    userval = int(input('Enter the insertion value: '))


def main():
    numbers = getInput()    # test input: 10 15 25 30 35
    insertOne(numbers)      # test input 20
    print(numbers)         # list value after insertion


if __name__ == '__main__':
    main()
