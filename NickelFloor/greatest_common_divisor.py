def gcd(a, b):
    while b != 0:
        remainder = a % b # get the remainder of dividing both numbers.
        a = b             # make a (first number) equal to b (second number). 
        b = remainder     # make b equal to the remainder
    return a              # return a (was the first number)

def main():
    ans = gcd(5425, 145)
    print(ans)

if __name__ == '__main__':
    main()

