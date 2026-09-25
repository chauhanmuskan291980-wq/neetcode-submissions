class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1,len(nums)):
                complement = -(nums[i]+nums[j])

                if complement in seen:
                    triplet = tuple(sorted([nums[i],nums[j],complement]))
                    output.add(triplet)
                seen.add(nums[j])
        return [list(triplet) for triplet in output]
        