# TODO: Complete this solution / problem
from typing import List, Dict, Union

Line = Dict[str, List[int]]
Lines = List[Line]


def minimum_bribes(q: object):
    lines_to_work: Lines = format_input(q)
    for line in lines_to_work:
        print(determine_bribe_count(line))


def determine_bribe_count(line: Line) -> Union[int, str]:
    bribe_count = 0
    cuts_made: Dict[int, str] = {}
    start = line["start"]
    finish = line["finish"]
    for i, val in enumerate(finish):
        # if the positions in line don't match, lets check on the bribes
        if finish[i] != start[i]:
            # if finish is greater, that number made a cut
            if finish[i] > start[i]:
                if val - i - 1 > 2:
                    return "Too chaotic"
                bribe_count += finish[i] - start[i]

    return bribe_count




def format_input(raw_input: object) -> Lines:
    line_to_format: int = 1
    lines: Lines = []
    while len(lines) < raw_input[0]:  # type: ignore
        lines.append({
            "start": list(range(1, raw_input[line_to_format] + 1)),  # type: ignore
            "finish": raw_input[line_to_format + 1]  # type: ignore
        })
        line_to_format += 2
    
    return lines


if __name__ == '__main__':
    q = [
        2,
        5,
        [2, 1, 5, 3, 4],
        5,
        [2, 5, 1, 3, 4]
    ]

    minimum_bribes(q)

