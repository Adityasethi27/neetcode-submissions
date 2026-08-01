class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1
        print(count)
        return sorted(count.keys(), key=lambda num: count[num],    reverse=True)[:k]


        