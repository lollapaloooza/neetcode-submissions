class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        for key, value in count.items():
            buckets[value].append(key)

        answer = []

        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            if(len(bucket) > 0):
                for num in bucket:
                    if(len(answer) >= k):
                        return answer
                    answer.append(num)
        
        return answer
