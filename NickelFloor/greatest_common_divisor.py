def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

def main():
    ans = gcd(105, 25)
    print(ans)

if __name__ == '__main__':
    main()

