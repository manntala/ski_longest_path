
# for creating a matrix from a text file
file = open('map.txt', 'r')
read_file = file.readlines()
row_num, column_num = read_file[0].split()

matrix = [] 
for line in read_file[1:]:
    matrix.append(list(map(int, line.split())))

def skiing(x, y):
    row = len(matrix)
    column = len(matrix[x])
    # indexes of the directions up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    number_of_steps = 0
    longest_and_steeper_path = list()
    for i, j in directions:
        """
        three conditions are needed to be met
        i index should be less than row total index
        j index should be less than column total index
        new matrix[row][column] value should be less 
        than the matrix[row][column] previous value
        """
        if 0 <= x + i < row:
            if 0 <= y + j < column:
                if matrix[x+i][y+j] < matrix[x][y]:
                    # skiing function returns the longest path and the number of steps
                    initial_steps_num, initial_path = skiing(x+i, y+j)

                    if initial_steps_num > number_of_steps:
                        number_of_steps = initial_steps_num
                        longest_and_steeper_path = initial_path

    return number_of_steps + 1, [matrix[x][y]] + longest_and_steeper_path

answer = []
for x_val, row in enumerate(matrix):
    for y_val, num in enumerate(row):
        answer.append(skiing(x_val, y_val))
        
final_answer =max(answer)

final_steps = [] 
for num in final_answer[1]:
    final_steps.append(str(num))

print(f'The longest path takes {final_answer[0]} steps with {"-".join(final_steps)} as its decreasing steps.')
