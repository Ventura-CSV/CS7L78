import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '10 15 25 30 35\n20'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert main.main.numbers[0] == 10
    assert main.main.numbers[1] == 15
    assert main.main.numbers[2] == 20
    assert main.main.numbers[3] == 25
    assert main.main.numbers[4] == 30
    assert main.main.numbers[5] == 35


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 2 3 4 5\n6'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert main.main.numbers[0] == 1
    assert main.main.numbers[1] == 2
    assert main.main.numbers[2] == 3
    assert main.main.numbers[3] == 4
    assert main.main.numbers[4] == 5
    assert main.main.numbers[5] == 6


def test_main_3():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 2 3 4 5\n0'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert main.main.numbers[0] == 0
    assert main.main.numbers[1] == 1
    assert main.main.numbers[2] == 2
    assert main.main.numbers[3] == 3
    assert main.main.numbers[4] == 4
    assert main.main.numbers[5] == 5


def test_main_4():
    # captureOut = io.StringIO()
    # sys.stdout = captureOut
    # # datastr = '90\n10\n50\n40\n30'
    # datastr = '1 2 3 4 5\n0'
    # sys.stdin = io.StringIO(datastr)

    # main.main()
    # sys.stdout = sys.__stdout__
    # print('Captured ', captureOut.getvalue())
    # lines = captureOut.getvalue().split('\n')
    # print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    # assert main.main.numbers[0] == 0
    # assert main.main.numbers[1] == 1
    # assert main.main.numbers[2] == 2
    # assert main.main.numbers[3] == 3
    # assert main.main.numbers[4] == 4
    # assert main.main.numbers[5] == 5
    detect = 0
    with open('main.py') as f:
        for line in f:
            if line.find('sort()') != -1:
                detect = 1
            if line.find('sorted') != -1:
                detect = 1
    assert detect == 0
