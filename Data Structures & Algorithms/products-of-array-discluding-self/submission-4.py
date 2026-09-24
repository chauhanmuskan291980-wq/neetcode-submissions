class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zero_count = nums.count(0)

        output = [0] * len(nums)

        # More than one zero
        if zero_count > 1:
            return output

        # Exactly one zero
        if zero_count == 1:
            product = 1

            for num in nums:
                if num != 0:
                    product *= num

            for i in range(len(nums)):
                if nums[i] == 0:
                    output[i] = product

            return output

        # No zeros
        total_product = 1

        for num in nums:
            total_product *= num

        for i in range(len(nums)):
            output[i] = total_product // nums[i]

        return output