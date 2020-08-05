from typing import Dict

# Complete the sockMerchant function below.
def sock_merchant(n: int, ar: list) -> int:
    count_of_pairs: int = 0
    socks: Dict[int, int] = {}

    for sock in ar:
        socks[sock] = socks.get(sock, 0) + 1

    for sock_type in socks.values():
        count_of_pairs += count_sock_type_pairs(sock_type)
    
    return count_of_pairs

def count_sock_type_pairs(socks_left: int, total_pairs: int = 0) -> int:
    if socks_left < 2:
        return total_pairs
    total_pairs += 1
    return count_sock_type_pairs(socks_left - 2, total_pairs)

if __name__ == '__main__':

    n = int(9)

    ar = list([10, 20, 20, 10, 10, 30, 50, 10, 20])

    result = sock_merchant(n, ar)

    print(result)