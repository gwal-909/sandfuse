def lcs(a, b):
    
    # create a two-dimensional array and populate with zeros. 
    # add 1 for both row and column, the two-dimensional array should have
    # the first row and first column will be padded with zeros 
    matrix = [[0 for col in range(len(b)+1)] for row in range(len(a)+1)]
    
    # nested for loop to iterate over columns for each row.
    for row, a_val in enumerate(a):
        for col, b_val in enumerate(b):
            if a_val == b_val:
                matrix[row+1][col+1] = matrix[row][col] + 1
            else:
                matrix[row+1][col+1] = max(matrix[row][col+1], matrix[row+1][col])

    x = len(a)
    y = len(b)

    result = ''

    # while loop to traverse the matrix and build the lcs result.
    while x != 0 and y != 0:
        if matrix[x][y] == matrix[x-1][y]:
            x -= 1
        elif matrix[x][y] == matrix[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result # place the matched indexed latter at front of string
            # traverse matrix diagonally up left
            x -= 1
            y -= 1 

    return result

def main():
    str1 = 'aqwdnfh awioawienfha;lohxfpaohnf'
    str2 = 'sacdf ;lif;ainsaswiuenfglzskunhcc'
    answer = lcs(str1, str2)
    print(answer)

if __name__ == '__main__':
    main()
