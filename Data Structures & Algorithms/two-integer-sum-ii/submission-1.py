class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            complement = target - numbers[i]
            low = i+1
            high = n-1
            while low <= high:
                mid = (low+high)//2

                if numbers[mid] == complement:
                    return [i+1,mid+1]
                elif numbers[mid] < complement:
                    low = mid + 1
                else:
                    high = mid - 1