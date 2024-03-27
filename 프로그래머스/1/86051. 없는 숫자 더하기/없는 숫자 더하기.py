def solution(numbers):
    nums = [0,1,2,3,4,5,6,7,8,9]
    for number in numbers:
        if number in nums:
            nums.remove(number)
    answer = sum(nums)
    return answer