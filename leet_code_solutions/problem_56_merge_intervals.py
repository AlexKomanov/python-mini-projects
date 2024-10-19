from typing import List

# https://leetcode.com/problems/merge-intervals/description/

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    # intervals.sort(key=lambda pair: pair[0])
    intervals.sort()
    output = [intervals[0]]

    for idx in range(1, len(intervals)):
        start, end = intervals[idx]
        last_interval = output[-1]
        last_end = last_interval[1]

        if start > last_end:
            output.append(intervals[idx])
        else:
            last_interval[1] = max(last_end, end)

    return output

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
print(merge_intervals([[1,4],[4,5]]))
