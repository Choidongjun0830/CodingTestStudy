def solution(nums):
    N = len(nums)
    pick = []
    nums.sort()
    for i in nums:
        if i not in pick:
            pick.append(i)
    if len(pick) >= N/2:
        return N/2
    return len(pick)