# using a dictionary structure
def containsDuplicate(nums) -> bool:
    myDict = {}

    for item in nums:
        if item in myDict:
            return True
        else:
            myDict[item] = True         # this could be True, or 1, or any value

    return False


# alternate version, using a set:
def containsDuplicate2(nums) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == '__main__':
    print([1,3,1,4], containsDuplicate([1,3,1,4]))
    print([1,3,2,8], containsDuplicate([1,3,2,8]))
    print([1,3,8,1], containsDuplicate([1,3,8,1]))

    print([1,3,1,4], containsDuplicate2([1,3,1,4]))
    print([1,3,2,8], containsDuplicate2([1,3,2,8]))
    print([1,3,8,1], containsDuplicate2([1,3,8,1]))

