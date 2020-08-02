import math
from bisect import bisect_left, insort_left

def activity_notification(expenditure, d):
    n = len(expenditure)
    notification_count = 0
    sorted_expenditures = sorted(expenditure[:d])

    def determine_median():
        return sorted_expenditures[d//2] if d % 2 else ((sorted_expenditures[d//2-1] + sorted_expenditures[d//2]) / 2)

    for i in range(d, n):
        if i < d:
            continue
        median_spend = determine_median()
        if expenditure[i] >= determine_median() * 2:
            notification_count += 1
        del sorted_expenditures[bisect_left(sorted_expenditures, expenditure[i - d])]
        insort_left(sorted_expenditures, expenditure[i])
    return notification_count



if __name__ == '__main__':
    print(activity_notification([1, 2, 3, 4, 4], 4))