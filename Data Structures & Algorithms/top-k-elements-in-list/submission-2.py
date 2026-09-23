class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqOfNum = {}

        for i in nums:
            if i in freqOfNum:
                freqOfNum[i] += 1
            else:
                freqOfNum[i] = 1
        
        freqOfTheNumbers =  list(freqOfNum.items())
        top_frequent = heapq.nlargest(
    k,
    freqOfTheNumbers,
    key=lambda x:x[1]
)
        return [item[0] for item in top_frequent]