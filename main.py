##################################################
# Comlete your code here
##################################################

# numbers = list(map(int, input().split()))

def main():

    ######################################################
    # Use this variable for the result
    ######################################################
    main.numbers = input().split()
    for i in range(len(main.numbers)):
        main.numbers[i] = int(main.numbers[i])
    print(main.numbers)

    ######################################################
    # Code your program here

    print("After insertion\n", main.numbers)


if __name__ == '__main__':
    main()
