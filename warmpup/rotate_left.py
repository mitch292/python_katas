from typing import List

def rotate_left(a: List[int], d: int) -> List[int]:
    rotations = 0
    while rotations < d:
        temp = a.pop(0)
        a.append(temp)
        rotations += 1
    return a



if __name__ == '__main__':

    print(rotate_left([1, 2, 3, 4, 5], 4))