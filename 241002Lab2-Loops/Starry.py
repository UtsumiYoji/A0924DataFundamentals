def main():
    while True:
        lines = input('How many lines do you want to print? :')
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines:
                break
        print('Invalid input. Please type again.')

    # part1
    for i in range(lines):
        for _ in range(lines-1-i):
            print(' ', end='')
        for _ in range(1+2*i):
            print('*', end='')
        print()
    
    # part2
    print()
    for i in range(lines):
        for _ in range(lines-i):
            print('*', end='')
        print()

    # part3 
    print()
    for i in range(lines):
        if lines//2 > i:
            for _ in range(i+1):
                print('*', end='')
        else:
            for _ in range(lines-i):
                print('*', end='')
        print()

    # part4
    print()
    for i in range(lines):
        if lines//2 > i:
            for _ in range(i):
                print(' ', end='')
            for _ in range(lines-i*2):
                print('*', end='')
        else:
            for _ in range(lines-i-1):
                print(' ', end='')
            for _ in range(i*2-lines+2):
                print('*', end='')
        print()

    # part5
    print()
    for i in range(lines):
        if lines//2 > i:
            for _ in range(lines//2-i):
                print(' ', end='')
            for _ in range(1+2*i):
                print('*', end='')
        else:
            for _ in range(i-lines//2):
                print(' ', end='')
            for _ in range(1+2*(lines-i-1)):
                print('*', end='')
        print()

if __name__ == "__main__":
    main()