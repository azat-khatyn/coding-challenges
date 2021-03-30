"""
example = [[1,4],[5,6]]
Output: [[1,4],[5,6]]

example = [[1,4],[0,4]]
Output = [[0,4]]
"""


def get_intervals(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda x: (x[0], x[1]))

    result = []
    current_interval = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= current_interval[1]:
            if intervals[i][1] > current_interval[1]:
                current_interval[1] = intervals[i][1]
        else:
            result.append(current_interval)
            current_interval = intervals[i]
    result.append(current_interval)
    return result




intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]

example = [[1,4],[5,6]]
# Output: [[1,4],[5,6]]

example2 = [[1,4],[0,4]]
# Output [[0,4]]

print(get_intervals(intervals))

# if len(intervals) == 2:
#     result.append(intervals[i])
#     result.append(intervals[i+1])
# elif len(result) == 0:
#     result.append(intervals[i])
# else:
#     result.append(intervals[i + 1])