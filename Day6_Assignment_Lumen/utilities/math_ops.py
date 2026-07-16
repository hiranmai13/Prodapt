def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    nums = sorted(numbers)
    n = len(nums)

    if n%2==0:
        return (nums[n//2 - 1] + nums[n//2]) / 2
    return nums[n//2]