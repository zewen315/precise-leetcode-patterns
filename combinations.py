from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = [[]]

    for n in nums:
        # res += [subset + [n] for subset in res]
        new_res = []
        for r in res:
            new_res.append(r + [n])
        res.extend(new_res)

    return res[1:]


def subsetsDuplicate(nums: List[int], k: int) -> List[List[int]]:
    res = [[]]

    for n in nums:
        new_res = []
        for r in res:
            for count in range(1, k + 1):
                new_res.append(r + [n] * count)
        res.extend(new_res)

    return res[1:]


def subsetsRecursive(nums: List[int]) -> List[List[int]]:
    res = []

    def helper(i, cur):
        if i == len(nums):
            if len(cur) > 0:
                res.append(cur)
            return

        helper(i + 1, cur + [nums[i]])  # include nums[i]
        helper(i + 1, cur)              # exclude nums[i]

    helper(0, [])
    return res


if __name__ == "__main__":
    nums = [1, 2, 3]

    print("Classic example of getting all subsets:")
    print(subsets(nums))
    print(subsetsRecursive(nums))

    print("Subsets with limit:")
    # Instead of choosing 0 or 1 of each number, you choose 0 to k copies of each number.
    print(subsetsDuplicate(nums, 2))