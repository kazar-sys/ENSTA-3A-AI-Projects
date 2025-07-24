grid = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4]
]

def allNumbersValidator(grid, index, case):
    number_to_appear = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if case == "line":
        for number in grid[index]:
            if number in number_to_appear:
                number_to_appear.remove(number)
        return len(number_to_appear) == 0
    elif case == "column":
        for j in range(9):
            if grid[j][index] in number_to_appear:
                number_to_appear.remove(grid[j][index])
        return len(number_to_appear) == 0
    else:
        for k in range(3):
            number_to_appear_bis = number_to_appear.copy()
            for i in range(3*k, 3*k+2):
                for j in range(3*k, 3*k+2):
                    if grid[i][j] in number_to_appear_bis:
                        number_to_appear_bis.remove(grid[i][j])
            if len(number_to_appear_bis) > 0:
                return False
        return True
            
    

def sumValidator(grid, case):

    if case == "line":
        target = sum(grid[0])
        for i in range(1, 9):
            if sum(grid[i]) != target:
                return False
    
    else:
        target = 0
        for j in range(9):
            target += grid[j][0]
        for i in range(1, 9):
            test = 0
            for j in range(9):
                test += grid[j][i]
            if test != target:
                return False
    return True

column_sum_test = sumValidator(grid, "column")
line_sum_test = sumValidator(grid, "line")
numbers_line = list()
for i in range(9):
    numbers_line.append(allNumbersValidator(grid, i, "line"))
numbers_line = all(numbers_line)
numbers_column = list()
for j in range(9):
    numbers_column.append(allNumbersValidator(grid, j, "column"))
numbers_column = all(numbers_column)
subgrid_test = allNumbersValidator(grid, 0, "sublist")
answer = column_sum_test and line_sum_test and numbers_column and numbers_line
print(str(answer).lower())

