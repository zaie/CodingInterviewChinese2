# 双指针
# 头	     尾	  操作
# 奇数	偶数	符合题意，l++、r--
# 偶数	奇数	头、尾均不符合题意，交换头尾数值，l++、r--
# 奇数	奇数	尾不符合题意，l++
# 偶数	偶数	头不符合题意，r--

def reorder(nums, target_func):
    if not isinstance(nums, list) or len(nums) == 0:
        return

    for num in nums:
        if not isinstance(num, int):
            return

    left = 0
    right = len(nums) - 1
    while left < right:
        while left < right and not target_func(nums[left]):
            left += 1

        while left < right and target_func(nums[right]):
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]


def is_even(num):
    """
    单独抽出来为了可扩展
    """
    return (num & 1) == 0


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    reorder(nums=nums, target_func=is_even)
    print(nums)
