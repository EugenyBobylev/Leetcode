from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        if i == len(nums) - 1:
            return []
        for j, m in enumerate(nums[i+1:]):
            if n + m == target:
                return [i, j+i+1]
    return []


if __name__ == '__main__':
    data_1 = [0,1,2,0,4,7,11,15]
    _target = 0
    res = twoSum(data_1, _target)
    print(res)
    