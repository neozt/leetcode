def sliding_window(nums):
    left = right = 0
    zero_count = 0
    best = 0

    while right < len(nums):
        if nums[right] == 0:
            zero_count += 1

        while zero_count == 2:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        best = max(best, right - left + 1)
        right += 1

    return best

print(sliding_window([1,0,1,1,0]))