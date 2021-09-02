'''
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.

Example 1:
  Input: nums = [10,2]
  Output: "210"

Example 2:
  Input: nums = [3,30,34,5,9]
  Output: "9534330"

Example 3:
  Input: nums = [1]
  Output: "1"

Example 4:
  Input: nums = [10]
  Output: "10"

'''

# build-in function
def largestNumber1(self, nums):
    if not any(nums):
        return "0"
    return "".join(sorted(map(str, nums), cmp=lambda n1, n2: -1 if n1+n2>n2+n1 else (1 if n1+n2<n2+n1 else 0)))
    
# bubble sort
def largestNumber2(self, nums):
    for i in range(len(nums), 0, -1):
        for j in range(i-1):
            if not self.compare(nums[j], nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return str(int("".join(map(str, nums))))
    
def compare(self, n1, n2):
    return str(n1) + str(n2) > str(n2) + str(n1)
    
# selection sort
def largestNumber3(self, nums):
    for i in range(len(nums), 0, -1):
        tmp = 0
        for j in range(i):
            if not self.compare(nums[j], nums[tmp]):
                tmp = j
        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
    return str(int("".join(map(str, nums))))
    
# insertion sort
def largestNumber4(self, nums):
    for i in range(len(nums)):
        pos, cur = i, nums[i]
        while pos > 0 and not self.compare(nums[pos-1], cur):
            nums[pos] = nums[pos-1]  # move one-step forward
            pos -= 1
        nums[pos] = cur
    return str(int("".join(map(str, nums))))

# merge sort        
def largestNumber5(self, nums):
    nums = self.mergeSort(nums, 0, len(nums)-1)
    return str(int("".join(map(str, nums))))
