def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = search(nums, target)
    print(f"search({nums}, {target}) = {result}")
