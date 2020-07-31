import math

def repeated_string(s: str, n: int) -> int:
    if n < len(s): 
        return s[:n].count("a")

    count_in_s = s.count("a")

    return count_in_s * math.floor(n / len(s)) + s[:n % len(s)].count("a")


if __name__ == '__main__':

    print(repeated_string('a', 1000000000000))
