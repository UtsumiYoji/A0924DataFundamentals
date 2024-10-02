def main():
    LINES = 7
    
    # part1
    for i in range(LINES):
        print(' ' * (LINES-i-1) + '*' * (2*i+1))
    print('\n')

    # part2
    for i in range(LINES):
        print('*' * (LINES-i))
    print('\n')

    # part3
    for i in range(LINES):
        if i < LINES//2:
            print('*' * (i+1))
        else:
            print('*' * (LINES-i))
    print('\n')

    # part4
    for i in range(LINES):
        if i < LINES//2:
            print(' ' * i + '*' * (LINES-i*2))
        else:
            print(' ' * (LINES-i-1) + '*' * (i*2-LINES+2))
    print('\n')

    # part5
    for i in range(LINES):
        if i < LINES//2:
            print(' ' * (3-i) + '*' * (2*i+1))
        else:
            print(' ' * (i-3) + '*' * (2*(LINES-i)-1))


if __name__ == "__main__":
    main()