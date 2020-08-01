from typing import List

def hourglass_sum(matrix: List[List[int]]) -> int:
    largest_hourglass_sum = None
    hourglass_positions: List[list[int]] = [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1]]


    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            hourglass_sum = matrix[i][j]
            for position in hourglass_positions:
                if 0 <= i + position[0] < len(matrix) and 0 <= j + position[1] < len(row): 
                    hourglass_sum += matrix[i + position[0]][j + position[1]]
                else:
                    hourglass_sum = None
                    break
            if hourglass_sum is not None and (largest_hourglass_sum is None or largest_hourglass_sum < hourglass_sum):
                largest_hourglass_sum = hourglass_sum

    return largest_hourglass_sum



if __name__ == '__main__':
    sample_list = [
        [-1, -1, 0,-9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5],
    ]

    print(hourglass_sum(sample_list))