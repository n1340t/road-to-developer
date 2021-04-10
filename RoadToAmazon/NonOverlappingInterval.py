# Leetcode 435
intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals.sort(key=lambda x:x[1])
minimum = intervals[0][1]

current_time = 0
non_overlap = 0
for x in intervals:
  if x[0] >= current_time:
    non_overlap += 1
    current_time = x[1]

print(len(intervals) - non_overlap)