def lcs(a, b):
    matrix = [[0 for col in range(len(b)+1)] for row in range(len(a)+1)]

    for row, a_val in enumerate(a):
        for col, b_val in enumerate(b):
            if a_val == b_val:
                matrix[row+1][col+1] = matrix[row][col] +1
            else:
                matrix[row+1][col+1] = max(matrix[row+1][col], matrix[row][col+1])
             
    x = len(a)
    y = len(b)

    result = ''

    while x != 0 and y != 0:
        if matrix[x][y] == matrix[x-1][y]:
            x -= 1
        elif matrix[x][y] == matrix[x][-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            y -= 1
            x -= 1

    return result

def main():
    str1 = 'xyzabc'
    str2 = 'abc'
    ans = lcs(str1, str2)
    print(ans)

if __name__ == '__main__':
    main()
