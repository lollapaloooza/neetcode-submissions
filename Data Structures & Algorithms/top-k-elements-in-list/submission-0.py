class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        answer = []

        for num in nums:
            count[num] += 1

        for key, value in count.items():
            buckets[value].append(key)

        for i in range(len(buckets) - 1, -1, -1):
            if(len(buckets[i]) > 0):
                for num in buckets[i]:
                    if(len(answer) >= k):
                        return answer
                    answer.append(num)

        return answer
        