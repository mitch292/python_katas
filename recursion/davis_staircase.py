cache = {
    1: 1,
    2: 2,
    3: 4
}
def step_perms(n):
    if n == 0:
        return 0
    if n in cache.keys():
        return cache[n]
    else:
        cache[n] = step_perms(n - 1) + step_perms(n - 2) + step_perms(n - 3)
        return cache[n]


if __name__ == "__main__":
    print(step_perms(7))