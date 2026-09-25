class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            st = i + 1
            end = len(nums) - 1

            while st < end:

                total = nums[i] + nums[st] + nums[end]

                if total == 0:
                    output.append([nums[i], nums[st], nums[end]])

                    st += 1
                    end -= 1

                    # Skip duplicate left values
                    while st < end and nums[st] == nums[st - 1]:
                        st += 1

                    # Skip duplicate right values
                    while st < end and nums[end] == nums[end + 1]:
                        end -= 1

                elif total < 0:
                    st += 1

                else:
                    end -= 1

        return output
                    
        