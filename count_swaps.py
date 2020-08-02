from typing import List

def count_swaps(a):
    bubble_results = special_bubble_sort(a)
    print("Array is sorted in {} swaps.".format(bubble_results["swaps"]))
    print("First Element: {}".format(bubble_results["first_element"]))
    print("Last Element: {}".format(bubble_results["last_element"]))


def special_bubble_sort(arr):
    n = len(arr)
    count_of_swaps = 0

    for i in range(n - 1):

        for j in range(n-i-1):
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count_of_swaps += 1
    return {
        "first_element": arr[0],
        "last_element": arr[len(arr)-1],
        "swaps": count_of_swaps,
        "sorted_list": arr
    }




if __name__ == '__main__':

    count_swaps([1, 2, 3])
