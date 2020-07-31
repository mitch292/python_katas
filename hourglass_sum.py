from typing import List

def hourglass_sum(List[List[int]]) -> int:
    if n < len(s): 
        return s[:n].count("a")

    count_in_s = s.count("a")

    return count_in_s * math.floor(n / len(s)) + s[:n % len(s)].count("a")


if __name__ == '__main__':
    sample_list = [
        [1, 1, 1, 0, 0, 0]
        [0, 1, 0, 0, 0, 0]
        [1, 1, 1, 0, 0, 0]
        [0, 0, 2, 4, 4, 0]
        [0, 0, 0, 2, 0, 0]
        [0, 0, 1, 2, 4, 0]
    ]
    print(hourglass_sum(sample_list)