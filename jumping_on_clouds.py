from typing import List

def jumping_on_clouds(c: List[int]) -> int:
    jump_count: int = 0
    current_cloud: int = 0

    while current_cloud < len(c):
        if current_cloud + 2 < len(c) and c[current_cloud + 2] == 0:
            current_cloud += 2
        elif current_cloud + 1 < len(c) and c[current_cloud + 1] == 0:
            current_cloud += 1
        else:
            break
        jump_count += 1
    
    return jump_count




if __name__ == '__main__':

    c = [0, 0, 1, 0, 0, 1, 0]

    print(jumping_on_clouds(c))


