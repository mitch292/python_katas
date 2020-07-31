def counting_valleys(n: int, s: str) -> int:
    elevation: int = 0
    valley_count: int = 0
    in_valley: bool = False

    for step in s:
        if step == "D":
            elevation -= 1
            if elevation < 0:
                if in_valley == False:
                    valley_count += 1
                    in_valley = True
        if step == "U":
            elevation += 1
            if elevation == 0:
                in_valley = False
    return valley_count




if __name__ == '__main__':
    n = 12

    s = "DDUUDDUDUUUD"

    print(counting_valleys(n, s))