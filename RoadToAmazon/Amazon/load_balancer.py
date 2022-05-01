from typing import List

class Solution:
    def get_minimum_difference(self, job: List[int], k: int) -> int:
        # horizontal_job = [0] * max(job)
        # max_job = max(job)
        # horizontal_job = [0 for i in range(max_job)]
        # job.sort()
        # temp = 0
        # for i, _ in enumerate(horizontal_job):
        #     for j in range(temp, len(job)):
        #         if job[j] > i:
        #             horizontal_job[i] = j
        #             temp = j
        #             k = k - j
        #             break
        #     if k < 0:
        #         return max_job - i
        #     elif k == 0:
        #         return max_job - i - 1
        # if k % len(job) == 0:
        #     return 0
        # return 1
        job.sort()
        max_job = max(job)
        temp = 0
        for i in range(max_job):
            for j in range(temp, len(job)):
                if job[j] > i:
                    temp = j
                    k = k - j
                    break
            if k < 0:
                return max_job - i
            if k == 0:
                return max_job - i - 1
        return 0 if k % len(job) == 0 else 1


if __name__ == '__main__':
    sol = Solution()
    job1 = [0, 0, 0, 0, 0]
