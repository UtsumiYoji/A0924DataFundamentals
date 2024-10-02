from math import log10

def main():
    while True:
        number = input('Type a number: ')
        if number.isdigit():
            number = int(number)
            if 0 < number:
                break
        print('Invalid input. Please type again.')
    digit = int(log10(number)//1+1)

    while True:
        n = input('Type a n: ')
        if n.isdigit():
            n = int(n)
            if 0 < n <= digit:
                break
        print('Invalid input. Please type again.')
    
    # Way to find 'n' nth number using with string
    print(f'The {n}th digit of {number} is {str(number)[digit-n]}')

    # way to find 'n' nth number using with math
    print(f'The {n}th digit of {number} is {number // 10**(n-1) % 10}')

if __name__ == "__main__":
    main()